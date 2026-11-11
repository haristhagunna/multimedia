---
hide:
  - toc
---

# Interactive simulators

Try the numericals yourself. Change a value and the result updates at once. Everything runs in your browser; nothing is sent anywhere.

## 1. Sampling and quantization (Unit 2)

Drag **fs** below **2 × f** and watch aliasing appear. Reduce the bits and watch the yellow staircase get coarser.

<div class="sim" data-sim="sampling"></div>

!!! exam "What to notice"
    Nyquist: **fs ≥ 2·fmax**. Data rate = fs × bits × channels. More bits means finer steps and a larger file.

## 2. Huffman coding builder (Unit 5)

Type any text. The simulator counts frequencies, merges the two smallest nodes at every step, labels left edges 0 and right edges 1 and compares the total with 8 bits per character. The first box is the textbook example (A=5, B=1, C=6, D=3 gives 28 bits against 120).

<div class="sim" data-sim="huffman"></div>

## 3. Real-time scheduler: RM and EDF (Unit 7)

Enter each task's computation time **C** and period **P**. Use *Load example* to see the classic case where Rate Monotonic misses a deadline but EDF does not. Dotted lines mark releases and ✕ marks a missed deadline.

<div class="sim" data-sim="scheduler"></div>

## 4. Token bucket traffic shaping (Unit 8)

Change the bucket depth **b** and rate **r**, then generate new random traffic. A flow conforms when its cumulative data stays under **b + r·t**.

<div class="sim" data-sim="bucket"></div>

## 5. JPEG: DCT and quantization (Unit 5)

One 8×8 block is transformed with the DCT and quantized with the standard JPEG luminance table scaled by the quality setting.

<div class="sim" data-sim="dct"></div>

## 6. Size and data-rate calculator (Units 2, 3, 4)

<div class="sim" data-sim="calc"></div>

*Use it to check your own exam numericals: write the formula, substitute, and compare.*
