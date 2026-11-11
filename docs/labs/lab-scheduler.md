# Lab 6: EDF and rate-monotonic scheduling

**Aim.** Reproduce the two classic timelines and discover why the RM utilization bound is only *sufficient*.

<p><a class="btn-s" href="code/scheduler.py" download>Download scheduler.py</a></p>

```python
"""Lab 3: EDF and rate-monotonic scheduling of periodic tasks (standard library only)."""
from math import gcd
from functools import reduce

def simulate(tasks, policy="EDF", horizon=None):
    """tasks = [(C, P), ...], deadline = period. Returns (timeline, missed)."""
    horizon = horizon or reduce(lambda a, b: a * b // gcd(a, b), (p for _, p in tasks))
    rem = [0] * len(tasks); dl = [0] * len(tasks); line = []; missed = []
    for t in range(horizon):
        for i, (c, p) in enumerate(tasks):
            if t % p == 0:
                if rem[i] > 0: missed.append((f"T{i+1}", t))
                rem[i], dl[i] = c, t + p
        ready = [i for i in range(len(tasks)) if rem[i] > 0]
        if ready:
            key = (lambda i: (dl[i], i)) if policy == "EDF" else (lambda i: (tasks[i][1], i))
            run = min(ready, key=key); rem[run] -= 1; line.append(f"T{run+1}")
        else: line.append("--")
        for i in range(len(tasks)):
            if rem[i] > 0 and dl[i] == t + 1: missed.append((f"T{i+1}", t + 1)); rem[i] = 0
    return line, missed

def report(tasks):
    u = sum(c / p for c, p in tasks); n = len(tasks)
    print(f"tasks {tasks}  U = {u:.3f}  RM bound = {n*(2**(1/n)-1):.3f}")
    for pol in ("EDF", "RM"):
        line, missed = simulate(tasks, pol)
        print(f"  {pol}: {' '.join(line)}   missed: {missed or 'none'}")

if __name__ == "__main__":
    report([(2, 5), (4, 7)])               # EDF yes, RM no (Mock Exam 1, C2)
    report([(1, 4), (2, 6), (3, 12)])      # RM bound fails but RM still works (Mock Exam 2, C1)
```

**Expected output (first rows)**

```text
tasks [(2, 5), (4, 7)]  U = 0.971  RM bound = 0.828
  EDF: ...   missed: none
  RM:  ...   missed: [('T2', 7)]
tasks [(1, 4), (2, 6), (3, 12)]  U = 0.833  RM bound = 0.780
  EDF: T1 T2 T2 T3 T1 T3 T2 T2 T1 T3 -- --   missed: none
  RM: T1 T2 T2 T3 T1 T3 T2 T2 T1 T3 -- --   missed: none
```

## Try it

1. Search for a task set with U ≤ 1 where RM misses and EDF does not.
2. Add a task with U > 1. What happens to EDF?
3. Why is the second set schedulable by RM even though U exceeds the bound?
