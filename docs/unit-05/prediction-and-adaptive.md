# Prediction and Adaptive Compression

!!! info "Not in the previous lecturer's notes"
    The lecturer's files do not cover this syllabus item (5.3). It is written from standard textbook knowledge so the syllabus is complete. Check the wording against your prescribed textbook before the exam.

## Prediction (differential) coding

**Idea:** neighbouring samples or pixels are similar, so instead of coding each value we **predict** it from earlier values and code only the **prediction error (difference)**. Differences are small and cluster near zero, so they need fewer bits (and entropy coding handles them well).

**Delta / DPCM:** send the first value, then the difference to the previous one.

| Sample | 100 | 102 | 105 | 104 | 104 |
|---|---|---|---|---|---|
| Sent | 100 | +2 | +3 | −1 | 0 |

- The decoder rebuilds each value as *previous + difference*.
- **DPCM** (differential PCM) does this for audio and images; **ADPCM** adapts the step size.
- **Motion compensation** in video is prediction in time: a frame is predicted from a previous frame and only the residual is coded ([MPEG](mpeg-h261-dvi.md)).
- JPEG codes the **DC coefficient** of each block as the difference from the previous block's DC.

## Adaptive compression

**Static** methods (the Huffman example) need the statistics first and a fixed table. **Adaptive** methods learn the statistics **while coding**, so no table is sent and the codes follow changing data.

| Technique | How it adapts |
|---|---|
| **Adaptive Huffman** | The tree is updated after each symbol, identically in encoder and decoder |
| **Dictionary coding (LZ77, LZ78, LZW)** | Builds a dictionary of repeated strings from the data itself and replaces repeats by references. LZW is used in **GIF** and compress |
| **ADPCM / adaptive quantization** | Step size changes with the signal level |

!!! example "LZ77 idea"
    In `abcabcabc` the second `abc` is replaced by "go back 3, copy 3". The text `abcabcabc` becomes `abc` + (3,6).

!!! exam "Exam tip"
    A 5-mark question: "Explain prediction coding and adaptive compression" needs one definition each, one example (DPCM numbers above; adaptive Huffman or LZW) and the benefit: **fewer bits and no need to send tables**.

## Checkpoint

??? question "Why are prediction errors cheaper to code than the original samples?"
    Neighbouring values are similar, so differences are small, concentrated near zero, and need fewer bits.

??? question "What is the main advantage of adaptive methods over static Huffman?"
    No code table or prior statistics are needed; the model adjusts to changing data.
