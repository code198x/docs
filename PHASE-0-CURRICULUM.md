# Phase 0 Curriculum: Commodore 64 BASIC

**Structure:** 64 lessons across 4 tiers (16 lessons each)
**Approach:** Spiral learning - touch concepts early, deepen through repetition
**Philosophy:** Hardware-aware from day one, honest about BASIC limitations

---

## Tier 1: Discovery (Lessons 1-16)

**Goal:** Foundation concepts + first hardware touch + first complete game
**End State:** Can write simple programs, understand memory/hardware basics, built a text adventure

### Lessons 1-6: Programming Foundations

**Lesson 1: Hello, Computer**
- PRINT, READY prompt, RUN, LIST, RUN/STOP
- Simple GOTO loop
- WOW: Infinite text scroll

**Lesson 2: Counting**
- Variables (A=5, B=10)
- Arithmetic operators
- WOW: Calculator program

**Lesson 3: Repeating Yourself**
- FOR...NEXT loops
- Loop counter usage
- WOW: Number patterns on screen

**Lesson 4: Making Decisions**
- IF...THEN, comparison operators
- Simple branching
- WOW: Number guessing game

**Lesson 5: Collections**
- Arrays with DIM
- Array indexing
- WOW: High score table

**Lesson 6: Data Everywhere**
- DATA, READ, RESTORE
- Separating data from logic
- WOW: Quiz program from DATA

### Lessons 7-11: Hardware Introduction

**Lesson 7: The First Color**
- Memory addresses concept
- POKE 53280 (border), 53281 (background)
- Hardware revelation: "You're controlling VIC-II registers"
- WOW: Rainbow border animation

**Lesson 8: Painting the Screen**
- Screen memory (1024-2023)
- Color memory (55296+)
- POKE to screen positions
- WOW: Pattern drawing (not just text)

**Lesson 9: Character Graphics**
- PETSCII characters
- CHR$() for special chars
- Graphics characters
- WOW: Border/box drawing

**Lesson 10: First Sound**
- SID chip at 54272
- Volume, frequency, waveform
- Bob Yannes designed this
- WOW: Play notes, simple melody

**Lesson 11: Sound Effects**
- ADSR envelopes
- Waveform types
- Duration control
- WOW: Explosion, beep, pickup sounds

### Lessons 12-15: Interactive Foundation

**Lesson 12: Listening to the Player**
- GET for keyboard input
- Non-blocking input
- WASD/cursor keys
- WOW: Move @ character around screen

**Lesson 13: Random Events**
- RND(1) random numbers
- Scaling ranges
- TI for seeding
- WOW: Random stars appearing

**Lesson 14: Game Logic Basics**
- Position-based collision
- Score tracking
- Win/lose conditions
- WOW: Catch falling objects (character-based)

**Lesson 15: Timing**
- TI jiffy clock
- Delay loops
- Frame timing concepts
- WOW: Countdown timer, timed challenge

### Lesson 16: SYNTHESIS - Text Adventure

**Combines:** Everything from Tier 1
**Builds:** Complete text adventure with:
- Colored rooms (POKE borders/background)
- Simple map navigation
- Item inventory
- Random enemy encounters
- Sound effects
- Win condition

**Honest framing:**
- "Slower than commercial games (they used assembly)"
- "You're controlling same hardware"
- "Next tier: sprites show BASIC's speed limits"

**Code:** 40-60 lines

---

## Tier 2: Building (Lessons 17-32)

**Goal:** Sprite-based games, deeper hardware, hitting BASIC speed limits naturally
**End State:** Built sprite game, understand VIC-II/SID/CIA chips, felt BASIC's ceiling

### Lessons 17-22: Sprites Introduced

**Lesson 17: Hardware Sprites**
- VIC-II sprite system overview
- 8 hardware sprites concept
- Sprite vs character graphics
- WOW: Single sprite appears

**Lesson 18: Sprite Shapes**
- Sprite pointers (2040-2047)
- 24×21 pixel format
- Designing sprite data
- DATA statements for sprites
- WOW: Custom sprite shape (spaceship/character)

**Lesson 19: Moving Sprites**
- X position ($D000, $D002, etc.)
- Y position ($D001, $D003, etc.)
- X MSB register ($D010)
- WOW: Smooth sprite movement

**Lesson 20: Multiple Sprites**
- Enabling sprites ($D015)
- Managing 2-4 sprites
- Sprite colors ($D027-$D02E)
- WOW: Small sprite formation

**Lesson 21: Sprite Collision**
- Hardware collision detection
- Sprite-sprite ($D01E)
- Sprite-background ($D01F)
- WOW: Collision detection demo

**Lesson 22: Sprite Animation**
- Frame cycling
- Switching sprite pointers
- Timing with TI
- WOW: Animated walking character

### Lessons 23-25: Sound Deepened

**Lesson 23: SID Voices**
- Three voice architecture
- Voice independence
- Frequency calculation
- WOW: Three-note chord

**Lesson 24: ADSR Mastery**
- Attack, decay, sustain, release
- Envelope shaping
- Voice-specific envelopes
- WOW: Varied instrument sounds

**Lesson 25: Simple Music**
- Note sequences
- Timing between notes
- Background music loops
- WOW: 8-bar melody

### Lessons 26-28: Joystick Control

**Lesson 26: Reading the Joystick**
- CIA chip concept
- PEEK(56320) for port 2
- Bit meanings (up/down/left/right/fire)
- WOW: Joystick test program

**Lesson 27: Joystick Sprite Movement**
- Update sprite position from joystick
- Movement speed
- Screen boundaries
- WOW: Player-controlled sprite

**Lesson 28: Diagonal Movement**
- Reading multiple directions
- Smooth 8-way movement
- Velocity concepts
- WOW: Smooth sprite control

### Lessons 29-31: Game Systems

**Lesson 29: Score Display**
- Fixed screen position for HUD
- Zero-padded numbers
- Updating without flicker
- WOW: Live score counter

**Lesson 30: Lives System**
- Health/lives counter
- Damage handling
- Game over condition
- WOW: Hearts/icons for lives

**Lesson 31: Game States**
- STATE variable pattern
- Title screen state
- Play state
- Game over state
- ON...GOTO dispatch
- WOW: Complete state machine

### Lesson 32: SYNTHESIS - Sprite Game

**Combines:** Sprites, joystick, collision, sound, score, states
**Builds:** Complete action game:
- Player sprite (joystick control)
- Enemy sprites (simple AI)
- Collision detection
- Score/lives display
- Sound effects
- Title/play/gameover states

**Honest moment:**
- "Sprite movement feels sluggish in BASIC"
- "Enemy AI is simple because BASIC is slow"
- "Assembly removes these speed limits"
- "But you've proven the concept works"

**Code:** 80-120 lines

---

## Tier 3: Limits (Lessons 33-48)

**Goal:** Advanced techniques, explicitly hit BASIC ceiling, prepare for assembly
**End State:** Attempted advanced effects, understand why assembly is needed, built ambitious game

### Lessons 33-37: Sprite Mastery

**Lesson 33: Advanced Animation**
- Multi-frame sequences
- Animation state machines
- Frame timing precision
- WOW: Complex character animation

**Lesson 34: Sprite Priority**
- Foreground/background ($D01B)
- Layering concepts
- Visual depth
- WOW: Sprite passes behind objects

**Lesson 35: Sprite Expansion**
- X/Y doubling ($D01D, $D017)
- When to use expansion
- Multicolor sprites ($D01C)
- WOW: Large boss sprite

**Lesson 36: Attempting Multiplexing**
- Concept: Reuse sprites mid-screen
- Why BASIC is too slow
- Andrew Braybrook's *Uridium* technique
- WOW: Demo attempt (shows flicker)
- **Honest:** "BASIC can't time this precisely, assembly can"

**Lesson 37: Sprite Optimization**
- Minimizing POKE calls
- Efficient sprite updates
- Best BASIC can do
- WOW: Optimized sprite movement (still has limits)

### Lessons 38-40: Advanced Sound

**Lesson 38: Multi-Voice Music**
- Melody + bass + rhythm
- Voice coordination
- Timing challenges in BASIC
- WOW: Three-voice music piece

**Lesson 39: Sound + Sprite Sync**
- Music during gameplay
- Sound effects interrupting music
- Timing coordination struggles
- WOW: Game with background music

**Lesson 40: Ring Modulation & Filters**
- SID advanced features
- Filter types
- Ring modulation
- WOW: Special effects sounds

### Lessons 41-43: Raster Concepts

**Lesson 41: Understanding Rasters**
- Electron beam concept
- Raster line position
- PAL vs NTSC timing
- WOW: Conceptual demo (BASIC too slow to exploit)

**Lesson 42: Mid-Screen Color Changes**
- Attempting color bars
- TI vs raster timing
- Why BASIC misses the timing
- WOW: Unstable color bars (showing limit)
- **Honest:** "Raster interrupts need assembly precision"

**Lesson 43: Timing Measurement**
- TI jiffy clock accuracy
- Profiling code sections
- Understanding overhead
- WOW: Performance comparison demo

### Lessons 44-47: Optimization

**Lesson 44: Address Tables**
- Pre-calculated values
- Lookup tables
- Trading memory for speed
- WOW: Faster calculations

**Lesson 45: Loop Unrolling**
- Eliminating loop overhead
- When to unroll
- Code size tradeoff
- WOW: Speed comparison

**Lesson 46: Efficient Screen Updates**
- Minimize screen writes
- Dirty rectangle concept
- Best BASIC patterns
- WOW: Flicker reduction

**Lesson 47: Memory Management**
- FRE() function
- Variable organization
- Array placement
- WOW: Memory usage display

### Lesson 48: SYNTHESIS - Ambitious Game

**Combines:** All Tier 3 techniques
**Builds:** Game that pushes BASIC hard:
- Multiple animated sprites
- Scrolling attempt (coarse)
- Complex collision
- Multi-voice music
- Performance optimizations

**Explicit limit-hitting:**
- Sprite flicker visible
- Music stutters during action
- Scrolling is jerky
- "This is BASIC's ceiling"

**Assembly preview:**
- "Assembly eliminates sprite flicker"
- "Raster interrupts enable smooth scrolling"
- "You've learned what's possible, now let's remove the interpreter"

**Code:** 120-150 lines

---

## Tier 4: Systems (Lessons 49-64)

**Goal:** Professional patterns, complete programs, smooth transition to assembly
**End State:** Built polished game, organized code well, ready for assembly Phase

### Lessons 49-52: Code Organization

**Lesson 49: Subroutine Libraries**
- GOSUB patterns
- Parameter passing conventions
- Return value patterns
- WOW: Reusable sprite library

**Lesson 50: Dispatch Tables**
- ON...GOSUB
- Function pointers concept
- Dynamic routing
- WOW: Plugin-style system

**Lesson 51: Initialization Routines**
- Setup/teardown pattern
- Clean state management
- Error recovery
- WOW: Robust game startup

**Lesson 52: Code Documentation**
- REM comment strategy
- Self-documenting variable names
- Structure markers
- WOW: Well-organized codebase

### Lessons 53-56: Data & Levels

**Lesson 53: Level Data Structure**
- Level format design
- DATA organization
- Multiple level storage
- WOW: 3-level game data

**Lesson 54: Level Loading**
- READ/RESTORE patterns
- Level initialization
- Validation
- WOW: Dynamic level loader

**Lesson 55: Save to Disk**
- OPEN, PRINT#, CLOSE
- Sequential files
- Save game state
- WOW: Save/load progress

**Lesson 56: High Score Table**
- Persistent storage
- Sorting scores
- Name entry
- WOW: Top 10 leaderboard

### Lessons 57-60: Polish & Menus

**Lesson 57: Title Screen**
- Animated title
- Press fire to start
- Credits display
- WOW: Professional title screen

**Lesson 58: Menu System**
- Array-driven menus
- Selection display
- Navigation
- WOW: Options menu

**Lesson 59: Instructions Screen**
- Multi-page text
- Controls display
- Pagination
- WOW: In-game manual

**Lesson 60: Configuration**
- Difficulty settings
- Control preferences
- Volume control
- WOW: Customizable game

### Lessons 61-63: Final Polish

**Lesson 61: Error Handling**
- ON ERROR GOTO
- ERR, ERL variables
- Graceful failure
- WOW: Crash-resistant program

**Lesson 62: Performance Profiling**
- Identifying bottlenecks
- TI measurement
- Optimization priorities
- WOW: Before/after comparison

**Lesson 63: Final Optimization**
- Variable placement
- Critical path optimization
- Best BASIC practices
- WOW: Maximum performance BASIC

### Lesson 64: CAPSTONE - Complete Game

**Combines:** Everything from Phase 0
**Builds:** Polished, complete game with:
- Title screen, menus, instructions
- Multiple levels
- Save/load system
- High scores
- Sound effects + music
- Optimized performance
- Error handling
- Professional presentation

**Transition to Assembly:**
- "You've built something impressive in BASIC"
- "Here's what I'd do differently in assembly:"
  - Sprite multiplexing for more objects
  - Raster interrupts for smooth scrolling
  - Faster collision detection
  - Precise music timing
- "Phase 0 complete. Now let's talk to the metal directly."
- "Next: Phase 1 - Assembly fundamentals"

**Code:** 200+ lines (substantial capstone project)

---

## Synthesis Lesson Summary

**Lesson 16:** Text adventure (Tier 1 capstone)
**Lesson 32:** Sprite action game (Tier 2 capstone)
**Lesson 48:** Ambitious game hitting limits (Tier 3 capstone)
**Lesson 64:** Complete polished game (Phase 0 capstone)

**Additional synthesis opportunities** (organic, not required):
- Lesson 8: First screen drawing program
- Lesson 22: First sprite animation demo
- Lesson 40: Sound showcase
- Lesson 56: Complete save system demo

---

## Spiral Concept Coverage

**Programming:** L1-6, L12-15, L49-52 (foundation → interaction → organization)
**Hardware:** L7-11, L17-22, L33-37, L41-43 (color → sprites → mastery → limits)
**Sound:** L10-11, L23-25, L38-40 (basics → music → advanced)
**Input:** L12, L26-28 (keyboard → joystick → mastery)
**Game Systems:** L14-15, L29-31, L57-60 (logic → HUD → polish)
**Performance:** L44-47, L61-63 (optimization → profiling → mastery)

---

## Teaching Philosophy Throughout

**Tier 1:** Build confidence, hardware is accessible
**Tier 2:** Build real things, feel BASIC's speed naturally
**Tier 3:** Understand limits explicitly, want assembly
**Tier 4:** Professional patterns, smooth transition

**Honesty checkpoints:**
- L16: "Commercial games used assembly"
- L32: "Sprites are sluggish in BASIC"
- L36: "Multiplexing needs assembly timing"
- L42: "Raster interrupts need assembly precision"
- L48: "This is BASIC's ceiling"
- L64: "Here's what assembly unlocks"

---

**Last Updated:** 2025-01-17
**Version:** 1.0 - Spiral learning structure
