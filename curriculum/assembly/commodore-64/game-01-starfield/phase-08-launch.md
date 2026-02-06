# Phase 8: Launch

**Game:** Starfield (C64 Game 1)
**Units:** 113–128
**Theme:** Commercial release quality
**6510 Focus:** Code optimisation, memory management, I/O routines, PAL/NTSC detection
**Hardware:** CIA timers for PAL/NTSC, keyboard matrix, complete system integration
**Status:** Planned

---

## Overview

Phase 8 adds everything a real 1986 C64 game would ship with: high scores with initials entry, difficulty selection, two-player alternating mode, an attract mode demo, and PAL/NTSC compatibility. No new hardware concepts are introduced — instead, every technique from Phases 1–7 is refined, optimised, and integrated into a polished product.

The 6510 focus shifts from learning to engineering. Code is profiled and optimised. Memory layout is audited. Edge cases are found and fixed. The result is a ROM-quality `.prg` file that could be put on tape and sold through a 1986 software house.

This phase also serves as a capstone assessment: if the learner can add these features — each touching multiple systems simultaneously — they've truly mastered C64 programming.

---

## Prerequisites from Phase 7

- Sprite multiplexing — attract mode must handle the same visual complexity
- Complex state machines — menu systems layer additional states
- Complete SID control — music and sound during menus and transitions
- Full VIC-II mastery — loading screens, title effects, and gameplay share the hardware

---

## Unit Progression

| Unit | Title | New 6510 Concept | Game Addition |
|------|-------|-----------------|---------------|
| 113 | High Score Table | Sorted insertion, multi-byte comparison | Top 5 scores |
| 114 | Initials Entry | Keyboard matrix scanning (`$DC00`/`$DC01`), character input | 3-letter names |
| 115 | High Scores on Title | Persistent display integration in title state | Bragging rights |
| 116 | Difficulty Select | Menu system, joystick cursor navigation | 3 difficulty levels |
| 117 | Difficulty Affects Gameplay | Parameter tables indexed by difficulty level | Real difference |
| 118 | Extra Life at 10,000 | Threshold detection with 16-bit compare, celebration effect | Skill reward |
| 119 | Two-Player Alternating | Player state switching, turn management on death | Social play |
| 120 | Score Comparison | Side-by-side display at game over | Competition |
| 121 | Attract Mode | Recorded input playback or simple AI pilot | Auto-play demo |
| 122 | Demo on Title Timeout | Timer-triggered state change after idle period | Shop display |
| 123 | PAL/NTSC Detection | CIA timer comparison for 50Hz vs 60Hz, speed adjustment | Platform correct |
| 124 | Continue Option | Limited continues, wave restart, score penalty | Forgiveness |
| 125 | Loading Screen | Advanced character graphics layout (charset art) | Presentation |
| 126 | Credits Screen | Text display with colour cycling effects | Attribution |
| 127 | Final Balance + Bug Sweep | Systematic edge case testing, playtesting | Release ready |
| 128 | **Complete Game** | Packaging, file optimisation, autostart | **Ship it** |

---

## Key Teaching Moments

### Sorted Insertion (Unit 113)

The high score table maintains 5 entries in descending order. When a new score qualifies, existing entries shuffle down to make room. This is a multi-byte comparison (scores are 3+ bytes) followed by a block copy. On the 6502, this means nested loops with careful index management. It's a real algorithm, not just hardware register manipulation — a signal that the learner has graduated from "hardware programmer" to "programmer."

### Keyboard Matrix (Unit 114)

The C64 keyboard is a matrix: CIA1 port A ($DC00) selects a row, port B ($DC01) reads the columns. Scanning requires writing to one port and reading the other, checking for key-down states. This is the first time the learner writes to a CIA port (previously, `$DC00` was read-only for joystick). The same hardware, used differently.

### PAL/NTSC Detection (Unit 123)

C64s exist in two flavours: PAL (50Hz, 312 scanlines, most of Europe) and NTSC (60Hz, 263 scanlines, North America). Games that assume one will run too fast or too slow on the other. Detection uses the CIA timer: count cycles during a known number of frames, compare against threshold. Once detected, speed parameters adjust globally. This is the kind of detail that separates amateur homebrew from professional releases.

### Attract Mode (Unit 121)

With no player input, the title screen transitions to a gameplay demo — either replaying recorded inputs or running a simple AI. This requires the entire game engine to run normally while input comes from a data stream instead of the joystick. The abstraction: input is read from a source (joystick or recording), and the game doesn't know the difference. This separation of input from logic validates the game's architecture.

### The Final .prg (Unit 128)

The last unit produces the release build. Memory is audited — no wasted bytes, no overlapping data. The BASIC stub launches the game. Everything loads from a single file. The learner has a complete artefact: a `.prg` file that runs on any C64, emulated or real.

---

## 6510 Concepts Introduced

1. Multi-byte comparison — comparing 3+ byte scores with cascading carry (Unit 113)
2. Block memory copy — shuffling table entries for sorted insertion (Unit 113)
3. Keyboard matrix scanning — CIA port A/B write-read pattern (Unit 114)
4. Menu state machine — joystick-driven cursor over options (Unit 116)
5. Parameter tables by difficulty — same code, different data per difficulty (Unit 117)
6. Input abstraction — game reads from source (live or recorded) (Unit 121)
7. CIA timer measurement — counting cycles for PAL/NTSC detection (Unit 123)
8. Speed compensation — adjusting movement/timing values for refresh rate (Unit 123)

---

## Hardware Registers

### New in Phase 8

| Register | Purpose | Introduced |
|----------|---------|-----------|
| `$DC01` | CIA1 port B (keyboard column read) | Unit 114 |
| `$DC00` | CIA1 port A (keyboard row select — new write usage) | Unit 114 |

All other registers are already known. Phase 8's challenge is using them all together correctly.

---

## Game State at Phase End

After Unit 128 — the complete game:

- **High scores** — top 5 with 3-letter initials, sorted, displayed on title screen
- **Difficulty** — Easy/Normal/Hard with joystick menu selection
- **Two-player** — alternating play, score comparison at game over
- **Attract mode** — auto-play demo after title screen timeout
- **PAL/NTSC** — detected automatically, speeds adjusted
- **Continue system** — limited continues with score penalty
- **Loading screen** — character art displayed while loading
- **Credits** — attribution screen with colour effects
- **Full audio** — three-voice music, crafted SFX, filter sweeps, jingles
- **Full visuals** — multicolour sprites, custom characters, raster splits, parallax starfield
- **Boss fights** — multi-phase encounters with sprite multiplexing
- **Wave system** — escalating difficulty with varied enemy types and compositions

A game you could put on tape and sell in 1986.

---

## Quality Comparison Across All Phases

| Aspect | Phase 1 | Phase 4 | Phase 8 |
|--------|---------|---------|---------|
| Graphics | Single-colour sprites, ROM font | + smooth movement | Multicolour, parallax, custom font, raster splits |
| Enemies | 3 identical, fall down | + shoot back, 4 types | + bosses, multiplexed sprites, patterns |
| Player | Move + shoot | + power-ups, shield | + difficulty select, two-player |
| Audio | 2 SID beeps | + 3 voices, varied SFX | Full music, filter sweeps, voice priority |
| Structure | 3 states | + waves, difficulty ramp | High scores, attract mode, PAL/NTSC |
| 6510 Skill | LDA/STA, branches | + interrupts, tables | Full instruction set, multiplexing, optimisation |

---

## What This Game Teaches

By completing Starfield, learners are ready for:

- **Game 2 (128 units)** — sprite skills transfer to character/tile-based movement; SID knowledge deepens
- **Game 3 (128 units)** — custom character sets become tile-based level design
- **Games 5–10** — raster interrupts, sprite multiplexing, and SID mastery are reused and extended
- **Every future C64 game** — the patterns established here (state machines, data-driven design, raster timing) are foundational

Starfield isn't just Game 1. It's the foundation for the entire C64 curriculum.

---

**Version:** 1.0
**Last Updated:** 2026-02-06
