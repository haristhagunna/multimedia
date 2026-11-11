# The Multimedia Development Cycle

```mermaid
flowchart LR
    P["1. Planning and costing"] --> D["2. Designing"] --> V["3. Developing and producing"] --> T["4. Testing and debugging"] --> L["5. Delivering"]
```

## 1. Planning and costing

Main concerns:

- capture the **ideas and requirements** of you or your clients;
- identify the **potential audience and users**;
- find the **benefit** of developing the application;
- evaluate **feasibility and cost** of the whole project (production, testing, delivery).

A **"back-of-the-envelope" or "paper napkin"** approach is often used: capture ideas and judge feasibility quickly. The most important considerations:

| Factor | Points |
|---|---|
| **Hardware** | The **most common limiting factor** for development time and end users: poor or no sound device, **limited storage**, **very narrow network bandwidth** |
| **Software** | **Development software is expensive**; software needed by end users adds up |
| **Contents** | Existing material may **not match** needs, may be **copyrighted** (permission may be refused); new material is **expensive and slow** |
| **Skills** | Very broad: **computer, artistic and application-domain** skills |

It helps to build a **pilot project or prototype** first.

## 2. Designing

A **creative activity** needing computer skills, **talent in graphic arts, video and music**, and knowledge of the **subject area**.

### Storyboarding

A **storyboard** describes the project **in exact detail with words and sketches** for each **screen image, sound and navigational choice**. It can be very detailed (every screen down to **colour, shade, text and attributes**) or only a schematic guide, drawn on **paper** or with a **computer tool**.

### Architecture

The **arrangement of the multimedia information**; a well-organised document lets users find information efficiently; start early. Types:

| Architecture | Structure |
|---|---|
| **Linear** | One path from start to end |
| **Hierarchical** | Tree of menus and sub-menus |
| **Non-linear** | Free links between nodes (hypermedia) |
| **Composite** | A mix of the above |

### User interface

The emphasis is on **multimedia presentation**; **content selection** is the key and is limited by the **size and complexity** of the presentation, the **quality of information**, **display hardware limits**, and the need for **completeness and coherence**. Media must be **"adequate"**: to teach tennis, **graphics and video** suit better than text. **Coordination** means composing the media.

**Interface techniques** (the remote **camera surveillance** example: a camera server on a serial interface, a remote client sends commands, video is digitised, compressed and sent):

- **Keyboard**: fixed commands on keys.
- **Buttons** in a GUI: clicking "left" pans left.
- **Scroll bars** beside the video window.
- **Special device**: a **joystick** is more natural.
- **Direct manipulation of the video window**: click a point to centre the camera there.

**User-friendliness** is the primary goal, though what it means and how to measure it are not always clear:

- **Easy to learn** and **easy to remember** instructions (for occasional and daily users);
- **Effective instructions**: logically connected functions presented together and similarly; **graphical symbols** beat text; media **exchangeable** between applications;
- **Prompt feedback** after each user action;
- Usable by **professional and occasional** users.

## 3. Developing and producing

Production is when the project is **actually rendered**. Tasks: **acquire all media elements**, **compose** them according to the storyboard, **track media elements** and **track progress**, and have a way (or an expert) to **solve technical problems quickly**.

### Rights and permissions

You must know who **owns** acquired content. There are **nine types of protected works**: **literary, dramatic, musical, artistic works; sound recordings, cinematograph films, television broadcasts, sound broadcasts, published editions of works**. **License the rights before use**; you may negotiate **outright ownership** or a **licence**. Questions to settle: **how** the material will be used and distributed; **fixed period**?; **exclusive or non-exclusive**?; **where** distributed?; does the owner have **authority** to assign rights?; **remuneration**?

## 4. Testing and debugging

An important and time-consuming phase.

| | Alpha testing | Beta testing |
|---|---|---|
| Who | **Internal**, the in-house team | A **wider range of testers**, **representative of real users**, **not those who built it** |

The product is used by many users who know little about computers and on **many platforms and configurations**, so test **widely**.

## 5. Delivering

Plan delivery **early**. **CD-ROM and the Internet** are the two most popular means (today also app stores and streaming). Plan **installation and use**. The distribution must include **all media elements** (clips), **runtime libraries** (Director runtime), **drivers** (DirectX), **helper programs** (QuickTime viewer, Acrobat reader) and the **installation program and compression/decompression programs**.

!!! exam "Exam tip"
    The five stages are a certain question. Add storyboard, architectures and alpha/beta testing for full marks.

## Checkpoint

??? question "Differentiate alpha and beta testing."
    Alpha: internal, in-house testers. Beta: wider group of representative users who were not part of the production.

??? question "Name the four types of architecture."
    Linear, hierarchical, non-linear, composite.
