# Lab 2: Images, colour depth and YUV (GIMP)

**Aim.** Connect image size, colour depth and dithering to the formulas in Units 3 and 4.

## Steps

1. Open a photograph in GIMP. Read **Image → Scale Image** to note width × height.
2. Compute the uncompressed size: width × height × 3 bytes (24-bit). Compare with the file size on disk and state the compression ratio.
3. **Image → Mode → Indexed…** choose 16 colours, first with **no dithering**, then **Floyd-Steinberg**. Zoom to 400 % and compare banding versus noise.
4. **Colors → Components → Decompose…** choose **YCbCr_ITU_R470**. Look at the Y layer (the brightness) and the two colour layers; note that Y alone is a usable greyscale picture.
5. Export as JPEG at quality 90, 50 and 10. Record file sizes and describe the 8 × 8 block artefacts at 10.

## Record your results

| Setting | File size | Observation |
|---|---|---|
| PNG (lossless) | | |
| JPEG 90 | | |
| JPEG 50 | | |
| JPEG 10 | | |
| Indexed 16, no dither | | |
| Indexed 16, Floyd-Steinberg | | |

## Reflect

1. Why does the Y layer look sharp while Cb and Cr look blurry and still give a good picture? (Chroma subsampling.)
2. Which setting gives the best quality per byte for *this* photograph?
