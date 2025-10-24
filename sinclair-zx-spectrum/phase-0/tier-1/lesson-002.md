# Lesson 002: The Number Oracle

**Arc:** Text Adventures
**Position:** Lesson 2 of 3 in arc
**Type:** Standard
**Estimated Completion:** 15 lines of code

## Learning Objectives

- Use INPUT to receive user responses
- Make decisions with IF...THEN
- Create interactive programs with branching logic
- Build upon Spectrum's excellent text handling

## Prerequisites

**From Previous Lessons:**
- L1: Variables, PRINT AT, loops

**BASIC Knowledge:**
- Variables (LET, assignment)
- PRINT AT positioning

## Key Concepts Introduced

### INPUT for User Interaction
INPUT pauses the program and waits for the user to type something. The entered value is stored in a variable for the program to use.

### Conditional Logic (IF...THEN)
Programs can make decisions based on conditions. IF tests whether something is true, and THEN specifies what happens if it is.

### String Variables
Variables ending with $ store text (strings) instead of numbers. Use these for names, words, and text responses.

### Comparison Operators
Test relationships between values: `=` (equals), `<` (less than), `>` (greater than), `<=` `>=` (less/greater or equal).

## Code Pattern

```basic
10 PRINT AT 10,10;"What is your name?"
20 INPUT n$
30 PRINT AT 12,10;"Hello ";n$;"!"
40 PRINT AT 14,8;"Pick a number 1-10:"
50 INPUT g
60 IF g=7 THEN PRINT AT 16,10;"Lucky!"
70 IF g<>7 THEN PRINT AT 16,8;"Try again!"
```

## Hardware Interaction

**Chips Involved:**
- Z80 CPU (BASIC interpreter, keyboard scanning)
- ULA (screen display, keyboard matrix)

**Screen Coordinates:**
- Multiple PRINT AT commands create conversational interface
- Centre text for visual balance

## Common Pitfalls

1. **Forgetting $ for strings:** Use `n$` not `n` for text
2. **No THEN after IF:** Must write `IF condition THEN command`
3. **Wrong comparison:** Use `=` for "equals", `<>` for "not equals"
4. **INPUT without prompt:** User won't know what to enter

## Extension Ideas

- Ask multiple questions in sequence
- Create a personality quiz
- Add scoring across multiple questions
- Use PRINT AT to position responses creatively
- Try INK colours for different responses

## Builds Toward

**In This Tier:**
- L3: Complete text adventure with multiple rooms
- L4-6: DATA statements for knowledge base

**In Next Tier:**
- INPUT for arcade game controls (initial/menu entry)
- Branching logic for game state management

## Quick Reference

**Essential Commands:**
- `INPUT variable` - Get user input (number or string)
- `INPUT "prompt";variable` - Show prompt before input
- `IF condition THEN command` - Conditional execution
- `variable$` - String variable (text)

**Comparison Operators:**
- `=` - Equals
- `<>` - Not equals
- `<` - Less than
- `>` - Greater than
- `<=` `>=` - Less/greater or equal

**String Operations:**
- Concatenation: `"Hello ";"World"` or `"Hello "+name$`
- Variables must end with $ for text

**Spectrum Keyboard:**
- ENTER to submit INPUT
- DELETE (CAPS SHIFT + 0) to correct mistakes

---

**Version:** 1.0
**Created:** 2025-10-24
**Status:** Lesson specification complete
