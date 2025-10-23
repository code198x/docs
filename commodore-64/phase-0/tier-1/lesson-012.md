# Lesson 012: Character Mover

**Arc:** Dodge & Catch
**Position:** Lesson 1 of 3 in arc
**Type:** Standard
**Estimated Completion:** 25 lines of code

## Learning Objectives

- Implement smooth character movement using GET
- Track character position separate from display
- Erase old position before drawing new position
- Create the foundation for action games

## Prerequisites

**From Previous Lessons:**
- GET command for keyboard input (L9)
- Screen memory manipulation (L8)
- Bounds checking (L9)

**BASIC Knowledge:**
- GET K$
- Screen memory addresses and formulas
- POKE for screen drawing

## Key Concepts Introduced

### Game Loop Fundamentals
Every action game follows this pattern: input → update → draw → repeat. This lesson establishes that core loop.

### Position Variables
Store position in variables (X, Y) separate from screen. This allows movement logic before redrawing, making animation smoother.

### Erase-Move-Draw Pattern
To move smoothly: erase character at old position (draw space), update position variables, draw character at new position. This prevents trails.

## Code Pattern

```basic
10 X=20:Y=12:C=81
20 REM Erase old position
30 POKE 1024+(Y*40)+X,32
40 REM Get input
50 GET K$
60 IF K$="W" AND Y>0 THEN Y=Y-1
70 IF K$="S" AND Y<24 THEN Y=Y+1
80 IF K$="A" AND X>0 THEN X=X-1
90 IF K$="D" AND X<39 THEN X=X+1
100 REM Draw new position
110 POKE 1024+(Y*40)+X,C
120 GOTO 20
```

## Hardware Interaction

**Chips Involved:**
- **VIC-II** - Screen display
- **CIA** - Keyboard scanning (via GET)

**Memory Addresses:**
- `1024-2023` - Screen memory
- `55296-56295` - Colour memory (optional)

## Common Pitfalls

1. **Not erasing old position:** Character leaves trail across screen
2. **Bounds checking after movement:** Allows X/Y to go out of bounds, then crashes
3. **Wrong erase character:** Must POKE 32 (space), not 0
4. **No input delay:** Movement may feel too fast without slight delay
5. **AND vs nested IF:** `IF K$="W" AND Y>0` is cleaner than nested IFs

## Extension Ideas

- Add colour to character (POKE to colour memory)
- Add different movement speeds
- Add diagonal movement (check two keys)
- Add boundary wrap-around (X=40 becomes X=0)
- Add character animation (cycle through different characters)
- Add obstacles that block movement

## Builds Toward

**In This Tier:**
- L13: Add falling objects to dodge
- L14: Add collision detection and scoring

**In Next Tier:**
- L18: Joystick control replaces keyboard
- Sprites replace character-based movement for smoothness

## Quick Reference

**Game Loop Pattern:**
```basic
10 REM Initialize position
20 REM Erase old position
30 REM Get input
40 REM Update position with bounds check
50 REM Draw new position
60 GOTO 20
```

**Erase-Move-Draw:**
```basic
10 POKE 1024+(Y*40)+X,32  :REM Erase (space)
20 REM Update X and Y variables
30 POKE 1024+(Y*40)+X,C   :REM Draw at new position
```

**WASD with Bounds:**
```basic
10 GET K$:IF K$="" THEN 10
20 IF K$="W" AND Y>0 THEN Y=Y-1
30 IF K$="S" AND Y<24 THEN Y=Y+1
40 IF K$="A" AND X>0 THEN X=X-1
50 IF K$="D" AND X<39 THEN X=X+1
```

**Smooth Movement Tips:**
- Store position in variables, not just screen location
- Always erase before moving
- Bounds check before updating position
- Use AND in IF statement for cleaner code
- Add slight delay if movement feels too fast
