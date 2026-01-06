# Commodore Amiga Curriculum

**Platform:** Commodore Amiga
**Killer Feature:** Custom chipset symphony (Agnus, Denise, Paula working together)
**Games:** 16 (14 at 16 units, 2 at 32 units)
**Total Units:** 288

---

## Overview

The Amiga curriculum teaches 68000 assembly programming through 16 complete games. The sequence begins by showcasing the custom chipset working as a unified system - Agnus orchestrating memory, Denise painting pixels, Paula pumping samples - and progresses through parallax scrolling, isometric projection, and advanced techniques until learners can produce commercial-quality games.

The Amiga wasn't about one killer feature. It was about the custom chips working in harmony: the Blitter accelerating graphics, the Copper synchronising effects to the display beam, Paula playing four channels of sampled audio. This curriculum teaches learners to conduct that orchestra.

By the final game, learners will have skills matching professional Amiga developers of the early 1990s.

---

## Game Sequence

### Game 1: Hop
**Units:** 16
**Concept:** Frogger-style lane crosser. Cross roads, ride logs, reach safety. A timing and navigation game that naturally exercises the entire chipset.

**Skills taught:**
- Display setup and copper list basics
- Hardware sprites (player)
- Blitter BOBs (cars, logs)
- Copper colour splits (road/water/grass)
- Paula sound effects (hop, splash, squish)
- Collision detection
- Game loop fundamentals

**Why first:** This simple game touches every custom chip without going deep on any. Learners see the chipset symphony from day one.

---

### Game 2: Salvo
**Units:** 16
**Concept:** Fixed-screen space shooter. Player ship versus enemy waves. Shoot, dodge, survive.

**Skills taught:**
- Player-controlled shooting
- Projectile spawning and management
- Enemy formations and patterns
- Multiple collision types (bullet-enemy, enemy-player)
- Wave progression
- Score tracking

---

### Game 3: Ricochet
**Units:** 16
**Concept:** Breakout clone. Paddle, ball, bricks. The Amiga makes this gorgeous with smooth movement, copper gradients, and sampled sounds.

**Skills taught:**
- Ball physics (velocity, angles)
- Paddle control
- Reflection/bounce mechanics
- Brick destruction with blitter
- Satisfying sound design
- Score and lives

---

### Game 4: Summit
**Units:** 16
**Concept:** Single-screen platformer. Climb the mountain - each level takes you higher, from green foothills to the snowy peak.

**Skills taught:**
- Gravity and falling
- Jump physics (impulse, arc, landing)
- Platform collision detection
- Player animation (walk cycle, jump frame)
- Hazards and enemies
- Level completion and progression

---

### Game 5: Sanctum
**Units:** 16
**Concept:** Flip-screen top-down exploration. Navigate mysterious rooms, collect items, avoid enemies. Atmospheric with copper-lit rooms and sampled ambient sounds.

**Skills taught:**
- 4-way (or 8-way) movement
- Room data structures
- Screen transitions
- Persistent state across rooms
- Simple inventory (keys, items)
- Enemies with chase behaviour

---

### Game 6: Fruit Pursuit
**Units:** 16
**Concept:** Pac-Man style maze game. Collect fruit, avoid ghosts, eat power pills to turn the tables.

**Skills taught:**
- Tile-based maze structure
- Constrained corridor movement
- Enemy AI with personality
- Power-ups that change game state
- Wrap-around screen edges
- Speed and difficulty progression

---

### Game 7: Serpentine
**Units:** 16
**Concept:** Snake game. Eat food, grow longer, don't hit yourself. Simple mechanics, tight gameplay.

**Skills taught:**
- Grid-based movement
- Growing entity management
- Self-collision detection
- Food spawning
- Increasing difficulty through length
- Tight game loop

---

### Game 8: Tumble
**Units:** 16
**Concept:** Falling blocks puzzle. Tetris-style rotation, stacking, and line clearing.

**Skills taught:**
- Piece rotation (4 orientations)
- Falling on a timer
- Grid collision (can piece fit?)
- Line detection and clearing
- Next piece preview
- Speed increases over time

---

### Game 9: Cosmic Onslaught
**Units:** 16
**Concept:** Horizontal parallax shooter. The Amiga showcase - multiple scrolling layers, copper colour splits, Paula soundtrack. This is the machine showing off.

**Skills taught:**
- Hardware scrolling fundamentals
- Dual playfield (two independent scroll layers)
- Parallax effect (layers at different speeds)
- Copper gradients synced to scroll
- Player in scrolling world
- Enemies and terrain collision

**Why here:** This is what people remember about Amiga games. Shadow of the Beast territory - the full audiovisual experience.

---

### Game 10: Wanderer: The Barrens
**Units:** 16
**Concept:** Scrolling platformer. Summit's mechanics in a larger, scrolling world. A lone figure crossing a desolate landscape.

**Skills taught:**
- Horizontal scrolling with platformer physics
- Camera following player
- Large level data structures
- Scrolling collision detection
- Enemies in scrolling world
- Checkpoints and progression
- Parallax backgrounds

---

### Game 11: Street Beatdown
**Units:** 16
**Concept:** Side-scrolling beat 'em up. Walk right, punch enemies. Big sprites, sampled impacts, Y-axis depth sorting.

**Skills taught:**
- Y-axis depth sorting (new concept)
- Melee combat mechanics
- Multiple enemy management
- Health and damage systems
- Walking "into" the screen
- Large animated sprites
- Stage progression

**Why here:** Y-depth sorting is the bridge to isometric. This game introduces layered drawing order.

---

### Game 12: Toxic Gridlock
**Units:** 16
**Concept:** Vertical scrolling racer. Post-apocalyptic traffic chaos - road rushing toward you, dodge wrecks, don't crash.

**Skills taught:**
- Vertical scrolling (new direction)
- Speed variation (accelerate, brake)
- Obstacle spawning
- Collision at speed
- Copper road effects (stripes, colour cycling)
- Road curves and variation
- Distance-based scoring

---

### Game 13: Vector Squadron
**Units:** 16
**Concept:** Vertical scrolling shooter. 1942-style planes and formations. Different feel from Cosmic Onslaught's horizontal flow.

**Skills taught:**
- Vertical scrolling for shooting game
- Formation enemy patterns
- Bullet patterns (enemy fire)
- Ground and air targets
- Power-up collection
- Boss encounters
- Score chaining

---

### Game 14: Lead Rain
**Units:** 16
**Concept:** Run 'n' gun action. Contra-style platforming with multi-directional shooting. Everything learnt, combined.

**Skills taught:**
- Platformer physics with shooting
- Multi-directional firing
- Shooting while moving/jumping
- Enemies that shoot back
- Weapon power-ups
- Boss encounters
- Level variety

---

### Game 15: Monolith of Madness
**Units:** 32
**Concept:** Isometric exploration game. The prestige technique - full 3D projection, depth sorting, mysterious architecture to explore.

**Skills taught:**
- Isometric projection maths
- 3D coordinate systems
- Depth sorting (painter's algorithm)
- Movement in isometric space
- Collision in 3D
- Room-based world structure
- Object interaction
- Puzzle elements

---

### Game 16: Ascension: The Guru Meditation
**Units:** 32
**Concept:** Action-adventure epic. The capstone project combining everything learnt into a commercial-quality game. The title reclaims the infamous Amiga error as a badge of honour.

**Skills taught:**
- Large world design
- Multiple gameplay mechanics integrated
- Story and progression elements
- Save system
- Polish and presentation
- Professional production values
- All previous techniques at mastery level

**Why last:** The curriculum ends with learners demonstrating full command of the machine. Every Amiga developer knows the Guru Meditation - now they've earned it.

---

## AMOS BASIC Track (Optional)

For learners wanting a different approach, an optional AMOS BASIC track is available. AMOS provides a gentler introduction to Amiga game development with built-in sprite and sound handling.

### AMOS Game 1: Star Catcher
**Units:** 8
**Concept:** Simple action game. Catch falling stars, avoid hazards. Shows off AMOS's built-in sprite handling.

**Skills taught:**
- AMOS BASIC fundamentals
- Sprite commands (SPRITE, GET SPRITE, etc.)
- Collision detection (SPRITE HIT)
- Sound and music playback
- Joystick/keyboard input
- Game loop structure

### AMOS Game 2: Tile Trap
**Units:** 8
**Concept:** Sliding puzzle game. Arrange tiles to solve the puzzle and escape. Logic-based, turn-based.

**Skills taught:**
- Array manipulation
- Grid-based logic
- Puzzle state management
- Win condition detection
- Difficulty progression
- Why assembly matters for complex games

The AMOS track is optional. Learners can start directly at Game 1 (Hop) with no BASIC knowledge required.

---

## Skill Progression

| Games | Focus | Era Equivalent |
|-------|-------|----------------|
| 1-4 | Single-screen fundamentals, chipset basics | 1985-1986 |
| 5-8 | Multi-screen and grid games | 1986-1987 |
| 9-11 | Scrolling and parallax | 1987-1989 |
| 12-14 | Combined mechanics, advanced scrolling | 1989-1990 |
| 15-16 | Isometric and commercial quality | 1990-1993 |

By Game 16, learners produce work comparable to late-era commercial releases like Lionheart (1993) and The Chaos Engine (1993).

---

## Platform Context

**Hardware:**
- **CPU:** Motorola 68000 @ 7.16 MHz (NTSC) / 7.09 MHz (PAL)
- **RAM:** 512KB chip RAM (A500), expandable
- **Display:** Multiple modes, typically 320×256 (PAL) or 320×200 (NTSC)
- **Colours:** 32 on-screen from 4096 palette (OCS/ECS), more with tricks
- **Sound:** Paula - 4 channels, 8-bit PCM samples
- **Storage:** 880KB 3.5" floppy disks

**The Custom Chipset:**

The Amiga's power came from three custom chips working together:

- **Agnus** - DMA controller and Blitter. Coordinates memory access, handles fast block graphics operations.
- **Denise** - Display and sprites. Generates video output, manages 8 hardware sprites, handles playfields.
- **Paula** - Audio and disk. Four channels of sampled sound, floppy disk control.

**The Copper:**
A co-processor built into Agnus that executes a display list synchronised to the video beam. Enables palette changes, sprite repositioning, and register modifications mid-screen - the key to many Amiga visual tricks.

**The Blitter:**
Hardware-accelerated block transfer and drawing. Copies rectangular areas, draws lines, fills shapes - all faster than the CPU could manage.

**Hardware Sprites:**
8 sprites, 16 pixels wide, 4 colours each (or paired for 16 colours). Can be reused multiple times per frame via copper repositioning.

**Blitter Objects (BOBs):**
Software sprites drawn by the blitter. More flexible than hardware sprites - any size, any colour depth - but require more CPU/blitter time.

---

## Version History

- **2.0 (2025-11-26):** Complete rewrite. Replaced phases/tiers/lessons with games model.
- **1.0 (2025-01-15):** Original 4,096-lesson curriculum.
