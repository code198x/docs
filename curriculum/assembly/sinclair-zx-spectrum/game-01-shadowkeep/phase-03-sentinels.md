# Phase 3: Sentinels

**Game:** Shadowkeep (ZX Spectrum Game 1)
**Units:** 33–48
**Theme:** Creatures that guard the keep
**Z80 Focus:** Array processing, timer management, CP chains for AI, XOR for animation
**Hardware:** FRAMES system variable for timing, border colour for feedback
**Status:** Planned

---

## Overview

Empty rooms are puzzles. Rooms with creatures are challenges. Phase 3 adds enemies that patrol corridors, block routes, and damage the player on contact. Each enemy follows a simple rule — walk until you hit a wall, then turn around — but multiple enemies with different speeds create complex situations.

The Z80 focus is array processing and simple AI. Enemy data lives in tables (position, direction, speed, alive flag). A loop processes each enemy per frame: move, check wall collision, reverse if blocked, check player proximity. The same attribute-reading collision that works for the player works for enemies — walls block them too.

By Unit 48, the keep feels dangerous. Enemies patrol, the player takes damage, weapons allow fighting back, and the sound design heightens tension.

---

## Prerequisites from Phase 2

- Room data structure — extended with enemy spawn data per room
- Attribute collision — enemies use the same wall-check as the player
- Health system — enemies deal damage on contact
- HL indirect addressing — enemy tables accessed via pointer
- Bit flags — enemy state (alive, stunned, etc.)

---

## Unit Progression

| Unit | Title | New Z80 Concept | Game Addition |
|------|-------|----------------|---------------|
| 33 | Enemy Character | Second character drawn to screen, position tracked | Creature visible |
| 34 | Enemy Patrol (Horizontal) | Direction variable, toggle on wall hit | Back-and-forth movement |
| 35 | Enemy Patrol (Vertical) | Same logic, vertical axis | Up-and-down movement |
| 36 | Enemy-Wall Collision | Reuse attribute check for enemy movement | Enemies respect walls |
| 37 | Enemy Touches Player | Position comparison, damage on match | **Contact hurts** |
| 38 | Damage Sound | Beeper: low descending tone on hit | Audio feedback |
| 39 | Invincibility Frames | Frame counter after hit, player blinks | Brief immunity |
| 40 | Enemy Animation | `XOR` to alternate between two characters | Visual life |
| 41 | Multiple Enemies | Enemy data table, process with loop | Several per room |
| 42 | Different Speeds | Speed field per enemy, frame-skip movement | Fast and slow creatures |
| 43 | Border Flash on Hit | `OUT ($FE)` border colour change, timed reset | Dramatic feedback |
| 44 | Sword Item | New collectible, enables attack | Offensive option |
| 45 | Attack Mechanic | Press key facing enemy, check adjacent cell | Defeat creatures |
| 46 | Enemy Defeat | Remove from room, score bonus, defeat sound | Satisfying elimination |
| 47 | Enemies per Room | Room data includes enemy spawn list | Room-specific creatures |
| 48 | Integration + Balance | Enemy placement, speed tuning, combat fairness | Tense but fair |

---

## Key Teaching Moments

### Enemy Tables (Unit 41)

Multiple enemies require structured data. Each enemy has: X position, Y position, direction, speed, alive flag. Stored contiguously in memory, accessed via HL pointer. The loop pattern:

```z80
    ld hl,enemy_table
    ld b,ENEMY_COUNT
enemy_loop:
    ld a,(hl)          ; X position
    inc hl
    ; ... process enemy ...
    djnz enemy_loop
```

This is the Spectrum equivalent of the C64's indexed addressing pattern (`LDA table,X`). The Z80's HL pointer with `INC HL` is more flexible — no stride calculation needed, just advance through the data.

### XOR for Animation (Unit 40)

`XOR` flips bits. If the current character code is $41 ('A') and the alternate is $42 ('B'), `XOR $03` toggles between them (since $41 XOR $03 = $42 and $42 XOR $03 = $41). This is faster than a compare-and-branch: one instruction, no conditional logic. The same technique works for any toggle between two values whose XOR is a constant.

### Reusable Collision (Unit 36)

The attribute-check subroutine written for player movement in Phase 1 works unchanged for enemies. Pass the target position in registers, call the routine, check the result. Enemies respect the same walls the player does — no separate collision map, no special cases. The attribute system's elegance pays off again: one collision system for everything.

### The FRAMES System Variable (Unit 39)

Address $5C6A holds a 16-bit counter that increments at 50Hz (PAL). Reading it gives a free timer without managing your own counter. Invincibility frames: record FRAMES + duration on hit, compare against current FRAMES each loop. When current >= target, invincibility ends. No frame counting, no decrement-and-check.

---

## Z80 Concepts Introduced

1. `XOR` — exclusive OR for toggling values (Unit 40)
2. Multi-field table processing — HL pointer walks through records (Unit 41)
3. Frame-skip for speed variation — process every Nth frame based on speed field (Unit 42)
4. `FRAMES` system variable — hardware-maintained timer at $5C6A (Unit 39)
5. Position comparison — `CP` for checking if enemy and player share a cell (Unit 37)
6. Adjacent-cell check — calculate neighbour position for attack direction (Unit 45)

---

## Hardware

### New in Phase 3

| Resource | Purpose | Introduced |
|----------|---------|-----------|
| `$5C6A` (FRAMES) | 16-bit frame counter at 50Hz | Unit 39 |
| Border colour via `OUT ($FE)` | Damage feedback (border flash) | Unit 43 |

---

## Game State at Phase End

After Unit 48:

- **Multiple enemies per room** — 2–4 creatures with different patrol patterns
- **Enemy types** — horizontal patrollers, vertical patrollers, fast and slow
- **Combat** — sword item enables attacking adjacent enemies
- **Damage system** — contact costs health, invincibility frames prevent stunlock
- **Feedback** — border flash, damage sound, defeat sound, enemy animation
- **Per-room enemies** — room data defines which enemies spawn where
- **Score bonus** — defeating enemies awards points

The keep is alive and dangerous. Navigation requires timing and route planning around patrols.

---

## What Carries to Phase 4

- **Enemy tables** — expanded with more enemy types and behaviours
- **Room data structure** — Phase 4 compresses it for more rooms
- **Attack mechanic** — extended with range and special weapons
- **Timer patterns** — FRAMES-based timing used for room events

---

**Version:** 1.0
**Last Updated:** 2026-02-06
