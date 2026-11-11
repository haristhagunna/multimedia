# Application Subsystem

The application subsystem contains the services that make **collaborative and distributed multimedia applications** possible. It uses the transport subsystem below it.

## Collaborative computing

**Computer-supported cooperative work (CSCW)**: people at different places work together with shared multimedia tools: video conferencing, shared whiteboard, shared applications, shared documents.

- **Synchronous** (same time, for example a video conference) and **asynchronous** (different times, for example multimedia mail).
- **Shared workspace**: one application's output is shown at several sites. **Shared execution environment**: each site runs the same application on the same data.

## Session management

A **session** is the period during which the participants and their media connections exist. Session management covers:

| Function | Meaning |
|---|---|
| **Session setup and teardown** | Create and end the session; announce it (**session directory**) |
| **Membership** | Who joins or leaves; **invitation**, **rendezvous** (finding the partners) |
| **Media management** | Which streams (audio, video, whiteboard) each participant uses; **configuration** |
| **Floor (conference) control** | Who may speak or control the shared tool now: **floor control** policies (chair-controlled, first come first served) |
| **QoS negotiation** | Agree on the quality each stream uses |

## Architectures

- **Centralised**: a **multipoint control unit (MCU)** receives all streams and mixes or switches them.
- **Distributed**: every participant sends to all others (multicast), no central mixer.

## Multimedia mail and messaging

Messages carrying text, images, audio and video. Large messages need **storage**; **MIME** describes the media types in the body.

## Checkpoint

??? question "What is floor control?"
    A mechanism that decides which participant may use a shared resource or speak at a given time, to avoid conflicts.

??? question "Differentiate synchronous and asynchronous collaboration."
    Synchronous: at the same time (video conference). Asynchronous: at different times (multimedia mail).
