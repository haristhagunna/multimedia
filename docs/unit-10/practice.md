# Unit 10: Practice Questions

Write your own answer on paper first, then click to reveal the model answer.

## Short answer

??? question "1. What does synchronization mean in multimedia? (3 marks)"
    The temporal relation between media objects: between time-dependent objects, and between time-dependent and time-independent ones (for example sound and picture in TV).

??? question "2. Explain content, spatial and temporal relations with examples. (6 marks)"
    Content: dependency on data (spreadsheet and graph). Spatial: layout, the area used on the output device. Temporal: time dependency (video and audio of a concert).

??? question "3. Differentiate intra-object and inter-object synchronization. (4 marks)"
    Intra: time relation between LDUs of one object (25 fps, 40 ms per frame). Inter: between objects (audio/video, pictures, animation with commentary).

??? question "4. Differentiate live and synthetic synchronization. (4 marks)"
    Live reproduces capture-time relations (video conference). Synthetic: relations are specified artificially (car-race path).

??? question "5. Define skew and state the lip-synchronization limits. (3 marks)"
    Skew: time difference between related audio and video LDUs. Tolerated ±80 ms (audio behind −80, ahead +80).

??? question "6. State the pointer synchronization limits. (2 marks)"
    Audio ahead of pointing 750 ms; pointing ahead of audio 500 ms.

??? question "7. Differentiate hard and soft synchronization. (2 marks)"
    Hard: strict timing (live news). Soft: some delay acceptable (offline playback).

??? question "8. Define latency and jitter. (2 marks)"
    Latency: delay; jitter: variation of delay.

??? question "9. What is the object layer? (3 marks)"
    The layer that takes the synchronization specification, computes and executes the presentation schedule for all media and calls the stream layer.

??? question "10. Write the requirements on a synchronization specification method. (4 marks)"
    Consistency, content abstraction, all relation types, integration of continuous and discrete media, QoS, hierarchy.

## Long answer

??? question "11. Why is a reference model for synchronization required and how is it defined? (8 marks)"
    Reasons (several users and levels, modular, comparison) and the four layers media, stream, object, specification with their abstractions and functions.

??? question "12. What is the importance of synchronization? Discuss the four-layer reference model. (8 marks)"
    Importance: correct presentation of lip-sync, slides with narration, conferencing, QoS; then the layer table.

??? question "13. Briefly describe synchronization specification. (6 marks)"
    Contents (intra, inter, QoS), categories (interval, axes, control-flow, event), scripts.

??? question "14. Explain synchronization in a distributed environment. (6 marks)"
    Transport of the specification (3 approaches), location, clock synchronization, multiple relations, six-step multi-step synchronization.

## Multiple choice

??? question "15. A 25 fps video needs each frame displayed for"
    - A. 25 ms
    - B. 40 ms
    - C. 80 ms
    - D. 250 ms

    **Answer: B.**

??? question "16. The layer with no explicit interface is the"
    - A. Media layer
    - B. Stream layer
    - C. Object layer
    - D. Specification layer

    **Answer: D.**

??? question "17. Pointing ahead of audio is tolerated up to"
    - A. 80 ms
    - B. 500 ms
    - C. 750 ms
    - D. 1000 ms

    **Answer: B.**

??? question "18. Time Petri nets belong to which specification category?"
    - A. Interval-based
    - B. Axes-based
    - C. Control-flow based
    - D. Event-based

    **Answer: C.**
