# Nintendo NES Curriculum

**Platform:** Nintendo Entertainment System (NES/Famicom)
**Language:** 6502 Assembly (no BASIC gateway)
**Killer Feature:** PPU (Picture Processing Unit) - tile-based graphics mastery
**Games:** 16
**Total Units:** 1,600

---

## Overview

The NES curriculum teaches 6502 assembly programming through 16 complete games. The sequence begins with the PPU - the heart of NES development - and progresses through scrolling, Metroidvania design, and advanced mapper techniques until learners can produce commercial-quality cartridge games.

The NES is fundamentally tile-based. Everything is 8×8 tiles: backgrounds built from pattern tables arranged in nametables, sprites limited to 64 objects with 8 per scanline. Understanding the PPU is understanding the NES. This curriculum embraces that architecture, teaching learners to think in tiles.

By the final game, learners will have skills matching professional NES developers of the late 1980s and early 1990s.

---

## Curriculum Structure

| Phase | Games | Units Each | Total |
|-------|-------|------------|-------|
| Foundation (shooter) | 1 | 128 | 128 |
| Foundation | 2-10 | 64 | 576 |
| Advanced | 11-15 | 128 | 640 |
| Capstone | 16 | 256 | 256 |
| **Total** | **16** | | **1,600** |

Each game is divided into 4 phases (foundation games) or 8 phases (advanced/Game 1) or 16 phases (capstone), with each phase containing 16 units.

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
**Units:** 64 (4 phases)
**Concept:** Single-screen platformer. Jump between platforms in a warehouse setting, avoid hazards, reach the exit. Crates as platforms.

**Skills taught:**
- Gravity and falling
- Jump physics (impulse, arc, landing)
- Platform collision detection (tile-based)
- Player animation (walk cycle, jump frame)
- Hazards and enemies
- Level completion logic
- Multiple levels

**Why here:** After shooting, platforming introduces gravity physics and tile collision - fundamental skills for NES games.

---

#### Game 3: Fracture Point
**Units:** 64 (4 phases)
**Concept:** Breakout clone. Paddle, ball, bricks. The tension builds to the breaking point.

**Skills taught:**
- Ball physics (velocity, angles)
- Paddle control
- Reflection/bounce mechanics
- Brick destruction (updating background tiles)
- APU sound design
- Score and lives
- Power-up bricks

---

#### Game 4: Pellet Panic
**Units:** 64 (4 phases)
**Concept:** Pac-Man style maze game. Collect pellets, avoid ghosts, power pills turn the tables. Frantic energy.

**Skills taught:**
- Tile-based maze structure
- Constrained corridor movement
- Enemy AI with personality
- Power-ups that change game state
- Wrap-around screen edges
- Speed and difficulty progression
- Ghost scatter/chase modes

---

#### Game 5: Crypt Crawler
**Units:** 64 (4 phases)
**Concept:** Flip-screen top-down exploration. Navigate dungeon rooms, collect items, avoid enemies. The ancestor to Zelda-style games.

**Skills taught:**
- 4-way (or 8-way) movement
- Room data structures
- Screen transitions
- Persistent state across rooms
- Simple inventory (keys, items)
- Enemies with chase behaviour
- Key/door mechanics

---

#### Game 6: Fangs for the Memory
**Units:** 64 (4 phases)
**Concept:** Snake game with a pun. Eat food, grow longer, don't hit yourself.

**Skills taught:**
- Grid-based movement
- Growing entity management (ring buffer)
- Self-collision detection
- Food spawning
- Increasing difficulty through length
- Tight game loop
- Multiple game modes

---

#### Game 7: Gridlock
**Units:** 64 (4 phases)
**Concept:** Falling blocks puzzle. Tetris-style rotation, stacking, and line clearing. Fill up the grid until you're locked.

**Skills taught:**
- Piece rotation (4 orientations)
- Falling on a timer
- Grid collision (can piece fit?)
- Line detection and clearing
- Next piece preview
- Speed increases over time
- Ghost piece preview

---

#### Game 8: Pixel Plains
**Units:** 64 (4 phases)
**Concept:** Side-scrolling platformer. The NES's signature genre - Crate Escape's mechanics in a larger, scrolling world.

**Skills taught:**
- Hardware scrolling fundamentals
- Scroll registers and nametable management
- Camera following player
- Large level data structures
- Scrolling collision detection
- Enemies in scrolling world

**Why here:** The NES has hardware scrolling - this is where it shines. Super Mario Bros. territory.

---

#### Game 9: Ion Trail
**Units:** 64 (4 phases)
**Concept:** Side-scrolling shooter. Gradius territory - horizontal scroll, shoot enemies, navigate terrain. Leave a trail of ions in your wake.

**Skills taught:**
- Horizontal scrolling for shooting game
- Player in scrolling playfield
- Projectiles in scrolling world
- Enemy waves and patterns
- Terrain collision
- Power-ups and weapon upgrades

---

#### Game 10: Arena Assault
**Units:** 64 (4 phases)
**Concept:** Top-down arena shooter. Enemies spawn from all directions, survive waves, collect power-ups. Tests all foundation skills before advanced games.

**Skills taught:**
- Integration of all foundation skills
- 8-way movement and shooting
- Heavy sprite management (approaching limits)
- Wave-based survival
- Multiple weapon types
- Boss encounters (foundation-level)
- Score attack design
- Polish and game feel refinement

**Why here:** Capstone of foundation phase. Combines shooting, collision, AI, and sprite management. Prepares learners for advanced techniques.

---

### Advanced Games (128 Units Each)

#### Game 11: Thunder Run
**Units:** 128 (8 phases)
**Concept:** Vertical scrolling shooter. 1942-style planes and formations. The thunder of engines and gunfire.

**Skills taught:**
- Vertical scrolling (new direction)
- Formation enemy patterns
- Bullet patterns (enemy fire)
- Ground and air targets
- Power-up collection
- Boss encounters
- MMC1 mapper basics
- Extended CHR banks

---

#### Game 12: Iron Assault
**Units:** 128 (8 phases)
**Concept:** Run 'n' gun action. Contra-style platforming with multi-directional shooting. Heavy metal assault.

**Skills taught:**
- Platformer physics with shooting
- Multi-directional firing (8-way)
- Shooting while moving/jumping
- Enemies that shoot back
- Weapon power-ups
- Boss encounters
- Two-player cooperative
- Advanced sprite management

---

#### Game 13: Pavement Justice
**Units:** 128 (8 phases)
**Concept:** Side-scrolling beat 'em up. Walk right, punch enemies, clean up the streets. Vigilante action with Y-depth sorting.

**Skills taught:**
- Y-axis depth sorting
- Melee combat mechanics
- Combo systems
- Multiple enemy management
- Health and damage systems
- Walking "into" the screen
- Stage progression
- Boss battles

---

#### Game 14: Tarmac Terror
**Units:** 128 (8 phases)
**Concept:** Pseudo-3D racing. Road rushing toward you, dodge traffic, survive the terror of the tarmac.

**Skills taught:**
- Pseudo-3D road rendering
- Sprite scaling simulation
- Speed variation (accelerate, brake)
- Obstacle spawning
- Collision at speed
- Road curves and hills
- Distance-based scoring
- Split-screen two-player

---

#### Game 15: Echoes of Eponium
**Units:** 128 (8 phases)
**Concept:** Metroidvania. Connected world, ability-gating, backtracking, upgrades. Explore the mysterious ruins of Eponium, where echoes of the past guide your way.

**Skills taught:**
- Large connected world map
- Non-linear progression
- Ability-gating (new powers unlock new areas)
- Backtracking and exploration
- Player upgrades and progression
- Save/password system
- Boss encounters that grant abilities
- World design and pacing
- MMC3 mapper features

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

- **3.3 (2026-01-18):** Reordered games per skill tree analysis. Removed Neon Nexus (redundant with Stellar Barrage). Crate Escape now Game 2. Added Arena Assault as Game 10 (foundation capstone). See `/docs/curriculum/SKILL-TREES.md`.
- **3.2 (2026-01-18):** Restructured Game 1. Stellar Barrage (shooter) now first game at 128 units for immediate engagement. Total now 1,600 units.
- **3.1 (2026-01-07):** Added post-capstone audio expansion games (VRC6, MMC5).
- **3.0 (2025-01-07):** Restructured to 1,536 units (64/128/256 scaling) matching C64 and ZX Spectrum curricula.
- **2.0 (2025-11-26):** Complete rewrite. Replaced phases/tiers/lessons with games model.
- **1.0 (2025-01-15):** Original curriculum.
