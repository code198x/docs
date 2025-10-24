# Lesson 015: Enemy AI

**Arc:** Mini Action Game
**Position:** Lesson 1 of 2 in arc
**Type:** Standard
**Estimated Completion:** 60 lines of code

## Learning Objectives

- Implement simple enemy movement AI
- Use arrays to track multiple enemies
- Create chase/patrol behaviour
- Master Dim for enemy data

## Key Concepts Introduced

### Enemy Arrays
Use parallel arrays for enemy state. `Dim ex(10),ey(10),ea(10)` creates arrays for X position, Y position, and active status.

### Chase AI
Simple AI: move towards player. Compare enemy X/Y with player X/Y, adjust position. Creates pursuit behaviour.

### Active State Tracking
Use boolean array (0/1) to track if enemy is active. Skip inactive enemies in update loop. Efficient enemy management.

### Multiple Independant Entities
Each enemy acts independently. Loop through all enemies, update each one. Foundation for complex gameplay.

## Code Pattern

```amos
Screen Open 0,320,256,32,Lowres
Curs Off: Flash Off: Cls 0

' Create sprites
Ink 2: Bar 0,0 To 15,15
Get Bob 1,0,0 To 16,16
Cls 0

Ink 1: Box 0,0 To 15,15
Get Bob 2,0,0 To 16,16
Cls 0

' Enemy data
Dim ex(5),ey(5),ea(5)

' Create enemies
For i=1 To 5
  ex(i)=Rnd(280)+20
  ey(i)=Rnd(220)+20
  ea(i)=1  ' Active
  Bob i+1,ex(i),ey(i),2
Next i

px=150: py=120
Bob 1,px,py,1

Do
  ' Player movement
  If Jleft(1) Then Dec px,2
  If Jright(1) Then Add px,2
  If Jup(1) Then Dec py,2
  If Jdown(1) Then Add py,2

  Bob 1,px,py,1

  ' Update enemies
  For i=1 To 5
    If ea(i)=1 Then
      ' Simple chase AI
      If ex(i)<px Then Add ex(i),1
      If ex(i)>px Then Dec ex(i),1
      If ey(i)<py Then Add ey(i),1
      If ey(i)>py Then Dec ey(i),1

      Bob i+1,ex(i),ey(i),2
    End If
  Next i

  ' Check collision with enemies
  hit=Col(1)
  If hit>1 Then
    ' Hit enemy - deactivate it
    enemyNum=hit-1
    If enemyNum>=1 and enemyNum<=5 Then
      ea(enemyNum)=0
      Bob Off hit
    End If
  End If

  Wait Vbl
  Bob Update
Loop Until Inkey$<>""
```

## Quick Reference

- `Dim array(size)` - Create array
- Use parallel arrays for entity data
- Loop through entities to update
- Simple AI: compare positions, adjust
- Track active/inactive state

---

**Version:** 1.0
**Created:** 2025-10-24
