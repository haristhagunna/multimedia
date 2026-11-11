# Transport Subsystem

## Requirements on a multimedia transport subsystem

1. **High throughput** for large continuous streams.
2. **Bounded delay and small jitter** (about 150 ms end-to-end for interactive audio and video).
3. **QoS support**: applications can specify and get guaranteed service.
4. **Multicast** for group communication.
5. **Suitable error handling**: continuous media prefer **timeliness over perfect reliability**.
6. **Synchronisation support** between streams (time stamps).
7. **Efficient processing**: low protocol overhead, no extra copying.

## Why TCP is unsuitable and UDP is not enough

| Protocol | For multimedia |
|---|---|
| **TCP** | Retransmission and congestion control add **delay and jitter**; **no multicast** |
| **UDP** | Fast, supports multicast, but **no ordering, timing or feedback** |

## Real-time protocols on the Internet

| Protocol | Role |
|---|---|
| **RTP** (Real-time Transport Protocol) | Runs over UDP; carries **payload type, sequence number and time stamp** so the receiver can reorder, detect loss and play out at the right time |
| **RTCP** (RTP Control Protocol) | Sends **feedback on quality** (loss, jitter), source identification and helps **synchronise** audio and video |
| **RTSP** (Real-Time Streaming Protocol) | Remote **control** of streams (play, pause, seek) |
| **RSVP** (Resource Reservation Protocol) | **Reserves** network resources along a path |
| **ST-II** | Stream protocol with resource reservation and multicast |

### Playout buffer

The receiver delays playback by a small **playout delay** held in a buffer, absorbing jitter. A larger buffer removes more jitter but increases delay.

!!! example "Playout delay"
    If packets arrive between 40 and 90 ms after sending, jitter is 50 ms. A playout delay of 90 ms from the send time makes every packet available when needed; the cost is 90 ms of latency.

## Error control

- **ARQ** (retransmission): reliable but adds delay; used only for data and when time allows.
- **FEC** (forward error correction): redundancy lets the receiver repair loss without retransmission.
- **Concealment**: repeat or interpolate missing audio or video parts.

## Networks

**Ethernet** (shared, no guarantee), **FDDI**, **ATM** (cells of 53 bytes, built-in QoS classes), **ISDN** (64 kbit/s channels), and today **IP networks with DiffServ or IntServ**.

## Checkpoint

??? question "Why is RTP used over UDP rather than TCP?"
    UDP avoids retransmission delay and supports multicast; RTP adds sequence numbers and time stamps for ordering and playout.

??? question "What does a playout buffer do?"
    Absorbs delay variation (jitter) so media plays smoothly, at the cost of extra delay.
