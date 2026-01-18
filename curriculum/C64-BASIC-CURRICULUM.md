# C64 BASIC Curriculum

**Purpose:** Define the 8-game BASIC curriculum track for Commodore 64 - a complete game development curriculum using Simons' BASIC.

**Last Updated:** 2026-01-18

---

## Overview

| Aspect | Details |
|--------|---------|
| **Track** | BASIC |
| **Platform** | Commodore 64 |
| **Games** | 8 |
| **Prerequisite** | None |
| **BASIC Version** | BASIC V2 + Simons' BASIC |
| **Outcome** | Complete, playable games |

---

## Philosophy

### Why BASIC?

| Reason | Benefit |
|--------|---------|
| **Immediate results** | Type and run |
| **Focus on game design** | Logic and creativity, not hardware registers |
| **Rapid iteration** | Quick testing cycle |
| **Historical authenticity** | Many learned this way |
| **Complete curriculum** | Real games, not just exercises |
| **Commercially viable** | Games were sold written in BASIC |

### Why Simons' BASIC?

Stock C64 BASIC V2 is inadequate for games:
- No sprite commands
- No sound commands
- No graphics commands

**Simons' BASIC** adds 114 commands making game development practical.

**Alternative:** Could use other extensions (Laser BASIC, etc.) but Simons' BASIC is well-documented and historically significant.

---

## Game Sequence

### Game 1: Number Guess
**"Psychic Computer"**

| Aspect | Details |
|--------|---------|
| **Units** | 8 |
| **Genre** | Number guessing |
| **Concepts** | Variables, input, conditionals, loops |
| **BASIC** | Stock BASIC V2 (no extension needed) |

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

### Game 2: Text Adventure
**"The Forgotten Key"**

| Aspect | Details |
|--------|---------|
| **Units** | 8 |
| **Genre** | Text adventure |
| **Concepts** | Strings, arrays, data structures |
| **BASIC** | Stock BASIC V2 |

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

### Game 3: Snake
**"Pixel Serpent"**

| Aspect | Details |
|--------|---------|
| **Units** | 8 |
| **Genre** | Snake/growth game |
| **Concepts** | Screen characters, movement, collision |
| **BASIC** | Stock BASIC V2 with PEEK/POKE |

**What You Build:**
- Character-based snake
- Food collection
- Growth mechanic
- Wall collision

**Skills Introduced:**
- PEEK and POKE (introduction)
- Screen memory (1024)
- Keyboard reading
- Game loop concept
- Collision detection (character)
- Screen coordinates

---

### Game 4: Breakout Clone
**"Wall Smasher"**

| Aspect | Details |
|--------|---------|
| **Units** | 8 |
| **Genre** | Breakout/brick breaker |
| **Concepts** | Movement, bounce physics, scoring |
| **BASIC** | Simons' BASIC (graphics commands) |

**What You Build:**
- Paddle (keyboard/joystick)
- Bouncing ball
- Breakable bricks
- Score display

**Skills Introduced:**
- **Simons' BASIC introduction**
- HIRES/MULTI graphics
- LINE, CIRCLE commands
- Joystick reading (JOY)
- Ball physics (angle reflection)
- Score tracking

**Transition Point:** This game introduces Simons' BASIC - students see the dramatic improvement over stock BASIC.

---

### Game 5: Space Shooter
**"Star Patrol"**

| Aspect | Details |
|--------|---------|
| **Units** | 8 |
| **Genre** | Fixed shooter |
| **Concepts** | Sprites, enemies, shooting |
| **BASIC** | Simons' BASIC |

**What You Build:**
- Player ship (sprite)
- Enemy waves
- Shooting
- Lives system

**Skills Introduced:**
- SPRITE commands
- MOB (moveable object blocks)
- Sprite collision
- Multiple sprites
- Wave patterns
- Lives/game over

---

### Game 6: Platform Game
**"Jump Quest"**

| Aspect | Details |
|--------|---------|
| **Units** | 8 |
| **Genre** | Single-screen platformer |
| **Concepts** | Gravity, jumping, platforms |
| **BASIC** | Simons' BASIC |

**What You Build:**
- Jumping character
- Platforms
- Collectibles
- Level completion

**Skills Introduced:**
- Gravity simulation
- Jump physics
- Platform collision
- Character animation (basic)
- Level design
- State (grounded/airborne)

---

### Game 7: Racing Game
**"Speed Circuit"**

| Aspect | Details |
|--------|---------|
| **Units** | 8 |
| **Genre** | Top-down racing |
| **Concepts** | Track, lap timing, obstacles |
| **BASIC** | Simons' BASIC |

**What You Build:**
- Car (sprite)
- Track (character graphics)
- Lap counting
- Timer

**Skills Introduced:**
- Character set graphics
- Track/boundary collision
- Timer implementation
- Lap logic
- Speed/acceleration

---

### Game 8: Puzzle Game
**"Block Slider"**

| Aspect | Details |
|--------|---------|
| **Units** | 8 |
| **Genre** | Sokoban-style puzzle |
| **Concepts** | Puzzle logic, undo, level design |
| **BASIC** | Simons' BASIC |

**What You Build:**
- Push-block mechanics
- Multiple levels
- Win detection
- Move counter

**Skills Introduced:**
- Puzzle state management
- Level data structures
- Push mechanics
- Undo system (array-based)
- Multiple levels from DATA

**Capstone:** This game brings together everything learned - logic, graphics, state management, level design.

---

## Skill Progression

### By Game

| Game | Primary Skills |
|------|----------------|
| 1 | Variables, conditionals, loops |
| 2 | Strings, arrays, DATA |
| 3 | PEEK/POKE, screen memory |
| 4 | Simons' BASIC graphics |
| 5 | Sprites, collision |
| 6 | Physics, state |
| 7 | Custom characters, timing |
| 8 | Complex state, levels |

### Cumulative Skills

By end of track, students can:
- Write structured BASIC programs
- Use Simons' BASIC commands
- Create sprites and graphics
- Handle input (keyboard and joystick)
- Implement game loops
- Manage game state
- Design levels

---

## Optional: Exploring Assembly

### If Students Want to Go Deeper

Some students may be curious about assembly language. The BASIC curriculum provides excellent preparation:

| BASIC Concept | Assembly Equivalent |
|---------------|---------------------|
| POKE 53280,0 | LDA #0 : STA $D020 |
| SPRITE commands | VIC-II registers |
| JOY(1) | CIA port reading |
| Screen memory | $0400+ |

### But Assembly is Not Required

The BASIC curriculum is **complete in itself**:
- 8 full games
- Real game development skills
- Historical authenticity
- Commercial games were made in BASIC

Students who complete this track have learned to make games. That's the goal.

---

## Technical Requirements

### Simons' BASIC Setup

```
LOAD "SIMONS BASIC",8
RUN
```

Simons' BASIC adds commands including:

| Category | Commands |
|----------|----------|
| **Graphics** | HIRES, MULTI, LINE, CIRCLE, PAINT |
| **Sprites** | SPRITE, MOB, MOBC |
| **Sound** | VOL, ENVELOPE |
| **Input** | JOY, PEN |
| **Utility** | RENUMBER, AUTO, etc. |

### Emulator Setup

VICE with Simons' BASIC cartridge image:
```
x64 -cart8 simons.crt
```

### File Format

Programs saved as:
```
SAVE "PROGRAM",8
```

---

## Sample Unit Structure

### Game 4, Unit 3: "Adding the Ball"

**Duration:** 60-90 minutes

**Objectives:**
- Create ball sprite
- Implement movement
- Add screen boundary bouncing

**BASIC Code:**

```basic
100 REM WALL SMASHER - UNIT 3
110 REM BALL MOVEMENT
120 HIRES 0,1: REM BLACK BG, WHITE FG
130 SPRITE 1,1,15,0,0: REM SPRITE 1 ON
140 BX=160: BY=100: REM BALL POSITION
150 DX=2: DY=-2: REM BALL DIRECTION
160 REM MAIN LOOP
170 BX=BX+DX: BY=BY+DY
180 IF BX<10 OR BX>310 THEN DX=-DX
190 IF BY<10 OR BY>190 THEN DY=-DY
200 MOB SET 1,BX,BY
210 GOTO 170
```

**What Students Learn:**
- Sprite positioning
- Direction variables
- Boundary checking
- Sign flipping for bounce

---

## Comparison to Assembly Track

| Aspect | BASIC Gateway | Assembly Track |
|--------|---------------|----------------|
| **Barrier** | Low | Higher |
| **Speed** | Slow but workable | Full speed |
| **Detail** | Abstracted | Hardware level |
| **Games** | 8 | 16 |
| **Duration** | Shorter units | Longer units |
| **Outcome** | Game design skills | Full system mastery |

---

## Notes for Instructors

### Common Struggles

| Issue | Solution |
|-------|----------|
| **BASIC line numbers** | Explain historical context |
| **Simons' BASIC setup** | Provide ready emulator configs |
| **Slow execution** | Frame expectations |
| **GOTO confusion** | Teach structured patterns |

### Historical Context

Include notes about:
- Why C64 BASIC was limited
- How people actually made games
- Magazine type-ins
- The path to assembly

---

## Vault Entries

| Entry | Type |
|-------|------|
| `c64-basic-gateway` | Curriculum |
| `simons-basic-games` | Culture |

**New entries: 2**

---

## Summary

The C64 BASIC curriculum provides:
- **8 complete, playable games**
- **Real game development skills**
- **Historical authenticity** - this is how people learned
- **Practical, transferable knowledge**
- **A complete curriculum** - not just a stepping stone

Students completing this track have:
- Made real games
- Learned game design
- Understood programming concepts
- Created something they can share and be proud of

**That's success. That's the goal.**
