# Sinclair ZX Spectrum Curriculum

**Platform:** Sinclair ZX Spectrum
**Killer Feature:** Attribute colour system
**Games:** 16 (14 at 16 units, 2 at 32 units)
**Total Units:** 288

---

## Overview

The ZX Spectrum curriculum teaches Z80 assembly programming through 16 complete games. The sequence begins with the attribute system - the Spectrum's defining characteristic that created its distinctive visual style - and progresses through scrolling, enemy AI, isometric projection, and advanced techniques until learners can produce commercial-quality games.

The Spectrum had no hardware sprites, no smooth scrolling, and a single-bit beeper for sound. Every impressive effect was achieved through software and creativity. This curriculum embraces those constraints, teaching learners to make the hardware sing through ingenuity.

By the final game, learners will have skills matching professional Spectrum developers of the late 1980s.

---

## Game Sequence

### Game 1: Ink War
**Units:** 16
**Concept:** Territory control game where the attribute system *is* the gameplay. Player vs AI, taking turns to claim 8×8 attribute cells. Control the majority to win.

**Skills taught:**
- Screen memory layout
- Attribute memory (INK, PAPER, BRIGHT, FLASH)
- Keyboard input
- Game state management
- Simple AI decision-making
- Turn-based game loop

**Why first:** The attribute system is what made Spectrum games look distinctly Spectrum. Starting here teaches the core constraint that shapes everything else.

---

### Game 2: Shatter
**Units:** 16
**Concept:** Breakout clone with a polish focus. Paddle, ball, bricks - but with custom font, smooth animation, and audio feedback woven in from the start. Builds on Ink War's foundation to teach production quality.

**Skills taught:**
- Custom font design and installation
- Smooth sub-cell movement (ball and paddle)
- Frame-based timing and delta movement
- Collision detection (walls, paddle, bricks)
- Bounce angles and reflection physics
- Brick destruction with visual effects
- Sound design (pitch variation, collision feedback)
- Power-up systems
- Level design and progression
- Title screen and attract mode
- Game feel and juice

---

### Game 3: Skyfire
**Units:** 16
**Concept:** Fixed-screen space shooter. Player ship versus descending enemy waves.

**Skills taught:**
- Player movement and shooting
- Projectile spawning and management
- Enemy patterns and waves
- Multiple collision types
- Beeper sound effects
- Increasing difficulty

---

### Game 4: Cavern
**Units:** 16
**Concept:** Single-screen platformer in the Manic Miner tradition. Platforms, hazards, collectibles.

**Skills taught:**
- Gravity and falling
- Jump physics (velocity, arc, landing)
- Platform collision detection
- Player animation (walk cycle, jump frame)
- Hazards and enemies
- Level completion logic

---

### Game 5: Chambers
**Units:** 16
**Concept:** Flip-screen top-down exploration. Navigate rooms, collect items, avoid enemies. Atic Atac territory.

**Skills taught:**
- 4-way movement
- Room data structures
- Screen transitions
- Persistent state across rooms
- Simple inventory (keys, items)
- Enemies with chase behaviour

---

### Game 6: Chomp
**Units:** 16
**Concept:** Pac-Man style maze game. Collect dots, avoid ghosts, eat power pills to turn the tables.

**Skills taught:**
- Tile-based maze structure
- Constrained corridor movement
- Enemy AI with personality
- Power-ups that change game state
- Wrap-around screen edges
- Levels and speed progression

---

### Game 7: Slither
**Units:** 16
**Concept:** Snake game. Eat food, grow longer, don't hit yourself.

**Skills taught:**
- Grid-based movement
- Growing entity management
- Self-collision detection
- Food spawning
- Increasing difficulty through length
- Tight game loop

---

### Game 8: Stack
**Units:** 16
**Concept:** Falling blocks puzzle. Tetris-style piece rotation, stacking, and line clearing.

**Skills taught:**
- Piece rotation (4 orientations)
- Falling on a timer
- Grid collision (can piece fit?)
- Line detection and clearing
- Next piece preview
- Speed increases over time

---

### Game 9: Blitz
**Units:** 16
**Concept:** Side-scrolling shooter. Horizontal scroll, shoot enemies, navigate terrain. Scramble/R-Type territory.

**Skills taught:**
- Software horizontal scrolling
- Tile map level data
- Player in scrolling playfield
- Terrain collision
- Enemies tied to scroll position
- Multiple stage sections

**Why here:** The Spectrum has no hardware scrolling - this is all software, shifting bytes. A fundamental skill for larger games.

---

### Game 10: Exodus
**Units:** 16
**Concept:** Scrolling platformer. Cavern's mechanics in a larger, scrolling world.

**Skills taught:**
- Horizontal scrolling with platformer physics
- Camera following player
- Large level data structures
- Scrolling collision detection
- Enemies in scrolling world
- Checkpoints and progression

---

### Game 11: Redline
**Units:** 16
**Concept:** Vertical scrolling racer. Road scrolls toward you, dodge traffic, don't crash.

**Skills taught:**
- Vertical software scrolling
- Speed variation (accelerate, brake)
- Obstacle spawning
- Collision at speed
- Road variation and curves
- Distance-based scoring

---

### Game 12: Recoil
**Units:** 16
**Concept:** Run 'n' gun action. Contra-style platforming with multi-directional shooting.

**Skills taught:**
- Combining platformer and shooter mechanics
- Multi-directional firing
- Shooting while moving/jumping
- Enemies that shoot back
- Weapon power-ups
- Boss encounters

---

### Game 13: Knuckle Brawl
**Units:** 16
**Concept:** Side-scrolling beat 'em up. Walk right, punch enemies. Introduces Y-axis depth.

**Skills taught:**
- Depth sorting (Y-axis layering)
- Melee combat mechanics
- Multiple enemy management
- Health and damage systems
- Walking "into" the screen
- Stage progression

**Why here:** Depth sorting is the bridge to isometric. This game introduces layered drawing order.

---

### Game 14: Strafe
**Units:** 16
**Concept:** Vertical scrolling shooter. 1942-style planes and enemy formations.

**Skills taught:**
- Vertical scrolling (different direction)
- Formation enemy patterns
- Bullet patterns
- Power-up collection
- Boss encounters
- Score chaining

---

### Game 15: Bastion
**Units:** 32
**Concept:** Isometric exploration game. Knight Lore territory - the prestige Spectrum technique.

**Skills taught:**
- Isometric projection maths
- 3D coordinate systems
- Depth sorting (painter's algorithm)
- Movement in isometric space
- Collision in 3D
- Attribute clash management in isometric view
- Room-based world structure
- Object interaction

---

### Game 16: Spectral Legacy
**Units:** 32
**Concept:** Action-adventure epic. The capstone project combining everything learnt into a commercial-quality game.

**Skills taught:**
- Large world design
- Multiple gameplay mechanics integrated
- Story and progression elements
- Save system
- Polish and presentation
- Professional production values
- All previous techniques at mastery level

**Why last:** The curriculum ends with learners demonstrating full command of the machine. "Spectral" nods to the Spectrum; "Legacy" is what they've built.

---

## Sinclair BASIC Track (Optional)

For learners wanting a different approach, an optional Sinclair BASIC track is available. BASIC is better suited to certain game types - particularly text adventures where string handling matters more than speed.

### BASIC Game 1: Caverns of Dorath
**Units:** 8
**Concept:** Text adventure. Explore caverns, solve puzzles, find treasure. Parser-based interaction with rooms and inventory.

**Skills taught:**
- Sinclair BASIC fundamentals
- String handling and INPUT
- IF/THEN logic
- Arrays for room and inventory data
- PRINT and CLS for display
- Game state management

### BASIC Game 2: Mindbreaker
**Units:** 8
**Concept:** Mastermind-style code breaker. Deduce the hidden code through logic and clues.

**Skills taught:**
- Array manipulation
- Logic and deduction algorithms
- Feedback systems (correct position vs correct colour)
- Game loop in BASIC
- Difficulty progression
- Why assembly matters for speed

The BASIC track is optional. Learners can start directly at Game 1 (Ink War) with no BASIC knowledge required.

---

## Skill Progression

| Games | Focus | Era Equivalent |
|-------|-------|----------------|
| 1-4 | Single-screen fundamentals | 1982-1983 |
| 5-8 | Multi-screen and grid games | 1983-1984 |
| 9-11 | Scrolling techniques | 1984-1986 |
| 12-14 | Combined mechanics | 1986-1988 |
| 15-16 | Advanced techniques | 1988-1991 |

By Game 16, learners produce work comparable to late-era commercial releases like Midnight Resistance (1990) and Navy Moves (1988).

---

## Platform Context

**Hardware:**
- **CPU:** Zilog Z80 @ 3.5 MHz
- **RAM:** 48K (16K on early models, 128K on later)
- **Display:** 256×192 pixels, 32×24 attribute cells
- **Colours:** 8 colours, each with normal/bright variant (15 total + black)
- **Sound:** 1-bit beeper (128K models add AY-3-8912 chip)
- **Storage:** Cassette tape

**The Attribute System:**
The Spectrum's display divides the screen into 8×8 pixel cells. Each cell has one attribute byte controlling:
- INK (foreground colour, 3 bits)
- PAPER (background colour, 3 bits)
- BRIGHT (intensity, 1 bit)
- FLASH (alternating, 1 bit)

This creates the infamous "colour clash" when differently-coloured objects overlap within an 8×8 cell. Managing this constraint is central to Spectrum development.

**No Hardware Sprites:**
Unlike the C64, the Spectrum has no hardware sprites. All moving graphics are software-rendered, making efficient drawing routines essential.

**No Hardware Scrolling:**
Smooth scrolling requires shifting screen memory in software - an expensive operation that defined what was possible on the platform.

---

## Version History

- **2.0 (2025-11-26):** Complete rewrite. Replaced phases/tiers/lessons with games model.
- **1.0 (2025-01-15):** Original 4,096-lesson curriculum.
