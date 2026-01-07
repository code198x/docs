# Commodore 64 BASIC V2 Curriculum

**Platform:** Commodore 64
**Language:** BASIC V2
**Purpose:** Gateway curriculum preparing learners for 6510 Assembly
**Games:** 8
**Total Units:** 512

---

## Overview

The BASIC V2 curriculum provides an accessible introduction to C64 game development. While BASIC V2 lacks dedicated game commands, it teaches fundamental programming concepts and demonstrates what's possible - and what isn't - without assembly language.

This curriculum teaches game design concepts and C64 capabilities through BASIC before learners tackle the complexities of 6510 assembly. Graduates will understand both the potential of the hardware and why direct machine access matters.

---

## Why BASIC V2 First?

BASIC V2 offers several advantages as a gateway:

1. **Immediate feedback** - Type and run instantly
2. **Built-in editor** - No external tools needed
3. **Readable code** - English-like syntax
4. **PEEK/POKE introduction** - First taste of hardware
5. **See the limits** - Understand why assembly is needed

By the end of this curriculum, learners will have created 8 complete games and will understand both what BASIC makes possible and where it struggles - motivating the transition to 6510 assembly.

---

## Curriculum Structure

| Phase | Games | Units Each | Total |
|-------|-------|------------|-------|
| Foundation | 1-8 | 64 | 512 |
| **Total** | **8** | | **512** |

Each game is divided into 4 phases of 16 units each.

---

## Game Sequence

### Game 1: Number Hunter
**Units:** 64 (4 phases)
**Concept:** Number guessing game with scoring. Simple text-based game introducing BASIC fundamentals.

**Skills taught:**
- BASIC environment and direct mode
- Variables and data types
- INPUT and PRINT statements
- IF/THEN logic
- FOR/NEXT loops
- Random numbers (RND)
- Simple scoring and game loop
- Screen clearing (PRINT CHR$(147))

---

### Game 2: Cosmic Drift
**Units:** 64 (4 phases)
**Concept:** Character-based animation. Moving stars across the screen - first visual game.

**Skills taught:**
- Screen coordinates and cursor positioning
- POKE to screen memory ($0400)
- POKE to colour memory ($D800)
- Character codes (PETSCII)
- Animation loops
- Timing with FOR/NEXT delays
- Multiple moving objects
- Colour usage

---

### Game 3: Catcher
**Units:** 64 (4 phases)
**Concept:** Catch falling objects with a paddle. Keyboard-controlled action game.

**Skills taught:**
- Keyboard input (GET)
- Real-time game loop
- Player movement
- Falling object mechanics
- Collision detection (screen PEEK)
- Score display
- Lives system
- Increasing difficulty

---

### Game 4: Maze Escape
**Units:** 64 (4 phases)
**Concept:** Navigate through a maze to reach the exit. Introduces DATA statements for level design.

**Skills taught:**
- DATA and READ statements
- Level data storage
- Maze rendering with characters
- Four-directional movement
- Wall collision
- Multiple levels
- Timer/scoring
- Level completion

---

### Game 5: Snake Trail
**Units:** 64 (4 phases)
**Concept:** Classic snake game using character graphics.

**Skills taught:**
- Array usage for snake body
- Timed movement (TI variable)
- Self-collision detection
- Food spawning
- Growth mechanics
- Screen wrapping
- Speed progression
- Game over conditions

---

### Game 6: Space Dodge
**Units:** 64 (4 phases)
**Concept:** Vertical scrolling avoidance game. Dodge obstacles moving down the screen.

**Skills taught:**
- Simulated scrolling with characters
- Multiple obstacle tracking
- Difficulty ramping
- High score tracking
- Custom characters (POKE 53272)
- Basic sprite concepts via characters
- Performance considerations
- BASIC speed limits

---

### Game 7: Memory Match
**Units:** 64 (4 phases)
**Concept:** Card matching puzzle game with custom characters.

**Skills taught:**
- Custom character definition
- Two-dimensional arrays
- Game state management
- Turn-based mechanics
- Match detection
- Score and move tracking
- Two-player mode
- Polish and presentation

---

### Game 8: Platform Peril
**Units:** 64 (4 phases)
**Concept:** Single-screen platformer pushing BASIC to its limits. Demonstrates why assembly is needed.

**Skills taught:**
- Gravity simulation in BASIC
- Platform collision
- Jump mechanics
- Enemy movement
- Collectibles
- Performance bottlenecks
- BASIC limitations exposed
- Transition preparation

---

## Skill Progression

| Game | Focus | Key Techniques |
|------|-------|----------------|
| 1 | Logic, variables | INPUT, IF/THEN, RND |
| 2 | Screen memory | POKE $0400, POKE $D800 |
| 3 | Real-time input | GET, game loop |
| 4 | Data structures | DATA/READ, levels |
| 5 | Arrays, timing | Arrays, TI timer |
| 6 | Scrolling concept | Character movement |
| 7 | Custom characters | POKE 53272, design |
| 8 | Physics, limits | Gravity, collisions |

---

## Why Transition to 6510 Assembly?

By Game 8, learners will encounter BASIC's limitations:

| BASIC Limitation | 6510 Solution |
|------------------|---------------|
| Slow execution | Direct machine code |
| No hardware sprites | Sprite registers |
| Character-only graphics | Bitmap modes |
| No smooth scrolling | Hardware scroll |
| Limited sound | SID chip access |
| No raster effects | Raster interrupts |

The BASIC curriculum intentionally pushes learners to these boundaries, creating natural motivation for the 6510 Assembly curriculum.

---

## BASIC V2 Context

### Key Commands Used

**Program Flow:**
- `IF...THEN`, `FOR...NEXT`, `GOTO`, `GOSUB`
- `ON...GOTO`, `ON...GOSUB`

**Input/Output:**
- `PRINT`, `INPUT`, `GET`
- `POKE`, `PEEK`

**Data:**
- `DATA`, `READ`, `RESTORE`
- `DIM` for arrays

**Functions:**
- `RND()`, `ABS()`, `INT()`
- `CHR$()`, `ASC()`

### Memory Locations

Learners are introduced to key addresses:
- `$0400` - Screen memory
- `$D800` - Colour memory
- `53272` - Character set pointer
- `53280/53281` - Border/background colour
- `TI` - System timer

---

## Distribution

Games are distributed as:
- `.PRG` files (direct load)
- `.D64` disk images
- Type-in listings (educational value)

---

## Progression to 6510 Assembly

After completing this curriculum, learners should:

1. Understand C64 memory layout basics
2. Know screen and colour memory
3. Have created 8 complete games
4. Recognise BASIC's performance limits
5. Be motivated to learn assembly
6. Have game design experience to apply

The 6510 Assembly curriculum (1,536 units) then teaches direct hardware control, building on these foundations.

---

## Version History

- **1.0 (2026-01-07):** Initial curriculum design - 512 units, 8 games.
