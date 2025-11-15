# Phase 0 Specification: Gateway Languages

**Version:** 1.0
**Last Updated:** 2025-01-15
**Purpose:** Complete specification for Phase 0 gateway/beginner content across platforms with high-level languages.

---

## Overview

Phase 0 is the optional beginner on-ramp for platforms with accessible high-level languages (BASIC, FORTH, etc.). It introduces programming fundamentals and game development concepts before transitioning to assembly language in Phase 1.

**Target Audience:**
- Complete programming novices
- Children (or their parents teaching them)
- Learners who want gentle introduction before assembly

**Key Principles:**
- Game-first approach (same as Phases 1-8)
- Simple, achievable, immediate results
- Build complete games early
- Demonstrate hardware capabilities
- Show BASIC limitations naturally (not preachy)
- Foundation for assembly concepts

---

## Structure

### Lesson Count

**Total Phase 0:** 64 lessons per platform
- **Tier 1:** 32 lessons (Lessons 1-32)
- **Tier 2:** 32 lessons (Lessons 33-64)

**Rationale:**
- 64 lessons provides solid foundation without overwhelming beginners
- 2 tiers allow natural progression (simple → complex)
- Each tier builds a complete game genre
- Manageable scope for young/novice learners

### Numbering

Phase 0 lessons are numbered 1-64 (not 0-63):
- Phase 0, Tier 1, Lesson 1 = Lesson 1
- Phase 0, Tier 1, Lesson 32 = Lesson 32
- Phase 0, Tier 2, Lesson 1 = Lesson 33
- Phase 0, Tier 2, Lesson 64 = Lesson 64

Phase 1 starts at lesson 65 (assembly begins).

---

## Platform Coverage

### Platforms with Phase 0

Phase 0 exists for any platform with a suitable high-level language:

| Platform | Language | Phase 0? | Notes |
|----------|----------|----------|-------|
| Commodore 64 | BASIC V2 | ✓ | Built-in, accessible, well-documented |
| Sinclair ZX Spectrum | Sinclair BASIC | ✓ | Built-in, beginner-friendly |
| Commodore Amiga | AMOS BASIC | ✓ | Game-focused BASIC variant |
| Nintendo NES | None | ✗ | No built-in BASIC - starts at Phase 1 (assembly) |
| Jupiter Ace | FORTH | ✓ | If platform covered - FORTH as gateway |
| Atari 8-bit | Atari BASIC | ✓ | If platform covered |
| BBC Micro | BBC BASIC | ✓ | If platform covered |
| MSX | MSX-BASIC | ✓ | If platform covered |

**Criteria for Phase 0 inclusion:**
- Platform has built-in or widely-available high-level language
- Language is accessible to beginners (not requiring compilation setup)
- Language can produce immediate visual/interactive results
- Language was historically used for learning/hobbyist development

---

## Tier Structure

### Tier 1: Foundation (Lessons 1-32)

**Genre Focus:** Simple arcade/action game (platform-appropriate)
- C64: Maze chase or simple shooter
- ZX Spectrum: Maze chase or collection game
- Amiga: Simple arcade game with BOBs

**Learning Progression:**
1. **Lessons 1-8:** Programming fundamentals
   - First program (Hello World equivalent)
   - Variables and simple math
   - Input (keyboard/joystick basics)
   - Loops (FOR...NEXT, GOTO)
   - Conditionals (IF...THEN)
   - Simple graphics (PRINT, POKE, or platform equivalent)
   - Simple sound
   - Data structures (DATA/READ or arrays)

2. **Lessons 9-16:** Interactive elements
   - Screen layout and design
   - Player character display
   - Movement (keyboard/joystick control)
   - Boundary detection
   - Simple collision detection
   - Score display
   - Lives/health system
   - Game state (start, playing, game over)

3. **Lessons 17-24:** Game mechanics
   - Enemy/obstacle creation
   - Enemy movement patterns
   - Sprite/character animation
   - Multiple enemies
   - Collectibles/power-ups
   - Level progression
   - Difficulty scaling
   - Sound effects integration

4. **Lessons 25-32:** Complete game polish
   - Title screen
   - Instructions/help screen
   - High score system
   - Game over sequence
   - Restart functionality
   - Final integration
   - Testing and debugging
   - **Lesson 32: Complete Tier 1 game**

**Outcome:** By Lesson 32, learner has created a complete, playable arcade game in BASIC.

---

### Tier 2: Expansion (Lessons 33-64)

**Genre Focus:** Different game style or advanced mechanics
- C64: Platformer or adventure game
- ZX Spectrum: Platformer or puzzle game
- Amiga: Multi-screen adventure or shoot-em-up

**Learning Progression:**
1. **Lessons 33-40:** Advanced concepts
   - Subroutines/procedures (GOSUB structure)
   - Arrays and data tables
   - Screen scrolling (simple)
   - Multi-screen levels
   - String manipulation
   - File I/O (save/load if applicable)
   - Timer-based gameplay
   - Advanced collision systems

2. **Lessons 41-48:** Hardware exploration
   - Direct hardware access (PEEK/POKE)
   - Custom character sets/graphics
   - Hardware sprites (if available)
   - Sound chip programming (SID, beeper, AY, Paula)
   - Color manipulation
   - Raster effects (simple, if possible)
   - Memory management basics
   - Understanding hardware limitations

3. **Lessons 49-56:** Complex game mechanics
   - Multiple game states
   - Enemy AI (simple)
   - Physics (gravity, inertia)
   - Power-up systems
   - Inventory/status screens
   - Boss encounters
   - Procedural generation (simple)
   - Difficulty balancing

4. **Lessons 57-64:** Complete second game
   - Game design and planning
   - Code organization strategies
   - Performance optimization (BASIC level)
   - Demonstrating BASIC limitations (speed/complexity)
   - Assembly preview concepts
   - Complete Tier 2 game
   - **Lesson 64: Transition preparation**

**Outcome:** By Lesson 64, learner has created TWO complete games and understands why assembly is beneficial.

---

## Pedagogical Approach

### Game-First Philosophy

Every lesson should connect to game development:

**DO:**
- Show immediate visual/interactive results
- Build toward playable prototypes
- Use game-relevant examples (sprites, sound effects, scoring)
- Demonstrate concepts through game mechanics
- Create something fun and shareable

**DON'T:**
- Abstract "learn to program" exercises divorced from games
- Mathematical/business examples
- Pure theory without application
- Defer game creation until "later"

---

### Progressive Complexity

**Early lessons (1-16):**
- 5-15 line programs
- Single concepts per lesson
- Immediate results
- Lots of experimentation suggestions
- Forgiving error handling

**Mid lessons (17-48):**
- 15-40 line programs
- Combining concepts
- Building reusable subroutines
- Multiple examples showing variations
- Debugging guidance

**Late lessons (49-64):**
- 40-80 line programs
- Complete systems
- Code organization strategies
- Performance considerations
- Preparing for assembly transition

---

### Platform Hardware Awareness

Introduce hardware concepts appropriate to the language:

**BASIC Level:**
```basic
10 REM C64 BASIC - DIRECT HARDWARE ACCESS
20 POKE 53280,0
30 POKE 53281,6
40 POKE 53265,11
```

**Explanation Level:**
- "The VIC-II chip controls the display"
- "We're writing to hardware registers"
- "The numbers are memory addresses the chip reads"
- **NOT:** Full VIC-II register documentation (save for assembly)

**Goal:** Learner understands they're controlling hardware, but details come in Phase 1.

---

### Demonstrating BASIC Limitations

**Natural Discovery (Good):**
```markdown
## Why This Runs Slowly

Your game updates the screen 50 times per second, but BASIC can only
recalculate positions about 10-20 times per second. This is why movement
feels jerky with multiple enemies.

Assembly language can update positions hundreds of times per second,
creating smooth motion. We'll learn assembly in Phase 1.
```

**Preachy Comparison (Bad):**
```markdown
## BASIC Is Too Slow

BASIC is an interpreted language, making it much slower than assembly.
Professional games never used BASIC because it's not fast enough. You
should learn assembly instead.
```

**Approach:**
- Let learner discover limitations through experience
- Mention assembly as solution, not criticism of BASIC
- Respect BASIC as teaching tool
- Show what's POSSIBLE in BASIC, acknowledge where it struggles
- Phase 1 is enhancement, not replacement

---

## Transition to Phase 1

### Lesson 64: Bridge to Assembly

The final Phase 0 lesson should:

1. **Celebrate accomplishments:**
   - "You've created two complete games"
   - "You understand programming fundamentals"
   - "You can control hardware through BASIC"

2. **Identify current limitations:**
   - "Our games slow down with many enemies"
   - "Scrolling is choppy"
   - "Complex graphics take too long to draw"

3. **Preview assembly benefits:**
   - "Assembly gives direct CPU control"
   - "Same hardware, but 50-100× faster"
   - "Professional game techniques become possible"

4. **Set expectations:**
   - "Assembly is more complex but we'll learn gradually"
   - "Same concepts (variables, loops, conditionals) in different syntax"
   - "We'll rebuild familiar game mechanics at full speed"

5. **Provide continuity:**
   - Link to Phase 1, Tier 1, Lesson 1 (Lesson 65)
   - Note that assembly starts simple (like Phase 0 did)
   - Reassure that hardware knowledge carries forward

**NO:**
- Don't trash BASIC
- Don't imply learner wasted time
- Don't make assembly sound scary
- Don't require assembly (some may stop at Phase 0)

---

## Phase 0 Tier Themes

### Tier 1 Themes by Platform

| Platform | Tier 1 Genre | Rationale |
|----------|--------------|-----------|
| C64 | Maze Chase | Simple collision, PETSCII graphics, immediate results |
| ZX Spectrum | Collection Game | UDG characters, simple movement, attribute colors |
| Amiga | Arcade Shooter | BOBs for sprites, simple controls, immediate feedback |

### Tier 2 Themes by Platform

| Platform | Tier 2 Genre | Rationale |
|----------|--------------|-----------|
| C64 | Platformer | Gravity, jumping, multi-screen, introduces complexity |
| ZX Spectrum | Puzzle Platformer | Logical thinking, attribute management, screen design |
| Amiga | Shoot-em-up | Scrolling, multiple enemies, introduces performance limits |

**Note:** Specific themes can vary based on pedagogical goals, but should:
- Be different genre from Tier 1
- Introduce new challenges
- Demonstrate language capabilities and limitations
- Be completable in 32 lessons

---

## Content Guidelines

### Code Examples

**Tier 1 Style (NO INDENTATION):**
```basic
10 REM SIMPLE ENEMY MOVEMENT
20 X=100:Y=50
30 X=X+1
40 IF X>300 THEN X=10
50 POKE 53248,X
60 POKE 53249,Y
70 GOTO 30
```

- Straightforward, linear logic
- Minimal optimization
- Clear variable names
- Comments explain purpose
- **NO indentation - all lines flush left**

**Tier 2 Style (NO INDENTATION):**
```basic
10 REM ENEMY MANAGEMENT SYSTEM
20 DIM EX(5),EY(5),ED(5)
30 FOR I=1 TO 5
40 EX(I)=RND(1)*300:EY(I)=RND(1)*200
50 ED(I)=RND(1)*4
60 NEXT I
70 REM MAIN LOOP
80 FOR I=1 TO 5
90 GOSUB 1000
100 NEXT I
110 GOTO 80
1000 REM UPDATE SINGLE ENEMY
1010 ON ED(I) GOTO 1100,1200,1300,1400
1100 EX(I)=EX(I)+1:RETURN
1200 EX(I)=EX(I)-1:RETURN
1300 EY(I)=EY(I)+1:RETURN
1400 EY(I)=EY(I)-1:RETURN
```

- Structured with subroutines
- Arrays for multiple entities
- Code reuse patterns
- Organized, maintainable
- **NO indentation - all lines flush left**

---

### Writing Style

**Tone:**
- Encouraging and friendly
- Patient and clear
- Enthusiastic but not condescending
- Age-appropriate for children/young learners

**Examples:**

**Good (Tier 1):**
```markdown
Let's make our player move! We'll use the joystick to control the X and Y
position. Type this program and try moving in all directions.
```

**Good (Tier 2):**
```markdown
This subroutine checks collision between the player and all enemies. We'll
use a FOR loop to test each enemy position against the player's position.
```

**Bad (too childish):**
```markdown
Yay! Let's make the super-duper player sprite zoom around! This is going
to be SO MUCH FUN!!!
```

**Bad (too complex):**
```markdown
Implement a collision detection algorithm utilizing Cartesian coordinate
comparison with boundary intersection testing via conditional branching.
```

---

### Screenshot Requirements

Same as Phases 1-8:
- Every visual example MUST have screenshot
- Use Read tool to verify (no error messages, correct output)
- Screenshots show working, playable game states
- Capture progression (early → middle → final game)

---

### British English

Same standards as Phases 1-8:
- colour, learnt, optimise, grey
- EXCEPTION: "program" for computer programs

---

## Platform-Specific Notes

### Commodore 64 BASIC

**Advantages:**
- Built-in sprite support via POKE
- SID sound chip access
- Well-documented
- Immediate mode for experimentation

**Limitations:**
- Slow interpreter
- No named procedures (GOSUB line numbers)
- Limited string handling
- 38KB program space

**Focus:**
- VIC-II graphics (sprites, colors)
- SID sound effects
- Joystick input (CIA)
- PETSCII character graphics

**Code formatting:**
- NO indentation (BASIC V2 standard)
- Line numbers flush left
- Lowercase keywords in `.bas` files
- Uppercase keywords in MDX display

---

### Sinclair ZX Spectrum BASIC

**Advantages:**
- Built-in graphics commands (PLOT, DRAW, CIRCLE)
- UDG (User-Defined Graphics)
- Immediate mode
- Keyword entry system

**Limitations:**
- No hardware sprites (software sprites only)
- Attribute clash
- Slow BASIC interpreter
- Beeper sound only (unless AY expansion)

**Focus:**
- Software sprite techniques
- UDG character creation
- Attribute color management
- Keyboard input
- DRAW/PLOT graphics

**Code formatting:**
- NO indentation (Sinclair BASIC standard)
- Line numbers flush left
- Lowercase keywords in `.bas` files
- Uppercase keywords in MDX display

---

### Commodore Amiga AMOS BASIC

**Advantages:**
- BOB (Blitter Object) sprite system
- Structured programming (procedures)
- Fast interpreter
- Built-in game commands

**Limitations:**
- Requires AMOS software (not built-in)
- Simplified hardware access
- Less educational about hardware

**Focus:**
- BOB sprite management
- Screen modes and palettes
- AMOS game commands
- Music and sound
- Copper effects (simple)

**Code formatting:**
- AMOS may support indentation (verify per platform)
- Check AMOS BASIC syntax standards

---

## Frontmatter Example

Phase 0 lessons use same frontmatter structure:

```yaml
---
title: "Your First Moving Sprite"
description: "Control a hardware sprite with joystick input, creating the foundation for player movement in your maze chase game."
pubDate: 2025-01-15
phase: 0
tier: 1
lessonNumber: 12
tags: ["basic", "sprites", "input", "vic-ii"]
prevLesson: "/commodore-64/phase-0/tier-1/lesson-011"
nextLesson: "/commodore-64/phase-0/tier-1/lesson-013"
layout: "../../../../layouts/LessonLayout.astro"
---
```

**Note:** `phase: 0` distinguishes Phase 0 from assembly phases.

---

## Validation Checklist

Phase 0 lessons must:

- [ ] Code runs on target platform BASIC interpreter
- [ ] Screenshots verified with Read tool
- [ ] No error messages in screenshots
- [ ] **NO indentation in BASIC code (flush left line numbers)**
- [ ] Game-relevant examples (not abstract exercises)
- [ ] Age-appropriate language (children/novices)
- [ ] British English (except "program")
- [ ] Platform-specific BASIC syntax correct
- [ ] Builds toward complete game by tier end
- [ ] Demonstrates hardware concepts appropriately
- [ ] Mentions assembly naturally (not preachy)

---

## Lesson Progression Example: C64 Tier 1

### Sample Outline (First 16 Lessons)

1. **Hello, Computer** - First program, PRINT, immediate results
2. **Counting On It** - Variables, simple math, FOR loops
3. **Making Choices** - IF...THEN, conditionals, branching
4. **The First Colour** - POKE to VIC-II, border/background colors
5. **Drawing With Characters** - PRINT positioning, PETSCII graphics
6. **Your First Sound** - POKE to SID, simple tones
7. **Reading the Joystick** - PEEK from CIA, directional input
8. **Data and Memory** - DATA/READ for level data
9. **The Game Screen** - Layout design, status area, play area
10. **A Character Appears** - Player character display with PETSCII
11. **Take Control** - Joystick controls player position
12. **Staying Inside** - Boundary checking, screen limits
13. **The Enemy Arrives** - First enemy character, simple movement
14. **Collision Detection** - Player/enemy overlap detection
15. **Score and Lives** - Display game stats, update on events
16. **Game Over** - End state, restart option

### Lessons 17-32 Continue:
- Multiple enemies, maze/level design, collectibles, sound effects, animation,
  difficulty progression, title screen, polish → Complete maze chase game at Lesson 32

---

## Future Platform Additions

When adding new platforms with Phase 0:

1. **Verify language availability:**
   - Built-in or widely available?
   - Beginner-accessible?
   - Can produce interactive graphics/sound?

2. **Identify platform strengths:**
   - Graphics capabilities (sprites, UDG, custom characters)
   - Sound system (chip, beeper, samples)
   - Input methods (keyboard, joystick, mouse)

3. **Choose appropriate genres:**
   - Tier 1: Simple, immediate-feedback game
   - Tier 2: More complex, demonstrates limitations

4. **Document platform-specific notes:**
   - Unique BASIC syntax
   - Hardware access methods
   - Common pitfalls
   - Limitations
   - **Indentation rules (most early BASIC: NO indentation)**

5. **Create validation tools:**
   - BASIC syntax validators if needed
   - Emulator screenshot capture process
   - Testing procedures

---

## Version History

- **1.0 (2025-01-15):** Initial Phase 0 specification
  - 64 lessons across 2 tiers
  - Game-first approach
  - Platform coverage criteria
  - Transition to Phase 1 strategy
  - **CRITICAL:** NO indentation in BASIC code
