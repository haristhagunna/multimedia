# Unit 11: Practice Questions

Write your own answer on paper first, then click to reveal the model answer.

## Short answer

??? question "1. What are abstraction levels in programming multimedia? (3 marks)"
    Different approaches with a varying degree of detail for representing, accessing and manipulating multimedia data: device, library, system software, toolkit, higher language, object-oriented.

??? question "2. Why do multimedia applications depend on hardware? (3 marks)"
    They are mostly written in procedural languages with device-specific libraries, so changing a device often requires re-implementation.

??? question "3. What is a library and why are many libraries needed? (3 marks)"
    A set of functions to process continuous media supplied with the hardware. OS support is insufficient, and there is no common integration, so many libraries with different abstraction levels exist.

??? question "4. What are time capsules? (3 marks)"
    A file-system abstraction where each LDU carries its data type, value and valid life span.

??? question "5. Define stream and name the Windows interface for streams. (3 marks)"
    The continuous flow of audio/video from a source to a sink, set up before flow; operations play, fast forward, rewind, stop; MCI.

??? question "6. Name the three kinds of process in Nemo. (3 marks)"
    System, device and application processes (with the NTSC supervisor call).

??? question "7. What are the uses of toolkits? (3 marks)"
    Abstract from the physical layer, uniform device interface, client-server paradigm, hide process structures.

??? question "8. Define class, object, inheritance, polymorphism. (6 marks)"
    As in [Object-Oriented Approaches](object-oriented.md).

??? question "9. Define BMO, SMO and CMO. (4 marks)"
    See the table; CMO has orchestration and concatenation headers.

## Long answer

??? question "10. Explain the abstraction levels of programming multimedia systems. (8 marks)"
    Diagram and description of device, library, system software, toolkit, HLL, OO.

??? question "11. Explain media as types, files and processes. (8 marks)"
    The three views with examples (OCCAM-2 mixing, open/read/mix/activate/close, create/send).

??? question "12. State the requirements on an HLL for real-time continuous media. (5 marks)"
    Parallel processing; compile-time and dynamic process numbers; IPC meeting time requirements; no new language but a language extension (OCCAM-2, Ada).

??? question "13. Explain the object-oriented approaches to multimedia. (8 marks)"
    Application-specific, application-generic, devices, processing units, media, communication-specific classes.

??? question "14. Explain the distribution of BMOs and CMOs. (6 marks)"
    SG:BMO and ST:BMO, SMO, CMO with orchestration and concatenation headers, multi-user requirements.

## Multiple choice

??? question "15. The simplest abstraction level is the"
    - A. Library
    - B. Toolkit
    - C. Object-oriented
    - D. HLL

    **Answer: A.**

??? question "16. A cow 'is a' mammal shows"
    - A. Polymorphism
    - B. Inheritance
    - C. Instantiation
    - D. Encapsulation only

    **Answer: B.**

??? question "17. The orchestration header of a CMO describes"
    - A. Spatial relations
    - B. Temporal relations
    - C. Colour
    - D. Compression

    **Answer: B.**

??? question "18. In Windows, the interface for continuous media streams is"
    - A. MCI
    - B. SMIL
    - C. DTD
    - D. MHEG

    **Answer: A.**
