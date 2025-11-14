# Phase 1 Curriculum: 6502 Assembly + Hardware Fundamentals (Lessons 1-256)

> **⚠️ STRUCTURED:** This curriculum uses granular documentation files for better organisation and context efficiency.

## Primary Documentation

**Start here:** [`phase-1/overview.md`](phase-1/overview.md)

This provides the Phase 1 overview with philosophy, structure, and learning outcomes for BBC Micro assembly development.

## Detailed Documentation

| What you need | Where to find it |
|---------------|------------------|
| **Tier 1 details** (Bounce, L1-32) | [`phase-1/tier-1/README.md`](phase-1/tier-1/README.md) |
| **Tier 2 details** (Egg Scramble, L33-64) | [`phase-1/tier-2/README.md`](phase-1/tier-2/README.md) |
| **Tier 3 details** (Dot Eater, L65-96) | [`phase-1/tier-3/README.md`](phase-1/tier-3/README.md) |
| **Tier 4 details** (Space Invasion, L97-128) | [`phase-1/tier-4/README.md`](phase-1/tier-4/README.md) |
| **Tier 5 details** (Diamond Quest, L129-160) | [`phase-1/tier-5/README.md`](phase-1/tier-5/README.md) |
| **Tier 6 details** (Planet Explorer, L161-192) | [`phase-1/tier-6/README.md`](phase-1/tier-6/README.md) |
| **Tier 7 details** (Formula Circuit, L193-224) | [`phase-1/tier-7/README.md`](phase-1/tier-7/README.md) |
| **Tier 8 details** (Starbase Defense, L225-256) | [`phase-1/tier-8/README.md`](phase-1/tier-8/README.md) |
| **Individual lesson specs** | [`phase-1/tier-{1-8}/lesson-NNN.md`](phase-1/) |

## Why This Structure?

**Organised by tier and lesson**

**Benefits:**
- **60-70% less context** when working on specific lessons
- **Better organisation** with clear hierarchy (phase → tier → lesson)
- **Easier navigation** to find specific game or concept
- **Scalable** for all phases and platforms

## BBC Micro-Specific Features

This curriculum highlights the BBC Micro's unique characteristics:

- **Integrated assembler in BASIC** - Write assembly within BASIC programs
- **Two-pass assembly** - Built into the language (pass% = 0 and pass% = 3)
- **MOS operating system** - Extensive OS routines (OSWRCH, OSRDCH, OSBYTE, etc.)
- **6502 CPU** - Clean 8-bit architecture, educational-friendly
- **Multiple screen modes** - MODE 0-7 with different resolutions/colours
- **6845 CRTC** - Hardware display controller for advanced effects
- **6522 VIA** - Versatile Interface Adapter for I/O
- **Educational heritage** - Government Computer Literacy Project legacy

## Curriculum Structure

### Phase 1: 6502 Assembly + Hardware Fundamentals (256 lessons)

**Total:** 256 lessons across 8 tiers
**Outcome:** 8 complete original games, assembly programming mastery, hardware understanding

### Tier Breakdown

**Tier 1 (L1-32):** Reflex - Reaction time challenge
- First assembly program using integrated assembler
- 6502 fundamentals (registers, addressing modes, basic instructions)
- Calling OS routines (OSWRCH, OSRDCH, OSBYTE)
- Screen flashes, player presses key as fast as possible
- OS timing via OSBYTE (read system clock)
- High score tracking in memory
- **Playable:** Lesson 3 (react to screen flash)
- **Complete:** Lesson 7 (scoring, difficulty progression)
- **Pattern focus:** Assembly basics, OS integration, screen memory
- **BBC showcase:** Extensive OS calls (OSWRCH, OSBYTE, timing), educational computing heritage

**Tier 2 (L33-64):** Melody Panic - Musical memory game
- OS SOUND and ENVELOPE commands from assembly
- Play sequence of notes, player repeats back
- Sequence gets longer each round (Simon-style)
- Rich sound via SOUND/ENVELOPE system
- Visual feedback in sync with audio
- **Playable:** Lesson 35 (play and repeat melodies)
- **Complete:** Lesson 39 (increasing difficulty, high scores)
- **Pattern focus:** OS sound system, sequences, memory game logic
- **BBC showcase:** Sophisticated SOUND/ENVELOPE system unique to BBC Micro

**Tier 3 (L65-96):** Teletext Raceway - MODE 7 racing
- MODE 7 teletext graphics (blocky pseudo-3D)
- Road rendered with teletext characters
- Car dodges obstacles (teletext graphics)
- Road curves (change character patterns)
- Speed and distance scoring
- **Playable:** Lesson 67 (drive on MODE 7 road, dodge obstacles)
- **Complete:** Lesson 71 (curves, speed progression, distance)
- **Pattern focus:** MODE 7 programming, character graphics
- **BBC showcase:** MODE 7 teletext mode - impossible on C64/Spectrum/NES

**Tier 4 (L97-128):** Haunted Halls - Text adventure
- Text adventure with room descriptions
- Room data loaded from disk files
- Item collection and use
- OS text I/O (OSRDCH, OSWRCH for formatting)
- Save/restore game state
- **Playable:** Lesson 99 (explore rooms, collect items)
- **Complete:** Lesson 103 (puzzles, win condition, save system)
- **Pattern focus:** File I/O, parsing, adventure engine
- **BBC showcase:** BBC's educational text adventure heritage, file system integration

**Tier 5 (L129-160):** Dimension Shift - Multi-MODE gameplay
- Each level in different MODE (0, 1, 2, 4, 5)
- Switch modes between levels
- Gameplay adapts to MODE (high-res precision vs low-res colour)
- Shows MODE trade-offs as gameplay mechanic
- Puzzle/action hybrid
- **Playable:** Lesson 131 (level in MODE 1, switches to MODE 4)
- **Complete:** Lesson 135 (5 levels across 5 MODEs, adapted gameplay)
- **Pattern focus:** MODE switching, memory layout differences
- **BBC showcase:** Multiple graphics modes unique to BBC architecture

**Tier 6 (L161-192):** Beat Match - Rhythm precision game
- 6522 VIA timer for microsecond-precise timing
- Hit button in time with beat
- Visual timing indicator
- Interrupt-driven timing (rock-solid accuracy)
- Scoring based on precision (early/late/perfect)
- **Playable:** Lesson 163 (hit beats, timing works)
- **Complete:** Lesson 167 (interrupts, perfect timing scoring, combos)
- **Pattern focus:** VIA hardware timers, interrupts, precision timing
- **BBC showcase:** 6522 VIA timer precision, hardware-level timing control

**Tier 7 (L193-224):** Starfield Runner - CRTC scrolling shooter
- 6845 CRTC register manipulation for smooth scrolling
- Hardware scrolling via R12/R13 (smooth as silk)
- Ship dodges/shoots obstacles in scrolling field
- Split-screen score via CRTC manipulation
- **Playable:** Lesson 195 (smooth scrolling works, dodge obstacles)
- **Complete:** Lesson 199 (shooting, enemies, split-screen HUD)
- **Pattern focus:** CRTC programming, hardware scrolling, register manipulation
- **BBC showcase:** 6845 CRTC direct control, hardware scrolling impossible on Spectrum

**Tier 8 (L225-256):** Mega Game - BASIC shell, assembly core
- Menu system in BASIC, game loops in assembly
- Multiple mini-games showing BASIC+ASM integration
- Assembly for speed, BASIC for flexibility
- Demonstrates integrated assembler power
- High score table saved to disk
- **Playable:** Lesson 227 (2-3 mini-games work in hybrid system)
- **Complete:** Lesson 231 (5 mini-games, polished BASIC UI, assembly speed)
- **Pattern focus:** BASIC/assembly integration, calling conventions
- **BBC showcase:** Integrated assembler unique to BBC, hybrid programming model

## Original Games for Phase 1

All games are 100% original concepts inspired by classic genres, tailored to BBC Micro capabilities.

### 1. Reflex (Tier 1, L1-32)
**Genre:** Reaction time challenge
**Description:** Screen flashes different colours - press key as fast as you can! Millisecond precision timing using OS calls.
**Technical focus:** Assembly basics, OS integration (OSWRCH, OSBYTE), screen memory, timing
**BBC showcase:** OS timing calls, educational computing heritage
**Playable:** Lesson 3 | **Complete:** Lesson 7

### 2. Melody Panic (Tier 2, L33-64)
**Genre:** Musical memory game (Simon-style)
**Description:** Computer plays melody sequence, you repeat it back. Sequences get longer and faster. Rich synthesized sound.
**Technical focus:** OS SOUND/ENVELOPE system, sequence logic, audio-visual sync
**BBC showcase:** Sophisticated SOUND/ENVELOPE system unique to BBC Micro
**Playable:** Lesson 35 | **Complete:** Lesson 39

### 3. Teletext Raceway (Tier 3, L65-96)
**Genre:** Pseudo-3D racing game
**Description:** Race down teletext road, dodge obstacles, curves ahead! Blocky but fast MODE 7 graphics.
**Technical focus:** MODE 7 teletext graphics, character-based pseudo-3D, road rendering
**BBC showcase:** MODE 7 teletext mode - impossible on C64/Spectrum/NES
**Playable:** Lesson 67 | **Complete:** Lesson 71

### 4. Haunted Halls (Tier 4, L97-128)
**Genre:** Text adventure
**Description:** Explore haunted mansion, collect items, solve puzzles. Room descriptions loaded from disk.
**Technical focus:** Text parsing, file I/O, adventure engine, save/restore
**BBC showcase:** Educational text adventure heritage, file system integration
**Playable:** Lesson 99 | **Complete:** Lesson 103

### 5. Dimension Shift (Tier 5, L129-160)
**Genre:** Multi-MODE puzzle/action
**Description:** Each level in different graphics mode - gameplay adapts to resolution and colour count!
**Technical focus:** MODE switching, memory layout changes, adaptive gameplay
**BBC showcase:** Multiple graphics modes unique to BBC architecture
**Playable:** Lesson 131 | **Complete:** Lesson 135

### 6. Beat Match (Tier 6, L161-192)
**Genre:** Rhythm precision game
**Description:** Hit beats with microsecond precision. Perfect/early/late scoring using hardware timers.
**Technical focus:** 6522 VIA hardware timers, interrupts, precision timing
**BBC showcase:** VIA timer precision, hardware-level timing control
**Playable:** Lesson 163 | **Complete:** Lesson 167

### 7. Starfield Runner (Tier 7, L193-224)
**Genre:** Scrolling space shooter
**Description:** Hardware-smooth scrolling starfield, dodge and shoot obstacles, split-screen HUD.
**Technical focus:** 6845 CRTC register manipulation, hardware scrolling, split-screen
**BBC showcase:** CRTC direct control, hardware scrolling impossible on Spectrum
**Playable:** Lesson 195 | **Complete:** Lesson 199

### 8. Mega Game (Tier 8, L225-256)
**Genre:** Mini-game collection
**Description:** BASIC menu system launches assembly mini-games. Showcases hybrid programming power.
**Technical focus:** BASIC/assembly integration, calling conventions, multi-game structure
**BBC showcase:** Integrated assembler unique to BBC, hybrid programming model
**Playable:** Lesson 227 | **Complete:** Lesson 231

## What Students Master

### 6502 Assembly Language
- All addressing modes (immediate, zero page, absolute, indexed, indirect)
- Complete instruction set (load/store, arithmetic, logic, branches, jumps)
- Stack operations (push, pull, subroutines)
- Status flags (carry, zero, negative, overflow)
- Efficient code patterns
- Code organisation and structure

### MOS Operating System
- **OSWRCH (&FFEE):** Write character/byte to screen
- **OSRDCH (&FFE0):** Read character from keyboard
- **OSBYTE (&FFF4):** Miscellaneous OS functions
- **OSWORD (&FFF1):** Complex OS operations
- **OS vectors:** Understanding system hooks
- **Screen control:** VDU commands via OSWRCH
- **File I/O:** OS file system calls

### BBC Micro Hardware
- **Screen memory:** Understanding video RAM layout per MODE
- **MODE system:** Switching between graphics modes (0-7)
- **Character redefinition:** Creating custom sprites
- **6845 CRTC:** Display controller programming
- **6522 VIA:** I/O operations, timers, keyboard scanning
- **Memory map:** Understanding BBC Micro memory layout
- **Paging:** Sideways ROM/RAM banks

### Game Development Patterns
- Game loop architecture
- Input handling (keyboard via OS)
- Sprite movement and animation
- Collision detection (AABB, pixel-perfect)
- Tile engines (rendering, collision, physics)
- Scrolling techniques (character-based, smooth)
- AI implementation (pathfinding, state machines)
- Physics simulation (gravity, momentum, collisions)
- Data structures (arrays, linked lists, queues)
- Level data management
- Save/load systems

### Advanced Techniques
- Two-pass assembly (resolving forward references)
- Self-modifying code
- Lookup tables for speed
- Fixed-point arithmetic
- Pseudo-3D rendering basics
- Procedural generation
- Data compression

## Integrated Assembler Advantage

Unlike C64 or Spectrum, BBC Micro students learn assembly within BASIC from day one:

```basic
10 REM Integrated assembly example
20 DIM code% 100
30 FOR pass% = 0 TO 3 STEP 3
40 P% = code%
50 [OPT pass%
60   LDA #65
70   JSR &FFEE
80   RTS
90 ]
100 NEXT
110 CALL code%
```

This unique approach:
- **Gradual transition** - Students already familiar with assembler syntax from Phase 0
- **Debugging in context** - Test assembly within BASIC scaffolding
- **Hybrid programs** - Mix BASIC and assembly as needed
- **Educational advantage** - Lower barrier to entry for assembly

## Transfer Knowledge from Phase 0

Students arriving from Phase 0 already understand:
- BASIC program structure
- BBC Micro memory map basics
- Screen modes and graphics
- OS calls from BASIC
- **Assembler syntax** (seen in Tier 4 of Phase 0)
- Two-pass assembly concept

Phase 1 builds on this foundation, transitioning fully to assembly.

## Transfer Knowledge to Other 6502 Platforms

Skills learned here transfer to:
- **Commodore 64:** Same CPU, different hardware (VIC-II, SID, CIA)
- **NES:** Same CPU core, PPU graphics, cartridge-based
- **Atari 2600:** 6507 (6502 variant), extreme constraints
- **Apple II:** Similar OS integration model

Approximately 85-90% of knowledge transfers within 6502 family.

## Comparison with C64 and Spectrum Assembly

| Feature | BBC Micro | C64 | Spectrum |
|---------|-----------|-----|----------|
| **CPU** | 6502 @ 2MHz | 6510 @ 1MHz | Z80 @ 3.5MHz |
| **Assembler** | Integrated in BASIC | Separate tools | Separate tools |
| **OS Calls** | Extensive (MOS) | Limited (Kernal) | Minimal |
| **Sprites** | Software | VIC-II hardware | Software |
| **Sound** | SOUND command/chip | SID chip | Beeper |
| **Graphics** | MODE 0-7, CRTC | VIC-II, char/bitmap | ULA, attributes |
| **Educational Use** | Government-funded | Home/hobbyist | Home/hobbyist |

## Educational Heritage

The BBC Micro's Phase 1 curriculum honours its Computer Literacy Project heritage:

- **Structured learning** - Clear progression from simple to complex
- **Documentation** - Extensive comments and explanations
- **Accessible assembly** - Integrated assembler lowers barrier
- **OS integration** - Professional development practices
- **Transferable skills** - Teaches principles applicable to all platforms

## Navigation

- **View all phases:** [`./`](./)
- **Hardware references:** Coming soon (6502, 6845 CRTC, 6522 VIA)
- **Documentation index:** [`../START-HERE.md`](../START-HERE.md)
- **Phase 0 curriculum:** [`PHASE-0-CURRICULUM.md`](PHASE-0-CURRICULUM.md)

---

**Last updated:** 2025-11-04
**Version:** 1.0
**Status:** Overview complete, tier details and individual lessons to be created
