# Commodore 64 Curriculum

**Platform:** Commodore 64
**Killer Feature:** SID sound chip
**Games:** 16
**Total Units:** 2,688

---

## Overview

The Commodore 64 curriculum teaches 6510 assembly programming through 16 complete games. The sequence begins with the SID chip - the C64's defining feature - and progresses through sprites, scrolling, raster effects, and advanced techniques until learners can produce commercial-quality games.

By the final game, learners will have skills matching professional C64 developers of the late 1980s and early 1990s - equivalent to teams at Factor 5, System 3, or Thalamus.

---

## Unit Structure

Games scale in unit count based on complexity:

| Games | Units Each | Total | Rationale |
|-------|-----------|-------|-----------|
| 1-8 | 128 | 1,024 | Foundation games - shooter, platformer, maze, breakout, exploration, rhythm, scrolling, Scramble |
| 9-10 | 64 | 128 | Foundation - core concepts |
| 11-13 | 128 | 384 | System-heavy - multiple complex systems |
| 14-15 | 128 | 256 | Advanced - new paradigms (isometric, Turrican-style) |
| 16 | 256 | 256 | Capstone - commercial quality with demo-scene techniques |
| **Total** | | **2,048** | |

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
**Units:** 128 (8 phases)
**Concept:** Breakout clone polished to commercial quality. Paddle, ball, bricks - with tight physics, satisfying destruction, and the SID chip making every bounce sing.

**Skills taught:**
- Ball physics with fixed-point maths (velocity, reflection, spin)
- Paddle collision with positional angle control
- Character graphics for brick fields
- Multiple brick types (hard, unbreakable, explosive)
- Power-up systems (extend, multi-ball, laser, catch, slow)
- SID audio design for satisfying impacts
- 20 levels of varied brick patterns
- High scores, difficulty options, two-player mode

**Why here:** Physics refinement - angles, reflections, vectors. Different feel from gravity-based games. 128 units allows full polish.

**Detailed outline:** `/docs/curriculum/templates/full-game-outline-c64-brick-basher.md`

---

### Game 5: Catacombs
**Units:** 128 (8 phases)
**Concept:** Flip-screen top-down dungeon exploration polished to commercial quality. Navigate interconnected rooms, collect keys and treasures, avoid monsters, find the exit. In the tradition of classic C64 explorers.

**Skills taught:**
- Room data structures and transitions
- Persistent state (items stay collected)
- Custom character set for dungeon tiles
- Inventory system (keys, potions, weapons)
- Enemy AI (patrol, chase, ranged)
- Combat system (melee and ranged)
- Multiple dungeon floors
- Coloured keys and locked doors
- Push blocks and puzzle elements
- Full SID audio (music and effects)
- Save/checkpoint system
- Boss battles

**Why here:** After single-screen games, learners manage multi-room worlds with persistent state - the foundation for larger adventure games.

**Detailed outline:** `/docs/curriculum/templates/full-game-outline-c64-catacombs.md`

---

### Game 6: SID Symphony
**Units:** 128 (8 phases)
**Concept:** Rhythm game polished to commercial quality. Notes scroll horizontally across three tracks (one per SID voice), hit the correct key when notes reach the hit zone. A deep dive into the SID chip through gameplay.

**Skills taught:**
- Deep SID chip mastery (all three voices, ADSR, waveforms)
- Keyboard matrix reading (not just joystick)
- Precise timing requirements
- Filter control and resonance
- Ring modulation and sync effects
- Pulse width modulation
- Song data structures and sequencing
- Timing accuracy system (Perfect/Good/OK)
- Combo and multiplier systems
- Multiple difficulty levels
- Song editor basics
- Two-player and battle modes

**Why here:** Rhythm games require timing precision and keyboard input - skills that benefit from 5 games of experience. The SID deep dive is more meaningful after hearing it in action games.

**Detailed outline:** `/docs/curriculum/templates/full-game-outline-c64-sid-symphony.md`

---

### Game 7: Scroll Runner
**Units:** 128 (8 phases)
**Concept:** Endless horizontal scroller. Runner dodges obstacles in an endless scroll, teaching VIC-II hardware scrolling, double buffering, and parallax effects.

**Skills taught:**
- VIC-II horizontal hardware scrolling ($D016)
- Fine scroll and coarse scroll coordination
- Colour RAM scrolling synchronisation
- Screen buffer management
- Double buffering for tear-free display
- Raster interrupts for colour splits
- Parallax background layers (multiple speeds)
- Procedural obstacle spawning
- Jump and duck mechanics
- Sprite multiplexing for extra enemies
- Power-up systems
- Speed progression and difficulty curves
- Custom character sets
- Music tempo that matches gameplay speed

**Why here:** Hardware scrolling is a defining C64 technique. After mastering single-screen games, learners tackle the fundamentals that power side-scrollers, shoot-em-ups, and platformers.

**Detailed outline:** `/docs/curriculum/templates/full-game-outline-c64-scroll-runner.md`

---

### Game 8: Night Raid
**Units:** 128 (8 phases)
**Concept:** Scramble-style side-scroller polished to commercial quality. Fly your jet through enemy territory, navigate scrolling terrain, shoot enemies, bomb ground targets, and manage fuel. A complete horizontal shooter showcasing combined scrolling and combat mechanics.

**Skills taught:**
- Scrolling combined with shooting mechanics
- Character-based terrain collision in scrolling world
- Resource management (fuel depletion and collection)
- Dual weapon systems (forward shots and bombs)
- Ground targets and air enemies
- Level streaming from compressed data
- Multiple enemy types with varied patterns
- Boss encounters with pattern-based attacks
- Power-up system (speed, rapid fire, shield, weapon upgrades)
- Raster colour effects for atmosphere
- Parallax starfield background
- Multiple levels with themed terrain
- Checkpoint and lives system
- Two-player alternating mode
- Demo/attract mode
- Turbo loader for fast loading

**Why here:** Building on Scroll Runner's horizontal scrolling foundation, Night Raid combines scrolling with the shooting mechanics learned in earlier games. Resource management adds strategic depth.

**Detailed outline:** `/docs/curriculum/templates/full-game-outline-c64-night-raid.md`

---

### Game 9: Sprite Storm
**Units:** 256 (16 phases)
**Concept:** Arena shooter displaying 24-32 sprites using THE defining C64 technique: sprite multiplexing. Master raster interrupt timing, Y-sorted sprite allocation, and cycle-exact code to overcome the 8-sprite hardware limit.

**Skills taught:**
- Sprite multiplexing (8→32 sprites)
- Y-sorted sprite lists with bucket sort
- Raster interrupt timing and chaining
- Double IRQ for stable raster
- Cycle-exact timing and badline awareness
- Self-modifying IRQ handlers
- Flicker management and priority systems
- Sprite crunch bug avoidance
- Arena shooter with wave-based spawning
- Multi-sprite composite bosses
- Multiple enemy AI types
- Weapon upgrade systems
- Two-player co-op and versus modes
- SID music during heavy IRQ load
- Performance profiling and optimisation

**Why expanded:** Sprite multiplexing is THE advanced C64 technique. Games like Katakis, Turrican, and Armalyte relied on it. 256 units allows mastery of raster timing, sorted allocation, and flicker-free display.

**Detailed outline:** `/docs/curriculum/templates/full-game-outline-c64-sprite-storm.md`

---

### Game 10: Raster Rider
**Units:** 256 (16 phases)
**Concept:** Outrun-style pseudo-3D racing using advanced raster techniques. Master per-scanline colour manipulation, road perspective mathematics, sprite scaling, and create a full championship racing experience.

**Skills taught:**
- Advanced raster interrupt chains
- Per-scanline colour manipulation
- Road perspective mathematics
- Curve and hill rendering
- Sprite scaling illusion for depth
- Speed-based colour cycling
- Track data compression
- Multiple themed tracks (coastal, desert, forest, mountain, night)
- Opponent car AI and collision
- Championship mode with points
- Weather and time-of-day variants
- Ghost replay system
- SID engine sound synthesis
- Full game structure and polish

**Why expanded:** Pseudo-3D racing requires deep mastery of raster timing and road mathematics. This technique defined classic racers and teaches advanced interrupt handling.

**Detailed outline:** `/docs/curriculum/templates/full-game-outline-c64-raster-rider.md`

---

### Game 11: Dungeon Crawl
**Units:** 256 (16 phases)
**Concept:** Zelda-style top-down adventure with inventory, NPCs, quests, and combat. Introduces C64 disk I/O for save games. Multi-room dungeon exploration with puzzles and boss encounters.

**Skills taught:**
- Multi-room map architecture
- Room transitions and state persistence
- Full inventory system with equipment
- NPC dialogue and branching conversations
- Quest framework with objectives
- Melee and ranged combat
- Environmental puzzles (blocks, switches, bombs)
- Multiple dungeon themes
- Boss encounters
- **Kernal disk I/O routines**
- **Disk save/load system**
- **D64 disk image creation**
- Password backup for non-disk users
- Second quest/New Game+ mode
- Full game polish and release

**Why expanded:** A complete adventure game with inventory, NPCs, quests, combat, puzzles, AND disk I/O requires 256 units for proper depth and polish.

**Detailed outline:** `/docs/curriculum/templates/full-game-outline-c64-dungeon-crawl.md`

**Detailed outline:** `/docs/plans/commodore-64/game-11-dungeon-crawl.md`

---

### Game 12: Arena Fighter
**Units:** 256 (16 phases)
**Concept:** Street Fighter II-inspired one-on-one fighting game with four unique characters, special moves, combos, and tournament mode. Deep state machines and frame-perfect timing.

**Skills taught:**
- Complex animation state machines
- Hitbox/hurtbox collision system
- Frame data (startup, active, recovery frames)
- Input buffering for responsive controls
- Motion input detection (QCF, QCB, DP motions)
- Special moves with invincibility frames
- Super meter and EX moves
- Combo system with cancels and links
- Juggle mechanics with limits
- AI opponent with spacing awareness and difficulty scaling
- 4 distinct character archetypes (Shoto, Grappler, Charge, Rushdown)
- Tournament/Arcade mode
- Training mode with input display
- Two-player versus mode
- Full SID audio (hit sounds, announcer, character themes)

**Why expanded:** Fighting games require mastery of complex state machines, frame-perfect timing, input detection, and complete character implementation. Four distinct archetypes plus AI and modes requires 256 units.

**Detailed outline:** `/docs/curriculum/templates/full-game-outline-c64-arena-fighter.md`

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

- **3.14 (2026-01-18):** Expanded Game 12 (Arena Fighter) to 256 units with fighting game mastery. Total now 2,688 units.
- **3.13 (2026-01-18):** Expanded Game 11 to 256 units. Total now 2,560 units.
- **3.12 (2026-01-18):** Expanded Game 10 (Raster Rider) to 256 units with pseudo-3D racing. Total now 2,432 units.
- **3.11 (2026-01-18):** Expanded Game 9 (Sprite Storm) to 256 units with sprite multiplexing mastery. Total now 2,240 units.
- **3.10 (2026-01-18):** Expanded Game 8 (Night Raid) to 128 units with Scramble-style gameplay, boss battles, and power-ups. Total now 2,048 units.
- **3.9 (2026-01-18):** Expanded Game 7 (Scroll Runner) to 128 units with VIC-II hardware scrolling, double buffering, and parallax. Total now 1,984 units.
- **3.8 (2026-01-18):** Expanded Game 6 (SID Symphony) to 128 units with deep SID exploration and rhythm gameplay. Total now 1,920 units.
- **3.7 (2026-01-18):** Replaced Game 5 Invader Wave with Catacombs (flip-screen exploration), expanded to 128 units. Total now 1,856 units.
- **3.6 (2026-01-18):** Expanded Game 4 (Brick Basher) to 128 units with full breakout polish. Total now 1,792 units.
- **3.5 (2026-01-18):** Expanded Game 3 (Maze Raider) to 128 units with ghost AI personalities and pathfinding. Total now 1,728 units.
- **3.4 (2026-01-18):** Expanded Game 2 (Platform Panic) to 128 units for full polish. Total now 1,664 units.
- **3.3 (2026-01-18):** Reordered games per skill tree analysis. Platform Panic now Game 2 (introduces gravity/tiles). SID Symphony moved to Game 6 (requires keyboard + timing skills). See `/docs/curriculum/SKILL-TREES.md`.
- **3.2 (2026-01-18):** Restructured Game 1. Starfield (shooter) now first game at 128 units for immediate engagement. Total now 1,600 units.
- **3.1 (2026-01-07):** Added optional enhancement versions section (MEGA65, REU). Updated BASIC gateway reference to 512-unit curriculum.
- **3.0 (2025-01-07):** Expanded to 1,536 units. Games 1-10 at 64 units, Games 11-15 at 128 units, Game 16 at 256 units. Added disk I/O, fast loaders, turbo tape.
- **2.0 (2025-11-25):** Complete rewrite. Replaced phases/tiers/lessons with games model.
- **1.0 (2025-01-15):** Original 4,096-lesson curriculum.
