# Lesson 001: Hello, Spectrum

**Arc:** Number Challenge
**Position:** Lesson 1 of 3 in arc
**Type:** Standard
**Estimated Completion:** 5 lines of code

## Learning Objectives

- Write your first Sinclair BASIC program on the ZX Spectrum
- Understand the concept of a program loop
- Learn to use variables to store and change values
- Experience the Spectrum's immediate responsiveness and fast BASIC execution

## Prerequisites

**From Previous Lessons:**
None - this is the starting point

**BASIC Knowledge:**
- None required - first program

## Key Concepts Introduced

### The Program Loop
A loop allows code to repeat automatically. The infinite counter demonstrates this by counting upward forever, showing how computers can perform repetitive tasks without tiring.

### Variables
Variables are named storage locations. The variable `c` stores our count, and we can read it, change it, and display it any time.

### PRINT AT for Positioning
Unlike other BASICs that scroll text, Spectrum's `PRINT AT` lets you print at specific screen positions (row, column). This keeps the counter in one place instead of scrolling.

### Immediate Feedback
Unlike traditional education, programming gives instant feedback. You type, run, and see results immediately. The Spectrum's fast BASIC means this counter runs noticeably quicker than on other 8-bit computers.

## Code Pattern

```basic
10 LET c=0
20 LET c=c+1
30 PRINT AT 10,15;c
40 GO TO 20
```

**Note:** Spectrum BASIC uses keyword entry. Press `P` for PRINT, `G` for GO TO, `L` for LET. The keywords appear as single characters on screen but represent full commands.

## Hardware Interaction

**Chips Involved:**
- Z80 CPU (executing BASIC interpreter)
- ULA (displaying output to screen)

**Memory Addresses:**
- None directly accessed yet - BASIC handles everything

**Screen Coordinates:**
- `PRINT AT row,column` where row is 0-21, column is 0-31
- Row 10, column 15 puts counter near centre of screen

## Common Pitfalls

1. **Forgetting line numbers:** Every BASIC line needs a number. Line 10 comes first, then 20, etc.
2. **Using GO TO wrong:** `GO TO 20` sends control back to line 20, creating the loop
3. **Stopping the program:** Press `BREAK` (CAPS SHIFT + SPACE) to halt an infinite loop
4. **Semicolon in PRINT AT:** The semicolon after coordinates prevents automatic newline

## Extension Ideas

- Change the starting number (try `LET c=100`)
- Count by different amounts (`LET c=c+10` for tens)
- Count backwards (`LET c=c-1`)
- Change the screen position (try different row/column values)
- Add `INK` and `PAPER` before PRINT to change colours

## Builds Toward

**In This Tier:**
- L2: Add INPUT and conditions to make a calculator
- L3: Complete guessing game with scoring

**In Next Tier:**
- Variables will store sprite positions, scores, and game state
- PRINT AT will position game elements

## Quick Reference

**Essential Commands:**
- `PRINT` - Display value on screen
- `PRINT AT row,column` - Display at specific position
- `LET` - Assign value to variable
- `GO TO` - Jump to a line number
- `RUN` - Execute the program
- `LIST` - Show program code
- `NEW` - Clear program from memory
- `BREAK` - Stop running program (CAPS SHIFT + SPACE)

**Keyword Entry:**
- Press `P` for PRINT
- Press `G` then select GO TO from menu
- Press `L` for LET
- Keywords appear as single inverse video characters

**Screen Coordinates:**
- Rows: 0 (top) to 21 (bottom)
- Columns: 0 (left) to 31 (right)
- Centre: approximately row 10, column 15

**Spectrum Advantages:**
- Fast BASIC - counter runs visibly quicker than C64
- PRINT AT - simpler than calculating screen memory addresses
- Keyword entry - faster than typing full commands

---

**Version:** 1.0
**Created:** 2025-10-23
**Status:** Lesson specification complete
