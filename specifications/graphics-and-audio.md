# Graphics and Audio — the A/V dimension of every path

**Updated:** 2026-06-10
**Purpose:** Graphics and audio are taught as a **first-class dimension of every curriculum path**,
not a separate art/music course. This spec is the per-platform reference and the fold-into-the-paths
model.

> **The fold (2026-06-10).** A/V is **co-equal with code** ([real-retro-games.md](../decisions/real-retro-games.md):
> code / visuals / audio / level design / polish are co-equal). So every game on every track carries
> a **graphics focus and an audio focus alongside its code rung**, and A/V skills **spiral** the same
> way code does — introduced once, revisited deeper, then owned. This replaces the old fixed
> "Games 1-4 / 5-8 / 9-16" framing (retired with the 2026 lineup replan); A/V now maps onto each
> track's ladder, not to fixed game numbers. Most bedroom coders weren't trained artists or
> musicians — they learned enough, worked within constraints, and collaborated. The curriculum
> teaches that same competence.

---

## How A/V folds into a path

Each game's brief and units carry three threads at once:

- **Code rung** — the new hardware/technique the game headlines (from the track's lineup record).
- **Graphics focus** — what the learner draws and *why it reads* on this hardware.
- **Audio focus** — what the learner makes the sound chip do, and when sound should fire.

A/V spirals across the ladder: early games teach **readability and feedback** (silhouette, contrast,
a hit sound), middle games teach **craft** (tile variety, animation, ADSR, jingles), late games teach
**exploitation** (dithering, palette tricks, filter sweeps, dynamic music). Each track also has at
least one **audio-foregrounded game** where the sound chip *is* the headline — e.g. C64 **SID Symphony**
(interrupt-driven SID) and **Soundsmith** (BASIC, full SID), Spectrum **Starfall** (128K AY), NES
**Thunder Run** (APU engine), Amiga **Onslaught** (MOD replay) and AMOS **Knight Watch** (SAM + AMOS
Music). When a game is briefed, its A/V focuses are recorded in its brief alongside the code rung.

---

## Per-platform graphics constraints (reference)

- **C64 (VIC-II)** — sprites 24×21, 3 colours + transparent (or 12×21 multicolour); characters 8×8,
  4 colours in multicolour; 40×25 screen, 16 colours. *The skill:* flexible character graphics around
  limited sprite colour.
- **ZX Spectrum (ULA)** — **no hardware sprites** (all software); **attribute clash** — 8×8 cells,
  2 colours each (ink + paper); 256×192, 32×24 cells. *The skill:* designing around colour clash is
  the whole game.
- **NES (PPU)** — sprites 8×8 / 8×16, 3 colours + transparent; background 8×8 tiles, 4 palettes;
  16×16 attribute regions share a palette. *The skill:* careful palette planning under tight limits.
- **Amiga (Denise/Agnus)** — hardware sprites 16px wide, 3 colours + transparent; BOBs any size via
  the Blitter (at CPU/Blitter cost); up to 32 colours (5 bitplanes), 64/4096 in special modes.
  *The skill:* the most flexible — but BOB rendering costs performance.

## Per-platform audio (reference)

- **C64 (SID)** — 3 voices, each waveform (triangle/saw/pulse/noise) + ADSR + frequency; one shared
  filter (low/high/band); ring mod + sync. *Constraint:* 3 voices for music **and** SFX.
- **ZX Spectrum** — 48K: single 1-bit **beeper** (costs CPU time); 128K: **AY-3-8912**, 3 voices +
  noise. *Constraint:* beeper is tightly limited; AY is crisp.
- **NES (APU)** — 2 pulse (duty cycle), 1 triangle (bass/melody), 1 noise (percussion), 1 DMC
  (1-bit samples). *Constraint:* few voices; DMC is fiddly.
- **Amiga (Paula)** — 4 channels of 8-bit **sampled** audio (1&4 left, 2&3 right). *Constraint:*
  sample memory and mixing balance, not synthesis limits.

---

## Technique ladders (intro → deepen → own)

**Graphics:** silhouette & contrast (readability) → colour-coding & grid/tile design → minimal
animation → tile variety & character personality → UI/HUD clarity → attribute-aware layout →
dithering, sub-pixel animation, palette tricks. Attribute-aware design is *foundational* on the
Spectrum (colour clash) and the NES (16×16 palette regions), *advanced* elsewhere.

**Audio:** feedback sounds & pitch variation (a hit, a jump) → sound priority & short melodies →
ADSR shaping, arpeggios, jingles, tracker basics → audio pacing (tempo matches gameplay) → filter
sweeps, PWM, ring mod, dynamic music (responds to game state), DMC/digi-drums. Each technique attaches
to the game whose hardware introduces it (e.g. ADSR + arpeggios at the SID game; DMC at the NES audio
capstone; ring mod at a C64 capstone).

---

## Tools (vault-worthy)

**Historical graphics:** Deluxe Paint (Amiga) · OCP Art Studio (C64/Spectrum) · Koala Painter (C64) ·
The Graphics Machine (Spectrum). **Modern:** Aseprite · Pro Motion NG · Multipaint (handles
attribute constraints) · YY-CHR / NES Screen Tool (NES) · Charpad / Spritepad (C64) · GIMP/Photoshop
with an indexed palette.

**Historical audio:** SoundTracker / ProTracker (Amiga) · SID Wizard / Sound Monitor (C64) ·
Wham! Music Box (Spectrum AY). **Modern:** FamiTracker (NES) · DefleMask (multi-platform) ·
Vortex Tracker II (Spectrum AY) · OpenMPT (MOD) · BFXR/SFXR (quick SFX).

## Vault targets

A/V deserves the same vault depth as code. Still-to-build entries:

- **Artists** — Bernie Drummond, Oliver Frey, Bob Wakelin, Mark Ferrari, Henk Nieborg, Paul Robertson.
- **Composers** — Jeroen Tel, Fred Gray, Jonathan Dunn, Matt Furniss, Neil Baldwin, Manami Matsumae,
  Hirokazu "Hip" Tanaka, Yuzo Koshiro (plus the SID/AY names already catalogued).
- **Techniques** — dithering, attribute-aware design, palette cycling, pixel clusters, tile variation,
  arpeggio, PWM, filter sweep, vibrato, echo/delay, digi-drums.
- **Tools** — the lists above (Deluxe Paint, ProTracker, FamiTracker, SID Wizard, DefleMask, …).

(Created as the units that reference them ship — the required-vs-nice-to-have rule in
[content-creation-workflow.md](content-creation-workflow.md).)

---

## Asset provision and the honest truth

For learners who struggle with art/audio: provide **base assets** they can modify, optional **asset
packs** (focus on code), point to **communities** for sharing, and ship **tool tutorials**.

What we *can* teach: the technical constraints (you must understand them to make anything), the
principles (readability, feedback, communication), the tools and workflows, the historical context,
the platform-specific tricks. What's harder: raw artistic talent and a musical ear — but **constraints
breed creativity** (a limited palette forces good design), modern tools are excellent, communities
exist, and "programmer art" is a respected genre (Tetris, Elite's wireframe, Rogue/Dwarf Fortress's
ASCII). Many bedroom legends — Matthew Smith, Jeff Minter — learned *enough*, and personality beat
polish.

---

**The principle:** no game ships as code-only. Every path teaches you to make it *look* and *sound*
like it belongs on the machine.
