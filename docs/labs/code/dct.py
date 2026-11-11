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
