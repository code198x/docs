# Lesson 003: Cave Explorer

**Arc:** Text Adventures
**Position:** Lesson 3 of 3 in arc
**Type:** Synthesis (Complete Game)
**Estimated Completion:** 40 lines of code

## Learning Objectives

- Combine PRINT AT, INPUT, and IF...THEN into a complete game
- Manage game state with variables
- Create multi-room navigation
- Build a playable text adventure

## Prerequisites

**From Previous Lessons:**
- L1: Variables, loops, PRINT AT
- L2: INPUT, IF...THEN, string variables

**BASIC Knowledge:**
- Text positioning and user input
- Conditional branching

## Key Concepts Introduced

### State Management
Track where the player is (room number) and what they're carrying (inventory flag) using variables.

### Multiple Paths
Use IF statements to create different outcomes based on player choices.

### Game Loop
Main loop that repeatedly asks "What do you do?" and processes commands.

### Win/Lose Conditions
Test for completion (found treasure) or failure (entered dangerous room).

## Code Pattern

```basic
10 REM Cave Explorer
20 LET room=1
30 LET haskey=0
40 CLS
50 IF room=1 THEN GOSUB 1000
60 IF room=2 THEN GOSUB 2000
70 IF room=3 THEN GOSUB 3000
80 INPUT "Command: ";c$
90 REM Process commands
100 GO TO 40
1000 REM Room 1 description
1010 PRINT AT 5,5;"Dark cave entrance"
1020 RETURN
2000 REM Room 2 description
2010 PRINT AT 5,5;"Treasure chamber"
2020 RETURN
```

## Hardware Interaction

**Chips Involved:**
- Z80 CPU (managing game logic)
- ULA (displaying room descriptions)

**Screen Layout:**
- Top: Room description
- Middle: Available exits
- Bottom: Command input

## Common Pitfalls

1. **Forgetting RETURN in GOSUBs:** Each room subroutine needs RETURN
2. **No CLS between rooms:** Screen becomes cluttered
3. **Complex string matching:** Keep commands simple (N, S, E, W)
4. **Infinite loops:** Ensure there's always a way forward

## Extension Ideas

- Add more rooms (dungeon map)
- Create inventory system (keys, torches)
- Add simple combat (random number checks)
- Include scoring (treasures collected)
- Save game state with variables

## Builds Toward

**In This Tier:**
- L4-6: DATA for quiz/knowledge games
- L7-9: Graphics to enhance text adventures

**In Next Tier:**
- Graphical adventures (mixing text and simple graphics)
- More complex state management

## Quick Reference

**Essential Commands:**
- `GOSUB linenumber` - Jump to subroutine
- `RETURN` - Return from subroutine
- `CLS` - Clear screen
- `REM` - Comment (remark)

**Game Structure:**
```basic
Main loop:
  Display current state
  Get player input
  Process command
  Update state
  Repeat
```

**String Comparisons:**
- Use `IF c$="N" THEN ...` for cardinal directions
- Consider `LEFT$(c$,1)` to match just first letter

**Spectrum Features:**
- Fast BASIC keeps text adventure responsive
- PRINT AT allows clean screen layouts
- Keyword entry speeds up development

---

**Version:** 1.0
**Created:** 2025-10-24
**Status:** Lesson specification complete
