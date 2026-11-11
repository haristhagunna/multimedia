# Mock Exam 1: Practice Questions

<div class="mock-timer" data-minutes="120" data-total="60"></div>

**Full marks: 60 · Time: 2 hours · Attempt all questions.** Start the timer, write your answers on paper, then open each question to check the model answer and marking scheme. Be honest with yourself: award marks only for points you actually wrote.

!!! tip "How to use this paper"
    1. Press **Start** and work without notes.
    2. Section A is auto-marked when you tap an option.
    3. For Sections B and C, compare with the **marking scheme** and tick the marks you earned in the scorer at the bottom.

## Section A: Multiple choice (10 × 1 = 10 marks)

??? question "A1. The minimum sampling rate needed to capture a 20 kHz signal without aliasing is"
    - A. 10 kHz
    - B. 20 kHz
    - C. 40 kHz
    - D. 44.1 kHz only

    **Answer: C.** Nyquist: f<sub>s</sub> ≥ 2 f<sub>max</sub> = 40 kHz (CD uses 44.1 kHz to leave a safety margin).

??? question "A2. The data rate of CD-DA audio is"
    - A. 64 kbit/s
    - B. 705.6 kbit/s
    - C. 1,411.2 kbit/s
    - D. 2,822.4 kbit/s

    **Answer: C.** 44,100 × 16 × 2 = 1,411,200 bit/s.

??? question "A3. Which of the following is a lossy technique?"
    - A. Run-length coding
    - B. Huffman coding
    - C. Quantization in JPEG
    - D. Arithmetic coding

    **Answer: C.** Quantization discards information; the others are entropy (lossless) coders.

??? question "A4. In a Huffman code, the prefix property means"
    - A. All codewords have equal length
    - B. No codeword is a prefix of another
    - C. The most frequent symbol has the longest code
    - D. Codes must be sorted alphabetically

    **Answer: B.** This makes decoding unambiguous without separators.

??? question "A5. Which colour model separates brightness from colour?"
    - A. RGB
    - B. YUV
    - C. CMY
    - D. Indexed colour

    **Answer: B.** Y carries luminance; U and V carry colour differences.

??? question "A6. Which scheduling algorithm assigns priorities from the period (shorter period = higher priority)?"
    - A. EDF
    - B. Round robin
    - C. Rate monotonic
    - D. FCFS

    **Answer: C.** Rate monotonic uses static priorities derived from the period.

??? question "A7. A DVD uses a laser of wavelength about"
    - A. 780 nm (infrared)
    - B. 650 nm (red)
    - C. 405 nm (blue-violet)
    - D. 1,550 nm

    **Answer: B.** CD 780 nm, DVD 650 nm, Blu-ray 405 nm; shorter wavelength means smaller pits and higher capacity.

??? question "A8. In MPEG, a B-frame is predicted from"
    - A. Nothing, it is intra coded
    - B. A previous frame only
    - C. Both a past and a future reference frame
    - D. A random frame

    **Answer: C.** B-frames are bidirectionally predicted, which gives the highest compression.

??? question "A9. The allowed audio-video skew for lip synchronization is about"
    - A. ±8 ms
    - B. ±80 ms
    - C. ±800 ms
    - D. ±8 s

    **Answer: B.**

??? question "A10. Which is NOT a lossless compression method?"
    - A. Huffman
    - B. RLE
    - C. JPEG (baseline DCT)
    - D. LZW

    **Answer: C.** Baseline JPEG is lossy because of quantization.

## Section B: Short answers (6 × 5 = 30 marks)

??? question "B1. Define multimedia and list its main characteristics. (5 marks)"
    **Marking scheme**

    - Definition: a system/application that integrates **several media** (text, graphics, images, audio, video) under computer control. **(1)**
    - Computer-controlled, **integrated** (a common digital representation). **(1)**
    - Includes at least one **continuous (time-dependent) medium** such as audio or video. **(1)**
    - **Independent**/interactive use of media; supports **synchronization**. **(1)**
    - Examples (education, video conferencing, games). **(1)**

??? question "B2. Calculate the storage for 1 minute of CD-quality stereo audio (44.1 kHz, 16-bit). (5 marks)"
    **Marking scheme**

    - Formula: size = f<sub>s</sub> × bits × channels × time / 8. **(1)**
    - Substitution: 44,100 × 16 × 2 × 60 / 8. **(2)**
    - Result: **10,584,000 bytes ≈ 10.58 MB (≈ 10.09 MiB)**. **(1)**
    - Unit handled correctly (bits → bytes). **(1)**

??? question "B3. Explain the stages of JPEG baseline compression. (5 marks)"
    **Marking scheme**

    - Colour conversion/downsampling and split into **8 × 8 blocks**. **(1)**
    - **DCT** of each block (moves energy to a few low-frequency coefficients). **(1)**
    - **Quantization**: divide by table value and round; the **only lossy step**. **(1)**
    - **Zigzag** scan to group zeros; **DC** coefficients coded by differences (DPCM). **(1)**
    - **Run-length + entropy (Huffman)** coding of the AC coefficients. **(1)**

??? question "B4. Build a Huffman code for A:45, B:13, C:12, D:16, E:9, F:5 and find the average code length. (5 marks)"
    **Marking scheme**

    - Merge the two smallest repeatedly: F+E = 14; C+B = 25; 14+D = 30; 25+30 = 55; 45+55 = 100. **(2)**
    - A valid prefix code, e.g. **A = 0, C = 100, B = 101, D = 111, F = 1100, E = 1101**. **(1)**
    - Total bits = 45·1 + 12·3 + 13·3 + 16·3 + 5·4 + 9·4 = **224** for 100 symbols. **(1)**
    - Average = **2.24 bits/symbol** (against 3 bits fixed length). **(1)**

    Different tie-breaking can give different codes, but the **total of 224 bits** must agree.

??? question "B5. Distinguish soft and hard real-time with examples, and state why multimedia needs real-time scheduling. (5 marks)"
    **Marking scheme**

    - **Hard**: missing a deadline is a failure with serious consequences (airbag, flight control). **(1.5)**
    - **Soft**: occasional misses degrade quality but are tolerable (video playback, audio streaming). **(1.5)**
    - Continuous media have **periodic deadlines**; a late frame or sample is useless or audible/visible. **(1)**
    - A conventional OS gives fairness, not timing guarantees, hence EDF/RM scheduling and resource reservation. **(1)**

??? question "B6. Explain the difference between a CD-DA and a CD-ROM sector. (5 marks)"
    **Marking scheme**

    - Both use a raw block of **2,352 bytes**. **(1)**
    - CD-DA: all 2,352 bytes are audio; error handling by CIRC and interpolation. **(1.5)**
    - CD-ROM Mode 1: header + **2,048 bytes user data** + **EDC/ECC** for exact data integrity. **(1.5)**
    - Reason: audio tolerates small errors, computer data does not. **(1)**

## Section C: Long answers (2 × 10 = 20 marks)

??? question "C1. Explain sampling and quantization of audio. A voice signal has a bandwidth of 4 kHz; find the sampling rate and the data rate if 8 bits per sample are used. Discuss aliasing and how to prevent it. (10 marks)"
    **Marking scheme**

    - Sampling = measuring amplitude at regular time intervals; quantization = rounding each sample to one of 2<sup>n</sup> levels; coding = binary representation. **(2)**
    - **Nyquist theorem** f<sub>s</sub> ≥ 2 f<sub>max</sub>. **(1)**
    - Sampling rate = 2 × 4 kHz = **8 kHz**. **(1)**
    - Data rate = 8,000 × 8 = **64 kbit/s** (telephone PCM). **(2)**
    - Aliasing: if f<sub>s</sub> is too low, high frequencies appear as false low frequencies. **(1)**
    - Prevention: **low-pass (anti-aliasing) filter** before the ADC, or raise f<sub>s</sub>. **(1)**
    - Quantization error/noise, more bits = more levels = better SNR; a labelled sketch. **(2)**

??? question "C2. Define EDF and rate-monotonic scheduling. For tasks T1 (C = 2, P = 5) and T2 (C = 4, P = 7) test schedulability by both. (10 marks)"
    **Marking scheme**

    - EDF: dynamic priority; the task with the **earliest absolute deadline** runs first. **(1.5)**
    - RM: **static** priority; shorter period, higher priority. **(1.5)**
    - Utilization U = 2/5 + 4/7 = 0.4 + 0.571 = **0.971**. **(2)**
    - EDF (D = P): schedulable if **U ≤ 1** → **yes**. **(1.5)**
    - RM bound for 2 tasks: 2(2<sup>1/2</sup> − 1) = **0.828**; U exceeds it, so the bound test fails. **(1.5)**
    - Timeline: T1 runs 0–2, T2 runs 2–5 (3 units), T1 again at 5–7, so T2 has only 3 of 4 units by its deadline at 7 → **misses**. RM **not** schedulable. **(2)**

    Mock 1 mirrors the style of previous years: one numerical, one derivation, the rest explanation.

<div class="mock-scorer" data-total="60"></div>
