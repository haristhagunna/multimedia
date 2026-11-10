# Process Management and Real-Time Scheduling

!!! info "Not in the previous lecturer's notes"
    Written from the syllabus and standard textbook knowledge (mainly Steinmetz and Nahrstedt, *Multimedia: Computing, Communications and Applications*). Check details against your prescribed textbook.

## Real-time processing requirement

For continuous media the **process manager** must schedule processes so that every periodic task meets its deadline. A periodic task is described by:

| Symbol | Meaning |
|---|---|
| **C** | Computation (execution) time per period |
| **P** | **Period** (a new instance is released every P) |
| **D** | Deadline, usually **D = P** (finish before the next instance) |
| **U = C ÷ P** | **Utilisation**: the fraction of the CPU the task needs |

Total utilisation of *n* tasks: **U = Σ Cᵢ ÷ Pᵢ**. If U > 1, no scheduler can succeed.

!!! example "A video task"
    Decoding a frame takes C = 10 ms and frames come every P = 40 ms (25 fps): U = 10 ÷ 40 = **0.25** (25 % of the CPU).

## Real-time scheduling

- A **conventional scheduler** (round robin, priority, FIFO) ignores deadlines.
- A **real-time scheduler** orders tasks by their **timing**. Two classical algorithms are used for continuous media: **Earliest Deadline First** and **Rate Monotonic**.
- Both are **preemptive**: a higher-priority task can interrupt the running one.
- Assumptions: periodic tasks, D = P, independent tasks, negligible switching time.

## Earliest Deadline First (EDF)

- **Rule:** at every moment run the ready task whose **absolute deadline is nearest**.
- **Dynamic priority** (priorities change as deadlines approach); **optimal** for a single CPU: if any algorithm can meet all deadlines, EDF can.
- **Schedulability test (D = P):** the task set is schedulable **if and only if U ≤ 1**.

## Rate Monotonic (RM)

- **Rule:** assign **static priorities by rate**: the task with the **shortest period (highest rate) gets the highest priority**; run the highest-priority ready task.
- **Static priority**, simple to implement, predictable; **optimal among static-priority algorithms**.
- **Sufficient test (Liu and Layland):**

181U \le n\left(2^{1/n}-1\right)181

| n | 1 | 2 | 3 | 4 | → ∞ |
|---|---|---|---|---|---|
| Bound | 1.000 | 0.828 | 0.780 | 0.757 | **0.693** |

If U is below the bound, RM surely works. If U is above it but ≤ 1, RM **may or may not** work (a timeline decides). EDF works up to **U = 1**.

## Worked example 1: both succeed

Tasks: **T1 (C = 1, P = 4)** and **T2 (C = 2, P = 6)**. U = 1/4 + 2/6 = 0.25 + 0.333 = **0.583**. RM bound for n = 2 is 0.828, so RM is guaranteed.

Timeline over 12 time units (RM, T1 has the higher priority; EDF gives the same here):

| t | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Running | T1 | T2 | T2 | idle | T1 | idle | T2 | T2 | T1 | idle | idle | idle |

All instances finish before their deadlines.

## Worked example 2: EDF succeeds, RM fails

Tasks: **T1 (C = 2, P = 5)** and **T2 (C = 4, P = 7)**. U = 2/5 + 4/7 = 0.400 + 0.571 = **0.971**.

- **EDF:** U ≤ 1, so schedulable. Timeline in the table below.
- **RM:** U = 0.971 is above the n = 2 bound 0.828, and the timeline shows a miss.

| t | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **RM** | T1 | T1 | T2 | T2 | T2 | T1 | T1 | **T2** | T1 | T1 | T2 | T2 |
| **EDF** | T1 | T1 | T2 | T2 | T2 | T2 | T1 | T1 | T2 | T2 | T2 | T2 |

Under RM, the first T2 instance (deadline 7) has had only 3 of its 4 units by t = 7 and finishes in slot 7, i.e. at time 8: **deadline missed**. Under EDF it finishes at time 6 and nothing misses.

!!! warning "Method check"
    Timelines like these are easy to get wrong by hand. The tables above were produced by a small simulation (unit time steps, deadline = period) and agree with the hand analysis. In the exam, mark each release and deadline on the time axis and state the priority rule you use at each decision.

!!! exam "Comparison to memorise"
    | | EDF | RM |
    |---|---|---|
    | Priority | **Dynamic** (nearest deadline) | **Static** (shortest period) |
    | Schedulable if | **U ≤ 1** | U ≤ n(2^{1/n} − 1) (sufficient) |
    | CPU use | Up to 100 % | About 69 % guaranteed for large n |
    | Overhead | Higher (priorities recomputed) | Lower |
    | Overload | Many tasks may miss | Low-priority tasks miss first |

!!! info "Other points"
    Textbooks also mention **priority inversion** (a low-priority task holds a resource needed by a high-priority one) and **overload handling**. These are not in the syllabus text.

## Checkpoint

??? question "A task set has U = 0.9. Is it schedulable by EDF? By RM?"
    EDF: yes (U ≤ 1). RM: the sufficient bound (at most 0.828 for n = 2, tends to 0.693) is exceeded, so RM is not guaranteed; check with a timeline.

??? question "Which priority does RM give to a 20 ms task and a 50 ms task?"
    The 20 ms task (shorter period, higher rate) has the higher priority.
