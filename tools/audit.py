"""Content audit: syllabus coverage + recomputation of the key figures quoted in the notes.
Copyright (c) 2026 Er. Harish Thagunna. All rights reserved.
Usage: python tools/audit.py   (writes docs/coverage.md, prints check results)"""
import os, re, math
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); D = os.path.join(R, "docs")
syl = open(os.path.join(D, "syllabus.md"), encoding="utf-8").read()
units = {}
cur = None
for line in syl.split("\n"):
    m = re.match(r"### Unit (\d+): (.*?) \[(\d+) hrs\]", line)
    if m: cur = int(m.group(1)); units[cur] = {"title": m.group(2), "hrs": int(m.group(3)), "items": []}; continue
    if cur and re.match(r"- \d+\.\d+", line): units[cur]["items"].append(line[2:].strip())
rows = []; missing = []
for n, u in units.items():
    idx = open(os.path.join(D, f"unit-{n:02d}", "index.md"), encoding="utf-8").read()
    cov = []
    for l in idx.split("\n"):
        if l.startswith("|") and re.match(r"\|\s*\d+\.\d+", l):
            cells = [c.strip() for c in l.strip().strip("|").split("|")]
            cov.append(cells)
    for it in u["items"]:
        num = re.match(r"(\d+\.\d+)", it).group(1)
        hit = [c for c in cov if c[0].startswith(num) or num in c[0]]
        if not hit: missing.append((n, it))
        rows.append((n, it, hit[0][1] if hit else "-"))
print("syllabus items:", len(rows), "unmapped:", missing)
def fixlinks(cell, n): return re.sub(r"\]\(([^)#]+\.md)", lambda m: f"](unit-{n:02d}/{m.group(1)}", cell)
out = ["# Syllabus coverage", "", "Every item of the syllabus and the page where it is covered. Use it to check that nothing in the course is missed.", "",
       "| Unit | Syllabus item | Where to study it |", "|---|---|---|"]
for n, it, pg in rows: out.append(f"| {n} | {it} | {fixlinks(pg, n)} |")
out += ["", f"**{len(rows)} syllabus items, all mapped.**" if not missing else f"**Unmapped: {missing}**", ""]
# numbers
chk = []
def eq(name, a, b, tol=1e-9): chk.append((name, abs(a - b) <= tol, a, b))
eq("CD-DA bit rate", 44100 * 16 * 2, 1411200); eq("CD block bytes", 1411200 / 75 / 8, 2352)
eq("74 min blocks", 74 * 60 * 75, 333000); eq("CD-DA capacity MiB", 333000 * 2352 / 2 ** 20, 746.9, .05)
eq("Mode1 capacity MiB", 333000 * 2048 / 2 ** 20, 650.4, .05)
eq("640x480x3x25x60", 640 * 480 * 3 * 25 * 60, 1382400000); eq("CIF 25fps Mbit/s", 352 * 288 * 3 * 25 * 8 / 1e6, 60.8256)
eq("RM bound n=2", 2 * (2 ** .5 - 1), .8284, 1e-4); eq("RM bound n=3", 3 * (2 ** (1 / 3) - 1), .7798, 1e-4)
eq("U example", 2 / 5 + 4 / 7, .9714, 1e-4); eq("Huffman bits", 6 * 1 + 5 * 2 + 1 * 3 + 3 * 3, 28)
eq("image 640x480x8 bytes", 640 * 480, 307200); eq("38.4 s at 64k", 307200 * 8 / 64000, 38.4)
eq("Y white", .30 + .59 + .11, 1.0); eq("40 ms at 25 fps", 1000 / 25, 40)
ok = all(c[1] for c in chk); print("numeric checks:", "ALL OK" if ok else [c for c in chk if not c[1]], len(chk))
open(os.path.join(D, "coverage.md"), "w", encoding="utf-8").write("\n".join(out))
