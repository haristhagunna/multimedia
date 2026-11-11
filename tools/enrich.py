"""Student-friendly enrichment for each topic: plain-words explanation, real-life example,
memory hook and key terms. Original wording by the course author.
Copyright (c) 2026 Er. Harish Thagunna. All rights reserved.
E[unit][page] = dict(plain, real, hook, terms=[(term, meaning), ...])
"""
E = {1: {}, 2: {}, 3: {}, 4: {}, 5: {}, 6: {}, 7: {}, 8: {}, 9: {}, 10: {}, 11: {}, 12: {}}
def t(u, p, plain, real, hook, terms): E[u][p] = dict(plain=plain, real=real, hook=hook, terms=terms)

# ---------------- Unit 1 ----------------
t(1, "what-is-multimedia", "Multimedia means using several kinds of information (text, pictures, sound, video, animation) together on a computer, with the user able to control what happens next.",
  "A lesson on YouTube: video and narration (continuous media), captions and diagrams (discrete media), and buttons that let you jump to any part.",
  "A true multimedia system is Computer-controlled, Integrated, Digital and Interactive: remember it as the word CIDI.",
  [("Medium", "A means of distributing and presenting information (text, graphics, speech, music, video)."), ("Multimedia", "Computer-controlled integration of several media, represented digitally and usually interactive."), ("Discrete medium", "Time-independent: text, still images, graphics."), ("Continuous medium", "Time-dependent: audio, video, animation."), ("Hypertext", "Text organised as linked nodes that the reader can follow in any order."), ("Non-linear", "The user, not the author, chooses the path through the content.")])
t(1, "multimedia-system", "A multimedia system is the whole package of hardware, software and network that can capture, store, process, send and present many media together.",
  "Your smartphone: camera and microphone capture, flash memory stores, the processor and apps process, Wi-Fi sends, screen and speaker present.",
  "Five jobs to remember: generate, represent, store, transmit, search and retrieve; compression and processing sit across all of them.",
  [("Multimedia system", "A system that processes multimedia data and applications."), ("Hardware", "Capture, storage, processing and presentation devices."), ("Software", "Operating system, drivers and application programs."), ("Network", "Carries media between systems, usually with real-time needs."), ("Compression", "Reducing the amount of data needed to represent a medium.")])
t(1, "global-structure", "Imagine a building: applications on the top floor, system services in the middle, devices in the basement, and a lift (synchronization) that serves every floor.",
  "A video call: the call app (application domain), operating system and network stack (system domain), camera, microphone and screen (device domain).",
  "Three domains and one bar: Application, System, Device, with Synchronization running through all three.",
  [("Application domain", "Tools and applications that users work with; provides the user interface."), ("System domain", "Database systems, operating system and communication services."), ("Device domain", "Physical devices: capture, storage, input and output hardware."), ("Synchronization", "Keeps media in the right time relation across all domains.")])
t(1, "media-classification", "There are several ways to ask what kind of medium something is: how we perceive it, how it is represented, presented, stored, transmitted and exchanged.",
  "A song: we perceive it by hearing, it is represented as MP3, presented through a speaker, stored on a phone and transmitted by streaming.",
  "Six categories: Perception, Representation, Presentation, Storage, Transmission, Exchange. Memory sentence: Please Read Pages, Study Thoroughly Every day.",
  [("Perception medium", "How humans sense information: seeing and hearing."), ("Representation medium", "How information is coded in the computer, for example ASCII, JPEG, MPEG."), ("Presentation medium", "Devices used for input and output: keyboard, screen, speaker."), ("Storage medium", "Where data is kept: disk, tape, CD."), ("Transmission medium", "What carries data: cable, fibre, radio."), ("Information exchange medium", "Combination of storage and transmission used to exchange information.")])
t(1, "media-concepts-and-properties", "Every medium has a space part (what it looks or sounds like at one instant) and sometimes a time part. A multimedia system should let you combine, process and exchange media freely.",
  "A photo has only space (pixels); a video adds time (25 photos every second).",
  "Discrete = space only. Continuous = space + time. Three properties: combination, independence, computer-supported integration.",
  [("Representation space", "The dimensions in which the medium is laid out (for example 2D for an image)."), ("Representation values", "The kind of values stored: continuous or discrete."), ("Representation dimensions", "Space and time."), ("Combination of media", "Using several media together for one purpose."), ("Media independence", "Media can be handled separately and combined freely."), ("Integration", "Computer-supported combination under one program.")])
t(1, "data-streams", "Continuous media flow as a stream, like water in a pipe. How strictly the timing must be kept gives three transmission modes.",
  "Downloading a file (asynchronous), a delay-bounded call setup (synchronous) and a live phone call with a steady beat (isochronous).",
  "Asynchronous = whenever. Synchronous = not later than a limit. Isochronous = not earlier and not later: a steady rhythm.",
  [("Data stream", "A sequence of data units that are sent and processed in time order."), ("Asynchronous", "No timing constraint on delivery."), ("Synchronous", "A maximum end-to-end delay is guaranteed."), ("Isochronous", "Both a maximum and a minimum delay: data arrives at a constant rate."), ("LDU", "Logical Data Unit: a sample, frame or other unit of a stream.")])

# ---------------- Unit 2 ----------------
t(2, "sound-basics", "Sound is vibration of the air. A microphone turns it into an electrical signal. A bigger wave is louder; a faster wave is higher in pitch.",
  "Pluck a guitar string harder and it gets louder (amplitude); press it on a fret to shorten it and it sounds higher (frequency).",
  "Amplitude decides loudness, frequency decides pitch. Humans hear about 20 Hz to 20 kHz. Frequency f = 1 / T.",
  [("Sound", "Mechanical wave energy that travels through a medium."), ("Audio", "Electrical signal (analog or digital) that represents sound."), ("Amplitude", "Height of the wave: loudness."), ("Frequency", "Cycles per second (Hz): pitch."), ("Period T", "Time of one full cycle; T = 1/f."), ("Infrasound / ultrasound", "Below 20 Hz / above 20 kHz: not heard by humans.")])
t(2, "digital-audio", "To digitise sound the computer measures the wave many times per second (sampling) and rounds each measurement to one of a fixed number of levels (quantization).",
  "An audio CD takes 44,100 measurements every second and stores each one in 16 bits for each of two channels.",
  "Sample at least twice the highest frequency (Nyquist). Size = rate × (bits/8) × channels × seconds.",
  [("Sampling rate", "Number of samples per second, in Hz."), ("Bit depth", "Bits per sample; 16 bits gives 65,536 levels."), ("Quantization", "Rounding a sample to the nearest allowed level."), ("PCM", "Pulse Code Modulation: samples written as binary codes."), ("Nyquist theorem", "fs must be at least 2 × fmax to avoid aliasing."), ("Channel", "Mono = 1 channel, stereo = 2.")])
t(2, "midi", "MIDI is sheet music for machines: it sends which note to play, how hard and on which instrument, not the sound itself.",
  "A MIDI keyboard connected to a laptop: the keys send small messages and the laptop's software instruments make the sound.",
  "MIDI files are tiny and easy to edit, but they need a synthesizer to be heard. Note On = status byte + key number + velocity.",
  [("MIDI", "Musical Instrument Digital Interface: hardware and message standard (early 1980s)."), ("Channel", "One of 16 logical channels, each usually carries one instrument."), ("Note On / Note Off", "Messages that start and stop a note."), ("Velocity", "How hard a key is struck (0 to 127)."), ("Synthesizer", "Device or software that makes sound from MIDI messages."), ("Sequencer", "Records, edits and plays back MIDI data.")])
t(2, "speech-analysis", "Speech analysis asks three questions about a voice: who is speaking, what was said and how was it said?",
  "Voice unlock (who), voice typing on your phone (what), a call-centre tool that senses an angry caller (how).",
  "Who = verification and identification. What = recognition and understanding. How = emotion and state of the speaker.",
  [("Speaker verification", "Checking a claimed identity from the voice."), ("Speaker identification", "Finding out who is speaking from a group."), ("Speech recognition", "Converting speech to words."), ("Speech understanding", "Working out the meaning of what was said."), ("Feature extraction", "Keeping only the characteristics needed, to reduce data.")])
t(2, "speech-generation", "Computers create speech by joining small recorded pieces (phones, diphones, syllables) or by computing the sounds with a model of the vocal tract.",
  "A navigation app speaking street names, or a screen reader reading a web page aloud.",
  "Two steps of synthesis: text is transcribed into a sound script, then the sounds are synthesised into speech.",
  [("Phone", "Smallest unit of sound in speech."), ("Morph", "Smallest unit of meaning."), ("Diphone", "Two neighbouring phones, which captures the transition between them."), ("Syllable", "A unit built from phones, used to make joins easier."), ("Formant", "A frequency band where the vocal tract strengthens sound; shapes vowels."), ("Concatenation", "Joining stored speech units.")])
t(2, "speech-transmission", "Sending speech costs bits. PCM keeps everything, source encoding uses properties of speech to save bits, and recognition plus synthesis sends only text.",
  "A normal phone call uses 64 kbit/s (8,000 samples × 8 bits); a good voice codec can use much less.",
  "PCM = accurate but big. Source encoding = smaller. Recognise-then-synthesise = smallest, but the original voice is lost.",
  [("PCM", "Digital representation by sampling and quantization."), ("Source encoding", "Compression that depends on the type of signal."), ("ADPCM", "Adaptive Differential PCM: sends small adaptive differences."), ("Bit rate", "Bits per second needed by a stream."), ("Compression", "Reducing data to save storage or bandwidth.")])

# ---------------- Unit 3 ----------------
t(3, "image-basics", "A digital image is a grid of tiny squares called pixels; each pixel holds a number for its brightness or colour. More pixels give more detail but more data.",
  "Zoom far into a phone photo and you see the individual coloured squares.",
  "Bitmap size = width × height × bits per pixel ÷ 8. Bitmaps store pixels; vector graphics store shapes.",
  [("Pixel", "Picture element: the smallest unit of an image."), ("Resolution", "Number of pixels, for example 640 × 480."), ("Bit depth", "Bits per pixel: 1 = black/white, 8 = 256 values, 24 = true colour."), ("Bitmap", "Image stored pixel by pixel."), ("Vector graphic", "Picture stored as shapes and formulas."), ("RGB / CMY", "Additive screen colours / subtractive print colours.")])
t(3, "formats", "A file format is the rule book for storing an image: some keep every pixel exactly (lossless), some throw away detail to be smaller (lossy).",
  "Photos on social media are usually JPEG; logos and screenshots are usually PNG; small web animations are GIF.",
  "Photos use JPEG. Sharp-edged graphics use PNG or GIF. TIFF is for high-quality storage.",
  [("BMP", "Simple, usually uncompressed bitmap."), ("GIF", "Up to 256 colours, lossless, supports animation."), ("JPEG", "Lossy compression suited to photographs."), ("PNG", "Lossless compression with true colour and transparency."), ("TIFF", "Flexible, high-quality format used in publishing and scanning."), ("Lossless vs lossy", "Exact copy after decoding / some information lost.")])
t(3, "image-analysis", "Image analysis lets a computer understand a picture: find edges and regions, then decide what objects they form.",
  "A phone that detects faces in the camera view, or a system that reads car number plates.",
  "Recognition pipeline: capture, pre-process, find features, label, interpret.",
  [("Image analysis", "Extracting information from images."), ("Image recognition", "Deciding what the image or an object in it is."), ("Pre-processing", "Cleaning the image: noise removal, contrast."), ("Segmentation", "Splitting the image into regions or objects."), ("Edge", "A line where brightness changes sharply."), ("Labeling", "Assigning names or classes to found structures.")])
t(3, "image-transmission", "To send an image you send its bits. The time depends on the size in bits and the speed of the link, so compression makes pictures arrive faster.",
  "A web page that shows a blurry picture first and sharpens it as more data arrives.",
  "Transmission time = size in bits ÷ link rate. A 640 × 480 8-bit image is 307,200 bytes: about 38.4 s at 64 kbit/s.",
  [("Bit rate", "Bits transmitted per second."), ("Bandwidth", "Capacity of a link."), ("Transmission time", "Size in bits divided by bit rate."), ("Compression", "Makes the image smaller, so it is sent faster."), ("Progressive display", "Showing a rough image early and refining it.")])
t(3, "synthesis-and-graphics-systems", "Image synthesis builds pictures from descriptions (shapes, colours, light) instead of capturing them with a camera. A graphics system is the hardware and software that draws and displays them.",
  "A 3D game or a CAD program drawing a building plan.",
  "Flow: host sends display commands, display controller draws into the refresh buffer, video controller reads the buffer and drives the monitor.",
  [("Display controller", "Turns display commands into a scanned image."), ("Refresh buffer", "Memory holding the image to show."), ("Video controller", "Reads the buffer repeatedly and drives the monitor."), ("Raster display", "Image drawn line by line as pixels."), ("Rendering", "Computing an image from a scene description.")])

# ---------------- Unit 4 ----------------
t(4, "video-representation", "Video is a fast sequence of still pictures. The eye blends them (persistence of vision), so we see smooth motion. TV sends brightness and colour separately.",
  "A flip-book: flick the pages quickly and the drawing moves.",
  "25 frames per second means 40 ms per frame. PAL: 625 lines, 25 fps. NTSC: 525 lines, about 30 fps.",
  [("Frame", "One complete still image of a video."), ("Frame rate", "Frames shown per second."), ("Interlacing", "Sending odd lines then even lines (two fields) to reduce flicker."), ("Luminance (Y)", "Brightness part of the signal."), ("Chrominance", "Colour information."), ("Aspect ratio", "Width to height, for example 4:3 or 16:9.")])
t(4, "computer-video-format", "A computer must digitise video. Resolution, colour depth and frame rate each multiply the amount of data.",
  "Capturing from a webcam: 640 × 480 pixels, 3 bytes per pixel, 25 frames each second is already about 23 MB every second before compression.",
  "Data rate = width × height × bytes per pixel × frames per second. CIF is 352 × 288.",
  [("Digitizer", "Converts analog video into digital frames."), ("Resolution", "Pixels per frame."), ("Frame rate", "Frames per second."), ("Chroma subsampling", "Storing colour at lower resolution than brightness."), ("CIF", "Common Intermediate Format: 352 × 288 pixels.")])
t(4, "video-transmission", "TV signals come in several forms: separate R, G, B; brightness plus colour differences (YUV or YIQ); or all mixed together in one composite signal.",
  "Old TVs received a single composite cable; studios use component signals for the best quality.",
  "Y = 0.30R + 0.59G + 0.11B. The eye is more sensitive to brightness than to colour, so colour can use less bandwidth.",
  [("RGB", "Three separate colour signals."), ("YUV", "Luminance plus two colour-difference signals (PAL)."), ("YIQ", "Luminance plus in-phase and quadrature signals (NTSC)."), ("Composite", "All components combined in one signal."), ("Digitization", "Sampling and quantizing the video signal.")])
t(4, "animation-basics", "Animation shows a series of images or model positions fast enough to create the illusion of movement. The animator sets key poses and the computer fills in the rest.",
  "A bouncing ball: draw it at the top, the floor and the top again; the computer creates the frames between.",
  "Key frames define the motion, in-betweens (tweening) fill the gaps. Film uses about 24 frames per second.",
  [("Key frame", "A frame that defines an important pose or position."), ("In-between", "A frame generated between two key frames."), ("Tweening", "Automatic creation of in-betweens by interpolation."), ("Cel animation", "Traditional method of drawing on transparent sheets."), ("Persistence of vision", "The eye keeps an image for a moment, blending frames.")])
t(4, "animation-languages-and-control", "Instead of drawing every frame, an animator can describe motion in a script or program; the computer produces the frames.",
  "A script that says 'move this logo from left to right over 2 seconds and make it spin'.",
  "Describe the motion, not the pictures: this saves effort and data.",
  [("Animation language", "A notation for describing objects and their motion."), ("Script", "A sequence of commands that creates the animation."), ("Procedural control", "Motion produced by a program or rule."), ("Constraint", "A rule that limits how objects move or connect."), ("Interpolation", "Computing in-between values from start and end.")])
t(4, "animation-display-and-transmission", "Animation can be shown with double buffering so the viewer never sees half-drawn frames, and it can be sent as commands that the receiver draws, which is far lighter than sending every frame.",
  "A web animation that sends a few shapes and movement rules instead of 25 pictures per second.",
  "Double buffering: draw the next frame off-screen, then swap. Symbolic transmission is smaller than pixel transmission.",
  [("Double buffering", "Drawing into a hidden buffer and swapping it with the visible one."), ("Frame buffer", "Memory holding the displayed image."), ("Symbolic transmission", "Sending objects and commands."), ("Pixel transmission", "Sending the finished frames."), ("Rendering", "Producing the image at the receiver.")])

# ---------------- Unit 5 ----------------
t(5, "basics", "Compression stores the same information in fewer bits by removing redundancy (lossless) or less important detail (lossy).",
  "A ZIP file keeps every byte (lossless); an MP3 or JPEG throws away what you are unlikely to notice (lossy).",
  "Compression ratio = original size ÷ compressed size. Dialogue applications need a delay below about 150 ms.",
  [("Redundancy", "Repeated or predictable information that can be removed."), ("Lossless", "Original is recovered exactly."), ("Lossy", "Some information is permanently lost."), ("Compression ratio", "Original size : compressed size."), ("Codec", "Coder and decoder pair."), ("Symmetric coding", "Encoding and decoding take similar effort.")])
t(5, "categories", "Coding techniques fall into three groups: entropy coding (lossless), source coding (usually lossy) and hybrid coding that combines both.",
  "JPEG is hybrid: lossy DCT and quantization, then lossless Huffman coding.",
  "Entropy = ignores meaning. Source = uses meaning. Hybrid = both.",
  [("Entropy coding", "Lossless; treats data as a bit sequence: RLE, Huffman, arithmetic."), ("Source coding", "Uses properties of the medium: prediction, transform, subband."), ("Hybrid coding", "Combines techniques: JPEG, MPEG, H.261, DVI."), ("Run-length coding", "Replaces runs with value and count."), ("DCT", "Discrete Cosine Transform used in JPEG and MPEG.")])
t(5, "rle-and-huffman", "Run-length coding counts repeats. Huffman coding gives short codes to common symbols and long codes to rare ones, so the average is shorter.",
  "Morse code: the common letter E is one dot, the rare Q is long.",
  "Huffman: repeatedly merge the two smallest frequencies; left edge 0, right edge 1; no code is a prefix of another.",
  [("Run", "Consecutive repeats of the same value."), ("Prefix code", "No code word is the start of another, so decoding is unambiguous."), ("Variable-length code", "Code words of different lengths."), ("Priority queue", "List kept sorted by frequency to find the two smallest."), ("Frequency", "How often a symbol occurs.")])
t(5, "prediction-and-adaptive", "Neighbouring samples are similar, so predict the next one and send only the small error (DPCM). Adaptive methods change their settings as the data changes.",
  "Forecasting tomorrow's temperature as today's value and reporting only the difference.",
  "Send the difference, not the value: small numbers need fewer bits.",
  [("Predictor", "Estimates the next value from earlier ones."), ("Residual", "Difference between actual and predicted value."), ("DPCM", "Differential PCM: codes the residual."), ("Delta modulation", "Sends only whether the signal went up or down."), ("Adaptive coding", "Parameters change with the signal.")])
t(5, "jpeg", "JPEG cuts the picture into 8 × 8 blocks, converts each block to frequencies (DCT), discards fine detail (quantization) and then compresses the numbers.",
  "A photo saved at 'low quality' looks blocky because quantization removed more high-frequency detail.",
  "Pipeline: colour transform, 8 × 8 blocks, DCT, quantization, zig-zag, run-length / differential, Huffman.",
  [("DCT", "Transform from pixel values to frequency coefficients."), ("Quantization", "Dividing and rounding coefficients: the lossy step."), ("DC coefficient", "Top-left coefficient: average of the block."), ("AC coefficients", "Remaining 63 coefficients."), ("Zig-zag scan", "Reading coefficients from low to high frequency."), ("Baseline JPEG", "The standard sequential lossy mode.")])
t(5, "mpeg-h261-dvi", "Video compression removes redundancy inside a frame (like JPEG) and between frames (motion compensation), because most of the picture stays the same.",
  "A news presenter: the background does not change, so only the moving face needs fresh data.",
  "I frames stand alone, P frames are predicted from the past, B frames from the past and the future.",
  [("I frame", "Intra-coded: independent, like a JPEG."), ("P frame", "Predicted from an earlier I or P frame."), ("B frame", "Bidirectionally predicted from earlier and later frames."), ("Motion compensation", "Describing movement of blocks between frames."), ("H.261", "ITU standard for video conferencing at p × 64 kbit/s."), ("MPEG", "ISO standards for compressed video and audio.")])

# ---------------- Unit 6 ----------------
t(6, "basic-technology", "A compact disc stores bits as microscopic pits along one long spiral track. A laser shines on the track and a sensor reads changes in the reflected light.",
  "A tiny, very precise version of a vinyl record read with light instead of a needle.",
  "Three layers: polycarbonate substrate, reflective layer, protective layer. A change between pit and land represents a 1.",
  [("Pit / land", "Recessed / flat areas of the track."), ("Spiral track", "One track winding from inside to outside."), ("Laser", "Light source used to read (and write) the disc."), ("Substrate", "Clear polycarbonate plastic carrying the pits."), ("CLV", "Constant Linear Velocity: the disc speed varies so data passes at a constant rate."), ("Optical storage", "Storage read with light.")])
t(6, "video-disks", "Video discs went from analog LaserDisc to digital DVD and then Blu-ray, using shorter laser wavelengths and tighter tracks to store more.",
  "A DVD movie holds about 4.7 GB; a Blu-ray movie disc holds 25 GB per layer.",
  "Shorter wavelength + smaller pits + tighter tracks = more capacity: CD 780 nm, DVD 650/635 nm, Blu-ray 405 nm.",
  [("LaserDisc", "Analog video disc using laser reading."), ("DVD", "Digital Versatile Disc: 4.7 GB single layer."), ("Blu-ray", "Uses a blue-violet 405 nm laser; 25 GB per layer."), ("Track pitch", "Distance between tracks: 1.6 µm CD, 0.74 µm DVD."), ("Dual layer", "Two data layers read at different focus.")])
t(6, "cd-audio", "CD-DA stores stereo sound as 44.1 kHz, 16-bit PCM. Heavy error correction (CIRC) and EFM coding make it robust against scratches.",
  "A scratched CD can still play because the player rebuilds lost data from redundant bits.",
  "Red Book. 44,100 × 16 × 2 = 1,411,200 bit/s. 74 min = 333,000 blocks of 2,352 bytes.",
  [("Red Book", "Specification of the audio CD."), ("EFM", "Eight-to-Fourteen Modulation: line code for the disc."), ("CIRC", "Cross-Interleaved Reed-Solomon Code for error correction."), ("Subcode", "Extra channel with track and time information."), ("Block / sector", "2,352 bytes; 75 per second.")])
t(6, "cd-rom", "CD-ROM adds an extra layer of error correction so computers can read data without a single wrong bit. Mode 1 is for data, Mode 2 for audio and video.",
  "Installing software from a disc needs perfect data; one wrong bit could break a program.",
  "Yellow Book. Mode 1 = 2,048 user bytes + EDC/ECC. Mode 2 = 2,336 user bytes.",
  [("Yellow Book", "CD-ROM specification."), ("Mode 1", "Computer data with error detection and correction."), ("Mode 2", "More user bytes, less error protection."), ("EDC / ECC", "Error detection / error correction code."), ("CD-ROM/XA", "Extended Architecture: mixes audio, video and data.")])
t(6, "cd-i-and-photo-cd", "CD-I is a disc and player system for interactive multimedia. Photo CD stores each photo in several resolutions.",
  "Photo CD lets you view a quick small preview or load the full high-resolution scan.",
  "Photo CD resolutions: Base/16, Base/4, Base, 4 Base, 16 Base. CD-I = Green Book.",
  [("CD-I", "Compact Disc Interactive."), ("Green Book", "CD-I specification."), ("CD-I Ready", "Disc playable on CD-I and on normal CD players."), ("Bridge disc", "Playable on both CD-ROM/XA and CD-I systems."), ("Photo CD", "Kodak disc holding images at several resolutions.")])
t(6, "cd-wo-and-cd-mo", "CD-WO lets you record once; CD-MO can be erased and written again using heat and a magnetic field.",
  "Burning a backup disc once (WO) versus a reusable magneto-optical cartridge (MO).",
  "Orange Book covers both: WO = write once, MO = magneto-optical rewritable.",
  [("CD-WO", "Write-Once CD, Orange Book part II."), ("CD-MO", "Magneto-optical rewritable disc."), ("Orange Book", "Specification for recordable CDs."), ("Magneto-optical", "Laser heats a spot so a magnetic field can change its polarity."), ("Multisession", "Adding data in several recording sessions.")])

# ---------------- Unit 7 ----------------
t(7, "introduction-real-time", "A real-time system must produce the right result at the right time. A correct answer that arrives late is a wrong answer.",
  "Video playback: if frame 100 is not ready at 4.00 s, the picture stutters, even though the frame is correct.",
  "Hard real time: a missed deadline is a failure. Soft real time: a miss reduces quality.",
  [("Deadline", "Latest time by which a task must finish."), ("Hard real time", "Missing a deadline is unacceptable."), ("Soft real time", "Occasional misses degrade quality only."), ("Periodic task", "Task that repeats with a fixed period."), ("Jitter", "Variation in timing.")])
t(7, "resource-management", "Multimedia needs CPU time, memory and bandwidth reserved in advance. Admission control decides whether a new stream can be accepted without hurting existing ones.",
  "A cinema does not sell more tickets than seats: it refuses extra customers to keep quality for those inside.",
  "Reserve first, then guarantee. LBAP model: B + R·t, the data that may arrive by time t.",
  [("Resource", "Anything a stream needs: CPU, memory, bandwidth, disk."), ("Admission control", "Accepting or rejecting a new request."), ("Reservation", "Setting resources aside in advance."), ("LBAP", "Linear Bounded Arrival Process model."), ("Utilisation", "Fraction of a resource in use.")])
t(7, "scheduling", "Scheduling decides which task runs next. EDF always runs the task with the nearest deadline; Rate Monotonic gives higher fixed priority to tasks with shorter periods.",
  "Doing homework: EDF is 'do the one due soonest first'; RM is 'always do the daily task before the weekly task'.",
  "Utilisation U = Σ C/P. EDF works if U ≤ 1. RM is guaranteed if U ≤ n(2^(1/n) − 1).",
  [("Period P", "Time between releases of a periodic task."), ("Computation time C", "CPU time needed per period."), ("Utilisation U", "Sum of C/P over all tasks."), ("EDF", "Earliest Deadline First: dynamic priority, optimal."), ("RM", "Rate Monotonic: static priority by period."), ("Preemption", "Interrupting a running task for a more urgent one.")])
t(7, "system-architecture", "A multimedia operating system adds real-time scheduling, a file system built for continuous data and fast buffer handling on top of an ordinary OS.",
  "Streaming a film from a server: the server must read the disk in time for every viewer's next block.",
  "Goal: guarantee timing. Layers: device, driver, kernel scheduler, file system, application interface.",
  [("Continuous-media file system", "Stores and retrieves streams at guaranteed rates."), ("Disk scheduling", "Orders disk requests to meet deadlines."), ("Buffer", "Memory used to smooth out timing differences."), ("Device driver", "Software controlling a device."), ("Kernel", "Core of the operating system.")])

# ---------------- Unit 8 ----------------
t(8, "introduction", "Networks built for data transfer do not suit multimedia. Streams need high bandwidth, low delay and steady timing, and often many receivers at once.",
  "A file download can wait; a live video call cannot.",
  "Needs: throughput, low delay, low jitter, tolerable loss, multicast.",
  [("Bandwidth", "Data capacity of a link."), ("Delay (latency)", "Time for data to travel from sender to receiver."), ("Jitter", "Variation of delay."), ("Loss", "Fraction of data that does not arrive."), ("Multicast", "One sender, many receivers.")])
t(8, "qos", "Quality of Service (QoS) is a set of promises about performance: how much data, how fast and how steadily. Applications ask for it and the system agrees or refuses.",
  "Booking a courier with 'delivery within 24 hours': you negotiate service and the company reserves capacity.",
  "QoS parameters: throughput, delay, jitter, loss. Shaping uses a leaky or token bucket.",
  [("QoS", "Quality of Service guarantees."), ("Guaranteed / best effort", "Firm promise / no promise."), ("Negotiation", "Agreeing a QoS between user and system."), ("Token bucket", "Allows bursts up to b and rate r."), ("Traffic shaping", "Smoothing the flow to match the agreed profile.")])
t(8, "transport-subsystem", "RTP carries media with sequence numbers and timestamps; RTCP reports quality. They run over UDP because late data is useless, so waiting for retransmission is pointless.",
  "Live streaming: a lost frame is skipped, not resent.",
  "UDP + RTP for media, RTCP for feedback, TCP is a poor fit for real time.",
  [("RTP", "Real-time Transport Protocol."), ("RTCP", "RTP Control Protocol: quality reports."), ("UDP", "Fast, connectionless transport without retransmission."), ("Sequence number", "Detects loss and reordering."), ("Timestamp", "Tells the receiver when to play a packet.")])
t(8, "application-subsystem", "The application subsystem supports people working together: collaborative computing, sessions, shared architectures and multimedia mail.",
  "Joining a video meeting, sharing your screen and sending a voice message later.",
  "Collaborative computing + session management + architecture + mail and messaging.",
  [("Collaborative computing", "Several users working together using computers."), ("Session management", "Creating, controlling and ending a session."), ("Centralised / replicated architecture", "One shared application / copies at each site."), ("Multimedia mail", "Messages containing several media."), ("Playout buffer", "Holds data briefly to smooth delay variation.")])

# ---------------- Unit 9 ----------------
t(9, "documents", "A multimedia document is more than data: it has content, a logical structure (chapters, sections) and a layout (how it is shown).",
  "A web page: the text is the content, headings define the structure and CSS defines the layout.",
  "Content, structure, layout: keep them separate for flexibility.",
  [("Document", "Structured collection of information, shown to a reader."), ("Logical structure", "Organisation into chapters, sections, paragraphs."), ("Layout structure", "How content is placed on the page or screen."), ("Content", "The actual text, images, audio."), ("Document architecture", "Model describing how a document is built.")])
t(9, "hypertext", "Hypertext connects pieces of information with links, and the reader chooses the path. Hypermedia does the same with all media.",
  "Wikipedia: every blue word leads to another article.",
  "Hypertext = nodes + links + anchors. The Dexter model describes the layers.",
  [("Node", "A unit of information."), ("Link", "A connection between nodes or anchors."), ("Anchor", "The active spot inside a node where a link starts or ends."), ("Hypermedia", "Hypertext with audio, video and images."), ("Dexter model", "Reference model for hypertext systems.")])
t(9, "hypermedia-systems", "Hypermedia systems grew from an early idea in 1945 to the World Wide Web, which made linked multimedia available to everyone.",
  "From Vannevar Bush's imagined Memex to the browser you use today.",
  "Remember the line: Memex (1945), hypertext term (1965), Web (1989 to 1991).",
  [("Memex", "Vannevar Bush's 1945 idea of a linked personal information machine."), ("Hypertext", "Term coined by Ted Nelson in 1965."), ("World Wide Web", "Proposed by Tim Berners-Lee in 1989; first web site in 1991."), ("Browser", "Program that displays and follows links."), ("Authoring system", "Tool used to create hypermedia.")])
t(9, "sgml-oda-mheg", "Three standards describe documents and objects: SGML separates content from formatting, ODA exchanges office documents and MHEG describes multimedia objects for interchange.",
  "HTML grew from SGML ideas: tags describe the meaning of parts, a style sheet decides the look.",
  "SGML = markup with a DTD. ODA = logical + layout structure. MHEG = multimedia objects for exchange.",
  [("SGML", "Standard Generalized Markup Language, ISO 8879."), ("DTD", "Document Type Definition: the allowed elements and structure."), ("ODA", "Open Document Architecture, ISO 8613."), ("MHEG", "Multimedia and Hypermedia Experts Group, ISO/IEC 13522."), ("Markup", "Tags added to text to describe structure.")])

# ---------------- Unit 10 ----------------
t(10, "notion", "Synchronization means the right media shown at the right time. It happens inside one stream (intra) and between streams (inter).",
  "Lip-sync: the speaker's lips must match the sound.",
  "Intra = smooth within a stream. Inter = aligned between streams. Live = real time source, synthetic = pre-planned.",
  [("Intra-object sync", "Correct timing inside one medium."), ("Inter-object sync", "Correct timing between different media."), ("Live synchronization", "Sync of live, captured media."), ("Synthetic synchronization", "Planned timing of stored media."), ("Hard / soft sync", "Strict / tolerant timing relation."), ("Skew", "Time difference between streams.")])
t(10, "reference-model", "A reference model organises synchronization into layers so that each layer solves one problem: from raw media up to the author's specification.",
  "Like postal service layers: the truck (media), the sorting centre (stream), the parcel (object), the order form (specification).",
  "Four layers: media, stream, object, specification.",
  [("Media layer", "Single continuous stream of LDUs."), ("Stream layer", "Groups of streams and their sync."), ("Object layer", "Complete multimedia objects, including discrete media."), ("Specification layer", "Author's description of the presentation."), ("Reference model", "Structured view that guides system design.")])
t(10, "presentation-requirements", "Humans accept small timing errors, but not large ones. Meeting these limits is a presentation requirement.",
  "If a speaker's voice is 200 ms behind the lips, viewers notice and get annoyed.",
  "Lip sync tolerance: audio may be 80 ms behind to 80 ms ahead of the video.",
  [("Lip synchronization", "Matching speech to lip movement."), ("Skew", "Difference in presentation time."), ("Tolerance", "The error people still accept."), ("Jitter", "Short-term delay variation."), ("Presentation requirement", "Timing limit that quality depends on.")])
t(10, "specification", "A specification tells the system how media are related in time. Different methods describe this in different ways.",
  "A slide show script: 'show slide 2 when narration clip 1 ends'.",
  "Four common categories: interval-based, axes (timeline) based, control-flow based, event-based.",
  [("Specification", "Formal description of timing relations."), ("Interval-based", "Uses time intervals and their relations."), ("Axes-based", "Places events on a common timeline."), ("Control-flow based", "Uses points in a flow of control."), ("Event-based", "Actions triggered by events.")])
t(10, "distributed", "In a network the sender and receiver have different clocks and the delay varies, so synchronization needs buffering and clock agreement.",
  "Two friends watch a stream together; each device downloads at a different speed.",
  "Delay variation is removed by buffers; clock drift by clock sync.",
  [("Clock drift", "Gradual difference between two clocks."), ("Buffering", "Delaying data to remove jitter."), ("Global time", "Common time reference."), ("Master / slave", "One stream leads, the other follows."), ("Distributed system", "Computers connected by a network.")])

# ---------------- Unit 11 ----------------
t(11, "abstraction-levels", "Programming for multimedia can happen at different levels of detail: from raw device access up to object-oriented applications.",
  "Driving a car versus building an engine: higher levels hide the details.",
  "Low to high: device, library, system software, toolkit, higher language, object-oriented.",
  [("Abstraction level", "Degree of detail used to represent and manipulate data."), ("Library", "Functions supplied with a device."), ("Toolkit", "Uniform interface that hides process structure."), ("Programming language", "Language with abstractions for media."), ("Object-oriented approach", "Class hierarchy for multimedia.")])
t(11, "object-oriented", "In the object-oriented view media, devices and processing units become classes with methods such as play and stop, so programs are easier to build and reuse.",
  "A Video class with play(), pause() and seek(); a DVD player object is a Video object with a device.",
  "Simple objects (BMO), simple multimedia objects (SMO) and compound multimedia objects (CMO).",
  [("Class", "Blueprint of an object."), ("Object", "An instance of a class."), ("Inheritance", "A class gets features from a parent class."), ("BMO", "Basic Media Object."), ("SMO / CMO", "Simple / Compound Multimedia Object.")])
t(11, "system-software", "System software gives a standard way to use multimedia: streams, time-aware data and scheduling, so applications do not handle each device.",
  "A media framework that plays any file without the app knowing the codec.",
  "Two models: data as time capsules, data as streams.",
  [("Stream", "Flow of data units from a source to a sink."), ("Time capsule", "Data stored with its timing information."), ("Nemo system", "Example of multimedia system software."), ("Scheduler", "Allocates CPU time."), ("Driver", "Controls hardware.")])
t(11, "toolkits-and-languages", "Toolkits hide complexity and give programmers ready-made media components. Some languages treat audio and video as normal data types.",
  "A toolkit lets you add a video player to your app with a few lines.",
  "Toolkit = ready-made parts. Language = media as data types (for example OCCAM-2 with parallel processes).",
  [("Toolkit", "Library of reusable multimedia components."), ("API", "Application Programming Interface."), ("Client-server toolkit", "Toolkit where a server controls devices for clients."), ("OCCAM-2", "Parallel language based on Communicating Sequential Processes."), ("Process", "A running program unit.")])

# ---------------- Unit 12 ----------------
t(12, "application-areas", "Multimedia is used in video on demand, video conferencing, education and training, information systems and entertainment.",
  "Online classes, movie streaming and digital museum guides.",
  "VoD needs a server, a network and a set-top box. Conferencing needs low delay.",
  [("Video on demand", "Watch a chosen video when you want."), ("Video conferencing", "Live audio-video link between sites."), ("Set-top box", "Connects the TV to the digital network."), ("Computer-based training", "Learning delivered by computer."), ("Information system", "System for storing and retrieving information.")])
t(12, "application-classes", "Applications can be grouped by what they do: games, repositories, interactive TV and VoD, conferencing and mail, shared workspaces and business workflow.",
  "A game console, a digital library, a video call and a company document system are four different classes.",
  "Six classes: games, repositories, iTV/VoD, conferencing/mail, shared workspaces, business workflow.",
  [("Game systems", "Leaders in multimedia technology."), ("Repository", "Large indexed database, mostly play-back."), ("Interactive TV", "TV with interactive services."), ("Shared workspace", "Remote users see the same application."), ("Workflow", "Business process using multimedia data.")])
t(12, "development-cycle", "Making a multimedia product follows five steps: plan and cost, design, develop and produce, test and debug, deliver.",
  "Making an educational app: plan the budget, storyboard screens, build, test with students, publish.",
  "Plan → Design → Produce → Test → Deliver, and always check copyright.",
  [("Storyboard", "Sequence of sketches showing the screens and flow."), ("Prototype", "Early working version."), ("Rights and permissions", "Legal permission to use others' content."), ("Testing", "Finding and fixing problems."), ("Delivery", "Publishing the product to users.")])
t(12, "system-types-and-components", "Multimedia systems come in several types and are built from input, output and storage components.",
  "A multimedia PC: webcam and microphone (input), screen and speakers (output), SSD and DVD (storage).",
  "Three component groups: input, output, storage.",
  [("Input systems", "Devices that capture media: camera, microphone, scanner."), ("Output systems", "Devices that present media: monitor, speakers, printer."), ("Storage systems", "Devices that keep media: disk, optical disc."), ("Stand-alone system", "System used by one person on one machine."), ("Networked system", "System connected for sharing.")])
