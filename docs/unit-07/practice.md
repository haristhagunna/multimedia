# Unit 7: Practice Questions

Write your own answer on paper first, then click to reveal the model answer.

!!! info "Not in the previous lecturer's notes"
    This unit and its questions come from the syllabus and standard textbook knowledge.

## Short answer

??? question "1. Why do multimedia applications need a special operating system? (4 marks)"
    Continuous media have time constraints; a conventional OS gives fair sharing but no timing guarantee, so frames and samples may miss their deadlines.

??? question "2. Define real-time process, deadline and real-time system. (3 marks)"
    A real-time process delivers its result within a given time span; the deadline is the latest allowed completion time; a real-time system is one in which correctness depends on both the result and its time.

??? question "3. Differentiate hard and soft real time. (4 marks)"
    Hard: a missed deadline is a failure (flight control), deterministic worst-case guarantee. Soft: occasional misses tolerated (video), statistical or best-effort guarantee.

??? question "4. List the requirements of a multimedia OS. (5 marks)"
    Real-time processing, resource management with QoS guarantees, efficient data handling and file system, synchronisation support, support of discrete and continuous media together, low latency and jitter.

??? question "5. Differentiate active and passive resources. (2 marks)"
    Active: CPU, network adapter (provide service over time). Passive: memory, bandwidth, buffers (provide capacity).

??? question "6. What is admission control? (3 marks)"
    A test whether a new request can be served together with the guarantees already given; if not it is rejected or renegotiated.

??? question "7. Differentiate deterministic, statistical and best-effort guarantees. (3 marks)"
    Deterministic: always met, worst-case based. Statistical: met with a probability, average-case based. Best effort: none.

??? question "8. Define the LBAP parameters. (3 marks)"
    M maximum message size, R maximum message rate, B maximum burst; messages in interval t ≤ B + R·t.

??? question "9. A video task needs 12 ms every 40 ms and an audio task 1 ms every 10 ms. Find the utilisation and test EDF and RM. (4 marks)"
    U = 12/40 + 1/10 = 0.3 + 0.1 = 0.4. EDF: ≤ 1 so yes. RM bound for n = 2 is 0.828; 0.4 is below, so yes.

??? question "10. Compare EDF and RM. (5 marks)"
    Dynamic vs static priority; U ≤ 1 vs the n(2^{1/n} − 1) test; overhead; behaviour in overload.

## Long answer

??? question "11. Explain the continuous media resource model. (6 marks)"
    Workload described by LBAP (M, R, B); each message has processing time and deadline; resource manager does the schedulability test and reservation; buffers absorb burst and jitter; end-to-end QoS is the combination of per-resource guarantees.

??? question "12. Schedule T1 (C = 1, P = 4) and T2 (C = 2, P = 6) by RM for 12 units. (6 marks)"
    U = 0.583 < 0.828. Order: T1 | T2 T2 | idle | T1 | idle | T2 T2 | T1 | idle idle idle. All deadlines met (see [Scheduling](scheduling.md)).

??? question "13. Show that T1 (2, 5) and T2 (4, 7) is schedulable by EDF but not by RM. (7 marks)"
    U = 0.971 ≤ 1 so EDF works. Under RM, T1 has priority; T2 gets only 3 units before time 7 and misses its deadline.

??? question "14. Describe the architecture of a multimedia OS. (6 marks)"
    Layers: applications, API/toolkits, QoS and resource managers, real-time kernel (scheduler, memory, IPC), continuous media file system, network, drivers; approaches: extended OS vs micro-kernel.

## Multiple choice

??? question "15. Which algorithm uses static priorities?"
    - A. EDF
    - B. Rate monotonic
    - C. Round robin only
    - D. Random

    **Answer: B.**

??? question "16. EDF schedulability condition (D = P)"
    - A. U ≤ 0.69
    - B. U ≤ 1
    - C. U ≤ 2
    - D. U = 0

    **Answer: B.**

??? question "17. Soft real time applies to"
    - A. Airbag control
    - B. Video playback
    - C. Reactor shutdown
    - D. Flight control

    **Answer: B.**

??? question "18. RM bound as n becomes large"
    - A. 0.5
    - B. 0.693
    - C. 0.9
    - D. 1.0

    **Answer: B.**
