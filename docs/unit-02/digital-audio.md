# Digital Audio and File Formats

## Computer representation of sound

The smooth, continuous curve of a sound wave **cannot be stored directly** in a computer. Instead:

1. The computer **measures the amplitude** of the waveform at **regular time intervals**.
2. This produces a series of numbers called **samples**.
3. The conversion is done by an **Analog-to-Digital Converter (ADC)**.
4. The reverse is done by a **Digital-to-Analog Converter (DAC)**.

An example of an ADC is the **AM79C30A digital subscriber controller chip**. A typical diagram shows the smooth pressure wave on the left and, on the right, the same wave as a row of vertical bars (the **samples**) whose heights follow the wave.

```mermaid
flowchart LR
    A["Sound wave (analog)"] --> B["Microphone / transducer"]
    B --> C["ADC: sample and quantize"]
    C --> D["Digital samples (numbers)"]
    D --> E["DAC"]
    E --> F["Speaker: sound wave"]
```

## Sampling rate

The rate at which a continuous waveform is sampled is the **sampling rate**, measured in **hertz**.

!!! exam "Nyquist sampling theorem"
    **For lossless digitization, the sampling rate should be at least twice the maximum frequency response.**

**Example.** The CD standard sampling rate is **44,100 Hz**: the waveform is sampled 44,100 times per second. A rate of 44,100 Hz can only represent frequencies **up to 22,050 Hz**, which is why it covers the audible range up to 20 kHz.

$$f_s \ge 2 f_{max} \qquad\Longleftrightarrow\qquad f_{max} \le \frac{f_s}{2}$$

## Quantization

The value of each sample must be stored as a **discrete** number. The **resolution (quantization)** of a sample depends on the **number of bits** used to measure the height of the waveform.

| Bits per sample | Number of levels | Example |
|---|---|---|
| 3-bit | 2³ = **8** | An illustration of coarse quantization |
| 8-bit | 2⁸ = **256** | Lower quality |
| 16-bit | 2¹⁶ = **65,536** | CD quality |

**The lower the quantization, the lower the quality of the sound.**

| | Controls | More means |
|---|---|---|
| **Sampling rate** | How often the wave is measured (time axis) | Higher frequencies captured |
| **Quantization (bits)** | How precisely each measurement is stored (amplitude axis) | Finer loudness detail |

## Quality versus file size

The size of a digital recording depends on the **sampling rate**, the **resolution** and the **number of channels**. Higher sampling rate and higher resolution give **higher quality but a bigger file**.

$$S = R \times \frac{b}{8} \times C \times D$$

| Symbol | Meaning | Unit |
|---|---|---|
| S | File size | bytes |
| R | Sampling rate | samples per second |
| b | Resolution | bits |
| C | Channels | 1 = mono, 2 = stereo |
| D | Recording duration | seconds |

Note: 1 KB = 1024 bytes and 1 MB = 1024 KB.

### Worked example

*Record 10 seconds of stereo music at 44.1 kHz, 16 bits.*

$$S = 44100 \times \frac{16}{8} \times 2 \times 10 = 1{,}764{,}000\ \text{bytes} = 1722.7\ \text{KB} \approx 1.68\ \text{MB}$$

High-quality sound files are very big, but the size can be reduced by **compression**.

!!! info "Extra: two extra practice calculations"
    - **Mono, 8 kHz, 8-bit, 1 minute:** S = 8000 × (8/8) × 1 × 60 = **480,000 bytes ≈ 468.75 KB**.
    - **Stereo, 44.1 kHz, 16-bit, 3 minutes (180 s):** S = 44100 × (16/8) × 2 × 180 = **31,752,000 bytes ≈ 30.3 MB**.

!!! exam "Exam tip"
    Always show the formula, substitute each value with its unit, and convert at the end (÷1024 for KB, ÷1024 again for MB). Forgetting **b/8** (bits to bytes) or the **channels** is the most common loss of marks.

## Audio file formats

| Format | Full name / origin | Key points |
|---|---|---|
| **WAV** | Waveform; developed by **Microsoft**; subset of RIFF | Most commonly used on Windows. Offers several encoding methods (including Wave or PCM), so check the player supports the one you use for Internet sound. |
| **AU** | **Sun Audio**; Sun Microsystems | For UNIX, NeXT and Sun SPARC workstations. A 16-bit compressed format, fairly common on the Web because it plays on the widest number of platforms. |
| **RA** | Progressive Networks **RealAudio** | Very popular for **streaming** on the Internet, with good compression **up to a factor of 18**. Streaming lets a file start playing before the whole file has downloaded. |
| **AIFF** | **Apple's Audio Interchange File Format** | The Macintosh waveform format; also supported on IBM compatibles and Silicon Graphics. Supports many sampling rates, up to 32 bits. |
| **MPEG / MPEG-2** | Motion Picture Experts Group | Compressed audio and video format, with compression of at least **14:1**. |

### Lossy and lossless formats

| | **Lossy** (smaller size, some quality loss) | **Lossless** (no quality loss, reduced size) |
|---|---|---|
| Formats | **MP3** (.mp3, most popular), **AAC** (.aac, better than MP3 at the same bitrate), **OGG Vorbis** (.ogg, open-source alternative to MP3), **WMA** (.wma, Microsoft) | **FLAC** (.flac, popular open source), **ALAC** (.m4a, Apple Lossless Audio Codec), **APE** (.ape, Monkey's Audio) |
| Typical use | Music streaming, portable devices | Archiving, high-quality playback |

## Checkpoint

??? question "State the Nyquist theorem and use it for a 44,100 Hz sampling rate."
    For lossless digitization, the sampling rate must be **at least twice the maximum frequency**. At 44,100 Hz the highest frequency that can be represented is **22,050 Hz**.

??? question "Calculate the size of 10 seconds of stereo audio at 44.1 kHz and 16 bits."
    S = 44100 × (16/8) × 2 × 10 = **1,764,000 bytes**, which is about **1722.7 KB** or **1.68 MB**.

??? question "Why are lossless formats used for archiving but lossy formats for streaming?"
    Lossless formats (FLAC, ALAC, APE) keep **all** the original quality while reducing size, so they suit archives. Lossy formats (MP3, AAC, OGG, WMA) give **much smaller files** with some quality loss, which suits streaming and portable devices.
