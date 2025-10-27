# Phase 0: Sinclair BASIC

**Lessons:** 1-64 (4 tiers × 16 lessons)
**Language:** Sinclair BASIC
**Approach:** Game-first discovery learning

## Philosophy

Learn programming by building games, not by memorising syntax. Each short arc (2-3 lessons) produces a complete playable game. Concepts emerge naturally from trying to make games better, faster, and more interesting.

The ZX Spectrum defined British home computing in the 1980s. Its unique characteristics shape this curriculum:

- **Attribute-based graphics** - Colour in 8×8 character blocks (not per-pixel)
- **Beeper sound** - Single-channel 1-bit audio (no dedicated sound chip on 48K)
- **Sinclair BASIC** - Fast interpreter, keyword-entry system with direct graphics commands
- **Memory constraints** - 48K total (16K screen, ~32K for programs on base model)
- **Instant response** - Direct screen access via PRINT AT, PLOT, DRAW, CIRCLE

Experience both the strengths (speed, responsiveness) and constraints (colour clash, attribute system) that defined British bedroom coding.

## Spectrum-Specific Advantages

1. **Fast BASIC interpreter** - Faster than C64 BASIC for many operations
2. **Direct screen access** - PLOT, DRAW, PRINT AT for immediate graphics
3. **Attribute system** - Quick colour changes without redrawing
4. **Responsive keyboard** - Fast INKEY$ polling
5. **128K model benefits** - AY sound chip, extra RAM, enhanced BASIC

## Spectrum-Specific Challenges

1. **Colour clash** - Attributes apply to 8×8 blocks, not individual pixels
2. **Simple sound** - BEEP command only (until 128K AY chip)
3. **No hardware sprites** - All sprites drawn in software
4. **Flash/bright attributes** - Creative constraint (flashing, high-intensity colours)

## Structure

### Tier 1: Discovery (L1-16) - Foundation Games

**Philosophy:** Quick wins with Spectrum's immediate feedback
**Code Range:** 5-60 lines

#### Arc 1: Text Adventures (L1-3)
- Leverage Spectrum's excellent text handling
- PRINT AT for precise positioning
- INPUT for simple interaction
- **Deliverable:** Text-based adventure game (~40 lines)

#### Arc 2: Knowledge Base (L4-6)
- DATA statements and arrays
- RESTORE for multiple quiz attempts
- **Deliverable:** Quiz game with scoring (~50 lines)

#### Arc 3: Character Graphics (L7-9)
- PLOT and DRAW commands
- Understanding attributes vs pixels
- INK, PAPER, BORDER, BRIGHT, FLASH
- **Deliverable:** Drawing tool (~60 lines)

#### Arc 4: Sound & Timing (L10-11)
- BEEP pitch and duration
- PAUSE for timing
- Simple sound effects
- **Deliverable:** Music/sound effects demo

#### Arc 5: Moving Sprites (L12-14)
- Software sprite movement (PRINT AT + UDG)
- INKEY$ for input
- Simple collision (character detection)
- **Deliverable:** Character movement game

#### Arc 6: Mini Action Game (L15-16)
- Combine movement, collision, scoring
- **Deliverable:** Complete arcade-style game (~60 lines)

### Tier 2: Building (L17-32) - Complete Systems

**Philosophy:** Professional game systems
**Code Range:** 60-150 lines

#### Arc 1: UDG Graphics System (L17-21)
- User-Defined Graphics (characters 144-164)
- Creating tile sets
- Character-based maps
- Attribute management
- **Deliverable:** Maze game with custom graphics

#### Arc 2: Arcade Action (L22-27)
- Fast sprite movement techniques
- Multiple moving objects
- Collision detection refinement
- Score/lives HUD
- **Deliverable:** Space Invaders-style game

#### Arc 3: Platform Game (L28-32)
- Gravity and jumping
- Level data (strings or arrays)
- Enemy AI basics
- **Deliverable:** Platform game with multiple screens

### Tier 3: Mastery (L33-48) - Professional Games

**Philosophy:** Genre mastery across three complete games
**Code Range:** 100-250 lines

#### Arc 1: Puzzle Game (L33-37)
- Grid-based logic
- Sokoban/Tetris-style mechanics
- Level progression
- **Deliverable:** Puzzle game with 10+ levels

#### Arc 2: Shooter (L38-43)
- Bullet management
- Wave patterns
- Power-ups
- **Deliverable:** Scrolling shooter

#### Arc 3: Adventure/RPG (L44-48)
- Room navigation (text or graphic)
- Inventory system
- Simple combat
- Save/load (tape simulation)
- **Deliverable:** Multi-room adventure game

### Tier 4: Limits (L49-64) - BASIC's Ceiling

**Philosophy:** Discover Spectrum BASIC's performance boundaries
**Code Range:** 150-300 lines

#### Arc 1: Speed Limit (L49-53)
- Action game with many sprites
- Measure frame rate (FRAMES variable)
- Optimization techniques
- **Conclusion:** BASIC hits ~10-15 fps ceiling

#### Arc 2: Colour Clash (L54-58)
- Attempt pixel-perfect sprite graphics
- Demonstrate attribute limitations
- Workarounds and compromises
- **Conclusion:** Attributes are fundamental constraint

#### Arc 3: 128K Features (L59-64)
- AY sound chip programming
- Extra memory banks
- Enhanced BASIC commands
- **Finale:** Complete game using all Phase 0 techniques, measuring limits

## Key Differences from C64 Phase 0

| Aspect | Commodore 64 | ZX Spectrum |
|--------|--------------|-------------|
| **Graphics** | Sprites, flexible colour | Software sprites, attribute clash |
| **Sound** | SID chip (3 voices) | BEEP (1-bit) / AY chip (128K) |
| **Colours** | Per-pixel | Per-character block (8×8) |
| **Memory** | 64K | 48K (128K model) |
| **BASIC speed** | Slow | Fast |
| **Screen access** | POKE 1024+ | PRINT AT, PLOT, DRAW |

## Learning Outcomes

By completing Phase 0, you will have:

- Mastered Sinclair BASIC fundamentals and unique commands
- Built 16+ complete games leveraging Spectrum's strengths
- Understood attribute system (colour clash, flash, bright)
- Created software sprites and character-based graphics
- Used UDGs (User-Defined Graphics) for custom tiles
- Experienced BASIC's speed ceiling (faster than C64, but still limited)
- **Discovered:** Spectrum BASIC is fast for turn-based/puzzle games, struggles with fast action
- **Motivation established:** Ready for Z80 assembly to unlock full potential

## Prerequisites

None - Phase 0 is the entry point.

## Builds Toward

**Phase 1:** Z80 Assembly Language + Hardware Mastery
- Leverage fast BASIC foundation
- Learn Z80 instruction set
- Master ULA (screen chip) programming
- Achieve 50fps smooth scrolling and sprites
- AY sound chip programming (128K)

## Spectrum-Specific Resources

**Hardware:**
- Z80 CPU (3.5MHz)
- ULA (Uncommitted Logic Array - graphics/timing)
- 48K/128K RAM models
- AY-3-8912 sound chip (128K only)

**Development Tools:**
- Fuse emulator
- zmakebas (BASIC to TAP/TZX)
- pasmo assembler (Phase 1+)

## Notes for Lesson Creators

**Embrace the constraints:**
- Colour clash is a feature, not a bug (teaches creative problem-solving)
- BEEP limitations inspire creative sound design
- Character-based graphics are fast and effective

**Spectrum BASIC advantages:**
- Keyword entry system (type P for PRINT)
- Fast execution compared to other 8-bit BASICs
- Excellent string handling
- Direct graphics commands (PLOT, DRAW, CIRCLE)

**British spelling throughout:** colour, centre, etc.

---

**Version:** 1.1
**Last Updated:** 2025-10-27
**Status:** Tier 1 (L1-16) complete, Tier 2 (L17-32) specs complete, Tier 3-4 to be created
