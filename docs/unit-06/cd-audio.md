# CD Audio (CD-DA)

!!! source "Source"
    *Unit 6 – cd* pp. 12–25; *Unit 6 – optical-storage-media* pp. 5–20.

## Characteristics

| Item | Value |
|---|---|
| Developed by | Philips and Sony (available **1983**) |
| Diameter | **120 mm** |
| Rotation | **Constant linear velocity (CLV)**: rotations per second depend on the head position |
| Track | One spiral, about **20,000 turns** (an LP has 850) |
| Sampling / quantization | **44,100 Hz, 16 bit**, **PCM**, stereo |
| Audio data rate | 44,100 × 16 × 2 = **1,411,200 bit/s = 176.4 KB/s** |
| S/N | about 6 dB per bit, 16 bit gives **98 dB** (LP/tape 50–60 dB) |
| Playing time | maximum **74 min** |
| Capacity (no error correction) | 74 × 60 × 1,411,200 = **6,265,728,000 bit ≈ 747 MB** |

Pit and land lengths are **multiples of 0.3 µm**.

!!! example "Check"
    6,265,728,000 ÷ 8 = 783,216,000 bytes; ÷ 1,048,576 = **746.9 MB**.

## Eight-to-Fourteen Modulation (EFM)

**Why a special code?**

- The laser has limited resolution: transitions cannot be too close, so **at least two 0s between two 1s**.
- The clock is recovered from the transitions: **not more than 10 consecutive 0s**.

**EFM:** each **8-bit** value is coded with **14 bits**. 267 fourteen-bit patterns satisfy the rules and **256 are used** (those cheapest to implement in gates).

When 14-bit values are concatenated the rules could be broken, so **three merging bits** are added between them. Each byte therefore uses **17 channel bits** (14 + 3).

!!! warning "Typo in the lecturer's example"
    The example shows "8 bit data 111101000 11100010", where the first value has 9 digits. It should be 8 bits. Study the **rule** (min 2 zeros, max 10 zeros, 3 merging bits) rather than the example.

## Error handling

Scratches, dust and fingerprints cause **burst errors**, which must be **detected and corrected**. Re-sending (ARQ) is impossible on a disc, so **forward error correction (FEC)** is used.

### CIRC: Cross Interleaved Reed-Solomon Code

Two levels:

1. **Reed-Solomon at byte level (EDC and ECC):** two groups, each with **4 correction bytes for 24 data bytes**. The first group corrects **single-byte** errors; the second corrects **double-byte** errors and **detects** further errors.
2. **Frame interleaving:** consecutive data bytes and their ECC bytes are **spread over adjacent frames**, turning a burst into scattered small errors.

Performance: error rate about **10⁻⁸** (about 1 bit in 100 million); bursts of **4,000 data bits (about 2.5 mm)** are corrected exactly; errors up to **12,300 data bits (about 7 mm)** are repaired by **interpolation**.

!!! warning "Arithmetic in the lecturer's slide"
    The slide multiplies 4,000 × 0.3 µm and writes "about 2.5 mm". The product is 1.2 mm; the **2.5 mm and 7 mm** figures are the usual quoted values. Learn the figures 4,000 bits/2.5 mm and 12,300 bits/7 mm.

!!! info "Beyond the slides: the theory the second file starts"
    - **Error detection** with a polynomial: treat data as A(x), divide by generator G(x), send the remainder; the receiver divides again. A **parity bit** (G(x) = x + 1) detects an odd number of errors but misses an even number.
    - **FEC** works by choosing codewords with large **Hamming distance**: if the minimum distance is 2t + 1, any error of t bits or fewer can be corrected.
    - **2-D parity** (row and column) can locate and correct a single error, but several errors can produce a wrong "correction".
    - For many receivers an **XOR** repair packet (c = a₁ ⊕ a₂ ⊕ … ⊕ aₙ) lets any receiver that lost one packet rebuild it.

## Frames

One **frame**:

| Part | Content |
|---|---|
| Audio data | 2 groups of 12 bytes (**24 bytes**) |
| Error detection/correction | 2 groups of 4 parity bytes (**8 bytes**, Reed-Solomon) |
| Control and display | **1 byte**; its bits are called P, Q, R, S, T, U, V, W; the same bit of 98 frames forms a **subchannel** (e.g. subchannel P marks audio versus data, Q holds the table of contents and time) |
| Synchronization pattern | 12 ones + 12 zeros + 3 merging bits = **27 bits**, a unique pattern marking the frame start |

Each frame has 24 + 8 + 1 = **33 bytes**, each coded in 17 bits = 561 bits, plus the 27-bit sync = **588 channel bits**.

## Three data streams

| Stream | Content | Rate |
|---|---|---|
| **Audio bit stream** | 16-bit stereo PCM, 44.1 kHz | **1.41 × 10⁶ bit/s** (1,411,200) |
| **Data bit stream** | audio + parity bytes + control and display byte | **1.94 × 10⁶ bit/s** |
| **Channel bit stream** | data + EFM + merging bits + sync | **4.32 × 10⁶ bit/s** |

!!! example "Check"
    Frames per second = 176,400 ÷ 24 = 7,350. Data: 7,350 × 33 × 8 = 1,940,400 bit/s. Channel: 7,350 × 588 = 4,321,800 bit/s.

## Areas and random access

- **Lead-in area:** table of contents, start of each track.
- **Program area:** up to **99 tracks**, typically one song per track.
- **Lead-out area:** lets the player leave the program area in a controlled way.
- **Index points:** **IP0** = start of track, **IP1** = start of audio data; the part between them is the **track pregap**.

## Summary and limits

CD-DA suits typical damage in audio and is the **base of the whole CD family**. But it was **not conceived for video** (different ECC/EDC needed) or **discrete data** (error rate too high), and does not allow simultaneous playback of several media.

!!! exam "Exam tip"
    Learn the three numbers 1,411,200 bit/s, 74 min ≈ 747 MB and 588 bits per frame, and the two EFM rules. CIRC is always "Reed-Solomon in two levels plus interleaving".

## Checkpoint

??? question "Why is EFM used?"
    To keep at least two and at most ten zeros between ones so the laser can resolve transitions and the clock can be recovered.

??? question "Why interleaving?"
    Burst errors hit consecutive bytes; spreading bytes over adjacent frames leaves only a few bytes in error per code word, which Reed-Solomon can correct.
