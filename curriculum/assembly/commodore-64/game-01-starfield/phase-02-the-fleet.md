# Phase 2: The Fleet

**Game:** Starfield (C64 Game 1)
**Units:** 17–32
**Theme:** Multiple enemy types with distinct behaviours
**6510 Focus:** Indexed addressing depth, lookup tables, indirect addressing, comparison chains
**Hardware:** Full VIC-II sprite system (all 8 slots), hardware collision registers
**Status:** Planned

---

## Overview

Phase 1 proved three identical enemies could work. Phase 2 makes them different. Fast divers, slow drifters, zigzag weavers — each enemy type has distinct graphics, colours, movement patterns, and point values, all driven by data tables rather than hard-coded logic.

The 6510 focus shifts from learning individual instructions to using them in combination. Stride-based table access gives the 6502 something resembling structs. Lookup tables replace `if`/`else` chains. The wave system adds game structure — clear all enemies, advance to the next wave with harder composition.

By Unit 32, all 8 hardware sprite slots are in active use and the learner understands data-driven design: change the tables, change the game.

---

## Prerequisites from Phase 1

- Indexed addressing (`LDA table,X`) — used extensively, now with stride offsets
- Subroutines (`JSR`/`RTS`) — expanded to multiple routines
- Sprite management — 5 slots used, Phase 2 fills all 8
- Collision detection — distance-check pattern generalised
- State machine — game states gain wave sub-states
- Screen RAM — HUD extends to show wave number

---

## Unit Progression

| Unit | Title | New 6510 Concept | Game Addition |
|------|-------|-----------------|---------------|
| 17 | Enemy Data Table | Stride access (`LDA table,X` with offset multiplication) | Organised enemy data |
| 18 | Multiple Enemies from Table | Loop with index offset, zero-page pointer arithmetic | Several enemies on screen |
| 19 | Fast Enemy | Speed as a data field, parameterised movement | Diver enemy type |
| 20 | Slow Enemy | Combined X+Y velocity from table | Drifter enemy type |
| 21 | Zigzag Enemy | Direction toggle or sine table lookup | Weaver enemy type |
| 22 | Sprite Graphics per Type | Sprite pointer table (`$07F8`+), indirect load | Visual distinction |
| 23 | Colours per Type | Colour as data field → `$D027`+ register write | Instant recognition |
| 24 | Point Values per Type | Score lookup table, indexed add to score | Risk/reward |
| 25 | Wave System | Enemy alive counter, wave-clear detection, state transitions | Structured progression |
| 26 | Wave Composition Tables | Data-driven wave definitions (type counts, spawn positions) | Varied challenge |
| 27 | Faster Each Wave | Timer adjustment per wave, difficulty curve | Escalation |
| 28 | Wave Number Display | HUD update routine for wave counter | Visible progress |
| 29 | Sprite Priority | `$D01B` (sprite-background priority register) | Correct visual layering |
| 30 | X High Bit Management | `$D010` bit manipulation across all 8 sprites | No X-position bugs |
| 31 | Hardware Collision | `$D01E` sprite-sprite, `$D01F` sprite-background | C64 collision registers |
| 32 | Integration + Balance | Wave composition tuning, speed parameters, playtesting | Fair, escalating challenge |

---

## Key Teaching Moments

### Stride-Based Table Access (Unit 17)

The 6510 has no structs. Phase 1's parallel arrays (separate tables for X, Y, flash) work for simple data, but enemy types need more fields: type, X, Y, speed, alive status, point value. The stride approach stores all fields for one enemy contiguously — enemy 0 at offsets 0–5, enemy 1 at offsets 6–11. `LDA enemy_table,X` with X set to the right multiple gives struct-like access. This pattern underpins every data-driven system from here on.

### Data-Driven Design (Units 22–24)

Three separate pieces of enemy data — sprite graphic, colour, point value — are stored as tables indexed by enemy type. The update loop doesn't contain type-specific code; it reads the type field, looks up the parameters, and applies them generically. Adding a new enemy type means adding table entries, not code. This is the first time the learner sees the power of separating data from logic.

### Hardware Collision Detection (Unit 31)

The VIC-II detects sprite-sprite collisions in hardware — reading `$D01E` returns a bitmask of which sprites overlap. No distance calculations needed. This is a genuine C64 advantage. But: the register clears on read (you get one chance), and it only tells you *which* sprites collided, not *which pair*. Software logic is still needed to determine what happened. The learner sees that hardware assistance and software logic complement each other.

### Wave System (Unit 25)

Until now, enemies just respawn indefinitely. The wave system adds structure: each wave defines a composition (which types, how many), and clearing all enemies triggers the next wave. An alive counter tracks remaining enemies — when it reaches zero, the wave is complete. This transforms "shoot things forever" into "clear wave → advance → harder wave."

---

## 6510 Concepts Introduced

1. Stride-based table access — multi-field records via offset multiplication (Unit 17)
2. Zero-page pointer arithmetic — calculating table offsets dynamically (Unit 18)
3. Lookup tables for parameterisation — type → graphic, colour, points (Units 22–24)
4. Counter-based state transitions — alive count triggers wave advance (Unit 25)
5. Data-driven wave definitions — game content as table data (Unit 26)
6. Multi-sprite `$D010` management — bit manipulation across all 8 sprites (Unit 30)
7. Hardware collision register (`$D01E`) — read-once bitmask (Unit 31)

---

## Hardware Registers

### New in Phase 2

| Register | Purpose | Introduced |
|----------|---------|-----------|
| `$D00A`–`$D00F` | Sprite 5–7 X/Y positions | Unit 18 |
| `$D01B` | Sprite-background priority | Unit 29 |
| `$D01E` | Sprite-sprite collision | Unit 31 |
| `$D01F` | Sprite-background collision | Unit 31 |
| `$D02C`–`$D02E` | Sprite 5–7 individual colours | Unit 23 |
| `$07FD`–`$07FF` | Sprite 5–7 data pointers | Unit 22 |

---

## Game State at Phase End

After Unit 32:

- **Enemy types** — 4+ distinct types: diver (fast, straight down), drifter (slow, diagonal), weaver (zigzag), and standard
- **Wave system** — clear all enemies to advance; each wave has defined composition and escalating difficulty
- **All 8 sprites** — ship (1), bullet (1), enemies (6) — all slots managed
- **Visual variety** — different sprite graphics and colours per enemy type
- **Scoring** — point values vary by type (risk/reward for targeting fast enemies)
- **HUD** — score + lives + wave number
- **Hardware collision** — VIC-II collision registers supplement distance checks

The game feels structured — not just endless spawning, but waves with rhythm and escalation.

---

## What Carries to Phase 3

- **Full sprite allocation** — all 8 slots used, Phase 3 must solve allocation when power-ups need sprites
- **Data-driven design** — power-up types stored as data tables, same pattern as enemy types
- **Wave system** — power-up drop rates can vary per wave
- **Stride-based tables** — extended for power-up state tracking

---

**Version:** 1.0
**Last Updated:** 2026-02-06
