# Commodore 64 Curriculum

**Platform:** Commodore 64
**Killer Feature:** SID sound chip
**Games:** 16
**Total Units:** 1,728

---

## Overview

The Commodore 64 curriculum teaches 6510 assembly programming through 16 complete games. The sequence begins with the SID chip - the C64's defining feature - and progresses through sprites, scrolling, raster effects, and advanced techniques until learners can produce commercial-quality games.

By the final game, learners will have skills matching professional C64 developers of the late 1980s and early 1990s - equivalent to teams at Factor 5, System 3, or Thalamus.

---

## Unit Structure

Games scale in unit count based on complexity:

| Games | Units Each | Total | Rationale |
|-------|-----------|-------|-----------|
| 1-3 | 128 | 384 | Foundation games - shooter, platformer, maze - full experience |
| 4-10 | 64 | 448 | Foundation - core concepts |
| 11-13 | 128 | 384 | System-heavy - multiple complex systems |
| 14-15 | 128 | 256 | Advanced - new paradigms (isometric, Turrican-style) |
| 16 | 256 | 256 | Capstone - commercial quality with demo-scene techniques |
| **Total** | | **1,728** | |

Each game follows a phase structure (4-16 phases depending on length), with each phase containing 16 units.

---

## Game Sequence

### Game 1: Starfield
**Units:** 128 (8 phases)
**Concept:** Single-screen space shooter. Player ship versus waves of enemies. Shoot, dodge, survive. Immediate engagement from Unit 1.

**Skills taught:**
- Hardware sprites (enabling, positioning, pointers)
- Joystick input via CIA
- Sprite-to-sprite collision
- Bullet management and pooling
- Score display
- Wave systems
- Power-ups and ship upgrades
- SID sound effects (integrated throughout)
- Multicolour sprites
- Boss battles
- Commercial-quality polish

**Why first:** A shooter gets something playable on screen immediately. Learners control a ship from Unit 2, shoot from Unit 3. The SID is introduced through satisfying sound effects, not theory.

**Detailed outline:** `/docs/curriculum/templates/full-game-outline-c64-starfield.md`

---

### Game 2: Platform Panic
**Units:** 128 (8 phases)
**Concept:** Single-screen platformer. Jump between platforms, avoid hazards, reach the exit. Polished to commercial quality.

**Skills taught:**
- Gravity and jump physics
- Platform collision (landing, bumping)
- Tile-based collision detection
- Animation frames and states
- Hazard timing and moving platforms
- Level design and progression
- Ladders, collectibles, enemies
- Variable jump height, coyote time
- Full SID music and sound
- High scores, passwords, boss level

**Why here:** After shooting, platforming introduces the fundamental physics model used in countless games. 128 units allows a fully polished game, not just a prototype.

**Detailed outline:** `/docs/curriculum/templates/full-game-outline-c64-platform-panic.md`

---

### Game 3: Maze Raider
**Units:** 128 (8 phases)
**Concept:** Pac-Man style maze chase polished to commercial quality. Navigate corridors, collect pellets, avoid ghosts. Grab power pills to turn the tables.

**Skills taught:**
- Custom character sets (redefining C64 characters)
- Tile-based maps with colour RAM
- Ghost AI personalities (Blinky, Pinky, Inky, Clyde behaviours)
- Pathfinding introduction (intersection decision-making)
- State machines (chase, scatter, frightened, eaten)
- Level design for maze games
- Bonus fruit and score multipliers
- Full SID audio (waka-waka, sirens, music)

**Why here:** After sprites in Games 1-2, learners master character graphics for tile-based worlds. Ghost AI introduces pathfinding - a fundamental skill for all future games.

**Detailed outline:** `/docs/curriculum/templates/full-game-outline-c64-maze-raider.md`

---

### Game 4: Brick Basher
**Units:** 64 (4 phases)
**Concept:** Breakout clone. Paddle, ball, bricks. Clear the screen.

**Skills taught:**
- Ball physics (velocity vectors, reflection angles)
- Paddle control
- Brick grid collision
- Power-up systems (multi-ball, laser, catch)
- Increasing difficulty
- Level design variety

**Why here:** Physics refinement - angles, reflections, vectors. Different feel from gravity-based games.

**Detailed outline:** `/docs/plans/commodore-64/game-04-brick-basher.md`

---

### Game 5: Invader Wave
**Units:** 64 (4 phases)
**Concept:** Space Invaders style fixed shooter. Enemy formation descends, player defends.

**Skills taught:**
- Formation movement patterns
- Enemy bullet management (enemies shoot back)
- Shields (destructible character graphics)
- Wave progression
- High score persistence
- UFO bonus enemies
- Increasing wave difficulty

**Why here:** Builds on shooter from Game 1, adds formation AI and destructible terrain.

**Detailed outline:** `/docs/plans/commodore-64/game-05-invader-wave.md`

---

### Game 6: SID Symphony
**Units:** 64 (4 phases)
**Concept:** Rhythm game - notes scroll horizontally across three tracks, hit the correct key when notes reach the hit zone.

**Skills taught:**
- Deep SID chip exploration (voices, ADSR, waveforms)
- Keyboard matrix reading (not just joystick)
- Precise timing requirements
- Screen layout with character graphics
- Song sequencing and patterns
- Difficulty progression

**Why here:** Rhythm games require timing precision and keyboard input - skills that benefit from 5 games of experience. The SID deep dive is more meaningful after hearing it in action games.

**Detailed outline:** `/docs/plans/commodore-64/game-06-sid-symphony.md`

---

### Game 7: Scroll Runner
**Units:** 64 (4 phases)
**Concept:** Horizontal scrolling introduction. Runner dodges obstacles in an endless scroll.

**Skills taught:**
- Hardware horizontal scrolling (VIC-II $D016)
- Colour RAM scrolling
- Screen buffer management
- Double buffering
- Colour splits (basic raster)
- Procedural obstacle spawning
- Basic parallax background

**Detailed outline:** `/docs/plans/commodore-64/game-07-scroll-runner.md`

---

### Game 8: Night Raid
**Units:** 64 (4 phases)
**Concept:** Scramble-style side-scroller. Fly through terrain, shoot enemies, manage fuel.

**Skills taught:**
- Scrolling combined with shooting
- Terrain collision
- Resource management (fuel)
- Ground and air targets
- Level streaming from data
- Boss encounters
- Bomb mechanics

**Detailed outline:** `/docs/plans/commodore-64/game-08-night-raid.md`

---

### Game 9: Sprite Storm
**Units:** 64 (4 phases)
**Concept:** Multi-sprite action game. More enemies than the hardware allows - enter multiplexing.

**Skills taught:**
- Sprite multiplexing (16-32 sprites)
- Sorted sprite lists
- Raster interrupt timing
- Sprite priority and overlap
- Performance optimisation
- Arena shooter gameplay
- Wave-based enemy spawning

**Detailed outline:** `/docs/plans/commodore-64/game-09-sprite-storm.md`

---

### Game 10: Raster Rider
**Units:** 64 (4 phases)
**Concept:** Racing game with pseudo-3D road using raster effects.

**Skills taught:**
- Advanced raster splits
- Colour cycling for speed effect
- Road perspective rendering
- Opponent cars
- Timer-based gameplay
- Track variety
- Position-based scoring

**Detailed outline:** `/docs/plans/commodore-64/game-10-raster-rider.md`

---

### Game 11: Dungeon Crawl
**Units:** 128 (8 phases)
**Concept:** Top-down adventure. Explore rooms, collect keys, unlock doors, solve puzzles, defeat enemies.

**Skills taught:**
- Multi-room map architecture
- Room transitions
- Full inventory system
- NPC dialogue system
- Quest framework
- Combat system
- Environmental puzzles
- **Disk I/O fundamentals** (Kernal routines)
- **Disk save/load system**
- **D64 disk image creation**
- Password backup system

**Why 128 units:** First game with multiple complex interconnected systems (inventory, quests, NPCs, combat, saves).

**Detailed outline:** `/docs/plans/commodore-64/game-11-dungeon-crawl.md`

---

### Game 12: Arena Fighter
**Units:** 128 (8 phases)
**Concept:** One-on-one fighting game. Four fighters, health bars, special moves, combos.

**Skills taught:**
- Complex animation state machines
- Hitbox/hurtbox collision system
- Frame data (startup, active, recovery)
- Input buffering
- Motion input detection (QCF, DP)
- Special moves and super meter
- AI opponent with difficulty scaling
- 4 distinct character archetypes

**Why 128 units:** Fighting games require deep state machine work, frame-perfect timing, and multiple complete characters.

**Detailed outline:** `/docs/plans/commodore-64/game-12-arena-fighter.md`

---

### Game 13: Parallax Patrol
**Units:** 128 (8 phases)
**Concept:** Advanced side-scrolling shooter with multi-layer parallax. R-Type/Gradius style.

**Skills taught:**
- Multi-layer parallax scrolling (3+ layers)
- Advanced weapon systems (4 types with upgrades)
- Option drones with formations
- Charge shot mechanics
- 7 complete stages with unique themes
- Epic multi-phase boss encounters
- Level compression (RLE)
- Checkpoint system
- Two-player cooperative mode

**Why 128 units:** 7 stages each needing unique terrain, enemies, and bosses plus complex weapon and option systems.

**Detailed outline:** `/docs/plans/commodore-64/game-13-parallax-patrol.md`

---

### Game 14: Isometric Quest
**Units:** 128 (8 phases)
**Concept:** Isometric adventure game. Explore a 3D-perspective world, solve puzzles, complete quests.

**Skills taught:**
- Isometric projection mathematics
- World-to-screen coordinate conversion
- Depth sorting (painter's algorithm)
- Isometric collision detection
- A* pathfinding in isometric space
- Z-height handling (elevated terrain)
- Large world with 64+ screens
- Full adventure game systems

**Why 128 units:** Isometric is a completely different paradigm requiring new mathematics, rendering, and collision approaches.

**Detailed outline:** `/docs/plans/commodore-64/game-14-isometric-quest.md`

---

### Game 15: Mega Blaster
**Units:** 128 (8 phases)
**Concept:** Turrican-style run'n'gun. Large scrolling world, multiple weapons, vehicle transformations, epic bosses.

**Skills taught:**
- Multi-directional scrolling (8-way)
- Advanced weapon variety (beam, spread, bounce, missiles)
- Grappling hook mechanics
- Vehicle transformation (wheel mode)
- Massive boss encounters
- Level streaming for huge worlds
- Exploration-based level design
- Hidden secrets and power-ups

**Why 128 units:** Turrican-level complexity requires extensive content and multiple interconnected systems.

**Detailed outline:** `/docs/plans/commodore-64/game-15-mega-blaster.md`

---

### Game 16: Symphony's End
**Units:** 256 (16 phases)
**Concept:** Commercial-quality capstone. A complete, polished action-adventure combining everything learnt with demo-scene techniques.

**Skills taught:**
- All previous techniques at mastery level
- **Demo-scene effects:** FLD, DYCP, AGSP
- **Advanced SID:** filters, ring modulation, multi-speed playback
- IRQ loader with music during load
- **Direct 1541 drive programming** (drive's 6502, serial protocol)
- **Custom fast loader** (bypassing Kernal, GCR decoding)
- **Turbo tape loader** for cassette distribution
- Professional disk mastering
- Dual distribution (D64 disk + tape)

**Why 256 units:** The capstone integrates all 15 previous games' skills plus demo-scene techniques and professional distribution.

**Why last:** The curriculum ends where it began - with the SID. But now the learner commands every aspect of the machine.

**Detailed outline:** `/docs/plans/commodore-64/game-16-symphonys-end.md`

---

## BASIC V2 Gateway (Optional)

For learners wanting a gentler introduction before assembly, an optional BASIC V2 curriculum is available. This 512-unit track (8 games × 64 units) teaches programming fundamentals through complete games before tackling 6510.

**Games:** Number Hunter, Cosmic Drift, Catcher, Maze Escape, Snake Trail, Space Dodge, Memory Match, Platform Peril

**Skills taught:**
- BASIC V2 fundamentals (PRINT, INPUT, IF/THEN)
- POKE/PEEK for screen and colour memory
- Character graphics and custom characters
- Real-time input with GET
- Arrays and game state
- BASIC's limits - why assembly is needed

The BASIC gateway is optional. Learners can start directly at Game 1 (SID Symphony) with no BASIC knowledge required. The gateway exists for those who prefer building foundational programming concepts before diving into assembly.

See `/docs/curriculum/commodore-64-basic-curriculum.md` for full details.

---

## Skill Progression

| Games | Focus | Era Equivalent |
|-------|-------|----------------|
| 1-6 | Single-screen fundamentals | 1982-1984 |
| 7-8 | Scrolling introduction | 1984-1985 |
| 9-10 | Advanced hardware techniques | 1985-1987 |
| 11-13 | Complex game systems | 1986-1988 |
| 14-15 | Advanced paradigms | 1988-1991 |
| 16 | Commercial/demo-scene quality | 1991-1993 |

By Game 16, learners produce work comparable to late-era commercial releases like Turrican II (1991) and Mayhem in Monsterland (1993), with loading and distribution matching System 3 or Thalamus standards.

---

## Distribution Skills Progression

| Game | Skills Introduced |
|------|------------------|
| 11 (Dungeon Crawl) | Kernal disk I/O, disk saves, basic D64 creation |
| 12-15 | Apply disk skills to releases |
| 16 (Symphony's End) | Direct 1541 programming, custom fast loader, turbo tape |

---

## Optional Enhancement Versions

Select games have optional enhanced versions for expanded hardware. Not every game warrants enhancement - these target games where the additional capabilities meaningfully improve the experience.

### MEGA65 Enhancements

For games that benefit from VIC-IV, 40MHz, and enhanced SID:

| Game | Units | Enhancement Focus |
|------|-------|-------------------|
| 9-16 (select) | 32-128 | VIC-IV graphics, DMA, dual SID, 40MHz |

MEGA65 enhancements follow the Amiga AGA model - separate versions that showcase the enhanced hardware while the main game remains stock C64 compatible.

**Structure (when implemented):**
- Games 9-14 MEGA65: 32 units each
- Game 15 MEGA65: 64 units
- Game 16 MEGA65: 128 units

### Post-Capstone: REU Programming

**Game 17: REU Adventure** (64 units)
Expansion hardware programming using the 1750 REU. DMA transfers, extended memory, techniques for REU-enhanced games.

See `/docs/plans/future-expansion-tracks.md` for full details.

---

## Version History

- **3.5 (2026-01-18):** Expanded Game 3 (Maze Raider) to 128 units with ghost AI personalities and pathfinding. Total now 1,728 units.
- **3.4 (2026-01-18):** Expanded Game 2 (Platform Panic) to 128 units for full polish. Total now 1,664 units.
- **3.3 (2026-01-18):** Reordered games per skill tree analysis. Platform Panic now Game 2 (introduces gravity/tiles). SID Symphony moved to Game 6 (requires keyboard + timing skills). See `/docs/curriculum/SKILL-TREES.md`.
- **3.2 (2026-01-18):** Restructured Game 1. Starfield (shooter) now first game at 128 units for immediate engagement. Total now 1,600 units.
- **3.1 (2026-01-07):** Added optional enhancement versions section (MEGA65, REU). Updated BASIC gateway reference to 512-unit curriculum.
- **3.0 (2025-01-07):** Expanded to 1,536 units. Games 1-10 at 64 units, Games 11-15 at 128 units, Game 16 at 256 units. Added disk I/O, fast loaders, turbo tape.
- **2.0 (2025-11-25):** Complete rewrite. Replaced phases/tiers/lessons with games model.
- **1.0 (2025-01-15):** Original 4,096-lesson curriculum.
