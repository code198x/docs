# Sinclair ZX Spectrum BASIC Curriculum

**Platform:** Sinclair ZX Spectrum
**Language:** Sinclair BASIC
**Purpose:** Gateway curriculum preparing learners for Z80 Assembly
**Games:** 8
**Total Units:** 512

---

## Overview

The Sinclair BASIC curriculum provides an accessible introduction to Spectrum game development. Sinclair BASIC is more capable than C64 BASIC V2, with built-in graphics commands (PLOT, DRAW, CIRCLE) and structured programming features. This makes it excellent for teaching game concepts before tackling Z80 assembly.

This curriculum teaches game design concepts and Spectrum capabilities through BASIC before learners face the complexities of Z80 assembly. Graduates will understand both the potential of the hardware and why direct machine access matters.

---

## Why Sinclair BASIC First?

Sinclair BASIC offers several advantages as a gateway:

1. **Rich graphics commands** - PLOT, DRAW, CIRCLE, INK, PAPER built-in
2. **Structured programming** - No line numbers required in modern usage
3. **Immediate feedback** - Type and run instantly
4. **User-defined graphics** - UDG characters for custom shapes
5. **Attribute system** - Understanding colour cells early
6. **See the limits** - Understand why assembly is needed

By the end of this curriculum, learners will have created 8 complete games and will understand both what Sinclair BASIC makes possible and where it struggles - motivating the transition to Z80 assembly.

---

## Curriculum Structure

| Phase | Games | Units Each | Total |
|-------|-------|------------|-------|
| Foundation | 1-8 | 64 | 512 |
| **Total** | **8** | | **512** |

Each game is divided into 4 phases of 16 units each.

---

## Game Sequence

### Game 1: Guess Quest
**Units:** 64 (4 phases)
**Concept:** Number guessing game with visual feedback. Text-based introduction to Sinclair BASIC.

**Skills taught:**
- Sinclair BASIC environment and commands
- Variables and data types
- INPUT and PRINT statements
- IF/THEN/ELSE logic
- FOR/NEXT loops
- Random numbers (RND)
- CLS and screen clearing
- Basic colour with INK/PAPER

---

### Game 2: Pixel Rain
**Units:** 64 (4 phases)
**Concept:** Falling pixels creating patterns. First visual game using PLOT command.

**Skills taught:**
- PLOT command - placing pixels
- Screen coordinates (0-255 × 0-175)
- INK colours for pixels
- Animation with PLOT
- Random positions
- Simple timing loops
- Screen clearing strategies
- Visual patterns

---

### Game 3: Paddle Battle
**Units:** 64 (4 phases)
**Concept:** Pong-style paddle game. Keyboard-controlled action using INKEY$.

**Skills taught:**
- INKEY$ - keyboard polling
- Real-time game loop
- Ball movement with PLOT
- Paddle drawing with DRAW
- Simple collision detection
- Score keeping
- Two-player option
- Speed control

---

### Game 4: Dungeon Explorer
**Units:** 64 (4 phases)
**Concept:** Navigate through dungeon rooms. DATA statements for room layouts.

**Skills taught:**
- DATA and READ statements
- Room data storage
- Character-based maps using PRINT AT
- Four-directional movement
- Wall collision (attribute check)
- Multiple rooms
- Inventory basics
- Door transitions

---

### Game 5: Snake Spectrum
**Units:** 64 (4 phases)
**Concept:** Classic snake game using character graphics and UDGs.

**Skills taught:**
- Array usage for snake body
- User-Defined Graphics (UDGs)
- UDG design and POKEing
- Self-collision detection
- Food spawning
- Growth mechanics
- Score display
- Speed progression

---

### Game 6: Asteroid Dodge
**Units:** 64 (4 phases)
**Concept:** Space game with scrolling asteroids. Ship dodges falling obstacles.

**Skills taught:**
- Multiple moving objects
- Simulated scrolling
- UDG sprites (ship, asteroids)
- DRAW for effects
- Difficulty ramping
- High score system
- Attribute clash awareness
- Performance observation

---

### Game 7: Pattern Match
**Units:** 64 (4 phases)
**Concept:** Memory/puzzle game with UDG tiles. Turn-based matching pairs.

**Skills taught:**
- Full UDG character set usage
- Two-dimensional arrays
- Game state management
- Turn-based mechanics
- Match detection
- Timer using PEEK (23672)
- Two-player competitive
- Visual polish

---

### Game 8: Platform Jump
**Units:** 64 (4 phases)
**Concept:** Single-screen platformer pushing Sinclair BASIC to its limits.

**Skills taught:**
- Gravity simulation
- Platform collision
- Jump mechanics
- UDG-based player sprite
- Enemy movement
- Collectibles
- Attribute clash problems
- BASIC limitations exposed

---

## Skill Progression

| Game | Focus | Key Techniques |
|------|-------|----------------|
| 1 | Logic, variables | INPUT, IF/THEN/ELSE, RND |
| 2 | Pixel graphics | PLOT, coordinates, INK |
| 3 | Real-time input | INKEY$, game loop, DRAW |
| 4 | Data structures | DATA/READ, PRINT AT |
| 5 | UDGs, arrays | User-Defined Graphics |
| 6 | Multiple objects | Simulated scrolling |
| 7 | Complex UDGs | Full character design |
| 8 | Physics, limits | Gravity, attribute clash |

---

## Why Transition to Z80 Assembly?

By Game 8, learners will encounter Sinclair BASIC's limitations:

| BASIC Limitation | Z80 Solution |
|------------------|--------------|
| Slow execution | Direct machine code |
| Attribute clash | Clever techniques, timing |
| No hardware sprites | Sprite routines |
| Slow graphics | Direct screen writes |
| Limited sound | Beeper control routines |
| No smooth scroll | Hardware tricks |

The Sinclair BASIC curriculum intentionally pushes learners to these boundaries, creating natural motivation for the Z80 Assembly curriculum.

---

## Sinclair BASIC Context

### Key Commands Used

**Program Flow:**
- `IF...THEN...ELSE`, `FOR...NEXT`, `GO TO`, `GO SUB`
- `RETURN`, `STOP`

**Input/Output:**
- `PRINT`, `PRINT AT`, `INPUT`, `INKEY$`
- `POKE`, `PEEK`

**Graphics:**
- `PLOT`, `DRAW`, `CIRCLE`
- `INK`, `PAPER`, `BRIGHT`, `FLASH`
- `BORDER`, `CLS`

**Data:**
- `DATA`, `READ`, `RESTORE`
- `DIM` for arrays

**Functions:**
- `RND`, `ABS`, `INT`, `SGN`
- `CHR$`, `CODE`, `VAL`, `STR$`

### Memory Locations

Learners are introduced to key addresses:
- `16384` - Screen memory start
- `22528` - Attribute memory start
- `23675-23677` - System variables (FRAMES)
- `USR "A"` - UDG memory location

### Attribute System

Understanding the 8×8 colour cell system:
- INK (foreground) - 0-7
- PAPER (background) - 0-7
- BRIGHT - 0 or 1
- FLASH - 0 or 1
- Attribute clash - why it happens

---

## Distribution

Games are distributed as:
- `.TAP` files (tape image)
- `.TZX` files (enhanced tape)
- `.SNA` snapshots
- Type-in listings (educational value)

---

## Progression to Z80 Assembly

After completing this curriculum, learners should:

1. Understand Spectrum memory layout basics
2. Know screen and attribute memory
3. Have created 8 complete games
4. Understand UDG character design
5. Recognise BASIC's performance limits
6. Be motivated to learn assembly
7. Have game design experience to apply

The Z80 Assembly curriculum (1,536 units) then teaches direct hardware control, building on these foundations.

---

## Version History

- **1.0 (2026-01-07):** Initial curriculum design - 512 units, 8 games.
