# MIDI

## Why MIDI exists

A **sound signal** can be stored as a **digitised sequence of samples**. But **music** can also be described in a **symbolic way**, the way a printed score lists notes. Computers and electronic musical instruments use a similar technique, and most of them use **MIDI (Musical Instrument Digital Interface)**, a standard developed in the **early 1980s**.

- The MIDI standard defines how to **code all the elements of a musical score**: sequences of notes, timing conditions, and the instrument that plays each note.
- It is a set of **specifications for instrument development**, so instruments from **different manufacturers** can easily exchange musical information.
- Each word describing an action in a musical performance is assigned a **specific binary code**.

!!! exam "Samples versus instructions"
    Digitised audio stores **what the sound looked like** (thousands of sample values per second). MIDI stores **what to play** (which note, how loud, on which instrument). That is why a MIDI file is tiny and why it contains **no individual sample values**.

## The two components of a MIDI interface

| Component | What it does |
|---|---|
| **Hardware** | Connects the equipment. It adds a **MIDI port** to an instrument, specifies a **MIDI cable**, and processes the **electrical signals** over the cable. |
| **Data format** | Encodes the information the hardware processes. It does **not** encode individual sampling values; instead it uses a specific data format for each instrument, covering the **start and end of a score**, the **basic frequency**, the **loudness** and the **instrument itself**. |

A typical diagram shows a laptop (the digital audio workstation) connected to a synthesizer, a MIDI keyboard and an audio interface with **USB, audio and MIDI cables**.

## MIDI messages

The MIDI data format is **digital**, and data are grouped into **MIDI messages**. When a musician **plays a key**, the MIDI interface **generates a message** that defines the **start of each note** and its **intensity**. The message is **transmitted to the machines connected** to the system.

## MIDI devices, channels and instruments

- An instrument that complies with **both components** of the MIDI interface (hardware and data format) is a **MIDI device**. Example: a **synthesizer**.
- The MIDI standard specifies **16 channels**. A MIDI device is **mapped onto a channel**.
- The standard identifies **128 instruments** by number, including **noise effects** such as a phone ringing or an airplane taking off.

| Number | Instrument |
|---|---|
| 0 | Piano |
| 12 | Marimba |
| 40 | Violin |
| 73 | Flute |

## MIDI and SMPTE timing

### MIDI clock

- Used to **synchronise timing between MIDI devices**.
- It keeps all connected devices **playing in time** with each other, which is crucial for **rhythm and tempo** in live performances and recordings.
- As an alternative, the **SMPTE clock** allows receiver-sender synchronisation.

!!! warning "A number that does not match the MIDI standard"
    Some sources say the MIDI clock sends **2 timing ticks per quarter note**. The MIDI specification itself defines **24 timing clocks per quarter note**. Always quote the standard figure of 24 in exams.

### SMPTE timing code

- Developed by the **Society of Motion Picture and Television Engineers**.
- Uses the format **hours:minutes:seconds:frames**.
- Typically used in **film and television** to **precisely synchronise audio and video**.
- Requires **more bandwidth than a MIDI connection can support**, because it carries detailed timing information for **each frame**.

**Format:** `HH:MM:SS:FF`, where HH = hours, MM = minutes, SS = seconds, FF = frames.

| Frame rate | Used for |
|---|---|
| **24 fps** | Film |
| **25 fps** | PAL (Europe, Asia): Phase Alternating Line |
| **29.97 fps** | NTSC (TV): National Television System Committee |
| **30 fps** | Video production |

## MIDI versus SMPTE

This is a classic assignment question, so expect it in the exam.

| | **MIDI** | **SMPTE** |
|---|---|---|
| Stands for | Musical Instrument Digital Interface | Society of Motion Picture and Television Engineers (timing code) |
| Purpose | Exchange **musical information** between instruments and computers (notes, timing, instrument) | **Precisely synchronise audio and video** with a time code |
| Data | Messages describing a performance: start of notes, intensity, instrument, channel | **HH:MM:SS:FF** time stamps for each frame |
| Timing role | **MIDI clock** keeps devices in step (tempo) | Frame-accurate timing for film and television |
| Bandwidth | Light; can be carried on a MIDI connection | Needs **more bandwidth than a MIDI connection supports** |
| Example | A keyboard sending note messages to a synthesizer | A film editor lining up a soundtrack with video at 24 fps |

## MIDI software

| Type | Purpose | Examples |
|---|---|---|
| **MIDI player** | Plays MIDI music | Windows Media Player, the Creative MIDI player that comes with the sound card, freeware/shareware players such as Midigate and Yamaha Midplug |
| **MIDI sequencer** | Records, edits and plays MIDI | Cakewalk Express, Home Studio, Professional; Cubasis; Encore; Voyetra MIDI Orchestrator Plus |

**Configuration:** like audio devices, MIDI devices **require a driver**. Select and configure the MIDI device from the **control panel**.

## Checkpoint

??? question "Name the two components of a MIDI interface."
    The **hardware** (port, cable and electrical signalling) and the **data format** (messages that encode score start/end, frequency, loudness and instrument).

??? question "How many channels and instruments does the MIDI standard define?"
    **16 channels** and **128 instruments** (identified by number, including noise effects).

??? question "Why does SMPTE not run over an ordinary MIDI connection?"
    Because SMPTE carries **detailed timing information for every frame**, which needs **more bandwidth than a MIDI connection can support**.
