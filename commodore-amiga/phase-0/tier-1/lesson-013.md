# Lesson 013: Collision Master

**Arc:** Moving BOBs
**Position:** Lesson 2 of 3 in arc
**Type:** Standard
**Estimated Completion:** 50 lines of code

## Learning Objectives

- Detect BOB collisions with Col
- Implement pickup mechanics
- Use multiple BOBs in gameplay
- Master Bob Off to hide sprites

## Key Concepts Introduced

### Col Command
`Col(number)` returns collision state. Returns BOB number that was hit, or 0 for no collision. Automatic hardware detection.

### Bob Off
`Bob Off number` disables and hides a BOB. More efficient than moving off-screen. Use for collected items.

### Multiple Active BOBs
Track multiple sprites (player + items). Each has its own number, position, and collision detection.

### Game Loop Pattern
Input → Movement → Collision → Update Display. Standard game architecture for interactive programs.

## Code Pattern

```amos
Screen Open 0,320,256,32,Lowres
Curs Off: Flash Off: Cls 0

' Create player sprite
Ink 2: Bar 0,0 To 15,15
Get Bob 1,0,0 To 16,16
Cls 0

' Create collectible
Ink 3: Circle 8,8,7
Get Bob 2,0,0 To 16,16
Cls 0

px=50: py=120
Bob 1,px,py,1

' 5 collectibles
For i=2 To 6
  Bob i,Rnd(280)+20,Rnd(220)+20,2
Next i

score=0

Do
  ' Player movement
  If Jleft(1) Then Dec px,2
  If Jright(1) Then Add px,2
  If Jup(1) Then Dec py,2
  If Jdown(1) Then Add py,2

  Bob 1,px,py,1

  ' Check collisions
  hit=Col(1)
  If hit>1 Then
    Bob Off hit
    Add score,10
  End If

  Locate 0,0: Print "Score: ";score

  Wait Vbl
  Bob Update
Loop Until Inkey$<>""
```

## Quick Reference

- `Col(number)` - Returns BOB number hit (0=none)
- `Bob Off number` - Hide BOB
- `Bob On number` - Show BOB
- Collision is hardware-detected
- Use For loop to create multiple BOBs

---

**Version:** 1.0
**Created:** 2025-10-24
