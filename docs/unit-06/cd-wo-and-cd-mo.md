# CD-WO and CD-MO

Both are defined in the **Orange Book**: **Part II = CD-WO**, **Part I = CD-MO**. They extend the CD family from read-only (RO) to write-once (WO) and read/write (R/W).

## CD Write-Once (CD-WO)

**Layers** (from the top): protective layer, reflective layer, **absorption layer**, substrate (with a **pre-grooved track**).

**Principle**

- A **pre-grooved track** guides the writing laser.
- An **absorption layer** sits between the substrate and the reflective layer.
- A stronger write laser **heats the absorption layer**, causing an **irreversible change of its reflection characteristics**, which acts as the pits. The data **cannot be erased**.
- A CD-WO can be **played in CD-DA players**.

**Sessions**

A CD player needs a table of contents. A CD-WO is written in **sessions**, each with a **lead-in, data part and lead-out**; **new sessions can be added**, up to **99 sessions**.

```mermaid
flowchart LR
    LI1["Lead-in"] --> D1["Information"] --> LO1["Lead-out"] --> LI2["Lead-in"] --> D2["Information"] --> LO2["Lead-out"] --> M["..."]
```

| | Regular CD-WO | Hybrid CD-WO |
|---|---|---|
| Sessions | **One** | **Several** |

Players made before **1992** can read only the **first session**.

## CD Magneto-Optical (CD-MO)

**Features:** write, read, **erase and rewrite**. Orange Book Part I. Capacity about **650 MB** (double-sided), data rate about **1.2 Mbit/s**.

**Principle of the magneto-optical technique**

| Operation | How |
|---|---|
| **Write** | **Heat** a block and apply a magnetic field (about **10 × the earth's field**); the single elements are **polarized** |
| **Erase** | Apply a **constant magnetic field** while **heating the block** |
| **Read** | The **polarization of the light** is influenced by the magnetic properties of the surface |

**Areas**

- **Optional premastered area:** read-only, readable on any CD player, uses Red, Yellow and Green Book specifications.
- **Rewritable area:** uses different magneto-optical encoding, **incompatible with other CDs** and **cannot be read by standard CD players**.

## Overall summary of the CD family

- Features: usable for **all kinds of storage**, wide application area, **large capacity**, based on CD-DA (except CD-MO), specifications built sequentially.
- Disadvantages: **long average access time**; **incompatibility of CD-MO**.
- Future (the common view): CDs with **more storage and faster retrieval**, and **smaller discs with similar capacity**.

| | CD-ROM | CD-WO | CD-MO |
|---|---|---|---|
| Write | No (pressed) | **Once** | **Many times** |
| Principle | Pits stamped | Heat changes absorption layer | Heat + magnetic polarization |
| Standard | Yellow | Orange II | Orange I |
| Compatible with CD players | Yes | Yes (CD-DA players can play) | **Rewritable area: No** |

!!! exam "Exam tip"
    "Explain the principle of CD-WO" needs: pre-grooved track, absorption layer, irreversible heating, sessions and 99-session limit, regular vs hybrid. For CD-MO give write/erase/read.

## Checkpoint

??? question "Why can a CD-WO not be rewritten?"
    The heating changes the absorption layer irreversibly.

??? question "Why can't standard CD players read the rewritable area of a CD-MO?"
    It uses magneto-optical encoding (polarization of light) unlike pits and lands.
