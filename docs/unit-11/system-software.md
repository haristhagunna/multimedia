# System Software

!!! source "Source"
    *Unit 11 – Abstractions for Programming* pp. 2–3.

Instead of a separate library per device, **device access becomes part of the operating system**. Continuous-data processing needs **real-time schedulers** (see [Unit 7](../unit-07/scheduling.md)).

## Example: the Nemo system

Nemo consists of the **Nemo Trusted Supervisor Call (NTSC)** running in **supervisor mode** and **three domains in user mode**: **system, device drivers and application**.

!!! warning "Not the TV standard"
    NTSC here means *Nemo Trusted Supervisor Call*. It has nothing to do with the NTSC television standard of [Unit 4](../unit-04/video-transmission.md).

- The **NTSC code** implements the functions needed by user-mode processes and supports **three kinds of processes**:
    - **System processes:** implement most of the OS services.
    - **Device processes:** like system processes but attached to **device interrupt stubs** that run in supervisor mode.
    - **Application processes:** contain user programs.
- NTSC calls are in **two classes**: calls only a **privileged system process** (for example the kernel) may execute, and calls **any process** may execute.
- NTSC provides the **interface between a multimedia hardware device and its driver process**, so even a device with only a low-level hardware interface can be used.
- Processes talk through **IPC (inter-process communication)**, built on low-level **events** and, if needed, **shared memory**.

## Data as time capsules

A **time capsule** is an abstraction related to **file systems**: a file extension for **storing, modifying and accessing continuous media**. Each **LDU** carries, besides its **data type and value**, its **valid life span**. The concept is used **more for video than for audio**.

## Data as streams

A **stream** is the **continuous flow of audio and video data**. It is **established between a source and a sink before the flow** starts. Operations on a stream: **play, fast forward, rewind, stop**.

In **Microsoft Windows** the **Media Control Interface (MCI)** gives access to continuous media streams and their devices.

!!! exam "Exam tip"
    Define time capsule (data plus life span), stream (source to sink), and name MCI. If Nemo is asked, give supervisor call plus three domains and three process types.

## Checkpoint

??? question "What does a time capsule contain?"
    Each LDU's data type, value and valid life span.

??? question "What is MCI?"
    The Media Control Interface of Microsoft Windows for accessing continuous media streams and devices.
