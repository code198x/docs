# Nintendo NES Curriculum

**Platform:** Nintendo Entertainment System (NES/Famicom)
**Language:** 6502 Assembly (no BASIC gateway)
**Killer Feature:** PPU (Picture Processing Unit) - tile-based graphics mastery
**Games:** 16
**Total Units:** 3,328

---

## Overview

The NES curriculum teaches 6502 assembly programming through 16 complete games. The sequence begins with the PPU - the heart of NES development - and progresses through scrolling, Metroidvania design, and advanced mapper techniques until learners can produce commercial-quality cartridge games.

The NES is fundamentally tile-based. Everything is 8×8 tiles: backgrounds built from pattern tables arranged in nametables, sprites limited to 64 objects with 8 per scanline. Understanding the PPU is understanding the NES. This curriculum embraces that architecture, teaching learners to think in tiles.

By the final game, learners will have skills matching professional NES developers of the late 1980s and early 1990s.

---

## Curriculum Structure

| Phase | Games | Units Each | Total |
|-------|-------|------------|-------|
| Foundation (shooter, platformer, breakout, maze, exploration, snake, puzzle, scrolling) | 1-8 | 128 | 1,024 |
| Intermediate | 9-10 | 256 | 512 |
| Advanced | 11-13 | 256 | 768 |
| Advanced | 14 | 256 | 256 |
| Expert | 15 | 512 | 512 |
| Capstone | 16 | 256 | 256 |
| **Total** | **16** | | **3,328** |

Each game is divided into 4 phases (foundation games) or 8 phases (advanced/Games 1-2) or 16 phases (capstone), with each phase containing 16 units.

---

## Game Sequence

### Foundation Games

#### Game 1: Stellar Barrage
**Units:** 128 (8 phases)
**Concept:** Fixed-screen space shooter. Player ship versus descending enemy waves. Immediate engagement from Unit 1.

**Skills taught:**
- PPU setup (pattern tables, nametables, palettes)
- Background tiles (the playfield)
- Sprites (player, enemies, bullets via OAM)
- Controller input
- Projectile spawning and management
- Enemy formations and patterns
- Multiple collision types (bullet-enemy, enemy-player)
- Wave progression
- Score tracking
- APU sound basics
- Sprite management under pressure (8-per-scanline limit)
- Sprite flickering techniques

**Why first:** A shooter gets something playable on screen immediately. Learners control a ship from Unit 2, shoot from Unit 3. The PPU is learned through building a real game.

**Detailed outline:** `/docs/curriculum/templates/full-game-outline-nes-stellar-barrage.md`

---

#### Game 2: Crate Escape
**Units:** 128 (8 phases)
**Concept:** Single-screen platformer polished to commercial quality. Jump between platforms, avoid hazards, collect items, defeat enemies, reach the exit.

**Skills taught:**
- Gravity and jump physics (with variable height, coyote time)
- Tile-based collision (the NES way)
- Metatile level design
- Player animation states
- Hazards (spikes, enemies, conveyors, collapsing platforms)
- Moving platforms (horizontal, vertical)
- Ladders and collectibles
- Full APU music and sound
- High scores, passwords, boss level
- 20 levels of varied design

**Why here:** After shooting, platforming introduces gravity and tile collision - fundamental NES skills. 128 units allows proper exploration of feel, level design, and polish.

**Detailed outline:** `/docs/curriculum/templates/full-game-outline-nes-crate-escape.md`

---

#### Game 3: Fracture Point
**Units:** 128 (8 phases)
**Concept:** Breakout clone polished to commercial quality. Paddle, ball, bricks - with fixed-point physics, power-ups, and 20 varied levels. The tension builds to the fracture point.

**Skills taught:**
- Ball physics with fixed-point maths (smooth sub-pixel movement)
- Background tile modification (bricks disappear from nametable)
- Paddle angle control (hit position affects bounce)
- Multiple brick types (hard, unbreakable, explosive)
- Power-up system (extend, multi-ball, laser, catch)
- APU sound design for impacts
- Level design variety
- Attribute table for brick colours
- Score multipliers and combos
- Full polish (20 levels, music, high scores)

**Why here:** After sprites in Games 1-2, learners master dynamic backgrounds. Ball physics teaches fixed-point maths before applying it to more complex games.

**Detailed outline:** `/docs/curriculum/templates/full-game-outline-nes-fracture-point.md`

---

#### Game 4: Pellet Panic
**Units:** 128 (8 phases)
**Concept:** Pac-Man style maze game polished to commercial quality. Collect all pellets, avoid ghosts, grab power pills to turn the tables. Frantic, panic-inducing energy with four distinct ghost personalities.

**Skills taught:**
- Tile-based maze structure (background tiles)
- Constrained corridor movement with smooth cornering
- Ghost AI personalities (Blinky chase, Pinky ambush, Inky flank, Clyde random)
- Chase/scatter mode switching on timers
- Frightened mode with ghost-eating chains
- Power-up state changes
- Screen wrap-around tunnels
- Speed and difficulty progression
- Bonus fruit per level
- Full APU audio (waka-waka, siren, death)
- High scores, demo mode, intermissions

**Why here:** After physics games, AI personalities bring the maze to life. 128 units allows four distinct ghost behaviours.

**Detailed outline:** `/docs/curriculum/templates/full-game-outline-nes-pellet-panic.md`

---

#### Game 5: Crypt Crawler
**Units:** 128 (8 phases)
**Concept:** Flip-screen top-down dungeon exploration polished to commercial quality. Navigate interconnected rooms, collect keys and treasures, defeat monsters, find the exit. The ancestor to Zelda-style adventure games.

**Skills taught:**
- Room data structures and metatile system
- Screen transitions with PPU updates
- Persistent state across rooms
- Inventory system (keys, potions, weapons)
- HUD display for health/items
- Enemy AI (patrol, chase, wall-aware)
- Melee combat with sword attack
- Multiple enemy types including ranged
- Coloured keys and locked doors
- Push blocks and puzzle elements
- Multiple dungeon floors
- Boss encounters
- Password/save system
- Full APU audio (music and effects)

**Why here:** After single-screen games, learners manage multi-room worlds with persistent state - foundation for adventure games.

**Detailed outline:** `/docs/curriculum/templates/full-game-outline-nes-crypt-crawler.md`

---

#### Game 6: Fangs for the Memory
**Units:** 128 (8 phases)
**Concept:** Snake game with a vampire bat theme polished to commercial quality. Eat food, grow longer, don't hit yourself. The ring buffer data structure taught through gameplay.

**Skills taught:**
- Ring buffer data structure (fundamental programming pattern)
- Grid-based movement with timing control
- Self-collision detection
- Food spawning and variety
- Speed progression as snake grows
- Input buffering for direction changes
- Multiple game modes (classic, levels, survival, time attack)
- Level obstacles and mazes
- Power-ups (speed, invincibility)
- Smooth animation between tiles
- Two-player and versus modes
- Full APU audio (music and effects)
- Password system for progress

**Why here:** After dungeon exploration, this simpler game teaches an important data structure while letting concepts consolidate. The ring buffer is used throughout game and audio programming.

**Detailed outline:** `/docs/curriculum/templates/full-game-outline-nes-fangs-for-the-memory.md`

---

#### Game 7: Gridlock
**Units:** 128 (8 phases)
**Concept:** Falling blocks puzzle polished to commercial quality. Tetris-style rotation, stacking, and line clearing. Fill up the grid until you're locked.

**Skills taught:**
- Piece rotation mathematics (4 orientations)
- Seven tetromino definitions
- Wall kick mechanics
- Falling on a timer with lock delay
- Grid collision (can piece fit?)
- Line detection and clearing
- Multiple line clear bonuses (Tetris)
- Next piece preview (extended queue)
- Hold piece feature
- Ghost piece projection
- T-spin detection and scoring
- Back-to-back bonuses
- 7-bag randomiser
- Multiple game modes (Marathon, Sprint, Ultra)
- Two-player versus with garbage lines
- Visual themes
- Challenge mode with preset scenarios
- Grade/ranking system
- APU music with tempo variation

**Why here:** The falling blocks puzzle is a classic that teaches rotation matrices, grid algorithms, and polished game feel. 128 units allows a feature-complete puzzle game with multiple modes.

**Detailed outline:** `/docs/curriculum/templates/full-game-outline-nes-gridlock.md`

---

#### Game 8: Pixel Plains
**Units:** 128 (8 phases)
**Concept:** Side-scrolling platformer polished to commercial quality. The NES's signature genre - take Crate Escape's mechanics and expand them into a larger, scrolling world with multiple themed areas, boss battles, and secrets.

**Skills taught:**
- NES hardware scrolling fundamentals
- PPUSCROLL and nametable management
- Camera following with smooth tracking
- Metatile-based level design
- Large level data structures with compression
- Scrolling collision detection
- Enemies that spawn and despawn with camera
- Moving platforms and environmental hazards
- Boss battles with multi-sprite bosses
- Multiple world themes (grass, cave, sky, castle)
- World map navigation
- Power-up and health systems
- Checkpoint and lives system
- Secret exits and bonus levels
- Time limit mechanics
- Water/swimming areas
- Save/password system
- APU music with level themes
- Demo/attract mode

**Why here:** The NES has hardware scrolling - this is where it shines. Super Mario Bros. territory. Building on Crate Escape's single-screen platforming, learners create their first scrolling world.

**Detailed outline:** `/docs/curriculum/templates/full-game-outline-nes-pixel-plains.md`

---

#### Game 9: Ion Trail
**Units:** 256 (16 phases)
**Concept:** Definitive NES horizontal shooter in Gradius style. Power-up progression system, trailing options, multiple weapon types, and epic boss encounters. Master the shmup genre on Nintendo's hardware.

**Skills taught:**
- Horizontal scrolling for shooters
- Gradius-style power meter system
- Option drone following algorithm (position history buffer)
- Multiple weapon types with upgrade levels
- Charge shot mechanics
- Complex enemy AI and formations
- Bullet pattern design (danmaku lite)
- Five complete stages with unique themes
- Five epic multi-phase boss battles
- Rank system (adaptive difficulty)
- Sprite management for high bullet counts
- Sprite 0 split for fixed HUD
- APU sound effects and music
- Multiple game modes (Normal, Boss Rush, Score Attack)
- Two-player co-op mode
- Second loop with true ending
- Battery save for high scores

**Why expanded:** A full Gradius-style shmup with options, weapon levels, and complex bosses requires deep coverage. The power-up system alone is a significant undertaking. 256 units allows a complete, polished shooter.

**Detailed outline:** `/docs/curriculum/templates/full-game-outline-nes-ion-trail.md`

---

#### Game 10: Arena Assault
**Units:** 256 (16 phases)
**Concept:** Foundation capstone - intense arena combat integrating ALL skills learned so far. 8-way movement and shooting, heavy sprite management, wave survival, bosses, and commercial-quality polish.

**Skills taught:**
- Integration of all foundation skills
- 8-way movement and shooting
- Sprite priority and flicker management
- Wave-based survival design
- Multiple enemy types with varied AI
- Wave composition and difficulty scaling
- Full power-up system
- Multiple weapon types (machine gun, shotgun, laser, homing)
- Shield and health systems
- Four boss encounters
- Multiple arenas with unique mechanics
- Arena hazards and teleporters
- Two-player co-op and versus modes
- Score attack and endless modes
- APU sound and music
- Statistics and achievements
- Battery save for high scores

**Why expanded:** As the foundation capstone, Arena Assault must demonstrate mastery of all techniques. 256 units allows a complete, polished arena shooter that proves readiness for advanced games.

**Detailed outline:** `/docs/curriculum/templates/full-game-outline-nes-arena-assault.md`

---

### Advanced Games

#### Game 11: Thunder Run
**Units:** 256 (16 phases)
**Concept:** 1942-style vertical shooter with formations, bullet patterns, and epic bosses. Introduces MMC1 mapper for expanded ROM and CHR banking.

**Skills taught:**
- Vertical scrolling mechanics
- Row-based level streaming
- Formation enemy patterns (V, line, circle)
- Bullet patterns (aimed, spread, spiral)
- Ground and air targets
- Five complete stages
- Five multi-phase bosses
- Multiple power-up types
- Weapon upgrade system
- **MMC1 mapper fundamentals**
- **Serial register writing**
- **CHR bank switching**
- **PRG bank switching**
- **Multiple tilesets per level**
- Rank/difficulty scaling
- Two-player alternating
- Second loop with true ending

**Why expanded:** A full vertical shmup plus MMC1 mapper mastery requires 256 units. Mapper knowledge is essential for larger NES games.

**Detailed outline:** `/docs/curriculum/templates/full-game-outline-nes-thunder-run.md`

---

#### Game 12: Iron Assault
**Units:** 256 (16 phases)
**Concept:** Contra-style run 'n' gun action with 8-way shooting, weapon power-ups, and intense boss battles. Two-player cooperative mode for maximum action.

**Skills taught:**
- Platformer + shooter hybrid mechanics
- 8-way directional shooting with arm sprite rotation
- Run and gun (shoot while moving/jumping)
- Crouching and prone aim positions
- Weapon system with 6 types (Rifle, Spread S, Laser L, Machine Gun M, Fire Ball F, Crush C)
- Weapon pickups with flying capsules
- Bullet pool management
- Enemy variety (Soldier, Sniper, Turret, Runner, Grenadier, Jetpack, Shield)
- Large boss assembly with multi-sprite composition
- Boss weak points and health bars
- 5 complete stages (Jungle, Base Exterior, Waterfall vertical, Base Interior, Alien Hive)
- Horizontal and vertical scrolling sections
- Top-down base sections
- Section transitions
- Two-player cooperative with shared camera
- Sprite limit management with flicker
- Individual/shared lives options
- Difficulty modes with one-hit death option
- Continue and checkpoint systems
- APU music and sound effects
- Demo/attract mode

**Why expanded:** A full Contra-style game with 8-way shooting, 6 weapons, 5 stages, epic bosses, AND two-player co-op with sprite management requires 256 units.

**Detailed outline:** `/docs/curriculum/templates/full-game-outline-nes-iron-assault.md`

---

#### Game 13: Pavement Justice
**Units:** 256 (16 phases)
**Concept:** Double Dragon/River City Ransom-style brawler with Y-depth sorting, combo systems, weapon pickups, and two-player co-op. Vigilante action cleaning up the streets.

**Skills taught:**
- Y-axis depth sorting with OAM ordering
- Large metasprite characters
- Melee combat (punches, kicks, grabs, throws)
- Combo system with chains and juggles
- Attack slots and enemy AI coordination
- Multiple enemy types (Punk, Thug, Knife, Big, Acrobat)
- Weapon pickups (Bat, Knife, Chain, Trash can)
- 5 complete stages with unique tilesets
- 5 boss encounters with patterns
- Multiple playable characters
- Two-player cooperative mode
- Sprite limit management and flicker distribution
- Health pickups and food items
- APU music and sound effects
- Demo/attract mode

**Why expanded:** A complete beat 'em up with Y-sorting, combos, enemy coordination, 5 stages, 5 bosses, AND two-player co-op with sprite management requires 256 units.

**Detailed outline:** `/docs/curriculum/templates/full-game-outline-nes-pavement-justice.md`

---

#### Game 14: Tarmac Terror
**Units:** 256 (16 phases)
**Concept:** Outrun-style racing with road rushing toward you. Dodge traffic, navigate curves, survive the terror of the tarmac. Master perspective mathematics and sprite scaling on NES hardware.

**Skills taught:**
- Pseudo-3D road rendering (perspective mathematics)
- Road width calculation per scanline
- Horizon line and ground plane
- Road stripes with animation
- Road curves (left and right offset)
- Road hills (uphill and downhill)
- Combined curve + hill rendering
- Sprite scaling simulation (pre-scaled sprites)
- Billboard objects (trees, signs, buildings)
- Player car with steering lean frames
- Acceleration, braking, and speed limits
- Gear system with shifting
- Curve physics (centrifugal force)
- Off-road penalty and crash detection
- Traffic system with multiple car types
- Traffic collision and crash sequence
- Checkpoint time extension
- 5 themed tracks (Coastal, City, Desert, Forest, Mountain)
- Branching path route selection
- Championship mode with points
- Time trial with ghost replay
- **Split-screen two-player mode**
- **Sprite 0 for screen split**
- APU engine sound synthesis
- Full APU music

**Why expanded:** Pseudo-3D racing with perspective mathematics, curves, hills, traffic, 5 tracks, AND split-screen multiplayer requires 256 units for NES implementation.

**Detailed outline:** `/docs/curriculum/templates/full-game-outline-nes-tarmac-terror.md`

---

#### Game 15: Echoes of Eponium
**Units:** 512 (32 phases)
**Concept:** Full Metroidvania epic. Explore the mysterious ruins of Eponium across 5 interconnected regions, gaining abilities that unlock new areas. Connected world, ability-gating, backtracking, upgrades, and multiple endings. The ultimate NES exploration game.

**Skills taught:**
- MMC3 mapper with IRQ scanline counter
- Large connected world map (5 regions × 40+ rooms)
- Non-linear progression with sequence breaking potential
- Ability-gating design (8+ abilities unlock areas)
- Movement abilities (wall jump, double jump, dash, morph)
- Combat abilities (charge beam, missiles, bombs)
- Backtracking and shortcuts
- Region-specific visual themes (ruins, caves, water, fire, sky)
- CHR bank switching for varied tilesets
- Parallax scrolling with IRQ timing
- Player progression system (health, energy, weapon upgrades)
- Battery-backed save system (SRAM)
- Multiple save slots
- Boss encounters that grant abilities (8 major bosses)
- Mini-bosses and optional challenges
- Environmental hazards per region
- Hidden items and expansions
- Map system with fog of war
- Percentage completion tracking
- Multiple endings based on completion
- Time attack and speedrun modes
- Advanced APU music with region themes
- DMC sample integration
- World design and pacing for 8+ hours of content

**Why 512 units:** Full Metroidvania requires extensive world building: 5 regions, 8+ abilities, ability-gating design, battery-backed saves, multiple endings, and careful pacing for non-linear exploration.

**Detailed outline:** `/docs/curriculum/templates/full-game-outline-nes-echoes-of-eponium.md`

---

### Capstone Game (256 Units)

#### Game 16: Requiem for a Mapper
**Units:** 256 (16 phases)
**Concept:** Action-adventure epic. The capstone project combining everything learnt into a commercial-quality game. The title honours the bank-switching magic that made larger NES games possible.

**Skills taught:**
- Large world design
- Multiple gameplay mechanics integrated
- Story and progression elements
- Advanced MMC3 usage
- IRQ-based effects (scanline counting)
- Save system (battery backup)
- Polish and presentation
- Professional production values
- All previous techniques at mastery level
- ROM image creation and distribution

**Why last:** The curriculum ends with learners demonstrating full command of the machine. Every NES developer knows the importance of mappers - now they've mastered them.

---

## Skill Progression

### Foundation Phase (Games 1-10)

| Games | Focus | Skills |
|-------|-------|--------|
| 1-2 | PPU basics | Nametables, sprites, platforming |
| 3-4 | Object management | Projectiles, physics, collision |
| 5-6 | AI and exploration | Enemy behaviour, multi-room |
| 7-8 | Data structures | Ring buffers, grids, rotation |
| 9-10 | Hardware scrolling | Horizontal scroll, camera |

### Advanced Phase (Games 11-15)

| Games | Focus | Skills |
|-------|-------|--------|
| 11 | Vertical scrolling | Different scroll direction, mappers |
| 12 | Run'n'gun | Multi-directional combat, co-op |
| 13 | Beat 'em up | Y-depth, melee combat |
| 14 | Pseudo-3D | Road rendering, scaling |
| 15 | Metroidvania | Connected worlds, ability gates |

### Capstone (Game 16)

Full integration of all skills into a commercial-quality game demonstrating complete platform mastery.

---

## Mapper Progression

| Game | Mapper | Capability |
|------|--------|------------|
| 1-10 | NROM | 32KB PRG, 8KB CHR - no banking |
| 11-12 | MMC1 | 256KB PRG, 128KB CHR - bank switching |
| 13-14 | MMC1 | Advanced banking techniques |
| 15 | MMC3 | Scanline counter, enhanced banking |
| 16 | MMC3 | Full mapper mastery, IRQ effects |

---

## Distribution Skills

| Game | Distribution Skill |
|------|-------------------|
| 1-10 | Basic iNES ROM creation |
| 11-14 | Mapper header configuration |
| 15 | Save/password systems |
| 16 | Battery backup, PRG-RAM, complete cartridge specification |

---

## Platform Context

### Hardware

- **CPU:** Ricoh 2A03 (MOS 6502 core) @ 1.79 MHz (NTSC) / 1.66 MHz (PAL)
- **RAM:** 2KB work RAM, 2KB video RAM
- **Display:** 256×240 pixels (NTSC), 256×224 visible
- **Colours:** 52 colours in palette, 25 on-screen (4 background palettes + 4 sprite palettes, 4 colours each including shared background)
- **Sound:** APU - 2 pulse, 1 triangle, 1 noise, 1 DMC (sample) channel
- **Storage:** Cartridge with ROM, optional battery backup

### The PPU (Picture Processing Unit)

The heart of NES graphics:

- **Pattern Tables** - Two 4KB tables holding 8×8 pixel tile definitions (256 tiles each for background and sprites)
- **Nametables** - Four 1KB screens defining which tiles appear where (32×30 tiles visible)
- **Attribute Tables** - Define which palette each 16×16 pixel area uses
- **OAM (Object Attribute Memory)** - 256 bytes defining 64 sprites (position, tile, palette, flip)

### The 8-Sprite Limit

Only 8 sprites can appear on a single scanline. More causes flickering. Managing this limit is a core NES skill.

### The APU (Audio Processing Unit)

Five channels of distinctive 8-bit sound:
- **Pulse 1 & 2** - Square waves with duty cycle control (melodies, harmony)
- **Triangle** - Pure triangle wave (bass, smooth tones)
- **Noise** - White noise generator (drums, percussion, effects)
- **DMC** - Delta modulation for samples (voice, complex sounds)

### Mappers

Bank-switching hardware on cartridges enabling larger games:
- **NROM** - No mapper, 32KB PRG + 8KB CHR (early games)
- **MMC1** - Bank switching up to 256KB PRG (Zelda, Metroid)
- **MMC3** - Advanced features, scanline counter (Super Mario Bros. 3)

The curriculum progresses from NROM-compatible basics to MMC3 mastery.

---

## Era Comparison

| Games | Era Equivalent | Commercial Examples |
|-------|----------------|---------------------|
| 1-4 | 1983-1985 | Donkey Kong, Excitebike |
| 5-8 | 1985-1986 | Pac-Man, Ice Climber |
| 9-10 | 1986-1987 | Super Mario Bros., Gradius |
| 11-12 | 1987-1988 | Contra, 1943 |
| 13-14 | 1988-1989 | Double Dragon, Rad Racer |
| 15 | 1989-1991 | Metroid, Castlevania |
| 16 | 1991-1994 | Kirby's Adventure, Shatterhand |

By Game 16, learners produce work comparable to late-era commercial releases.

---

## Post-Capstone: Audio Expansion

The NES had several cartridge mappers with built-in audio expansion chips, adding extra sound channels beyond the standard 2A03. These are highly prized for homebrew development.

### Game 17: VRC6 Symphony (64 units)
Audio expansion using Konami's VRC6 mapper (Castlevania III, Akumajou Densetsu).
- Two additional pulse channels
- One sawtooth channel
- Enhanced music composition
- Mapper programming

### Game 18: MMC5 Mastery (64 units)
Advanced mapper techniques using Nintendo's MMC5.
- Extended nametables
- 8×8 attribute mode
- Extra sound channel
- Split-screen effects

These expansion games target learners interested in pushing beyond standard NES capabilities, particularly for enhanced homebrew releases.

See `/docs/plans/future-expansion-tracks.md` for full details.

---

## Version History

- **3.17 (2026-01-18):** Expanded Game 15 (Echoes of Eponium) to 512 units with full Metroidvania, MMC3 mapper, and battery-backed saves. Total now 3,328 units.
- **3.16 (2026-01-18):** Expanded Game 14 (Tarmac Terror) to 256 units with Outrun-style pseudo-3D racing. Total now 2,944 units.
- **3.15 (2026-01-18):** Expanded Game 13 (Pavement Justice) to 256 units with Y-depth sorting and beat 'em up mechanics. Total now 2,816 units.
- **3.14 (2026-01-18):** Expanded Game 12 (Iron Assault) to 256 units with run 'n' gun mastery. Total now 2,688 units.
- **3.13 (2026-01-18):** Expanded Game 11 to 256 units. Total now 2,560 units.
- **3.12 (2026-01-18):** Expanded Game 10 (Arena Assault) to 256 units as foundation capstone. Total now 2,432 units.
- **3.11 (2026-01-18):** Expanded Game 9 (Ion Trail) to 256 units with Gradius-style power system and options. Total now 2,240 units.
- **3.10 (2026-01-18):** Expanded Game 8 (Pixel Plains) to 128 units with NES scrolling, world map, and boss battles. Total now 2,048 units.
- **3.9 (2026-01-18):** Expanded Game 7 (Gridlock) to 128 units with rotation matrices, multiple modes, and two-player versus. Total now 1,984 units.
- **3.8 (2026-01-18):** Expanded Game 6 (Fangs for the Memory) to 128 units with ring buffer teaching. Total now 1,920 units.
- **3.7 (2026-01-18):** Expanded Game 5 (Crypt Crawler) to 128 units with full Zelda-style exploration. Total now 1,856 units.
- **3.6 (2026-01-18):** Expanded Game 4 (Pellet Panic) to 128 units with four distinct ghost AI personalities. Total now 1,792 units.
- **3.5 (2026-01-18):** Expanded Game 3 (Fracture Point) to 128 units with full breakout polish and power-ups. Total now 1,728 units.
- **3.4 (2026-01-18):** Expanded Game 2 (Crate Escape) to 128 units for full platformer polish. Total now 1,664 units.
- **3.3 (2026-01-18):** Reordered games per skill tree analysis. Removed Neon Nexus (redundant with Stellar Barrage). Crate Escape now Game 2. Added Arena Assault as Game 10 (foundation capstone). See `/docs/curriculum/SKILL-TREES.md`.
- **3.2 (2026-01-18):** Restructured Game 1. Stellar Barrage (shooter) now first game at 128 units for immediate engagement. Total now 1,600 units.
- **3.1 (2026-01-07):** Added post-capstone audio expansion games (VRC6, MMC5).
- **3.0 (2025-01-07):** Restructured to 1,536 units (64/128/256 scaling) matching C64 and ZX Spectrum curricula.
- **2.0 (2025-11-26):** Complete rewrite. Replaced phases/tiers/lessons with games model.
- **1.0 (2025-01-15):** Original curriculum.
