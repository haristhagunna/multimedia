# Lab 3: Audio and video with FFmpeg

**Aim.** Measure how sampling rate, channels and codecs change size. All commands were run and the sizes below are from a 3-second 440 Hz test tone (yours will differ for your own files).

## Audio

```bash
# 1. make a test tone (3 s, 44.1 kHz stereo)
ffmpeg -f lavfi -i "sine=frequency=440:duration=3" -ar 44100 -ac 2 a.wav
# 2. reduce to telephone quality: 8 kHz mono
ffmpeg -i a.wav -ar 8000 -ac 1 a8k.wav
# 3. lossy compression to MP3 at 128 kbit/s
ffmpeg -i a.wav -c:a libmp3lame -b:a 128k a.mp3
```

| File | Size | Check by formula |
|---|---|---|
| a.wav | 529,278 bytes | 44,100 × 2 B × 2 ch × 3 s = 529,200 + header |
| a8k.wav | 48,078 bytes | 8,000 × 2 B × 1 ch × 3 s = 48,000 + header |
| a.mp3 | 48,945 bytes | 128 kbit/s × 3 s / 8 = 48,000 + header |

Headers account for the few extra bytes. Notice that a 128 kbit/s MP3 is about **11 times smaller** than the 1,411 kbit/s WAV.

## Video

```bash
# 1. test video 640x480, 25 fps, 2 s
ffmpeg -f lavfi -i testsrc=size=640x480:rate=25:duration=2 -c:v libx264 -crf 23 v.mp4
# 2. smaller frame, lower frame rate, stronger compression
ffmpeg -i v.mp4 -vf scale=320:240 -r 12 -c:v libx264 -crf 30 v_small.mp4
# 3. inspect
ffprobe -v error -show_entries stream=codec_name,width,height,r_frame_rate -of default=nw=1 v.mp4
# 4. extract the I-frames
ffmpeg -i v.mp4 -vf "select=eq(pict_type\,I)" -vsync vfr i%d.png
```

Compute the **raw** size of the 2-second 640 × 480 × 24-bit × 25 fps clip (= 46,080,000 bytes) and compare with the 17 KB H.264 file. That ratio is why compression matters.

## Reflect

1. Which steps were lossy? Which were lossless?
2. Why do I-frames matter for random access in MPEG-style video?
