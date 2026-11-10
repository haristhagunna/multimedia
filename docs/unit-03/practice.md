# Unit 3: Practice Questions

Write your own answer on paper first, then click to reveal the model answer. Marks are a guide to how much detail the question deserves.

## Short answer

??? question "1. Differentiate an image and a graphic. (4 marks)"
    - **Graphic:** created in a graphics application; internally an **assemblage of objects** (lines, curves, circles); **aware of semantics**; objects can be **individually deleted, added, moved or modified**; small storage but the abstract definition must be **processed to produce a bitmap** before display.
    - **Image:** from the real world or virtual (scanner, video camera, software); a **bitmap** of pixels that **ignores semantics**; no object-based editing (only enhancing and retouching); **much more storage** but **no processing** before display.

??? question "2. Calculate the storage needed for a 64 × 64 monochrome bitmap. (2 marks)"
    64 × 64 = 4,096 pixels × 1 bit = 4,096 bits = **512 bytes**.

??? question "3. Calculate the size of a 800 × 600 true-colour (24-bit) image. (3 marks)"
    800 × 600 = 480,000 pixels × 3 bytes = **1,440,000 bytes** = 1,406.25 KB ≈ **1.37 MB**.

??? question "4. Find the size of a 1024 × 768 image at 8 bits per pixel. (3 marks)"
    1024 × 768 = 786,432 pixels × 1 byte = **786,432 bytes = 768 KB = 0.75 MB**.

??? question "5. Why does a 24-bit image support 16,777,216 colours? (2 marks)"
    24 bits per pixel give 2²⁴ = 16,777,216 combinations: **8 bits each for red, green and blue**, each primary having 256 levels (256 × 256 × 256).

??? question "6. Define image synthesis and give three applications. (4 marks)"
    Image synthesis is the **generation of images of real or imaginary objects**. It is part of all computer user interfaces and indispensable for visualising 2D, 3D and higher-dimensional objects. Applications: **user interface** (point-and-click, menu-driven), **office automation and electronic publishing** (desktop publishing, hypermedia), **simulation and animation** for scientific visualisation and entertainment (fluid-flow models, cartoons, flying logos).

??? question "7. Differentiate motion dynamics and update dynamics with examples. (3 marks)"
    **Motion dynamics:** objects move or are activated relative to a static observer (or the environment moves), e.g. a **flight simulator**. **Update dynamics:** the shape, colour or other properties of objects actually change, e.g. **deformation of an in-flight aeroplane structure**.

??? question "8. What is dithering and why is it useful? (4 marks)"
    Dithering produces **shades of gray or tints of colour** on output devices (monitors, some printers) using fewer colours. It exploits the eye's **spatial integration**: from a distance the eye averages fine detail and records overall intensity. It is also called **halftoning**; the shades are **halftones**.

??? question "9. A 2 × 2 dither matrix is used for each of the red, green and blue channels. How many colours can be shown? (2 marks)"
    A 2 × 2 matrix gives **5 intensity levels** per channel (0 to 4 dots lit). 5 × 5 × 5 = **125 colours**.

??? question "10. Differentiate image analysis and image recognition. (3 marks)"
    **Recognition** identifies and categorises, relying heavily on **classification models**. **Analysis** is a broader, detailed examination using **segmentation, feature extraction and statistical analysis**.

??? question "11. State three network requirements for image transmission. (3 marks)"
    The network must accommodate **bursty** data (large images); transport should be **reliable**; **time dependence is not dominant**, unlike audio and video.

## Long answer

??? question "12. Explain the framework of an interactive graphics system. (8 marks)"
    Three software components (plus hardware):

    1. **Application model**: the data or objects to be pictured (descriptions of primitives, attributes and connectivity), stored in an **application database**, application-specific and independent of any display system.
    2. **Application program**: converts the model into graphics-system commands in **two steps**: **extract** the portions to be viewed (selection or query), then **convert** the geometry to the proper format; it sends a series of graphics output commands.
    3. **Graphics system**: the **intermediary** between program and display hardware that actually produces the picture, performing **output transformations** (model to view) and **input transformations** (user actions to application inputs).
    4. **Graphics hardware**: input devices (mouse, tablet, touch panel, trackball, data glove) and a **raster display**.

??? question "13. Explain the working of a raster display. (6 marks)"
    A CRT has rows of **phosphor dots** that glow when hit by electrons from the **electron gun**. Picture information is held in the **refresh buffer**. The **video controller** reads the buffer and turns the beam on and off, **one row at a time, top to bottom**; after each row the beam returns to the start of the next row (**horizontal retrace**). A **display controller** interprets output commands; in a PC it is software in a graphics library and the refresh buffer is part of CPU memory.

??? question "14. Explain the steps of image recognition. (8 marks)"
    **Formatting** (capture and digitise); **conditioning** (suppress noise and background, highlight informative patterns); **labeling** (find structure such as edges and corners by edge detection with a threshold; label them); **grouping** (cluster similar patterns into coherent regions); **extracting** (compute properties of each group: centroid, area, orientation, moments, holes, curvature, and relationships between groups); **matching** (compare each object with stored models or templates and pick the best match).

??? question "15. Explain the three formats for image transmission. (6 marks)"
    **Raw:** transmitted in digital form from the video digitiser; size = spatial resolution × pixel quantization (e.g. 640 × 480 × 8 = 2,457,600 bits = 307,200 bytes). **Compressed:** compressed (JPEG, MPEG) before transmission; size depends on method and rate. **Symbolic:** primitives, attributes and control information, as in computer graphics; size equals the structure carrying the symbols.

## Multiple choice

??? question "16. Which is true of a bitmap compared with graphics?"
    - A. It needs less storage
    - B. It needs no processing before display
    - C. Its objects can be individually moved
    - D. It stores primitives and attributes

    **Answer: B.** A, C and D describe graphics.

??? question "17. A 16 × 16 monochrome bitmap needs"
    - A. 16 bytes
    - B. 32 bytes
    - C. 256 bytes
    - D. 2,048 bytes

    **Answer: B.** 256 pixels × 1 bit = 256 bits = 32 bytes.

??? question "18. How many colours does an 8-bit pixel allow?"
    - A. 8
    - B. 128
    - C. 256
    - D. 65,536

    **Answer: C.** 2⁸ = 256.

??? question "19. Which pair describes graphics formats?"
    - A. Pixels and resolution
    - B. Primitives and attributes
    - C. Dpi and bit depth
    - D. Fields and frames

    **Answer: B.** Graphics formats are specified through primitives (lines, circles, polyhedra) and attributes (line style, width, colour).

??? question "20. Which technique suits devices that cannot display individual dots, such as laser printers?"
    - A. Dispersed-dot ordered dithering
    - B. Clustered-dot ordered dithering
    - C. Edge detection
    - D. Pulse code modulation

    **Answer: B.** Dispersed-dot dithering is for devices (such as CRTs) that can display individual dots.

??? question "21. In image recognition, which step compares objects with stored models?"
    - A. Conditioning
    - B. Labeling
    - C. Extracting
    - D. Matching

    **Answer: D.** Matching compares each object with stored models and selects the best match.

??? question "22. Which statement about image transmission is correct?"
    - A. It is dominated by time dependence, like video
    - B. It is bursty and needs reliable transport
    - C. It never uses compression
    - D. Its size is always equal to the structure size

    **Answer: B.** A is false (time dependence is not dominant), C is false (JPEG/MPEG are used), and D is true only for symbolic transmission.
