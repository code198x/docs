# Phase 7: Command

**Game:** Starfield (C64 Game 1)
**Units:** 97–112
**Theme:** Boss fights that demand sprite multiplexing
**6510 Focus:** Raster-precise timing, sprite multiplexing algorithm, complex state machines
**Hardware:** VIC-II sprite register reuse via raster timing
**Status:** Planned

---

## Overview

A boss built from 4 sprites plus the player, bullets, and enemies exceeds 8 hardware slots. Sprite multiplexing — the technique that separates bedroom C64 games from professional ones — becomes necessary, not optional.

The VIC-II draws the screen top-to-bottom. Once a sprite has been fully drawn (the beam is past its last scanline), its registers can be repointed to display it again further down. A raster interrupt fires just below the first appearance; the handler repositions the sprite for its second use. This is how games like Armalyte display dozens of sprites with only 8 hardware slots.

The gameplay motivation is boss encounters: multi-phase fights with health bars, attack patterns, and dramatic audio. Sprite multiplexing makes bosses visually impressive. The raster interrupt skills from Phase 4 make multiplexing possible.

---

## Prerequisites from Phase 6

- Raster interrupt framework — multiplexing requires precisely timed raster handlers
- CIA timer interrupts — music continues during complex raster operations
- SID sound system — boss encounters need warning sirens, impact sounds, victory jingles
- Full sprite and character set mastery — bosses use multicolour sprites and custom graphics

---

## Unit Progression

| Unit | Title | New 6510 Concept | Game Addition |
|------|-------|-----------------|---------------|
| 97 | Mini-Boss Every 3 Waves | Conditional trigger on wave count | First taste of bosses |
| 98 | Mini-Boss: Tough Enemy | Hit counter, damage state tracking (3 hits to kill) | Tougher target |
| 99 | Mini-Boss Movement Pattern | Pattern table (left-right-dive sequence) | Distinct behaviour |
| 100 | Boss Every 5 Waves | Multi-sprite entity, coordinated positioning (4 sprites) | **Impressive size** |
| 101 | The 8-Sprite Problem | Analysis: boss(4) + player(1) + bullets = overflow | Understanding the limit |
| 102 | Sprite Multiplexing | Reuse sprite registers at different Y via raster IRQ | **The C64 trick** |
| 103 | Boss Sweep Pattern | Complex pattern table with timing data | Menacing movement |
| 104 | Boss Health Bar | Custom character gradual depletion display in HUD | Visible progress |
| 105 | Boss Hit Flash | Sprite colour register toggle on collision | Satisfying feedback |
| 106 | Boss Shoots | Multiple bullet spawn positions, angle offsets | Dangerous patterns |
| 107 | Boss Phase 2 | State machine transition at 50% health, pattern change | Escalation |
| 108 | Boss Death Sequence | Scripted multi-sprite chain explosion | Dramatic payoff |
| 109 | Boss Victory | Score bonus, SID celebration jingle | Triumph |
| 110 | Second Boss Type | Different shape and pattern, same data-driven system | Variety |
| 111 | Boss Warning | Border pulse + SID siren before boss appears | Anticipation |
| 112 | Integration + Boss Balance | Health/damage tuning, multiplexer stability | Memorable, fair fights |

---

## Key Teaching Moments

### The 8-Sprite Problem (Unit 101)

This is a design unit, not a coding unit. The learner counts: boss needs 4 sprites (it's large), player needs 1, player bullet needs 1, enemy bullets need at least 1. That's 7 — and there are still regular enemies. The hard limit is hit. The unit analyses the problem before solving it, so the learner understands *why* multiplexing exists, not just how it works.

### Sprite Multiplexing (Unit 102)

The most important advanced technique on the C64. The algorithm:

1. Sort all virtual sprites by Y position
2. For each hardware sprite slot, assign the highest on-screen virtual sprite
3. Set a raster interrupt below each sprite's last scanline
4. When the interrupt fires, reassign that slot to the next virtual sprite waiting to be displayed

The raster interrupt skills from Phase 4 make this possible. The key insight: the VIC-II doesn't care *when* you change a sprite's position and data — it only reads them when the beam reaches that scanline. Change them after the beam passes, and the old sprite stays on screen while the new one appears below.

### Multi-Phase Boss (Unit 107)

The boss state machine has nested states: normal → attack pattern A → attack pattern B → enraged (50% health) → death sequence. This is the most complex state machine in the game. The `CMP`/`BEQ` chain pattern from Unit 15's title screen scales to handle it, but the number of states and transitions forces careful organisation.

### Data-Driven Boss Design (Unit 110)

The second boss reuses the same boss system — movement patterns, health, attack tables — with different data. This validates the data-driven approach: changing the tables changes the boss entirely. No code duplication. The learner sees the payoff of separating data from logic, first introduced in Phase 2.

---

## 6510 Concepts Introduced

1. Sprite Y-sorting — comparison-based sort for multiplexer scheduling (Unit 102)
2. Raster-precise sprite register rewrite — change position/data between beam passes (Unit 102)
3. Chained raster interrupts for multiplexing — each handler schedules the next (Unit 102)
4. Complex state machines — nested states with multiple transition conditions (Unit 107)
5. Pattern tables with timing — position + duration data for choreographed movement (Unit 103)
6. Multi-sprite entity — coordinated positioning of 4 sprites as one object (Unit 100)

---

## Hardware Registers

### Used Differently in Phase 7

No new registers — Phase 7 uses existing VIC-II sprite registers in a fundamentally new way. The key advance is *reusing* `$D000`–`$D00F`, `$07F8`–`$07FF`, and `$D027`–`$D02E` multiple times per frame via raster timing.

| Technique | Registers | Timing |
|-----------|-----------|--------|
| Sprite position rewrite | `$D000`–`$D00F` | After beam passes sprite's last scanline |
| Sprite data swap | `$07F8`–`$07FF` | Same timing window |
| Sprite colour change | `$D027`–`$D02E` | Same timing window |

---

## Game State at Phase End

After Unit 112:

- **Mini-bosses** — appear every 3 waves, 3 hits to kill, distinct movement
- **Full bosses** — appear every 5 waves, multi-sprite (4 sprites), health bar, two phases
- **Sprite multiplexing** — more than 8 virtual sprites on screen simultaneously
- **Boss attack patterns** — spread shots, sweep movement, enraged mode at 50% health
- **Boss death sequence** — chain explosion across multiple sprites
- **Two boss types** — different shapes and patterns, data-driven system
- **Boss warning** — border pulse and SID siren build anticipation
- **Victory reward** — score bonus and jingle on boss defeat

Boss fights are the highlight of the game. Multi-phase encounters with real drama, powered by sprite multiplexing.

---

## What Carries to Phase 8

- **Sprite multiplexing** — the attract mode demo must handle the same sprite count
- **Complex state machines** — menu systems, two-player alternation, difficulty selection
- **Pattern data** — attract mode playback uses recorded or scripted input sequences
- **Full system mastery** — Phase 8 optimises and extends everything, adding no new hardware

---

**Version:** 1.0
**Last Updated:** 2026-02-06
