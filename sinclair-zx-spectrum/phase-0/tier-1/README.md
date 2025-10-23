# Tier 1: Discovery (Lessons 1-16)

**Philosophy:** Foundation games with immediate wins
**Arc Length:** Short (2-3 lessons)
**Games Built:** 6 complete games
**Code Range:** 5-60 lines
**Hardware Introduced:** ULA (screen), BEEP sound, keyboard

## Goals

- Learn by building games, not memorising syntax
- Each arc produces a complete playable game in 2-3 lessons
- Discover programming concepts naturally through gameplay needs
- First exposure to Spectrum's unique features (PRINT AT, PLOT, DRAW, attributes)
- Build confidence with rapid progression and immediate results

## Arcs Overview

### Arc 1: Number Challenge (L1-3)
**Game:** Guess the Number with scoring
**Concepts:** Variables, INPUT, conditionals, loops, RND (random numbers)

- **L1:** Hello, Spectrum - Infinite counter with PRINT AT
- **L2:** Maths Master - Calculator quiz
- **L3:** Guess the Number - Complete guessing game with scoring

### Arc 2: Knowledge Base (L4-6)
**Game:** Data-Driven Quiz Engine
**Concepts:** DATA statements, arrays, string handling, READ/RESTORE

- **L4:** Quiz Master - Simple quiz with DATA
- **L5:** High Score Hall - Top 5 leaderboard with sorting
- **L6:** Data-Driven Quiz - Expandable quiz engine

### Arc 3: Visual Creation (L7-9)
**Tool:** Pattern Designer (direct graphics)
**Concepts:** Graphics commands, attribute system introduction
**Hardware:** First direct hardware access with PLOT, DRAW, CIRCLE!

- **L7:** Rainbow Border - Animated colour cycling (BORDER command)
- **L8:** Screen Painter - PLOT and DRAW for patterns
- **L9:** Pattern Designer - Interactive graphics tool with attributes

### Arc 4: Sound Lab (L10-11)
**Tool:** Sound FX Generator
**Concepts:** BEEP command (pitch, duration), musical notes, sound effects

- **L10:** Beep Composer - Play musical notes with BEEP
- **L11:** Sound FX Generator - 4-5 game sound effects library

### Arc 5: Dodge & Catch (L12-14)
**Game:** Star Catcher (complete action game)
**Concepts:** INKEY$ keyboard control, collision detection, game loop, timing

- **L12:** Character Mover - Arrow key control with INKEY$
- **L13:** Falling Stars - Add random falling objects
- **L14:** Star Catcher - Complete game with collision, score, lives

### Arc 6: Mini Adventure (L15-16)
**Game:** Mystery Manor (synthesis game, ~60 lines)
**Concepts:** PRINT AT screen layout, state management, text adventure structure

- **L15:** Room Navigator - Multi-room text adventure framework
- **L16:** **SYNTHESIS** - Mystery Manor (complete text adventure, ~60 lines)

## Learning Outcomes

By completing Tier 1, you will have:

- Built **6 complete games** from scratch
- Mastered Sinclair BASIC fundamentals (variables, loops, conditionals, arrays, DATA)
- Used Spectrum's direct graphics commands (PRINT AT, PLOT, DRAW, CIRCLE)
- Understood attribute system basics (INK, PAPER, BORDER)
- Created sound effects with BEEP
- Learned INKEY$ for responsive keyboard control
- Written programs ranging from 5 to 60 lines
- Understood the game development loop (input ’ process ’ output ’ repeat)

## Prerequisites

None. This is the starting point for the entire curriculum.

## Builds Toward

**Tier 2:** Building (L17-32) - UDG mastery, software sprites, advanced graphics
**Next Concepts:** User-Defined Graphics, character animation, attribute management

## Key Discovery Moments

Throughout Tier 1, you'll experience several "wow" realisations:

1. **L1-3:** "I can make the Spectrum interactive!"
2. **L7:** "BORDER changes instantly - this is immediate feedback!"
3. **L8-9:** "PLOT and DRAW are so much simpler than POKEing screen memory!"
4. **L10-11:** "BEEP is simple but I can create recognisable tunes!"
5. **L14:** "I built a complete action game in BASIC!"
6. **L16:** "I can combine everything into something genuinely fun"

## Teaching Notes

**Spectrum Advantages in Tier 1:**
- PRINT AT provides instant positioned text (no POKE calculations)
- PLOT/DRAW/CIRCLE work immediately for graphics
- BEEP is simple to learn (pitch, duration)
- INKEY$ is more responsive than GET on C64
- Fast BASIC means games feel snappy even in BASIC

**Spectrum Constraints Introduced:**
- Colour applies to 8×8 blocks (attribute system)
- Simple sound (BEEP only in 48K)
- No hardware sprites (introduces concept of software sprites)

**British Spelling Throughout:**
- colour (not color)
- centre (not center)
- metre (not meter)
- emphasise (not emphasize)

## Comparison with C64 Tier 1

| Aspect | ZX Spectrum | Commodore 64 |
|--------|-------------|--------------|
| **Screen positioning** | PRINT AT (instant) | POKE 1024+ (must calculate) |
| **Graphics** | PLOT, DRAW, CIRCLE (immediate) | POKE screen memory (more work) |
| **Sound** | BEEP (simple, immediate) | POKE SID registers (powerful but complex) |
| **Input** | INKEY$ (responsive) | GET (slower) |
| **BASIC speed** | Fast | Slow |

Both curricula teach the same fundamentals, but Spectrum's simpler commands allow faster initial progress.

---

**Version:** 1.0
**Created:** 2025-10-23
**Status:** Overview complete - individual lesson specs to be created
