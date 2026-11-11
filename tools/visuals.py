"""Custom chart/diagram slides for the class decks (matplotlib -> inline SVG).
Copyright (c) 2026 Er. Harish Thagunna. All rights reserved.
VIS[unit] = [(page_slug, "start"|"end", title, svg, caption), ...]
"""
import io, re, math, warnings
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle, Circle, FancyArrowPatch, Polygon
warnings.filterwarnings("ignore")

TX, MU = "#e8eaff", "#9aa0cc"
IN, VI, PK, CY, GR, OR, YE = "#818cf8", "#c084fc", "#f472b6", "#22d3ee", "#34d399", "#fb923c", "#fbbf24"
plt.rcParams.update({"svg.fonttype": "none", "font.family": ["DejaVu Sans"], "font.size": 12,
                     "text.color": TX, "axes.labelcolor": TX, "xtick.color": MU, "ytick.color": MU,
                     "axes.edgecolor": "#4b5190", "axes.facecolor": "none", "figure.facecolor": "none",
                     "axes.spines.top": False, "axes.spines.right": False, "axes.grid": False, "grid.color": "#2a2f5c"})
_n = [0]

def fig(w=10, h=4.6):
    _n[0] += 1
    plt.rcParams["svg.hashsalt"] = "f%d" % _n[0]
    return plt.figure(figsize=(w, h))

def svg(f):
    b = io.StringIO(); f.savefig(b, format="svg", transparent=True, bbox_inches="tight", pad_inches=.08); plt.close(f)
    s = b.getvalue(); s = s[s.index("<svg"):]
    s = re.sub(r'width="[\d.]+pt"\s+height="[\d.]+pt"', "", s, 1)
    s = s.replace("'DejaVu Sans'", "Inter, system-ui, sans-serif").replace("DejaVu Sans", "Inter, system-ui, sans-serif")
    return s

def box(ax, x, y, w, h, text, fc="#27306b", ec=IN, fs=11, tc=TX, r=.08, bold=False):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle=f"round,pad=0,rounding_size={r}", fc=fc, ec=ec, lw=1.4))
    ax.text(x + w / 2, y + h / 2, text, ha="center", va="center", fontsize=fs, color=tc, fontweight="bold" if bold else "normal")

def arrow(ax, p, q, c=IN, lw=1.6, st="-|>"):
    ax.add_patch(FancyArrowPatch(p, q, arrowstyle=st, mutation_scale=14, color=c, lw=lw))

def blank(w=10, h=4.6, xl=(0, 10), yl=(0, 5)):
    f = fig(w, h); ax = f.add_axes([0, 0, 1, 1]); ax.set_xlim(*xl); ax.set_ylim(*yl); ax.axis("off"); return f, ax

VIS = {}
def add(u, page, pos, title, s, cap=""):
    VIS.setdefault(u, []).append((page, pos, title, s, cap))

# ======================= UNIT 1 =======================
def u1():
    f = fig(9, 4.4); ax = f.add_subplot()
    items = [("1 page of text\n(~2,000 characters)", 2000), ("640×480 image\n24-bit", 640 * 480 * 3),
             ("1 min CD-quality\naudio", 44100 * 2 * 2 * 60), ("1 min raw video\n640×480, 25 fps", 640 * 480 * 3 * 25 * 60)]
    v = [i[1] for i in items]
    bars = ax.bar(range(4), v, color=[IN, VI, PK, OR], width=.6)
    ax.set_yscale("log"); ax.set_xticks(range(4)); ax.set_xticklabels([i[0] for i in items], fontsize=10)
    ax.set_ylabel("bytes (log scale)"); ax.set_ylim(1e3, 5e9)
    lab = ["2 KB", "0.92 MB", "10.6 MB", "1.38 GB"]
    for b, l in zip(bars, lab): ax.text(b.get_x() + b.get_width() / 2, b.get_height() * 1.4, l, ha="center", fontweight="bold")
    ax.grid(axis="y", alpha=.4); ax.set_axisbelow(True)
    add(1, "what-is-multimedia", "end", "Why multimedia is data-hungry", svg(f),
        "Computed: 640×480×3 B; 44,100×2 B×2 ch×60 s; 640×480×3 B×25×60 s. Each step is ~100× larger, which is why compression matters (Unit 5).")

    f, ax = blank(10, 4.4, (0, 10), (0, 4.6))
    ax.text(5, 4.3, "Discrete (time-independent)  vs  Continuous (time-dependent)", ha="center", fontsize=14, fontweight="bold")
    for i, (t, c) in enumerate([("Text", IN), ("Graphics", VI), ("Still image", PK)]):
        box(ax, .5 + i * 1.65, 2.4, 1.45, .9, t, ec=c, bold=True)
    ax.text(2.75, 1.9, "Each item is complete at any instant", ha="center", color=MU, fontsize=11)
    t = np.linspace(0, 1, 200)
    ax.plot(5.9 + t * 3.6, 2.9 + .45 * np.sin(t * 40) * np.exp(-t * 1.2), color=CY, lw=2)
    ax.text(7.7, 3.55, "Audio: meaning lives in the time axis", ha="center", color=CY, fontsize=11)
    for i in range(5):
        ax.add_patch(Rectangle((5.9 + i * .74, 1.95), .62, .62, fc="#27306b", ec=GR, lw=1.3))
        ax.text(5.9 + i * .74 + .31, 2.26, str(i + 1), ha="center", va="center", color=GR, fontweight="bold")
    ax.text(7.7, 1.55, "Video: 25 frames every second", ha="center", color=GR, fontsize=11)
    ax.plot([5.45, 5.45], [1.3, 4.0], color="#4b5190", ls="--")
    arrow(ax, (.5, .7), (9.5, .7), c=MU); ax.text(9.4, .35, "time", color=MU, ha="right")
    ax.text(5, 0.05, "Multimedia = discrete + continuous media, synchronised and presented together", ha="center", color=TX, fontsize=11.5, fontweight="bold")
    add(1, "media-classification", "end", "Discrete vs continuous media", svg(f))

    f, ax = blank(10, 4.2, (0, 10), (0, 4.2))
    ax.text(.1, 3.85, "Audio stream", color=CY, fontweight="bold")
    ax.text(.1, 2.3, "Video stream", color=GR, fontweight="bold")
    for i in range(10):
        box(ax, .2 + i * .96, 3.05, .88, .55, f"LDU {i + 1}", ec=CY, fs=9)
    for i in range(5):
        box(ax, .2 + i * 1.92, 1.5, 1.8, .55, f"Frame {i + 1}", ec=GR, fs=9)
    arrow(ax, (.1, .85), (9.8, .85), c=MU); ax.text(9.8, .45, "time", ha="right", color=MU)
    for x in (.2, 2.12, 4.04, 5.96, 7.88): ax.plot([x, x], [.9, 3.6], color="#4b5190", ls=":")
    ax.text(5, .1, "LDU = Logical Data Unit: the smallest unit the system schedules, stores and synchronises", ha="center", color=MU, fontsize=11)
    add(1, "data-streams", "end", "Continuous media as streams of LDUs", svg(f),
        "Dotted lines show points where audio and video units must line up (inter-stream synchronisation).")
u1()

# ======================= UNIT 2 =======================
def u2():
    f = fig(10, 4.2); ax = f.add_subplot()
    t = np.linspace(0, 2, 600); y = np.sin(2 * np.pi * t)
    ax.plot(t, y, color=IN, lw=2.4)
    ax.axhline(0, color="#4b5190", lw=1)
    ax.annotate("", xy=(0, 1.25), xytext=(1, 1.25), arrowprops=dict(arrowstyle="<->", color=PK)); ax.text(.5, 1.33, "one period T = 1/f", ha="center", color=PK)
    ax.annotate("", xy=(.27, 0), xytext=(.27, 1), arrowprops=dict(arrowstyle="<->", color=GR)); ax.text(.22, .45, "amplitude\n(loudness)", color=GR, fontsize=11, ha="right")
    ax.text(1.5, -1.45, "frequency f = cycles per second (Hz) → pitch", ha="center", color=OR, fontsize=12)
    ax.set_ylim(-1.7, 1.7); ax.set_xlim(-.4, 2.05); ax.set_xticks([]); ax.set_yticks([])
    for s in ax.spines.values(): s.set_visible(False)
    add(2, "sound-basics", "end", "Anatomy of a sound wave", svg(f), "Sound is a longitudinal pressure wave; a sine is the simplest model of it.")

    f = fig(10, 3.3); ax = f.add_subplot()
    bands = [("Infrasound", .1, 20, MU), ("Audible\n20 Hz–20 kHz", 20, 20e3, GR), ("Ultrasound", 20e3, 1e9, VI), ("Hypersound", 1e9, 1e13, PK)]
    for i, (n, a, b, c) in enumerate(bands):
        ax.barh(0, math.log10(b) - math.log10(a), left=math.log10(a), color=c, height=.5, edgecolor="#0b0d1c")
        ax.text((math.log10(a) + math.log10(b)) / 2, 0, n, ha="center", va="center", color="#0b0d1c", fontweight="bold", fontsize=10.5)
    ax.set_xticks([0, 1.3, 4.3, 9, 13]); ax.set_xticklabels(["1 Hz", "20 Hz", "20 kHz", "1 GHz", "10 THz"]); ax.set_yticks([]); ax.set_xlim(-1, 13); ax.set_ylim(-.6, .6)
    ax.spines["left"].set_visible(False)
    add(2, "sound-basics", "end", "The frequency spectrum of sound (log scale)", svg(f), "Humans hear roughly 20 Hz to 20 kHz.")

    f = fig(10, 3.8)
    t = np.linspace(0, 1, 800); fr = 3
    s = np.sin(2 * np.pi * fr * t)
    ax1 = f.add_subplot(1, 3, 1); ax1.plot(t, s, color=IN, lw=2); ts = np.arange(0, 1.0001, 1 / 12)
    ax1.vlines(ts, 0, np.sin(2 * np.pi * fr * ts), color=PK, lw=1.4); ax1.plot(ts, np.sin(2 * np.pi * fr * ts), "o", color=PK, ms=5)
    ax1.set_title("1  Sampling\n(fs = 12 Hz, f = 3 Hz)", fontsize=11, color=TX); ax1.set_xticks([]); ax1.set_yticks([])
    ax2 = f.add_subplot(1, 3, 2); lv = 8
    q = np.round((np.sin(2 * np.pi * fr * ts) + 1) / 2 * (lv - 1)) / (lv - 1) * 2 - 1
    ax2.plot(t, s, color="#4b5190", lw=1.2); ax2.step(ts, q, where="post", color=VI, lw=2); ax2.plot(ts, q, "o", color=VI, ms=4)
    for l in np.linspace(-1, 1, lv): ax2.axhline(l, color="#2a2f5c", lw=.6)
    ax2.set_title("2  Quantization\n(3 bit = 8 levels)", fontsize=11); ax2.set_xticks([]); ax2.set_yticks([])
    ax3 = f.add_subplot(1, 3, 3); ax3.axis("off"); ax3.set_xlim(0, 1); ax3.set_ylim(0, 1)
    codes = [format(int(round((v + 1) / 2 * 7)), "03b") for v in np.sin(2 * np.pi * fr * ts[:8])]
    ax3.text(.5, .95, "3  Encoding", ha="center", fontsize=11, va="top")
    for i, c in enumerate(codes): ax3.text(.5, .8 - i * .095, c, ha="center", family="monospace", color=GR, fontsize=12)
    for a in (ax1, ax2):
        for sp in a.spines.values(): sp.set_color("#4b5190")
    add(2, "digital-audio", "start", "Analog to digital: sample, quantize, encode", svg(f), "The first 8 samples are encoded as 3-bit PCM words on the right.")

    f = fig(10, 3.6)
    t = np.linspace(0, 1, 1000); ax = f.add_subplot()
    ax.plot(t, np.sin(2 * np.pi * 9 * t), color="#4b5190", lw=1.3, label="true signal, f = 9 Hz")
    ts = np.arange(0, 1.0001, .1); ax.plot(ts, np.sin(2 * np.pi * 9 * ts), "o", color=PK, ms=7, label="samples at fs = 10 Hz")
    tt = np.linspace(0, 1, 400); ax.plot(tt, -np.sin(2 * np.pi * 1 * tt), color=OR, lw=2.4, label="what the samples look like: 1 Hz alias")
    ax.legend(loc="upper right", fontsize=9.5, frameon=False, labelcolor=TX); ax.set_xticks([]); ax.set_yticks([]); ax.set_ylim(-1.3, 2.1)
    for s_ in ax.spines.values(): s_.set_visible(False)
    add(2, "digital-audio", "end", "Nyquist: sampling too slowly creates aliases", svg(f),
        "Rule: fs ≥ 2·fmax. A 9 Hz tone sampled at 10 Hz (< 18 Hz) is indistinguishable from a 1 Hz tone.")

    f = fig(10, 3.9); ax = f.add_subplot()
    cfg = [("Telephone\n8 kHz, 8-bit, mono", 8000 * 1 * 1 * 60), ("Radio\n22.05 kHz, 16-bit, mono", 22050 * 2 * 1 * 60),
           ("CD\n44.1 kHz, 16-bit, stereo", 44100 * 2 * 2 * 60), ("Studio\n48 kHz, 24-bit, stereo", 48000 * 3 * 2 * 60)]
    b = ax.bar(range(4), [c[1] / 1e6 for c in cfg], color=[IN, VI, PK, OR], width=.6)
    ax.set_xticks(range(4)); ax.set_xticklabels([c[0] for c in cfg], fontsize=10); ax.set_ylabel("MB per minute")
    for r, c in zip(b, cfg): ax.text(r.get_x() + r.get_width() / 2, r.get_height() + .3, f"{c[1] / 1e6:.2f} MB", ha="center", fontweight="bold")
    ax.grid(axis="y", alpha=.4); ax.set_axisbelow(True)
    add(2, "digital-audio", "end", "Uncompressed audio size per minute", svg(f), "S = R × (b/8) × C × D, evaluated for D = 60 s.")

    f, ax = blank(10, 3.5, (0, 16), (0, 3.5))
    ax.text(.1, 3.1, "MIDI Note On message = 3 bytes", fontsize=13, fontweight="bold")
    fields = [("1", PK), ("0", PK), ("0", PK), ("1", PK)]
    x = .3
    for i, (lab, w_, c, d) in enumerate([("status byte", 4, PK, "1001 cccc"), ("data byte 1", 4, CY, "0 kkkkkkk"), ("data byte 2", 4, GR, "0 vvvvvvv")]):
        box(ax, x + i * 5, 1.7, 4.6, .9, d, ec=c, fs=13, bold=True); ax.text(x + i * 5 + 2.3, 1.3, lab, ha="center", color=c, fontsize=11)
    ax.text(2.6, .75, "1001 = Note On\ncccc = channel (1–16)", ha="center", color=MU, fontsize=10.5)
    ax.text(7.6, .75, "kkkkkkk = key number 0–127\n(60 = middle C)", ha="center", color=MU, fontsize=10.5)
    ax.text(12.6, .75, "vvvvvvv = velocity 0–127\n(how hard the key is hit)", ha="center", color=MU, fontsize=10.5)
    add(2, "midi", "end", "Anatomy of a MIDI message", svg(f), "MIDI sends instructions (which note, how loud), not audio samples, so files are tiny.")

    f = fig(10, 3.6); ax = f.add_subplot()
    cfg = [("CD audio PCM", 44100 * 16 * 2 / 1000), ("Telephone PCM (G.711)", 64), ("ADPCM 4-bit @ 8 kHz", 32)]
    b = ax.barh(range(3), [c[1] for c in cfg], color=[PK, IN, VI], height=.55); ax.set_xscale("log")
    ax.set_yticks(range(3)); ax.set_yticklabels([c[0] for c in cfg]); ax.invert_yaxis(); ax.set_xlabel("kbit/s (log scale)")
    for r, c in zip(b, cfg): ax.text(r.get_width() * 1.08, r.get_y() + r.get_height() / 2, f"{c[1]:g} kbit/s", va="center", fontweight="bold")
    ax.set_xlim(10, 6000)
    add(2, "speech-transmission", "end", "Bit rates: what must the network carry?", svg(f), "CD: 44,100 × 16 × 2 = 1,411.2 kbit/s. Telephone PCM: 8,000 × 8 = 64 kbit/s. ADPCM: 8,000 × 4 = 32 kbit/s.")
u2()

# ======================= UNIT 3 =======================
def u3():
    f = fig(10, 4.4)
    ax = f.add_subplot(1, 2, 1)
    A = ["00011000", "00111100", "01100110", "01100110", "01111110", "01100110", "01100110", "01100110"]
    for r, row in enumerate(A):
        for c, ch in enumerate(row):
            ax.add_patch(Rectangle((c, 7 - r), 1, 1, fc=IN if ch == "1" else "#12152b", ec="#2a2f5c", lw=1))
            ax.text(c + .5, 7 - r + .5, ch, ha="center", va="center", fontsize=9, color="#0b0d1c" if ch == "1" else MU)
    ax.set_xlim(0, 8); ax.set_ylim(0, 8); ax.set_aspect("equal"); ax.axis("off"); ax.set_title("Bitmap: 8×8 pixels, 1 bit each = 8 bytes", fontsize=11)
    ax = f.add_subplot(1, 2, 2); ax.set_aspect("equal"); ax.axis("off")
    th = np.linspace(0, 2 * np.pi, 300); ax.plot(np.cos(th), np.sin(th), color=PK, lw=3)
    ax.plot([-1, 1], [0, 0], color=VI, lw=2); ax.plot([0, 0], [-1, 1], color=VI, lw=2)
    ax.text(0, -1.35, "Vector: circle(cx,cy,r) + line()\nstored as a few numbers; scales without blur", ha="center", fontsize=11, color=TX)
    ax.set_title("Vector graphic", fontsize=11); ax.set_xlim(-1.4, 1.4); ax.set_ylim(-1.8, 1.4)
    add(3, "image-basics", "start", "Bitmap vs vector", svg(f), "Bitmaps store every pixel (resolution-dependent); vectors store geometric descriptions (resolution-independent).")

    N = 300; yy, xx = np.mgrid[-1.5:1.5:N * 1j, -1.5:1.5:N * 1j]
    def disc(cx, cy, r): return ((xx - cx) ** 2 + (yy - cy) ** 2) < r * r
    R, G, B = disc(-.5, .45, .8), disc(.5, .45, .8), disc(0, -.4, .8)
    add_img = np.stack([R, G, B], -1).astype(float)
    C, M, Y = disc(-.5, .45, .8), disc(.5, .45, .8), disc(0, -.4, .8)
    sub = np.ones((N, N, 3)); sub[C] *= [0, 1, 1]; sub[M] = sub[M] * [1, 0, 1] if False else sub[M]
    sub = np.ones((N, N, 3))
    for m, col in ((C, [0, 1, 1]), (M, [1, 0, 1]), (Y, [1, 1, 0])): sub[m] = sub[m] * np.array(col)
    f = fig(10, 4.2)
    for i, (img, t) in enumerate([(add_img, "RGB: additive (screens)\nR+G+B = white"), (sub, "CMY: subtractive (print)\nC+M+Y ≈ black (K added)")]):
        ax = f.add_subplot(1, 2, i + 1)
        bg = np.zeros((N, N, 3)) + (0.05 if i == 0 else 0.98)
        ax.imshow(np.clip(img if i else img, 0, 1), origin="lower"); ax.axis("off"); ax.set_title(t, fontsize=11)
    add(3, "image-basics", "end", "Colour models", svg(f), "Screens add light (RGB); printing subtracts light with inks (CMY + K).")

    f = fig(10, 4); ax = f.add_subplot()
    cfg = [("640×480\n8-bit", 640 * 480 * 1), ("640×480\n24-bit", 640 * 480 * 3), ("1024×768\n24-bit", 1024 * 768 * 3), ("1920×1080\n24-bit", 1920 * 1080 * 3)]
    b = ax.bar(range(4), [c[1] / 1e6 for c in cfg], color=[IN, VI, PK, OR], width=.6)
    for r, c in zip(b, cfg): ax.text(r.get_x() + r.get_width() / 2, r.get_height() + .1, f"{c[1] / 1e6:.2f} MB", ha="center", fontweight="bold")
    ax.set_xticks(range(4)); ax.set_xticklabels([c[0] for c in cfg], fontsize=10); ax.set_ylabel("uncompressed MB"); ax.grid(axis="y", alpha=.4); ax.set_axisbelow(True)
    add(3, "image-analysis", "start", "Uncompressed bitmap size = width × height × bits / 8", svg(f), "Decimal MB (1 MB = 10⁶ bytes).")
u3()

# ======================= UNIT 4 =======================
def u4():
    f = fig(10, 3.9)
    ax = f.add_subplot(1, 2, 1); ax.axis("off"); ax.set_xlim(0, 10); ax.set_ylim(0, 10)
    for i in range(10):
        c = IN if i % 2 == 0 else PK
        ax.plot([1, 9], [9.3 - i * .9] * 2, color=c, lw=3)
        ax.text(.6, 9.3 - i * .9, str(i + 1), ha="right", va="center", color=c, fontsize=9)
    ax.set_title("Interlaced scan: odd lines (field 1), even lines (field 2)", fontsize=10.5)
    ax2 = f.add_subplot(1, 2, 2)
    bars = [("White", 1, 1, 1), ("Yellow", 1, 1, 0), ("Cyan", 0, 1, 1), ("Green", 0, 1, 0), ("Magenta", 1, 0, 1), ("Red", 1, 0, 0), ("Blue", 0, 0, 1), ("Black", 0, 0, 0)]
    Ys = [.30 * r + .59 * g + .11 * b for _, r, g, b in bars]
    for i, ((n, r, g, b), y) in enumerate(zip(bars, Ys)):
        ax2.add_patch(Rectangle((i, 1.1), 1, 1, fc=(r, g, b), ec="none")); ax2.add_patch(Rectangle((i, 0), 1, 1, fc=(y, y, y), ec="none"))
        ax2.text(i + .5, -.25, f"{y:.2f}", ha="center", fontsize=8.5, color=MU); ax2.text(i + .5, 2.25, n, ha="center", fontsize=8, rotation=0, color=MU)
    ax2.set_xlim(0, 8); ax2.set_ylim(-.6, 2.7); ax2.axis("off"); ax2.set_title("Y = 0.30R + 0.59G + 0.11B (luminance)", fontsize=10.5)
    add(4, "video-representation", "end", "Scanning and luminance", svg(f), "Interlacing halves the flicker for the same bandwidth; Y gives the black-and-white picture, and U, V carry colour differences.")

    f = fig(10, 3.8)
    for k, name in enumerate(["4:4:4", "4:2:2", "4:2:0"]):
        ax = f.add_subplot(1, 3, k + 1); ax.set_xlim(-.2, 4.2); ax.set_ylim(-.2, 2.4); ax.set_aspect("equal"); ax.axis("off")
        for r in range(2):
            for c in range(4):
                ax.add_patch(Rectangle((c, 1 - r), 1, 1, fc="#12152b", ec="#2a2f5c")); ax.plot(c + .5, 1 - r + .5, "s", color=YE, ms=7)
        if k == 0: pts = [(c + .5, 1 - r + .5) for c in range(4) for r in range(2)]
        elif k == 1: pts = [(c + 1.0, 1 - r + .5) for c in (0, 2) for r in range(2)]
        else: pts = [(c + 1.0, 1.0) for c in (0, 2)]
        for x_, y_ in pts: ax.plot(x_, y_, "o", color=CY, ms=9, mfc="none", mew=2)
        ax.set_title(name, fontsize=13, fontweight="bold")
    f.text(.5, .03, "■ luminance (Y) at every pixel      ○ chrominance (U,V) sample shared by neighbouring pixels", ha="center", fontsize=10, color=MU)
    add(4, "computer-video-format", "end", "Chroma subsampling", svg(f), "The eye is less sensitive to colour detail than to brightness, so U and V can be sampled less often than Y.")

    f = fig(10, 3.9); ax = f.add_subplot()
    cfg = [("CIF\n352×288", 352 * 288 * 3 * 25), ("VGA\n640×480", 640 * 480 * 3 * 25), ("Full HD\n1920×1080", 1920 * 1080 * 3 * 25)]
    b = ax.bar(range(3), [c[1] * 8 / 1e6 for c in cfg], color=[IN, VI, PK], width=.55)
    for r, c in zip(b, cfg): ax.text(r.get_x() + r.get_width() / 2, r.get_height() + 15, f"{c[1] * 8 / 1e6:,.0f} Mbit/s", ha="center", fontweight="bold")
    ax.set_xticks(range(3)); ax.set_xticklabels([c[0] for c in cfg]); ax.set_ylabel("Mbit/s"); ax.grid(axis="y", alpha=.4); ax.set_axisbelow(True)
    add(4, "computer-video-format", "end", "Raw video data rate (24-bit colour, 25 fps)", svg(f), "Rate = width × height × 3 bytes × 25 × 8. Even CIF needs ~61 Mbit/s uncompressed.")

    f = fig(10, 3.8); ax = f.add_subplot()
    x = np.linspace(0, 10, 400); y = 4 * (1 - ((x - 5) / 5) ** 2) * 0.9 + .3
    ax.plot(x, y, color="#4b5190", ls="--", lw=1.2)
    keys = [0, 5, 10]
    for i, xv in enumerate(np.linspace(0, 10, 11)):
        yv = 4 * (1 - ((xv - 5) / 5) ** 2) * 0.9 + .3
        key = xv in (0, 5, 10)
        ax.add_patch(Circle((xv, yv), .38 if key else .22, fc=PK if key else "none", ec=PK if key else VI, lw=1.8, alpha=1 if key else .8))
    ax.text(0, 1.4, "key frame", color=PK, ha="center"); ax.text(5, 4.7, "key frame", color=PK, ha="center"); ax.text(10, 1.4, "key frame", color=PK, ha="center")
    ax.text(8.6, 4.5, "in-betweens (tweening)\ngenerated by the computer", color=VI, ha="center", fontsize=11)
    ax.set_xlim(-1, 11); ax.set_ylim(-.4, 5.6); ax.set_aspect("equal"); ax.axis("off")
    add(4, "animation-basics", "end", "Key frames and in-betweens", svg(f), "The animator defines key poses; interpolation produces the frames between them.")
u4()

# ======================= UNIT 5 =======================
def u5():
    f = fig(10, 3.2); ax = f.add_subplot(); ax.axis("off"); ax.set_xlim(0, 15); ax.set_ylim(0, 3.2)
    s = "aaaabbcccccddd"; cols = {"a": IN, "b": VI, "c": PK, "d": CY}
    for i, ch in enumerate(s):
        ax.add_patch(Rectangle((.3 + i * .95, 1.9), .9, .9, fc=cols[ch], ec="#0b0d1c")); ax.text(.3 + i * .95 + .45, 2.35, ch, ha="center", va="center", color="#0b0d1c", fontweight="bold", fontsize=13)
    ax.text(.3, 3.05, "Input: 14 characters", color=MU, fontsize=11)
    arrow(ax, (7, 1.8), (7, 1.35), c=MU)
    for i, (ch, n) in enumerate([("a", 4), ("b", 2), ("c", 5), ("d", 3)]):
        ax.add_patch(Rectangle((3.4 + i * 2, .25), 1.8, .9, fc="#12152b", ec=cols[ch], lw=2)); ax.text(3.4 + i * 2 + .9, .7, f"{ch}{n}", ha="center", va="center", fontsize=15, fontweight="bold", color=cols[ch])
    ax.text(.3, .7, "Output: 8 chars\nratio 14 : 8 = 1.75 : 1", color=GR, fontsize=11, va="center")
    add(5, "rle-and-huffman", "start", "Run-length encoding in pictures", svg(f))

    f, ax = blank(8.6, 4.8, (0, 12.6), (0, 6))
    def node(x, y, t, c=IN, w=1.2): box(ax, x - w / 2, y - .35, w, .7, t, ec=c, fs=12, bold=True)
    node(6, 5.2, "15"); node(3, 3.8, "C (6)", CY, 1.5); node(9, 3.8, "9"); node(6.6, 2.4, "4"); node(11.4, 2.4, "A (5)", CY, 1.5)
    node(5.4, 1.0, "B (1)", CY, 1.5); node(8.2, 1.0, "D (3)", CY, 1.5)
    for (a, b, l) in [((6, 4.85), (3, 4.15), "0"), ((6, 4.85), (9, 4.15), "1"), ((9, 3.45), (6.6, 2.75), "0"), ((9, 3.45), (11.4, 2.75), "1"), ((6.6, 2.05), (5.4, 1.35), "0"), ((6.6, 2.05), (8.2, 1.35), "1")]:
        ax.plot([a[0], b[0]], [a[1], b[1]], color=MU, lw=1.5); ax.text((a[0] + b[0]) / 2 + (-.2 if l == "0" else .2), (a[1] + b[1]) / 2 + .1, l, color=YE, fontweight="bold", fontsize=13)
    rows = [("C", "0", 6), ("A", "11", 5), ("B", "100", 1), ("D", "101", 3)]
    ax.text(.2, 5.5, "Code table", fontweight="bold", color=TX)
    for i, (c, code, fq) in enumerate(rows):
        ax.text(.2, 4.9 - i * .5, f"{c} (freq {fq}) → {code}", family="monospace", color=GR, fontsize=12.5)
    bits = sum(len(c) * q for _, c, q in rows)
    ax.text(.2, 2.6, f"Total = 6×1 + 5×2 + 1×3 + 3×3\n      = {bits} bits  vs  15×8 = 120 bits", family="monospace", color=TX, fontsize=11)
    ax.text(.2, 1.6, f"Compression ratio ≈ {120 / bits:.2f} : 1", color=OR, fontweight="bold", fontsize=12)
    add(5, "rle-and-huffman", "end", "Huffman tree and codes (worked example)", svg(f), "Frequent symbols (C, A) get short codes; rare ones (B, D) get longer codes; no code is a prefix of another.")

    f = fig(10, 3.6); ax = f.add_subplot()
    t = np.linspace(0, 1, 500); s = np.sin(2 * np.pi * 3 * t) + .35 * np.sin(2 * np.pi * 11 * t)
    q = np.round(s * 2.2) / 2.2
    ax.plot(t, s, color=IN, lw=2, label="original"); ax.step(t, q, color=PK, lw=1.4, where="mid", label="lossy reconstruction")
    ax.fill_between(t, s, q, color=OR, alpha=.25, label="discarded detail (error)")
    ax.legend(frameon=False, fontsize=10, labelcolor=TX, loc="lower center", ncol=3, bbox_to_anchor=(.5, -.18)); ax.set_xticks([]); ax.set_yticks([])
    for sp in ax.spines.values(): sp.set_visible(False)
    add(5, "basics", "end", "Lossless vs lossy", svg(f), "Lossless: exact original after decoding (RLE, Huffman). Lossy: fine detail the senses barely notice is thrown away for a much higher ratio.")

    f = fig(7, 5); ax = f.add_subplot(); ax.set_xlim(0, 8); ax.set_ylim(0, 8); ax.set_aspect("equal"); ax.axis("off")
    order = []
    for s in range(15):
        pts = [(i, s - i) for i in range(8) if 0 <= s - i < 8]
        if s % 2 == 1: pts = pts[::-1]
        order += pts
    idx = {}
    for k, (c, r) in enumerate(order): idx[(c, r)] = k
    for (c, r), k in idx.items():
        v = 1 - k / 63
        ax.add_patch(Rectangle((c, 7 - r), 1, 1, fc=plt.cm.cool(k / 63), ec="#0b0d1c", alpha=.55)); ax.text(c + .5, 7 - r + .5, str(k), ha="center", va="center", fontsize=8.5, color="#fff")
    xs = [c + .5 for c, r in order]; ys = [7 - r + .5 for c, r in order]
    ax.plot(xs, ys, color="#fff", lw=1, alpha=.6)
    ax.text(0, -.5, "DC (low freq) top-left → high frequencies bottom-right", fontsize=10.5, color=MU)
    ax.text(4, 8.4, "Zig-zag scan of the 8×8 DCT block", ha="center", fontweight="bold", fontsize=12)
    add(5, "jpeg", "end", "JPEG zig-zag order", svg(f), "After quantization most high-frequency coefficients are 0, so zig-zag ordering produces long zero runs that RLE/Huffman compress well.")

    f, ax = blank(10, 4.6, (0, 14), (0, 4.9))
    disp = ["I", "B", "B", "P", "B", "B", "P"]; nums = [0, 1, 2, 3, 4, 5, 6]
    colr = {"I": PK, "P": IN, "B": GR}
    ax.text(0, 4.6, "Display order", fontweight="bold")
    for i, (t, n) in enumerate(zip(disp, nums)): box(ax, .2 + i * 1.9, 3.0, 1.5, .7, f"{t}{n}", ec=colr[t], bold=True, fs=13)
    for a, b_ in [(0, 3), (3, 6)]:
        ax.add_patch(FancyArrowPatch((.95 + a * 1.9, 3.75), (.95 + b_ * 1.9, 3.75), connectionstyle="arc3,rad=-.45", arrowstyle="-|>", mutation_scale=13, color=IN, lw=1.6))
    ax.text(5.3, 4.45, "forward prediction", color=IN, fontsize=10, ha="center")
    ax.text(0, 1.75, "Transmission / decoding order", fontweight="bold")
    tx = ["I0", "P3", "B1", "B2", "P6", "B4", "B5"]
    for i, t in enumerate(tx): box(ax, .2 + i * 1.9, .8, 1.5, .7, t, ec=colr[t[0]], bold=True, fs=13)
    ax.text(7, .2, "B-pictures need both a past and a future reference, so the future P is sent first.", ha="center", color=MU, fontsize=10.5)
    add(5, "mpeg-h261-dvi", "end", "MPEG picture types and reordering", svg(f), "I = intra (self-contained), P = predicted from earlier I/P, B = bidirectionally predicted from both sides.")

    f = fig(10, 3.9); ax = f.add_subplot()
    t = np.arange(0, 24); s = 50 + 30 * np.sin(t / 3.2) + 6 * np.sin(t * 1.7) * 0 + t * 1.2
    res = np.diff(s, prepend=s[0])
    ax.plot(t, s, "-o", color=IN, ms=4, lw=1.8, label="signal samples")
    ax.bar(t, res, color=PK, width=.55, label="difference to previous sample (what DPCM sends)")
    ax.axhline(0, color="#4b5190", lw=1); ax.legend(frameon=False, fontsize=10, labelcolor=TX, loc="upper left"); ax.set_xticks([]); ax.set_yticks([])
    for sp in ax.spines.values(): sp.set_visible(False)
    add(5, "prediction-and-adaptive", "end", "Prediction (DPCM): send differences, not values", svg(f), "Neighbouring samples are similar, so differences are small numbers that need fewer bits.")
u5()

# ======================= UNIT 6 =======================
def u6():
    f, ax = blank(10, 4.2, (0, 12), (0, 5))
    layers = [(3.2, 1.0, "Label / protective lacquer", "#3b2a6b"), (2.4, .7, "Reflective aluminium layer (pits & lands)", "#5b6bd6"), (.9, 1.5, "Polycarbonate substrate (clear plastic)", "#1c2150")]
    y = 3.2
    ax.add_patch(Rectangle((.5, 3.7), 9, .45, fc="#3b2a6b", ec=IN)); ax.text(5, 3.92, "Label / lacquer", ha="center", va="center", fontsize=11)
    ax.add_patch(Rectangle((.5, 3.3), 9, .4, fc="#7c85ff", ec=IN)); ax.text(5, 3.5, "Reflective aluminium layer", ha="center", va="center", fontsize=11, color="#0b0d1c")
    ax.add_patch(Rectangle((.5, 1.9), 9, 1.4, fc="#161a3a", ec=IN)); ax.text(5, 2.6, "Polycarbonate (clear plastic)", ha="center", va="center", fontsize=11, color=MU)
    for i, x in enumerate([1.2, 2.6, 4.4, 6.0, 7.5]):
        ax.add_patch(Rectangle((x, 3.1), .9 if i % 2 == 0 else .5, .2, fc="#0b0d1c", ec=PK))
    ax.text(1.65, 2.95, "pit", color=PK, ha="center", fontsize=10); ax.text(3.3, 2.95, "land", color=GR, ha="center", fontsize=10)
    ax.add_patch(Polygon([[4.2, 0.5], [5.3, 0.5], [4.85, 3.3]], fc=OR, alpha=.35, ec=OR))
    ax.text(4.75, .2, "Laser beam from below (~780 nm)", ha="center", color=OR, fontsize=11)
    ax.text(10.1, 3.4, "read from the\nunderside", color=MU, fontsize=10, va="center")
    ax.text(10.1, 2.2, "Land: beam reflected\nPit: scattered/less\nlight → bit pattern", color=MU, fontsize=10, va="center")
    add(6, "basic-technology", "end", "Cross-section of a compact disc", svg(f), "Data is a spiral track of pits and lands; the transition between them, not the pit itself, encodes a 1.")

    f = fig(10, 4); ax = f.add_subplot()
    ax.set_xlim(0, 2352); ax.set_ylim(-.5, 3.2); ax.axis("off")
    def row(y, parts, lab):
        x = 0
        for name, n, c in parts:
            ax.add_patch(Rectangle((x, y), n, .6, fc=c, ec="#0b0d1c")); 
            if n > 150: ax.text(x + n / 2, y + .3, f"{name}", ha="center", va="center", fontsize=10, color="#0b0d1c", fontweight="bold")
            x += n
        ax.text(-30, y + .3, lab, ha="right", va="center", fontsize=11, fontweight="bold")
    row(2.2, [("Audio data (2,352 bytes)", 2352, CY)], "CD-DA")
    row(1.3, [("Sync", 12, PK), ("Hdr", 4, VI), ("User data (2,048 bytes)", 2048, IN), ("EDC", 4, OR), ("", 8, MU), ("ECC (276)", 276, GR)], "Mode 1")
    row(.4, [("Sync", 12, PK), ("Hdr", 4, VI), ("User data (2,336 bytes)", 2336, "#7c85ff")], "Mode 2")
    ax.text(1176, 1.15, "Sync 12 · Header 4 · EDC 4 · reserved 8", ha="center", color=MU, fontsize=9.5)
    ax.text(1176, -.35, "Every sector is 2,352 bytes; 75 sectors per second", ha="center", color=MU, fontsize=11)
    ax.set_xlim(-330, 2352)
    add(6, "cd-rom", "end", "Sector layout: CD-DA vs CD-ROM modes", svg(f), "Mode 1 adds error detection/correction (EDC/ECC) for computer data (2,048 user bytes). Mode 2 keeps 2,336 user bytes for audio/video.")

    f = fig(10, 3.9); ax = f.add_subplot()
    cfg = [("CD", .65, IN), ("DVD-5\n1 layer", 4.7, VI), ("DVD-9\n2 layers", 8.5, PK), ("DVD-10\n2 sides", 9.4, CY), ("DVD-18\n2 sides, 2 layers", 17.0, OR)]
    b = ax.bar(range(len(cfg)), [c[1] for c in cfg], color=[c[2] for c in cfg], width=.6)
    for r, c in zip(b, cfg): ax.text(r.get_x() + r.get_width() / 2, r.get_height() + .3, f"{c[1]} GB", ha="center", fontweight="bold")
    ax.set_xticks(range(len(cfg))); ax.set_xticklabels([c[0] for c in cfg], fontsize=10); ax.set_ylabel("capacity (GB)"); ax.grid(axis="y", alpha=.4); ax.set_axisbelow(True)
    add(6, "video-disks", "end", "Capacity ladder: CD to DVD", svg(f), "Shorter laser wavelength and a tighter track pitch (0.74 µm vs 1.6 µm) give DVD about 7× the capacity of a CD.")
u6()

# ======================= UNIT 7 =======================
def sim(tasks, policy, horizon):
    """tasks: list of (name, C, P). Unit-step simulation; returns slots[t]=name|None, misses."""
    rem = {n: 0 for n, _, _ in tasks}; dl = {}; slots = []; misses = []
    for t in range(horizon):
        for n, c, p in tasks:
            if t % p == 0:
                if rem[n] > 0: misses.append((n, t))
                rem[n] = c; dl[n] = t + p
        ready = [n for n, c, p in tasks if rem[n] > 0]
        if not ready: slots.append(None); continue
        if policy == "EDF": pick = min(ready, key=lambda n: (dl[n], n))
        else: pick = min(ready, key=lambda n: [p for nn, c, p in tasks if nn == n][0])
        rem[pick] -= 1; slots.append(pick)
        for n, c, p in tasks:
            if rem[n] > 0 and dl[n] == t + 1 and n != pick: pass
        for n in list(rem):
            if rem[n] > 0 and dl[n] == t + 1: misses.append((n, t + 1)); rem[n] = 0
    return slots, misses

def u7():
    tasks = [("T1", 2, 5), ("T2", 4, 7)]; H = 14
    f = fig(10, 4.4)
    for k, pol in enumerate(["RM", "EDF"]):
        ax = f.add_subplot(2, 1, k + 1); slots, miss = sim(tasks, pol, H)
        for t, n in enumerate(slots):
            if n: ax.add_patch(Rectangle((t, 0 if n == "T1" else 1), 1, .8, fc=IN if n == "T1" else PK, ec="#0b0d1c"))
        for n, c, p in tasks:
            for r in range(0, H + 1, p): ax.plot([r, r], [0 if n == "T1" else 1] * 1 + [0], "none")
        for t in range(0, H + 1, 5): ax.annotate("", xy=(t, .8), xytext=(t, 1.15), arrowprops=dict(arrowstyle="-", color=IN, lw=1)) if False else None
        for m_n, m_t in miss: ax.text(m_t, 2.1, "deadline\nmissed", ha="center", color="#f87171", fontsize=9, fontweight="bold"); ax.plot([m_t, m_t], [-.1, 1.9], color="#f87171", ls="--")
        ax.set_xlim(0, H); ax.set_ylim(-.3, 2.9); ax.set_yticks([.4, 1.4]); ax.set_yticklabels(["T1 (C=2,P=5)", "T2 (C=4,P=7)"], fontsize=9.5); ax.set_xticks(range(0, H + 1))
        ax.set_title(f"{pol}: {'static priority by period' if pol == 'RM' else 'earliest deadline first'}  →  {'MISS' if miss else 'all deadlines met'}", fontsize=11.5, color=("#f87171" if miss else GR), loc="left")
        for sp in ("left",): ax.spines[sp].set_visible(False)
    f.tight_layout()
    u = 2 / 5 + 4 / 7
    add(7, "scheduling", "end", "Same task set, two policies", svg(f), f"U = 2/5 + 4/7 = {u:.3f} ≤ 1, so EDF can schedule it; it exceeds the RM bound for n=2 (0.828), and here RM misses T2's first deadline at t = 7.")

    f = fig(10, 3.8); ax = f.add_subplot()
    n = np.arange(1, 21); b = n * (2 ** (1 / n) - 1)
    ax.plot(n, b, "-o", color=VI, lw=2.2, ms=5, label="RM sufficient bound  n(2^{1/n} − 1)"); ax.axhline(1.0, color=GR, lw=2, label="EDF bound (U ≤ 1)")
    ax.axhline(math.log(2), color=PK, ls="--", lw=1.4, label="limit ln 2 ≈ 0.693")
    ax.set_ylim(.6, 1.05); ax.set_xlabel("number of tasks n"); ax.set_ylabel("utilisation U"); ax.legend(frameon=False, fontsize=10, labelcolor=TX, loc="center right"); ax.grid(alpha=.3)
    add(7, "scheduling", "end", "Schedulability bounds", svg(f), "n=1: 1.000, n=2: 0.828, n=3: 0.780, → 0.693 as n grows. Above the RM bound a set may still pass an exact test; EDF is optimal up to U = 1.")
u7()

# ======================= UNIT 8 =======================
def u8():
    f = fig(10, 4); ax = f.add_subplot()
    t = np.linspace(0, 10, 500); b, r = 4, 1.2
    ax.plot(t, b + r * t, color=GR, lw=2.4, label="token-bucket envelope  b + r·t")
    ev = [(0, 3), (1, 2), (2.2, 1), (5, 4), (7.3, 3), (9, 2)]
    cum = 0; xs = [0]; ys = [0]
    for tt, sz in ev:
        xs += [tt, tt]; ys += [cum, cum + sz]; cum += sz
    xs.append(10); ys.append(cum)
    ax.plot(xs, ys, color=PK, lw=2.2, label="actual arrivals (cumulative bursts)")
    ax.legend(frameon=False, fontsize=10.5, labelcolor=TX, loc="upper left"); ax.set_xlabel("time"); ax.set_ylabel("data sent"); ax.grid(alpha=.3)
    ax.text(.15, b + .9, "burst allowance b", color=GR, fontsize=10.5); ax.text(7.7, b + r * 8.5 - 4.1, "average rate r", color=GR, fontsize=10.5, rotation=18)
    add(8, "qos", "end", "Traffic shaping with a token bucket", svg(f), "A flow conforms if its cumulative traffic never exceeds b + r·t: bursts up to b are allowed, the long-term rate is limited to r.")

    f, ax = blank(10, 3.8, (0, 32), (0, 3.8))
    ax.text(0, 3.45, "RTP fixed header (32-bit words)", fontweight="bold", fontsize=13)
    def seg(x0, w, y, t, c): ax.add_patch(Rectangle((x0, y), w, .75, fc="#1c2150", ec=c, lw=1.5)); ax.text(x0 + w / 2, y + .37, t, ha="center", va="center", fontsize=10.5)
    y = 2.3
    seg(0, 2, y, "V=2", IN); seg(2, 1, y, "P", IN); seg(3, 1, y, "X", IN); seg(4, 4, y, "CC", IN); seg(8, 1, y, "M", VI); seg(9, 7, y, "payload type", VI); seg(16, 16, y, "sequence number", PK)
    seg(0, 32, 1.4, "timestamp", CY); seg(0, 32, .5, "SSRC (synchronisation source identifier)", GR)
    for xx in (0, 8, 16, 24, 32): ax.text(xx, 3.15, str(xx), ha="center", color=MU, fontsize=8.5)
    add(8, "transport-subsystem", "end", "RTP header layout", svg(f), "Sequence numbers detect loss and reordering; timestamps let the receiver play media at the right time and measure jitter.")
u8()

# ======================= UNIT 9 =======================
def u9():
    f, ax = blank(10, 4.6, (0, 12), (0, 6))
    def n(x, y, t, c=IN, w=1.7): box(ax, x - w / 2, y - .3, w, .6, t, ec=c, fs=10.5)
    ax.text(.2, 5.6, "Document = hierarchy of elements (SGML / structured documents)", fontweight="bold", fontsize=12.5)
    n(6, 4.7, "<book>", VI); n(3, 3.5, "<chapter>", IN); n(9, 3.5, "<chapter>", IN)
    n(1.5, 2.3, "<title>", CY, 1.3); n(4, 2.3, "<section>", GR, 1.5); n(8, 2.3, "<title>", CY, 1.3); n(10.5, 2.3, "<section>", GR, 1.5)
    n(3, 1.1, "<para>", PK, 1.3); n(5, 1.1, "<figure>", OR, 1.3); n(10.5, 1.1, "<para>", PK, 1.3)
    for a, b in [((6, 4.4), (3, 3.8)), ((6, 4.4), (9, 3.8)), ((3, 3.2), (1.5, 2.6)), ((3, 3.2), (4, 2.6)), ((9, 3.2), (8, 2.6)), ((9, 3.2), (10.5, 2.6)), ((4, 2.0), (3, 1.4)), ((4, 2.0), (5, 1.4)), ((10.5, 2.0), (10.5, 1.4))]:
        ax.plot([a[0], b[0]], [a[1], b[1]], color=MU, lw=1.2)
    ax.text(.2, .25, "The DTD defines which elements are allowed and how they nest; content is separated from layout.", color=MU, fontsize=10.5)
    add(9, "sgml-oda-mheg", "start", "Logical structure of a document", svg(f))

    f, ax = blank(10, 4.4, (0, 12), (0, 5))
    pos = {"A": (2, 3.8), "B": (6, 4.2), "C": (10, 3.6), "D": (3.5, 1.3), "E": (8, 1.6)}
    for k, (x, y) in pos.items():
        ax.add_patch(Rectangle((x - .9, y - .55), 1.8, 1.1, fc="#27306b", ec=IN, lw=1.5)); ax.text(x, y + .15, f"Node {k}", ha="center", fontsize=11, fontweight="bold")
        ax.text(x, y - .25, "text / image / audio", ha="center", fontsize=8, color=MU)
    ax.plot(pos["A"][0] + .4, pos["A"][1] - .3, "o", color=PK, ms=6)
    def edge(p, q):
        dx, dy = q[0] - p[0], q[1] - p[1]
        t = min(.9 / abs(dx) if dx else 9, .55 / abs(dy) if dy else 9)
        return (p[0] + dx * t * 1.12, p[1] + dy * t * 1.12)
    for a, b, lab in [("A", "B", "link"), ("B", "C", "link"), ("A", "D", "link"), ("B", "E", "link"), ("D", "E", "link")]:
        arrow(ax, edge(pos[a], pos[b]), edge(pos[b], pos[a]), c=VI, lw=1.6)
    ax.text(.2, 4.7, "Hypertext/hypermedia = nodes + links + anchors", fontweight="bold", fontsize=12.5)
    ax.text(.2, .3, "Pink dot = anchor (the active spot inside a node). Following a link moves you to another node, so reading order is chosen by the reader.", color=MU, fontsize=10)
    add(9, "hypertext", "end", "Nodes, anchors and links", svg(f))
u9()

# ======================= UNIT 10 =======================
def u10():
    f = fig(10, 3.6); ax = f.add_subplot()
    ax.axvspan(-80, 80, color=GR, alpha=.25); ax.text(0, .55, "in sync\n(±80 ms)", ha="center", color=GR, fontweight="bold")
    ax.axvspan(-300, -80, color=OR, alpha=.18); ax.axvspan(80, 300, color=OR, alpha=.18)
    ax.text(-190, .55, "audio behind video\nnoticeable", ha="center", color=OR, fontsize=10.5); ax.text(190, .55, "audio ahead of video\nnoticeable", ha="center", color=OR, fontsize=10.5)
    ax.set_xlim(-300, 300); ax.set_ylim(0, 1); ax.set_yticks([]); ax.set_xlabel("audio–video skew (ms)")
    for sp in ("left",): ax.spines[sp].set_visible(False)
    add(10, "presentation-requirements", "end", "Lip synchronisation tolerance", svg(f), "Skew between −80 ms (audio behind) and +80 ms (audio ahead) is generally unnoticed.")

    f, ax = blank(10, 4.8, (0, 12), (-.6, 5.2))
    ax.text(.1, 4.85, "Temporal relations between media objects on a timeline", fontweight="bold", fontsize=12.5)
    rows = [("Video", 0, 8, PK), ("Audio narration", 0, 8, CY), ("Slide 1", 0, 4, IN), ("Slide 2", 4, 8, VI), ("Subtitle", 2, 6, GR)]
    for i, (n, a, b, c) in enumerate(rows):
        y = 3.9 - i * .8
        ax.add_patch(Rectangle((2.6 + a, y), b - a, .55, fc=c, ec="#0b0d1c", alpha=.85)); ax.text(2.4, y + .27, n, ha="right", va="center", fontsize=10.5)
    for tck in range(0, 9): ax.plot([2.6 + tck] * 2, [.05, .2], color=MU)
    arrow(ax, (2.6, .35), (11.4, .35), c=MU); ax.text(11.5, .35, "t", color=MU, va="center")
    ax.text(2.6, -.35, "Video & audio: equal (inter-stream sync) · Slide 2 starts when Slide 1 ends (meets) · Subtitle overlaps both slides", color=MU, fontsize=9.5)
    add(10, "notion", "end", "Synchronisation as a timeline", svg(f), "Intra-object sync keeps one stream smooth; inter-object sync keeps different objects in the right temporal relation.")
u10()

# ======================= UNIT 11 =======================
def u11():
    f, ax = blank(10, 5.2, (0, 10), (0, 5.4))
    L = [("Applications", PK), ("Object-oriented approach: class hierarchy", VI), ("Higher programming language: media as types", IN), ("Toolkit: uniform interface, hides process structure", "#38bdf8"), ("System software: OS device driver + RM/EDF scheduler", CY), ("Library: functions per device", GR), ("Device: separate component with its own driver", OR)]
    for i, (t, c) in enumerate(L):
        ax.add_patch(FancyBboxPatch((.5, 4.55 - i * .68), 8.9, .56, boxstyle="round,pad=0,rounding_size=.1", fc="#1c2150", ec=c, lw=1.8))
        ax.text(5, 4.83 - i * .68, t, ha="center", va="center", fontsize=11.5)
    arrow(ax, (9.75, .3), (9.75, 5.1), c=MU); ax.text(9.9, 2.7, "more abstract", rotation=90, color=MU, va="center", fontsize=10)
    add(11, "abstraction-levels", "end", "Layers of abstraction for multimedia programming", svg(f), "Higher layers hide device and timing detail so programmers can work with media objects instead of raw hardware.")
u11()

# ======================= UNIT 12 =======================
def u12():
    f, ax = blank(10, 4.4, (0, 12), (0, 5))
    ax.text(.2, 4.7, "Multimedia development cycle", fontweight="bold", fontsize=13)
    steps = [("1 Plan\n& cost", IN), ("2 Design\n(storyboard, UI)", VI), ("3 Develop\n& produce", PK), ("4 Test\n& debug", OR), ("5 Deliver", GR)]
    for i, (t, c) in enumerate(steps):
        box(ax, .3 + i * 2.3, 2.2, 1.9, 1.3, t, ec=c, fs=11.5, bold=True)
        if i < 4: arrow(ax, (2.25 + i * 2.3, 2.85), (2.6 + i * 2.3, 2.85), c=MU)
    ax.add_patch(FancyArrowPatch((11.2, 2.1), (1.2, 2.1), connectionstyle="arc3,rad=-.22", arrowstyle="-|>", mutation_scale=14, color=MU, lw=1.4, ls="--"))
    ax.text(6.2, .3, "iterate: feedback from testing and users returns to design", ha="center", color=MU, fontsize=11)
    add(12, "development-cycle", "start", "The cycle at a glance", svg(f))
u12()
