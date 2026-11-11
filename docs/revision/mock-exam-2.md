# Mock Exam 2: Practice Questions

<div class="mock-timer" data-minutes="120" data-total="60"></div>

**Full marks: 60 · Time: 2 hours · Attempt all questions.** This paper puts more weight on units 6–12 (storage, OS, communication, hypermedia, synchronization and programming) so that it complements Mock Exam 1.

## Section A: Multiple choice (10 × 1 = 10 marks)

??? question "A1. The Dexter hypertext reference model has the layers"
    - A. Physical, Data link, Network
    - B. Run-time, Storage, Within-component
    - C. Client, Server, Proxy
    - D. Logical, Layout, Content

    **Answer: B.**

??? question "A2. MHEG stands for"
    - A. Multimedia Home Entertainment Group
    - B. Multimedia and Hypermedia information coding Experts Group
    - C. Motion Hardware Encoding Group
    - D. Multi-Host Exchange Gateway

    **Answer: B.**

??? question "A3. ODA (Office Document Architecture) describes a document by"
    - A. Logical and layout structures
    - B. Only its fonts
    - C. Only its bitmap
    - D. Network addresses

    **Answer: A.** Logical structure (chapters, paragraphs) and layout structure (pages, frames).

??? question "A4. EDF can schedule periodic tasks with D = P if the total utilization is"
    - A. ≤ 0.69
    - B. ≤ 1
    - C. ≤ 2
    - D. exactly 0.5

    **Answer: B.**

??? question "A5. RTP packets carry"
    - A. Only routing tables
    - B. Sequence numbers and time stamps for real-time media
    - C. Disk addresses
    - D. Encryption keys only

    **Answer: B.**

??? question "A6. A leaky bucket is used to"
    - A. Compress video
    - B. Shape traffic to a constant output rate
    - C. Store hypertext links
    - D. Convert RGB to YUV

    **Answer: B.** Bursty input leaves at a constant rate; excess is buffered or dropped.

??? question "A7. The laser wavelength of Blu-ray is about"
    - A. 780 nm
    - B. 650 nm
    - C. 405 nm
    - D. 1,064 nm

    **Answer: C.**

??? question "A8. Which medium is a continuous (time-dependent) medium?"
    - A. Text
    - B. Still image
    - C. Audio
    - D. Graphics drawing

    **Answer: C.**

??? question "A9. A sender clock 0.1 % faster than the receiver causes how much drift in 10 minutes?"
    - A. 0.06 s
    - B. 0.6 s
    - C. 6 s
    - D. 60 s

    **Answer: B.** 600 s × 0.001 = 0.6 s, far beyond the ±80 ms lip-sync limit.

??? question "A10. A 'toolkit' in multimedia programming is best described as"
    - A. A set of reusable software components/objects for building applications
    - B. A hardware card
    - C. A video format
    - D. A network cable

    **Answer: A.**

## Section B: Short answers (6 × 5 = 30 marks)

??? question "B1. Differentiate hypertext, hypermedia and multimedia. (5 marks)"
    **Marking scheme**

    - **Hypertext**: text nodes joined by links, non-linear reading. **(1.5)**
    - **Hypermedia**: hypertext extended with other media (image, audio, video) as nodes/anchors. **(1.5)**
    - **Multimedia**: integrates media but need not provide links or navigation. **(1)**
    - Relation: hypermedia = hypertext + multimedia; example (the Web). **(1)**

??? question "B2. Compute the uncompressed size of one minute of 640 × 480, 24-bit video at 25 frames/s. (5 marks)"
    **Marking scheme**

    - Frame = 640 × 480 × 3 bytes = **921,600 bytes**. **(2)**
    - Per second = 921,600 × 25 = **23,040,000 bytes** (184.32 Mbit/s). **(1.5)**
    - Per minute = × 60 = **1,382,400,000 bytes ≈ 1.38 GB**. **(1)**
    - Conclusion: compression is essential. **(0.5)**

??? question "B3. What is skew? State the lip-synchronization limits and name two causes of loss of synchronization. (5 marks)"
    **Marking scheme**

    - Skew: time difference between related LDUs of different streams. **(1.5)**
    - Lip sync tolerated within **±80 ms**. **(1.5)**
    - Causes: network delay jitter, different clock rates of sender/receiver, processing delays, buffering. **(2)**

??? question "B4. Explain the leaky bucket mechanism. (5 marks)"
    **Marking scheme**

    - Packets enter a buffer ("bucket") and leave at a **constant rate**. **(2)**
    - Bursts are smoothed; if the bucket is full, packets are **dropped** (or marked). **(1.5)**
    - Used for **traffic shaping/policing** to keep within the agreed QoS. **(1)**
    - Simple diagram. **(0.5)**

??? question "B5. Write a small SGML document with a DTD for a memo (to, from, body) and explain what the DTD does. (5 marks)"
    **Marking scheme**

    - DTD, e.g. `<!ELEMENT memo (to, from, body)>` with `<!ELEMENT to (#PCDATA)>` and similarly for `from` and `body`. **(2)**
    - Document instance using the tags `<memo><to>Ram</to><from>Sita</from><body>…</body></memo>`. **(1.5)**
    - The DTD defines the **allowed elements and their structure** so documents can be validated; separates structure from presentation. **(1.5)**

??? question "B6. Describe the layered structure of the multimedia communication system (application and transport subsystems). (5 marks)"
    **Marking scheme**

    - **Application subsystem**: collaborative work, session management, user interface, media services. **(2)**
    - **Transport subsystem**: transport protocols (RTP/UDP, TCP) and network service with **QoS** support. **(2)**
    - Mention of QoS negotiation/guarantees between layers. **(1)**

## Section C: Long answers (2 × 10 = 20 marks)

??? question "C1. Three periodic tasks are T1 (C = 1, P = 4), T2 (C = 2, P = 6), T3 (C = 3, P = 12). Test schedulability with EDF and rate monotonic and draw the schedule over 12 time units. (10 marks)"
    **Marking scheme**

    - U = 1/4 + 2/6 + 3/12 = 0.25 + 0.333 + 0.25 = **0.833**. **(2)**
    - EDF: U ≤ 1 → **schedulable**. **(1.5)**
    - RM utilization bound for 3 tasks: 3(2<sup>1/3</sup> − 1) = **0.780**. U = 0.833 exceeds it, so the **bound test is inconclusive**: the bound is *sufficient, not necessary*. **(2.5)**
    - Exact check by simulation (RM priorities T1 > T2 > T3): 0–1 T1, 1–3 T2, 3–4 T3, 4–5 T1, 5–6 T3, 6–8 T2, 8–9 T1, 9–10 T3, 10–12 idle. All deadlines are met, so RM **is** schedulable here. **(3)**
    - Timeline diagram. **(1)**

    This is a favourite trap: failing the RM bound does **not** prove a task set unschedulable. Always run the timeline when U lies between the bound and 1.

??? question "C2. Explain the MHEG standard: its objective, the object classes and where it is used. Compare it briefly with SGML. (10 marks)"
    **Marking scheme**

    - Objective: a **final-form, interchangeable** representation of multimedia/hypermedia objects, suitable for real-time delivery and run-time engines. **(2)**
    - Classes (any 4 with purpose): Content, Selection/Modification/Interaction, Composite, Action, Link, Script, Descriptor, Container, Macro. **(3)**
    - Use: interactive TV, set-top boxes, digital broadcasting, distributed multimedia. **(1.5)**
    - Comparison: SGML describes **document structure** to be processed and formatted (authoring); MHEG is an **end-delivery** format that carries objects and their temporal/spatial relations. **(2.5)**
    - Clear headings/diagram. **(1)**

<div class="mock-scorer" data-total="60"></div>
