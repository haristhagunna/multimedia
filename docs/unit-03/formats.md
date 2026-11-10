# Image and Graphics Formats

!!! source "Source"
    *Unit 3 – Image and Graphics* pp. 14–19; *mul c3* pp. 12–14.

The lecturer considers two distinct kinds of **image format**: the format in which the image is **created during digitising** (capturing format), and the format in which images are **stored and often transmitted** (storage format). **Graphics formats** are a separate case.

## Image capturing format

The format is specified by **two main parameters**:

1. **Spatial resolution**, indicated in **pixels** (pixels × pixels).
2. **Colour encoding**, specified by **bits per pixel**.

The values of both depend on the **hardware and software** used to input and output images.

- Example: a **SPARCstation** captures images at **320 × 240**.
- Colour encoding may be **1 bit, 8 bits or 24 bits**.

## Image storage format

The image is stored as a **two-dimensional matrix** in which **each value corresponds to the data for one pixel**.

- In **bitmaps** the values are **binary numbers**.
- In colour images it is good to store **RGB triples** (red, green and blue components).
- Example: a **640 × 480, 24-bit** colour image needs **900 KB** (921,600 bytes).

### File formats named by the lecturer

| Format | Extension(s) |
|---|---|
| Microsoft Windows DIB | .bmp, .dib, .rle |
| Microsoft Palette | .pal |
| AutoCAD format 2D | .dxf |
| JPEG (Joint Photographic/Picture Experts Group) | .jpg |
| Windows Metafile | .wmf |
| Portable Network Graphics | .png |
| CompuServe GIF (Graphics Interchange Format) | .gif |
| Apple Macintosh | .pict, .pic, .pct |

Other formats mentioned in the text: **X11 bitmap**, **PostScript**, **TIFF (Tagged Image File Format)**, and **IRIS** (in *mul c3*).

## Graphics format

**Graphics image formats** are **not specified by pixels**. They are specified through **graphics primitives and their attributes**.

| | Examples |
|---|---|
| **Graphics primitives** | Lines, rectangles, circles, ellipses, text strings (2D); polyhedron (3D) |
| **Graphics attributes** | Line style, line width, colour |

Primitives and attributes are a **higher-level** description of the image. At some point in processing, for example when the computer displays the image, this higher level must be **mapped to a lower level** (pixels).

| | Points |
|---|---|
| **Advantages** | **Reduces the data volume** stored for each image; allows **simpler image manipulation** |
| **Disadvantage** | An **additional conversion step** from primitives and attributes to the pixel representation |

### Graphics packages

| Package | Note from the notes |
|---|---|
| **SRGP** (Simple Raster Graphics Package) | Includes the primitives-to-bitmap conversion (one-way conversion to bit/pixmap) |
| **PHIGS** (Programmer's Hierarchical Interactive Graphics System) | A graphics standard of this type |
| **GKS** (Graphical Kernel System) | A graphics standard of this type; image representation only in pixmap |

## Comparison of the three formats

| | Capturing format | Storage format | Graphics format |
|---|---|---|---|
| Described by | Spatial resolution + bits per pixel | 2D matrix of pixel values | Primitives + attributes |
| When it matters | While **digitising** an image | When **saving or sending** an image | When describing an image **symbolically** |
| Depends on | Input/output hardware and software | File format chosen | Graphics package |
| Example | 320 × 240, 8 bits | GIF, JPEG, TIFF, PNG | SRGP, PHIGS, GKS |

!!! exam "Exam tip"
    A common question is "Explain image formats". Cover **capturing** (two parameters), **storage** (2D matrix, RGB triples, file formats) and **graphics** (primitives, attributes, advantage and disadvantage).

## Checkpoint

??? question "Which two parameters specify an image capturing format?"
    **Spatial resolution** in pixels and **colour encoding** in bits per pixel.

??? question "Give one advantage and one disadvantage of graphics primitives."
    **Advantage:** less data to store and simpler manipulation. **Disadvantage:** an extra conversion step from primitives and attributes to pixels.

??? question "Name four image file formats with their extensions."
    For example **GIF (.gif)**, **JPEG (.jpg)**, **PNG (.png)**, **Windows DIB (.bmp)**; also TIFF, DXF (.dxf) and PICT (.pict).
