# C64 BASIC Curriculum

**Purpose:** Define the 8-game BASIC curriculum track for Commodore 64 - a complete game development curriculum using stock BASIC V2.

**Last Updated:** 2026-01-18

---

## Overview

| Aspect | Details |
|--------|---------|
| **Track** | BASIC |
| **Platform** | Commodore 64 |
| **Games** | 8 |
| **Units per game** | 4, 8, or 16 (varies by complexity) |
| **Prerequisite** | None |
| **BASIC Version** | Stock BASIC V2 (no extensions required) |
| **Outcome** | Complete, playable games |

---

## Philosophy

### Why Stock BASIC V2?

| Reason | Benefit |
|--------|---------|
| **Everyone had it** | Built into every C64 |
| **Historical authenticity** | Magazine type-ins used PEEK/POKE |
| **No setup required** | Works on any C64 or emulator |
| **Teaches hardware** | PEEK/POKE reveals the machine |
| **Real limitation** | Understanding constraints breeds creativity |

### The PEEK/POKE Approach

Stock C64 BASIC has no graphics, sound, or sprite commands - but PEEK and POKE give you direct hardware access:

```basic
POKE 53280,0          : REM BORDER BLACK
POKE 53281,0          : REM BACKGROUND BLACK
POKE 1024,81          : REM PUT BALL CHARACTER ON SCREEN
POKE 54296,15         : REM SID VOLUME MAX
J=PEEK(56320)         : REM READ JOYSTICK
```

This is how people *actually* programmed C64 BASIC games.

### Why NOT Simons' BASIC?

| Consideration | Reality |
|---------------|---------|
| **Cost** | Simons' BASIC was a separate purchase |
| **Availability** | Most users didn't have it |
| **Type-ins** | Magazine listings assumed stock BASIC |
| **Learning** | PEEK/POKE teaches hardware better |
| **Authenticity** | This is how it was really done |

---

## Game Sequence

### Game 1: Psychic Computer

| Aspect | Details |
|--------|---------|
| **Units** | 4 |
| **Genre** | Number guessing |
| **Concepts** | Variables, input, conditionals, loops |
| **Graphics** | Text only |

**What You Build:**
- Computer picks a number
- Player guesses
- Higher/lower feedback
- Win condition

**Skills Introduced:**
- Variables (numeric)
- INPUT statement
- IF/THEN
- GOTO (simple looping)
- PRINT formatting
- RND() function

---

### Game 2: The Forgotten Key

| Aspect | Details |
|--------|---------|
| **Units** | 16 |
| **Genre** | Text adventure |
| **Concepts** | Strings, arrays, data structures |
| **Graphics** | Text only |

**What You Build:**
- Room descriptions
- Movement (N/S/E/W)
- Inventory
- Simple puzzles

**Skills Introduced:**
- String variables (A$)
- Arrays (DIM)
- DATA/READ statements
- String comparison
- Simple state management
- Multi-room structure

---

### Game 3: Pixel Serpent

| Aspect | Details |
|--------|---------|
| **Units** | 8 |
| **Genre** | Snake/growth game |
| **Concepts** | Screen memory, movement, collision |
| **Graphics** | Character-based |

**What You Build:**
- Character-based snake
- Food collection
- Growth mechanic
- Wall collision

**Skills Introduced:**
- PEEK and POKE (introduction)
- Screen memory (1024-2023)
- Colour memory (55296-56295)
- Keyboard reading (PEEK(197))
- Game loop concept
- Collision detection (PEEK screen)

**Key Code:**
```basic
100 S=1024: REM SCREEN MEMORY
110 POKE S+Y*40+X, 81: REM DRAW BALL
120 IF PEEK(S+NY*40+NX)=81 THEN 500: REM HIT SELF
```

---

### Game 4: Wall Smasher

| Aspect | Details |
|--------|---------|
| **Units** | 8 |
| **Genre** | Breakout/brick breaker |
| **Concepts** | Character graphics, physics, collision |
| **Graphics** | Character-based |

**What You Build:**
- Paddle (character)
- Bouncing ball (character)
- Breakable bricks (characters)
- Score display

**Skills Introduced:**
- PETSCII graphics characters
- Ball physics (character movement)
- Joystick reading (PEEK(56320))
- Screen collision (PEEK)
- Colour for different bricks
- Score tracking

**Key Code:**
```basic
100 J=PEEK(56320): REM READ JOYSTICK
110 IF (J AND 4)=0 THEN PX=PX-1: REM LEFT
120 IF (J AND 8)=0 THEN PX=PX+1: REM RIGHT
130 REM CHECK WHAT BALL HIT
140 C=PEEK(1024+BY*40+BX)
150 IF C=160 THEN SC=SC+10: REM HIT BRICK
```

---

### Game 5: Star Patrol

| Aspect | Details |
|--------|---------|
| **Units** | 8 |
| **Genre** | Fixed shooter |
| **Concepts** | Custom characters, shooting |
| **Graphics** | Character-based with redefined characters |

**What You Build:**
- Player ship (custom character)
- Enemy waves (custom characters)
- Shooting (character movement)
- Lives system

**Skills Introduced:**
- Custom character sets
- Character memory (POKE 53272)
- Copying character ROM to RAM
- Designing 8x8 characters
- Bullet management
- Multiple enemies

**Key Code:**
```basic
100 REM COPY CHARSET TO RAM
110 POKE 56334,0: POKE 1,51
120 FOR I=0 TO 2047: POKE 12288+I,PEEK(53248+I): NEXT
130 POKE 1,55: POKE 56334,1
140 POKE 53272,(PEEK(53272)AND240)+12
150 REM NOW REDEFINE CHARACTER 128
160 FOR I=0 TO 7: READ D: POKE 12288+128*8+I,D: NEXT
170 DATA 24,60,126,255,255,90,36,102
```

---

### Game 6: Jump Quest

| Aspect | Details |
|--------|---------|
| **Units** | 8 |
| **Genre** | Single-screen platformer |
| **Concepts** | Gravity, jumping, platforms |
| **Graphics** | Character-based |

**What You Build:**
- Jumping character
- Platforms (characters)
- Collectibles
- Level completion

**Skills Introduced:**
- Gravity simulation
- Jump physics
- Platform collision (PEEK below)
- Level data in DATA statements
- Simple animation (2-frame)
- Game state

**Key Code:**
```basic
100 REM CHECK IF ON PLATFORM
110 BELOW=PEEK(1024+(PY+1)*40+PX)
120 IF BELOW=160 THEN GROUNDED=1: VY=0: GOTO 150
130 GROUNDED=0: VY=VY+1: REM GRAVITY
140 REM JUMP
150 IF PEEK(197)=60 AND GROUNDED THEN VY=-3
```

---

### Game 7: Speed Circuit

| Aspect | Details |
|--------|---------|
| **Units** | 8 |
| **Genre** | Top-down racing |
| **Concepts** | Track design, timing, collision |
| **Graphics** | Character-based track |

**What You Build:**
- Car (character)
- Track (custom characters)
- Lap counting
- Timer
- Grass slowdown

**Skills Introduced:**
- Track design with custom characters
- Timer using TI variable
- Checkpoint detection
- Different surface effects
- Lap logic
- Best time tracking

**Key Code:**
```basic
100 REM CHECK SURFACE
110 SURFACE=PEEK(1024+CY*40+CX)
120 IF SURFACE=32 THEN SPEED=1: REM GRASS - SLOW
130 IF SURFACE=160 THEN SPEED=3: REM ROAD - FAST
140 TI$="000000": REM RESET TIMER
```

---

### Game 8: Block Slider

| Aspect | Details |
|--------|---------|
| **Units** | 16 |
| **Genre** | Sokoban-style puzzle |
| **Concepts** | Puzzle logic, undo, level design |
| **Graphics** | Character-based (perfect fit) |

**What You Build:**
- Push-block mechanics
- Multiple levels
- Win detection
- Move counter
- Simple undo

**Skills Introduced:**
- Puzzle state management
- Level data structures
- Push logic (check two ahead)
- Array-based undo
- Multiple levels from DATA
- Victory detection

**Key Code:**
```basic
100 REM CHECK PUSH
110 NX=PX+DX: NY=PY+DY: REM NEXT CELL
120 BX=NX+DX: BY=NY+DY: REM BEYOND THAT
130 NC=PEEK(1024+NY*40+NX): BC=PEEK(1024+BY*40+BX)
140 IF NC=66 AND BC=32 THEN GOSUB 500: REM PUSH BOX
```

**Capstone:** Sokoban works beautifully with character graphics - this is the ideal C64 BASIC puzzle game.

---

## Skill Progression

### By Game

| Game | Primary Skills |
|------|----------------|
| 1 | Variables, conditionals, loops |
| 2 | Strings, arrays, DATA |
| 3 | PEEK/POKE, screen memory |
| 4 | Joystick, collision |
| 5 | Custom characters |
| 6 | Physics, gravity |
| 7 | Timing, surfaces |
| 8 | Complex state, levels |

### Key Memory Locations

| Address | Purpose |
|---------|---------|
| **1024-2023** | Screen memory |
| **55296-56295** | Colour memory |
| **53280** | Border colour |
| **53281** | Background colour |
| **56320** | Joystick port 2 |
| **197** | Current key pressed |
| **53272** | Character set location |

### Cumulative Skills

By end of track, students can:
- Write structured BASIC programs
- Use PEEK/POKE for hardware access
- Create custom characters
- Handle input (keyboard and joystick)
- Implement game loops
- Manage game state
- Design levels

---

## Optional: Exploring Assembly

### If Students Want to Go Deeper

The PEEK/POKE approach provides excellent preparation for assembly:

| BASIC Concept | Assembly Equivalent |
|---------------|---------------------|
| POKE 53280,0 | LDA #0 : STA $D020 |
| PEEK(56320) | LDA $DC00 |
| Screen memory | $0400+ |
| Colour memory | $D800+ |

### But Assembly is Not Required

The BASIC curriculum is **complete in itself**:
- 8 full games
- Real game development skills
- Historical authenticity
- Magazine type-ins worked exactly like this

Students who complete this track have learned to make games. That's the goal.

---

## Technical Requirements

### No Extensions Needed

Just a C64 (or emulator):
```
LOAD "*",8
RUN
```

Or type programs in directly - exactly as it was done.

### Emulator Setup

Any C64 emulator works:
- VICE (x64)
- Frodo
- CCS64

No cartridges, no extensions, no special setup.

### File Format

Programs saved as:
```
SAVE "PROGRAM",8
```

---

## Comparison to Assembly Track

| Aspect | BASIC Track | Assembly Track |
|--------|-------------|----------------|
| **Barrier** | Low | Higher |
| **Speed** | Slower but playable | Full speed |
| **Detail** | PEEK/POKE level | Register level |
| **Games** | 8 | 16 |
| **Graphics** | Character-based | Sprites, bitmaps |
| **Authenticity** | Magazine type-ins | Professional dev |
| **Outcome** | Game design skills | Full system mastery |

---

## Notes for Instructors

### Common Struggles

| Issue | Solution |
|-------|----------|
| **BASIC line numbers** | Explain historical context |
| **PEEK/POKE confusion** | Memory map diagrams help |
| **Slow execution** | Frame expectations - it's BASIC |
| **GOTO confusion** | Teach structured patterns |
| **Character codes** | PETSCII reference charts |

### Historical Context

This is exactly how magazine type-ins worked:
- Programs published in CRASH, ZZAP!64, Compute!
- Readers typed them in character by character
- PEEK/POKE for everything
- Character graphics, not sprites
- Hundreds of games published this way

---

## Vault Entries

| Entry | Type |
|-------|------|
| `c64-basic-v2-games` | Culture |
| `magazine-type-ins` | Culture |
| `peek-poke-gaming` | Technique |

**New entries: 3**

---

## Summary

The C64 BASIC curriculum provides:
- **8 complete, playable games**
- **Stock BASIC V2 only** - no extensions needed
- **Historical authenticity** - exactly like magazine type-ins
- **PEEK/POKE mastery** - direct hardware access
- **Character-based graphics** - the authentic approach
- **A complete curriculum** - not just a stepping stone

Students completing this track have:
- Made real games using the same techniques as 1980s programmers
- Learned game design principles
- Understood C64 hardware through PEEK/POKE
- Created something they can share and be proud of

**That's success. That's the goal.**
