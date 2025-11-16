# Commodore 64 Phase 0 Tier 1 Curriculum

**Platform:** commodore-64
**Phase:** 0 (BASIC V2)
**Tier:** 1 (Discovery - Foundation)
**Total Lessons:** 16
**Target Audience:** Complete beginners (including children)
**End Goal:** Playable falling catcher game with polish and understanding

---

## Curriculum Philosophy

### Game-First Learning
- **Lesson 1:** Immediate interaction (character moves on screen)
- **Lessons 1-3:** Build game-like feel quickly
- **Lessons 5-8:** PLAYABLE GAME (falling catcher)
- **Lessons 9-16:** Polish, features, deeper understanding

### Spiral Learning
- First pass: Quick implementation (get it working)
- Second pass: Understanding and refinement (why it works, how to improve)
- Third pass: Creative expansion (make it your own)

### Lesson-Level Pacing
- Each lesson adds ONE clear concept
- Immediate application to the game
- Build confidence through progressive wins
- By lesson 8: Complete playable game
- By lesson 16: Polished game + deep understanding

---

## The Game: Falling Catcher

A simple but engaging game where:
- Objects fall from the top of the screen
- Player moves a catcher left/right at the bottom
- Goal: Catch falling objects to score points
- Challenge: Speed increases, different object types appear

**Why this game?**
- Teaches fundamental game loop: INPUT → UPDATE → DRAW → REPEAT
- Natural progression from simple to complex
- Works perfectly in text mode (no sprites needed yet)
- Timeless mechanic that's still fun today
- Everything learned applies to other game types

---

## Tier 1 Lesson Breakdown

### Act 1: Interactive Foundation (Lessons 1-3)

#### **Lesson 1: Your First Command**
**Core Concept:** Getting something on screen, making it respond to input
**What You Build:** Character that moves left/right with keyboard
**New Syntax:** `PRINT`, `GET`, `IF...THEN`, basic game loop
**Learning Goal:** Immediate interaction - program responds to you
**Prerequisites:** None (absolute beginner)

**Key Moment:** First time pressing a key makes something move on screen

---

#### **Lesson 2: Things That Appear**
**Core Concept:** Random positioning, screen codes, clearing screen
**What You Build:** Random object appears at top of screen
**New Syntax:** `RND()`, `INT()`, `POKE` for screen memory, screen codes
**Learning Goal:** Create variety - things appear in different places
**Prerequisites:** Lesson 1 (basic PRINT and variables)

**Key Moment:** Each run shows object in different position

---

#### **Lesson 3: Making Things Move**
**Core Concept:** Game loop with timing, vertical movement
**What You Build:** Object falls from top to bottom
**New Syntax:** `FOR...NEXT` delays, position updates in loops
**Learning Goal:** Continuous motion - things happen automatically
**Prerequisites:** Lessons 1-2 (screen positioning, variables)

**Key Moment:** Watching object fall smoothly down screen

---

### Act 2: First Playable Game (Lessons 4-8)

#### **Lesson 4: The Game Loop**
**Core Concept:** Proper game loop structure (init → loop → end)
**What You Build:** Continuous falling with player movement combined
**New Syntax:** `GOTO` for main loop, separating init/update/draw
**Learning Goal:** Game structure - how games are organized
**Prerequisites:** Lessons 1-3 (movement and falling separately)

**Key Moment:** Player and falling object both active at same time

---

#### **Lesson 5: When Things Touch**
**Core Concept:** Collision detection (position comparison)
**What You Build:** Detect when catcher touches falling object
**New Syntax:** Comparison operators, compound conditionals (`AND`)
**Learning Goal:** Game rules - detecting events that matter
**Prerequisites:** Lesson 4 (game loop with both objects active)

**Key Moment:** Object disappears when you catch it

---

#### **Lesson 6: Keeping Score**
**Core Concept:** Variables that persist, displaying game state
**What You Build:** Score counter that increases on catch
**New Syntax:** Variable incrementing, status display
**Learning Goal:** Persistence - game remembers what happened
**Prerequisites:** Lesson 5 (collision detection)

**Key Moment:** Score going up when you succeed

---

#### **Lesson 7: More Challenge**
**Core Concept:** Multiple objects, spawn timing
**What You Build:** Multiple falling objects at once
**New Syntax:** Arrays (or parallel variables), managing multiple entities
**Learning Goal:** Complexity - handling many things at once
**Prerequisites:** Lesson 6 (single object working with score)

**Key Moment:** Juggling multiple falling objects

---

#### **Lesson 8: Game Over**
**Core Concept:** Lives system, win/lose conditions, replay
**What You Build:** PLAYABLE GAME with lives, game over, restart
**New Syntax:** Game state tracking, end conditions, user prompts
**Learning Goal:** Complete game - start, play, end, replay
**Prerequisites:** Lessons 1-7 (all mechanics combined)

**Key Moment:** First complete playthrough - you made a real game!

---

### Act 3: Polish and Expand (Lessons 9-16)

#### **Lesson 9: Getting Harder**
**Core Concept:** Dynamic difficulty (speed progression)
**What You Build:** Game speeds up as score increases
**New Syntax:** Delay adjustment, difficulty curves
**Learning Goal:** Balance - keeping game challenging
**Prerequisites:** Lesson 8 (complete playable game)

**Key Moment:** Feeling the tension as game speeds up

---

#### **Lesson 10: Level Up**
**Core Concept:** Structured difficulty levels
**What You Build:** Explicit levels with thresholds
**New Syntax:** Level tracking, threshold checks
**Learning Goal:** Progression - giving players goals
**Prerequisites:** Lesson 9 (dynamic difficulty)

**Key Moment:** Screen showing "LEVEL 2" for first time

---

#### **Lesson 11: Good and Bad**
**Core Concept:** Multiple object types with different effects
**What You Build:** Bonus items (extra points) and penalties (lose life)
**New Syntax:** Type tracking, conditional scoring
**Learning Goal:** Variety - different objects = different strategies
**Prerequisites:** Lessons 7-8 (multiple objects, lives system)

**Key Moment:** Having to choose which objects to catch

---

#### **Lesson 12: Visual Language**
**Core Concept:** Using color and characters to communicate
**What You Build:** Color-coded objects, better visuals
**New Syntax:** Color codes (`POKE 646`), PETSCII characters
**Learning Goal:** Communication - visuals tell player what to do
**Prerequisites:** Lesson 11 (multiple object types)

**Key Moment:** Instantly recognizing good vs bad by color

---

#### **Lesson 13: Sound Matters**
**Core Concept:** Audio feedback for game events
**What You Build:** Sound effects for catch, miss, level up
**New Syntax:** `POKE` to sound registers (basic SID)
**Learning Goal:** Feedback - sound confirms player actions
**Prerequisites:** Lessons 6, 8, 10 (events that need sound)

**Key Moment:** Satisfying "bloop" when catching object

---

#### **Lesson 14: Making it Smoother**
**Core Concept:** Animation and timing refinement
**What You Build:** Smooth movement, visual polish
**New Syntax:** Timing optimization, better loops
**Learning Goal:** Feel - small improvements make big difference
**Prerequisites:** Lesson 4 (game loop to optimize)

**Key Moment:** Game feels more responsive and professional

---

#### **Lesson 15: First Impressions**
**Core Concept:** Title screen, instructions, high score display
**What You Build:** Professional presentation (start and end screens)
**New Syntax:** Screen layout, text formatting, data persistence
**Learning Goal:** Presentation - making game feel complete
**Prerequisites:** Lesson 8 (complete game to frame)

**Key Moment:** Seeing your game title on screen like real games

---

#### **Lesson 16: Understanding the Whole**
**Core Concept:** Code organization, documentation, extensibility
**What You Build:** Clean, commented, organized final version
**New Syntax:** `REM` comments, code organization patterns
**Learning Goal:** Craftsmanship - understanding every line
**Prerequisites:** Lessons 1-15 (complete game to document)

**Key Moment:** Realizing you understand how the whole thing works

---

## Learning Outcomes

By the end of Tier 1, students will:

### Programming Fundamentals
- ✅ Understand variables, conditionals, loops
- ✅ Write and structure a complete program
- ✅ Debug simple logic errors
- ✅ Read and modify existing code

### Game Development Concepts
- ✅ Implement core game loop (input, update, draw)
- ✅ Handle collision detection
- ✅ Manage game state (score, lives, level)
- ✅ Create difficulty progression
- ✅ Provide player feedback (visual and audio)

### C64-Specific Skills
- ✅ Use BASIC V2 syntax correctly
- ✅ Manipulate screen memory directly (`POKE`)
- ✅ Read keyboard input (`GET`)
- ✅ Generate random numbers (`RND`)
- ✅ Use PETSCII characters and color codes
- ✅ Create simple sound effects (basic SID)

### Confidence and Creativity
- ✅ Complete a real, playable game from scratch
- ✅ Understand how to extend and modify the game
- ✅ Ready to tackle new game ideas
- ✅ Prepared for assembly language (Phase 1)

---

## Transition to Tier 2

Tier 1 builds a complete falling catcher game and teaches fundamental programming through game development.

**Tier 2 (Lessons 17-32)** will introduce:
- Sprites (hardware-accelerated graphics)
- More complex game types (maze games, shooters)
- Advanced collision and physics
- Multi-level game structures
- Data structures for game content

The falling catcher serves as reference: students can compare sprite-based versions to their text-mode game, understanding what each technology brings.

---

## Notes for Lesson Authors

### Pacing Guidelines
- **Lessons 1-3:** Fast pace, immediate wins, build excitement
- **Lessons 4-8:** Steady build, each lesson adds clear value
- **Lessons 9-16:** Deeper exploration, refinement, understanding

### Code Complexity
- Lesson 1: ~10 lines
- Lesson 8: ~80-100 lines (complete game)
- Lesson 16: ~100-120 lines (polished with comments)

### Testing Requirements
- All code must compile with `petcat`
- All code must run without errors in VICE
- Screenshots must show expected output (no error messages)
- British English throughout (except "program" for computer programs)

### Vocabulary Progression
Introduce terms progressively:
- Lessons 1-3: Variable, loop, print, input
- Lessons 4-8: Game loop, collision, condition, array
- Lessons 9-16: State, difficulty curve, feedback, animation

---

**Document Status:** Complete and approved
**Date Created:** 2025-11-15
**Next Step:** Write Lesson 1 following this curriculum
