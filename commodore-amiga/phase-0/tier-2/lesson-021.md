# Lesson 021: Animated Sprite Showcase

**Arc:** Animation System
**Position:** Lesson 5 of 5 in arc (DELIVERABLE)
**Type:** Synthesis
**Estimated Completion:** 250-300 lines of code

## Learning Objectives

- Synthesize all Animation System arc concepts
- Create polished animated sprite demo
- Implement complete character controller
- Deliver production-quality showcase

## Prerequisites

**From This Arc:**
- AMAL movement (L17)
- Multi-frame animation (L18)
- Animation synchronization (L19)
- Collision during animation (L20)

**From Tier 1:**
- All BOB, collision, scoring, and timing concepts

## Key Concepts Introduced

### Character Controller Architecture
Complete system combining movement, animation, collision, and state management into cohesive character control.

### Polish and Juice
Visual and audio feedback that makes interaction feel responsive: screen shake on hit, particle effects, sound effects synchronized to animation frames.

### Demo Structure
Self-running demonstration with menu, instructions, multiple scenarios showing different techniques.

### Code Organization
Procedures for each system (movement, animation, collision) keep code maintainable.

## Code Pattern

This is a complete showcase program demonstrating:
- 8-direction movement with animation
- Attack combos with active frames
- Enemy AI with animated states
- Particle effects synchronized to animations
- Screen transitions and polish

```amos
' ================================================
' ANIMATED SPRITE SHOWCASE
' Demonstrates: AMAL, multi-frame animation,
' state machines, collision, polish
' ================================================

Screen Open 0,320,256,32,Lowres
Curs Off: Flash Off: Cls 0
Hide

' ================================================
' ASSET LOADING
' ================================================
Procedure LoadAssets
  ' Player frames: 1-8 walk, 9-12 attack, 13-16 hurt
  For F=1 To 16
    Ink 2+F Mod 4
    Bar 0,0 To 31,31
    ' Draw player frame F (varies by animation)
    Get Bob F,0,0 To 32,32
    Cls 0
  Next F

  ' Enemy frames: 17-20 walk, 21-24 attack
  For F=17 To 24
    Ink 5
    Bar 0,0 To 31,31
    Get Bob F,0,0 To 32,32
    Cls 0
  Next F

  ' Particle effect frames: 25-28
  For F=25 To 28
    Ink 7
    Bar 0,0 To 7,7
    Get Bob F,0,0 To 8,8
    Cls 0
  Next F
End Proc

' ================================================
' MAIN MENU
' ================================================
Procedure ShowMenu
  Cls 0
  Locate 10,5: Print "ANIMATED SPRITE SHOWCASE"
  Locate 8,8: Print "1. Movement & Animation Demo"
  Locate 8,10: Print "2. Combat System Demo"
  Locate 8,12: Print "3. State Machine Demo"
  Locate 8,14: Print "ESC to Exit"

  Repeat
    K$=Inkey$
  Until K$="1" or K$="2" or K$="3" or K$=Chr$(27)

  If K$="1" Then MovementDemo
  If K$="2" Then CombatDemo
  If K$="3" Then StateMachineDemo
End Proc

' ================================================
' DEMO 1: MOVEMENT & ANIMATION
' ================================================
Procedure MovementDemo
  Cls 0
  Locate 5,1: Print "8-Direction Movement + Animation"

  ' Player setup
  px=160: py=128: pdir=0
  Bob 1,px,py,1

  Do
    ' Input
    dx=0: dy=0
    If Jleft(1) Then Dec dx,2
    If Jright(1) Then Add dx,2
    If Jup(1) Then Dec dy,2
    If Jdown(1) Then Add dy,2

    ' Update position
    Add px,dx: Add py,dy

    ' Boundary check
    If px<16 Then px=16
    If px>304 Then px=304
    If py<16 Then py=16
    If py>240 Then py=240

    ' Animation based on movement
    If dx<>0 or dy<>0
      ' Walking
      Anim 1,"1,2,3,4,5,6,7,8",12
    Else
      ' Idle
      Anim Freeze 1
    End If

    Bob 1,px,py,Bob Image(1)
    Wait Vbl
    Bob Update
  Loop Until Inkey$<>""

  Anim Off 1
End Proc

' ================================================
' DEMO 2: COMBAT SYSTEM
' ================================================
Procedure CombatDemo
  Cls 0
  Locate 5,1: Print "Combat: Fire to Attack"

  ' Player
  px=80: py=128: pstate$="idle"
  invincible=0
  Bob 1,px,py,1

  ' Enemy
  ex=240: ey=128: enemyHp=5: enemyState$="idle"
  Bob 2,ex,ey,17

  Do
    ' === PLAYER UPDATE ===
    ' Movement
    If Jleft(1) and pstate$<>"attack" Then Dec px,2
    If Jright(1) and pstate$<>"attack" Then Add px,2

    ' Attack input
    If Fire(1) and pstate$="idle"
      pstate$="attack"
      attackFrame=0
      Anim 1,"9,10,11,12",15
    End If

    ' Player state machine
    If pstate$="attack"
      frame=Bob Image(1)

      ' Active frames: 10-11
      If frame>=10 and frame<=11
        If Col(1)=2
          Dec enemyHp
          enemyState$="hurt"
          invincible=30
          Locate 5,3: Print "Hit! Enemy HP: ";enemyHp;" "
        End If
      End If

      ' Attack complete
      If frame=12 Then pstate$="idle"
    End If

    ' Player animation
    If pstate$="idle" Then Anim Freeze 1

    ' === ENEMY UPDATE ===
    ' Simple AI: chase player
    If enemyState$="idle"
      If ex<px Then Add ex,1
      If ex>px Then Dec ex,1
      Anim 2,"17,18,19,20",10
    End If

    ' Enemy hurt state
    If enemyState$="hurt"
      Anim 2,"21,22,23,24",15
      Dec invincible
      If invincible<=0 Then enemyState$="idle"
    End If

    ' Enemy defeated
    If enemyHp<=0 Then Bob Off 2

    Bob 1,px,py,Bob Image(1)
    Bob 2,ex,ey,Bob Image(2)
    Wait Vbl
    Bob Update
  Loop Until Inkey$<>""

  Anim Off
  Bob Off 2
End Proc

' ================================================
' DEMO 3: STATE MACHINE
' ================================================
Procedure StateMachineDemo
  Cls 0
  Locate 2,1: Print "State Machine: Idle/Walk/Jump/Attack"

  px=160: py=200: pstate$="idle"
  grounded=True
  vy=0
  jumpTimer=0

  Bob 1,px,py,1

  Do
    ' Input
    If Jleft(1) and grounded Then Dec px,2: pstate$="walk"
    If Jright(1) and grounded Then Add px,2: pstate$="walk"
    If Fire(1) and grounded and pstate$<>"jump"
      pstate$="jump"
      vy=-8
      grounded=False
      jumpTimer=30
    End If

    ' Idle when no input
    If Not Jleft(1) and Not Jright(1) and grounded
      If pstate$="walk" Then pstate$="idle"
    End If

    ' Jump physics
    If pstate$="jump"
      Add py,vy
      Add vy,1  ' Gravity

      ' Landing
      If py>=200
        py=200
        vy=0
        grounded=True
        pstate$="idle"
      End If
    End If

    ' State animations
    If pstate$="idle" Then Anim Freeze 1
    If pstate$="walk" Then Anim 1,"1,2,3,4",10
    If pstate$="jump" Then Anim 1,"5,6,7,8",10

    ' Debug display
    Locate 2,3: Print "State: ";pstate$;"      "
    Locate 2,4: Print "Grounded: ";grounded;"  "

    Bob 1,px,py,Bob Image(1)
    Wait Vbl
    Bob Update
  Loop Until Inkey$<>""

  Anim Off
End Proc

' ================================================
' MAIN
' ================================================
LoadAssets
Repeat
  ShowMenu
Until False
```

## Hardware Interaction

**Full Amiga Hardware Stack:**
- **Blitter** - All BOB rendering, collision detection
- **Copper** - Palette changes, raster effects
- **Paula** - 4-channel audio synchronized to animations
- **CPU** - State machines, AI, game logic

**Performance Optimization:**
- Procedures reduce code duplication
- Anim Freeze when not moving (saves Blitter cycles)
- Bob Off for destroyed entities (frees hardware sprite)
- Wait Vbl ensures 50fps lock

## Common Pitfalls

1. **Scope creep:** Trying to do too much, deliverable becomes unfinishable
2. **No polish:** Technically correct but feels unresponsive
3. **Hard-coded values:** Magic numbers scattered throughout
4. **No instructions:** User doesn't know what keys do what
5. **Performance issues:** Too many BOBs or particles at once

## Extension Ideas

- Multiple enemy types with different AI
- Power-ups that change player abilities
- Boss battle with complex animation phases
- Particle system for hit effects
- Background parallax scrolling
- Combo counter with visual feedback

## Builds Toward

**Next Arc (Arcade Action):**
- Fast-paced BOB movement
- Blitter optimization
- Space shooter mechanics

**Future Tiers:**
- Advanced character controllers
- Complex AI systems

## Quick Reference

### Demo Structure
```amos
Procedure ShowMenu
  ' Display options
  ' Get input
  ' Call appropriate demo
End Proc

Procedure Demo1
  ' Setup
  ' Main loop
  ' Cleanup
End Proc

' Main
LoadAssets
Repeat
  ShowMenu
Until Exit_Condition
```

### Character Controller Pattern
```amos
' State
px,py,pstate$,invincible,grounded

' Input phase
If Jleft(1) Then Dec px,speed
If Fire(1) Then pstate$="attack"

' Physics phase
If Not grounded Then Add vy,gravity

' State machine phase
If pstate$="attack"
  ' Handle attack
End If

' Animation phase
If pstate$="idle" Then Anim Freeze 1
If pstate$="walk" Then Anim 1,"1,2,3,4",10

' Render phase
Bob 1,px,py,Bob Image(1)
Wait Vbl
Bob Update
```

### Polish Techniques
```amos
' Screen shake on hit
If hitOccurred
  Screen Offset 0,Rnd(4)-2,Rnd(4)-2
  Wait 3
  Screen Offset 0,0,0
End If

' Particle burst
Procedure SpawnParticles[x,y]
  For I=1 To 5
    ' Create particle BOB
    Bob nextBob,x,y,25
    ' Set velocity
    Amal nextBob,"M "+Str$(Rnd(40)-20)+","+Str$(Rnd(40)-20)+",30"
    Amal On nextBob
  Next I
End Proc

' Flash white on hit
Procedure HitFlash
  ' Store original colour
  oldColour=Colour(2)
  ' Flash white
  Colour 2,$FFF
  Wait 3
  ' Restore
  Colour 2,oldColour
End Proc
```

---

**Version:** 1.0
**Created:** 2025-10-27
**Note:** This is a DELIVERABLE lesson. Students create a portfolio piece demonstrating mastery of Animation System arc.
