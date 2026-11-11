# Unit 5: Practice Questions

Write your own answer on paper first, then click to reveal the model answer. Marks are a guide to how much detail the question deserves.

## Short answer

??? question "1. Why is data compression needed in multimedia? (3 marks)"
    Uncompressed media is huge (a 640 × 480, 8-bit image is 300 KB; CD audio is 1.41 Mbit/s). Compression **reduces the storage**, the **transmission bandwidth** and the volume to be sent.

??? question "2. State the coding requirements for multimedia. (3 marks)"
    Best possible quality; minimal complexity for cost-effective implementation; processing must not exceed a given time span.

??? question "3. Differentiate lossless and lossy compression. (4 marks)"
    Lossless: decoded data **identical** to the original (RLE, Huffman, arithmetic). Lossy: decoded data **similar but not identical**, higher compression (JPEG, MPEG, MP3).

??? question "4. Define entropy coding, source coding and hybrid coding. (6 marks)"
    Entropy: ignores semantics, treats data as a value sequence, lossless. Source: uses semantics, normally lossy (e.g. removing high frequencies, frequency-domain formants). Hybrid: both, e.g. JPEG, MPEG, H.261, DVI.

??? question "5. Encode `aaabccdddd` with run-length coding. (2 marks)"
    a3b1c2d4 (10 characters to 8).

??? question "6. When does run-length coding fail? (2 marks)"
    When there are no runs: `abcd` becomes `a1b1c1d1` and the size doubles.

??? question "7. State the prefix rule. (2 marks)"
    No codeword may be a prefix of another, so decoding is unambiguous.

??? question "8. Build a Huffman code for A = 5, B = 1, C = 6, D = 3 and compute the compressed size. (6 marks)"
    B+D = 4; 4+A = 9; 9+C = 15. Codes C = 0, A = 11, B = 100, D = 101. Data bits = 10 + 3 + 6 + 9 = **28**. With the tree (32 + 15 bits) the total is **75 bits** against 120 bits.

??? question "9. Decode `1011100` using the code C = 0, A = 11, B = 100, D = 101. (3 marks)"
    101 = D; 11 = A; 0 = C; 0 = C. Result: **DACC**.

??? question "10. Why does JPEG use 8 × 8 blocks and the DCT? (3 marks)"
    The number of operations grows with the square of the block size, so small blocks are cheap. DCT puts most information in a few low-frequency coefficients; the rest can be coarsely quantized.

??? question "11. Where is the loss introduced in JPEG? (2 marks)"
    In quantization (divide by table entry and round); DCT alone is practically reversible.

??? question "12. What is the zigzag scan for? (2 marks)"
    It orders AC coefficients from low to high frequency to group zeros together for efficient run-length and Huffman coding.

??? question "13. Differentiate the I, P and B frames. (5 marks)"
    I: independent, JPEG-like, lower compression. P: predicted from previous I or P with motion estimation and compensation. B: bidirectional from past and future I/P, highest compression, needs reordering.

??? question "14. Define GOP and prediction span. (2 marks)"
    GOP: number of frames between successive I-frames. Prediction span: number of frames between a P-frame and the preceding I-frame.

??? question "15. What is px64? (2 marks)"
    The H.261 data rate p × 64 kbit/s (p = 1…30) for videoconferencing over ISDN. *(Extra.)*

## Long answer

??? question "16. Explain Huffman coding with an example. (8 marks)"
    Algorithm (frequencies, priority queue, merge two smallest, 0 left/1 right), the A/B/C/D worked example with tree, code table, 75 vs 120 bits, decoding, applications.

??? question "17. Explain the JPEG compression process. (8 marks)"
    Colour transform and down-sampling; 8 × 8 blocks; forward DCT; quantization with 64-entry table; DC treated separately; zigzag order for AC; Huffman (or arithmetic) coding. Mention sequential and expanded (progressive) modes.

??? question "18. Compare the lossy sequential and expanded lossy DCT-based modes. (4 marks)"
    8 bits vs 8 or 12 bits; Huffman only vs Huffman and arithmetic; sequential only vs sequential and progressive (layered coding).

??? question "19. Explain MPEG video compression: spatial and temporal redundancy and frame types. (10 marks)"
    Use the tables in [MPEG](../unit-05/mpeg-h261-dvi.md): intra-frame (macroblock, DCT, quantization, entropy), inter-frame (motion estimation, vectors, compensation, residual), I/P/B frames, GOP, rate limits.

??? question "20. Explain prediction coding and adaptive compression. (5 marks)"
    See [Prediction and Adaptive Compression](prediction-and-adaptive.md): code differences from predicted values; adaptive methods learn statistics while coding (adaptive Huffman, LZW). *(Extra.)*

??? question "21. Explain arithmetic coding and compare it with Huffman. (5 marks)"
    One codeword for a whole string; interval 0–1 split by probabilities, narrowed per symbol, termination character; Huffman uses one codeword per symbol (whole number of bits).

## Multiple choice

??? question "22. Which is a lossless technique?"
    - A. JPEG quantization
    - B. Huffman coding
    - C. MP3
    - D. Motion compensation

    **Answer: B.**

??? question "23. In JPEG, the lossy step is"
    - A. Zigzag scan
    - B. Huffman coding
    - C. Quantization
    - D. Block preparation

    **Answer: C.**

??? question "24. Which MPEG frame needs no reference frame?"
    - A. I
    - B. P
    - C. B
    - D. All of them

    **Answer: A.**

??? question "25. The best compression among MPEG frames comes from"
    - A. I
    - B. P
    - C. B
    - D. DC

    **Answer: C.**

??? question "26. The Huffman code assigns"
    - A. Equal length codes
    - B. Shortest codes to the most frequent symbols
    - C. Shortest codes to the rarest symbols
    - D. One code to the whole string

    **Answer: B.**

??? question "27. Run-length coding of `0001111100011` gives"
    - A. (0,3)(1,5)(0,3)(1,2)
    - B. (0,3)(1,4)(0,3)(1,3)
    - C. 0315032
    - D. (3,0)(5,1)

    **Answer: A.**

??? question "28. Hybrid coding standards include"
    - A. Huffman and RLE
    - B. JPEG and MPEG
    - C. PCM and ADPCM
    - D. Pixmap and bitmap

    **Answer: B.**
