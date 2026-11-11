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
