# Sinclair ZX Spectrum BASIC Curriculum

**Platform:** Sinclair ZX Spectrum
**Language:** Sinclair BASIC
**Purpose:** Gateway curriculum preparing learners for Z80 Assembly
**Games:** 8
**Total Units:** 76

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

| Game | Units |
|------|-------|
| 1. Think of a Number | 4 |
| 2. The Cursed Manor | 16 |
| 3. Lost in the Labyrinth | 8 |
| 4. Block Breaker | 8 |
| 5. Spectrum Serpent | 8 |
| 6. Starfire | 8 |
| 7. Miner Mick | 8 |
| 8. The Crystal Quest | 16 |
| **Total** | **76** |

---

## Game Sequence

### Game 1: Think of a Number
**Units:** 4
**Genre:** Number Guessing
**Concept:** Classic number guessing game. Introduction to Sinclair BASIC's unique keyword entry system.

**Skills taught:**
- Sinclair BASIC environment and commands
- Keyword entry system
- Variables and data types
- INPUT and PRINT statements
- IF/THEN/ELSE logic
- Random numbers (RND, INT)
- CLS and screen clearing

---

### Game 2: The Cursed Manor
**Units:** 16
**Genre:** Text Adventure
**Concept:** Complete text adventure - hugely popular genre on the Spectrum. Games like The Hobbit proved text adventures could be commercial successes.

**Skills taught:**
- DATA and READ statements
- Room data storage
- String handling
- Two-word parser
- Inventory system
- Game state management
- Atmospheric descriptions
- Puzzle design

---

### Game 3: Lost in the Labyrinth
**Units:** 8
**Genre:** Maze Game
**Concept:** Navigate a maze to find the exit. Introduction to Spectrum's built-in graphics commands.

**Skills taught:**
- PLOT and DRAW commands
- Screen coordinates (0-255 × 0-175)
- INK colours for graphics
- Wall collision using ATTR
- INKEY$ keyboard polling
- Timer challenge
- Real-time game loop

---

### Game 4: Block Breaker
**Units:** 8
**Genre:** Breakout
**Concept:** Classic brick-breaking game using Spectrum's attribute system for colourful bricks.

**Skills taught:**
- Ball physics and movement
- Paddle control with INKEY$
- PRINT AT for bricks
- Collision detection
- Score and lives system
- Level progression
- Attribute system for colours

---

### Game 5: Spectrum Serpent
**Units:** 8
**Genre:** Snake
**Concept:** Classic Snake game. Spectrum BASIC is fast enough for smooth character-based gameplay.

**Skills taught:**
- Array usage for snake body
- User-Defined Graphics (UDGs)
- Self-collision detection
- Food spawning
- Growth mechanics
- Score display
- Speed progression
- High score system

---

### Game 6: Starfire
**Units:** 8
**Genre:** Space Shooter
**Concept:** Space shooter introducing User Defined Graphics (UDGs) for custom sprites.

**Skills taught:**
- Full UDG character design
- Multiple moving objects
- Shooting mechanics
- Enemy wave patterns
- Collision detection
- Difficulty ramping
- Score system
- Attribute clash awareness

---

### Game 7: Miner Mick
**Units:** 8
**Genre:** Platformer
**Concept:** Single-screen platformer - homage to Manic Miner, which defined Spectrum gaming.

**Skills taught:**
- Gravity simulation
- Platform collision
- Jump mechanics
- UDG-based player sprite
- Hazards and enemies
- Collectible items
- Level completion
- Multiple caverns

---

### Game 8: The Crystal Quest
**Units:** 16
**Genre:** Puzzle Adventure
**Concept:** Capstone project combining text adventure elements with graphical screens. Collect crystals, solve puzzles, escape the dungeon.

**Skills taught:**
- Multiple graphical screens
- Inventory system
- Puzzle elements
- NPCs with dialogue
- Crystal collection quest
- Complete game experience
- All previous skills combined
- BASIC limitations exposed

---

## Skill Progression

| Game | Focus | Key Techniques |
|------|-------|----------------|
| 1 | Logic, variables | INPUT, IF/THEN/ELSE, RND |
| 2 | Text, data | DATA/READ, strings, parser |
| 3 | Graphics | PLOT, DRAW, ATTR |
| 4 | Real-time input | INKEY$, game loop, collision |
| 5 | UDGs, arrays | User-Defined Graphics |
| 6 | Multiple objects | UDG sprites, shooting |
| 7 | Physics | Gravity, platform collision |
| 8 | Integration | All skills combined |

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
- **1.1 (2026-01-19):** Updated to match authoritative outline files - 76 units, 8 games with specific titles.
