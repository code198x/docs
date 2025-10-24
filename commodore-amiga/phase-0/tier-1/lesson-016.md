# Lesson 016: Amiga Arcade

**Arc:** Mini Action Game
**Position:** Lesson 2 of 2 in arc
**Type:** Synthesis (Complete Game)
**Estimated Completion:** 100 lines of code

## Learning Objectives

- Combine all Phase 0 Tier 1 concepts
- Create complete arcade game
- Master game state management
- Implement restart functionality

## Key Concepts Introduced

### Complete Game Architecture
Menu system, game loop, game over screen. All states handled. Clean separation of procedures. Professional structure.

### Difficulty Progression
Enemies get faster or more numerous over time. Implement using timer or score threshold. Keeps gameplay engaging.

### Polish Elements
Sound effects for events, visual feedback, particle effects (multiple small BOBs), screen shake. Makes game feel complete.

### Restart System
Return to menu after game over. Reinitialize all variables. Allow repeated plays. Use procedures for clean organization.

## Code Pattern

```amos
Screen Open 0,320,256,32,Lowres
Curs Off: Flash Off

Procedure Menu
  Cls 0
  Locate 10,8: Print "AMIGA ARCADE"
  Locate 12,10: Print "1. Start Game"
  Locate 13,10: Print "2. Quit"

  Do
    k$=Inkey$
    If k$="1" Then PlayGame
    If k$="2" Then End
  Loop
End Proc

Procedure PlayGame
  Cls 0

  ' Create sprites
  Ink 2: Bar 0,0 To 15,15
  Get Bob 1,0,0 To 16,16
  Cls 0

  Ink 1: Box 0,0 To 15,15
  Get Bob 2,0,0 To 16,16
  Cls 0

  Ink 3: Circle 8,8,7
  Get Bob 3,0,0 To 16,16
  Cls 0

  ' Initialize game state
  Dim ex(8),ey(8),ea(8)
  Dim cx(10),cy(10),ca(10)

  ' Player
  px=150: py=120
  Bob 1,px,py,1

  ' Enemies
  enemyCount=5
  enemySpeed=1
  For i=1 To enemyCount
    ex(i)=Rnd(280)+20
    ey(i)=Rnd(220)+20
    ea(i)=1
    Bob i+10,ex(i),ey(i),2
  Next i

  ' Collectibles
  For i=1 To 10
    cx(i)=Rnd(280)+20
    cy(i)=Rnd(220)+20
    ca(i)=1
    Bob i+20,cx(i),cy(i),3
  Next i

  score=0
  lives=3
  Timer=60*50

  ' Game loop
  Do
    ' Player movement
    If Jleft(1) Then Dec px,3
    If Jright(1) Then Add px,3
    If Jup(1) Then Dec py,3
    If Jdown(1) Then Add py,3

    ' Boundaries
    If px<0 Then px=0
    If px>304 Then px=304
    If py<0 Then py=0
    If py>240 Then py=240

    Bob 1,px,py,1

    ' Update enemies
    For i=1 To enemyCount
      If ea(i)=1 Then
        If ex(i)<px Then Add ex(i),enemySpeed
        If ex(i)>px Then Dec ex(i),enemySpeed
        If ey(i)<py Then Add ey(i),enemySpeed
        If ey(i)>py Then Dec ey(i),enemySpeed
        Bob i+10,ex(i),ey(i),2
      End If
    Next i

    ' Collect items
    hit=Col(1)
    If hit>=21 and hit<=30 Then
      itemNum=hit-20
      If ca(itemNum)=1 Then
        ca(itemNum)=0
        Bob Off hit
        Add score,10
        Sam Play 0,1
      End If
    End If

    ' Hit enemy
    If hit>=11 and hit<=10+enemyCount Then
      enemyNum=hit-10
      If ea(enemyNum)=1 Then
        ea(enemyNum)=0
        Bob Off hit
        Dec lives,1
        Sam Play 1,5
        If lives<=0 Then Exit
      End If
    End If

    ' Difficulty increase
    If score>50 and enemySpeed=1 Then enemySpeed=2

    ' Display HUD
    Locate 0,0: Print "Score: ";score
    Locate 0,1: Print "Lives: ";lives
    Locate 0,2: Print "Time: ";Timer/50

    ' Time up
    If Timer<=0 Then Exit

    Wait Vbl
    Bob Update
  Loop

  ' Game over
  For i=1 To 30
    Bob Off i
  Next i

  Cls 0
  Locate 10,10
  If lives>0 Then
    Print "TIME'S UP!"
  Else
    Print "GAME OVER!"
  End If
  Locate 9,12: Print "Final Score: ";score
  Locate 8,14: Print "Press any key"

  Wait Key
  Menu
End Proc

' Start game
Menu
```

## Quick Reference

- Combine: Procedures, Arrays, BOBs, Collision, Input, Sound, Timer
- Use procedures for clean state management
- Initialize all variables at procedure start
- For loop to create/hide multiple BOBs
- Menu → Game → Game Over → Menu loop

**This lesson synthesizes all Phase 0 Tier 1 concepts into a complete playable game.**

---

**Version:** 1.0
**Created:** 2025-10-24
