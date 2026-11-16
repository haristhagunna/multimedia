"""Class 1 deck: Introduction and Syllabus Overview (uses the same template as the unit decks)."""
import os, sys, html
sys.path.insert(0, os.path.dirname(__file__))
import build_decks as B
units = B.yload(os.path.join(B.ROOT, "mkdocs.yml"))["extra"]["units"]
T = sum(u["hours"] for u in units)
S = []
def sec(no, title, lead): S.append(f'<section><div class="sec"><div class="no">{no}</div><h2>{title}</h2><div class="lead">{lead}</div></div></section>')
def slide(kicker, title, body, notes=""):
    S.append(f'<section><h2><small>{kicker}</small>{title}</h2>{body}' + (f'<aside class="notes">{notes}</aside>' if notes else "") + '</section>')
def cards(items, cls="two"):
    return f'<div class="{cls}">' + "".join(f'<div class="card"><h4 style="margin-top:0">{h}</h4><p style="font-size:.82em">{p}</p></div>' for h, p in items) + '</div>'

# 1 title
S.append('<section><div class="title-slide"><div class="kick">Class 1 &middot; Multimedia System &middot; BIT477MS</div><h1>Introduction and<br>Syllabus Overview</h1>'
         '<p style="max-width:72%;color:#aeb6d6">What this course is about, how it is organised, how you are assessed, and how to study it well.</p>'
         '<div class="chips"><span>Year IV, Semester VII</span><span>45 teaching hours</span><span>12 units</span></div>'
         '<div class="by">Er. Harish Thagunna</div>'
         '<aside class="notes">Welcome the class. Take attendance, introduce yourself, and say that today is orientation: no heavy theory, but everything you need to plan the semester. Controls: arrows, Space, Esc overview, S speaker view, F full screen.</aside></div></section>')
# 2 agenda
ag = ["About the course", "Why multimedia matters", "Syllabus at a glance", "Hours and weekly plan", "Marks and exam pattern", "Laboratory work", "How to study with this site", "First assignment and Q&amp;A"]
S.append('<section><h2><small>Today</small>Agenda</h2><div class="agenda">' + "".join(f'<div class="card"><span class="n">{i+1}</span>{a}</div>' for i, a in enumerate(ag)) + '</div><aside class="notes">Spend about 5 minutes on each part. Leave the last 10 minutes for questions.</aside></section>')
# --- about
sec("01", "About the course", "Code, load, objective and what you will be able to do at the end.")
slide("About the course", "Course snapshot", '<div class="two">'
      '<div class="card"><h4 style="margin-top:0">Identity</h4><p><b>Multimedia System</b></p><p>Code <code>BIT477MS</code></p><p>Year IV, Semester VII</p></div>'
      '<div class="card"><h4 style="margin-top:0">Weekly load</h4><p><b>3</b> hours theory</p><p><b>1</b> hour tutorial</p><p><b>2</b> hours practical</p></div></div>'
      '<div class="callout tip"><div class="ct">Plan your time</div><p>Theory classes explain the ideas, tutorials practise numericals and exam answers, and practicals build the skills. Skipping any of the three leaves a gap.</p></div>',
      "Read the load out loud. Ask: how many of you have used video-editing or audio software before?")
slide("About the course", "Course objective", '<div class="callout"><div class="ct">Official objective</div><p style="font-size:1.1em">To introduce the technologies, concepts and techniques associated with the development of multimedia systems.</p></div>'
      '<h4>By the end you should be able to</h4><ul><li><b>Explain</b> how sound, images and video are represented in a computer.</li><li><b>Calculate</b> storage, data rate, compression ratio and schedulability.</li><li><b>Describe</b> how multimedia is stored, scheduled, transmitted and synchronized.</li><li><b>Apply</b> the ideas in practical work: audio, images, compression and scheduling.</li></ul>')
slide("Why multimedia matters", "You already use it every day", cards([
    ("Streaming and calls", "Video and audio must be compressed, sent in real time and kept in sync."),
    ("Games and animation", "Graphics, sound and interaction are all scheduled against strict deadlines."),
    ("Learning and libraries", "E-learning, digital libraries and archives combine text, images, audio and video."),
    ("Broadcast and storage", "Digital TV, CDs, DVDs and Blu-ray rely on the standards you will study.")]) +
    '<div class="callout ex"><div class="ct">Think</div><p>Pick one app on your phone. Which of its media must be compressed, and which must arrive on time?</p></div>',
    "Cold-call two students for their answer to the Think box.")
slide("Why multimedia matters", "What is multimedia?", '<div class="two"><div class="card"><h4 style="margin-top:0">Discrete media</h4><p>Do not depend on time.</p><ul style="font-size:.85em"><li>Text</li><li>Still images</li><li>Graphics</li></ul></div>'
      '<div class="card"><h4 style="margin-top:0">Continuous media</h4><p>Depend on time; late data is useless.</p><ul style="font-size:.85em"><li>Audio</li><li>Video</li><li>Animation</li></ul></div></div>'
      '<div class="callout exam"><div class="ct">Exam focus</div><p>A multimedia system is <b>computer-controlled</b>, <b>integrated</b>, handles <b>digital</b> media and is <b>interactive</b>, with at least one continuous medium.</p></div>',
      "This definition returns in Unit 1. Ask students to remember the four words: computer-controlled, integrated, digital, interactive.")
chain = ["Represent", "Compress", "Store", "Schedule", "Transmit", "Synchronize", "Program", "Apply"]
S.append('<section><h2><small>Big picture</small>The story of the course</h2><div class="agenda" style="grid-template-columns:repeat(4,1fr)">' +
         "".join(f'<div class="card" style="flex-direction:column;align-items:flex-start;gap:.2em"><span class="n">{i+1}</span>{c}</div>' for i, c in enumerate(chain)) +
         '</div><div class="callout tip"><div class="ct">Reading order</div><p>First learn what media <b>are</b> (units 1&ndash;4), then how to <b>shrink and store</b> them (5&ndash;6), how a system <b>delivers</b> them on time (7&ndash;10), and finally how to <b>build and use</b> them (11&ndash;12).</p></div>'
         '<aside class="notes">Trace the path of a video call: capture, compress, schedule, send, synchronize, play.</aside></section>')
# --- syllabus
sec("02", "Syllabus at a glance", "Twelve units, 45 teaching hours, 15 weeks.")
rows = "".join(f'<tr><td>{u["n"]}</td><td>{html.escape(u["title"])}</td><td>{u["hours"]}</td><td>{u["weeks"]}</td></tr>' for u in units)
slide("Syllabus", "All 12 units", f'<table class="xdense"><thead><tr><th>Unit</th><th>Title</th><th>Hours</th><th>Weeks</th></tr></thead><tbody>{rows}<tr><td></td><td><b>Total</b></td><td><b>{T}</b></td><td>15</td></tr></tbody></table>',
      "Point out that Unit 5 is the longest at 6 hours; it is also the most numerical.")
groups = [("Part 1 &middot; Foundations", "Units 1&ndash;4", "What multimedia is; how sound, images, video and animation are represented, stored in files and transmitted."),
          ("Part 2 &middot; Compression and storage", "Units 5&ndash;6", "Run-length, Huffman, predictive and adaptive coding; JPEG, H.261, MPEG, DVI; CD, DVD and Blu-ray media."),
          ("Part 3 &middot; Systems", "Units 7&ndash;10", "Real-time operating systems and scheduling (EDF, rate monotonic); communication and QoS; hypertext, SGML, ODA, MHEG; synchronization."),
          ("Part 4 &middot; Building and applying", "Units 11&ndash;12", "Abstraction levels, libraries, toolkits and object-oriented approaches; video on demand, conferencing, education and information systems.")]
slide("Syllabus", "Four parts, one story", '<div class="trio dense">' + "".join(f'<div class="card c{(i%3)+1}"><div class="ct">{a} &middot; {b}</div><p>{c}</p></div>' for i, (a, b, c) in enumerate(groups)) + '</div>',
      "Each part builds on the one before. Compression needs the representation from Part 1; scheduling needs the data rates from Part 2.")
# hours chart svg
mx = max(u["hours"] for u in units); w, h = 1000, 330; bw = 62; gap = (w - 60 - bw * 12) / 11
bars = ""
for i, u in enumerate(units):
    x = 30 + i * (bw + gap); bh = u["hours"] / mx * 220; y = 250 - bh
    bars += f'<rect x="{x:.0f}" y="{y:.0f}" width="{bw}" height="{bh:.0f}" rx="8" fill="{"#e6b95c" if u["hours"]==mx else "#6f86e6"}"/><text x="{x+bw/2:.0f}" y="{y-10:.0f}" text-anchor="middle" fill="#fff" font-size="22" font-weight="700">{u["hours"]}</text><text x="{x+bw/2:.0f}" y="285" text-anchor="middle" fill="#aeb6d6" font-size="20">U{u["n"]}</text>'
svg = f'<svg viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" font-family="Inter,sans-serif"><line x1="20" y1="250" x2="{w-20}" y2="250" stroke="rgba(255,255,255,.25)"/>{bars}</svg>'
slide("Hours and weekly plan", "Where the teaching hours go", f'<div class="vis">{svg}</div><p class="cap">Teaching hours per unit (total {T}). Unit 5, Data Compression, is the heaviest.</p>'
      '<div class="callout exam"><div class="ct">Exam focus</div><p>Hours hint at weight: give compression, scheduling and storage numericals extra practice time.</p></div>')
wk = "".join(f'<tr><td>{u["weeks"]}</td><td>{u["n"]}. {html.escape(u["title"])}</td></tr>' for u in units)
slide("Hours and weekly plan", "Week-by-week map", f'<table class="xdense"><thead><tr><th style="width:18%">Week</th><th>Unit</th></tr></thead><tbody>{wk}</tbody></table><p class="cap">Indicative plan; the exact dates follow the academic calendar. See the Instructor section of the site for the full plan.</p>')
# --- assessment
sec("03", "Marks and exam pattern", "How the 100 marks are earned.")
S.append('<section><h2><small>Assessment</small>The 100-mark scheme</h2><div class="two">'
         '<div class="card"><h4 style="margin-top:0">Internal &middot; 40</h4><p style="font-size:1.6em;margin:.1em 0"><b>20</b> theory</p><p style="font-size:1.6em;margin:.1em 0"><b>20</b> practical</p><p style="font-size:.75em;color:#aeb6d6">Assignments, quizzes, attendance and lab work.</p></div>'
         '<div class="card"><h4 style="margin-top:0">Final &middot; 60</h4><p style="font-size:1.6em;margin:.1em 0"><b>60</b> theory</p><p style="font-size:.75em;color:#aeb6d6">Written examination at the end of the semester. There is no final practical examination.</p></div></div>'
         '<div class="callout warn"><div class="ct">Note</div><p>Internal marks are earned during the semester and cannot be repaired at the end, so start early.</p></div>'
         '<aside class="notes">Confirm the exact split against the latest university notice before the class; the figures here come from the syllabus document.</aside></section>')
slide("Assessment", "What the final paper looks like", '<table><thead><tr><th>Section</th><th>Typical content</th><th>Marks</th></tr></thead><tbody>'
      '<tr><td>A &middot; Short objective</td><td>10 questions, 1 mark each</td><td>10</td></tr>'
      '<tr><td>B &middot; Short answers</td><td>6 questions, 5 marks each</td><td>30</td></tr>'
      '<tr><td>C &middot; Long answers</td><td>2 questions, 10 marks each</td><td>20</td></tr>'
      '<tr><td><b>Total</b></td><td></td><td><b>60</b></td></tr></tbody></table>'
      '<div class="callout tip"><div class="ct">Practice it</div><p>The two <b>Mock Exams</b> on this site follow exactly this layout, with a timer and a marking scheme.</p></div>'
      '<p class="cap">This is the pattern used in the mock papers. Always check the latest official question format.</p>')
slide("Assessment", "How marks are won", '<div class="trio"><div class="card c1"><div class="ct">Definition + diagram + example</div><p>Short answers: state the idea, draw it, give one concrete example.</p></div>'
      '<div class="card c2"><div class="ct">Show every step in numericals</div><p>Formula, substitution, result with units. Method marks are given even if the final value is wrong.</p></div>'
      '<div class="card c3"><div class="ct">Compare and contrast</div><p>Use a small table: it earns marks quickly (EDF vs RM, lossy vs lossless, CD vs DVD).</p></div></div>')
# --- labs
sec("04", "Laboratory work", "Two practical hours every week.")
slide("Laboratory work", "Practical topics in the syllabus", '<ol><li>Integration of multimedia: audio, speech and music, video, static media, movie and animation programming.</li><li>Image enhancement in Photoshop and Flash.</li><li>2D and 3D animation in OpenGL, Maya, Flash or C++.</li><li>Image compression algorithm: JPEG.</li><li>Real-time scheduling algorithm.</li></ol>'
      '<div class="callout tip"><div class="ct">Bring</div><p>A notebook for lab records, headphones, and any photos or short audio clips you want to work on.</p></div>')
slide("Laboratory work", "Labs and tools on this site", cards([("Python labs", "Sampling and aliasing, Huffman and RLE, DCT and quantization, EDF and RM scheduling, synchronization drift. Every script is tested."),
      ("Tool labs", "GIMP for images and colour, Audacity for audio, FFmpeg for conversion and compression."),
      ("Simulators", "Six live simulators in the browser: sampling, Huffman, scheduler, bucket, DCT and a calculator."),
      ("Lab record", "Write aim, steps, results with screenshots, and a short reflection for each lab.")]))
# --- study
sec("05", "How to study with this site", "Notes, slides, practice, revision tools.")
slide("Study toolkit", "Everything in one place", cards([
    ("Topic notes", "Deep notes for every unit with worked examples and exam-focus boxes."),
    ("Class slides", "Animated decks for each unit, with quick checks and speaker notes."),
    ("Practice questions", "Self-marking MCQs, short and long questions with model answers and flashcards."),
    ("Revision hub", "Formula sheet, cheat sheets, mock exams with a timer, planner and Nepali glossary.")], "two") +
    '<p class="cap">Progress is saved in your own browser; the site tracks what you have completed.</p>')
slide("Study routine", "A weekly routine that works", '<div class="trio"><div class="card c1"><div class="ct">Before class &middot; 20 min</div><p>Skim the unit overview and the key terms.</p></div>'
      '<div class="card c2"><div class="ct">After class &middot; 40 min</div><p>Read the topic notes, then answer the practice questions for that topic without looking.</p></div>'
      '<div class="card c3"><div class="ct">Weekend &middot; 60 min</div><p>Flashcards, one simulator, and one numerical written out in full.</p></div></div>')
slide("Warm-up", "Check yourself", '<div class="chk"><div class="lab">Check yourself</div><p class="q">Which of these is a continuous medium: text, a still image, or audio?</p>'
      '<div class="fragment ans">Audio. Its meaning depends on time; late samples are useless.</div></div>'
      '<div class="chk"><div class="lab">Check yourself</div><p class="q">How many marks is the final theory paper, and how many are internal?</p>'
      '<div class="fragment ans">60 marks final theory; 40 marks internal (20 theory + 20 practical).</div></div>')
# --- close
slide("Next steps", "First assignment", '<ol><li>Read the <b>Unit 1 overview</b> and the topic <i>Introduction to multimedia</i>.</li><li>Attempt the first five <b>practice questions</b> of Unit 1.</li><li>Open the <b>sampling simulator</b> and find the lowest sampling rate that still shows a clean 1 kHz tone.</li><li>Write down two questions for the next class.</li></ol>'
      '<div class="callout exam"><div class="ct">Next class</div><p>Unit 1: the multimedia system, media properties and data streams.</p></div>')
S.append('<section><div class="title-slide"><div class="kick">End of Class 1</div><h1>Questions?</h1><p style="color:#aeb6d6;max-width:70%">Revise with the notes, attempt the practice questions, and bring your doubts to the next class.</p><div class="by">&copy; 2026 Er. Harish Thagunna. All rights reserved.</div></div></section>')
body = "\n".join(S)
body = B.prerender_math(body)
out = B.TEMPLATE.replace("Unit @@N@@: @@TITLE@@", "Class 1: Introduction and Syllabus Overview").replace("'Unit @@N@@'", "'Class 1'").replace("@@SLIDES@@", body)
open(os.path.join(B.DOCS, "decks", "class-01-introduction.html"), "w", encoding="utf-8").write(out)
print("slides:", out.count("<section"))
