# Introduction and Real Time

!!! info "Not in the previous lecturer's notes"
    Written from the syllabus and standard textbook knowledge (mainly Steinmetz and Nahrstedt, *Multimedia: Computing, Communications and Applications*). Check details against your prescribed textbook.

## Why an ordinary OS is not enough

An **operating system (OS)** manages the hardware resources (CPU, memory, disk, network) and offers them to applications. Conventional OSs were designed for **discrete data** and fairness: they give each process a fair share, with no promise about *when* a result appears.

Multimedia needs more because **continuous media** (audio, video) have **time constraints**: each logical data unit (LDU, for example one video frame every 40 ms at 25 fps) must be processed and presented on time, or the user sees jerky video and hears clicks.

!!! exam "Requirements on a multimedia OS"
    1. **Real-time processing** of continuous media (meet deadlines).
    2. **Resource management** with **QoS guarantees** (CPU, memory, bandwidth, buffers).
    3. **Efficient data handling**: large data volumes, **continuous media file system**, fast copying.
    4. **Synchronisation** support (audio and video together).
    5. **Support for both discrete and continuous media** at the same time.
    6. **Low latency** and **small jitter**, with predictable behaviour.

## Real time

A **real-time process** is a process that **delivers its result within a given time span**. A **real-time system** is a system that delivers results within given time limits. Correctness depends on **both the value and the time** of the result.

- The time limit is the **deadline**.
- A **real-time system** must be **predictable**: the worst-case behaviour must be known.

| | Hard real time | Soft real time |
|---|---|---|
| Deadline miss | **Not allowed**: failure may be catastrophic | **Tolerated** occasionally; quality drops |
| Guarantee | **Deterministic**, based on worst case | **Statistical** or best effort |
| Examples | Nuclear plant control, flight control, airbag | **Video and audio playback**, video conferencing |
| In multimedia | Rare (for example some medical or studio uses) | **Typical** |

!!! info "Deadlines in multimedia"
    A deadline is the latest time by which the work must finish. For a video at 25 fps, each frame's period is 1 ÷ 25 = **40 ms**; the frame must be decoded and displayed within its period. For CD-quality audio in 1 ms blocks, the period is 1 ms.

### Characteristics of real-time processing

- **Periodic** (continuous media: one LDU every period P) or **aperiodic** (event driven, for example a mouse click).
- **Predictable and bounded** execution time.
- **Latency** (delay from request to result) and **jitter** (variation of the delay) must be small.

## Checkpoint

??? question "Differentiate hard and soft real time with examples."
    Hard: a missed deadline is a failure (flight control). Soft: occasional misses are tolerated (video playback).

??? question "Why does a general-purpose OS fail for video?"
    It gives fair sharing but no time guarantees, so frames may be late.
