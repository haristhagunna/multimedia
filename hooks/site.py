"""Build hooks: site statistics, reading time and progress-tracking slots.

Copyright (c) 2026 Er. Harish Thagunna. All rights reserved.
"""
import os
import re
import shutil

try:
    import yaml
except ImportError:  # pragma: no cover
    yaml = None

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def _release():
    path = os.path.join(ROOT, "release.yml")
    data = {}
    if yaml and os.path.exists(path):
        data = yaml.safe_load(open(path, encoding="utf-8")) or {}
    norm = lambda xs: [str(x).strip().strip("/").removesuffix(".md") for x in (xs or [])]
    return norm(data.get("always_open")), norm(data.get("unlocked"))


def _match(key, entries):
    return any(key == e or key.startswith(e + "/") for e in entries)


def is_open(key, always, unlocked):
    """key is a page path without .md, e.g. 'unit-05/slides'."""
    if key in ("404",) or _match(key, always):
        return True
    if _match(key, unlocked):
        return True
    m = re.match(r"^(unit-\d\d)/index$", key)
    if m and any(e == m.group(1) or e.startswith(m.group(1) + "/") for e in unlocked):
        return True
    return False


def _url(key):
    if key == "index":
        return ""
    return key[:-6] + "/" if key.endswith("/index") else key + "/"


UNIT_RE = re.compile(r"^unit-(\d\d)/(.+)\.md$")


def _words(text):
    text = re.sub(r"```.*?```", " ", text, flags=re.S)
    text = re.sub(r"<[^>]+>", " ", text)
    return len(re.findall(r"[A-Za-z0-9][A-Za-z0-9'’\-\.]*", text))


def on_config(config):
    docs = config["docs_dir"]
    stats = {"questions": 0, "notes": 0, "decks": 0, "words": 0, "units": 0}
    pages = {}
    for root, _, files in os.walk(docs):
        for f in files:
            if not f.endswith(".md"):
                continue
            rel = os.path.relpath(os.path.join(root, f), docs).replace(os.sep, "/")
            text = open(os.path.join(root, f), encoding="utf-8").read()
            stats["words"] += _words(text)
            m = UNIT_RE.match(rel)
            if not m:
                continue
            n, name = int(m.group(1)), m.group(2)
            stats["questions"] += len(re.findall(r"^\?\?\? question", text, flags=re.M))
            if name == "slides":
                stats["decks"] += 1
            elif name != "index":
                pages[n] = pages.get(n, 0) + 1
                if name != "practice":
                    stats["notes"] += 1
    stats["units"] = len(config["extra"].get("units", []))
    stats["practice_questions"] = stats.pop("questions")
    stats["hours"] = sum(u["hours"] for u in config["extra"]["units"])
    for u in config["extra"]["units"]:
        u["pages"] = pages.get(u["n"], 0)
    config["extra"]["stats"] = stats
    always, unlocked = _release()
    locked_urls = []
    for root, _, files in os.walk(docs):
        for f in files:
            if f.endswith(".md") and "includes" not in root:
                key = os.path.relpath(os.path.join(root, f), docs).replace(os.sep, "/")[:-3]
                if not is_open(key, always, unlocked):
                    locked_urls.append(_url(key))
    config["extra"]["locked_urls"] = sorted(locked_urls)
    for u in config["extra"]["units"]:
        k = "unit-%02d" % u["n"]
        full = _match(k, unlocked)
        part = any(e.startswith(k + "/") for e in unlocked)
        u["state"] = "open" if full else ("partial" if part else "locked")
        u["slides_open"] = is_open(k + "/slides", always, unlocked)
        u["practice_open"] = is_open(k + "/practice", always, unlocked)
    config["extra"]["released_units"] = sum(1 for u in config["extra"]["units"] if u["state"] != "locked")
    return config


def on_page_markdown(markdown, page, config, files):
    src = page.file.src_uri
    m = UNIT_RE.match(src)
    if not m:
        return markdown
    n, name = int(m.group(1)), m.group(2)
    lines = markdown.split("\n")
    if not lines or not lines[0].startswith("# "):
        return markdown
    if name == "slides":
        return markdown
    if name == "index":
        total = next((u["pages"] for u in config["extra"]["units"] if u["n"] == n), 0)
        slot = f'<div class="unit-progress" data-unit="{n}" data-total="{total}"></div>'
        meta = ""
    else:
        words = _words(markdown)
        minutes = max(1, round(words / 200))
        kind = "Practice" if name == "practice" else "Notes"
        meta = (f'<p class="page-meta"><span>Unit {n}</span><span>{kind}</span>'
                f'<span>{minutes} min read</span></p>')
        slot = f'<div class="track-slot" data-unit="{n}" data-page="{name}"></div>'
    lines.insert(1, "\n" + meta + "\n" + slot + "\n")
    return "\n".join(lines)
