# Lesson 014: Collect & Score

**Arc:** Moving BOBs
**Position:** Lesson 3 of 3 in arc
**Type:** Synthesis (Complete Gameplay)
**Estimated Completion:** 70 lines of code

## Learning Objectives

- Implement timer countdown
- Create win/lose conditions
- Master Timer command
- Build complete game loop

## Key Concepts Introduced

### Timer Command
`Timer=value` sets timer (in 50Hz ticks). `Timer` reads current value. Counts down automatically. 50 ticks = 1 second.

### Game States
Track game state: playing, won, lost. Use state variable to control flow. Different behaviour per state.

### Win Conditions
Check score threshold and timer. Multiple conditions determine outcome. Clear feedback to player.

### Game Over Handling
Stop game loop when condition met. Display result. Wait for key to restart or quit.

## Code Pattern

```amos
Screen Open 0,320,256,32,Lowres
Curs Off: Flash Off

Procedure PlayGame
  Cls 0

  ' Create sprites
  Ink 2: Bar 0,0 To 15,15
  Get Bob 1,0,0 To 16,16
  Cls 0

  Ink 3: Circle 8,8,7
  Get Bob 2,0,0 To 16,16
  Cls 0

  px=150: py=120
  Bob 1,px,py,1

  ' Create 10 collectibles
  For i=2 To 11
    Bob i,Rnd(280)+20,Rnd(220)+20,2
  Next i

  score=0
  target=100
  Timer=30*50  ' 30 seconds

  Do
    ' Player movement
    If Jleft(1) Then Dec px,2
    If Jright(1) Then Add px,2
    If Jup(1) Then Dec py,2
    If Jdown(1) Then Add py,2

    Bob 1,px,py,1

    ' Collision detection
    hit=Col(1)
    If hit>1 Then
      Bob Off hit
      Add score,10
      Sam Play 0,1
    End If

    ' Display status
    Locate 0,0: Print "Score: ";score;" / ";target
    Locate 0,1: Print "Time: ";Timer/50

    ' Win condition
    If score>=target Then Exit

    ' Lose condition
    If Timer<=0 Then Exit

    Wait Vbl
    Bob Update
  Loop

  ' Game over
  Cls 0
  Locate 10,12
  If score>=target Then
    Print "YOU WIN!"
  Else
    Print "TIME'S UP!"
  End If
  Locate 9,14: Print "Final: ";score

  Wait Key
End Proc

PlayGame
```

## Quick Reference

- `Timer=value` - Set timer (50Hz ticks)
- `Timer` - Read current timer value
- 50 ticks = 1 second
- Use Exit to break from Do loop
- Procedure for restart capability

---

**Version:** 1.0
**Created:** 2025-10-24
