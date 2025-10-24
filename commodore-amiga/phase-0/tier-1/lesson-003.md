# Lesson 003: Dungeon Quest

**Arc:** Text Adventures
**Position:** Lesson 3 of 3 in arc
**Type:** Synthesis (Complete Game)
**Estimated Completion:** 50 lines of code

## Learning Objectives

- Combine Locate, Input$, and If...Then into complete game
- Use procedures (Proc/End Proc) for code organisation
- Manage game state with variables
- Create multi-room text adventure

## Prerequisites

**From Previous Lessons:**
- L1: Variables, loops, screen positioning
- L2: Input$, If...Then...End If

**AMOS Knowledge:**
- Structured programming basics

## Key Concepts Introduced

### Procedures (Proc...End Proc)
Procedures are named code blocks you can call from anywhere. Like subroutines but with structured syntax and no line numbers.

### State Variables
Track player location (room number), inventory (has_key), and progress using variables.

### Procedure Calls
Use procedure name to execute that block of code. Return to caller automatically.

### Game Loop Structure
Main loop repeatedly displays current state, gets input, processes commands, updates state.

## Code Pattern

```amos
' Dungeon Quest
room=1
has_key=0

Do
  Cls
  
  If room=1 Then Room1
  If room=2 Then Room2
  If room=3 Then Room3
  
  Locate 20,5: Input "Command: ";cmd$
  
  If cmd$="N" Then Add room,1
  If cmd$="S" Then Add room,-1
  
  If room>3 Then room=3
  If room<1 Then room=1
Loop

Procedure Room1
  Locate 5,10: Print "Dark cave entrance"
  Locate 7,10: Print "Exits: North"
End Proc

Procedure Room2
  Locate 5,10: Print "Treasure chamber"
  Locate 7,10: Print "You see a golden key"
End Proc
```

## Hardware Interaction

**Chips Involved:**
- 68000 CPU (managing game logic, procedure calls)
- Denise (displaying room descriptions)

**Screen Management:**
- Cls clears screen between rooms
- Locate positions room text and prompts
- Fast screen updates (no flicker)

## Common Pitfalls

1. **Forgetting End Proc:** Every Proc needs End Proc
2. **Wrong procedure call:** Just use name, no GOSUB or brackets
3. **Infinite loops:** Ensure valid commands always exist
4. **No Cls:** Screen becomes cluttered with old text

## Extension Ideas

- Add inventory system (keys, items)
- Create combat with random numbers
- Add scoring (treasures collected)
- Include multiple endings
- Save game state to variables

## Builds Toward

**In This Tier:**
- L4-6: Data for quiz/knowledge games
- L7-9: Graphics to enhance adventures

**In Next Tier:**
- Graphical adventures with BOBs and backgrounds
- Complex state management

## Quick Reference

**Essential Commands:**
- `Proc Name` - Define procedure
- `End Proc` - End procedure definition
- `Name` - Call procedure
- `Do...Loop` - Infinite loop (use Exit If to break)

**Game Structure:**
```amos
' Main loop
Do
  Display current state
  Get player input
  Process command
  Update state
Loop
```

**Procedure Pattern:**
```amos
Procedure ShowRoom
  Cls
  Print "Room description"
End Proc
```

**AMOS Advantages:**
- No line numbers (readable code)
- Procedures for organisation
- Fast BASIC execution
- Clean screen management

---

**Version:** 1.0
**Created:** 2025-10-24
**Status:** Lesson specification complete
