# Types and Components of Multimedia Systems

!!! source "Source"
    *Unit 12 – multimedia-application* slides 9–15.

## Types of multimedia systems

| Type | Description |
|---|---|
| **Home / entertainment systems** | **Mostly interactive but not live**; the interaction is **completely pre-programmed**. May include a **PC and a set-top box plus a TV**, connected to a **cable service** or an Internet service |
| **Business systems: dedicated** | Creation, storage and manipulation of multimedia objects happen **completely within the system** |
| **Business systems: departmental** | Use a **LAN** for **shared object storage management and processing**; support a specific business process shared by most users in the department |
| **Business systems: enterprise-wide** | **Many LANs and WANs interconnected**; share departmental or enterprise-level storage and processing; support **local, departmental and inter-departmental** applications |

## Components of a multimedia system

```mermaid
flowchart LR
    I["Input systems"] --> S["Storage systems"] --> O["Output systems"]
```

### Multimedia input systems

| Node | Role |
|---|---|
| **Scanning node** | Captures **still images and document images** |
| **User workstation** | May serve as **voice and video input** node |
| **Video capture node** | Needed because video capture needs **special hardware and software** |
| **Professional studio** | For **high-quality, professional** multimedia objects |

### Multimedia output systems

| Node | Role |
|---|---|
| **User workstation** | Output node for text, graphics, image, audio, video |
| **Teleconferencing studio** | A professional studio with **multiple monitors, sound systems and channel-switching controls** |
| **Print server** | **Hard-copy** output of text, graphics and images |
| **Fax server** | Data arriving through the **telephone channel** |
| **Gateway nodes** | Communication with **other systems** |

### Multimedia storage systems

Need **large on-line storage as well as near-line and off-line storage**, and the ability to **duplicate** objects.

| Server | Role |
|---|---|
| **Database server** | Normal database needs of a multimedia application |
| **Image server** | **Storage and indexing** of document images and graphics |
| **Voice mail server** | Voice messages |
| **Audio server** | Manages **digitised voice and audio objects**; can do **isochronous playback** |
| **Video server** | Must maintain **constant playback speed** and handle **very large data volumes** |
| **Duplication station** | **High-speed duplication** to recordable CDs, optical disks, etc. |

!!! exam "Exam tip"
    "List the components of a multimedia system" = input (scanner, workstation, video capture, studio), storage (the six servers), output (workstation, teleconferencing studio, print, fax, gateway).

## Checkpoint

??? question "Differentiate dedicated, departmental and enterprise-wide business systems."
    Dedicated: all inside one system. Departmental: LAN-based shared storage and processing for a department. Enterprise-wide: many interconnected LANs and WANs.

??? question "Why does a video server differ from an image server?"
    It must keep a constant playback rate and handle very large data volumes.
