# Image and Graphics Basics

!!! source "Source"
    *Unit 3 – Image and Graphics* pp. 2–13; *mul c3* pp. 3–11.

## What is an image?

An **image** is a **spatial representation of an object**: a two-dimensional or three-dimensional scene, or another image. Abstractly, an image is a **continuous function defining a rectangular region of a plane**.

| Where it appears | Form of the image |
|---|---|
| Recorded image | Photograph, analog video signal, or digital format |
| Computer vision | Video image, digital image or picture |
| Computer graphics | Digital image |
| Multimedia | **All** of the above |

### The digital image

A **digital image** is a **matrix of numeric values** given by the function **I(r, c)**, where **r** and **c** are the **row and column** of a point.

- The point is called a **pixel**.
- **I(r, c)** is the **intensity value** (gray level) at that point.
- Gray scale for a monochrome picture: **0 and 1**. For an 8-bit image: **0 to 255**.
- The **number of pixels** is the **resolution**.

## Image versus graphics

!!! exam "Exam tip"
    This comparison is the most likely short question in the unit. Learn all four rows.

| | **Graphics** | **Image** |
|---|---|---|
| How it is made | Created in a **graphics application** and represented internally as an **assemblage of objects** such as lines, curves or circles | Comes from the **real world or is virtual**; captured from an analog signal by a **scanner or video camera**, or created with software tools |
| Semantics | The representation is **aware of semantics** | **Ignores semantic content** |
| Editing | Objects can be **individually deleted, added, moved or modified** later | **Object-based editing is not possible**, but tools exist for **enhancing and retouching** bitmap images |
| Storage | Stores an **abstract definition** (small) | Stores a **bitmap**: much more storage |
| Display | The definition must be **processed first** to produce a bitmap | **No processing needed** before display |

- The **smallest addressable image element** is a **pixel**.
- The **array of pixels** is a **bitmap**.
- **Drawback of bitmaps:** they need much more storage than graphics.
- **Advantage of bitmaps:** no processing before display.

## Bitmaps

A **bitmap** with **1 bit per pixel** is a **monochrome** image (this is what very early computers could manage): each pixel is either 0 (off) or 1 (on).

### Worked example 1: a 16 × 16 bitmap

The lecturer's figure shows a black cat drawn on a 16 × 16 grid, with the 0s and 1s printed beside it.

| Step | Working |
|---|---|
| Pixels | 16 × 16 = **256 pixels** |
| Bits per pixel | **1 bit** |
| Total bits | **256 bits** |
| In bytes | 256 / 8 = **32 bytes** |

### Worked example 2: a 640 × 480 bitmap

*mul c3* states a 640 × 480 bitmap needs **37.5 KB**: 640 × 480 = 307,200 bits, ÷ 8 = 38,400 bytes, ÷ 1024 = **37.5 KB**.

## Bitmap resolution

**Image resolution** is a **measure of pixel density**, given in **dots per inch (dpi)**. Smaller pixels fit more on the screen, which means a **higher pixel density**. A resolution of **300 dpi** means **300 pixels (dots) packed into each inch**.

### Worked example 3: a 100 × 100 bitmap

| Step | Working |
|---|---|
| Pixels | 100 × 100 = **10,000** |
| Bits | **10,000 bits** (1 bit per pixel) |
| Bytes | 10,000 / 8 = **1,250 bytes** |
| Kilobytes | 1,250 / 1,024 = **1.22 KB** |

## Colour bitmaps

To show colour you need **more bits per pixel**. The number of colours is 2 raised to the bits per pixel.

| Bits per pixel | Colours | Name |
|---|---|---|
| 1 | 2 | Monochrome |
| 4 | 16 | |
| 8 | 2⁸ = **256** | **Pseudo colour** (one byte per pixel) |
| 24 | 2²⁴ = **16,777,216** | **True colour** (three bytes per pixel) |

In **24-bit colour** each byte holds the intensity of one **primary colour: Red, Green and Blue**, each with **256 levels** (256 × 256 × 256 colours).

The **depth** of an image is the **number of bits used to represent each pixel**.

| | 8-bit (pseudo colour) | 24-bit (true colour) |
|---|---|---|
| Bytes per pixel | 1 | 3 |
| Colours | 256 | 256 × 256 × 256 |
| 640 × 480 image needs | **307.2 KB** | **921.6 KB** |

### Worked example 4: a 960 × 640 colour image

| Step | Working |
|---|---|
| Pixels | 960 × 640 = **614,400** |
| Bytes per pixel | **3** |
| Bytes | 614,400 × 3 = **1,843,200** |
| KB | 1,843,200 / 1,024 = **1,800 KB** |
| MB | 1,800 / 1,024 = **1.76 MB** |

## The general formula

$$\text{Size (bits)} = \text{width} \times \text{height} \times \text{bits per pixel} \qquad \text{Size (bytes)} = \frac{\text{width} \times \text{height} \times \text{bits per pixel}}{8}$$

!!! warning "KB means two things in the lecturer's slides"
    The slide on pseudo and true colour says a 640 × 480 24-bit image needs **921.6 KB** (that divides by **1000**). The slide on stored image format says **900K** (that divides by **1024**). Both come from 640 × 480 × 3 = **921,600 bytes**. In the exam, **state the byte count first**, then give the KB value and say which you divided by.

## Checkpoint

??? question "Differentiate an image and a graphic in two points."
    A **graphic** is stored as **objects** (lines, curves, circles) with semantics, so objects can be edited individually and the file is small but needs processing before display. An **image** is a **bitmap** of pixels that ignores semantics, needs more storage, and is displayed without processing.

??? question "How many bytes are needed for a 16 × 16 monochrome bitmap?"
    16 × 16 = 256 pixels at 1 bit each = 256 bits = **32 bytes**.

??? question "Why does a 24-bit image give 16,777,216 colours?"
    24 bits per pixel gives 2²⁴ = **16,777,216** combinations: 8 bits each for red, green and blue, each with 256 levels.
