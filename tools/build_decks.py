"""Generate reveal.js class decks from the topic notes.
Copyright (c) 2026 Er. Harish Thagunna. All rights reserved.
Usage: python tools/build_decks.py [unit numbers...]
"""
import hashlib, html, os, re, subprocess, sys
import yaml, markdown

class _L(yaml.SafeLoader): pass
_L.add_multi_constructor("tag:yaml.org,2002:python/", lambda l, s, n: None)
def yload(path): return yaml.load(open(path).read(), Loader=_L)

from bs4 import BeautifulSoup, NavigableString, Tag

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCS = os.path.join(ROOT, "docs")
CACHE = os.path.join(ROOT, "tools", ".mmcache")
os.makedirs(CACHE, exist_ok=True)
TEMPLATE = open(os.path.join(ROOT, "tools", "deck_template.html")).read()
try:
    from visuals import VIS, SRC
    from enrich import E as ENRICH
except Exception:
    sys.path.insert(0, os.path.join(ROOT, "tools"))
    try:
        from visuals import VIS, SRC
        from enrich import E as ENRICH
    except Exception as e:
        print("no visuals:", e); VIS = {}; SRC = {}; ENRICH = {}

EXT = ["admonition", "attr_list", "def_list", "tables", "md_in_html", "pymdownx.details",
       "pymdownx.arithmatex", "pymdownx.superfences", "pymdownx.mark", "pymdownx.caret", "pymdownx.tilde",
       "pymdownx.tasklist", "pymdownx.keys", "footnotes"]
EXTCFG = {"pymdownx.arithmatex": {"generic": True}}
BUDGET = 14.0

def prerender_math(h):
    """Render arithmatex spans with KaTeX at build time (no browser plugin needed)."""
    import json
    pat = re.compile(r'<(span|div) class="arithmatex">(\\\(|\\\[)(.*?)(\\\)|\\\])</\1>', re.S)
    items = [(m.group(0), m.group(3), m.group(2) == "\\[") for m in pat.finditer(h)]
    if not items: return h
    env = dict(os.environ, KATEX_PATH="/opt/npm-tools/node_modules/katex")
    try:
        r = subprocess.run(["node", os.path.join(ROOT, "tools", "katex_render.js")], input=json.dumps([{"tex": html.unescape(t), "display": d} for _, t, d in items]), capture_output=True, text=True, env=env, timeout=60)
        out = json.loads(r.stdout)
    except Exception as e:
        print("katex failed", e); return h
    for (orig, _, d), rendered in zip(items, out):
        h = h.replace(orig, f'<span class="mathx{" blk" if d else ""}">{rendered}</span>', 1)
    return h

def md2html(text):
    return markdown.markdown(text, extensions=EXT, extension_configs=EXTCFG, output_format="html")

# ---------- mermaid ----------
def render_mermaid(code):
    h = hashlib.sha1(code.encode()).hexdigest()[:12]
    out = os.path.join(CACHE, h + ".svg")
    if not os.path.exists(out):
        src = os.path.join(CACHE, h + ".mmd"); open(src, "w").write(code)
        pj = os.path.join(CACHE, "p.json"); open(pj, "w").write('{"args":["--no-sandbox","--disable-setuid-sandbox"]}')
        r = subprocess.run(["mmdc", "-i", src, "-o", out, "-t", "dark", "-b", "transparent", "-c",
                            os.path.join(ROOT, "tools", "mmconfig.json"), "-p", pj], capture_output=True, text=True)
        if not os.path.exists(out):
            print("mermaid fail", r.stderr[:300]); return "<p>[diagram]</p>"
    svg = open(out).read()
    svg = re.sub(r"^<\?xml.*?\?>", "", svg).strip()
    svg = svg.replace("my-svg", "mm" + h)
    svg = re.sub(r'style="max-width:[^"]*"', "", svg, count=1)
    return svg

def extract_mermaid(md):
    store = {}
    def rep(m):
        k = "MMTOKEN%dX" % len(store); store[k] = m.group(2)
        return "\n\n" + m.group(1) + k + "\n\n"
    md = re.sub(r"^(\s*)```mermaid\n(.*?)\n\s*```", lambda m: rep(re.match(r"(\s*)```mermaid\n(.*)", m.group(0), re.S) and type("M", (), {"group": lambda s, i: [None, m.group(1), m.group(2)][i]})()), md, flags=re.S | re.M)
    return md, store

# ---------- helpers ----------
def txt(el): return re.sub(r"\s+", " ", el.get_text(" ", strip=True))
def inner(el): return "".join(str(c) for c in el.children)

def split_sentences(h):
    parts = re.split(r"(?<=[.!?])\s+(?=[A-Z<(*])", h.strip())
    return [p for p in parts if p]

def weight(el):
    n = el.name
    cl = el.get("class") or []
    if "chk" in cl: return len(txt(el)) / 52 + 3.2 + len(el.find_all("li")) * .3
    if n == "div" and "callout" in cl and el.find("svg"): return 9.5
    if n == "p":
        if el.find("svg") or "MMTOKEN" in el.get_text(): return 9
        return len(txt(el)) / 70 + .5
    if n in ("ul", "ol"):
        return sum(len(txt(li)) / 62 + .35 for li in el.find_all("li", recursive=False)) + .3
    if n == "table": return len(el.find_all("tr")) * 1.05 + .8 + sum(len(txt(td)) > 60 for td in el.find_all("td")) * .6
    if n == "div" and "callout" in (el.get("class") or []): return len(txt(el)) / 62 + 1.8
    if n == "div" and "diagram" in (el.get("class") or []): return 9.5
    if n == "pre": return el.get_text().count("\n") * .62 + 1.3
    if n in ("h3", "h4"): return 1.3
    if n == "dl": return len(txt(el)) / 62 + 1
    return len(txt(el)) / 70 + .8

def callout(kind, title, body_html):
    cls = {"exam": "exam", "warning": "warn", "danger": "warn", "failure": "warn", "bug": "warn", "tip": "tip", "success": "tip",
           "hint": "tip", "example": "ex"}.get(kind, "")
    lab = {"exam": "Exam focus", "warning": "Watch out", "danger": "Watch out", "tip": "Tip", "example": "Example",
           "note": "Note", "info": "Note", "abstract": "Summary", "quote": "Quote", "success": "Remember"}.get(kind, "Note")
    if title and title.lower() not in (kind, lab.lower()): lab = title
    return f'<div class="callout {cls}"><div class="ct">{lab}</div>{body_html}</div>'

def convert_blocks(soup, store):
    """Return list of block Tags (top-level) ready for packing; transforms admonitions/details/mermaid."""
    blocks = []
    for el in list(soup.children):
        if isinstance(el, NavigableString):
            if el.strip():
                blocks.append(BeautifulSoup(f"<p>{el}</p>", "html.parser").p)
            continue
        cls = el.get("class") or []
        if el.name == "p" and "MMTOKEN" in el.get_text():
            k = re.search(r"MMTOKEN\d+X", el.get_text()).group(0)
            blocks.append(BeautifulSoup(f'<div class="diagram">{render_mermaid(store[k])}</div>', "html.parser").div)
            continue
        if el.name == "div" and "admonition" in cls:
            kind = [c for c in cls if c != "admonition"][0] if len(cls) > 1 else "note"
            if kind == "source": continue
            t = el.find("p", class_="admonition-title"); title = txt(t) if t else ""
            if t: t.extract()
            inner_soup = BeautifulSoup(inner(el), "html.parser")
            # mermaid inside admonition
            for p in inner_soup.find_all("p"):
                if "MMTOKEN" in p.get_text():
                    k = re.search(r"MMTOKEN\d+X", p.get_text()).group(0)
                    p.replace_with(BeautifulSoup(f'<div class="diagram">{render_mermaid(store[k])}</div>', "html.parser"))
            diag = inner_soup.find("div", class_="diagram")
            if diag:
                diag.extract()
                c = BeautifulSoup(callout(kind, title, ""), "html.parser").div
                sp = BeautifulSoup(f'<div class="sp"><div class="txt">{str(inner_soup)}</div></div>', "html.parser").div
                sp.append(diag); c.append(sp); c["class"] = c["class"] + ["split"] + (["long"] if len(txt(sp)) > 380 else [])
                blocks.append(c)
            else:
                blocks.append(BeautifulSoup(callout(kind, title, str(inner_soup)), "html.parser").div)
            continue
        if el.name == "details":
            s = el.find("summary"); q = inner(s) if s else ""
            if s: s.extract()
            blocks.append(BeautifulSoup(f'<div class="chk"><div class="lab">Check yourself</div><p class="q">{q}</p>'
                                        f'<div class="fragment ans">{inner(el)}</div></div>', "html.parser").div)
            continue
        blocks.append(el)
    return blocks

def shrink(el):
    """Long paragraphs -> bullets."""
    if el.name == "p" and len(txt(el)) > 260 and not el.find("svg"):
        ss = split_sentences(inner(el))
        if len(ss) >= 3:
            ul = BeautifulSoup("<ul></ul>", "html.parser").ul
            for s in ss: ul.append(BeautifulSoup(f"<li>{s}</li>", "html.parser").li)
            return ul
    return el

def split_big(el):
    """Split an oversize list/table into pieces."""
    w = weight(el)
    if w <= BUDGET: return [el]
    out = []
    if el.name in ("ul", "ol"):
        lis = el.find_all("li", recursive=False); cur = []; cw = 0
        start = int(el.get("start", 1)) if el.name == "ol" else 1; idx = start
        for li in lis:
            lw = len(txt(li)) / 62 + .35
            if cur and cw + lw > BUDGET - 1.5:
                out.append((cur, idx)); idx += len(cur); cur = []; cw = 0
            cur.append(li); cw += lw
        if cur: out.append((cur, idx))
        res = []
        for items, st in out:
            new = BeautifulSoup(f"<{el.name}></{el.name}>", "html.parser").find(el.name)
            if el.name == "ol": new["start"] = st
            for li in items: new.append(BeautifulSoup(str(li), "html.parser").li)
            res.append(new)
        return res
    if el.name == "table":
        rows = el.find_all("tr"); head = rows[0]; body = rows[1:]
        per = 7; res = []
        for i in range(0, len(body), per):
            t = BeautifulSoup("<table></table>", "html.parser").table
            t.append(BeautifulSoup(str(head), "html.parser").tr)
            for r in body[i:i + per]: t.append(BeautifulSoup(str(r), "html.parser").tr)
            res.append(t)
        return res
    return [el]

def pack(blocks):
    """Pack blocks into slides by weight."""
    pre = []
    for b in blocks:
        b = shrink(b)
        pre.extend(split_big(b))
    slides = []; cur = []; cw = 0
    for b in pre:
        w = weight(b)
        if cur and cw + w > BUDGET:
            slides.append(cur); cur = []; cw = 0
        cur.append(b); cw += w
    if cur: slides.append(cur)
    return slides, [sum(weight(b) for b in s) for s in slides]

def frag_lists(blocks):
    for b in blocks:
        if b.name in ("ul", "ol"):
            lis = b.find_all("li", recursive=False)
            if 3 <= len(lis) <= 7:
                for li in lis:
                    li["class"] = (li.get("class") or []) + ["fragment", "fade-up"]

def slide_html(title, sub, blocks, w, notes=""):
    frag_lists(blocks)
    cls = "xdense" if w > 13.2 else ("dense" if w > 11 else "")
    body = "".join(str(b) for b in blocks)
    # two-column layout when a slide is exactly a short list + table/diagram? keep simple
    h = f'<h2>{"<small>" + sub + "</small>" if sub else ""}{title}</h2>' if title else ""
    n = f'<aside class="notes">{notes}</aside>' if notes else ""
    return f'<section class="{cls}">{h}{body}{n}</section>'

# ---------- page -> slides ----------
def page_slides(path, topic_url, topic_title):
    md = open(path, encoding="utf-8").read()
    md = re.sub(r"^# .*\n", "", md, count=1)
    # drop snippets / tabs unsupported
    md, store = extract_mermaid_simple(md)
    soup = BeautifulSoup(md2html(md), "html.parser")
    blocks = convert_blocks(soup, store)
    groups = []; cur = {"h2": None, "h3": None, "blocks": []}
    for b in blocks:
        if b.name == "h2":
            if cur["blocks"] or cur["h2"]: groups.append(cur)
            cur = {"h2": inner(b), "h3": None, "blocks": []}
        elif b.name == "h3":
            if cur["blocks"]: groups.append(cur)
            cur = {"h2": cur["h2"], "h3": inner(b), "blocks": []}
        else:
            cur["blocks"].append(b)
    if cur["blocks"] or cur["h2"]: groups.append(cur)
    items = []
    for g in groups:
        if not g["blocks"]: continue
        title = g["h3"] or g["h2"] or topic_title
        sub = (g["h2"] if g["h3"] else topic_title) or ""
        sl, ws = pack(g["blocks"])
        for i, (b, w) in enumerate(zip(sl, ws)):
            t = title + (f' <span style="opacity:.55;font-size:.6em">({i + 1}/{len(sl)})</span>' if len(sl) > 1 else "")
            items.append({"title": t, "plain": title, "sub": sub, "blocks": b, "w": w})
    # merge small neighbours so slides are well filled
    merged = []
    for it in items:
        if merged and merged[-1]["w"] < 8 and merged[-1]["w"] + it["w"] + 1.2 <= 13.5 and not any(weight(b) >= 9 for b in it["blocks"]):
            m = merged[-1]
            h3 = BeautifulSoup(f"<h3>{it['plain']}</h3>", "html.parser").h3
            m["blocks"] = m["blocks"] + [h3] + it["blocks"]; m["w"] += it["w"] + 1.2
        else:
            merged.append(it)
    out = [slide_html(m["title"], m["sub"], m["blocks"], m["w"], f'Source note: <a href="../../{topic_url}/">{topic_title}</a>') for m in merged]
    return out

def extract_mermaid_simple(md):
    store = {}
    def rep(m):
        k = "MMTOKEN%dX" % len(store)
        indent = m.group(1)
        body = "\n".join(l[len(indent):] if l.startswith(indent) else l for l in m.group(2).split("\n"))
        store[k] = body
        return f"\n{indent}{k}\n"
    md = re.sub(r"^([ \t]*)```mermaid\n(.*?)\n[ \t]*```", rep, md, flags=re.S | re.M)
    return md, store

# ---------- quiz ----------
def quiz_slides(unit_dir, n):
    p = os.path.join(unit_dir, "practice.md")
    if not os.path.exists(p): return []
    soup = BeautifulSoup(md2html(re.sub(r"^# .*\n", "", open(p, encoding="utf-8").read(), count=1)), "html.parser")
    mc = []
    for d in soup.find_all("details"):
        s = d.find("summary"); ul = d.find("ul"); ans = d.find("p")
        if not (s and ul and ans): continue
        lis = ul.find_all("li", recursive=False)
        if len(lis) < 3 or not all(re.match(r"[A-E]\.\s", txt(li)) for li in lis): continue
        a = [p for p in d.find_all("p") if re.match(r"Answer", txt(p))]
        if not a: continue
        mc.append((inner(s), lis, a[0]))
    if not mc: return []
    step = max(1, len(mc) // 6); pick = mc[::step][:6]
    out = []
    for i, (q, lis, a) in enumerate(pick):
        opts = "".join(f"<li>{inner(li)}</li>" for li in lis)
        out.append(f'<section><h2><small>Quick check {i + 1} / {len(pick)}</small>{re.sub(r"^\\d+\\.\\s*", "", q)}</h2><ul class="opts">{opts}</ul><div class="fragment ans">{inner(a)}</div></section>')
    return out

def exam_recap(blocks_all):
    items = []
    for sl in blocks_all:
        for m in re.finditer(r'<div class="callout exam">.*?</div>(?=\s*(<|$))', sl, flags=re.S):
            items.append(m.group(0))
    return items

# ---------- unit ----------
def load_nav():
    cfg = yload(os.path.join(ROOT, "mkdocs.yml"))
    return cfg

def unit_deck(n, cfgunits):
    u = [x for x in cfgunits if x["n"] == n][0]
    d = os.path.join(DOCS, f"unit-{n:02d}")
    # topic order from nav
    nav = yload(os.path.join(ROOT, "mkdocs.yml"))["nav"]
    topics = []
    def walk(x):
        if isinstance(x, list):
            for i in x: walk(i)
        elif isinstance(x, dict):
            for k, v in x.items():
                if isinstance(v, str) and v.startswith(f"unit-{n:02d}/"): topics.append((k, v))
                else: walk(v)
    walk(nav)
    topics = [(k, v) for k, v in topics if not re.search(r"(index|slides|practice)\.md$", v)]
    title = u["title"]
    sections = []
    # title slide
    stats_topics = len(topics)
    sections.append(f'<section class="title-slide"><div class="kick">Multimedia and Application &middot; BCA429CO</div><h1>Unit {n}<br>{title}</h1>'
                    f'<p style="max-width:75%;color:#aab0d6">{u.get("blurb","")}</p>'
                    f'<div class="chips"><span>{u["hours"]} teaching hours</span><span>{stats_topics} topics</span><span>Interactive deck</span></div>'
                    f'<div class="by">Er. Harish Thagunna</div>'
                    f'<aside class="notes">Navigate: arrows, Space. Esc for overview, S for speaker view, F fullscreen, Ctrl+Shift+F search, Alt+click zoom.</aside></section>')
    # overview/agenda from index
    ag = "".join(f'<div class="card"><span class="n">{i + 1}</span>{k}</div>' for i, (k, v) in enumerate(topics))
    idx = os.path.join(d, "index.md"); intro = ""
    if os.path.exists(idx):
        isoup = BeautifulSoup(md2html(re.sub(r"^# .*\n", "", open(idx, encoding="utf-8").read(), count=1)), "html.parser")
        isoup = BeautifulSoup(re.sub(r'<div class="unit-progress.*?</div>', "", str(isoup)), "html.parser")
        iblocks = convert_blocks(isoup, {})
        lst = next((b for b in iblocks if b.name in ("ol", "ul") and len(b.find_all("li", recursive=False)) >= 3), None)
        intro = next((b for b in iblocks if b.name == "p" and not b.find("a") and 60 < len(txt(b)) < 420 and not re.search(r"hours|weeks", txt(b))), None)
        if intro:
            sections.append(slide_html("Overview", f"Unit {n}", [intro], 3))
        if lst:
            sl, ws = pack([lst])
            for s_, w in zip(sl, ws): sections.append(slide_html("What you must master", f"Unit {n} objectives", s_, w))
    sections.append(f'<section><h2><small>Roadmap</small>What we will cover</h2><div class="agenda">{ag}</div></section>')
    all_html = []
    for ti, (k, v) in enumerate(topics):
        path = os.path.join(DOCS, v)
        url = v[:-3]
        slides = page_slides(path, url, k)
        vis = [x for x in VIS.get(n, []) if x[0] == os.path.basename(v)[:-3]]
        pre = [x for x in vis if x[1] == "start"]; post = [x for x in vis if x[1] != "start"]
        def vh(x):
            return f'<section><h2><small>{k}</small>{x[2]}</h2><div class="vis">{x[3]}</div><div class="cap">{x[4] if len(x) > 4 else ""}</div></section>'
        intro_slide = (f'<section class="sec"><div class="no">{ti + 1:02d}</div><h2>{k}</h2>'
                       f'<div class="lead">Unit {n} &middot; topic {ti + 1} of {len(topics)}</div></section>')
        en = ENRICH.get(n, {}).get(os.path.basename(v)[:-3])
        plain = terms = None
        if en:
            plain = (f'<section><h2><small>{k}</small>In plain words</h2><div class="trio">'
                     f'<div class="card c1"><div class="ct">The idea</div><p>{en["plain"]}</p></div>'
                     f'<div class="card c2"><div class="ct">Real-life picture</div><p>{en["real"]}</p></div>'
                     f'<div class="card c3"><div class="ct">Remember it</div><p>{en["hook"]}</p></div></div></section>')
            tc = "".join(f'<div class="card term"><b>{a}</b><span>{b}</span></div>' for a, b in en["terms"])
            terms = f'<section><h2><small>{k}</small>Key terms</h2><div class="terms">{tc}</div></section>'
        stack = [intro_slide] + ([plain] if plain else []) + [vh(x) for x in pre] + slides + ([terms] if terms else []) + [vh(x) for x in post]
        all_html.extend(slides)
        sections.append(f'<section data-topic="{html.escape(k)}">' + "".join(stack) + "</section>")
    # exam recap
    ex = exam_recap(all_html)
    if ex:
        chunks = []; cur = []; cw = 0
        for e in ex:
            w = len(re.sub(r"<[^>]+>", "", e)) / 62 + 2
            if cur and cw + w > 11: chunks.append(cur); cur = []; cw = 0
            cur.append(e); cw += w
        if cur: chunks.append(cur)
        rs = "".join(f'<section><h2><small>Revision</small>Exam focus recap ({i + 1}/{len(chunks)})</h2>{"".join(c)}</section>' for i, c in enumerate(chunks))
        sections.append('<section data-topic="Exam recap">' + rs + "</section>")
    refs = SRC.get(n)
    if refs:
        li = "".join(f"<li>{r}</li>" for r in refs)
        sections.append(f'<section data-topic="Sources"><section><h2><small>Go deeper</small>Sources and further reading</h2><ul class="small">{li}</ul>'
                        f'<div class="callout"><div class="ct">About the figures</div><p>Charts and diagrams in this deck were drawn for this course from standard formulas, specifications and textbook knowledge. They are original drawings, not copies of figures from any publication.</p></div></section></section>')
    q = quiz_slides(d, n)
    if q:
        sections.append('<section data-topic="Quick check"><section class="sec"><div class="no">?</div><h2>Quick check</h2><div class="lead">Try each question before revealing the answer.</div></section>' + "".join(q) + "</section>")
    sections.append(f'<section class="title-slide"><div class="kick">End of Unit {n}</div><h1>Thank you</h1>'
                    f'<p style="color:#aab0d6;max-width:70%">Revise with the topic notes, attempt the practice questions, and use the flashcards on the practice page.</p>'
                    f'<div class="by">&copy; 2026 Er. Harish Thagunna. All rights reserved.</div></section>')
    body = "\n".join(sections)
    # never force display on <section> itself (reveal.js toggles it): wrap in an inner div instead
    body = re.sub(r'<section class="(sec|title-slide)">(.*?)</section>', r'<section><div class="\1">\2</div></section>', body, flags=re.S)
    body = prerender_math(body)
    out = TEMPLATE.replace("@@N@@", str(n)).replace("@@TITLE@@", title).replace("@@SLIDES@@", body)
    open(os.path.join(DOCS, "decks", f"unit-{n:02d}.html"), "w", encoding="utf-8").write(out)
    cnt = out.count("<section")
    print(f"unit {n}: {len(topics)} topics, {cnt} sections, {len(out)//1024} KB")

if __name__ == "__main__":
    cfg = yload(os.path.join(ROOT, "mkdocs.yml"))
    units = cfg["extra"]["units"]
    which = [int(a) for a in sys.argv[1:]] or list(range(1, 13))
    for n in which: unit_deck(n, units)
