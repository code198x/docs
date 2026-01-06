# Commodore 64 Curriculum

**Platform:** Commodore 64
**Killer Feature:** SID sound chip
**Games:** 16 (14 at 16 units, 2 at 32 units)
**Total Units:** 288

---

## Overview

The Commodore 64 curriculum teaches 6510 assembly programming through 16 complete games. The sequence begins with the SID chip - the C64's defining feature - and progresses through sprites, scrolling, raster effects, and advanced techniques until learners can produce commercial-quality games.

By the final game, learners will have skills matching professional C64 developers of the late 1980s and early 1990s.

---

## Game Sequence

### Game 1: SID Symphony
**Units:** 16
**Concept:** Rhythm game - notes scroll horizontally across three tracks, hit the correct key when notes reach the hit zone. Guitar Hero on the C64.

**Skills taught:**
- SID chip fundamentals (voices, ADSR, waveforms)
- Raster timing basics
- Keyboard input
- Screen layout with character graphics
- Game loop structure

**Why first:** The SID chip is why people remember the C64. Starting here creates immediate emotional investment and produces impressive audio from Unit 1.

---

### Game 2: Starfield
**Units:** 16
**Concept:** Single-screen space shooter. Player ship versus waves of enemies. Shoot, dodge, survive.

**Skills taught:**
- Hardware sprites (enabling, positioning, pointers)
- Joystick input via CIA
- Sprite-to-sprite collision
- Bullet management
- Score display

---

### Game 3: Maze Raider
**Units:** 16
**Concept:** Pac-Man style maze chase. Navigate corridors, collect pellets, avoid enemies.

**Skills taught:**
- Character graphics (custom character sets)
- Tile-based maps
- Tile collision detection
- Simple enemy AI (chase behaviour)
- Screen-based level data

---

### Game 4: Platform Panic
**Units:** 16
**Concept:** Single-screen platformer. Jump between platforms, avoid hazards, reach the exit.

**Skills taught:**
- Gravity and jump physics
- Platform collision (landing, bumping)
- Animation frames
- Hazard timing
- Level progression

---

### Game 5: Brick Basher
**Units:** 16
**Concept:** Breakout clone. Paddle, ball, bricks. Clear the screen.

**Skills taught:**
- Ball physics (velocity, reflection angles)
- Paddle control
- Brick grid collision
- Power-up systems
- Increasing difficulty

---

### Game 6: Invader Wave
**Units:** 16
**Concept:** Space Invaders style fixed shooter. Enemy formation descends, player defends.

**Skills taught:**
- Formation movement patterns
- Enemy bullet management
- Shields (destructible character graphics)
- Wave progression
- High score persistence

---

### Game 7: Scroll Runner
**Units:** 16
**Concept:** Horizontal scrolling introduction. Runner dodges obstacles in an endless scroll.

**Skills taught:**
- Hardware horizontal scrolling (VIC-II $D016)
- Colour RAM scrolling
- Screen buffer management
- Colour splits (basic raster)
- Procedural obstacle spawning

---

### Game 8: Night Raid
**Units:** 16
**Concept:** Scramble-style side-scroller. Fly through terrain, shoot enemies, manage fuel.

**Skills taught:**
- Scrolling combined with shooting
- Terrain collision
- Resource management (fuel)
- Ground and air targets
- Increasing complexity curves

---

### Game 9: Sprite Storm
**Units:** 16
**Concept:** Multi-sprite action game. More enemies than the hardware allows - enter multiplexing.

**Skills taught:**
- Sprite multiplexing (16+ sprites)
- Sorted sprite lists
- Raster interrupt timing
- Sprite priority and overlap
- Performance optimisation

---

### Game 10: Raster Rider
**Units:** 16
**Concept:** Racing game with pseudo-3D road using raster effects.

**Skills taught:**
- Advanced raster splits
- Colour cycling for speed effect
- Road perspective rendering
- Opponent cars
- Timer-based gameplay

---

### Game 11: Dungeon Crawl
**Units:** 16
**Concept:** Top-down adventure. Explore rooms, collect keys, unlock doors, find treasure.

**Skills taught:**
- Multi-screen map structure
- Room transitions
- Inventory system
- Key/door mechanics
- Save state (basic)

---

### Game 12: Arena Fighter
**Units:** 16
**Concept:** One-on-one combat. Two fighters, health bars, special moves.

**Skills taught:**
- Complex animation states
- Hit detection with timing windows
- Health and damage systems
- Two-player input
- Match structure (rounds, wins)

---

### Game 13: Parallax Patrol
**Units:** 16
**Concept:** Advanced side-scrolling shooter with multi-layer backgrounds.

**Skills taught:**
- Multi-layer parallax scrolling
- Large level design
- Weapon upgrade systems
- Boss encounters
- Memory management for large games

---

### Game 14: Isometric Quest
**Units:** 32
**Concept:** Isometric adventure game. Explore a 3D-perspective world.

**Skills taught:**
- Isometric projection maths
- Depth sorting (painter's algorithm)
- Isometric collision
- Larger world exploration
- NPC interaction

---

### Game 15: Mega Blaster
**Units:** 16
**Concept:** Turrican-style run'n'gun. Large scrolling world, multiple weapons, bosses.

**Skills taught:**
- All scrolling techniques combined
- Weapon variety and switching
- Large sprite bosses
- Level streaming
- Music integration

---

### Game 16: Symphony's End
**Units:** 32
**Concept:** Commercial-quality showcase. A complete, polished game combining everything learnt.

**Skills taught:**
- All techniques at mastery level
- Demo-scene visual tricks
- Advanced SID (filters, multi-speed)
- Professional polish
- Loader and packaging

**Why last:** The curriculum ends where it began - with the SID. But now the learner commands the full machine.

---

## BASIC Gateway (Optional)

For learners wanting a gentler introduction before assembly, an optional BASIC track is available.

### BASIC Game 1: Maze Muncher
**Units:** 8
**Concept:** Simple maze game in BASIC V2. Navigate, collect, avoid.

**Skills taught:**
- BASIC V2 fundamentals
- POKE/PEEK for hardware access
- Keyboard input
- PETSCII graphics
- Game loop in interpreted language

### BASIC Game 2: Sprite Bounce
**Units:** 8
**Concept:** Ball-and-paddle game using hardware sprites from BASIC.

**Skills taught:**
- Sprite control via POKE
- SID sound effects from BASIC
- Joystick reading
- BASIC limitations (speed ceiling)
- Why assembly matters

The BASIC track is optional. Learners can start directly at Game 1 (SID Symphony) with no BASIC knowledge required.

---

## Skill Progression

| Games | Focus | Era Equivalent |
|-------|-------|----------------|
| 1-6 | Single-screen fundamentals | 1982-1984 |
| 7-8 | Scrolling introduction | 1984-1985 |
| 9-10 | Advanced hardware | 1985-1987 |
| 11-12 | Complex game systems | 1986-1988 |
| 13-16 | Commercial quality | 1988-1993 |

By Game 16, learners produce work comparable to late-era commercial releases like Turrican II (1991) and Mayhem in Monsterland (1993).

---

## Version History

- **2.0 (2025-11-25):** Complete rewrite. Replaced phases/tiers/lessons with games model.
- **1.0 (2025-01-15):** Original 4,096-lesson curriculum.
