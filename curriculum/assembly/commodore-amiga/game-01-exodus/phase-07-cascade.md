# Phase 7: Cascade

**Game:** Exodus (Amiga Game 1)
**Units:** 97-112
**Theme:** Complex puzzles demanding ability combinations and precise timing
**68000 Focus:** Complex data structures, optimised Blitter scheduling, performance profiling
**Hardware:** Blitter performance optimisation, advanced Copper timing
**Status:** Planned

---

## Overview

Phase 7 is where puzzle design reaches its peak. Chain reactions: one creature's action enables another's path. Split flows: creatures diverge to reach multiple exits. Timed sequences: actions must happen at specific moments or the cascade fails.

New terrain modifiers -- conveyors, teleporters, one-way surfaces, rising hazards -- create routing puzzles that demand every ability in combination. Skill-limited levels give the player only 1-2 of each ability, forcing efficient solutions. The satisfaction is watching a complex plan execute: dig, redirect, build, pause, climb, float -- each action cascading into the next.

The engineering challenge is Blitter performance. Many creatures, each rendered as a cookie-cut BOB, plus terrain modifications, plus effects -- all need to complete within a frame. Real-world performance management becomes a teaching focus.

---

## Prerequisites from Phase 6

- MOD music engine with SFX priority
- Complete visual system with themed palettes
- All 7 abilities functional
- 8+ levels with terrain types

---

## Unit Progression

| Unit | Title | New 68000 Concept | Game Addition |
|------|-------|-------------------|---------------|
| 97 | Timed Puzzles | Frame-accurate action timing, sequence planning | Precision |
| 98 | Chain Reactions | One creature's action enables another's path | Combo puzzles |
| 99 | Split Flow | Creatures diverge to multiple exits | Routing complexity |
| 100 | Conveyor Terrain | Surface modifies creature movement speed/direction | Movement modifier |
| 101 | Teleport Zones | Creatures warp between positions | Spatial puzzles |
| 102 | One-Way Terrain | Pass only in one direction | Flow control |
| 103 | Rising Hazard (Lava/Acid) | Timer-driven terrain destruction from below | Time pressure |
| 104 | Wind Zones | Horizontal force on falling creatures | Physics modifier |
| 105 | Skill-Limited Puzzles | Only 1-2 of each ability, every use counts | Minimal solutions |
| 106 | Tutorial Sequences | Early levels teach one mechanic at a time | Learning curve |
| 107 | Expert Puzzles | Multi-step solutions requiring all abilities | Challenge |
| 108 | Blitter Performance | Optimised scheduling, queued operations | Stable framerate |
| 109 | Many Creatures (30+) | Efficient object pool, update loop optimisation | Busy screen |
| 110 | Creature Pathfinding | Smarter decisions in crowd situations | Less frustration |
| 111 | Level Design: 20 Levels | Full set with difficulty curve across themes | Complete content |
| 112 | Integration + Puzzle Balance | Solution testing, fairness, alternative paths | Satisfying difficulty |

---

## Key Teaching Moments

### Chain Reactions (Unit 98)

The defining puzzle pattern:

1. Assign "digger" to creature A -- digs through dirt, falls to lower passage
2. Assign "builder" to creature B -- builds bridge over the gap A's digging created
3. Creature C walks across B's bridge to reach the exit

Each ability enables the next. The puzzle is designing the sequence. The satisfaction is watching it cascade -- one action triggering the conditions for the next, a Rube Goldberg machine of creature abilities.

The code challenge: multiple creatures in different ability states, modifying terrain that other creatures interact with in real time. The data structures from Phase 1 (creature table, terrain bitmap, ability state) combine into emergent complexity.

### Blitter Performance (Unit 108)

Each frame requires:
- Background restore for each creature BOB (N Blitter ops)
- Terrain modifications (dig/build operations)
- Creature rendering via cookie-cut (N Blitter ops)
- Effect animations (explosion, spark operations)

With 30 creatures, that's 60+ Blitter operations per frame. Each operation takes time proportional to its size. Solutions:

```asm
; Priority queue: critical operations first
; 1. Restore backgrounds (prevents visual artifacts)
; 2. Terrain modifications (affects gameplay)
; 3. Render creatures (visual, can tolerate one frame delay)
; 4. Effects (cosmetic, lowest priority)

; Split large operations across frames
; A 32x32 explosion can be rendered as four 16x16 blits
; spread over 4 frames for smooth frame rate
```

The CPU can do small operations (single-pixel terrain checks) while the Blitter handles large rectangle copies. Interleaving CPU and Blitter work maximises throughput.

### Rising Hazard (Unit 103)

Lava rises from the bottom of the level. Each second, the lowest row of terrain is destroyed (Blitter clear) and the lava colour extends upward (Copper colour change at the new lava line). Creatures below the lava line die. The player must guide creatures to the exit before the lava reaches them. Time pressure creates urgency without requiring fast reflexes -- it's still a puzzle, just one with a deadline.

---

## 68000 Concepts Introduced

1. Operation priority queuing -- schedule Blitter ops by importance (Unit 108)
2. Frame-splitting -- distribute work across multiple frames (Unit 108)
3. CPU/Blitter interleaving -- small ops on CPU while Blitter runs (Unit 108)
4. Complex state machines -- creatures with multiple interacting states (Unit 98)
5. Timer-driven terrain destruction -- lava/acid as rising Blitter clear (Unit 103)
6. `DBRA` loop optimisation -- tight inner loops for creature updates (Unit 109)
7. Object pool management -- efficient allocation/deallocation for 30+ entities (Unit 109)

---

## Hardware

### New in Phase 7

Phase 7 introduces no new hardware registers. The focus is on optimising use of existing hardware -- particularly the Blitter -- under load.

| Technique | Purpose | Introduced |
|-----------|---------|------------|
| Blitter operation queuing | Prioritise critical operations | Unit 108 |
| Frame-split rendering | Spread large operations across frames | Unit 108 |
| CPU/Blitter parallelism | Use CPU for small ops while Blitter is busy | Unit 108 |

---

## Game State at Phase End

After Unit 112:

- **Chain reactions** -- multi-step ability cascades
- **Split flow** -- creatures to multiple exits
- **Conveyors** -- terrain that modifies movement
- **Teleporters** -- spatial warps between positions
- **One-way surfaces** -- directional flow control
- **Rising hazards** -- lava/acid with time pressure
- **Wind zones** -- physics modifiers for falling
- **Skill-limited puzzles** -- minimal ability counts force efficient solutions
- **Tutorial and expert levels** -- full difficulty curve
- **20 levels** -- complete set across all themes
- **30+ creatures** -- busy screen, stable performance
- **Optimised Blitter** -- queued operations, frame-split rendering

Complex puzzles with cascading solutions. Every level has a satisfying "aha" moment.

---

## What Carries to Phase 8

- **Complete game systems** -- Phase 8 polishes, doesn't add mechanics
- **Performance techniques** -- applied to attract mode and title effects
- **Level content** -- expanded to 30 levels
- **Difficulty curve** -- refined with additional levels filling gaps

---

**Version:** 1.0
**Last Updated:** 2026-02-06
