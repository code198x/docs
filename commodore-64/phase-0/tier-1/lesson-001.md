# Lesson 001: Hello, Computer

**Arc:** Number Challenge
**Position:** Lesson 1 of 3 in arc
**Type:** Standard
**Estimated Completion:** 5 lines of code

## Learning Objectives

- Write your first BASIC program on the C64
- Understand the concept of a program loop
- Learn to use variables to store and change values
- Experience immediate computer responsiveness

## Prerequisites

**From Previous Lessons:**
None - this is the starting point

**BASIC Knowledge:**
- None required - first program

## Key Concepts Introduced

### The Program Loop
A loop allows code to repeat automatically. The infinite counter demonstrates this by counting upward forever, showing how computers can perform repetitive tasks without tiring.

### Variables
Variables are named storage locations. The variable `C` stores our count, and we can read it, change it, and display it any time.

### Immediate Feedback
Unlike traditional education, programming gives instant feedback. You type, run, and see results immediately.

## Code Pattern

```basic
10 C=0
20 C=C+1
30 PRINT C
40 GOTO 20
```

## Hardware Interaction

**Chips Involved:**
- None - pure BASIC fundamentals

**Memory Addresses:**
- None yet

## Common Pitfalls

1. **Forgetting line numbers:** Every BASIC line needs a number. Line 10 comes first, then 20, etc.
2. **Using GOTO wrong:** `GOTO 20` sends control back to line 20, creating the loop
3. **Stopping the program:** Press `RUN/STOP` key to halt an infinite loop

## Extension Ideas

- Change the starting number (try `C=100`)
- Count by different amounts (`C=C+10` for tens)
- Count backwards (`C=C-1`)

## Builds Toward

**In This Tier:**
- L2: Add input and conditions to make a calculator
- L3: Complete guessing game with scoring

**In Next Tier:**
- Variables will store sprite positions, scores, and game state

## Quick Reference

**Essential Commands:**
- `PRINT` - Display value on screen
- `GOTO` - Jump to a line number
- `RUN` - Execute the program
- `LIST` - Show program code
- `NEW` - Clear program from memory
