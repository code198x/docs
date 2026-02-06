# Phase 8: Cartridge

**Game:** Dash (NES Game 1)
**Units:** 113-128
**Theme:** Commercial release quality -- the complete game
**6502 Focus:** Code optimisation, memory management, NTSC/PAL detection, iNES packaging
**Hardware:** Full NES hardware mastery, iNES cartridge format
**Status:** Planned

---

## Overview

Phase 8 adds everything a commercial 1987 NES game would ship with: high scores, difficulty selection, passwords, attract mode, and a credits screen. No new gameplay mechanics -- instead, every system from Phases 1-7 is polished, balanced, and integrated into a release-quality product.

The game's completion is measured in content: 8+ designed levels with a difficulty curve, multiple themes, boss encounters, and a satisfying ending. The journey from a single sprite on screen (Unit 1) to a complete, polished platformer (Unit 128) mirrors the learner's journey from zero 6502 knowledge to genuine NES programming competence.

---

## Prerequisites from Phase 7

- Complete game with all mechanics -- Phase 8 polishes, doesn't add
- Music engine with SFX priority
- Boss fights and designed encounters
- Scrolling, metasprites, metatiles all solid

---

## Unit Progression

| Unit | Title | New 6502 Concept | Game Addition |
|------|-------|------------------|---------------|
| 113 | High Score Table | Multi-byte comparison, sorted insertion | Top 5 scores |
| 114 | Name Entry | On-screen keyboard, cursor navigation | 3-letter initials |
| 115 | High Scores on Title | Display integration | Bragging rights |
| 116 | Difficulty Select | Menu system, cursor highlight | Easy / Normal / Hard |
| 117 | Difficulty Affects Gameplay | Parameter tables: enemy speed, damage, health | Real difference |
| 118 | Extra Life at Threshold | Score check, 1-up jingle | Skill reward |
| 119 | Continue System | Level restart with limited continues | Forgiveness |
| 120 | Password System | Level progress encoded as 4-character code | Persistence |
| 121 | Attract Mode | Recorded input playback, game plays itself | Demo mode |
| 122 | Demo on Title Timeout | Timer-triggered transition | Arcade feel |
| 123 | NTSC/PAL Detection | Frame timing comparison, speed adjustment | Platform correct |
| 124 | Credits Screen | Scrolling nametable text with palette effects | Attribution |
| 125 | 8+ Designed Levels | Full set with difficulty curve and themes | Complete content |
| 126 | Final Testing | Edge cases, balance, difficulty curve | Release quality |
| 127 | Memory Audit | PRG-ROM and CHR-ROM usage map, fit check | Fits in NROM |
| 128 | **Complete Game** | iNES packaging, final build, documentation | **Ship it** |

---

## Key Teaching Moments

### Password System (Unit 120)

The NES has no battery RAM on NROM cartridges. Passwords encode level progress into a short string. A simple scheme: XOR the level number with a key, convert to 4 alphanumeric characters. On the password screen, enter the characters, decode, validate (reject invalid codes), and jump to the right level. Cheating via guessing is possible -- and acceptable for a 1987 game.

### Attract Mode (Unit 121)

Attract mode records controller inputs during a sample playthrough: each frame's button state stored in a byte array. During playback, the array replaces live controller input -- the game "plays itself" using its own engine. The recording is compact (one byte per frame, ~900 bytes for 15 seconds at 60fps). This is how arcade games and many console titles create demo modes.

### NTSC/PAL Detection (Unit 123)

NTSC NES runs at 60Hz; PAL at 50Hz. A timing loop counts CPU cycles during a known VBlank period. If the count differs from NTSC expectations, the system is PAL. The game adjusts: gravity and velocity constants scale by 6/5 to compensate for the slower frame rate. Music tempo adjusts ticks per row. Without this, PAL players get a sluggish game.

---

## 6502 Concepts Introduced

1. Multi-byte comparison -- cascading `CMP`/`SBC` for score ranking (Unit 113)
2. Sorted insertion -- shift array entries to maintain order (Unit 113)
3. Input recording/playback -- byte array of controller state per frame (Unit 121)
4. Timing-based detection -- cycle counting for NTSC/PAL (Unit 123)
5. XOR encoding -- simple password generation/validation (Unit 120)
6. Memory map audit -- systematic allocation review (Unit 127)

---

## Hardware

### New in Phase 8

| Resource | Purpose | Introduced |
|----------|---------|------------|
| Full iNES header options | Mapper, mirroring, battery RAM flags | Unit 128 |

Phase 8 is primarily about game logic and polish. No new hardware features -- full mastery of existing hardware.

---

## Game State at Phase End

After Unit 128 -- the complete game:

- **High scores** -- top 5 with initials, sorted, displayed on title
- **Difficulty** -- Easy/Normal/Hard with menu selection
- **Password system** -- 4-character codes for level progress
- **Attract mode** -- auto-play demo after title timeout
- **Continue system** -- limited continues from current level
- **Extra life** -- bonus life at score threshold
- **Credits screen** -- scrolling text with effects
- **8+ levels** -- full difficulty curve across themed worlds
- **Boss encounters** -- multi-phase fights at level ends
- **Full audio** -- 4-channel music, crafted SFX, jingles
- **Full visuals** -- metasprites, themed CHR art, parallax, animation
- **NTSC/PAL** -- detected and compensated automatically
- **Scrolling** -- seamless hardware scrolling with fixed HUD

A game you could put on a cartridge and sell in 1987.

---

## Quality Comparison Across All Phases

| Aspect | Phase 1 | Phase 4 | Phase 8 |
|--------|---------|---------|---------|
| Graphics | Single sprite, basic tiles | + themed tiles, animation frames | Metasprites, parallax, CHR art |
| World | 1 screen | + hardware scrolling, long levels | 8+ levels, bosses, varied themes |
| Player | Run + jump | + variable jump, coyote time | + combat, projectiles, animation |
| Enemies | None | + hazards, moving platforms | Patrol, flying, shooting, bosses |
| Audio | One SFX | + effect library | Full 4-channel music, priority SFX |
| Features | Move + collect + die | + checkpoints, health, ladders | High scores, passwords, attract |
| 6502 Skill | LDA, STA, branches | + 16-bit, indexed, VBlank | Full toolkit, music engine, pools |

---

## What This Game Teaches

By completing Dash, learners are ready for:

- **Crate Escape (Game 2)** -- jump physics transfer directly. Single-screen focus deepens polish. Metatile system reused
- **Fracture Point (Game 3)** -- VBlank discipline enables dynamic nametable updates. Ball physics builds on velocity system
- **Crypt Crawler (Game 5)** -- metatile system becomes room renderer. Object pools manage monsters
- **Pixel Plains (Game 8)** -- hardware scrolling becomes full-world scrolling. Seam loading enables open worlds
- **Every future NES game** -- the NMI framework, VBlank discipline, PPU update patterns, and APU music engine from Dash are reused throughout

Dash isn't just Game 1. It's the foundation for the entire NES curriculum.

---

**Version:** 1.0
**Last Updated:** 2026-02-06
