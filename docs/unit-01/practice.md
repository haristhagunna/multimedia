# Unit 1: Practice Questions

Write your own answer on paper first, then click to reveal the model answer. Marks are a guide to how much detail the question deserves.

## Short answer

??? question "1. Define multimedia and medium. (3 marks)"
    A **medium** is the means for distribution and presentation of information (text, graphics, speech, music, video).

    **Multimedia** is the computer-controlled integration of text, graphics, drawings, still and moving images, animation, audio and any other media, where every type of information can be **represented, stored, transmitted and processed digitally**, and is usually delivered **interactively**.

??? question "2. List the five building blocks of multimedia and describe any two. (4 marks)"
    **Text, audio, graphics, video, animation.**

    Example descriptions: **Audio** is produced by vibration and perceived by hearing; in multimedia it takes the form of speech, effects and music. **Animation** is the rapid display of a sequence of images of 2D artwork or model positions to create an illusion of movement, due to persistence of vision.

??? question "3. State the four basic characteristics of a multimedia system. (4 marks)"
    1. **Computer controlled**: the computer controls production, storage, transmission and presentation.
    2. **Integrated**: all media and devices are integrated and controlled by one computer; digital storage is used for all media types.
    3. **Digitally represented**: analog signals are converted to digital, which can be processed effectively.
    4. **Interactive**: the user can choose the time, order and speed of presentation and can modify content.

??? question "4. Why is a text processor with embedded images not a multimedia application? (3 marks)"
    Text and still images are both **discrete** (time-independent) media. Multimedia requires the use of **both discrete and continuous** (time-dependent, such as audio and video) media. Adding an audio or video clip would make it multimedia.

??? question "5. Differentiate asynchronous, synchronous and isochronous transmission. (5 marks)"
    - **Asynchronous:** synchronization at the byte level; gaps between bytes are possible; good for random communication (WWW, e-mail, keyboard).
    - **Synchronous:** no start and stop bits; sender and receiver must be synchronized with clocks.
    - **Isochronous:** data is transferred at a fixed, steady rate; best for multimedia communication.

??? question "6. What is the role of the synchronization layer in the global structure? (3 marks)"
    It is a **vertical, cross-domain layer** that coordinates multiple media types **in time**: audio must match video, subtitles must appear at the right moment. It is critical for video conferencing, movies and e-learning. Poor synchronization causes audio-video mismatch and a poor user experience.

## Long answer

??? question "7. Draw and explain the global structure of multimedia. (8 marks)"
    Draw three stacked domains with a tall vertical **Synchronization** bar spanning them.

    - **Application domain**: tools and applications, documents, user interface, programming abstractions. It lets users develop and present multimedia projects; system services reach it through programming abstractions.
    - **System domain**: operating systems (CPU, memory, disk and I/O management, real-time scheduling, device drivers), database systems (store, search, index, retrieve multimedia objects), communication systems (protocols such as TCP/IP and RTP), on top of computer technology.
    - **Device domain**: storage, compression, network, and the media hardware for sound, image/graphics and video/animation.
    - **Synchronization (cross domain)**: temporal coordination of media across all domains.

??? question "8. Explain the classification of media with examples. (8 marks)"
    Six categories, each with a central question:

    | Medium | Central question | Examples |
    |---|---|---|
    | Perception | How do humans perceive information? | Seeing (text, image, video); hearing (music, noise, speech) |
    | Representation | How is information coded in the computer? | ASCII, JPEG, PCM, PAL/NTSC/SECAM, MPEG |
    | Presentation | Through which devices is information delivered and introduced? | Output: paper, screen, speaker. Input: keyboard, mouse, camera, microphone |
    | Storage | How is information stored? | Hard disk, CD-ROM, SSD |
    | Transmission | Over what is information transmitted? | Coaxial cable, fibre optics, free air space |
    | Information exchange | Which carrier moves information between places? | Storage plus transmission, e.g. e-mail |

??? question "9. Explain the challenges of multimedia computing and the desirable features of a multimedia system. (6 marks)"
    **Challenges:** synchronization; sequencing; latency and delay on distributed networks; large storage and very high bandwidth for continuous media; complex algorithms and hardware; automatic analysis and indexing of audio, image and video is harder than for text.

    **Desirable features:** very high processing power and real-time delivery; a multimedia file system; special hardware such as RAID; real-time compression and decompression; efficient I/O; terabytes of storage and gigabytes of memory with large caches and fast buses; network support for client-server and distributed use; software tools to handle and deliver media.

## Multiple choice

??? question "10. Which pairing is correct?"
    - A. Perception medium: how information is coded in the computer
    - B. Presentation medium: the devices through which information is delivered to and introduced into the computer
    - C. Storage medium: what information is transmitted over
    - D. Information exchange medium: how humans sense information

    **Answer: B.** A describes the representation medium, C the transmission medium, and D the perception medium.

??? question "11. A monitor is best classified as a"
    - A. Perception medium
    - B. Representation medium
    - C. Presentation medium
    - D. Transmission medium

    **Answer: C.** A screen is an output (presentation) device. Perception is the human sense that receives the image.

??? question "12. Which of these is a continuous (time-dependent) medium?"
    - A. A text document
    - B. A still photograph
    - C. A movie
    - D. A page of ASCII characters

    **Answer: C.** A movie's information depends on its time of occurrence. The others have no time component.

??? question "13. Which transmission mode is best for multimedia?"
    - A. Asynchronous
    - B. Synchronous
    - C. Isochronous
    - D. Parallel

    **Answer: C.** Isochronous transfer is at a fixed, steady rate. Asynchronous allows gaps between bytes; synchronous removes start and stop bits and relies on shared clocks; parallel is not one of the three modes, and multimedia communication is generally serial.

??? question "14. In the global structure, compression, storage and network belong to the"
    - A. Application domain
    - B. System domain
    - C. Device domain
    - D. Synchronization layer

    **Answer: C.** The system domain holds operating, database and communication systems; the application domain holds tools, documents, user interface and programming abstractions.

??? question "15. Which is NOT one of the four basic characteristics of a multimedia system?"
    - A. Computer controlled
    - B. Integrated
    - C. Analog representation
    - D. Interactive

    **Answer: C.** Multimedia information must be represented **digitally**.

??? question "16. Which of these correctly describes asynchronous transmission?"
    - A. No start and stop bits, clock-synchronized
    - B. Synchronization at the byte level, with possible gaps between bytes
    - C. Fixed-rate delivery
    - D. Parallel bit transfer

    **Answer: B.** A describes synchronous, C isochronous. D is not a transmission mode in the notes.

??? question "17. Which statement about 'combination of media' is correct?"
    - A. Any two media make a multimedia application
    - B. Multimedia requires both continuous and discrete media
    - C. Multimedia requires at least three discrete media
    - D. Multimedia requires only continuous media

    **Answer: B.** That is why a text processor with pictures (both discrete) is not multimedia.
