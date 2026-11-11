# Document Architecture: SGML, ODA and MHEG

## SGML: Standard Generalized Markup Language (ISO 8879, 1986)

- A **meta-language** for defining **markup languages**. The document is **text with tags** that mark its **logical structure**; **layout is not specified** (left to the application).
- Parts of an SGML system:
  - **Document Type Definition (DTD):** declares the **allowed elements**, their **order and nesting** and **attributes**.
  - The **document instance:** the marked-up content.
  - **Entities:** named pieces of text or data.
- **HTML** is an SGML application; **XML** is a simplified subset.

```
<!ELEMENT book (title, chapter+)>
<!ELEMENT chapter (heading, paragraph*)>
<!ELEMENT title (#PCDATA)>

<book>
  <title>Multimedia</title>
  <chapter><heading>Audio</heading><paragraph>Sound is ...</paragraph></chapter>
</book>
```

- **Advantages:** platform independent, long-lived, validated by the DTD, reusable. **Limits:** no layout, no time or multimedia synchronisation (hence **HyTime**, an SGML-based standard for hypermedia and time).

## ODA: Open Document Architecture (ISO 8613)

- An architecture for **interchange of documents** between systems of different vendors, covering **structure, content and layout**.
- **Two structures** per document:

| Structure | Contains |
|---|---|
| **Logical structure** | Chapters, sections, paragraphs (the author's view) |
| **Layout structure** | Pages, blocks, frames (the reader's view) |

- A **document profile** holds attributes of the document as a whole.
- **Content architectures:** **character** content, **raster graphics** and **geometric graphics**. (Later extensions added audio and video.)
- **Forms:** **formatted** (FF), **processable** (PF), **formatted processable** (FPF).
- **Interchange formats:** ODIF (data stream) and ODL (language).
- Compared with SGML: ODA includes **layout** as well as logical structure.

## MHEG: Multimedia and Hypermedia information coding Experts Group (ISO/IEC 13522)

- A standard for the **coding of multimedia and hypermedia information objects for interchange** between applications and systems, especially **interactive TV and set-top boxes** (final-form, run-time use).
- **Object-oriented:** a document is a set of **MHEG objects** that a receiver (the **MHEG engine**) interprets and presents. It is **not an authoring or editing format**: it is the **final form**.
- Main classes of objects:

| Class | Role |
|---|---|
| **Content** | Wraps the media data (text, graphic, audio, video) and its coding |
| **Selection / Modification / Interaction** | Offer user choices and interaction |
| **Composite** | Groups other objects into a presentation or scene |
| **Action** | Operations on objects (start, stop, set volume) |
| **Link** | **Condition → action**: when an event happens, do the actions |
| **Script** | Embeds a program for complex behaviour |
| **Descriptor** | Describes the resources an object needs, for negotiation |
| **Container** | A package of objects for interchange |
| **Macro** | Reusable definitions |

- MHEG supports **time-based presentation**, **spatial layout**, **links and interaction**, so it covers what SGML and ODA do not (synchronised multimedia).
- **MHEG-5** (a simplified, widely used version) is used for **digital TV** in several countries.

| | SGML | ODA | MHEG |
|---|---|---|---|
| Describes | Logical structure by markup | Logical + layout of documents | Final-form multimedia objects |
| Time and media | No | Limited | **Yes (synchronised)** |
| Typical use | Publishing, HTML/XML | Office document interchange | Interactive TV, multimedia interchange |

!!! exam "Exam tip"
    "Compare SGML, ODA and MHEG" is a table question. For MHEG always mention **objects**, **final form**, **links (condition–action)** and **interactive TV**.

## Checkpoint

??? question "What does a DTD define?"
    The elements, their allowed structure and order, and attributes of an SGML document type.

??? question "Which standard of the three handles time-based multimedia?"
    MHEG.

??? question "What are the two structures of an ODA document?"
    Logical and layout structure.
