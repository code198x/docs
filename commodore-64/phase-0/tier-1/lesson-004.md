# Lesson 004: Quiz Master

**Arc:** Knowledge Base
**Position:** Lesson 1 of 3 in arc
**Type:** Standard
**Estimated Completion:** 20 lines of code

## Learning Objectives

- Work with string variables (A$, B$, etc.)
- Compare string values for quiz answers
- Structure a simple quiz with multiple questions
- Understand string vs numeric variables

## Prerequisites

**From Previous Lessons:**
- Variables and INPUT (L1-2)
- IF/THEN conditionals (L2-3)
- Scoring system (L3)

**BASIC Knowledge:**
- `PRINT`, `INPUT`, `IF/THEN`
- Basic program flow

## Key Concepts Introduced

### String Variables
String variables end with `$` and store text instead of numbers. `A$="HELLO"` stores text, while `A=5` stores a number. They're different types and can't be mixed.

### String Comparison
You can compare strings just like numbers: `IF A$="LONDON" THEN...`. BASIC compares letter by letter.

### Quiz Structure
A quiz is a sequence of question → answer → check → feedback. This pattern builds more complex information systems.

## Code Pattern

```basic
10 S=0
20 PRINT "WHAT IS THE CAPITAL OF ENGLAND?"
30 INPUT A$
40 IF A$="LONDON" THEN S=S+1:PRINT "CORRECT!"
50 IF A$<>"LONDON" THEN PRINT "WRONG! IT'S LONDON"
60 PRINT "SCORE:";S
```

## Hardware Interaction

**Chips Involved:**
- None - pure BASIC string handling

**Memory Addresses:**
- None yet

## Common Pitfalls

1. **Forgetting the $:** String variables must end with $ (A$ not A)
2. **Case sensitivity:** "LONDON" ≠ "London" ≠ "london" on C64 (uppercase only by default)
3. **Mixing types:** Can't compare string to number (A$=5 is an error)
4. **Partial matches:** "LOND" won't match "LONDON" - need exact match or advanced techniques

## Extension Ideas

- Add more questions (5-10 question quiz)
- Give hints for wrong answers
- Add categories (history, science, geography)
- Show percentage correct at end
- Allow multiple attempts per question

## Builds Toward

**In This Tier:**
- L5: High score hall uses string variables for names
- L6: DATA-driven quiz for expandability

**In Next Tier:**
- String handling for game messages
- Player name entry for high scores

## Quick Reference

**String Variable Rules:**
- Declaration: `A$="TEXT"`
- Input: `INPUT A$`
- Comparison: `IF A$="VALUE" THEN...`
- String + string: `A$="HELLO"+"WORLD"` gives "HELLOWORLD"

**Common String Operations:**
- `LEFT$(A$,N)` - First N characters
- `RIGHT$(A$,N)` - Last N characters
- `MID$(A$,P,N)` - N characters starting at position P
- `LEN(A$)` - Length of string
