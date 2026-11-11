# Lab 5: The DCT and quantization in JPEG

**Aim.** Verify that the DCT is reversible and that quantization is where information is lost.

<p><a class="btn-s" href="code/dct.py" download>Download dct.py</a></p>

```python
"""Lab 4: 8x8 DCT, quantization and zigzag (numpy only)."""
import numpy as np

N = 8
C = np.array([[np.sqrt(1 / N) if k == 0 else np.sqrt(2 / N) * np.cos((2 * n + 1) * k * np.pi / (2 * N))
               for n in range(N)] for k in range(N)])          # orthonormal DCT-II matrix

def dct2(b): return C @ b @ C.T
def idct2(c): return C.T @ c @ C

Q = np.array([[16, 11, 10, 16, 24, 40, 51, 61], [12, 12, 14, 19, 26, 58, 60, 55],
              [14, 13, 16, 24, 40, 57, 69, 56], [14, 17, 22, 29, 51, 87, 80, 62],
              [18, 22, 37, 56, 68, 109, 103, 77], [24, 35, 55, 64, 81, 104, 113, 92],
              [49, 64, 78, 87, 103, 121, 120, 101], [72, 92, 95, 98, 112, 100, 103, 99]])

def zigzag(m):
    idx = sorted(((i, j) for i in range(N) for j in range(N)),
                 key=lambda p: (p[0] + p[1], p[1] if (p[0] + p[1]) % 2 == 0 else p[0]))
    return [int(m[i, j]) for i, j in idx]

if __name__ == "__main__":
    x = np.arange(N)
    block = 128 + 40 * np.sin(x[:, None] / 3) + 10 * np.cos(x[None, :] / 2)   # smooth test block
    coef = dct2(block - 128)
    q = np.round(coef / Q)                      # <- the only lossy step
    print("non-zero coefficients after quantization:", int(np.count_nonzero(q)), "of 64")
    zz = zigzag(q); print("zigzag:", zz[:20], "...")
    rec = idct2(q * Q) + 128
    print("max reconstruction error:", round(float(np.abs(rec - block).max()), 2))
    print("DCT alone is reversible:", np.allclose(idct2(coef) + 128, block))
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
