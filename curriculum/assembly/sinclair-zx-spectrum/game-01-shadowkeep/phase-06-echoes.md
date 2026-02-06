# Phase 6: Echoes

**Game:** Shadowkeep (ZX Spectrum Game 1)
**Units:** 81–96
**Theme:** Sound and music — from beeper to AY chip
**Z80 Focus:** Precise timing loops, OUT port mastery, interrupt modes, 128K detection
**Hardware:** Beeper (port $FE bit 4), AY-3-8912 (128K, ports $FFFD/$BFFD), interrupt mode 2
**Status:** Planned

---

## Overview

The 48K Spectrum's "sound chip" is a single bit. Toggling bit 4 of port $FE creates a square wave. The pitch depends entirely on how fast your code toggles it — which means sound generation is CPU-intensive. No background music during gameplay unless you're very clever.

Phase 6 starts with the beeper's constraints and wrings everything possible from them: pitch control, duration, slides, multi-tone tricks. Then it introduces the 128K Spectrum's AY-3-8912 — a proper 3-voice sound chip with hardware envelopes, noise generation, and register-based control. With the AY, background music becomes trivial.

The phase handles both models: 48K gets crafted beeper effects, 128K gets full music. A detection routine at startup chooses the right path. This dual-target approach mirrors real commercial Spectrum development.

---

## Prerequisites from Phase 5

- Tight loops — timing precision from pixel calculation work
- OUT instruction — already used for border colour
- LDIR and memory management — sound data stored efficiently
- Complete game to enhance — all gameplay systems are in place

---

## Unit Progression

| Unit | Title | New Z80 Concept | Game Addition |
|------|-------|----------------|---------------|
| 81 | Beeper Fundamentals | `OUT ($FE),A` bit 4 toggle, delay loop = pitch | First controlled tone |
| 82 | Pitch Control | Loop count determines frequency, note table | Tuneable pitch |
| 83 | Sound Effect Library | Parameterised routine (pitch, duration, sweep) | Collect, hit, door, death |
| 84 | Duration Control | Outer loop wraps pitch loop, counts cycles | Timed sounds |
| 85 | Pitch Slides | Increment/decrement delay value over time | Sweeping effects |
| 86 | Multi-Tone | Rapid alternation between two frequencies | Richer beeper sound |
| 87 | Staccato Rhythms | Short bursts with silence gaps | Percussion feel |
| 88 | Title Music (Beeper) | Note sequence with timing data, playback routine | 48K atmosphere |
| 89 | In-Game Ambient (Beeper) | Brief phrases between game updates | Subtle tension |
| 90 | AY-3-8912 Introduction | Register-based chip, 3 voices, port $FFFD/$BFFD | **128K sound chip** |
| 91 | AY Sound Effects | Hardware envelope, noise channel | Richer effects |
| 92 | AY Music Engine | Note table, 3-voice playback, pattern sequencing | Proper background music |
| 93 | Interrupt Mode 2 | `IM 2`, vector table, interrupt-driven music | Music plays during gameplay |
| 94 | AY Title Music | Full 3-voice title theme | Atmospheric title |
| 95 | 48K/128K Detection | Test for AY presence, choose audio path | Both models supported |
| 96 | Integration + Balance | Volume, effect placement, music-SFX coexistence | Cohesive audio |

---

## Key Teaching Moments

### The Beeper (Unit 81)

The simplest sound hardware possible: one bit controls a speaker. Toggle it fast, high pitch. Toggle it slow, low pitch. The Z80 code is a delay loop with `OUT` at each end:

```z80
beep:
    ld b,duration
.loop:
    xor $10             ; Toggle bit 4
    out ($fe),a         ; Send to speaker
    ld c,pitch
.delay:
    dec c
    jr nz,.delay
    djnz .loop
    ret
```

The constraint: while this loop runs, nothing else happens. No enemies move, no input is read. Sound blocks the CPU. This is why 48K Spectrum games often have brief sound effects between game frames rather than continuous music.

### The AY-3-8912 (Unit 90)

The 128K Spectrum includes a General Instrument AY-3-8912 — the same chip found in the Amstrad CPC and MSX. Three tone channels, one noise channel, hardware ADSR-like envelopes, and register-based control. Access is indirect: write the register number to port $FFFD, then write the value to port $BFFD. The AY runs independently — set up the registers and it generates sound without CPU intervention.

### Interrupt Mode 2 (Unit 93)

`IM 2` sets up a vector table that the Z80 indexes on each interrupt. A 50Hz interrupt (from the ULA's VSYNC) drives the music sequencer: read the next note, update AY registers, advance the sequence pointer. Music plays automatically during gameplay with no main loop coordination needed. This is how every commercial 128K Spectrum game handles background music.

### 48K/128K Detection (Unit 95)

Commercial games detect the machine model at startup. Write a value to an AY register, read it back. If it matches, the AY chip is present (128K). If not, fall back to beeper. The game stores a flag and all audio code branches on it:

```z80
    ld a,(is_128k)
    or a
    jr z,beeper_sound
    ; AY sound code...
```

This is real-world multi-target development — the same binary runs correctly on both machines.

---

## Z80 Concepts Introduced

1. `OUT ($FE),A` bit 4 — beeper toggle (Unit 81)
2. Timing loops for pitch — `DEC C` / `JR NZ` as delay (Unit 81)
3. Parameterised sound routine — pitch, duration, sweep as parameters (Unit 83)
4. AY register access — `OUT ($FFFD),A` then `OUT ($BFFD),A` (Unit 90)
5. `IM 2` — interrupt mode 2, vector table setup (Unit 93)
6. 50Hz interrupt handler — music sequencer driven by VSYNC (Unit 93)
7. `DI` / `EI` — disable/enable interrupts during setup (Unit 93)
8. Hardware detection — write/read test for AY presence (Unit 95)

---

## Hardware

### New in Phase 6

| Port/Register | Purpose | Introduced |
|---------------|---------|-----------|
| `$FE` bit 4 | Beeper output (already known for border) | Unit 81 |
| `$FFFD` | AY register select (128K only) | Unit 90 |
| `$BFFD` | AY register write (128K only) | Unit 90 |

### AY-3-8912 Registers (128K)

| Register | Purpose | Introduced |
|----------|---------|-----------|
| R0/R1 | Channel A tone period (12-bit) | Unit 90 |
| R2/R3 | Channel B tone period | Unit 92 |
| R4/R5 | Channel C tone period | Unit 92 |
| R6 | Noise period (5-bit) | Unit 91 |
| R7 | Mixer: tone/noise enable per channel | Unit 90 |
| R8–R10 | Channel A/B/C volume (or envelope flag) | Unit 90 |
| R11/R12 | Envelope period | Unit 91 |
| R13 | Envelope shape | Unit 91 |

---

## Game State at Phase End

After Unit 96:

- **48K beeper effects** — collect, hit, door open/denied, death, room complete
- **48K beeper music** — simple title theme, brief in-game phrases
- **128K AY effects** — richer versions of all effects with hardware envelopes
- **128K AY music** — 3-voice title theme, in-game background music
- **Automatic detection** — game detects 48K/128K and uses appropriate audio
- **Interrupt-driven music** — AY music plays during gameplay without blocking (128K)
- **Pitch slides** — sweeping effects on beeper for dramatic moments
- **Balanced mix** — effects don't clash with music on 128K

The keep has atmosphere. Footsteps echo, doors creak, creatures snarl, and music builds tension.

---

## What Carries to Phase 7

- **Interrupt mode 2** — Phase 7 uses interrupts for game timing and effects
- **AY control** — atmospheric sound during fog-of-war and boss sequences
- **Beeper expertise** — dramatic sound cues for 48K players
- **48K/128K branching** — pattern reused for extra 128K content

---

**Version:** 1.0
**Last Updated:** 2026-02-06
