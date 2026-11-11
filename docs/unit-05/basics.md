# Basic Concepts and Coding Requirements

## Why compress?

- To **reduce the volume of data** to be transmitted.
- To **reduce the bandwidth** needed for transmission and the **storage requirement**.

**Data compression** is the process of **reducing the size of digital data** to optimise storage, transmission or processing. It works by **eliminating redundancy**, **removing irrelevant information** or **encoding data in the most compact form** while preserving usability.

## The storage problem

Uncompressed graphics, audio and video need considerable storage.

| Medium | Uncompressed requirement (from the notes) |
|---|---|
| Text | **2 bytes** for every 8 × 8 pixel character; in a 640 × 480 window that is 80 × 60 = 4,800 characters, about **9,600 bytes** |
| Bitmap, 256 colours | 1 byte/pixel; 640 × 480 = **307,200 bytes ≈ 300 KB** |
| CD-quality stereo audio | 44.1 kHz, 16 bits, 2 channels |
| Video | Frames × bitmap size (see [Unit 4](../unit-04/computer-video-format.md)) |

!!! example "Calculations"
    - Text: (640 ÷ 8) × (480 ÷ 8) = 80 × 60 = 4,800 characters × 2 bytes = **9,600 bytes**.
    - Audio: 44,100 × 16 × 2 = **1,411,200 bits/s ≈ 172 KB/s ≈ 10.1 MB per minute**.
    - Video: 640 × 480 × 8 bits × 25 fps = 61,440,000 bits/s ≈ **7.3 MB/s**.

It is also said that "90 % of raw audio can be deleted without affecting the quality". Treat this as an illustration of **irrelevance**: much of the signal cannot be heard.

## Coding requirements for multimedia

1. The **quality** of the compressed data should be **as good as possible**.
2. For cost-effective implementation, the **complexity** of the technique should be **minimal**.
3. The **processing time** of the algorithm must **not exceed a certain span** (real-time for continuous media).

!!! info "Extra"
    Textbooks add **dialogue-mode requirements** (end-to-end delay below about 150 ms; compression must be symmetric) and **retrieval-mode requirements** (fast forward/rewind, random access). They also define the **compression ratio = original size ÷ compressed size**. Example: 300 KB compressed to 30 KB is 10 : 1.

## Lossless and lossy

| | Lossless | Lossy |
|---|---|---|
| Decoded data | **Identical** to original | **Similar but not identical** |
| Typical methods | RLE, Huffman, arithmetic | JPEG, MPEG, MP3 |
| Use | Text, programs, medical images | Photos, audio, video |
| Ratio | Modest | High |

!!! exam "Exam tip"
    "Why is compression necessary for multimedia?" Answer with the 300 KB image, the 1.4 Mbit/s CD audio and the three requirements. Then name lossless vs lossy.

## Checkpoint

??? question "State three requirements on a multimedia compression technique."
    Best possible quality; minimal complexity for cost-effective implementation; processing time within a limit.

??? question "Calculate the storage of a 640 × 480, 8-bit image."
    307,200 bytes ≈ 300 KB.
