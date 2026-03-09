# Sinclair ZX Spectrum Curriculum

**Platform:** Sinclair ZX Spectrum
**Killer Feature:** Attribute colour system
**Assembly Games:** 4
**Total Units:** 1,408

---

## Overview

The ZX Spectrum curriculum teaches Z80 assembly programming through four complete games. The sequence begins with the attribute system — the Spectrum's defining characteristic that created its distinctive visual style — and progresses through software scrolling, isometric projection, and professional production techniques until learners can produce commercial-quality games.

The Spectrum had no hardware sprites, no smooth scrolling, and a single-bit beeper for sound. Every impressive effect was achieved through software and creativity. This curriculum embraces those constraints, teaching learners to make the hardware sing through ingenuity.

By the final game, learners will have skills matching professional Spectrum developers of the late 1980s — equivalent to teams at Ultimate, Ocean, or Codemasters.

---

## Assembly Track

### Structure

| Game | Units | Phases | Units/Phase | Role |
|------|-------|--------|-------------|------|
| 1 | 128 | 8 | 16 | Accessible entry — attributes as game mechanic |
| 2 | 256 | 8 | 32 | Signature technique — software pixel scrolling |
| 3 | 512 | 16 | 32 | Ambitious — isometric adventure with 128K features |
| 4 | 512 | 16 | 32 | Capstone — commercial-quality dual-mode release |
| **Total** | **1,408** | | | |

---

### Game 1: Single-Screen Platformer

**Units:** 128 (8 phases)
**Genre:** Single-screen platformer
**Inspired by:** Manic Miner, Jet Set Willy
**Working title:** TBD

**Concept:** Jump between platforms, collect items, avoid hazards, reach the exit. Each level fits on a single screen. The attribute system is the game — INK defines walls, PAPER defines floors, BRIGHT marks collectibles. The learner sees pixels on screen in unit 1, moves a character in unit 2, and has a playable level by unit 4.

**Skills taught:**
- Z80 fundamentals (registers, addressing modes, flags, stack)
- Screen memory layout ($4000-$57FF) and its non-linear row organisation
- Attribute memory ($5800-$5AFF) — INK, PAPER, BRIGHT, FLASH bits
- Keyboard input via port reads and ROM routines
- Character-cell movement (8-pixel grid)
- Gravity and jump physics (velocity, acceleration, variable jump height)
- Platform collision detection via attribute reading
- Player animation (walk cycle, jump, fall, death)
- Patrolling enemies (path following, speed variation)
- Crumbling platforms, conveyor belts, moving platforms
- Air supply or timer mechanic (time pressure)
- Level data structures (tile maps, compact encoding)
- Beeper sound effects (pitch and duration variation)
- Multi-level progression with increasing difficulty
- Score display and high score table
- Title screen and game-over sequence

**Why first:** Manic Miner is the Spectrum. A single-screen platformer makes the attribute system the core game mechanic from unit 1. Walls are INK, floors are PAPER, items are BRIGHT — the Spectrum's defining feature becomes the game design tool. The game looks like a real Spectrum release because it IS one: the same techniques, the same constraints, the same visual style that defined the platform.

---

### Game 2: Horizontal Scrolling Shoot 'Em Up

**Units:** 256 (8 phases × 32 units)
**Genre:** Horizontal scrolling shmup
**Inspired by:** R-Type, Zynaps, Nemesis
**Working title:** TBD

**Concept:** Pilot a ship through alien landscapes, fight waves of enemies, defeat massive bosses. The Spectrum has no hardware scroll registers, so every pixel of scrolling is achieved through software — shift operations across screen memory, timed to avoid visible tearing. Building this game is the Spectrum's crowning technical achievement.

**Skills taught:**
- Software pixel scrolling (the hard technique — no hardware support)
- Contended memory timing (ULA steals cycles during screen refresh)
- Pixel-level shift operations across screen bytes
- Double buffering approaches for flicker-free display
- Background tile map management during scroll
- Pixel-precise collision detection
- Player ship with smooth multi-directional movement
- Weapon systems (primary fire, power-ups, charge shots)
- Enemy wave patterns and formation AI
- Large multi-character boss sprites
- Boss behaviour patterns (movement phases, weak points, attacks)
- Parallax effects via software (background layers at different speeds)
- Screen layout optimisation (attribute-friendly colour zones)
- Beeper sound engine (music during gameplay)
- Level progression with distinct visual themes
- Lives, continues, score, and high score persistence

**Why here:** Software pixel scrolling is the hardest thing to do well on the Spectrum. There are no scroll registers — every frame, the code shifts pixels across memory while the ULA fights for bus access. Games like R-Type on the Spectrum were technical miracles. This game teaches the technique through necessity: the gameplay demands scrolling, so the learner builds it. By the end, they understand contended memory timing at a level that makes every other Spectrum technique feel straightforward.

---

### Game 3: Isometric Adventure

**Units:** 512 (16 phases × 32 units)
**Genre:** Isometric adventure
**Inspired by:** Knight Lore, Head Over Heels, Batman
**Working title:** TBD

**Concept:** Explore a castle or fortress rendered in isometric 3D. Push blocks onto pressure plates, avoid enemies, collect items, solve environmental puzzles across 100+ rooms. The Spectrum invented this genre — Ultimate's Knight Lore was the first isometric adventure, and it changed what people believed the hardware could do.

This is the first game to use 128K features: AY-3-8912 music, bank switching for a larger world, and dual-page rendering.

**Skills taught:**
- Isometric projection mathematics (world-to-screen coordinate conversion)
- Depth sorting (painter's algorithm — draw back-to-front)
- Isometric tile and object rendering
- Z-height collision detection (walking on raised platforms, falling)
- Room-based world structure with transitions
- Push-block puzzles (Sokoban-style within isometric space)
- Pressure plates, doors, gates, keys
- Multiple enemy types with distinct behaviours
- Player abilities (jump, carry, push, use items)
- Inventory system
- Transformation or time mechanic (Knight Lore's werewolf, Head Over Heels' character switching)
- 128K detection and adaptation
- AY-3-8912 music (three channels, envelope, noise)
- Bank switching for room data (fitting 100+ rooms)
- Dual-screen rendering (draw off-screen, flip)
- 5+ themed zones with distinct visual palettes (within attribute constraints)
- Save or password system for progress
- Title screen with AY music, in-game ambient sound

**Why here:** The isometric adventure is the Spectrum's unique gift to gaming. Knight Lore in 1984 made people believe the Spectrum could do 3D. This game teaches the mathematics behind the illusion — projection, depth sorting, Z-collision — while building a world large enough to justify 128K bank switching. It's where the curriculum's techniques come together: attribute mastery from Game 1, display timing from Game 2, and now spatial reasoning in isometric space.

---

### Game 4: Capstone

**Units:** 512 (16 phases × 32 units)
**Genre:** Scrolling action-adventure (distinct from Games 1-3)
**Inspired by:** Late-era Ocean, Codemasters, or Rare releases
**Working title:** TBD

**Concept:** A scrolling action-adventure that combines platforming, combat, and exploration across multiple zones. This is not a repetition of Games 1-3 — it is a new genre that requires all previous skills (attribute awareness, smooth scrolling, large world management) plus the production techniques that separated bedroom coders from commercial studios.

The capstone's new material is distribution and production: turbo tape loading, +3 disk support, 128K/48K dual-mode code paths, and loading screens. The finished game should look like it could sit on a shop shelf next to Midnight Resistance or Robocop.

**Skills taught:**
- All techniques from Games 1-3 at mastery level
- Scrolling world with varied terrain and enemy placement
- Melee and ranged combat systems
- Multi-zone world design (distinct themes, palettes, enemy sets)
- 128K/48K dual-mode detection and code paths
- AY music on 128K with beeper fallback on 48K
- Turbo tape loader (custom loading routine, faster than ROM)
- +3 disk version (accessing the uPD765 FDC)
- Loading screen (displayed during tape/disk load)
- Professional title sequence
- Multiple difficulty levels
- Password or save system
- End-game sequence and credits
- Testing across models (48K, 128K, +2, +2A, +3)

**Why last:** The capstone proves the learner can ship a product. The game itself combines scrolling action with exploration — genres the learner has already mastered individually. The new challenge is production: making the game load from tape and disk, adapting to different Spectrum models, and presenting a professional package. Every game in the curriculum runs on real hardware; the capstone makes that fact visible through custom loaders and multi-model support.

---

## BASIC Gateway

The Sinclair BASIC curriculum is maintained separately. See `/docs/curriculum/basic/sinclair-zx-spectrum/sinclair-zx-spectrum-basic-curriculum.md`.

---

## Changelog

- **v4.0 (2026-03-09):** Major restructure. Reduced from 16 to 4 assembly games. No-repetition rule across primary platforms. Every game inspired by a real commercial release. BASIC gateway expanded from 8 to 4 focused games. Previous 16-game curriculum preserved in game outline files for reference.
- **v3.20 (2026-02-06):** Replaced Game 1 (Skyfire) with Shadowkeep.
- **v3.0 (2026-01-18):** Initial 16-game curriculum.
