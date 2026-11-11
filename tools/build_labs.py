"""Assemble lab pages; code blocks are embedded from docs/labs/code (each file is tested)."""
import pathlib
code = lambda n: pathlib.Path(f"docs/labs/code/{n}").read_text().rstrip()
def dl(n): return f'<p><a class="btn-s" href="code/{n}" download>Download {n}</a></p>'
P = {}
P["index.md"] = """# Labs

Hands-on practice. Each lab has a short aim, steps, **expected results** (so you can check yourself) and reflection questions. Python labs need only Python 3 (labs 1 and 4 also need numpy); every script was run and the outputs shown are real.

| Lab | Tool | Units |
|---|---|---|
| [1. Sampling and aliasing](lab-sampling.md) | Python + Audacity | 2 |
| [2. Images and colour](lab-images.md) | GIMP | 3, 4 |
| [3. Audio and video with FFmpeg](lab-ffmpeg.md) | FFmpeg | 2, 4, 5 |
| [4. Huffman and run-length coding](lab-huffman.md) | Python | 5 |
| [5. JPEG's DCT and quantization](lab-dct.md) | Python + numpy | 5 |
| [6. Real-time scheduling](lab-scheduler.md) | Python | 7 |
| [7. Synchronization drift](lab-sync.md) | Python | 10 |

Prefer the browser? Use the [interactive simulators](simulators.md).
"""
P["lab-sampling.md"] = f"""# Lab 1: Sampling, quantization and aliasing

**Aim.** See Nyquist in action and measure how bit depth affects noise.

## Part A: Python

{dl('sampling.py')}

```python
{code('sampling.py')}
```

**Expected output**

```text
1000 Hz sampled at 8000 Hz appears as 1000 Hz
3000 Hz sampled at 8000 Hz appears as 3000 Hz
5000 Hz sampled at 8000 Hz appears as 3000 Hz
7000 Hz sampled at 8000 Hz appears as 1000 Hz
 4 bits: SNR =  25.1 dB
 8 bits: SNR =  51.0 dB
12 bits: SNR =  74.1 dB
16 bits: SNR =  98.2 dB
CD audio, 1 minute: 10584000 bytes
```

The SNR rises about **6 dB per bit**, which is why 16-bit audio has a dynamic range near 98 dB.

## Part B: Audacity

1. Open Audacity, **Generate → Tone** (sine, 5000 Hz, 2 s) with project rate 8000 Hz. Listen: you hear **3000 Hz**, not 5000 Hz.
2. Open `alias_5k.wav` (made by the script) and `tone_1k.wav`; compare them with **View → Show Spectrogram**.
3. Change the project rate to 44100 Hz and regenerate the 5 kHz tone; the alias disappears.

## Reflect

1. Why does the CD use 44.1 kHz and not exactly 40 kHz?
2. What would an anti-aliasing filter do before the ADC?
3. Which bit depth gives at least 90 dB SNR?
"""
P["lab-images.md"] = """# Lab 2: Images, colour depth and YUV (GIMP)

**Aim.** Connect image size, colour depth and dithering to the formulas in Units 3 and 4.

## Steps

1. Open a photograph in GIMP. Read **Image → Scale Image** to note width × height.
2. Compute the uncompressed size: width × height × 3 bytes (24-bit). Compare with the file size on disk and state the compression ratio.
3. **Image → Mode → Indexed…** choose 16 colours, first with **no dithering**, then **Floyd-Steinberg**. Zoom to 400 % and compare banding versus noise.
4. **Colors → Components → Decompose…** choose **YCbCr_ITU_R470**. Look at the Y layer (the brightness) and the two colour layers; note that Y alone is a usable greyscale picture.
5. Export as JPEG at quality 90, 50 and 10. Record file sizes and describe the 8 × 8 block artefacts at 10.

## Record your results

| Setting | File size | Observation |
|---|---|---|
| PNG (lossless) | | |
| JPEG 90 | | |
| JPEG 50 | | |
| JPEG 10 | | |
| Indexed 16, no dither | | |
| Indexed 16, Floyd-Steinberg | | |

## Reflect

1. Why does the Y layer look sharp while Cb and Cr look blurry and still give a good picture? (Chroma subsampling.)
2. Which setting gives the best quality per byte for *this* photograph?
"""
P["lab-ffmpeg.md"] = """# Lab 3: Audio and video with FFmpeg

**Aim.** Measure how sampling rate, channels and codecs change size. All commands were run and the sizes below are from a 3-second 440 Hz test tone (yours will differ for your own files).

## Audio

```bash
# 1. make a test tone (3 s, 44.1 kHz stereo)
ffmpeg -f lavfi -i "sine=frequency=440:duration=3" -ar 44100 -ac 2 a.wav
# 2. reduce to telephone quality: 8 kHz mono
ffmpeg -i a.wav -ar 8000 -ac 1 a8k.wav
# 3. lossy compression to MP3 at 128 kbit/s
ffmpeg -i a.wav -c:a libmp3lame -b:a 128k a.mp3
```

| File | Size | Check by formula |
|---|---|---|
| a.wav | 529,278 bytes | 44,100 × 2 B × 2 ch × 3 s = 529,200 + header |
| a8k.wav | 48,078 bytes | 8,000 × 2 B × 1 ch × 3 s = 48,000 + header |
| a.mp3 | 48,945 bytes | 128 kbit/s × 3 s / 8 = 48,000 + header |

Headers account for the few extra bytes. Notice that a 128 kbit/s MP3 is about **11 times smaller** than the 1,411 kbit/s WAV.

## Video

```bash
# 1. test video 640x480, 25 fps, 2 s
ffmpeg -f lavfi -i testsrc=size=640x480:rate=25:duration=2 -c:v libx264 -crf 23 v.mp4
# 2. smaller frame, lower frame rate, stronger compression
ffmpeg -i v.mp4 -vf scale=320:240 -r 12 -c:v libx264 -crf 30 v_small.mp4
# 3. inspect
ffprobe -v error -show_entries stream=codec_name,width,height,r_frame_rate -of default=nw=1 v.mp4
# 4. extract the I-frames
ffmpeg -i v.mp4 -vf "select=eq(pict_type\\,I)" -vsync vfr i%d.png
```

Compute the **raw** size of the 2-second 640 × 480 × 24-bit × 25 fps clip (= 46,080,000 bytes) and compare with the 17 KB H.264 file. That ratio is why compression matters.

## Reflect

1. Which steps were lossy? Which were lossless?
2. Why do I-frames matter for random access in MPEG-style video?
"""
P["lab-huffman.md"] = f"""# Lab 4: Huffman and run-length coding

**Aim.** Build Huffman codes by program, confirm the exam answer **224 bits**, and see when RLE expands data.

{dl('huffman.py')}

```python
{code('huffman.py')}
```

**Expected output**

```text
A 45 0
B 13 101
C 12 100
D 16 111
E 9 1101
F 5 1100
total bits 224 average 2.24
aaabccdddd -> a3b1c2d4
abcd -> a1b1c1d1 (RLE can expand data)
abracadabra Huffman bits: 23 vs 88 ASCII bits
```

Tie-breaking may give different codes in your own runs, but the **total bit count must match**.

## Try it

1. Change the frequencies to all equal (10 each). What happens to the average length?
2. Encode your own name; compare Huffman bits with 8 bits per character.
3. Find a string where RLE makes the output longer.
"""
P["lab-dct.md"] = f"""# Lab 5: The DCT and quantization in JPEG

**Aim.** Verify that the DCT is reversible and that quantization is where information is lost.

{dl('dct.py')}

```python
{code('dct.py')}
```

**Expected output**

```text
non-zero coefficients after quantization: 6 of 64
zigzag: [13, 6, -7, -5, 0, 1, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0] ...
max reconstruction error: 4.5
DCT alone is reversible: True
```

## Try it

1. Multiply `Q` by 4 (coarser quantization). How do the non-zero count and the error change?
2. Replace the smooth block with random noise. What happens to the number of non-zero coefficients? (Noisy blocks compress badly.)
3. Why does the zigzag list end in long runs of zeros, and why is that good for run-length coding?
"""
P["lab-scheduler.md"] = f"""# Lab 6: EDF and rate-monotonic scheduling

**Aim.** Reproduce the two classic timelines and discover why the RM utilization bound is only *sufficient*.

{dl('scheduler.py')}

```python
{code('scheduler.py')}
```

**Expected output (first rows)**

```text
tasks [(2, 5), (4, 7)]  U = 0.971  RM bound = 0.828
  EDF: ...   missed: none
  RM:  ...   missed: [('T2', 7)]
tasks [(1, 4), (2, 6), (3, 12)]  U = 0.833  RM bound = 0.780
  EDF: T1 T2 T2 T3 T1 T3 T2 T2 T1 T3 -- --   missed: none
  RM: T1 T2 T2 T3 T1 T3 T2 T2 T1 T3 -- --   missed: none
```

## Try it

1. Search for a task set with U ≤ 1 where RM misses and EDF does not.
2. Add a task with U > 1. What happens to EDF?
3. Why is the second set schedulable by RM even though U exceeds the bound?
"""
P["lab-sync.md"] = f"""# Lab 7: Clock drift and lip sync

**Aim.** Quantify how a tiny clock error breaks synchronization.

{dl('sync.py')}

```python
{code('sync.py')}
```

**Expected output**

```text
0.1% fast for 10 min -> 0.60 s drift
0.05% fast for 20 min -> 0.60 s drift
limit reached after 80.0 s
0.1% error: limit after 80 s
0.01% error: limit after 800 s
0.001% error: limit after 8000 s
```

A 0.1 % error exceeds the ±80 ms lip-sync limit after only 80 seconds. This is why players adapt buffering and use RTCP/time stamps to resynchronize.
"""
for n, t in P.items(): pathlib.Path("docs/labs/" + n).write_text(t)
print(len(P), "lab pages")
