# Commodore Amiga AMOS BASIC Curriculum

**Platform:** Commodore Amiga
**Language:** AMOS BASIC
**Purpose:** Gateway curriculum preparing learners for 68000 Assembly
**Games:** 8
**Total Units:** 512

---

## Overview

The AMOS BASIC curriculum provides a gentler introduction to Amiga game development. AMOS abstracts the hardware complexity while still producing impressive results - sprites, bobs, samples, and scrolling are all accessible through BASIC commands.

This curriculum teaches game design concepts and Amiga capabilities without requiring assembly language knowledge. Graduates are prepared to tackle the 68000 Assembly curriculum with a solid understanding of what the Amiga can do and why low-level access matters.

---

## Why AMOS First?

AMOS BASIC offers several advantages as a gateway:

1. **Immediate results** - Games running within minutes
2. **Built-in graphics** - Sprites, bobs, screens handled automatically
3. **Built-in audio** - Sample playback and music without Paula registers
4. **Focus on design** - Learn game logic without hardware details
5. **See the limits** - Understand why assembly is needed for advanced games

By the end of this curriculum, learners will have created 8 complete games and will understand both what AMOS makes easy and where it struggles - motivating the transition to 68000 assembly.

---

## Curriculum Structure

| Phase | Games | Units Each | Total |
|-------|-------|------------|-------|
| Foundation | 1-8 | 64 | 512 |
| **Total** | **8** | | **512** |

Each game is divided into 4 phases of 16 units each.

---

## Game Sequence

### Game 1: Star Catcher
**Units:** 64 (4 phases)
**Concept:** Catch falling stars while avoiding hazards. Simple action game showcasing AMOS sprite handling.

**Skills taught:**
- AMOS environment and editor
- Screen setup and display modes
- Sprite commands (SPRITE, GET SPRITE)
- Sprite collision (SPRITE HIT, SPRITE COL)
- Joystick and keyboard input (JOY, INKEY$)
- Sound playback (BOOM, SHOOT, SAM PLAY)
- Score display and game loop
- Menu screens and game states

---

### Game 2: Crate Stack
**Units:** 64 (4 phases)
**Concept:** Single-screen platformer. Jump between platforms, collect items, reach the exit. Introduction to physics in AMOS.

**Skills taught:**
- Gravity and velocity variables
- Jump mechanics
- Platform collision using sprites
- Bob (Blitter Object) basics
- Animation sequences
- Level data in DATA statements
- Multiple levels
- Lives and scoring

---

### Game 3: Space Swarm
**Units:** 64 (4 phases)
**Concept:** Fixed-screen shooter. Player ship versus descending enemies. Classic arcade action.

**Skills taught:**
- Player shooting mechanics
- Projectile management (sprite arrays)
- Enemy formations
- Multiple collision types
- Wave progression
- Difficulty scaling
- High score persistence
- Sound effects variety

---

### Game 4: Bounce Back
**Units:** 64 (4 phases)
**Concept:** Breakout clone. Paddle, ball, and bricks with AMOS's smooth movement and sound.

**Skills taught:**
- Ball physics (angles, reflection)
- Paddle control
- Brick destruction
- Power-up bricks
- Bob drawing for bricks
- Screen updates with SCREEN SWAP
- Level editor concepts
- Music during gameplay

---

### Game 5: Maze Runner
**Units:** 64 (4 phases)
**Concept:** Pac-Man style maze game. Collect items, avoid enemies, use power-ups.

**Skills taught:**
- Tile-based maze using PASTE BOB
- Constrained movement
- Ghost AI with different personalities
- Power-up state changes
- Screen wrapping
- AMOS Banks for data storage
- Timing and speed control
- Multi-screen maze

---

### Game 6: Dungeon Doors
**Units:** 64 (4 phases)
**Concept:** Flip-screen exploration. Navigate rooms, collect keys, find the exit.

**Skills taught:**
- Room data structures
- Screen transitions
- Persistent state (items collected)
- Key/door mechanics
- Enemy chase behaviour
- Inventory display
- Map system
- Save/load game state

---

### Game 7: Block Drop
**Units:** 64 (4 phases)
**Concept:** Falling blocks puzzle. Tetris-style rotation and line clearing.

**Skills taught:**
- Piece rotation logic
- Grid-based collision
- Line detection and clearing
- Next piece preview
- Score multipliers
- Speed progression
- Ghost piece preview
- Two-player mode

---

### Game 8: Scroll Quest
**Units:** 64 (4 phases)
**Concept:** Side-scrolling platformer. A scrolling world built in AMOS - seeing both capabilities and limitations.

**Skills taught:**
- AMOS scrolling commands (SCREEN OFFSET)
- Large level storage
- Camera following
- Parallax attempts
- Enemies in scrolling world
- Performance limitations
- Why assembly is needed
- Transition preparation

---

## Skill Progression

| Game | Focus | Key AMOS Features |
|------|-------|-------------------|
| 1 | Sprites, input, sound | SPRITE, JOY, SAM PLAY |
| 2 | Physics, bobs | Bob drawing, animation |
| 3 | Multiple objects | Sprite arrays, collisions |
| 4 | Ball physics | Angles, SCREEN SWAP |
| 5 | AI, tiles | PASTE BOB, AI behaviours |
| 6 | Multi-screen | Banks, state management |
| 7 | Grid logic | Rotation, line clearing |
| 8 | Scrolling | SCREEN OFFSET, limitations |

---

## Why Transition to 68000 Assembly?

By Game 8, learners will encounter AMOS's limitations:

| AMOS Limitation | 68000 Solution |
|-----------------|----------------|
| Slow scrolling | Direct bitplane manipulation |
| Limited sprite control | Hardware sprite registers |
| No Copper access | Full Copper list control |
| Blitter inefficiency | Direct Blitter programming |
| Audio limitations | Paula register control |
| Memory constraints | Bank switching, optimisation |

The AMOS curriculum intentionally pushes learners to these boundaries, creating natural motivation for the 68000 Assembly curriculum.

---

## AMOS-Specific Context

### AMOS Commands Used

**Graphics:**
- `SCREEN OPEN`, `SCREEN DISPLAY`
- `SPRITE`, `GET SPRITE`, `PUT SPRITE`
- `BOB`, `GET BOB`, `PASTE BOB`
- `SCREEN OFFSET`, `SCREEN SWAP`
- `INK`, `PALETTE`

**Sound:**
- `SAM PLAY`, `SAM LOOP`
- `BOOM`, `SHOOT`, `BELL`
- `MUSIC`, `VOICE`

**Input:**
- `JOY()`, `JLEFT()`, `JRIGHT()`, etc.
- `INKEY$`, `KEY STATE`
- `MOUSE KEY`, `X MOUSE`, `Y MOUSE`

**Collision:**
- `SPRITE HIT`, `SPRITE COL`
- `BOB HIT`, `BOB COL`
- `POINT()`, `ZONE()`

### AMOS Extensions

The curriculum uses standard AMOS Professional features. Extensions like AMOS 3D or Craft are not required.

---

## Distribution

Games are distributed as:
- AMOS source files (.AMOS)
- Compiled executables (for standalone play)
- ADF disk images

---

## Progression to 68000 Assembly

After completing this curriculum, learners should:

1. Understand Amiga display modes and capabilities
2. Know what sprites, bobs, and scrolling can achieve
3. Recognise where AMOS struggles
4. Be motivated to learn hardware-level programming
5. Have 8 complete games demonstrating core concepts

The 68000 Assembly curriculum (2,048 units) then teaches direct hardware control, starting from the fundamentals and building to commercial-quality games.

---

## Version History

- **1.0 (2025-01-07):** Initial curriculum design - 512 units, 8 games.
