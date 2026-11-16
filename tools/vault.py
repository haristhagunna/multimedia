"""Encrypt the built site so only people with the student or admin password can read it.

Run after `mkdocs build`:   STUDENT_PASSWORD=... ADMIN_PASSWORD=... python tools/vault.py

Every page (except the home page and About) is encrypted with its own random key. That key is
wrapped twice: with the admin key (always) and with the student key (only when the page is
released in release.yml). Locked pages are therefore unreadable to students, even in the
published files. Copyright (c) 2026 Er. Harish Thagunna. All rights reserved.
"""
import base64, hashlib, html, json, os, re, sys
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
from hooks.site import is_open, _release  # noqa: E402

SITE = os.path.join(ROOT, "site")
ITER = 300_000
b64 = lambda b: base64.b64encode(b).decode()


def salt(role): return hashlib.sha256(("mm-vault-v1|" + role).encode()).digest()[:16]


def kek(password, role):
    return PBKDF2HMAC(hashes.SHA256(), 32, salt(role), ITER).derive(password.encode("utf-8"))


def seal(key, data):
    iv = os.urandom(12)
    return {"iv": b64(iv), "ct": b64(AESGCM(key).encrypt(iv, data, None))}


def package(data, key_s, key_a, student_ok):
    dek = os.urandom(32)
    out = seal(dek, data)
    out["wa"] = seal(key_a, dek)
    out["ws"] = seal(key_s, dek) if student_ok else None
    return out


def main():
    sp, ap = os.environ.get("STUDENT_PASSWORD", ""), os.environ.get("ADMIN_PASSWORD", "")
    if len(sp) < 8 or len(ap) < 8 or sp == ap:
        sys.exit("vault: set STUDENT_PASSWORD and ADMIN_PASSWORD (different, at least 8 characters).")
    key_s, key_a = kek(sp, "student"), kek(ap, "admin")
    always, unlocked = _release()
    pages, encrypted = [], set()

    sections = ("labs", "revision", "instructor")
    for root, dirs, files in os.walk(SITE):
        rel_root = os.path.relpath(root, SITE).replace(os.sep, "/")
        if rel_root.split("/")[0] in ("assets", "search", "javascripts", "stylesheets", "decks"):
            continue
        if "index.html" not in files:
            continue
        if rel_root == ".":
            key = "index"
        elif re.match(r"^unit-\d\d$", rel_root) or rel_root in sections:
            key = rel_root + "/index"
        else:
            key = rel_root
        path = os.path.join(root, "index.html")
        text = open(path, encoding="utf-8").read()
        m = re.search(r'(<article class="md-content__inner md-typeset">)(.*)(</article>)', text, flags=re.S)
        if not m:
            continue
        title_m = re.search(r"<h1[^>]*>(.*?)</h1>", m.group(2), flags=re.S)
        title = html.unescape(re.sub(r"<[^>]+>", "", title_m.group(1))).replace("\u00b6", "").strip() if title_m else key
        short = key
        public = key in always
        released = is_open(key, always, unlocked) and key != "admin"
        pages.append({"key": key, "title": title, "released": bool(released)})
        if public:
            continue
        pkg = package(m.group(2).encode("utf-8"), key_s, key_a, released)
        gate = ('<div class="vault-gate" data-key="%s" data-vault="%s"><h1>%s</h1>'
                '<p class="vault-msg">This page is protected. Sign in to read it.</p>'
                '<noscript><p>JavaScript is required to unlock this page.</p></noscript></div>'
                % (html.escape(short), html.escape(json.dumps(pkg, separators=(",", ":"))), html.escape(title)))
        text = text[:m.start(2)] + gate + text[m.end(2):]
        text = re.sub(r'(<nav class="md-nav md-nav--secondary"[^>]*>).*?(</nav>)', r"\1\2", text, count=1, flags=re.S)
        open(path, "w", encoding="utf-8").write(text)
        encrypted.add(key)

    # ---- files (downloads, lab code, syllabus scans) ----
    fmap = {"labs/code/sampling.py": "labs/lab-sampling", "labs/code/huffman.py": "labs/lab-huffman",
            "labs/code/scheduler.py": "labs/lab-scheduler", "labs/code/dct.py": "labs/lab-dct",
            "labs/code/sync.py": "labs/lab-sync", "downloads/cheat-sheets.pdf": "revision/cheat-sheets",
            "downloads/question-bank.csv": "instructor", "assets/syllabus-page-1.jpg": "syllabus",
            "assets/syllabus-page-2.jpg": "syllabus"}
    types = {".py": "text/x-python", ".pdf": "application/pdf", ".csv": "text/csv", ".jpg": "image/jpeg"}
    fl = []
    for rel, page in fmap.items():
        p = os.path.join(SITE, rel)
        if not os.path.exists(p):
            continue
        pkg = package(open(p, "rb").read(), key_s, key_a, is_open(page, always, unlocked))
        pkg["type"] = types[os.path.splitext(rel)[1]]
        open(p + ".enc", "w").write(json.dumps(pkg, separators=(",", ":")))
        os.remove(p)
        fl.append(rel)

    # ---- decks: encrypted shell that decrypts itself in the browser ----
    shell = open(os.path.join(ROOT, "tools", "deck_shell.html"), encoding="utf-8").read()
    ddir = os.path.join(SITE, "decks")
    if os.path.isdir(ddir):
        for f in sorted(os.listdir(ddir)):
            if not f.endswith(".html"):
                continue
            mu = re.match(r"unit-(\d\d)\.html$", f)
            page = "unit-%s/slides" % mu.group(1) if mu else "class-01"
            p = os.path.join(ddir, f)
            pkg = package(open(p, "rb").read(), key_s, key_a, is_open(page, always, unlocked))
            open(p, "w", encoding="utf-8").write(shell.replace("@@VAULT@@", html.escape(json.dumps(pkg, separators=(",", ":")))))

    # ---- search index: keep page titles only ----
    sp_path = os.path.join(SITE, "search", "search_index.json")
    if os.path.exists(sp_path):
        idx = json.load(open(sp_path, encoding="utf-8"))
        keep = []
        for d in idx["docs"]:
            loc = d["location"]
            if "#" in loc:
                continue
            d["text"] = ""
            keep.append(d)
        idx["docs"] = keep
        json.dump(idx, open(sp_path, "w", encoding="utf-8"), separators=(",", ":"))

    manifest = {"v": 1, "iter": ITER, "saltS": b64(salt("student")), "saltA": b64(salt("admin")),
                "checkS": seal(key_s, b"mm-vault-ok"), "checkA": seal(key_a, b"mm-vault-ok"),
                "files": fl, "pages": pages}
    json.dump(manifest, open(os.path.join(SITE, "vault.json"), "w"), separators=(",", ":"))
    # drop unencrypted leftovers that leak content
    for leak in ("sitemap.xml.gz",):
        p = os.path.join(SITE, leak)
        if os.path.exists(p):
            os.remove(p)
    print("vault: encrypted %d pages, %d files, %d decks" % (len(encrypted), len(fl), len(os.listdir(ddir)) if os.path.isdir(ddir) else 0))


if __name__ == "__main__":
    main()
