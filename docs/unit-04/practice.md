# Unit 4: Practice Questions

Write your own answer on paper first, then click to reveal the model answer. Marks are a guide to how much detail the question deserves.

## Short answer

??? question "1. Define video and frame rate. (3 marks)"
    Video is a combination of image and audio: a sequence of still **frames** shown at a fixed speed, the **frame rate** in fps. Because of persistence of vision the frames merge into apparent motion; 20 to 30 fps looks smooth.

??? question "2. State the three aspects of video signal representation. (3 marks)"
    **Visual representation, transmission and digitization.**

??? question "3. What is the Kell factor? Compute the effective vertical resolution for 576 active lines. (4 marks)"
    Some detail falls between scan lines, so only about **70 %** of the vertical resolution is usable: the **Kell factor 0.7**. 576 × 0.7 = **403.2 lines**. Required horizontal resolution for 4:3 = 4/3 × 403.2 = **537.6**.

??? question "4. Define aspect ratio. Why must it be preserved? (2 marks)"
    Picture **width ÷ height** (4/3 for TV, 16/9 widescreen). If it differs between source and display the picture looks too wide or too narrow.

??? question "5. What is flicker and how is it avoided? (4 marks)"
    Periodic brightness fluctuation when the refresh rate is too low. Minimum refresh to avoid it: **50 Hz**. Avoid by **raising the refresh rate** or by **interlaced scanning** (odd lines then even lines, two fields per frame).

??? question "6. Calculate the video bandwidth for a = 1312, b = 800, c = 100 Hz. (3 marks)"
    a × b × c / 2 = 1312 × 800 × 100 / 2 = **52.48 MHz**. The division by 2 is because two adjacent pixels are scanned per cycle.

??? question "7. Calculate the raw frame size and data rate for 352 × 288, 16 bits/pixel, 25 fps. (4 marks)"
    Frame = 352 × 288 × 16 = **1,622,016 bits** (202,752 bytes). Rate = × 25 = **40,550,400 bits/s** ≈ **4.83 MB/s** (÷ 8 × 1024 × 1024).

??? question "8. Differentiate component and composite video signals. (4 marks)"
    Component (RGB, YUV, YIQ): separate signals, best quality, more bandwidth/wires. Composite: luminance and chrominance mixed into **one carrier**, cheaper, but **interference** between them, reduced by modulation.

??? question "9. Why is YUV used instead of RGB for broadcast? (3 marks)"
    Eye is more sensitive to **luminance** than chrominance; U and V can be scaled down to **save bandwidth**, and Y alone gives a **black-and-white** picture for old sets.

??? question "10. Write the equations for Y, U and V. (2 marks)"
    Y = 0.30R + 0.59G + 0.11B; U = 0.493(B − Y); V = 0.877(R − Y).

??? question "11. Define sampling and quantizing. (2 marks)"
    Sampling digitizes the **spatial position** (M × N points); quantizing digitizes the **colour/brightness** values.

??? question "12. Differentiate motion dynamics and update dynamics. (3 marks)"
    Motion dynamics: change of position (bouncing ball). Update dynamics: change of shape, size or structure (flower blooming).

??? question "13. What is in-betweening? Why are splines preferred to lerp? (4 marks)"
    Creating frames with intermediate positions between key frames. Lerp joins key positions by straight lines (a thrown ball with three keys moves unrealistically). **Splines smooth** the interpolation.

??? question "14. What is a pencil test? (2 marks)"
    A check that the animation is correct, done with an animation camera before cleaning and painting the drawings; pan and zoom can be applied.

??? question "15. Explain CLUT animation. (3 marks)"
    Colours are changed by cycling or editing the entries of the colour look-up table in the frame buffer, recolouring parts of the image; faster than sending a new pixmap each frame.

## Long answer

??? question "16. Explain the nine measures of visual representation of video. (8 marks)"
    Vertical detail and viewing distance (scan lines, Kell factor 0.7); horizontal detail and picture width (bandwidth, aspect ratio); total detail (vertical × horizontal elements); depth perception (perspective, focal length); luminance and chrominance (Y, U, V); temporal aspects of illumination; continuity of motion (>15 fps, 30 fps for filmed, 24 fps film, NTSC 29.97, PAL 25); flicker (≥ 50 Hz, interlacing); temporal aspect of bandwidth (a·b·c/2, 1/25 s per frame).

??? question "17. Explain RGB, YUV, YIQ and composite signals. (8 marks)"
    Describe each as in [Video Transmission](video-transmission.md): RGB for monitors, best colour but more bandwidth; YUV with equations and scaled chrominance; YIQ for NTSC with Q needing less bandwidth; composite all in one carrier with interference and modulation.

??? question "18. Explain the raster display architecture and the role of the video controller and CLUT. (6 marks)"
    Graphics program → display controller (writes pixels into refresh buffer) → video controller (reads buffer in sync with scan, uses CLUT to turn pixel values into R, G, B analog signals) → monitor. CLUT: pixel value as an address to three colour values.

??? question "19. Explain the three categories of animation languages with examples. (6 marks)"
    Linear list (frame numbers + event, Scefo/SMIL, the PALM example), general purpose (embedded in a programming language, ASAS on LISP), graphical (picture of action, GENESYS, DIAL, S-Dynamics).

??? question "20. Describe any four methods of controlling animation. (8 marks)"
    Full explicit control (BBOP), procedural control, constraint-based (Sketchpad), tracking live action (rotoscoping, data glove), kinematics and dynamics. One paragraph each.

??? question "21. Explain display of animation and double buffering. (6 marks)"
    Objects scan-converted into pixmap; at least 10 (preferably 15–20) per second so ≤ 100 ms per image; single buffer cannot erase/redraw in time; use two buffers, display one while building the other.

??? question "22. Compare symbolic and pixmap transmission of animation. (6 marks)"
    Use the table in [Display and Transmission](animation-display-and-transmission.md).

## Multiple choice

??? question "23. The minimum refresh rate to avoid flicker is"
    - A. 15 Hz
    - B. 24 Hz
    - C. 50 Hz
    - D. 100 Hz

    **Answer: C.**

??? question "24. The PAL frame rate is"
    - A. 24
    - B. 25
    - C. 29.97
    - D. 30

    **Answer: B.** NTSC is 29.97.

??? question "25. Which signal does NTSC use?"
    - A. YUV
    - B. YIQ
    - C. RGB only
    - D. S-video only

    **Answer: B.**

??? question "26. The Kell factor is about"
    - A. 0.3
    - B. 0.5
    - C. 0.7
    - D. 0.9

    **Answer: C.**

??? question "27. Which language is general purpose?"
    - A. Scefo
    - B. ASAS
    - C. GENESYS
    - D. SMIL

    **Answer: B.** ASAS is built on LISP.

??? question "28. Which transmission method has shorter display time?"
    - A. Symbolic
    - B. Pixmap
    - C. Both equal
    - D. Neither

    **Answer: B.**

??? question "29. A thrown ball animated by lerp with three key frames looks unrealistic. The fix is"
    - A. Splines
    - B. More colours
    - C. Interlacing
    - D. YUV

    **Answer: A.**
