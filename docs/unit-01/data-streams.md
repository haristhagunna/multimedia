# Data Streams and Transmission Modes

This page covers syllabus item 1.3, **data stream characteristics for traditional and continuous media**.

!!! info "Extra"
    The syllabus covers this item through two ideas: **discrete versus continuous media** (see [Media Concepts and Properties](media-concepts-and-properties.md#representation-dimensions)) and the **three transmission modes** below. No further data-stream attributes (such as rate or periodicity) appear in the course text's notes.

## Serial transmission

Multimedia communication is **generally transmitted serially: one bit at a time**. The three modes below differ in *how the receiver stays in step with the sender*.

## Asynchronous transmission

- **Synchronization at the byte level.**
- There may be **gaps between bytes**, which makes it good for **random** communication.
- Examples: **WWW, e-mail, keyboard**.

!!! info "Extra"
    Because there is no shared clock, each byte is wrapped with a **start bit and a stop bit** so the receiver knows where it begins and ends. That is why the course text notes that *synchronous* transmission has **no start and stop bits**.

## Synchronous transmission

- **No start and stop bits.**
- Sender and receiver **must be synchronized**, using **clocks**.

## Isochronous transmission

- Data is transferred **at a fixed rate**.
- It delivers data at a **steady rate**.
- It is **best for multimedia communication**.

## Comparison

| | Asynchronous | Synchronous | Isochronous |
|---|---|---|---|
| Timing unit | Byte level | Clock shared by sender and receiver | Fixed, steady rate |
| Gaps allowed? | Yes, between bytes | Clock-driven | Data arrives at a steady rate |
| Start/stop bits | Used (implied) | **None** | Not stated in the notes |
| Best for | Random, bursty traffic | Clock-aligned transfer | **Multimedia** |
| Examples | WWW, e-mail, keyboard | – | Audio and video streams |

## Why multimedia needs a steady rate

Continuous media only make sense if they arrive **on time and in order**: a late audio sample is a click, a late video frame is a stutter. That is why it is called isochronous transfer "best for multimedia", and why the challenges of **latency, delay and synchronization** keep returning (see [The Multimedia System](multimedia-system.md#challenges-of-multimedia-computing)).

!!! exam "Do not confuse these"
    **Synchronization** (the cross-domain layer that coordinates media in time) is **not** the same as **synchronous transmission** (a transmission mode where sender and receiver share a clock). Name each one clearly in your answers.

## Checkpoint

??? question "Which transmission mode is best for multimedia, and why?"
    **Isochronous**, because it transfers data at a **fixed, steady rate**, which is what continuous media such as audio and video need.

??? question "Give two differences between asynchronous and synchronous transmission."
    Asynchronous synchronizes at the **byte level** and allows **gaps between bytes** (e.g. keyboard, e-mail, WWW). Synchronous uses **no start and stop bits** and needs sender and receiver to be **synchronized with clocks**.

??? question "Is the synchronization layer in the global structure the same as synchronous transmission?"
    No. The **synchronization layer** coordinates different media **in time** across all domains (for example audio with video). **Synchronous transmission** is a mode of sending data in which sender and receiver share a clock.
