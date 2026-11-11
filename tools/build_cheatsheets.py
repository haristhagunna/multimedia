"""Generate docs/revision/cheat-sheets.md (one printable page per unit)."""
import sys, html, yaml, os
sys.path.insert(0, os.path.dirname(__file__))
import enrich
E = enrich.E
cfg = yaml.safe_load(open("mkdocs.yml").read().replace("!!python/name", "#")) if False else None
import re
txt = open("mkdocs.yml").read()
units = re.findall(r'\{n: (\d+),\s+title: "([^"]+)"', txt)
F = {
 1: ["Multimedia = Computer-controlled + Integrated + Digital + Interactive (CIDI)", "Discrete: text, image, graphics. Continuous: audio, video, animation."],
 2: ["Nyquist: fs ≥ 2·fmax", "Size (bytes) = rate × bits/8 × channels × seconds", "CD-DA = 44,100 × 16 × 2 = 1,411,200 bit/s", "Levels = 2^bits"],
 3: ["Bitmap bytes = W × H × bits / 8", "640×480×8-bit = 307,200 bytes", "Dithering trades resolution for apparent colour depth"],
 4: ["Y = 0.30R + 0.59G + 0.11B; U ∝ (B−Y); V ∝ (R−Y)", "25 fps → 40 ms per frame", "Raw 640×480×24-bit×25 fps = 184.32 Mbit/s"],
 5: ["Ratio = original : compressed", "Avg length = Σ pᵢ·lᵢ", "RLE: aaabccdddd → a3b1c2d4", "JPEG: 8×8 → DCT → quantize (lossy) → zigzag → RLE/Huffman"],
 6: ["Block = 2,352 bytes, 75 blocks/s", "74 min × 60 × 75 = 333,000 blocks", "Mode 1 user data 2,048 B (≈650 MB); Mode 2 2,336 B", "Lasers: CD 780 nm, DVD 650 nm, Blu-ray 405 nm"],
 7: ["U = Σ Cᵢ/Pᵢ", "EDF: schedulable iff U ≤ 1 (D = P)", "RM bound: n(2^(1/n) − 1); sufficient, not necessary", "Example (2,5)+(4,7): U = 0.971 → EDF yes, RM no"],
 8: ["Leaky bucket: constant output rate, overflow dropped", "RTP: sequence no. + timestamp; RTCP: feedback", "QoS: negotiate → admit → guarantee"],
 9: ["Hypermedia = hypertext + multimedia", "Dexter layers: Run-time / Storage / Within-component", "SGML: structure via DTD; ODA: logical + layout; MHEG: final-form objects"],
 10: ["Lip sync: skew within ±80 ms", "Drift = clock error × time (0.1% × 600 s = 0.6 s)", "Fix: clock sync, buffering, adaptive playout"],
 11: ["Abstraction levels: device/system → library → toolkit → language → application", "Toolkit = reusable object components"],
 12: ["Development cycle: plan → design (storyboard) → produce → test → deliver", "Systems: input + processing + storage + output components", "Applications: VoD, video conferencing, education, information systems, digital libraries, entertainment"],
}
out = ['# Cheat sheets', '',
 '<div class="cheat-bar"><button class="btn-s primary" onclick="window.print()">Print / Save as PDF</button> '
 '<a class="btn-s" href="../../downloads/cheat-sheets.pdf" download>Download PDF</a> '
 '<span>One A4 page per unit. Memorise these the night before; understand them from the notes first.</span></div>', '']
for n, title in units:
    n = int(n); pages = E.get(n, {})
    out.append(f'<section class="cheat"><h2>Unit {n}: {html.escape(title)}</h2>')
    out.append('<div class="cheat-f"><b>Formulas and facts</b><ul>' + ''.join(f'<li>{html.escape(x)}</li>' for x in F[n]) + '</ul></div>')
    out.append('<div class="cheat-hooks"><b>Memory hooks</b><ul>' + ''.join(f'<li>{html.escape(p["hook"])}</li>' for p in pages.values() if p.get("hook")) + '</ul></div>')
    seen = set(); rows = []
    for p in pages.values():
        for t, d in p.get("terms", []):
            if t not in seen: seen.add(t); rows.append((t, d))
    out.append('<div class="cheat-terms"><b>Key terms</b><dl>' + ''.join(f'<dt>{html.escape(t)}</dt><dd>{html.escape(d)}</dd>' for t, d in rows[:16]) + '</dl></div>')
    out.append(f'<p class="cheat-foot">© 2026 Er. Harish Thagunna · Multimedia and Application (BCA429CO)</p></section>')
open("docs/revision/cheat-sheets.md", "w").write("\n".join(out) + "\n")
print("ok", len(units))
