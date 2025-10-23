# Lesson 001: Hello, Amiga

**Arc:** Text Adventures
**Position:** Lesson 1 of 3 in arc
**Type:** Standard
**Estimated Completion:** 10 lines of code

## Learning Objectives

- Write your first AMOS Professional program on the Amiga
- Understand structured programming (no line numbers)
- Learn to use variables and loops
- Experience AMOS's modern syntax and fast execution

## Prerequisites

**From Previous Lessons:**
None - this is the starting point

**AMOS Knowledge:**
- None required - first program

## Key Concepts Introduced

### Structured Programming
Unlike traditional BASIC, AMOS Professional doesn't use line numbers. Programs are organised with labels, procedures, and structured control flow (Repeat...Until, While...Wend, For...Next). This makes code easier to read and maintain.

### Variables
Variables are named storage locations. The variable `count` stores our counter, and we can read it, change it, and display it any time. AMOS supports various types: integers (count%), strings (name$), floating-point (score#).

### Locate for Positioning
AMOS's `Locate` command positions the text cursor at a specific row and column on screen. Row 10, column 15 keeps the counter in one place instead of scrolling.

### Repeat...Until Loops
The loop structure `Repeat...Until condition` repeats code until a condition becomes true. `Until False` creates an infinite loop - it runs forever until you press Ctrl+C to break.

### Immediate Feedback
AMOS Professional compiles your code internally, making it run significantly faster than interpreted BASIC on C64 or Spectrum. This counter updates smoothly and quickly.

## Code Pattern

```amos
' Infinite counter demonstration
count=0

Repeat
  count=count+1
  Locate 10,15
  Print count
Until False
```

**Note:** AMOS Professional uses single quotes (') for comments instead of REM. The code has no line numbers - it executes from top to bottom unless redirected by loops or procedures.

## Hardware Interaction

**Chips Involved:**
- Motorola 68000 CPU (executing compiled AMOS code)
- Denise (displaying output to screen)
- Agnus (managing screen memory)

**Memory Addresses:**
- None directly accessed yet - AMOS handles everything
- Screen buffer managed automatically by AMOS

**Screen Coordinates:**
- `Locate row,column` where row is 0-24, column is 0-39 (low-res mode)
- Row 10, column 15 puts counter near centre of screen
- Default screen: 320×256 pixels (PAL low-res)

## Common Pitfalls

1. **Forgetting to increment:** `count=count+1` is essential - without it, you'll print the same number repeatedly
2. **Wrong Locate syntax:** It's `Locate row,column` not `Locate column,row`
3. **Stopping the program:** Press `Ctrl+C` to halt an infinite loop (not Esc or Break)
4. **Print overwrites:** Without `Cls` (clear screen) first, old numbers may show through
5. **Case sensitivity:** AMOS isn't case-sensitive, but consistent capitalisation improves readability

## Extension Ideas

- Change the starting number (try `count=100`)
- Count by different amounts (`count=count+10` for tens)
- Count backwards (`count=count-1`)
- Change the screen position (try different row/column values)
- Add `Cls 0` at the start to clear the screen to black
- Use `Ink 2 : Print count` to change text colour
- Add `Wait Vbl` after Print to slow down the counting

## Builds Toward

**In This Tier:**
- L2: Add Input$ and conditionals to make a calculator
- L3: Complete text adventure game with scoring

**In Next Tier:**
- Variables will store BOB positions, scores, and game state
- Locate will position game HUD elements
- Procedures will organise complex game logic

## Quick Reference

**Essential Commands:**
- `Print` - Display value on screen
- `Locate row,column` - Position text cursor (0-based)
- `Input$` - Get text input from user
- `count=value` - Assign value to variable (no LET required)
- `Repeat...Until` - Loop structure
- `Cls N` - Clear screen to colour N (0=black)
- `Ink N` - Set text colour to N
- `Wait Vbl` - Wait for vertical blank (sync to screen refresh)
- `Ctrl+C` - Stop running program

**Comments:**
- Use `'` for single-line comments
- `Rem` also works but `'` is preferred in AMOS

**Variable Types:**
- No suffix: Integer or float (automatic)
- `name$`: String
- `count%`: Integer (forced)
- `score#`: Floating-point (forced)

**Screen Coordinates:**
- Rows: 0 (top) to 24 (bottom) in low-res text mode
- Columns: 0 (left) to 39 (right) in low-res text mode
- Centre: approximately row 12, column 19

**Control Flow:**
```amos
' Infinite loop
Repeat
  ' code
Until False

' Conditional
If count>100 Then
  Print "High!"
End If
```

**Amiga Advantages:**
- No line numbers - structured like modern languages
- Fast execution - compiled internally by AMOS
- Locate simpler than calculating screen memory addresses
- Consistent syntax across all commands

---

**Version:** 1.0
**Created:** 2025-10-23
**Status:** Lesson specification complete
