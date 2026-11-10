# Unit 6: Practice Questions

Write your own answer on paper first, then click to reveal the model answer. Marks are a guide to how much detail the question deserves.

## Short answer

??? question "1. How is information stored on a CD? (4 marks)"
    In a **spiral track** of **pits and lands** in the substrate. A **transition** (pit to land or land to pit) is a **1**; between transitions there are **0s**. The laser is reflected almost totally by lands and scattered by pits.

??? question "2. Name the three layers of a CD. (3 marks)"
    Transparent **substrate** (polycarbonate with pits and lands), **reflective layer** (aluminium), **protective layer** (with label).

??? question "3. List four advantages of optical storage. (4 marks)"
    High data density (16,000 tpi against 96 tpi of a floppy), long-term storage (surface out of focus, dust and scratches insensitive), low probability of head crashes (distance > 1 mm), adequate error correction; each disc equals the master.

??? question "4. Calculate the audio data rate and the capacity of CD-DA. (4 marks)"
    44,100 × 16 × 2 = **1,411,200 bit/s (176.4 KB/s)**. 74 × 60 × 1,411,200 = 6,265,728,000 bits = **about 747 MB**.

??? question "5. Why is EFM used and what does it do? (4 marks)"
    Laser resolution needs at least two 0s between 1s; clock recovery needs at most ten 0s. EFM codes 8 data bits into **14 channel bits** (256 of the 267 valid patterns) and 3 merging bits are added between codewords.

??? question "6. What is CIRC? (4 marks)"
    Cross Interleaved Reed-Solomon Code: two-level Reed-Solomon coding at byte level (4 correction bytes per 24 data bytes) plus interleaving over adjacent frames, so bursts up to 4,000 bits (2.5 mm) are corrected and up to 12,300 bits (7 mm) interpolated.

??? question "7. Describe a CD-DA frame. (4 marks)"
    24 audio bytes (2 × 12), 8 parity bytes (2 × 4), 1 control and display byte, plus a 27-bit sync pattern; 588 channel bits in all.

??? question "8. Name the three data streams of CD-DA with their rates. (3 marks)"
    Audio 1.41 Mbit/s; data 1.94 Mbit/s; channel 4.32 Mbit/s.

??? question "9. What are lead-in, program and lead-out areas and index points? (4 marks)"
    Lead-in: table of contents and track starts. Program: up to 99 tracks. Lead-out: controlled exit. IP0 = start of track, IP1 = start of audio; between them the pregap.

??? question "10. Why is CD-DA unsuitable for computer data? (2 marks)"
    The error rate is too high for discrete data, and the scheme was not designed for video; blocks are needed for random access.

??? question "11. Compare CD-ROM mode 1 and mode 2. (5 marks)"
    Mode 1: 2,048 user bytes + EDC 4 + ECC 276 + 8 blank; error rate 10⁻¹²; 650 MB; 150 KB/s; any data. Mode 2: 2,336 user bytes, no EDC/ECC; 741.85 MB; 171 KB/s; compressed audio and video.

??? question "12. Calculate bytes per block and blocks per CD. (3 marks)"
    1,411,200 ÷ 75 ÷ 8 = **2,352 bytes**; 74 × 60 × 75 = **333,000 blocks**.

??? question "13. What is ISO 9660? (3 marks)"
    The logical file format for CD-ROM (from the High Sierra proposal): directory tree, path table, file interleaving, 16-block system area, primary volume descriptor, logical block 512–2,048 bytes.

??? question "14. Explain CD-ROM/XA Form 1 and Form 2. (4 marks)"
    Both mode 2 with an 8-byte subheader. Form 1: 2,048 user bytes + EDC + ECC, for text and programs. Form 2: 2,324 user bytes + EDC only, for compressed audio/video, 13 % more data.

??? question "15. State two drawbacks of CD-ROM/XA. (2 marks)"
    Compression only referenced (MPEG audio not compatible); special disc layout and complex application development.

??? question "16. What is a bridge disc? Give an example. (3 marks)"
    Playable in CD-ROM/XA and CD-I players; all data in mode 2, no CD-I tracks in the TOC. Example: Photo CD.

??? question "17. Differentiate regular and hybrid CD-WO. (3 marks)"
    Regular: one session. Hybrid: several sessions (max 99); pre-1992 players read only the first.

## Long answer

??? question "18. Compare CD and DVD. (8 marks)"
    Use the table in [Video Disks](video-disks.md): wavelength 780 nm vs 650/635 nm; track pitch 1.6 vs 0.74 µm; min pit 0.83 vs 0.4 µm; layers and sides; capacity 650 MB vs 4.7/8.5/9.4 GB; MPEG-1 vs MPEG-2; sound; subtitles.

??? question "19. Explain Laser Vision. (4 marks)"
    Video and audio, analogue, frequency modulation, no quantization of pit length, about 30 cm, 2.6 GB; from VLP (1973).

??? question "20. Briefly describe Blu-ray. (4 marks)"
    405 nm blue-violet laser, track pitch 0.32 µm, 25/50 GB, HD video. *(Beyond the lecturer's notes.)*

??? question "21. Explain the principle of CD-WO and CD-MO. (8 marks)"
    See [CD-WO and CD-MO](cd-wo-and-cd-mo.md): pre-groove, absorption layer, irreversible heating, sessions; MO write, erase, read; premastered and rewritable areas; incompatibility.

??? question "22. Explain the structure of CD-I and the CD-I audio levels. (6 marks)"
    Green Book system with CD-RTOS and decoder; levels A, B, C with sampling, coding, S/N, playing time (table in [CD-I](cd-i-and-photo-cd.md)).

??? question "23. Explain Photo CD and ImagePac. (5 marks)"
    Kodak/Philips, bridge disc on CD-WO, 8-bit Y and Cb/Cr, ImagePac with five resolutions (hierarchical), 3–6 MB per photo.

## Multiple choice

??? question "24. In CD-DA the sampling rate and quantization are"
    - A. 22.05 kHz, 8 bit
    - B. 44.1 kHz, 16 bit
    - C. 48 kHz, 24 bit
    - D. 44.1 kHz, 8 bit

    **Answer: B.**

??? question "25. User bytes in a CD-ROM mode 1 block"
    - A. 2,352
    - B. 2,336
    - C. 2,048
    - D. 2,324

    **Answer: C.**

??? question "26. Which Book defines CD-ROM?"
    - A. Red
    - B. Yellow
    - C. Green
    - D. Orange

    **Answer: B.**

??? question "27. EFM converts"
    - A. 8 bits into 14 bits
    - B. 14 bits into 8 bits
    - C. 16 bits into 24 bits
    - D. 4 bits into 8 bits

    **Answer: A.**

??? question "28. The maximum number of sessions on a CD-WO is"
    - A. 9
    - B. 50
    - C. 99
    - D. 255

    **Answer: C.**

??? question "29. A DVD single-layer, single-sided disc holds about"
    - A. 650 MB
    - B. 4.7 GB
    - C. 8.5 GB
    - D. 25 GB

    **Answer: B.**
