# Toolkits and Higher Programming Languages

!!! source "Source"
    *Unit 11 – Abstractions for Programming* pp. 4–6.

## Toolkits

**Toolkits** control audio and video processing **in a programming environment**. They **represent interfaces at the system-software level**, can be embedded into programming languages or object-oriented environments, and are used to:

- **abstract from the physical layer**;
- give a **uniform interface** for all different continuous-media devices;
- introduce the **client-server paradigm**;
- **hide process structures**.

It would be valuable to have the **same toolkit on all platforms**, but experience shows this **remains a wish** and would **reduce performance**.

## Higher programming languages

In a **higher (high-level) language (HLL)**, processing of continuous media is done by **groups of similarly built functions**. The calls are mostly **hardware and driver independent**. Programs either **access multimedia data structures directly** or **communicate with the active processes of the real-time environment**; devices are controlled through drivers.

Media can be seen in three ways inside a language.

### 1. Media as types

Audio and video are **data types**, just as **character** is the type for text (the smallest addressable element). A program can copy, compare, delete, read, store and display them, and use them in other data structures. Example from the notes (OCCAM-2, derived from **Communicating Sequential Processes** for **transputers**): two audio LDUs from two microphones are read in parallel and **mixed**:

```
a, b REAL;
ldu.left1, ldu.left2, ldu.left_mixed AUDIO_LDU;
WHILE
  COBEGIN
    PROCESS_1  Input(micro1, ldu.left1)
    PROCESS_2  Input(micro2, ldu.left2)
  ldu.left_mixed := a * ldu.left1 + b * ldu.left2;
END WHILE
```

!!! warning "Listing slips"
    The handout's listing is garbled (for example "ldu.left-mixed", a stray `\_`, and "COBEGIN" inside a `WHILE`). The idea is clear: two parallel input processes and a weighted sum **a·ldu1 + b·ldu2**.

### 2. Media as files

A continuous stream is treated as a **file**: `open` associates a device with a file name and returns a **file descriptor**; `read`, `mix`, `activate`, `deactivate` and `close` follow.

```
file_h1 = open(MICROPHONE_1, ...)
file_h2 = open(MICROPHONE_2, ...)
file_h3 = open(SPEAKER, ...)
read(file_h1); read(file_h2)
mix(file_h3, file_h1, file_h2)
activate(file_h1, file_h2, file_h3)
...
deactivate(...);  rc1 = close(file_h1) ...
```

Difference from discrete files: **continuous read/write** keep assigning **new values continuously** to a variable bound to one `read`, whereas for discrete data **each read call fetches the next value**.

### 3. Media as processes

Processing continuous data is **time dependent**: the **life span of a process equals the life span of a connection** between source and destination (local or remote). The process is created, **reserves the devices** at creation, and its actions are controlled by **IPC messages**:

```
PROCESS cont_process_a;
  on_message_do
    set_volume ...
    set_loudness ...
pid = create(cont_process_a)
send(pid, set_volume, 3)
send(pid, set_loudness)
```

## Language requirements

- The HLL must support **parallel processing**; the **number of processes** is known at compile time, and processes can also be **defined dynamically** at run time.
- The **IPC mechanism** must transmit audio and video **in time** (they have a limited life span). It must:
    - understand **a priori or implicitly specified time requirements**;
    - **transmit** the data according to those requirements;
    - **start processing** the received data **on time**.
- **Language:** the authors see **no demand for a new dedicated language**. Replacing a language is difficult because cooperation between the real-time environment and other programs needs semantic changes. A **language extension** is proposed, a **simple language** meeting the requirements; examples: **OCCAM-2, Ada, parallel C variants for transputers**.

| View | Media is a | Typical operations |
|---|---|---|
| **Types** | Data type (like `char`) | Assign, copy, mix with operators |
| **Files** | File | open, read, write, activate, close |
| **Processes** | Process (life span = connection) | create, send messages |

## Checkpoint

??? question "Name the three views of media in a programming language."
    As types, as files, as processes.

??? question "What must the IPC mechanism of a real-time language do?"
    Understand time requirements, transmit continuous data according to them, and start processing on time.
