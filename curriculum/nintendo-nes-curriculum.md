# Nintendo NES Curriculum

**Platform:** Nintendo Entertainment System (NES/Famicom)
**Killer Feature:** PPU (Picture Processing Unit) - tile-based graphics mastery
**Games:** 16 (14 at 16 units, 2 at 32 units)
**Total Units:** 288

---

## Overview

The NES curriculum teaches 6502 assembly programming through 16 complete games. The sequence begins with the PPU - the heart of NES development - and progresses through scrolling, Metroidvania design, and advanced techniques until learners can produce commercial-quality cartridge games.

The NES is fundamentally tile-based. Everything is 8×8 tiles: backgrounds built from pattern tables arranged in nametables, sprites limited to 64 objects with 8 per scanline. Understanding the PPU is understanding the NES. This curriculum embraces that architecture, teaching learners to think in tiles.

By the final game, learners will have skills matching professional NES developers of the late 1980s and early 1990s.

---

## Game Sequence

### Game 1: Neon Nexus
**Units:** 16
**Concept:** Fixed-screen action game. Player moves around a single screen, avoids enemies, collects items. A digital/futuristic vibe that teaches PPU fundamentals.

**Skills taught:**
- PPU setup (pattern tables, nametables, palettes)
- Background tiles (the playfield)
- Sprites (player, enemies, items via OAM)
- Controller input
- Basic collision detection
- Game loop on NES

**Why first:** The PPU is the heart of NES development. This simple game touches all the fundamentals without overwhelming complexity.

---

### Game 2: Crate Escape
**Units:** 16
**Concept:** Single-screen platformer. Jump between platforms in a warehouse setting, avoid hazards, reach the exit. Crates as platforms.

**Skills taught:**
- Gravity and falling
- Jump physics (impulse, arc, landing)
- Platform collision detection
- Player animation (walk cycle, jump frame)
- Hazards and enemies
- Level completion logic

---

### Game 3: Stellar Barrage
**Units:** 16
**Concept:** Fixed-screen space shooter. Player ship versus descending enemy waves. Space Invaders territory.

**Skills taught:**
- Projectile spawning and management
- Enemy formations and patterns
- Multiple collision types (bullet-enemy, enemy-player)
- Wave progression
- Score tracking
- Sprite management under pressure (8-per-scanline limit)

---

### Game 4: Fracture Point
**Units:** 16
**Concept:** Breakout clone. Paddle, ball, bricks. The tension builds to the breaking point.

**Skills taught:**
- Ball physics (velocity, angles)
- Paddle control
- Reflection/bounce mechanics
- Brick destruction (updating background tiles)
- APU sound basics
- Score and lives

---

### Game 5: Pellet Panic
**Units:** 16
**Concept:** Pac-Man style maze game. Collect pellets, avoid ghosts, power pills turn the tables. Frantic energy.

**Skills taught:**
- Tile-based maze structure
- Constrained corridor movement
- Enemy AI with personality
- Power-ups that change game state
- Wrap-around screen edges
- Speed and difficulty progression

---

### Game 6: Crypt Crawler
**Units:** 16
**Concept:** Flip-screen top-down exploration. Navigate dungeon rooms, collect items, avoid enemies. The ancestor to Zelda-style games.

**Skills taught:**
- 4-way (or 8-way) movement
- Room data structures
- Screen transitions
- Persistent state across rooms
- Simple inventory (keys, items)
- Enemies with chase behaviour

---

### Game 7: Fangs for the Memory
**Units:** 16
**Concept:** Snake game with a pun. Eat food, grow longer, don't hit yourself.

**Skills taught:**
- Grid-based movement
- Growing entity management
- Self-collision detection
- Food spawning
- Increasing difficulty through length
- Tight game loop

---

### Game 8: Gridlock
**Units:** 16
**Concept:** Falling blocks puzzle. Tetris-style rotation, stacking, and line clearing. Fill up the grid until you're locked.

**Skills taught:**
- Piece rotation (4 orientations)
- Falling on a timer
- Grid collision (can piece fit?)
- Line detection and clearing
- Next piece preview
- Speed increases over time

---

### Game 9: Pixel Plains
**Units:** 16
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

### Game 10: Ion Trail
**Units:** 16
**Concept:** Side-scrolling shooter. Gradius territory - horizontal scroll, shoot enemies, navigate terrain. Leave a trail of ions in your wake.

**Skills taught:**
- Horizontal scrolling for shooting game
- Player in scrolling playfield
- Projectiles in scrolling world
- Enemy waves and patterns
- Terrain collision
- Power-ups and weapon upgrades

---

### Game 11: Thunder Run
**Units:** 16
**Concept:** Vertical scrolling shooter. 1942-style planes and formations. The thunder of engines and gunfire.

**Skills taught:**
- Vertical scrolling (new direction)
- Formation enemy patterns
- Bullet patterns (enemy fire)
- Ground and air targets
- Power-up collection
- Boss encounters

---

### Game 12: Iron Assault
**Units:** 16
**Concept:** Run 'n' gun action. Contra-style platforming with multi-directional shooting. Heavy metal assault.

**Skills taught:**
- Platformer physics with shooting
- Multi-directional firing
- Shooting while moving/jumping
- Enemies that shoot back
- Weapon power-ups
- Boss encounters

---

### Game 13: Pavement Justice
**Units:** 16
**Concept:** Side-scrolling beat 'em up. Walk right, punch enemies, clean up the streets. Vigilante action with Y-depth sorting.

**Skills taught:**
- Y-axis depth sorting
- Melee combat mechanics
- Multiple enemy management
- Health and damage systems
- Walking "into" the screen
- Stage progression

---

### Game 14: Tarmac Terror
**Units:** 16
**Concept:** Vertical scrolling racer. Road rushing toward you, dodge traffic, survive the terror of the tarmac.

**Skills taught:**
- Vertical scrolling (different context)
- Speed variation (accelerate, brake)
- Obstacle spawning
- Collision at speed
- Road variation
- Distance-based scoring

---

### Game 15: Echoes of Eponium
**Units:** 32
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

---

### Game 16: Requiem for a Mapper
**Units:** 32
**Concept:** Action-adventure epic. The capstone project combining everything learnt into a commercial-quality game. The title honours the bank-switching magic that made larger NES games possible.

**Skills taught:**
- Large world design
- Multiple gameplay mechanics integrated
- Story and progression elements
- Advanced mapper usage (MMC1/MMC3)
- Save system
- Polish and presentation
- Professional production values
- All previous techniques at mastery level

**Why last:** The curriculum ends with learners demonstrating full command of the machine. Every NES developer knows the importance of mappers - now they've mastered them.

---

## Skill Progression

| Games | Focus | Era Equivalent |
|-------|-------|----------------|
| 1-4 | Single-screen fundamentals, PPU basics | 1983-1985 |
| 5-8 | Grid-based games, tile mastery | 1985-1986 |
| 9-12 | Scrolling and combined mechanics | 1986-1988 |
| 13-14 | Advanced genres | 1988-1989 |
| 15-16 | Metroidvania and commercial quality | 1989-1994 |

By Game 16, learners produce work comparable to late-era commercial releases like Kirby's Adventure (1993) and Shatterhand (1991).

---

## Platform Context

**Hardware:**
- **CPU:** Ricoh 2A03 (MOS 6502 core) @ 1.79 MHz (NTSC) / 1.66 MHz (PAL)
- **RAM:** 2KB work RAM, 2KB video RAM
- **Display:** 256×240 pixels (NTSC), 256×224 visible
- **Colours:** 52 colours in palette, 25 on-screen (4 background palettes + 4 sprite palettes, 4 colours each including shared background)
- **Sound:** APU - 2 pulse, 1 triangle, 1 noise, 1 DMC (sample) channel
- **Storage:** Cartridge with ROM, optional battery backup

**The PPU (Picture Processing Unit):**

The heart of NES graphics:

- **Pattern Tables** - Two 4KB tables holding 8×8 pixel tile definitions (256 tiles each for background and sprites)
- **Nametables** - Four 1KB screens defining which tiles appear where (32×30 tiles visible)
- **Attribute Tables** - Define which palette each 16×16 pixel area uses
- **OAM (Object Attribute Memory)** - 256 bytes defining 64 sprites (position, tile, palette, flip)

**The 8-Sprite Limit:**
Only 8 sprites can appear on a single scanline. More causes flickering. Managing this limit is a core NES skill.

**The APU (Audio Processing Unit):**

Five channels of distinctive 8-bit sound:
- **Pulse 1 & 2** - Square waves with duty cycle control (melodies, harmony)
- **Triangle** - Pure triangle wave (bass, smooth tones)
- **Noise** - White noise generator (drums, percussion, effects)
- **DMC** - Delta modulation for samples (voice, complex sounds)

**Mappers:**

Bank-switching hardware on cartridges enabling larger games:
- **NROM** - No mapper, 32KB PRG + 8KB CHR (early games)
- **MMC1** - Bank switching up to 256KB PRG (Zelda, Metroid)
- **MMC3** - Advanced features, scanline counter (Super Mario Bros. 3)

The curriculum progresses from NROM-compatible basics to MMC3 mastery.

---

## Version History

- **2.0 (2025-11-26):** Complete rewrite. Replaced phases/tiers/lessons with games model.
- **1.0 (2025-01-15):** Original 4,096-lesson curriculum.
