# Phase 0 Curriculum: BBC BASIC (Game-First Approach)

> **⚠️ STRUCTURED:** This curriculum uses granular documentation files for better organisation and context efficiency.

## Primary Documentation

**Start here:** [`phase-0/overview.md`](phase-0/overview.md)

This provides the Phase 0 overview with philosophy, structure, and learning outcomes tailored to the BBC Micro's unique characteristics.

## Detailed Documentation

| What you need | Where to find it |
|---------------|------------------|
| **Tier 1 details** (Discovery, L1-16) | [`phase-0/tier-1/README.md`](phase-0/tier-1/README.md) |
| **Tier 2 details** (Building, L17-32) | [`phase-0/tier-2/README.md`](phase-0/tier-2/README.md) |
| **Tier 3 details** (Mastery, L33-48) | [`phase-0/tier-3/README.md`](phase-0/tier-3/README.md) |
| **Tier 4 details** (Limits, L49-64) | [`phase-0/tier-4/README.md`](phase-0/tier-4/README.md) |
| **Individual lesson specs** | [`phase-0/tier-{1,2,3,4}/lesson-NNN.md`](phase-0/) |

## Why This Structure?

**Organised by tier and lesson**

**Benefits:**
- **60-70% less context** when working on specific lessons
- **Better organisation** with clear hierarchy (phase → tier → lesson)
- **Easier navigation** to find specific content
- **Scalable** for all phases and platforms

## BBC Micro-Specific Features

This curriculum highlights the BBC Micro's unique characteristics:

- **Sophisticated BASIC** - Structured programming with PROCedures and FUNctions
- **Integrated assembler** - Seamlessly mix BASIC and 6502 assembly
- **Robust operating system** - MOS provides extensive system calls
- **MODE 7 teletext graphics** - Hardware-accelerated text-based graphics
- **Educational design** - Government-funded computer literacy project
- **Professional tools** - *EDIT, *SAVE, *LOAD commands and comprehensive editor
- **Fast execution** - Compiled BASIC tokens run efficiently
- **Multiple graphics modes** - MODE 0-7 for different resolutions and colour depths

## Curriculum Structure

### Phase 0: BBC BASIC Gateway (64 lessons)

**Total:** 64 lessons across 4 tiers
**Outcome:** 10 complete original games, programming fundamentals through gameplay

### Tier Breakdown

**Tier 1 (L1-16):** Discovery
- 4 foundation games introducing BASIC concepts
- Simple text interaction, number games, basic graphics
- PRINT, INPUT, IF/THEN, FOR/NEXT, MODE commands
- 5-30 lines per game

**Tier 2 (L17-32):** Building
- 3 technical games exploring hardware capabilities
- Graphics primitives (PLOT, DRAW, CIRCLE)
- Sound (SOUND, ENVELOPE)
- Simple sprite-like movement
- 25-80 lines per game

**Tier 3 (L33-48):** Mastery
- 2 professional-quality games
- PROCedures and FUNctions for code organisation
- Data structures and arrays
- Complex game logic
- 45-150 lines per game

**Tier 4 (L49-64):** Limits
- 1 ambitious game demonstrating BASIC ceiling
- Introduction to assembly integration
- Complex systems pushing BASIC capabilities
- Natural transition motivation to Phase 1
- 80-200 lines

## Original Games for Phase 0

### Tier 1: Discovery (4 games)

1. **"Number Guess"** (L1-4)
   - Guess the number game with feedback
   - **Playable:** Lesson 1
   - Introduces: PRINT, INPUT, IF/THEN, RND

2. **"Text Quest"** (L5-8)
   - Simple text adventure with 4-5 rooms
   - **Playable:** Lesson 5
   - Introduces: String variables, GOTO, simple branching

3. **"Shape Drawer"** (L9-12)
   - Draw shapes on screen with graphics primitives
   - **Playable:** Lesson 9
   - Introduces: MODE, PLOT, DRAW, GCOL, coordinate system

4. **"Target Practice"** (L13-16)
   - Press key when target appears
   - **Playable:** Lesson 13
   - Introduces: TIME, GET, timing loops, scoring

### Tier 2: Building (3 games)

5. **"Dot Collector"** (L17-24)
   - Move character collecting dots (like Snake but without growing)
   - **Playable:** Lesson 19
   - Introduces: Character redefinition, keyboard input, arrays, collision
   - **Pattern focus:** Character movement, simple collision

6. **"Paddle Ball"** (L25-32)
   - Pong-style paddle and ball game
   - **Playable:** Lesson 27
   - Introduces: Ball physics, paddle control, scoring, SOUND
   - **Pattern focus:** Simple physics, bouncing

7. **"Space Rocks"** (L33-40)
   - Simple shooting game with rocks to destroy
   - **Playable:** Lesson 35
   - Introduces: Shooting mechanics, multiple objects, explosion effects
   - **Pattern focus:** Multiple objects, projectiles

### Tier 3: Mastery (2 games)

8. **"Maze Chase"** (L41-48)
   - Navigate maze, avoid enemy, collect items
   - **Playable:** Lesson 43
   - Introduces: PROCedures, maze data, simple chase AI
   - **Pattern focus:** Structured programming, basic AI

9. **"Platform Jump"** (L49-56)
   - Single-screen platformer with jump physics
   - **Playable:** Lesson 51
   - Introduces: Gravity, jumping, platform collision
   - **Pattern focus:** Jump physics, platform detection

### Tier 4: Limits (1 game)

10. **"Breakout"** (L57-64)
    - Paddle, ball, bricks - pushes BASIC to its limits
    - **Playable:** Lesson 59
    - Shows where BASIC struggles (speed, many objects)
    - Hints at assembly solution in final lessons
    - Natural motivation for Phase 1 transition
    - **Pattern focus:** BASIC ceiling, performance limits

## Unique BBC Micro Advantages

### Integrated Assembly
Unlike C64 or Spectrum, BBC BASIC includes a full 6502 assembler. Students can:
- Write assembly code within BASIC programs
- Call assembly routines from BASIC seamlessly
- Gradually transition from BASIC to assembly
- Learn assembly in context of existing programs

### Example (Tier 4 preview):
```basic
10 REM Fast sprite movement using assembly
20 DIM code% 100
30 FOR pass% = 0 TO 3 STEP 3
40 P% = code%
50 [OPT pass%
60 .sprite_move
70   LDA x_pos
80   CLC
90   ADC x_velocity
100  STA x_pos
110  RTS
120 ]
130 NEXT
140 CALL code%
```

### Professional Development Environment
- *EDIT command for full-screen editing
- *SAVE and *LOAD with file system support
- Error handling with ON ERROR
- Comprehensive debugger
- OS calls accessible from BASIC

## Learning Outcomes

Upon completing Phase 0, students will have:

**Programming Fundamentals:**
- Variables, conditionals, loops, procedures
- Structured programming with PROCedures and FUNctions
- Data structures and arrays
- String manipulation
- File I/O

**BBC Micro-Specific Knowledge:**
- Multiple graphics modes (MODE 0-7)
- Graphics primitives (PLOT, DRAW, CIRCLE, POINT)
- Sound synthesis (SOUND, ENVELOPE)
- Keyboard input (GET, INKEY)
- System timer (TIME)
- OS calls basics

**Game Development Skills:**
- Game loop structure
- Input handling
- Collision detection
- Score and lives systems
- Simple AI
- Physics simulation basics
- Procedural generation concepts

**Assembly Preview:**
- Understanding why assembly is needed
- Basic familiarity with assembler syntax
- Integration patterns between BASIC and assembly
- Natural motivation for Phase 1

## Why BBC BASIC is Special

1. **Most sophisticated 8-bit BASIC** - Structured programming features
2. **Integrated assembly** - Unique among 8-bit platforms
3. **Educational mandate** - Designed for learning, not just gaming
4. **Professional tools** - Editor, file system, error handling
5. **Multiple audiences** - Hobbyists, students, professionals
6. **Government backing** - Computer Literacy Project created established curriculum

## Comparison with C64 and Spectrum BASIC

| Feature | BBC Micro | C64 | Spectrum |
|---------|-----------|-----|----------|
| **Speed** | Fast | Slow | Very Fast |
| **Structure** | PROCs/FNs | Line numbers only | Line numbers only |
| **Assembly** | Integrated | Separate | Separate |
| **Graphics** | MODE system, primitives | POKE only | PLOT, DRAW, CIRCLE |
| **Editor** | Full-screen | Line-by-line | Line-by-line with keywords |
| **OS Integration** | Extensive | Limited | Minimal |

## Navigation

- **View all phases:** [`./`](./)
- **Hardware references:** Coming soon (6502, 6845 CRTC, 6522 VIA)
- **Documentation index:** [`../START-HERE.md`](../START-HERE.md)

---

**Last updated:** 2025-11-04
**Version:** 1.0
**Status:** Overview complete, tier details and individual lessons to be created
