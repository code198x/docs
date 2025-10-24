# Lesson 009: Sprite Gallery

**Arc:** BOB Graphics
**Position:** Lesson 3 of 3 in arc
**Type:** Synthesis (Interactive Demo)
**Estimated Completion:** 80 lines of code

## Learning Objectives

- Create multiple BOBs for sprites
- Capture different frames for animation
- Interactive sprite viewer
- Master Bob command for automatic BOB management

## Key Concepts Introduced

### Bob Command (vs Paste Bob)
Bob command manages BOBs automatically: collision, movement tracking. Paste Bob is manual display.

### Multiple BOBs
Create sprite library with Get Bob for different graphics. Number them 1, 2, 3, etc.

### Bob Movement
Bob x,y,image sets BOB position and which image to display.

## Code Pattern

```amos
Screen Open 0,320,256,32,Lowres
Curs Off: Flash Off: Cls 0

' Create sprite graphics
Ink 2: Bar 0,0 To 15,15
Get Bob 1,0,0 To 16,16
Cls 0

Ink 3: Circle 8,8,7
Get Bob 2,0,0 To 16,16
Cls 0

' Display with Bob command
Bob 1,100,100,1
Bob 2,150,100,2

Do
  Wait Vbl
  Bob Update
Loop Until Inkey$<>""
```

## Quick Reference

- `Bob number,x,y,image` - Position and display BOB
- `Bob Update` - Refresh all BOBs
- `Wait Vbl` - Wait for vertical blank (50Hz PAL)
- Use Bob for automatic management
- Use Paste Bob for manual control

---

**Version:** 1.0
**Created:** 2025-10-24
