# Lesson 002: Maths Master

**Arc:** Number Challenge
**Position:** Lesson 2 of 3 in arc
**Type:** Standard
**Estimated Completion:** 15 lines of code

## Learning Objectives

- Accept user input with INPUT
- Perform mathematical operations
- Make decisions using IF/THEN
- Create interactive programs that respond to users

## Prerequisites

**From Previous Lessons:**
- Variables (L1)
- PRINT command (L1)

**BASIC Knowledge:**
- `PRINT` - Display output
- Variables for storage

## Key Concepts Introduced

### User Input
The `INPUT` command pauses the program and waits for the user to type something. This makes programs interactive rather than just displaying information.

### Conditional Logic
`IF/THEN` allows programs to make decisions. The computer checks a condition and does different things based on whether it's true or false.

### Mathematical Operations
BASIC can perform calculations: `+`, `-`, `*` (multiply), `/` (divide). This turns the computer into an interactive calculator.

## Code Pattern

```basic
10 PRINT "WHAT IS 5+3?"
20 INPUT A
30 IF A=8 THEN PRINT "CORRECT!"
40 IF A<>8 THEN PRINT "TRY AGAIN"
```

## Hardware Interaction

**Chips Involved:**
- None - pure BASIC logic

**Memory Addresses:**
- None yet

## Common Pitfalls

1. **Forgetting INPUT prompt:** Always tell users what to enter
2. **Using = vs <>:** The `<>` means "not equal to" in BASIC
3. **Missing THEN:** IF requires THEN to specify what happens when true

## Extension Ideas

- Ask multiple questions in sequence
- Keep score of correct answers
- Generate random numbers for questions (preview of L3)
- Add harder problems (multiplication, division)

## Builds Toward

**In This Tier:**
- L3: Add random numbers and scoring system
- L4: String input for quiz questions

**In Next Tier:**
- Keyboard input for game control (L12)
- Complex conditionals for collision detection (L14)

## Quick Reference

**Essential Commands:**
- `INPUT` - Get user input
- `IF/THEN` - Conditional execution
- Comparison operators: `=`, `<>`, `<`, `>`, `<=`, `>=`

**Mathematical Operators:**
- `+` Addition
- `-` Subtraction
- `*` Multiplication
- `/` Division
