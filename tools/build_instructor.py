"""Build the instructor pack: question bank CSV + instructor pages."""
import re, csv, glob, os
txt = open("mkdocs.yml").read()
units = [(int(n), t, int(h), w) for n, t, h, w in re.findall(r'\{n: (\d+),\s+title: "([^"]+)",\s+hours: (\d+), weeks: "([^"]+)"', txt)]
rows = []
for n, title, h, w in units:
    sec = ""; cur = None
    for line in open(f"docs/unit-{n:02d}/practice.md", encoding="utf-8").read().splitlines():
        if line.startswith("## "): sec = line[3:].strip(); continue
        m = re.match(r'\?\?\? question "(\d+)\.\s*(.*)"\s*$', line)
        if m:
            cur = {"unit": n, "no": int(m[1]), "section": sec, "q": m[2], "ans": []}; rows.append(cur); continue
        if cur is not None and (line.startswith("    ") or not line.strip()): cur["ans"].append(line.strip())
        elif cur is not None and line.strip(): cur = None
for r in rows:
    mk = re.search(r"\((\d+) marks?\)", r["q"]); r["marks"] = int(mk[1]) if mk else (1 if "choice" in r["section"].lower() else 0)
    r["q"] = re.sub(r"\s*\(\d+ marks?\)", "", r["q"])
    r["type"] = "MCQ" if "choice" in r["section"].lower() else ("Numerical" if re.search(r"calculate|compute|find|numerical|how many|how much", r["q"], re.I) else "Theory")
    r["difficulty"] = "Easy" if r["marks"] <= 2 else ("Medium" if r["marks"] <= 5 else "Hard")
    r["ans"] = " ".join(a for a in r["ans"] if a).strip()
with open("docs/downloads/question-bank.csv", "w", newline="", encoding="utf-8-sig") as f:
    wr = csv.writer(f); wr.writerow(["unit", "no", "section", "type", "marks", "difficulty", "question", "model_answer"])
    for r in rows: wr.writerow([r["unit"], r["no"], r["section"], r["type"], r["marks"], r["difficulty"], r["q"], r["ans"]])
print(len(rows), "questions")
from collections import Counter
cnt = Counter((r["unit"], r["difficulty"]) for r in rows)
# --- week plan
wk = ["# Week-by-week teaching plan", "", "A 15-week plan matching the unit hours. Adjust to your calendar; the **buffer** lines are where revision, quizzes or holidays usually fall.", "",
      "| Week | Unit | Teach | Class activity | Assess |", "|---|---|---|---|---|"]
act = {1: "Discuss everyday multimedia products; classify media", 2: "Sampling simulator; record and inspect a waveform", 3: "Dithering demo; compare image formats", 4: "Colour conversion exercise (RGB to YUV)", 5: "Huffman and DCT simulators; hand-build a code", 6: "CD block calculation relay", 7: "Scheduler simulator: EDF vs RM", 8: "Leaky-bucket simulator; draw the layer stack", 9: "Mark up a small SGML document", 10: "Skew and drift worked examples", 11: "Compare toolkit vs library with examples", 12: "Storyboard a small application"}
asg = {2: "Assignment 1 set", 5: "Quiz 1 (units 1–4)", 7: "Assignment 1 due", 9: "Assignment 2 set", 11: "Quiz 2 (units 5–8)", 13: "Assignment 2 due", 15: "Mock exam, revision"}
for n, title, h, w in units:
    first = w.replace("–", "-").split("-")[0]
    wk.append(f"| {w} | {n} | [{title}](../unit-{n:02d}/index.md) ({h} h) | {act[n]} | {asg.get(int(first), '')} |")
wk += ["", "## Per-session pattern (about 50 minutes)", "", "1. **5 min**: retrieval question from the previous session.", "2. **25 min**: teach from the class slides; stop at each *Check yourself* slide.", "3. **10 min**: one simulator or worked numerical, done live.", "4. **10 min**: students attempt two practice questions on paper; reveal and mark.", "", "## Revision weeks", "", "Use [Mock Exam 1](../revision/mock-exam-1.md) as a timed class test and give [Mock Exam 2](../revision/mock-exam-2.md) as homework. Hand out the [cheat sheets](../revision/cheat-sheets.md).", ""]
open("docs/instructor/week-plan.md", "w").write("\n".join(wk))
# --- assignments
A = """# Assignments and rubrics

Two assignments of 10 marks each. Marks are suggestions; scale them to your internal assessment.

## Assignment 1: Digital media measurement (units 2–4)

**Task.** Choose any short audio clip (10–30 s) and any photograph. For each, report:

1. Sampling rate, bit depth, channels, duration and the **uncompressed size** you calculate by formula; compare with the real file size and state the compression ratio.
2. For the image: width, height, colour depth, uncompressed size; convert to a lower bit depth and discuss the visual change (dithering).
3. Use the [sampling simulator](../labs/simulators.md) to show aliasing for a tone of your choice and explain it in 100 words.

| Criterion | Marks | Full marks look like |
|---|---|---|
| Correct formulas and units | 3 | Every calculation shows formula, substitution, result and unit |
| Comparison with real files | 2 | Ratio computed and explained (codec, lossy or lossless) |
| Aliasing explanation | 2 | Nyquist stated, example frequency worked out |
| Evidence (screenshots) | 1 | Tools and settings visible |
| Presentation | 2 | Clear structure, references, no copied text |

## Assignment 2: Compression and real-time design (units 5, 7, 10)

**Task.**

1. Choose a 40-character message with repeated letters. Build its Huffman tree by hand, give the codes, the encoded length and the compression ratio. Verify with the [Huffman simulator](../labs/simulators.md).
2. Create a set of three periodic tasks (C, P) with U between 0.78 and 1. Test with EDF and RM, draw both timelines over the hyperperiod, and verify with the [scheduler simulator](../labs/simulators.md).
3. A sender clock is 0.05 % fast. Compute the drift after 20 minutes and say what a player must do to stay within ±80 ms lip sync.

| Criterion | Marks | Full marks look like |
|---|---|---|
| Huffman tree and codes | 3 | Correct merges, prefix property noted, total bits right |
| Schedulability analysis | 3 | U, bound, timeline; notes that the RM bound is sufficient, not necessary |
| Drift calculation | 2 | 0.0005 × 1200 = 0.6 s; remedy named |
| Verification and reflection | 2 | Simulator evidence and one paragraph of lessons |

## Quick marking guide

- Award **method marks** even when the final number is wrong.
- Penalise a missing unit once, not on every line.
- Check originality: figures and code must be the student's own or credited.
"""
open("docs/instructor/assignments.md", "w").write(A)
# --- question bank page
tot = Counter(r["unit"] for r in rows); QB = ["# Question bank", "", "A tagged bank of every practice question in the course, ready for Excel or Google Sheets. Columns: unit, question number, section, type (MCQ, Numerical, Theory), marks, difficulty (from marks: ≤2 Easy, 3–5 Medium, ≥6 Hard), question, model answer.", "",
      '<p><a class="btn-s primary" href="../../downloads/question-bank.csv" download>Download question-bank.csv</a></p>', "", "| Unit | Questions | Easy | Medium | Hard |", "|---|---|---|---|---|"]
for n, t, h, w in units:
    QB.append(f"| {n}. {t} | {tot[n]} | {cnt[(n,'Easy')]} | {cnt[(n,'Medium')]} | {cnt[(n,'Hard')]} |")
QB += ["", f"**Total: {len(rows)} questions.**", "", "## Building a paper", "", "A balanced 60-mark paper: 10 MCQs (all units) + 6 medium theory questions + 2 hard questions with one numerical. The two [mock exams](../revision/mock-exam-1.md) follow this pattern.", ""]
open("docs/instructor/question-bank.md", "w").write("\n".join(QB))
open("docs/instructor/index.md", "w").write("""# Instructor pack

Resources for teaching this course. Students can read them too, but they are written for the lecturer.

<div class="grid cards" markdown>

- **[Week-by-week plan](week-plan.md)**: 15 weeks, activities and assessments.
- **[Assignments and rubrics](assignments.md)**: two ready-to-set assignments with marking criteria.
- **[Question bank](question-bank.md)**: tagged CSV of all practice questions.
- **[Mock exams](../revision/mock-exam-1.md)**: two timed 60-mark papers with marking schemes.
- **[Simulators](../labs/simulators.md)**: live demos for class.
- **Speaker notes**: open any class deck and press **S** for presenter view.

</div>
""")
