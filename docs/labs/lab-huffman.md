# Lab 4: Huffman and run-length coding

**Aim.** Build Huffman codes by program, confirm the exam answer **224 bits**, and see when RLE expands data.

<p><a class="btn-s" href="code/huffman.py" download>Download huffman.py</a></p>

```python
"""Lab 2: Huffman coding and run-length coding (standard library only)."""
import heapq
from collections import Counter

def huffman_codes(freq):
    heap = [[w, i, [s, ""]] for i, (s, w) in enumerate(sorted(freq.items()))]
    heapq.heapify(heap); n = len(heap)
    if n == 1: return {heap[0][2][0]: "0"}
    while len(heap) > 1:
        a = heapq.heappop(heap); b = heapq.heappop(heap)
        for pair in a[2:]: pair[1] = "0" + pair[1]
        for pair in b[2:]: pair[1] = "1" + pair[1]
        heapq.heappush(heap, [a[0] + b[0], n] + a[2:] + b[2:]); n += 1
    return {s: c for s, c in heap[0][2:]}

def rle(s):
    out, i = [], 0
    while i < len(s):
        j = i
        while j < len(s) and s[j] == s[i]: j += 1
        out.append(f"{s[i]}{j - i}"); i = j
    return "".join(out)

if __name__ == "__main__":
    freq = {"A": 45, "B": 13, "C": 12, "D": 16, "E": 9, "F": 5}      # Mock Exam 1, B4
    codes = huffman_codes(freq)
    bits = sum(freq[s] * len(codes[s]) for s in freq)
    for s in sorted(codes): print(s, freq[s], codes[s])
    print("total bits", bits, "average", bits / sum(freq.values()))
    text = "aaabccdddd"
    print(text, "->", rle(text))
    print("abcd ->", rle("abcd"), "(RLE can expand data)")
    enc = "".join(huffman_codes(Counter("abracadabra"))[c] for c in "abracadabra")
    print("abracadabra Huffman bits:", len(enc), "vs", 8 * 11, "ASCII bits")
```

**Expected output**

```text
A 45 0
B 13 101
C 12 100
D 16 111
E 9 1101
F 5 1100
total bits 224 average 2.24
aaabccdddd -> a3b1c2d4
abcd -> a1b1c1d1 (RLE can expand data)
abracadabra Huffman bits: 23 vs 88 ASCII bits
```

Tie-breaking may give different codes in your own runs, but the **total bit count must match**.

## Try it

1. Change the frequencies to all equal (10 each). What happens to the average length?
2. Encode your own name; compare Huffman bits with 8 bits per character.
3. Find a string where RLE makes the output longer.
