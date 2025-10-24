# Lesson 012: BOB Movement

**Arc:** Moving BOBs
**Position:** Lesson 1 of 3 in arc
**Type:** Standard
**Estimated Completion:** 40 lines of code

## Learning Objectives

- Move BOBs with keyboard/joystick input
- Understand coordinate system
- Implement smooth movement
- Master Bob X/Y for position reading

## Key Concepts Introduced

### Bob Movement
Bob command updates BOB position. `Bob number,x,y,image` sets coordinates. Movement is setting new coordinates each frame.

### Input Handling
`Jleft(port)`, `Jright(port)`, `Jup(port)`, `Jdown(port)` read joystick. Port 1 is standard. Returns -1 if pressed, 0 otherwise.

### Position Reading
`Bob X(number)` and `Bob Y(number)` return current BOB coordinates. Use for boundary checking and collision.

### Movement Speed
Control speed by adding different values to coordinates. `Add x,2` moves faster than `Add x,1`.

## Code Pattern

```amos
Screen Open 0,320,256,32,Lowres
Curs Off: Flash Off: Cls 0

' Create sprite
Ink 2: Bar 0,0 To 15,15
Get Bob 1,0,0 To 16,16
Cls 0

x=150: y=120
speed=2

Do
  ' Read joystick port 1
  If Jleft(1) Then Dec x,speed
  If Jright(1) Then Add x,speed
  If Jup(1) Then Dec y,speed
  If Jdown(1) Then Add y,speed

  ' Boundary checking
  If x<0 Then x=0
  If x>304 Then x=304
  If y<0 Then y=0
  If y>240 Then y=240

  ' Update BOB
  Bob 1,x,y,1

  Wait Vbl
  Bob Update
Loop Until Inkey$<>""
```

## Quick Reference

- `Bob X(number)` - Get BOB X coordinate
- `Bob Y(number)` - Get BOB Y coordinate
- `Jleft(port)`, `Jright(port)` - Joystick input
- `Jup(port)`, `Jdown(port)` - Joystick input
- `Add variable,value` - Increment
- `Dec variable,value` - Decrement

---

**Version:** 1.0
**Created:** 2025-10-24
