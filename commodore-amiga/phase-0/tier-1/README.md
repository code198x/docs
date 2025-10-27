# Tier 1: Discovery (Lessons 1-16)

**Philosophy:** Foundation games with immediate wins
**Arc Length:** Short (2-3 lessons)
**Games Built:** 6 complete games
**Code Range:** 10-80 lines
**Hardware Introduced:** Paula (audio), Denise (graphics), Agnus (blitter), keyboard/joystick

## Goals

- Learn by building games, not memorising syntax
- Each arc produces a complete playable game in 2-3 lessons
- Discover programming concepts naturally through gameplay needs
- First exposure to Amiga's unique features (BOBs, structured AMOS, Paula audio)
- Build confidence with rapid progression and immediate results

## Arcs Overview

### Arc 1: Text Adventures (L1-3)
**Game:** Dungeon Quest with scoring
**Concepts:** Structured programming (no line numbers), procedures, Locate, Input$

- **L1:** Hello, Amiga - Infinite counter with Locate positioning
- **L2:** Interactive Oracle - User input and conditional branching
- **L3:** Dungeon Quest - Complete text adventure with procedures and scoring

### Arc 2: Knowledge Base (L4-6)
**Game:** Data-Driven Quiz Engine
**Concepts:** Data/Read statements, arrays, string handling, Restore

- **L4:** Quiz Master - Simple quiz with Data statements
- **L5:** High Score Hall - Top 5 leaderboard with sorting
- **L6:** Data-Driven Quiz - Expandable quiz engine with categories

### Arc 3: BOB Graphics (L7-9)
**Tool:** Pattern Designer (hardware-accelerated graphics)
**Concepts:** BOB system, screen modes, double buffering
**Hardware:** First experience with Agnus (blitter) and Denise (video)!

- **L7:** Rainbow Screen - Animated palette cycling with Fade
- **L8:** Screen Painter - Plot, Draw, and Circle for patterns
- **L9:** Pattern Designer - Interactive BOB-based graphics tool

### Arc 4: Paula Audio (L10-11)
**Tool:** Sound FX Generator
**Concepts:** Sample Bank, Music Bank, Sam Play, 4-channel mixing

- **L10:** Sound Player - Play samples with Paula's 4 channels
- **L11:** Sound FX Generator - 4-5 game sound effects library

### Arc 5: Moving BOBs (L12-14)
**Game:** Star Catcher (complete action game)
**Concepts:** BOB animation, Joypad/Inkey$ input, collision detection, game loop

- **L12:** BOB Mover - Joystick control with BOB animation
- **L13:** Falling Stars - Add random falling BOBs
- **L14:** Star Catcher - Complete game with collision, score, lives

### Arc 6: Mini Action Game (L15-16)
**Game:** Space Defender (synthesis game, ~80 lines)
**Concepts:** AMAL animation basics, screen organisation, state management

- **L15:** Shooting Gallery - Projectile system with collision
- **L16:** **SYNTHESIS** - Space Defender (complete shooter, ~80 lines)

## Learning Outcomes

By completing Tier 1, you will have:

- Built **6 complete games** from scratch
- Mastered AMOS Professional fundamentals (structured programming, procedures, functions)
- Used BOBs (Blitter OBjects) for hardware-accelerated sprites
- Understood screen modes and double buffering
- Created sound effects with Paula's 4-channel audio
- Learned Joypad/Inkey$ for responsive input
- Written programs ranging from 10 to 80 lines
- Understood the game development loop (input � process � output � repeat)

## Prerequisites

None. This is the starting point for the entire curriculum.

## Builds Toward

**Tier 2:** Building (L17-32) - AMAL mastery, advanced BOB techniques, blitter optimisation
**Next Concepts:** AMAL animation language, copper basics, parallax scrolling

## Key Discovery Moments

Throughout Tier 1, you'll experience several "wow" realisations:

1. **L1-3:** "AMOS is structured like modern programming - no line numbers!"
2. **L7:** "Screen fading happens instantly - hardware acceleration is real!"
3. **L8-9:** "BOBs are so much faster than software sprites!"
4. **L10-11:** "Paula's sample-based audio sounds incredible compared to chip tunes!"
5. **L14:** "I built a smooth action game with hardware sprites!"
6. **L16:** "I can combine everything into something genuinely impressive"

## Teaching Notes

**Amiga Advantages in Tier 1:**
- Structured programming (procedures, functions, labels) feels modern
- Locate provides instant positioned text (similar to PRINT AT)
- BOBs provide hardware-accelerated sprites with collision detection
- Paula's sample-based audio sounds professional immediately
- Double buffering eliminates flicker without manual effort
- Fast execution means games feel smooth even in Tier 1

**Amiga Constraints Introduced:**
- BOBs must be in Chip RAM (memory management preview)
- 8 hardware sprites limit (use BOBs for more)
- Screen mode complexity (low-res/high-res trade-offs)
- Sample memory requirements (Paula uses Chip RAM)

**British Spelling Throughout:**
- colour (not color)
- centre (not center)
- metre (not meter)
- emphasise (not emphasize)

## Comparison with Other Platforms

| Aspect | Commodore 64 | ZX Spectrum | Amiga |
|--------|--------------|-------------|-------|
| **Screen positioning** | POKE 1024+ (calculate) | PRINT AT (instant) | Locate (instant) |
| **Graphics** | POKE screen memory | PLOT, DRAW, CIRCLE | Plot, Draw, Circle (double buffered) |
| **Sprites** | Hardware sprites (VIC-II) | Software sprites (slow) | BOBs (blitter-accelerated) |
| **Sound** | POKE SID registers | BEEP (simple) | Sam Play (sample-based) |
| **Input** | GET (slow) | INKEY$ (fast) | Joypad/Inkey$ (fast) |
| **BASIC speed** | Slow | Fast | Very fast (compiled) |
| **Structure** | Line numbers | Line numbers | Procedures/labels (modern) |

All three platforms teach the same fundamentals, but Amiga's architecture allows for more sophisticated results earlier.

## AMOS Professional Syntax Notes

**Key differences from traditional BASIC:**

```amos
' Comments use single quote (not REM)
' No line numbers - use labels

Procedure MyProcedure
  ' Code here
End Proc

' Structured control flow
If condition Then
  ' Code
Else
  ' Code
End If

Repeat
  ' Code
Until condition

While condition
  ' Code
Wend

For I=1 To 10
  ' Code
Next I
```

**Screen coordinates:**
- X: 0-319 (low-res), 0-639 (high-res)
- Y: 0-199 (non-interlace), 0-255 (PAL overscan)
- Locate row,column (text positioning, 0-based)

**BOB basics:**
```amos
Get Bob 1,X1,Y1 To X2,Y2     ' Capture BOB image
Bob 1,X,Y,1                   ' Display BOB 1 at X,Y, image 1
Bob Update                    ' Update all BOB positions
```

---

**Version:** 1.0
**Created:** 2025-10-23
**Status:** Overview complete - individual lesson specs to be created
