# Image Analysis and Recognition

## Image analysis

**Image analysis** is concerned with **techniques for extracting descriptions of objects from images**. In some textbooks' terms, image-processing algorithms **alter an input image to create a new image**, or **extract image descriptions** (shape, position, orientation) for **higher-level analysis**.

Analysis techniques include:

- **Computation of perceived brightness and colour**.
- **Partial or complete recovery of 3D data** in a scene.
- **Location of discontinuities** that correspond to objects in the scene.
- **Characterisation of the properties of uniform regions** in the image.

It may also deal with calculating and comparing **intensity, hue and saturation**, the **centroid**, identifying **noise**, detecting **patterns**, or **recognising** the image itself.

### Analysis versus recognition

| | Image recognition | Image analysis |
|---|---|---|
| **Techniques** | Relies heavily on **classification models** | A **broader range**: segmentation, feature extraction, statistical analysis |
| **Purpose** | **Identifying and categorising** | **Detailed examination and understanding** of images |

### Applications of image analysis

- **Aerial surveillance** photographs
- **Slow-scan images** of the moon or planets from space probes
- **Television images** from an industrial robot's visual sensor
- **X-ray images** and **CAT (computerised axial tomography) scans**

## Areas of image processing

| Area | What it does | Example |
|---|---|---|
| **Image enhancement** | Improves quality by **removing noise** or **enhancing contrast** | X-ray images, CAT scans |
| **Pattern detection and recognition** | **Detects and classifies standard patterns** and finds **distortions** from the patterns | **OCR** (optical character recognition) |
| **Scene analysis** | Describes what is in a scene | |
| **Computer vision** | **Recognises and reconstructs 3D models** of a scene from several 2D images | A robot sensing the **size, shape, position and colour** of objects |

!!! info "Static versus dynamic recognition (OCR)"
    Recognising characters **while they are being written** is easier than recognising **scanned** characters, because a **dynamic recogniser records the sequence, direction, speed and pressure** of each stroke.

## Image recognition

To **fully recognise** an object in an image means knowing that there is **agreement between the sensory projections and the observed image**. How the object appears is given by the **spatial configuration of the pixel values**, so the observed configuration must agree with the expected one.

This requires two capabilities:

1. **Infer the object's position and orientation** from the spatial configuration. That means working out **which pixels belong to the object**, and distinguishing **features** such as special markings, curves and lines.
2. **Confirm the inference is correct** by **matching distinguishing image features with the corresponding object features**.

The **difficulty** of recognition depends on the **kind of object, the background, the imaging sensor** and similar factors. A simple **corner extraction** can identify some images.

## Steps of image recognition

!!! exam "Exam tip"
    This is a likely long question. Different books give **slightly different lists**: some give **six steps** (including **Grouping**), some **five** (no grouping). Learn the **six** and write them in this order. Mention grouping with one line.

```mermaid
flowchart LR
    A["1 Formatting"] --> B["2 Conditioning"]
    B --> C["3 Labeling"]
    C --> D["4 Grouping"]
    D --> E["5 Extracting"]
    E --> F["6 Matching"]
```

| # | Step | What happens |
|---|---|---|
| 1 | **Formatting** | **Capture the image** from a camera and bring it into **digital form**: a pixel representation. |
| 2 | **Conditioning** | **Preprocess** the data to make it suitable for recognition. Suppress **noise and background**, which hide informative patterns, and highlight the interesting parts. Tasks: **noise reduction, image enhancement, normalisation, feature extraction**. |
| 3 | **Labeling** | Assign **labels** to the structure. In other treatments: analyse adjacent pixels to find structure such as **edges** (**edge detection** finds continuous adjacent pixels that differ greatly in intensity or colour; a **threshold** filters out insignificant edges) and **corners**; edges and corners are **labelled**. In the main slides: assign **semantic labels or categories** to objects or patterns. |
| 4 | **Grouping** | **Organise similar objects or patterns** into groups, for example with **clustering** to form coherent regions. *(Unit 3 only.)* |
| 5 | **Extracting** | Compute a **list of properties for each group of pixels**: **centroid, area, orientation, spatial moments, gray-tone moments, number of holes, average curvature**. It also describes the **topological relationship** between groups. Techniques: edge detection, texture analysis, shape analysis. |
| 6 | **Matching** | **Compare each object** in the image with **previously stored models or templates** and determine the **best match**. Uses similarity measures, template matching or classifiers. |

## Checkpoint

??? question "Differentiate image analysis and image recognition."
    **Recognition** identifies and categorises, relying on **classification models**. **Analysis** is a broader, detailed examination using **segmentation, feature extraction and statistical analysis**.

??? question "Why is dynamic character recognition easier than scanned-character recognition?"
    Because a dynamic recogniser records the **sequence, direction, speed and pressure** of each stroke as it is written.

??? question "List the steps of image recognition in order."
    **Formatting, conditioning, labeling, grouping, extracting, matching.**
