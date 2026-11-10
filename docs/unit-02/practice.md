# Unit 2: Practice Questions

Write your own answer on paper first, then click to reveal the model answer. Marks are a guide to how much detail the question deserves.

## Short answer

??? question "1. Differentiate sound and audio. (3 marks)"
    **Sound** is mechanical wave energy (longitudinal sound waves) that travels through a medium and causes pressure variations: the action of vibration. **Audio** is electrical energy (an analog or digital signal) that represents sound: the end result, the technology used to hear sounds from natural or human-made sources. A microphone's transducer converts the sound energy into a voltage.

??? question "2. Define frequency and amplitude, with units and the audible range. (4 marks)"
    **Frequency:** reciprocal of the period; the number of periods per second, in hertz. The human audible range is **20 Hz to 20 kHz**.
    **Amplitude:** displacement of the air-pressure wave from its mean value; perceived as loudness; measured in **decibels**.

??? question "3. State the Nyquist sampling theorem and explain why CD audio uses 44.1 kHz. (3 marks)"
    For lossless digitization the sampling rate must be **at least twice the maximum frequency**. A rate of 44,100 Hz can represent frequencies up to **22,050 Hz**, which covers the audible range up to 20 kHz.

??? question "4. A recording is 30 seconds of mono sound at 22.05 kHz and 8 bits. Find the file size. (3 marks)"
    S = R × (b/8) × C × D = 22050 × (8/8) × 1 × 30 = **661,500 bytes** ≈ 646.0 KB ≈ 0.63 MB.

??? question "5. Differentiate MIDI and SMPTE with a suitable example. (5 marks)"
    **MIDI** is a standard (hardware plus data format) for exchanging **musical information** (notes, timing, instrument, channel) between instruments and computers. It stores **instructions**, not samples. **SMPTE** is a **time code** (HH:MM:SS:FF) used in film and television to **precisely synchronise audio and video**; it needs **more bandwidth than a MIDI connection** because it carries timing for each frame.
    *Example:* a keyboard sends note messages to a synthesizer over MIDI; a film editor aligns a soundtrack to video at 24 fps using SMPTE.

??? question "6. Differentiate a phone, an allophone and a morph. (3 marks)"
    A **phone** is the smallest speech unit that distinguishes one word from another (*m* of *mat*). **Allophones** are variants of a phone (aspirated *p* of *pit*, unaspirated *p* of *spit*). A **morph** is the smallest speech unit that carries meaning (*consider*).

??? question "7. Differentiate voiced and unvoiced sounds. (2 marks)"
    **Voiced** sounds are produced by the oscillation of the vocal cords (*m*, *v*, *l*) and depend strongly on the speaker. **Unvoiced** sounds are produced with the vocal cords open (*f*, *s*) and are relatively independent of the speaker.

??? question "8. What is an acoustic fingerprint, and what is it used for? (2 marks)"
    A digitally stored speech probe of a person (for example a certain statement), used to **identify and verify** the speaker.

## Long answer

??? question "9. Explain how an analog sound wave is converted to digital form, including sampling, quantization and the effect on file size. (8 marks)"
    - The computer **measures the amplitude** at regular time intervals to give **samples**; an **ADC** does this and a **DAC** reverses it.
    - **Sampling rate** (Hz): by **Nyquist**, at least twice the highest frequency. CD standard 44,100 Hz represents up to 22,050 Hz.
    - **Quantization**: the bits per sample set the number of levels (8-bit = 256, 16-bit = 65,536, 3-bit = 8). Fewer bits give lower quality.
    - **File size** S = R × (b/8) × C × D. Example: 10 s stereo at 44.1 kHz and 16 bits = 1,764,000 bytes ≈ 1.68 MB. Higher rate and resolution give higher quality but bigger files; **compression** reduces the size.

??? question "10. Explain MIDI: purpose, interface components, messages, devices and software. (8 marks)"
    - **Purpose:** describe music symbolically (notes, timing, instrument) so instruments from different makers can exchange information; standard from the early 1980s.
    - **Components:** **hardware** (MIDI port, cable, electrical signals) and **data format** (start/end of score, basic frequency, loudness, instrument; no sample values).
    - **Messages:** playing a key generates a message defining the **start of the note and its intensity**, sent to connected machines.
    - **Devices:** an instrument complying with both components (for example a synthesizer); **16 channels**; **128 instruments** (0 piano, 12 marimba, 40 violin, 73 flute).
    - **Software:** MIDI **players** and **sequencers**; devices need a **driver** configured from the control panel.

??? question "11. Explain time-dependent and frequency-dependent sound concatenation in speech generation. (6 marks)"
    **Time-dependent:** stored sound segments are pieced together as building blocks (phones, **diphones**, syllables, whole words). A few phones give an unlimited vocabulary; whole words give the best pronunciation. Natural-sounding but needs extensive databases and careful transitions.
    **Frequency-dependent:** e.g. **formant synthesis**; formants are frequency maxima in the spectrum; mathematical vocal-tract models control formant frequency and amplitude. Flexible and low storage, but harder to make natural.

??? question "12. Describe speech recognition with a block diagram. (8 marks)"
    **Definition:** converting an acoustic signal from a microphone or telephone into a set of words (written text). It depends on speaker (dependent/independent), speech (discrete words/continuous), vocabulary (small/large) and environment (quiet/noisy).
    **Principle:** *extract characteristics to reduce data*: **speech analysis** (parameter and property extraction) feeds **pattern recognition** (comparison with reference storage and a decision) to give recognised speech.
    **Steps:** **acoustic and phonetic analysis** (sound patterns, word models) → **syntactical analysis** (syntax) → **semantic analysis** (semantics) → understood speech.

??? question "13. Explain the principles of speech transmission. (6 marks)"
    **PCM:** digitises the waveform, ignores speech-specific properties, favours accurate representation over data reduction. **Source encoding:** uses signal properties (silence suppression, parametric systems such as the channel vocoder); chain A/D → speech analysis → coded signal → reconstruction → D/A. **Recognition/synthesis:** recognition at the sender, synthesis at the receiver, and only the characteristics of the speech elements are transmitted.

## Multiple choice

??? question "14. The human audible range is"
    - A. 0 to 20 Hz
    - B. 20 Hz to 20 kHz
    - C. 20 kHz to 1 GHz
    - D. 1 GHz to 10 THz

    **Answer: B.** A is infrasound, C ultrasound, D hypersound.

??? question "15. A CD sampling rate of 44,100 Hz can represent frequencies up to"
    - A. 44,100 Hz
    - B. 22,050 Hz
    - C. 88,200 Hz
    - D. 16,000 Hz

    **Answer: B.** By the Nyquist theorem the maximum frequency is half the sampling rate.

??? question "16. How many levels does 16-bit quantization give?"
    - A. 256
    - B. 4,096
    - C. 65,536
    - D. 16

    **Answer: C.** 2¹⁶ = 65,536. 256 is 8-bit.

??? question "17. In the file-size formula S = R × (b/8) × C × D, what does C stand for?"
    - A. Compression ratio
    - B. Number of channels
    - C. Clock rate
    - D. Codec

    **Answer: B.** C is the number of channels (1 = mono, 2 = stereo).

??? question "18. How many channels does the MIDI standard specify?"
    - A. 8
    - B. 16
    - C. 64
    - D. 128

    **Answer: B.** 16 channels. 128 is the number of instruments.

??? question "19. SMPTE time code is expressed as"
    - A. HH:MM:SS:FF
    - B. DD:MM:YYYY
    - C. kbps:fps
    - D. Hz:dB

    **Answer: A.** Hours, minutes, seconds and frames.

??? question "20. Which technique builds speech from formants?"
    - A. Time-dependent sound concatenation
    - B. Frequency-dependent sound concatenation
    - C. Pulse code modulation
    - D. Silence suppression

    **Answer: B.** Formants are frequency maxima, so formant synthesis is frequency-dependent.

??? question "21. Which of these is a lossless audio format?"
    - A. MP3
    - B. AAC
    - C. FLAC
    - D. WMA

    **Answer: C.** MP3, AAC and WMA are lossy.

??? question "22. In the recognition/synthesis method of speech transmission, recognition takes place"
    - A. At the receiver
    - B. At the sender
    - C. On the network
    - D. Nowhere; only synthesis is used

    **Answer: B.** Recognition at the sender, synthesis at the receiver, and only the characteristics of the speech elements are transmitted.
