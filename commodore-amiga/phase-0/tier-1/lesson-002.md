# Lesson 002: Interactive Oracle

**Arc:** Text Adventures
**Position:** Lesson 2 of 3 in arc
**Type:** Standard
**Estimated Completion:** 20 lines of code

## Learning Objectives

- Use Input$ to receive user text input
- Make decisions with If...Then...End If
- Create interactive branching programs
- Master AMOS's structured conditionals (no line numbers)

## Prerequisites

**From Previous Lessons:**
- L1: Variables, loops, Locate, Repeat...Until

**AMOS Knowledge:**
- Variables and screen positioning

## Key Concepts Introduced

### Input$ for User Interaction
Input$ pauses and waits for user to type text. Returns the entered string for the program to use.

### Structured Conditionals (If...End If)
AMOS uses If...Then...End If blocks (not single-line IF THEN). This allows multiple commands inside conditions without line numbers.

### String Comparison
Compare strings with = (equals). AMOS is not case-sensitive by default for string comparisons.

### Multiple Conditions
Use Else for alternative paths, Or/And for compound conditions.

## Code Pattern

```amos
' Interactive greeting
name$=""

Print "What is your name?"
Input name$

If name$="Alice" Then
  Print "Hello Alice, welcome back!"
Else
  Print "Nice to meet you, "+name$
End If

Print "Pick a number 1-10:"
Input guess

If guess=7 Then
  Print "Lucky number!"
Else
  Print "Try again!"
End If
```

## Hardware Interaction

**Chips Involved:**
- 68000 CPU (AMOS interpreter, string processing)
- CIA chips (keyboard scanning)
- Denise (screen display)

**Screen:**
- Text appears in current screen mode (default 320×256 low-res)
- Locate positions cursor for clean layouts

## Common Pitfalls

1. **Forgetting End If:** Every If must have matching End If
2. **No Then:** Must write `If condition Then` (not just `If condition`)
3. **Wrong string syntax:** Use $ for string variables (`name$` not `name`)
4. **No Else If in early AMOS:** Use nested If blocks instead

## Extension Ideas

- Ask multiple questions in sequence
- Create personality quiz with scoring
- Add Ink commands for coloured responses
- Use Locate to position text creatively
- Create choose-your-own-adventure branches

## Builds Toward

**In This Tier:**
- L3: Complete text adventure with rooms
- L4-6: Data statements for knowledge systems

**In Next Tier:**
- Input$ for game configuration (difficulty, player name)
- Complex branching for game state

## Quick Reference

**Essential Commands:**
- `Input variable$` - Get string input from user
- `If condition Then...End If` - Conditional block
- `Else` - Alternative branch
- `Or` / `And` - Combine conditions

**String Operations:**
- Concatenation: `"Hello "+name$`
- Comparison: `If name$="Alice" Then`
- Case-insensitive by default

**Structured Syntax:**
```amos
If score>100 Then
  Print "High score!"
  Add bonus,50
Else
  Print "Keep trying"
End If
```

---

**Version:** 1.0
**Created:** 2025-10-24
**Status:** Lesson specification complete
