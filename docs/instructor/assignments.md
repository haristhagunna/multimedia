# Assignments and rubrics

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
