# Lab 7: Clock drift and lip sync

**Aim.** Quantify how a tiny clock error breaks synchronization.

<p><a class="btn-s" href="code/sync.py" download>Download sync.py</a></p>

```python
"""Lab 5: clock drift and lip-sync limit (standard library only)."""
LIMIT = 0.080   # +/-80 ms

def drift(ppm_or_percent, seconds, percent=True):
    return seconds * (ppm_or_percent / 100 if percent else ppm_or_percent * 1e-6)

if __name__ == "__main__":
    d = drift(0.1, 600); print(f"0.1% fast for 10 min -> {d:.2f} s drift")
    d2 = drift(0.05, 1200); print(f"0.05% fast for 20 min -> {d2:.2f} s drift")
    # time until the +/-80 ms limit is hit for a 0.1% error
    print("limit reached after", LIMIT / 0.001, "s")
    for pct in (0.1, 0.01, 0.001):
        print(f"{pct}% error: limit after {LIMIT / (pct / 100):.0f} s")
```

**Expected output**

```text
0.1% fast for 10 min -> 0.60 s drift
0.05% fast for 20 min -> 0.60 s drift
limit reached after 80.0 s
0.1% error: limit after 80 s
0.01% error: limit after 800 s
0.001% error: limit after 8000 s
```

A 0.1 % error exceeds the ±80 ms lip-sync limit after only 80 seconds. This is why players adapt buffering and use RTCP/time stamps to resynchronize.
