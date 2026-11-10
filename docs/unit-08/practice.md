# Unit 8: Practice Questions

Write your own answer on paper first, then click to reveal the model answer.

!!! info "Not in the previous lecturer's notes"
    This unit and its questions come from the syllabus and standard textbook knowledge.

## Short answer

??? question "1. Why is multimedia communication more demanding than ordinary data communication? (4 marks)"
    Large volume, delay and jitter limits, multicast, stream synchronisation; some loss tolerated but not lateness.

??? question "2. Name the subsystems of a multimedia communication system. (3 marks)"
    Application subsystem, transport subsystem (on the network), with QoS and resource management across them.

??? question "3. What is CSCW? Differentiate synchronous and asynchronous use. (4 marks)"
    Computer-supported cooperative work: people cooperate with shared multimedia tools. Synchronous: same time (video conference); asynchronous: different times (mail).

??? question "4. What is floor control? (2 marks)"
    Deciding who may speak or control the shared tool now.

??? question "5. List the requirements of a multimedia transport subsystem. (5 marks)"
    Throughput, bounded delay and jitter, QoS support, multicast, suitable error handling, synchronisation, efficiency.

??? question "6. Why are TCP and UDP not ideal for multimedia? (3 marks)"
    TCP: retransmission delay and no multicast. UDP: no ordering, timing or feedback.

??? question "7. What do RTP and RTCP do? (4 marks)"
    RTP: payload type, sequence numbers, time stamps over UDP. RTCP: quality feedback, source identification, help with synchronisation.

??? question "8. What is a playout buffer? (2 marks)"
    A buffer that delays playback to absorb jitter.

??? question "9. State four network QoS parameters. (2 marks)"
    Throughput, delay, jitter, loss rate.

??? question "10. Differentiate guaranteed, statistical and best-effort service. (3 marks)"
    Always met (worst case); met with probability; no guarantee.

## Long answer

??? question "11. Explain the QoS management process. (8 marks)"
    Specification, negotiation, admission control, reservation, monitoring and policing, adaptation.

??? question "12. Explain leaky bucket and token bucket with an example. (6 marks)"
    Leaky bucket: constant output. Token bucket: tokens at rate r, bucket b, bursts up to b; example r = 100/s, b = 20.

??? question "13. Explain session management in the application subsystem. (6 marks)"
    Setup/teardown, membership and rendezvous, media configuration, floor control, QoS negotiation; centralised (MCU) versus distributed architecture.

??? question "14. Describe the transport protocols for real-time multimedia on the Internet. (6 marks)"
    RTP, RTCP, RTSP, RSVP, ST-II, over UDP with multicast.

## Multiple choice

??? question "15. RTP normally runs over"
    - A. TCP
    - B. UDP
    - C. ATM only
    - D. HTTP only

    **Answer: B.**

??? question "16. Jitter is"
    - A. Average delay
    - B. Variation of delay
    - C. Loss rate
    - D. Bandwidth

    **Answer: B.**

??? question "17. Which shaper allows bursts?"
    - A. Leaky bucket
    - B. Token bucket
    - C. Neither
    - D. Both exactly the same

    **Answer: B.**

??? question "18. Interactive audio end-to-end delay should be at most about"
    - A. 15 ms
    - B. 150 ms
    - C. 1.5 s
    - D. 15 s

    **Answer: B.**
