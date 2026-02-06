# Phase 1: Ignition

**Game:** Starfield (C64 Game 1)
**Units:** 1–16
**Theme:** Complete game loop — shoot enemies, score points, die, restart
**6510 Focus:** Registers (A/X/Y), zero page, addressing modes, branches, subroutines
**Hardware:** VIC-II sprites, SID voices 1–2, CIA joystick port, screen/colour RAM
**Status:** Implemented (Units 1–16 published)

---

## Overview

Phase 1 takes a learner from zero assembly knowledge to a complete, playable game. By Unit 16, Starfield has a player ship with full-width movement, three simultaneous enemies, collision detection, scoring, three lives, a parallax starfield background, a title screen, and sound effects. Every unit produces a visible or audible change — there are no theory-only sessions.

Two principles guided implementation: **always playable** (the ship moves from Unit 2) and **one concept per unit** (each session introduces exactly one new 6510 idea). This keeps momentum high and debugging manageable — when something breaks, the learner knows which change caused it.

The phase covers an enormous amount of ground in 16 units: from `LDA`/`STA` to indirect indexed addressing, from a static sprite to a three-state game with parallax scrolling. The secret is that every concept earns its place — nothing is taught in the abstract.

---

## What Changed from the Outline

The full game outline proposed a different unit order for Phase 1. Several changes were made during implementation:

| Planned | Actual | Reason |
|---------|--------|--------|
| Unit 9: Enemies spawn continuously (SID random) | Enemy Waves (indexed addressing, JSR/RTS) | Indexed addressing and subroutines are more fundamental than SID random. Three simultaneous enemies are more visually exciting than continuous single spawning |
| Unit 12: Press fire to restart | Three Lives | Restart logic was absorbed into Game Over (Unit 11). Lives needed to precede the title screen |
| Unit 13: Title screen | Life Lost Flash | Border flash is simpler and gives immediate feedback. The state machine is complex enough to come later |
| Unit 14: Three lives | Starfield | With lives done at Unit 12, this slot could give the game its visual identity |
| Unit 15: Life lost flash/sound | Title Screen | The three-state machine is the most architecturally significant addition — it benefits from coming near the end |
| Unit 16: Integration + edge cases | Screen Edges | `$D010` is a genuine teaching moment deserving its own unit, not just cleanup |

The biggest change: the starfield background was pulled from Phase 5 (Unit 66 in the outline) into Phase 1. This uses screen RAM characters (asterisks and periods) rather than custom character sets — a simpler approach that still gives the game its name and visual identity. Phase 5 will upgrade to proper custom characters with animation.

The random X position for enemy spawning uses the raster register (`$D012`) rather than the SID oscillator (`$D41B`). SID random is deferred to Phase 4 where it fits more naturally alongside raster interrupts.

---

## Unit Progression

| Unit | Title | New 6510 Concept | Game Addition |
|------|-------|-----------------|---------------|
| 1 | Ship on Screen | `LDA`/`STA`, immediate addressing, memory-mapped I/O | White ship on black screen |
| 2 | Joystick Movement | `AND` bit mask, `BEQ`/`BNE`, `INC`/`DEC`, game loop (`JMP`) | Ship moves with joystick |
| 3 | Fire Button Shoots | Zero-page variables, sprite enable/disable via `ORA`/`AND` | Bullet flies upward |
| 4 | Laser Sound | SID registers (`$D400`+), waveform selection, gate bit | "Pew" on fire |
| 5 | Enemy Appears | Second sprite setup, `CMP`/`BCC` for boundary check | Enemy drifts downward |
| 6 | Direct Hit | `SEC`/`SBC` for distance, multi-condition branches | Bullet destroys enemy |
| 7 | Explosion | SID voice 2 (noise channel), sprite colour change, frame timer | Flash + boom on kill |
| 8 | Scoring Points | Screen RAM writes (`$0400`), colour RAM (`$D800`), BCD-style display | Two-digit score |
| 9 | Enemy Waves | `LDA table,X` indexed addressing, `JSR`/`RTS`, `LDY`/`CPX` loop | Three enemies at once |
| 10 | Player Death | Collision loop over enemy array, `game_over` flag | Ship can be destroyed |
| 11 | Game Over | Screen RAM text output, `init_game` reset routine | "GAME OVER" + restart |
| 12 | Three Lives | `DEC` for countdown, HUD display in top corner | Three chances per game |
| 13 | Life Lost Flash | Border colour (`$D020`), death timer, invulnerability window | Red border flash on death |
| 14 | Starfield | Indirect indexed `STA ($fb),Y`, row address lookup tables | Parallax star background |
| 15 | Title Screen | State machine (title/playing/game over), `CMP`/`BEQ` chains | "STARFIELD — PRESS FIRE" |
| 16 | Screen Edges | `$D010` MSB register, `EOR` bit toggling, boundary clamping | Full-width sprite movement |

---

## Key Teaching Moments

### Memory-Mapped I/O (Unit 1)

The entire C64 hardware is controlled by writing values to memory addresses. No function calls, no APIs — `STA $D027` changes sprite 0's colour because the VIC-II chip watches that address. This is the single most important concept in the phase: once a learner understands that hardware responds to memory writes, every subsequent unit is just "write the right value to the right address."

### The Game Loop (Unit 2)

Unit 2 establishes the read-input → update-state → draw pattern that every subsequent unit follows. The loop is a bare `JMP` back to the top — no frame timing, no interrupts. It works because the VIC-II reads sprite registers asynchronously. Frame-locked timing comes in Phase 4 with raster interrupts; for now, the simple loop is correct and sufficient.

### Indexed Addressing and Subroutines (Unit 9)

The jump from one enemy to three is the phase's largest code change. Single variables become parallel arrays. `LDA enemy_x` becomes `LDA enemy_x_tbl,X`. The X register transforms from "another register" into a loop index that processes all three enemies with identical code. Simultaneously, `spawn_enemy` becomes the first subroutine — code called from two places (init and respawn) via `JSR`/`RTS`. This unit introduces two fundamental concepts at once, justified by the fact that they're needed together.

### Indirect Indexed Addressing (Unit 14)

Writing a star to a specific screen position requires a 16-bit address calculated from row and column. `STA ($fb),Y` — store at the address in zero-page bytes $fb/$fc, offset by Y — is the 6502's most powerful addressing mode. A row-address lookup table provides the base; Y provides the column offset. This is the most sophisticated concept in Phase 1 and the foundation for all future screen RAM manipulation.

### The State Machine (Unit 15)

Three game states (title, playing, game over) controlled by a single zero-page variable and `CMP`/`BEQ` chains. This is the first time code is structured around states rather than linear flow. Each state has its own update logic, its own draw logic, and defined transitions. Every future game in the curriculum uses this pattern.

### 9-Bit Sprite Positions (Unit 16)

The VIC-II stores sprite X positions in 8-bit registers, but the screen is 320 pixels wide. `$D010` provides the ninth bit for each sprite. Managing this across movement (toggle on wrap), collision (skip when MSB differs), and state resets (clear on respawn) is genuinely complex. It earns a dedicated unit rather than being buried in an "integration" session.

---

## 6510 Concepts Introduced

In order of first appearance:

1. `LDA` / `STA` — load and store (Unit 1)
2. `LDX` / `INX` / `BNE` — loop with counter (Unit 1, screen clear)
3. `JMP` — unconditional jump, game loop (Unit 2)
4. `AND` — bit masking for joystick (Unit 2)
5. `BEQ` / `BNE` — conditional branches (Unit 2)
6. `INC` / `DEC` — increment/decrement memory (Unit 2)
7. `ORA` — set specific bits (Unit 3, sprite enable)
8. `CMP` / `BCC` / `BCS` — unsigned comparison and branches (Unit 5)
9. `SEC` / `SBC` — subtract with borrow (Unit 6, distance check)
10. `CLC` / `ADC` — add with carry (Unit 8, score)
11. `LDA table,X` / `STA table,X` — indexed addressing (Unit 9)
12. `LDY` / `CPX` — Y register, compare X (Unit 9)
13. `JSR` / `RTS` — subroutine call and return (Unit 9)
14. `STA ($fb),Y` — indirect indexed addressing (Unit 14)
15. `EOR` — exclusive OR for bit toggling (Unit 16)

---

## Hardware Registers

### VIC-II ($D000–$D02E)

| Register | Purpose | Introduced |
|----------|---------|-----------|
| `$D000`/`$D001` | Sprite 0 X/Y position | Unit 1 |
| `$D002`–`$D009` | Sprite 1–4 X/Y positions | Units 3, 5, 9 |
| `$D010` | Sprite X position MSB (9th bit) | Unit 16 |
| `$D015` | Sprite enable (1 bit per sprite) | Unit 1 |
| `$D020` | Border colour | Unit 13 |
| `$D021` | Background colour | Unit 1 |
| `$D027`–`$D02B` | Sprite 0–4 individual colours | Units 1, 3, 5, 7, 9 |
| `$07F8`–`$07FC` | Sprite 0–4 data pointers | Units 1, 3, 5, 9 |

### SID ($D400–$D418)

| Register | Purpose | Introduced |
|----------|---------|-----------|
| `$D400`/`$D401` | Voice 1 frequency (lo/hi) | Unit 4 |
| `$D404` | Voice 1 control (waveform + gate) | Unit 4 |
| `$D405`/`$D406` | Voice 1 ADSR | Unit 4 |
| `$D407`–`$D40D` | Voice 2 frequency, control, ADSR | Unit 7 |
| `$D418` | Volume + filter mode | Unit 4 |

### CIA ($DC00)

| Register | Purpose | Introduced |
|----------|---------|-----------|
| `$DC00` | Joystick port 2 (active low) | Unit 2 |

### Memory

| Address Range | Purpose | Introduced |
|---------------|---------|-----------|
| `$0400`–`$07E7` | Screen RAM (40×25 characters) | Unit 1 (clear), Unit 8 (score), Unit 14 (stars) |
| `$07F8`–`$07FF` | Sprite data pointers | Unit 1 |
| `$D800`–`$DBE7` | Colour RAM | Unit 8 (score colour) |
| `$2000`–`$2140` | Sprite graphic data (blocks 128–132) | Unit 1 |

---

## Game State at Phase End

After Unit 16, the learner has a complete, playable game:

- **Player ship** — full-width joystick movement (X range 0–320 via $D010), boundary-clamped
- **Bullet** — fires upward on button press, one active at a time
- **Three enemies** — descend at constant speed, respawn on kill or off-screen
- **Collision** — bullet→enemy (kill + score) and enemy→ship (death)
- **Scoring** — two-digit display in screen RAM, increments per kill
- **Three lives** — displayed in HUD, border flash and invulnerability on death
- **Sound** — SID voice 1 (pulse laser), SID voice 2 (noise explosion)
- **Starfield** — eight stars at two parallax speeds behind gameplay
- **Title screen** — "STARFIELD" centred with "PRESS FIRE TO PLAY", stars scrolling
- **Game over** — "GAME OVER" text, fire button restarts
- **State machine** — three states (title → playing → game over → title) with clean transitions

Code size: ~800 lines of assembly. Zero-page usage: `$02`–`$19`. Sprites: 0 (ship), 1 (bullet), 2–4 (enemies). SID: voices 1–2. No raster interrupts, no custom character set, no music.

---

## What Carries to Phase 2

Phase 2 (The Fleet) builds directly on:

- **Indexed addressing** — enemy tables expand from 3 entries to support multiple types with different behaviours
- **Subroutine pattern** — `spawn_enemy` becomes a model for parameterised routines throughout
- **Sprite management** — Phase 2 fills all 8 sprite slots, requiring careful allocation
- **Collision framework** — generalised to handle different entity types and point values
- **Screen RAM** — HUD expands to show wave number and additional information
- **State machine** — gains sub-states for wave transitions and gameplay structure

Phase 2 assumes all Phase 1 concepts are solid. No Phase 1 topic is re-taught.

---

## Implementation Notes

**What worked well:**
- One-concept-per-unit pacing kept each session focused and debuggable
- Sound from Unit 4 (not Unit 10+) gave early emotional payoff
- Pulling the starfield into Phase 1 gave the game its identity immediately
- Indexed addressing + subroutines in the same unit worked because the motivation (three enemies) made both concepts obviously necessary

**What to watch for in future phases:**
- The game loop is a bare `JMP` with no frame timing — Phase 4 must replace this with raster interrupt timing
- The starfield uses default character ROM characters — Phase 5 should upgrade to custom characters
- Enemy spawning uses `$D012` (raster register) for random X — Phase 4 introduces `$D41B` (SID random) as a proper alternative
- Only 5 of 8 sprite slots are used — Phase 2 immediately needs the remaining three

---

**Version:** 1.0
**Last Updated:** 2026-02-06
