# Lesson 009: Box Designer

**Arc:** Visual Creation
**Position:** Lesson 3 of 3 in arc
**Type:** Synthesis
**Estimated Completion:** 35 lines of code

## Learning Objectives

- Combine GET for keyboard input with POKE for screen control
- Create interactive graphics tool
- Implement cursor movement and drawing
- Synthesize all Visual Creation arc concepts

## Prerequisites

**From Previous Lessons:**
- POKE for colours (L7)
- Screen memory manipulation (L8)
- Loops and conditionals (L1-3)

**BASIC Knowledge:**
- POKE command
- Screen memory addresses
- Character codes

## Key Concepts Introduced

### GET Command
`GET K$` reads a single keypress immediately without waiting for ENTER. Returns empty string if no key pressed. Perfect for interactive tools.

### Interactive Loop Pattern
Main loop: read input → process command → update display → repeat. This is the foundation of interactive programs.

### Cursor Tracking
Variables track cursor position (X,Y). User input modifies these, and cursor is redrawn at new position. This is how all drawing tools work.

## Code Pattern

```basic
10 X=20:Y=12:C=42
20 GET K$
30 IF K$="" THEN 20
40 IF K$="W" THEN Y=Y-1
50 IF K$="S" THEN Y=Y+1
60 IF K$="A" THEN X=X-1
70 IF K$="D" THEN X=X+1
80 IF K$=" " THEN POKE 1024+(Y*40)+X,C
90 IF X<0 THEN X=0
100 IF X>39 THEN X=39
110 IF Y<0 THEN Y=0
120 IF Y>24 THEN Y=24
130 POKE 1024+(Y*40)+X,81
140 GOTO 20
```

## Hardware Interaction

**Chips Involved:**
- **VIC-II** - Screen display
- **CIA** - Keyboard scanning (accessed by GET)

**Memory Addresses:**
- `1024-2023` - Screen memory
- `55296-56295` - Colour memory (optional for coloured drawing)

## Common Pitfalls

1. **GET returns string:** Even for single character, K$="" when no key pressed
2. **Bounds checking:** Cursor can go negative or >39/24 without limits
3. **Cursor trail:** Old cursor position must be cleared or will leave marks
4. **Key repeat:** GET may read same key multiple times if held
5. **Case sensitivity:** "W" ≠ "w" (use uppercase in C64 default mode)

## Extension Ideas

- Add colour selection (number keys choose colour)
- Add character selection (change drawing character)
- Add erase mode (draw spaces)
- Add fill tool (flood fill from cursor position)
- Add save/load patterns (preview of disk operations L44)
- Add pattern library (draw box, circle, line)

## Builds Toward

**In This Tier:**
- L12: Character movement for games uses same WASD pattern
- L14: GET for game input (Star Catcher)

**In Next Tier:**
- Joystick control replaces GET (L18)
- But keyboard patterns remain useful for text input

## Quick Reference

**GET Command:**
- `GET K$` - Read single keypress (no ENTER needed)
- Returns `""` if no key pressed
- Returns single-character string if key pressed
- Does NOT wait (unlike INPUT)

**WASD Control Pattern:**
```basic
10 GET K$
20 IF K$="" THEN 10
30 IF K$="W" THEN Y=Y-1  :REM Up
40 IF K$="S" THEN Y=Y+1  :REM Down
50 IF K$="A" THEN X=X-1  :REM Left
60 IF K$="D" THEN X=X+1  :REM Right
```

**Bounds Checking:**
```basic
100 IF X<0 THEN X=0
110 IF X>39 THEN X=39
120 IF Y<0 THEN Y=0
130 IF Y>24 THEN Y=24
```

**Interactive Tool Loop:**
```basic
10 REM Initialize
20 GET K$          :REM Input
30 IF K$="" THEN 20
40 REM Process input
50 REM Bounds check
60 REM Update display
70 GOTO 20         :REM Repeat
```
