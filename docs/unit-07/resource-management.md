# Resource Management

!!! info "Not in the previous lecturer's notes"
    Written from the syllabus and standard textbook knowledge (mainly Steinmetz and Nahrstedt, *Multimedia: Computing, Communications and Applications*). Check details against your prescribed textbook.

## Resources

A **resource** is anything a process needs to run.

| Kind | Examples |
|---|---|
| **Active** (provide a service over time) | **CPU**, network adapter, disk controller |
| **Passive** (provide capacity) | **Main memory**, **bandwidth** of bus, network and disk, buffer space |

## Requirements

For continuous media the resource manager must:

1. **Share** resources among competing processes (and with discrete-media work).
2. **Guarantee** the capacity each continuous media stream needs (deadlines, bandwidth, buffers).
3. Handle **several streams at once** with different QoS.
4. **Reject** a new request if it would break existing guarantees (**admission control**).

## Allocation schemes

Resource allocation works with **reservation** of resources before use.

1. The application states its **QoS** requirements (for example frame rate, delay).
2. The system maps them into **resource requirements**.
3. **Admission control (schedulability test)**: can the request be served **together with all existing guarantees**?
4. If yes, the resources are **reserved** (**accepted**); if no, the request is **rejected** or **renegotiated** with lower QoS.
5. During the run the system **enforces** the reservation and **monitors** it.

| Guarantee | Meaning | Reservation based on |
|---|---|---|
| **Deterministic (hard)** | QoS always met | **Worst case**; may waste resources |
| **Statistical** | QoS met with a given probability | **Average** case; better use |
| **Best effort** | No guarantee | Whatever is left |

!!! example "Admission control by utilisation"
    Two audio and one video streams already use 70 % of the CPU. A new stream needs 40 %. 70 + 40 = 110 % > 100 %, so it is **rejected** (or offered a lower frame rate needing, say, 25 %).

## Continuous media resource model (LBAP)

The model describes the **workload** a stream puts on a resource and the **guarantee** the system gives. The **Linear Bounded Arrival Process (LBAP)** characterises a stream by three parameters:

| Symbol | Meaning |
|---|---|
| **M** | **Maximum message (LDU) size** |
| **R** | **Maximum message rate** (messages per second) |
| **B** | **Maximum burst** (number of messages that may arrive back to back) |

The number of messages arriving in any interval of length *t* is bounded **linearly**:

164\text{messages in } t \;\le\; B + R\cdot t164

!!! example "Check"
    A video stream with R = 25 messages/s and burst B = 3: in 2 s at most 3 + 25 × 2 = **53** messages. If M = 10 KB per frame, the peak data rate is M × R = **250 KB/s**.

Associated ideas in the model:

- Each message needs **processing time** on the resource and has a **deadline** (delay bound).
- A **resource manager** per resource performs the schedulability test and the reservation.
- **Buffers** absorb the burst B and the jitter.
- The **end-to-end QoS** is the combination of the guarantees of all resources along the path (disk, CPU, network).

## Checkpoint

??? question "Why is admission control needed?"
    To protect the guarantees already given: a new stream is accepted only if the resources remain sufficient for all.

??? question "What do M, R and B stand for in LBAP?"
    Maximum message size, maximum message rate, maximum burst.
