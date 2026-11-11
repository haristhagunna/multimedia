# Animation Languages and Control

## Animation languages (three categories)

### 1. Linear-list notations

Text-based scripts where each event gives **start frame, end frame and action**, written sequentially like a list. Easy to follow; used in early multimedia and timeline-based engines.

!!! example "Example"
    `42, 53, B, ROTATE "PALM", 1, 30` means: between frames 42 and 53 rotate the object PALM about axis 1 by 30 degrees, the amount per frame being taken from table B.

Examples: **Scefo** (SCEne FOrmat); **SMIL** (Synchronized Multimedia Integration Language) with `<seq>` and `<par>`; a traffic light script: `00s setColor light RED`, `05s … YELLOW`, `07s … GREEN`, `12s … RED`.

### 2. General-purpose languages

Animation capability **embedded in a general programming language**; variables of the language serve as parameters of animation routines. Example: **ASAS**, built on **LISP**, with many geometric transformations.

### 3. Graphical languages

Textual languages cannot visualise action. Graphical languages let the animator **provide a picture of the action**, to express, edit and understand simultaneous changes. Examples: **GENESYS, DIAL, S-Dynamics System**.

| Category | Describes by | Example |
|---|---|---|
| Linear list | Event list with frame numbers | Scefo, SMIL |
| General purpose | Program code | ASAS |
| Graphical | Pictures of actions | GENESYS, DIAL, S-Dynamics |

## Methods of controlling animation

Control is **independent of the language** used to describe the animation.

| Method | Idea | Example |
|---|---|---|
| **Full explicit control** | Simplest. Animator describes **everything** (scaling, translation, rotation or key frames plus interpolation), possibly by mouse, joystick, data glove | **BBOP** (3D key-frame figure animation) |
| **Procedural control** | Objects **communicate** to determine properties; position of one object affects another | Balls cannot pass through walls; actors pass positions to other actors |
| **Constraint-based** | Animator sets **constraints**; system solves for motion obeying all. Compound, non-linear motion of objects in contact | Sutherland's **Sketchpad**; character rigging, robotics |
| **Tracking live action** | Trajectories taken from real motion | **Rotoscoping**; markers on a body; **data glove** |
| **Kinematics and dynamics** | Describe motion by position/velocity (kinematics) or by forces (dynamics) | Cube example below |

### Tracking live action

- **Rotoscoping**: film of people or animals acting the parts; animators **draw over the film**, replacing the actors with animated equivalents.
- **Indicators on key body points**: tracked positions give locations for the matching points of an animated model. A **data glove** measures hand **position and orientation** and the **flexion and hyperextension of each finger**.

### Kinematics vs dynamics

- **Kinematics**: **position and velocity** of points. "The cube is at the origin at t = 0 and moves with constant acceleration in direction (1, 1, 5)."
- **Dynamics**: includes the **physical laws** (Newton): acceleration is proportional to force, the constant being the mass. "At t = 0 the cube is at (0, 100, 0) m, has mass 100 g, and gravity acts on it."
- Knowing kinematics and dynamics at a point lets us determine the **next point** of the motion.

!!! exam "Exam tip"
    "Explain any three methods of controlling animation" is common: pick explicit, procedural and constraint-based, with one example each.

## Checkpoint

??? question "Give one example each of a linear-list, general-purpose and graphical language."
    Scefo (or SMIL); ASAS; GENESYS (or S-Dynamics).

??? question "What is rotoscoping?"
    Drawing over film of live actors so that the animated characters copy their motion.

??? question "Differentiate kinematics and dynamics."
    Kinematics: position and velocity. Dynamics: adds the physical laws and forces (mass, gravity).
