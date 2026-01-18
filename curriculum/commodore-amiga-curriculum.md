# Commodore Amiga 68000 Assembly Curriculum

**Platform:** Commodore Amiga
**Language:** 68000 Assembly
**Prerequisite:** AMOS BASIC curriculum (recommended) or equivalent experience
**Games:** 16 (OCS/ECS) + 8 AGA enhancements
**Total Units:** 2,880 (2,496 OCS/ECS + 384 AGA)

---

## Overview

The Amiga 68000 Assembly curriculum teaches direct hardware programming through 16 complete games. The sequence begins with the custom chipset fundamentals - Agnus, Denise, and Paula working together - and progresses through Blitter mastery, Copper programming, parallax scrolling, isometric projection, and advanced techniques until learners can produce commercial-quality games.

The Amiga wasn't about one killer feature. It was about the custom chips working in harmony: the Blitter accelerating graphics, the Copper synchronising effects to the display beam, Paula playing four channels of sampled audio. This curriculum teaches learners to conduct that orchestra.

This is an expanded curriculum because the Amiga's hardware requires deeper coverage - Blitter operations, Copper lists, DMA timing, and the interplay between all components.

By the final game, learners will have skills matching professional Amiga developers of the early 1990s.

---

## Curriculum Structure

| Phase | Games | Units Each | Total |
|-------|-------|------------|-------|
| Foundation (shooter, timing, breakout, platformer, exploration, maze, snake) | 1-7 | 128 | 896 |
| Foundation | 8 | 64 | 64 |
| Advanced | 9-14 | 128 | 768 |
| Expert | 15 | 256 | 256 |
| Capstone | 16 | 512 | 512 |
| **Total** | **16** | | **2,496** |

The expanded structure allows thorough coverage of:
- Blitter operations (copy, fill, line draw, cookie-cut)
- Copper programming (display lists, effects, timing)
- DMA channels and timing
- Dual playfield modes
- Hardware sprites and Blitter objects
- Paula audio (sample playback, mixing)
- Disk access (trackdisk vs AmigaDOS)

---

## Game Sequence

### Foundation Games

#### Game 1: Blast Zone
**Units:** 128 (8 phases)
**Concept:** Fixed-screen space shooter. Player ship versus enemy waves. Immediate engagement from Unit 1, bootable from the start.

**Skills taught:**
- 68000 assembly fundamentals
- Display setup and Copper list basics
- Hardware sprites (player ship)
- Blitter objects (BOBs for enemies)
- Copper gradients and colour effects
- Paula sample playback
- Bootable ADF creation (from Unit 1)
- Projectile spawning and pooling
- Enemy formations and patterns
- Multiple collision types
- Wave progression
- Score display with Blitter text
- Boss battles
- Commercial-quality polish

**Why first:** A shooter gets something playable on screen immediately. Learners control a ship from Unit 2, shoot from Unit 3. The chipset symphony is learned through building a real game, and learners can run their game from a bootable disk from day one.

**Detailed outline:** `/docs/curriculum/templates/full-game-outline-amiga-blast-zone.md`

---

#### Game 2: Signal
**Units:** 128 (8 phases)
**Concept:** Frogger-style lane crosser polished to commercial quality. Cross roads, ride logs, avoid hazards, reach home. A timing game that showcases Amiga audiovisuals.

**Skills taught:**
- Grid-based hop movement (different from continuous)
- Lane objects as BOBs (cars, trucks, logs, turtles)
- Riding moving objects (velocity transfer)
- Timing-based gameplay (patience vs. reflexes)
- Copper gradient backgrounds (sky, water)
- MOD music with SFX mixing
- Multiple hazards (crocs, snakes, diving turtles)
- Power-ups (bonus flies, lady frog escort)
- High scores, difficulty, multiplayer
- 15 levels with increasing challenge

**Why here:** After the action-focused shooter, Signal teaches timing and patience - a different gameplay rhythm. 128 units allows proper exploration of feel and polish.

**Detailed outline:** `/docs/curriculum/templates/full-game-outline-amiga-signal.md`

---

#### Game 3: Shatter Point
**Units:** 128 (8 phases)
**Concept:** Breakout clone polished to commercial quality. Paddle, ball, bricks - with Copper gradient backgrounds, sampled impacts, and Blitter-powered destruction.

**Skills taught:**
- Ball physics with 16.16 fixed-point maths
- Blitter fills for brick rendering and destruction
- Copper gradient backgrounds (dynamic sky effects)
- Paula sample playback for varied impacts
- Paddle angle control for ball direction
- Multiple brick types (hard, unbreakable, explosive)
- Power-up system (extend, multi-ball, laser, catch)
- Multi-ball management
- Level design variety (20 levels)
- MOD music with SFX mixing
- Full polish (high scores, difficulty options)

**Why here:** After BOBs and sprites in Games 1-2, learners apply Blitter skills to physics-based gameplay and background manipulation.

**Detailed outline:** `/docs/curriculum/templates/full-game-outline-amiga-shatter-point.md`

---

#### Game 4: Ascent
**Units:** 128 (8 phases)
**Concept:** Single-screen platformer polished to commercial quality. Climb upward through hazards, collect items, reach the exit. Smooth 50fps gameplay with Copper-enhanced visuals and sampled audio.

**Skills taught:**
- Gravity and jump physics (velocity, acceleration, variable height)
- Platform collision with Blitter backgrounds
- BOB animation for player character (walk cycle, jump frames)
- Blitter cookie-cut masking
- Moving platforms (horizontal and vertical)
- Crumbling platforms and environmental hazards
- Patrolling and flying enemies
- Stomping enemies mechanic
- Power-ups (speed, high jump, invincibility)
- 20 levels across multiple themed worlds
- Boss battles
- MOD music with SFX mixing

**Why here:** After horizontal gameplay in Games 1-3, learners tackle vertical movement and jump physics - the foundation for countless games.

**Detailed outline:** `/docs/curriculum/templates/full-game-outline-amiga-ascent.md`

---

#### Game 5: Crypt
**Units:** 128 (8 phases)
**Concept:** Flip-screen top-down dungeon exploration polished to commercial quality. Navigate interconnected rooms, collect keys and treasures, defeat monsters, find the exit. Smooth 50fps with Copper-enhanced room transitions.

**Skills taught:**
- Room data structures and Blitter tile rendering
- Screen transitions with Copper fades
- Persistent state management
- Inventory system (keys, potions, weapons)
- Enemy AI (patrol, chase, wall-aware)
- Combat system (melee attack)
- Multiple enemy types including ranged
- Coloured keys and locked doors
- Push blocks and puzzle elements
- Multiple dungeon floors
- Copper zone palettes for visual variety
- Boss encounters
- Save system
- MOD music with SFX mixing

**Why here:** After single-screen games, learners manage multi-room worlds with persistent state - foundation for adventure games.

**Detailed outline:** `/docs/curriculum/templates/full-game-outline-amiga-crypt.md`

---

#### Game 6: Gobble
**Units:** 128 (8 phases)
**Concept:** Pac-Man style maze game polished to commercial quality. Collect dots, avoid ghosts with distinct AI personalities, eat power pills to turn the tables. Smooth 50fps with Copper-enhanced effects.

**Skills taught:**
- Tile-based maze with Blitter rendering
- Constrained corridor movement
- Four ghost AI personalities (Blinky, Pinky, Inky, Clyde)
- Chase/scatter mode state machines
- Frightened mode with ghost-eating
- Screen wrapping via tunnels
- Speed and difficulty progression
- Copper gradient backgrounds
- Intermission cut-scenes
- Paula sample audio (waka, siren)
- MOD music for title
- Demo mode
- Two-player simultaneous mode

**Why here:** After dungeon exploration, learners create constrained corridor movement with sophisticated enemy AI. Four distinct ghost behaviours create emergent gameplay.

**Detailed outline:** `/docs/curriculum/templates/full-game-outline-amiga-gobble.md`

---

#### Game 7: Venom
**Units:** 128 (8 phases)
**Concept:** Classic snake game polished to commercial quality. Uses ring buffer for efficient body management and showcases Blitter segment rendering with Copper colour effects.

**Skills taught:**
- Ring buffer implementation in 68000
- Grid-based movement system
- Self-collision detection algorithms
- Blitter-based segment rendering
- Growth mechanics
- Speed scaling with difficulty progression
- Multiple level packs with maze layouts
- Moving obstacles and teleport portals
- Power-up system (slow-down, ghost, score multiplier)
- Two-player split-screen mode
- AI opponent with difficulty levels
- Theme system (Jungle, Tech, Desert)
- Copper colour effects and gradients
- Paula sound effects and module music
- Achievement and statistics tracking
- Demo/attract mode

**Why here:** After maze navigation in Gobble, learners tackle a different grid-based challenge. The ring buffer is fundamental to game programming, and the Amiga's hardware makes segment rendering smooth and colourful.

**Detailed outline:** `/docs/curriculum/templates/full-game-outline-amiga-venom.md`

---

#### Game 8: Tetrad
**Units:** 64 (4 phases)
**Concept:** Falling blocks puzzle with Blitter rendering.

**Skills taught:**
- Piece rotation maths
- Grid collision detection
- Line clearing with Blitter scroll
- Next piece preview
- Ghost piece
- Score multipliers
- Two-player mode

---

### Advanced Games (128 Units Each)

#### Game 9: Parallax
**Units:** 128 (8 phases)
**Concept:** Horizontal parallax shooter - the quintessential Amiga showcase.

**Skills taught:**
- Dual playfield mode
- Multiple scroll layers at different speeds
- Copper palette cycling
- Hardware scrolling with Blitter updates
- Enemy patterns in scrolling world
- Terrain collision
- Power-up system
- Boss encounters
- Paula MOD replay basics

**Why expanded:** Dual playfield and parallax scrolling require deep understanding of bitplane DMA timing.

---

#### Game 10: Wanderer
**Units:** 128 (8 phases)
**Concept:** Scrolling platformer. Large world exploration.

**Skills taught:**
- Horizontal scrolling platformer
- Camera following with dead zones
- Large level data (compression)
- Checkpoints and progress
- Moving platforms
- Environmental hazards
- Parallax backgrounds
- Extended enemy AI

---

#### Game 11: Brawler
**Units:** 128 (8 phases)
**Concept:** Side-scrolling beat 'em up with Y-depth sorting.

**Skills taught:**
- Y-axis depth sorting
- Large sprite animation
- Melee combat mechanics
- Combo systems
- Multiple enemy coordination
- Health and damage
- Weapon pickups
- Boss fights
- Two-player cooperative

---

#### Game 12: Highway
**Units:** 128 (8 phases)
**Concept:** Pseudo-3D racing with Copper road effects.

**Skills taught:**
- Perspective projection
- Copper-based road rendering
- Sprite scaling simulation
- Speed simulation
- Traffic and obstacles
- Road curves via Copper
- Hill rendering
- Split-screen two-player
- Time trial and championship modes

---

#### Game 13: Onslaught
**Units:** 128 (8 phases)
**Concept:** Vertical scrolling shooter with bullet patterns.

**Skills taught:**
- Vertical scrolling
- Formation enemy patterns
- Bullet pattern systems
- Ground and air targets
- Multi-phase bosses
- Weapon upgrade trees
- Rank system (dynamic difficulty)
- Full MOD soundtrack

---

#### Game 14: Fortress
**Units:** 128 (8 phases)
**Concept:** Isometric action-adventure. 3D projection with exploration and puzzles.

**Skills taught:**
- Isometric projection maths
- 3D coordinate systems
- Depth sorting (painter's algorithm)
- Isometric collision detection
- Block puzzle mechanics
- Equipment and inventory
- Multiple zones
- Boss encounters

---

### Expert Game (256 Units)

#### Game 15: Echoes of the Ancients
**Units:** 256 (16 phases)
**Concept:** Connected world exploration with ability-gating. Metroidvania design on Amiga hardware.

**Skills taught:**
- Large connected world map
- Non-linear progression
- Ability-gating design
- Backtracking and shortcuts
- Player progression system
- Save system with battery backup
- Multiple endings
- Advanced Blitter techniques
- Memory management for large games
- Advanced Copper effects
- Multi-disk support

**Why expanded:** Metroidvania design requires extensive world building, ability systems, and careful memory management.

---

### Capstone Game (512 Units)

#### Game 16: Ascension: The Guru Meditation
**Units:** 512 (32 phases)
**Concept:** Epic action-adventure combining everything. The title reclaims the infamous Amiga error as a badge of honour.

**Skills taught:**
- All previous techniques at mastery
- Large world design
- Multiple gameplay styles
- Deep combat system
- Equipment and magic
- NPC dialogue and quests
- Full save system
- Advanced Copper tricks
- Optimised Blitter usage
- Custom disk loading
- Professional production values
- Complete portfolio piece

**Why capstone:** Demonstrates total mastery of the Amiga hardware. A commercial-quality game worthy of the platform's legacy.

---

## AGA Enhancement Games

The AGA (Advanced Graphics Architecture) chipset, introduced with the A1200 and A4000 in 1992, offered significant improvements over OCS/ECS. Many commercial games shipped in separate OCS and AGA versions - learners follow this industry practice by creating enhanced AGA versions of Games 9-16.

### AGA Curriculum Structure

| OCS Game | OCS Units | AGA Enhancement | AGA Units |
|----------|-----------|-----------------|-----------|
| 9: Parallax | 128 | Parallax AGA | 32 |
| 10: Wanderer | 128 | Wanderer AGA | 32 |
| 11: Brawler | 128 | Brawler AGA | 32 |
| 12: Highway | 128 | Highway AGA | 32 |
| 13: Onslaught | 128 | Onslaught AGA | 32 |
| 14: Fortress | 128 | Fortress AGA | 32 |
| 15: Echoes | 256 | Echoes AGA | 64 |
| 16: Ascension | 512 | Ascension AGA | 128 |
| **Totals** | **1,536** | | **384** |

### AGA Hardware Features

**Lisa (replaces Denise):**
- 256 colours on-screen from 16.7 million (24-bit) palette
- 8 bitplane modes (vs 6 for ECS)
- Enhanced sprite capabilities
- Wider sprites (64 pixels)

**Alice (replaces Agnus):**
- 2MB chip RAM support
- Enhanced DMA bandwidth
- Improved Blitter

**Key AGA Modes:**
- 256-colour chunky/planar modes
- HAM8 - 262,144 colours (vs HAM6's 4,096)
- Super hi-res with more colours

### AGA Enhancement Games (32-128 Units Each)

#### Game 9 AGA: Parallax AGA
**Units:** 32 (2 phases)
**Enhancement focus:** 256-colour parallax layers, smoother gradients, enhanced palette cycling.

---

#### Game 10 AGA: Wanderer AGA
**Units:** 32 (2 phases)
**Enhancement focus:** Richer environment palettes, more detailed sprites, enhanced parallax depth.

---

#### Game 11 AGA: Brawler AGA
**Units:** 32 (2 phases)
**Enhancement focus:** Larger, more colourful character sprites, richer backgrounds, enhanced effects.

---

#### Game 12 AGA: Highway AGA
**Units:** 32 (2 phases)
**Enhancement focus:** Smoother road colour gradients, better sprite scaling, enhanced sky effects.

---

#### Game 13 AGA: Onslaught AGA
**Units:** 32 (2 phases)
**Enhancement focus:** More colourful bullet patterns, richer backgrounds, enhanced explosion effects.

---

#### Game 14 AGA: Fortress AGA
**Units:** 32 (2 phases)
**Enhancement focus:** Richer isometric tiles, enhanced lighting effects, more detailed environments.

---

#### Game 15 AGA: Echoes of the Ancients AGA
**Units:** 64 (4 phases)
**Enhancement focus:** 256-colour Metroidvania visuals, enhanced atmospheric effects, richer zone palettes, HAM8 cutscenes.

---

#### Game 16 AGA: Ascension AGA
**Units:** 128 (8 phases)
**Enhancement focus:** Full AGA showcase - 256-colour graphics throughout, HAM8 cinematics, enhanced effects, A1200/A4000 optimisations. The definitive version.

---

### AGA Skills Taught

| Phase | Skills |
|-------|--------|
| Games 9-12 AGA | AGA register basics, 256-colour modes, palette expansion |
| Games 13-14 AGA | Enhanced bitplane modes, AGA Copper techniques |
| Game 15 AGA | HAM8 mode, advanced AGA effects |
| Game 16 AGA | Full AGA mastery, A1200/A4000 optimisation |

---

## Hardware Skill Progression

### Blitter Progression

| Games | Blitter Skills |
|-------|---------------|
| 1-4 | Basic copy, simple BOBs |
| 5-8 | Cookie-cut, fills, tile rendering |
| 9-11 | Scrolling updates, large BOBs |
| 12-14 | Line draw, complex fills, isometric |
| 15 | Optimised blits, interleaved |
| 16 | Full Blitter mastery |

### Copper Progression

| Games | Copper Skills |
|-------|--------------|
| 1-4 | Display setup, colour splits |
| 5-8 | Palette changes, transitions |
| 9-11 | Parallax coordination, gradients |
| 12-14 | Road effects, sprite repositioning |
| 15 | Complex display lists |
| 16 | Full Copper mastery |

### Paula Progression

| Games | Audio Skills |
|-------|-------------|
| 1-4 | Sample playback, sound effects |
| 5-8 | Multiple samples, mixing basics |
| 9-11 | MOD replay, dynamic music |
| 12-14 | Positional audio, effects |
| 15 | Advanced mixing, priorities |
| 16 | Full audio production |

---

## Platform Context

### Hardware

- **CPU:** Motorola 68000 @ 7.16 MHz (NTSC) / 7.09 MHz (PAL)
- **RAM:** 512KB chip RAM (A500), expandable
- **Display:** Multiple modes, typically 320×256 (PAL) or 320×200 (NTSC)
- **Colours:** 32 on-screen from 4096 palette (OCS/ECS), more with tricks
- **Sound:** Paula - 4 channels, 8-bit PCM samples
- **Storage:** 880KB 3.5" floppy disks

### The Custom Chipset

**Agnus** - DMA controller and Blitter
- Coordinates all memory access
- Contains the Blitter for fast graphics
- Contains the Copper coprocessor
- Manages bitplane, sprite, audio DMA

**Denise** - Display and sprites
- Generates video output
- Manages 8 hardware sprites
- Handles playfield display
- Colour palette registers

**Paula** - Audio and disk
- Four channels of sampled sound
- Floppy disk control
- Interrupt control

### Key Concepts

**Copper:** Display-list coprocessor that executes commands synchronised to the video beam. Essential for:
- Palette changes mid-screen
- Sprite repositioning
- Register modifications
- Parallax effects

**Blitter:** Hardware block transfer and drawing:
- Area copy with masking
- Line drawing
- Area filling
- Cookie-cut compositing

**Hardware Sprites:** 8 sprites, 16 pixels wide, 3 colours + transparent. Can be:
- Paired for 15 colours
- Repositioned via Copper for more appearances
- Attached for wider sprites

**Blitter Objects (BOBs):** Software sprites drawn by Blitter:
- Any size
- Any colour depth
- More flexible but CPU/Blitter intensive

---

## Distribution

Games are distributed as:
- ADF disk images (880KB)
- Multi-disk for larger games
- Bootable (game loads directly)
- Optional AmigaDOS loading for development

---

## Era Comparison

| Games | Era Equivalent | Commercial Examples |
|-------|----------------|---------------------|
| 1-4 | 1985-1986 | Marble Madness, Defender of the Crown |
| 5-8 | 1987-1988 | Barbarian, Xenon |
| 9-11 | 1988-1990 | Shadow of the Beast, Turrican |
| 12-14 | 1990-1991 | Lotus, SWIV, Cadaver |
| 15 | 1991-1992 | Super Metroid-style exploration |
| 16 | 1992-1994 | Lionheart, The Chaos Engine |

By Game 16, learners produce work comparable to late-era commercial releases.

---

## Version History

- **3.9 (2026-01-18):** Expanded Game 7 (Venom) to 128 units with ring buffer, two-player split-screen, and theme system. OCS/ECS total now 2,496 units.
- **3.8 (2026-01-18):** Expanded Game 6 (Gobble) to 128 units with four ghost AI personalities. OCS/ECS total now 2,432 units.
- **3.7 (2026-01-18):** Expanded Game 5 (Crypt) to 128 units with full dungeon exploration. OCS/ECS total now 2,368 units.
- **3.6 (2026-01-18):** Expanded Game 4 (Ascent) to 128 units with full platformer polish. OCS/ECS total now 2,304 units.
- **3.5 (2026-01-18):** Expanded Game 3 (Shatter Point) to 128 units with Blitter physics and power-ups. OCS/ECS total now 2,240 units.
- **3.4 (2026-01-18):** Expanded Game 2 (Signal) to 128 units for full timing-game polish. OCS/ECS total now 2,176 units.
- **3.3 (2026-01-18):** Restructured Game 1. Blast Zone (shooter) now first game at 128 units for immediate engagement, bootable from Unit 1. Signal moved to Game 2.
- **3.2 (2026-01-07):** Added AGA enhancement games (384 units) for Games 9-16. Total now 2,432 units.
- **3.1 (2026-01-07):** Corrected structure to use only powers of 2 for unit counts (64/128/256/512).
- **3.0 (2025-01-07):** Restructured to 2,048 units with expanded hardware coverage. AMOS moved to separate curriculum.
- **2.0 (2025-11-26):** Complete rewrite. Replaced phases/tiers/lessons with games model.
- **1.0 (2025-01-15):** Original curriculum.
