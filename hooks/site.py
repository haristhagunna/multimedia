"""Build hooks: site statistics, reading time and progress-tracking slots.

Copyright (c) 2026 Er. Harish Thagunna. All rights reserved.
"""
import os
import re

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
