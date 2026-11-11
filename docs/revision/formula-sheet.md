# Formula sheet

!!! exam "Always write the formula, substitute, then state the unit."

## Sound (Unit 2)

| Quantity | Formula |
|---|---|
| Nyquist limit | \(f_s \ge 2 f_{max}\) |
| Frequency from period | \(f = 1/T\) |
| Uncompressed audio size | \(S = R \times (b/8) \times C \times D\) bytes (R = Hz, b = bits, C = channels, D = seconds) |
| Quantization levels | \(2^{b}\) |
| CD-DA data rate | \(44{,}100 \times 16 \times 2 = 1{,}411{,}200\) bit/s |

## Image and video (Units 3 and 4)

| Quantity | Formula |
|---|---|
| Bitmap size | width × height × bits per pixel / 8 bytes |
| Frame duration at 25 fps | \(1/25 = 40\) ms |
| Luminance (YUV) | \(Y = 0.30R + 0.59G + 0.11B\) |
| Video bandwidth | \(B = \dfrac{a \cdot b \cdot c}{2}\) with Kell factor 0.7 on the vertical resolution |
| Raw video size | frame size × frame rate × duration |

## Compression (Unit 5)

| Quantity | Formula |
|---|---|
| Compression ratio | original size : compressed size |
| Huffman average length | \(\sum p_i \, l_i\) bits/symbol |
| Space saving | \(1 - \text{compressed}/\text{original}\) |

## Optical storage (Unit 6)

| Quantity | Value |
|---|---|
| CD-DA block (sector) | 2,352 bytes, 75 blocks/s |
| Blocks on 74 min disc | ≈ 333,000 |
| Data rate | 2,352 × 75 = 176,400 byte/s |

## Real-time scheduling (Unit 7)

| Quantity | Formula |
|---|---|
| CPU utilisation | \(U = \sum C_i / P_i\) |
| EDF schedulable iff | \(U \le 1\) |
| RM sufficient bound | \(U \le n(2^{1/n} - 1)\) (≈ 0.693 as n grows) |

## Networking and QoS (Unit 8)

| Quantity | Formula |
|---|---|
| Leaky/linear bounded arrival | \(A(t) \le B + R\,t\) |
| Token bucket | tokens sent in time t ≤ \(b + r\,t\) |
