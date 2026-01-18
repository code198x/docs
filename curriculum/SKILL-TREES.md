# Curriculum Skill Trees

**Purpose:** Map skill dependencies to understand optimal game ordering.

---

## How to Read These Trees

```
[Skill A] ──→ [Skill B]   means A is prerequisite for B
[Skill A] ──┬→ [Skill B]  means A unlocks both B and C
            └→ [Skill C]
```

Games are shown in **bold** where they primarily teach that skill.

---

## Commodore 64 Skill Tree

```
                                    ┌─────────────────────────────────────────┐
                                    │           FOUNDATION                     │
                                    │  (Memory model, registers, addressing)   │
                                    └────────────────┬────────────────────────┘
                                                     │
                        ┌────────────────────────────┼────────────────────────────┐
                        │                            │                            │
                        ▼                            ▼                            ▼
              ┌─────────────────┐          ┌─────────────────┐          ┌─────────────────┐
              │   VIC-II        │          │   CIA I/O       │          │   SID AUDIO     │
              │   (Display)     │          │   (Input)       │          │   (Sound)       │
              └────────┬────────┘          └────────┬────────┘          └────────┬────────┘
                       │                            │                            │
         ┌─────────────┼─────────────┐              │              ┌─────────────┼─────────────┐
         │             │             │              │              │             │             │
         ▼             ▼             ▼              ▼              ▼             ▼             ▼
    ┌─────────┐  ┌─────────┐  ┌─────────┐   ┌─────────────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐
    │ Screen  │  │ Sprites │  │ Chars   │   │  Joystick   │  │  Basic  │  │  ADSR   │  │ Filters │
    │ Memory  │  │ (hw)    │  │ (tiles) │   │  Reading    │  │  SFX    │  │ Envelopes│  │         │
    └────┬────┘  └────┬────┘  └────┬────┘   └──────┬──────┘  └────┬────┘  └────┬────┘  └────┬────┘
         │            │            │               │              │            │            │
         │            │            │               │              │            │            │
         │      ┌─────┴─────┐     │               │              │      ┌─────┴─────┐      │
         │      │           │     │               │              │      │           │      │
         ▼      ▼           ▼     ▼               │              ▼      ▼           ▼      ▼
    ┌─────────────┐   ┌───────────────┐           │         ┌─────────────────────────────────┐
    │  Sprite     │   │   Multicolour │           │         │       MUSIC COMPOSITION         │
    │  Collision  │   │   Sprites     │           │         │   (Multi-voice, sequencing)     │
    └──────┬──────┘   └───────────────┘           │         └────────────────┬────────────────┘
           │                                      │                          │
           │                                      │                          │
    ═══════╪══════════════════════════════════════╪══════════════════════════╪═══════════════════
           │          ** GAME 1: STARFIELD **     │                          │
           │          (Sprites, joystick, SFX,    │                          │
           │           collision, waves)          │                          │
    ═══════╪══════════════════════════════════════╪══════════════════════════╪═══════════════════
           │                                      │                          │
           ▼                                      ▼                          │
    ┌─────────────┐                        ┌─────────────┐                   │
    │  Gravity    │                        │  Keyboard   │                   │
    │  Physics    │                        │  Matrix     │                   │
    └──────┬──────┘                        └──────┬──────┘                   │
           │                                      │                          │
    ═══════╪══════════════════════════════════════╪══════════════════════════╪═══════════════════
           │    ** GAME 2: PLATFORMER **          │                          │
           │    (Gravity, jumping, tile collision)│                          │
    ═══════╪══════════════════════════════════════╪══════════════════════════╪═══════════════════
           │                                      │                          │
           │                               ┌──────┴──────┐                   │
           │                               │             │                   │
           ▼                               ▼             ▼                   ▼
    ┌─────────────┐                 ┌─────────────┐ ┌─────────────┐   ┌─────────────┐
    │  Tile-based │                 │  AI Path-   │ │  Timing     │   │  Rhythm     │
    │  Collision  │                 │  finding    │ │  Precision  │   │  Gameplay   │
    └──────┬──────┘                 └─────────────┘ └──────┬──────┘   └──────┬──────┘
           │                                               │                 │
    ═══════╪═══════════════════════════════════════════════╪═════════════════╪═══════════════════
           │    ** GAME 3: MAZE **                         │                 │
           │    (Tiles, pathfinding, AI)                   │                 │
    ═══════╪═══════════════════════════════════════════════╪═════════════════╪═══════════════════
           │                                               │                 │
           │                                               └────────┬────────┘
           │                                                        │
           │                                               ═════════╪═════════════════════════════
           │                                               ** GAME 6: SID SYMPHONY **
           │                                               (Deep SID, rhythm, timing)
           │                                               ═══════════════════════════════════════
           │
           ▼
    ┌─────────────────┐
    │   SCROLLING     │
    │   (Hardware)    │
    └────────┬────────┘
             │
    ┌────────┼────────┐
    │        │        │
    ▼        ▼        ▼
┌───────┐ ┌───────┐ ┌───────┐
│ Horiz │ │ Vert  │ │Colour │
│Scroll │ │Scroll │ │ RAM   │
└───┬───┘ └───────┘ └───────┘
    │
════╪════════════════════════════════════════════════════════════════════════════════════════════
    │    ** GAME 7: SCROLL RUNNER **
    │    (Horizontal scrolling fundamentals)
════╪════════════════════════════════════════════════════════════════════════════════════════════
    │
    ▼
┌─────────────────┐
│  RASTER TIMING  │
│  (Interrupts)   │
└────────┬────────┘
         │
    ┌────┴────┐
    │         │
    ▼         ▼
┌───────┐ ┌───────────┐
│Colour │ │  Sprite   │
│Splits │ │  Multiplex│
└───────┘ └───────────┘
         │
═════════╪═══════════════════════════════════════════════════════════════════════════════════════
         │    ** GAME 9: SPRITE STORM **
         │    (Multiplexing, raster interrupts)
═════════╪═══════════════════════════════════════════════════════════════════════════════════════
```

### C64 Key Insights

1. **SID Symphony requires keyboard + timing precision** - these aren't introduced until after basic games
2. **Scrolling is independent of audio** - can be learned in parallel
3. **Multiplexing requires raster timing** - must come after scrolling introduces raster concepts
4. **Platforming unlocks tile collision** - needed for maze games

**Recommended C64 order based on tree:**
1. Starfield (shooter) - foundation
2. Platformer - gravity, tiles
3. Maze - pathfinding, AI
4. Breakout - physics refinement
5. Invader Wave - formations
6. SID Symphony - deep audio (keyboard + timing now available)
7. Scroll Runner - scrolling
8. Night Raid - scrolling + shooting
9. Sprite Storm - multiplexing
10. Raster Rider - advanced raster

---

## ZX Spectrum Skill Tree

```
                                    ┌─────────────────────────────────────────┐
                                    │           FOUNDATION                     │
                                    │  (Z80, memory model, ROM routines)       │
                                    └────────────────┬────────────────────────┘
                                                     │
                        ┌────────────────────────────┼────────────────────────────┐
                        │                            │                            │
                        ▼                            ▼                            ▼
              ┌─────────────────┐          ┌─────────────────┐          ┌─────────────────┐
              │  SCREEN MEMORY  │          │   KEYBOARD      │          │   BEEPER        │
              │  ($4000-$57FF)  │          │   (ROM/direct)  │          │   (Port $FE)    │
              └────────┬────────┘          └────────┬────────┘          └────────┬────────┘
                       │                            │                            │
         ┌─────────────┼─────────────┐              │                            │
         │             │             │              │                            │
         ▼             ▼             ▼              │                            ▼
    ┌─────────┐  ┌─────────┐  ┌───────────┐        │                    ┌─────────────┐
    │ Pixel   │  │Attribute│  │  Custom   │        │                    │  Pitch &    │
    │ Drawing │  │ System  │  │  Fonts    │        │                    │  Duration   │
    └────┬────┘  └────┬────┘  └─────┬─────┘        │                    └──────┬──────┘
         │            │             │              │                           │
         │            │             │              │                           │
    ═════╪════════════╪═════════════╪══════════════╪═══════════════════════════╪═══════════════
         │   ** GAME 1: SKYFIRE **  │              │                           │
         │   (Screen, attributes,   │              │                           │
         │    keyboard, beeper)     │              │                           │
    ═════╪════════════╪═════════════╪══════════════╪═══════════════════════════╪═══════════════
         │            │             │              │                           │
         ▼            │             │              │                           │
    ┌─────────┐       │             │              │                           │
    │Sub-pixel│       │             │              │                           │
    │Movement │       │             │              │                           │
    └────┬────┘       │             │              │                           │
         │            │             │              │                           │
    ┌────┴────────────┤             │              │                           │
    │                 │             │              │                           │
    ▼                 ▼             │              │                           │
┌─────────┐    ┌───────────┐        │              │                           │
│  Ball   │    │  Colour   │        │              │                           │
│ Physics │    │  Clash    │        │              │                           │
│         │    │  Mgmt     │        │              │                           │
└────┬────┘    └───────────┘        │              │                           │
     │                              │              │                           │
═════╪══════════════════════════════╪══════════════╪═══════════════════════════╪═══════════════
     │    ** GAME 2: SHATTER **     │              │                           │
     │    (Sub-pixel, physics)      │              │                           │
═════╪══════════════════════════════╪══════════════╪═══════════════════════════╪═══════════════
     │                              │              │                           │
     ▼                              │              │                           │
┌─────────────┐                     │              │                           │
│  Gravity    │                     │              │                           │
│  Physics    │                     │              │                           │
└──────┬──────┘                     │              │                           │
       │                            │              │                           │
═══════╪════════════════════════════╪══════════════╪═══════════════════════════╪═══════════════
       │    ** GAME 3: CAVERN **    │              │                           │
       │    (Platforming)           │              │                           │
═══════╪════════════════════════════╪══════════════╪═══════════════════════════╪═══════════════
       │                            │              │                           │
       │                            ▼              ▼                           │
       │                     ┌─────────────────────────┐                       │
       │                     │    STRATEGIC AI         │                       │
       │                     │    (Turn-based, decisions)                      │
       │                     └────────────┬────────────┘                       │
       │                                  │                                    │
       │                     ═════════════╪════════════════════════════════════╪═══════════════
       │                     ** GAME 5: INK WAR **                             │
       │                     (Strategy, AI, attribute mastery)                 │
       │                     ══════════════════════════════════════════════════╪═══════════════
       │                                                                       │
       ▼                                                                       │
┌─────────────────┐                                                            │
│   SCROLLING     │                                                            │
│   (Software)    │                                                            │
└────────┬────────┘                                                            │
         │                                                                     │
═════════╪═════════════════════════════════════════════════════════════════════╪═══════════════
         │    ** GAMES 7-9: SCROLLING GAMES **                                 │
═════════╪═════════════════════════════════════════════════════════════════════════════════════
```

### ZX Spectrum Key Insights

1. **Ink War needs strategic AI** - which benefits from having more game-building experience first
2. **Sub-pixel movement unlocks both ball physics AND platforming**
3. **Colour clash management is its own skill** - learned through experience
4. **Scrolling is a major milestone** - everything before is fixed-screen

**Recommended ZX order based on tree:**
1. Skyfire (shooter) - foundation
2. Shatter (breakout) - sub-pixel, physics
3. Cavern (platformer) - gravity, builds on physics
4. Byte Biter (snake) - data structures
5. Ink War (strategy) - AI, now learner has experience
6. Block Drop (tetris) - rotation, grids
7+ Scrolling games

---

## NES Skill Tree

```
                                    ┌─────────────────────────────────────────┐
                                    │           FOUNDATION                     │
                                    │  (6502, NES memory map, PPU basics)      │
                                    └────────────────┬────────────────────────┘
                                                     │
              ┌──────────────────────────────────────┼──────────────────────────────────────┐
              │                                      │                                      │
              ▼                                      ▼                                      ▼
    ┌─────────────────┐                    ┌─────────────────┐                    ┌─────────────────┐
    │      PPU        │                    │   CONTROLLER    │                    │      APU        │
    │  (Graphics)     │                    │   (Input)       │                    │   (Audio)       │
    └────────┬────────┘                    └────────┬────────┘                    └────────┬────────┘
             │                                      │                                      │
    ┌────────┼────────┐                             │                             ┌────────┼────────┐
    │        │        │                             │                             │        │        │
    ▼        ▼        ▼                             │                             ▼        ▼        ▼
┌───────┐┌───────┐┌───────┐                         │                         ┌───────┐┌───────┐┌───────┐
│Pattern││Name-  ││OAM/   │                         │                         │ Pulse ││Triangle││ Noise │
│Tables ││tables ││Sprites│                         │                         │ Ch.   ││ Ch.    ││ Ch.   │
└───┬───┘└───┬───┘└───┬───┘                         │                         └───────┘└────────┘└───────┘
    │        │        │                             │
    │        │        ├─────────────────────────────┤
    │        │        │                             │
    │        │        ▼                             │
    │        │   ┌─────────┐                        │
    │        │   │ Sprite  │                        │
    │        │   │ Limits  │                        │
    │        │   │ (8/line)│                        │
    │        │   └────┬────┘                        │
    │        │        │                             │
════╪════════╪════════╪═════════════════════════════╪════════════════════════════════════════════════════
    │   ** GAME 1: STELLAR BARRAGE **               │
    │   (PPU, sprites, collision, APU basics, limits)
════╪════════╪════════╪═════════════════════════════╪════════════════════════════════════════════════════
    │        │        │                             │
    │        ▼        │                             │
    │   ┌─────────┐   │                             │
    │   │  Tile   │   │                             │
    │   │Collision│   │                             │
    │   └────┬────┘   │                             │
    │        │        │                             │
    │   ┌────┴────┐   │                             │
    │   │         │   │                             │
    │   ▼         ▼   │                             │
    │┌───────┐┌───────┐                             │
    ││Gravity││ Maze  │                             │
    ││Physics││ Logic │                             │
    │└───┬───┘└───┬───┘                             │
    │    │        │                                 │
════╪════╪════════╪═════════════════════════════════════════════════════════════════════════════════════
    │    │  ** GAME 2: CRATE ESCAPE **
    │    │  (Platforming, tile collision)
════╪════╪════════════════════════════════════════════════════════════════════════════════════════════════
    │    │
    │    ▼
    │ ┌─────────────────┐
    │ │   SCROLLING     │
    │ │   (Hardware)    │
    │ └────────┬────────┘
    │          │
    │     ┌────┴────┐
    │     │         │
    │     ▼         ▼
    │ ┌───────┐ ┌───────┐
    │ │ Horiz │ │ Vert  │
    │ │Scroll │ │Scroll │
    │ └───┬───┘ └───────┘
    │     │
════╪═════╪════════════════════════════════════════════════════════════════════════════════════════════════
    │     │  ** GAME 8: PIXEL PLAINS **
    │     │  (Scrolling platformer)
════╪═════╪════════════════════════════════════════════════════════════════════════════════════════════════
    │     │
    │     ▼
    │ ┌─────────────────┐
    │ │    MAPPERS      │
    │ │  (Bank switching)│
    │ └────────┬────────┘
    │          │
    │     ┌────┴────┐
    │     │         │
    │     ▼         ▼
    │ ┌───────┐ ┌───────┐
    │ │ MMC1  │ │ MMC3  │
    │ └───────┘ └───────┘
```

### NES Key Insights

1. **Neon Nexus is largely redundant** - Stellar Barrage teaches the same PPU skills
2. **Tile collision is prerequisite for both platforming AND maze games**
3. **Scrolling requires solid tile collision understanding**
4. **Mappers are late-game** - need everything else first

**Recommended NES order based on tree:**
1. Stellar Barrage (shooter) - PPU foundation, 128 units
2. Crate Escape (platformer) - tile collision, gravity
3. Fracture Point (breakout) - physics refinement
4. Pellet Panic (maze) - tile-based maze, AI
5. Crypt Crawler (exploration) - multi-room, state
6. Fangs (snake) - data structures
7. Gridlock (tetris) - rotation logic
8. Pixel Plains (scroll platformer) - hardware scrolling
9. Ion Trail (scroll shooter) - scrolling + combat
10. **NEW: Something that builds toward mappers**

**Neon Nexus verdict:** Remove or make optional "practice project"

---

## Amiga Skill Tree

```
                                    ┌─────────────────────────────────────────┐
                                    │           FOUNDATION                     │
                                    │  (68000, Amiga memory, chip/fast RAM)    │
                                    └────────────────┬────────────────────────┘
                                                     │
         ┌───────────────────────────────────────────┼───────────────────────────────────────────┐
         │                                           │                                           │
         ▼                                           ▼                                           ▼
┌─────────────────┐                         ┌─────────────────┐                         ┌─────────────────┐
│     COPPER      │                         │     BLITTER     │                         │     PAULA       │
│  (Display list) │                         │  (Graphics acc) │                         │   (Audio)       │
└────────┬────────┘                         └────────┬────────┘                         └────────┬────────┘
         │                                           │                                           │
    ┌────┼────┐                              ┌───────┼───────┐                           ┌───────┼───────┐
    │    │    │                              │       │       │                           │       │       │
    ▼    ▼    ▼                              ▼       ▼       ▼                           ▼       ▼       ▼
┌─────┐┌─────┐┌─────┐                    ┌─────┐ ┌─────┐ ┌─────┐                     ┌─────┐ ┌─────┐ ┌─────┐
│Basic││Color││Wait │                    │Copy │ │Fill │ │Line │                     │Sample│ │Vol/ │ │MOD  │
│List ││Cycle││Instr│                    │Mode │ │Mode │ │Draw │                     │Play  ││Period││Player│
└──┬──┘└─────┘└─────┘                    └──┬──┘ └─────┘ └─────┘                     └──┬──┘ └─────┘ └──┬──┘
   │                                        │                                           │              │
   │                                        ├───────────────┐                           │              │
   │                                        │               │                           │              │
   │                                        ▼               ▼                           │              │
   │                                   ┌─────────┐    ┌───────────┐                     │              │
   │                                   │Hardware │    │   BOBs    │                     │              │
   │                                   │Sprites  │    │(Blitter   │                     │              │
   │                                   │         │    │ Objects)  │                     │              │
   │                                   └────┬────┘    └─────┬─────┘                     │              │
   │                                        │               │                           │              │
   │                                        └───────┬───────┘                           │              │
   │                                                │                                   │              │
═══╪════════════════════════════════════════════════╪═══════════════════════════════════╪══════════════╪════
   │                  ** GAME 1: BLAST ZONE **      │                                   │              │
   │                  (Copper basics, sprites, BOBs,│samples, bootable ADF)             │              │
═══╪════════════════════════════════════════════════╪═══════════════════════════════════╪══════════════╪════
   │                                                │                                   │              │
   │                                                │                                   │              │
   │                                                ▼                                   │              │
   │                                         ┌─────────────┐                            │              │
   │                                         │   Timing    │                            │              │
   │                                         │   Gameplay  │                            │              │
   │                                         └──────┬──────┘                            │              │
   │                                                │                                   │              │
═══╪════════════════════════════════════════════════╪═══════════════════════════════════════════════════════
   │                  ** GAME 2: SIGNAL **          │
   │                  (Lane timing, different gameplay model)
═══╪════════════════════════════════════════════════════════════════════════════════════════════════════════
   │
   ▼
┌─────────────────┐
│ Advanced Copper │
│ (Mid-screen fx) │
└────────┬────────┘
         │
    ┌────┴────┐
    │         │
    ▼         ▼
┌───────┐ ┌───────┐
│Gradient│ │Palette│
│ Bars  │ │ Swap  │
└───────┘ └───────┘
         │
         ▼
┌─────────────────┐
│   SCROLLING     │
│ (Hardware/soft) │
└────────┬────────┘
         │
    ┌────┴────┐
    │         │
    ▼         ▼
┌───────┐ ┌───────────┐
│ Horiz │ │   Dual    │
│Scroll │ │ Playfield │
└───────┘ └───────────┘
```

### Amiga Key Insights

1. **Signal works as Game 2** - it's genuinely different (timing vs action)
2. **Copper effects build gradually** - basics in G1, advanced later
3. **MOD playback is separate from sample playback** - can be introduced later
4. **Dual playfield requires solid scrolling understanding**

**Recommended Amiga order:** Current sequence works well. Signal as Game 2 introduces timing-based gameplay which is distinct from shooting.

---

## Summary: Skill Tree Findings

| Platform | Major Change Needed? | Key Adjustment |
|----------|---------------------|----------------|
| **C64** | Yes | SID Symphony → Game 6 (needs keyboard + timing) |
| **ZX Spectrum** | Yes | Ink War → Game 5 (needs AI/strategy experience) |
| **NES** | Yes | Remove Neon Nexus (redundant), or make optional |
| **Amiga** | No | Signal works as Game 2 |

### Universal Pattern

```
GAME 1: Shooter (128 units)
   └─→ Sprites, input, collision, sound effects, waves, polish

GAME 2: Different physics model
   └─→ Platformer OR Ball physics OR Timing game
   └─→ Introduces gravity/reflection/patience

GAMES 3-5: Variety of fixed-screen games
   └─→ Maze, puzzle, strategy
   └─→ AI, data structures, different genres

GAMES 6+: Platform-specific advanced features
   └─→ Scrolling, multiplexing, mappers, etc.
```

---

**Version:** 1.0
**Created:** 2026-01-18
