# Run-Length and Huffman Coding

!!! source "Source"
    *Unit 5* pp. 10–16; *Huffman Coding* pp. 1–5.

## Run-length encoding (RLE)

A **run** is a sequence in which the same value occurs in many consecutive elements. RLE stores each run as **(value, count)** instead of repeating it. It is **lossless**.

| Input | Output |
|---|---|
| `aaaabbcccccddd` | `a4b2c5d3` |
| `abcd` | `a1b1c1d1` (doubles the size) |
| `0001111100011` | (0,3) (1,5) (0,3) (1,2) |
| `010101` | (0,1)(1,1)(0,1)(1,1)(0,1)(1,1) |

- **Advantage:** reversible (lossless), **very well suited to bitmap images** with large uniform areas (fax, icons).
- **Drawback:** if the data has **no runs, RLE doubles** the amount of numbers.

!!! example "Compression ratio"
    `aaaabbcccccddd` is 14 characters; `a4b2c5d3` is 8, ratio 14 : 8 = 1.75 : 1.

## Huffman coding

- Developed by **David Huffman (1951)**. **Lossless**, entropy coding for data with **frequently occurring characters**.
- **Prefix rule:** no code is a prefix of another, so decoding is unambiguous.
- The **most frequent character gets the shortest code**, the least frequent the longest. It is a **variable-length code**.
- Time complexity **θ(n log n)**.

### Algorithm

1. Count the frequency of each character.
2. Put characters in a **priority queue** sorted by increasing frequency.
3. Make each character a **leaf node**.
4. Create a new node z: the **smallest** frequency is the **left child**, the **second smallest** the **right child**; z = their sum.
5. Remove the two from the queue, **insert z**.
6. Repeat until one node (the root) remains.
7. Label **left edges 0** and **right edges 1**. A character's code is the path from the root.

!!! example "Worked example from the notes (15 characters, 8 bits each = 120 bits)"
    Frequencies: **A = 5, B = 1, C = 6, D = 3**.

    1. Smallest two: B(1) + D(3) → node **4** (B left, D right).
    2. Next smallest: 4 and A(5) → node **9** (4 left, A right).
    3. Next: C(6) and 9 → node **15** (C left, 9 right).

    ```mermaid
    flowchart TB
        R["15"] -- 0 --> C["C (6)"]
        R -- 1 --> N9["9"]
        N9 -- 0 --> N4["4"]
        N9 -- 1 --> A["A (5)"]
        N4 -- 0 --> B["B (1)"]
        N4 -- 1 --> D["D (3)"]
    ```

    | Character | Frequency | Code | Bits |
    |---|---|---|---|
    | A | 5 | 11 | 5 × 2 = 10 |
    | B | 1 | 100 | 1 × 3 = 3 |
    | C | 6 | 0 | 6 × 1 = 6 |
    | D | 3 | 101 | 3 × 3 = 9 |
    | | | | **28** |

    The tree must also be sent: **4 characters × 8 bits = 32 bits** for the characters plus **15 bits** for the tree structure. **Total = 32 + 15 + 28 = 75 bits**, against 120 bits uncompressed.

    **Decoding:** walk from the root; 0 goes left, 1 goes right; at a leaf output the character and restart. `101` → 1 (to node 9), 0 (to node 4), 1 (D) = **D**.

!!! warning "Slips in the lecturer's file"
    Step 7 is printed three times ("Repeat steps 3 to 5…"), and it says "repeat steps 3 to 5" when it should repeat steps 4 and 5 (the leaves already exist). The figures that show the tree are pictures; the table of codes (C = 0, A = 11, B = 100, D = 101) matches the tree drawn above.

!!! example "A second example to practise (not in the notes)"
    Frequencies per 100 characters: A 45, B 13, C 12, D 16, E 9, F 5.
    Merges: F5 + E9 = 14; C12 + B13 = 25; 14 + D16 = 30; 25 + 30 = 55; A45 + 55 = 100.
    One valid code set: **A = 0, C = 100, B = 101, F = 1100, E = 1101, D = 111**.
    Bits = 45×1 + 12×3 + 13×3 + 5×4 + 9×4 + 16×3 = **224** bits, against 300 bits with a fixed 3-bit code (about 25 % saving).
    Ties may be broken differently, so another correct tree may give different codes but the **same total (224)**.

**Applications:** file compression (ZIP), **JPEG, MPEG, TIFF**, fax modems, video cards, sound cards.

!!! exam "Exam tip"
    Always show: frequency table → merge steps → tree with 0/1 labels → code table → total bits and comparison with 8 bits per character. State "the tree is sent too" if the question asks the compressed size.

## Arithmetic coding

- Unlike Huffman (one codeword per character), arithmetic coding gives **one codeword for a whole string**.
- First divide the range **0 to 1** into segments, one per character (including a **termination character**), each segment sized by the character's **probability**. The message narrows the interval step by step.

!!! info "Beyond the lecturer's notes"
    Example: A = 0.6, B = 0.4. Message **AB**: A selects [0, 0.6); inside it B takes the upper 0.4 share, [0.36, 0.6). Any number in [0.36, 0.6), such as 0.5, identifies "AB" (given the symbol count or an end symbol). Arithmetic coding can code a symbol in fractions of a bit, so it can beat Huffman.

## Checkpoint

??? question "Encode `wwwwbbw` with RLE."
    w4b2w1.

??? question "What is the prefix rule?"
    No codeword is the beginning of another codeword, so a bit stream can be decoded without separators.

??? question "Why does Huffman give shorter codes to frequent characters?"
    It lowers the total number of bits (frequency × code length), and the two rarest characters are merged first so they end deepest in the tree.
