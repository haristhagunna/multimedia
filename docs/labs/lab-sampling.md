# Lab 1: Sampling, quantization and aliasing

**Aim.** See Nyquist in action and measure how bit depth affects noise.

## Part A: Python

<p><a class="btn-s" href="code/sampling.py" download>Download sampling.py</a></p>

```python
"""Lab 1: sampling, quantization and aliasing. Needs numpy only (writes WAV files)."""
import wave
import numpy as np

def tone(freq, fs, seconds=1.0, bits=16):
    t = np.arange(int(fs * seconds)) / fs
    x = np.sin(2 * np.pi * freq * t)
    levels = 2 ** (bits - 1) - 1
    return np.round(x * levels).astype(np.int16 if bits == 16 else np.int8), levels

def save(name, samples, fs):
    with wave.open(name, "wb") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(fs)
        w.writeframes(samples.astype("<i2").tobytes())

def apparent_frequency(f, fs):
    """Frequency we actually see after sampling f at fs (folding about fs/2)."""
    f = f % fs
    return fs - f if f > fs / 2 else f

if __name__ == "__main__":
    fs = 8000
    for f in (1000, 3000, 5000, 7000):      # 5 kHz and 7 kHz exceed fs/2 = 4 kHz
        print(f"{f} Hz sampled at {fs} Hz appears as {apparent_frequency(f, fs)} Hz")
    x, _ = tone(5000, fs); save("alias_5k.wav", x, fs)
    x, _ = tone(1000, fs); save("tone_1k.wav", x, fs)
    # quantization noise: SNR grows ~6 dB per bit
    t = np.arange(fs) / fs; sig = np.sin(2 * np.pi * 440 * t)
    for bits in (4, 8, 12, 16):
        q = np.round(sig * (2 ** (bits - 1) - 1)) / (2 ** (bits - 1) - 1)
        snr = 10 * np.log10(np.mean(sig ** 2) / np.mean((sig - q) ** 2))
        print(f"{bits:2d} bits: SNR = {snr:5.1f} dB")
    size = 44100 * 16 * 2 * 60 // 8
    print("CD audio, 1 minute:", size, "bytes")
```

**Expected output**

```text
1000 Hz sampled at 8000 Hz appears as 1000 Hz
3000 Hz sampled at 8000 Hz appears as 3000 Hz
5000 Hz sampled at 8000 Hz appears as 3000 Hz
7000 Hz sampled at 8000 Hz appears as 1000 Hz
 4 bits: SNR =  25.1 dB
 8 bits: SNR =  51.0 dB
12 bits: SNR =  74.1 dB
16 bits: SNR =  98.2 dB
CD audio, 1 minute: 10584000 bytes
```

The SNR rises about **6 dB per bit**, which is why 16-bit audio has a dynamic range near 98 dB.

## Part B: Audacity

1. Open Audacity, **Generate → Tone** (sine, 5000 Hz, 2 s) with project rate 8000 Hz. Listen: you hear **3000 Hz**, not 5000 Hz.
2. Open `alias_5k.wav` (made by the script) and `tone_1k.wav`; compare them with **View → Show Spectrogram**.
3. Change the project rate to 44100 Hz and regenerate the 5 kHz tone; the alias disappears.

## Reflect

1. Why does the CD use 44.1 kHz and not exactly 40 kHz?
2. What would an anti-aliasing filter do before the ADC?
3. Which bit depth gives at least 90 dB SNR?
