# Phase 4: Incoming

**Game:** Starfield (C64 Game 1)
**Units:** 49–64
**Theme:** Enemies shoot back — and raster interrupts change everything
**6510 Focus:** Interrupts (SEI/CLI), IRQ vector, raster register ($D012), hardware timing
**Hardware:** VIC-II raster interrupt system, SID oscillator 3 for random numbers
**Status:** Planned

---

## Overview

Phase 4 is the most important phase in the C64 curriculum. Not because of the gameplay feature (enemies shooting back), but because of the technique that enables it: **raster interrupts**.

The VIC-II can trigger a CPU interrupt when the electron beam reaches a specific screen line. Code runs at *exactly* that moment — not "sometime during the frame" but precisely at line N. This enables stable frame timing (replacing the bare `JMP` loop from Phase 1), colour effects, and eventually sprite multiplexing in Phase 7.

Every serious C64 game uses raster interrupts. Learning them here — motivated by the need for stable game timing — pays off for the entire curriculum.

The gameplay addition is two-way combat: enemies fire back. Combined with raster-stable timing, the game becomes a genuine challenge.

---

## Prerequisites from Phase 3

- Stack operations (PHA/PLA) — interrupt handlers must save and restore all registers
- Bit manipulation (AND/ORA) — interrupt enable and acknowledge bits
- Sprite allocation — enemy bullets need sprite slots
- 16-bit arithmetic — raster line values and timing calculations

---

## Unit Progression

| Unit | Title | New 6510 Concept | Game Addition |
|------|-------|-----------------|---------------|
| 49 | Enemy Bullet | Bullet pool pattern applied to enemy fire | Danger from above |
| 50 | Enemy Bullet Sprite | Distinct graphic from player bullet | Visible threat |
| 51 | Enemy Bullet Hits Player | Shared collision routine (generic, reusable) | Real danger |
| 52 | Enemy Fire Sound | SID voice 3 (noise channel for distinct gunshot) | Audio warning |
| 53 | Random Enemy Fires | SID oscillator 3 (`$D41B`) — free random byte | Unpredictable fire |
| 54 | Shooter Enemy Type | Direction calculation via subtraction | Aimed shots |
| 55 | Multiple Enemy Bullets | Pool allocation, cycling freed sprite slots | Intensity |
| 56 | Raster Interrupts Explained | `$D012`, `$D01A`, IRQ vector (`$FFFE`), `SEI`/`CLI` | **The big unlock** |
| 57 | Main Loop on Raster Sync | IRQ-driven frame timing replaces `JMP` loop | Smooth, stable animation |
| 58 | Raster Colour Bar | Colour change at specific scanline | C64 signature effect |
| 59 | Aimed vs Random Mix | Probability via `AND` mask on `$D41B` random byte | Shot variety |
| 60 | Bullet Destroys Bullet | Bullet-bullet collision check | Skill option |
| 61 | Death Clears Bullets | State reset, sprite disable sequence | Fair restart |
| 62 | Difficulty Ramp per Wave | Parameter tables indexed by wave number | Escalation |
| 63 | Bullet Density Tuning | Max bullet count, fire rate caps per wave | Not overwhelming |
| 64 | Integration + Combat Balance | Full playtesting with raster-stable timing | Challenging but fair |

---

## Key Teaching Moments

### SID Random Numbers (Unit 53)

The SID gives free random numbers with zero code. Voice 3's oscillator runs independently — set it to noise waveform, then read `$D41B` for a random byte whenever needed. No seed, no algorithm, no computation. This is a genuine C64 luxury that other platforms (Spectrum, NES) lack. From this point on, `$D41B` is the go-to random source.

### Raster Interrupts (Unit 56)

This is the single most important unit in the game — possibly in the entire C64 curriculum. The VIC-II's raster register (`$D012`) tracks which screen line is currently being drawn. By writing a line number to `$D012` and enabling raster interrupts (`$D01A`), the VIC-II triggers a CPU interrupt when the beam reaches that line.

The interrupt handler:
1. Saves registers (PHA/TXA/PHA/TYA/PHA)
2. Acknowledges the interrupt (write to `$D019`)
3. Runs game logic
4. Restores registers
5. Returns with `RTI`

The `SEI`/`CLI` pair disables/enables interrupts during setup. The IRQ vector at `$FFFE`/`$FFFF` (or the Kernal vector at `$0314`/`$0315`) points to the handler.

### Frame-Locked Timing (Unit 57)

Phase 1's game loop was a bare `JMP` — it ran as fast as the CPU could go, with no consistent frame rate. The raster interrupt replaces this: game logic runs once per frame, triggered by the raster reaching a specific line. Movement speeds become predictable. Animation timing becomes consistent. The game feels professional.

### Raster Colour Bar (Unit 58)

The classic C64 effect: change the border colour at a specific scanline to create a coloured band across the screen. This is a visual proof that raster interrupts work — if the colour bar is stable and clean, the timing is right. If it wobbles, there's a problem. The technique scales to multi-colour splits in Phase 5.

---

## 6510 Concepts Introduced

1. `SEI` / `CLI` — disable/enable interrupts (Unit 56)
2. IRQ vector — `$FFFE`/`$FFFF` or Kernal `$0314`/`$0315` (Unit 56)
3. `RTI` — return from interrupt (Unit 56)
4. Raster register `$D012` — set target line, read current line (Unit 56)
5. Interrupt acknowledge — write to `$D019` (Unit 56)
6. `$D41B` — SID voice 3 random byte (Unit 53)
7. Register save/restore in interrupt handler — PHA/TXA/TYA sequence (Unit 56)

---

## Hardware Registers

### New in Phase 4

| Register | Purpose | Introduced |
|----------|---------|-----------|
| `$D012` | Raster line compare (write target, read current) | Unit 56 |
| `$D019` | Interrupt status (write to acknowledge) | Unit 56 |
| `$D01A` | Interrupt enable (bit 0 = raster IRQ enable) | Unit 56 |
| `$D41B` | SID voice 3 oscillator output (random byte) | Unit 53 |
| `$D40E`/`$D40F` | Voice 3 frequency (set high for fast noise) | Unit 53 |
| `$D412` | Voice 3 control register (noise waveform) | Unit 53 |
| `$0314`/`$0315` | Kernal IRQ vector (alternative to `$FFFE`) | Unit 56 |

---

## Game State at Phase End

After Unit 64:

- **Two-way combat** — enemies fire bullets at the player (random and aimed)
- **Raster interrupts** — frame timing is locked to the display refresh
- **Colour bar** — visible raster effect in the border (proof of technique)
- **SID random** — `$D41B` used for fire timing and spawn decisions
- **Difficulty curve** — enemy fire rate, bullet speed, and bullet count escalate per wave
- **Bullet interaction** — player bullets can destroy enemy bullets (skill option)
- **Fair restarts** — death clears all enemy bullets

The game is now a genuine challenge. Two-way combat with raster-stable timing makes it feel like a commercial C64 game.

---

## What Carries to Phase 5

- **Raster interrupts** — the foundation for colour splits, screen splits, and eventually multiplexing
- **Interrupt handler structure** — save/restore pattern reused for all future interrupt code
- **$D012 timing** — understanding raster lines is essential for visual effects
- **Frame-locked updates** — all future phases assume consistent timing

Phase 4's raster interrupt framework is the single most reused piece of code in the entire game.

---

**Version:** 1.0
**Last Updated:** 2026-02-06
