# Lesson 020: Collision During Animation

**Arc:** Animation System
**Position:** Lesson 4 of 5 in arc
**Type:** Standard
**Estimated Completion:** 120 lines of code

## Learning Objectives

- Detect collisions on specific animation frames
- Implement frame-based hitboxes
- Create attack animations with active frames
- Handle collision response during animation states

## Prerequisites

**From Previous Lessons:**
- Collision detection (L13)
- Multi-frame animation (L18)
- Animation synchronization (L19)

**AMOS Knowledge:**
- Col function for hardware collision
- Bob Image for frame detection
- State machine patterns

## Key Concepts Introduced

### Frame-Based Collision Boxes
Different animation frames have different collision areas. A punch animation might only deal damage on frames 3-5 (arm extended), not during windup (frames 1-2) or recovery (frames 6-8).

### Active Frames
Specific frames in an animation where collision should be checked. Attack animations have "active" frames where they can hit enemies.

### Collision Response States
When hit during animation, interrupt current animation and switch to damage/knockback state. Prevents unrealistic behavior (continuing attack while being hit).

### Invulnerability Frames (I-Frames)
Brief period after taking damage where further hits don't register. Prevents unfair rapid-fire damage from single attack.

## Code Pattern

```amos
Screen Open 0,320,256,32,Lowres
Curs Off: Flash Off: Cls 0

' Create frames
' 1-4: Walk, 5-8: Attack, 9-12: Hurt
For F=1 To 12
  Ink 2
  Bar 0,0 To 15,15
  Get Bob F,0,0 To 16,16
  Cls 0
Next F

' Player BOB
Bob 1,100,128,1
x=100: y=128: state$="idle"
invincible=0

' Enemy BOB
Bob 2,200,128,1
ex=200: ey=128: enemyHp=3

' Main loop
Do
  ' Player input
  If Jleft(1) Then Dec x,2: state$="walk"
  If Jright(1) Then Add x,2: state$="walk"

  If Fire(1) and state$<>"attack" Then
    state$="attack"
    attackFrame=1
    Anim 1,"5,6,7,8",15
  End If

  ' Player animation state
  If state$="walk" and Not Jleft(1) and Not Jright(1) Then state$="idle"
  If state$="idle" Then Anim Freeze 1
  If state$="walk" Then Anim 1,"1,2,3,4",10

  ' Attack animation
  If state$="attack"
    currentFrame=Bob Image(1)

    ' Active frames: 6-7 (arm extended)
    If currentFrame>=6 and currentFrame<=7
      ' Check collision with enemy
      If Col(1)=2
        Dec enemyHp
        Print "Hit! Enemy HP: ";enemyHp
        If enemyHp<=0 Then Bob Off 2
      End If
    End If

    ' Attack complete
    If currentFrame=8 Then state$="idle"
  End If

  ' Player takes damage
  If invincible<=0
    If Col(1)=2 and state$<>"attack"
      state$="hurt"
      invincible=50  ' 1 second invulnerability
      Anim 1,"9,10,11,12",10
    End If
  Else
    Dec invincible
  End If

  ' Hurt animation complete
  If state$="hurt" and Bob Image(1)=12
    state$="idle"
  End If

  Bob 1,x,y,Bob Image(1)
  Bob 2,ex,ey,1
  Wait Vbl
  Bob Update
Loop Until Inkey$<>""
```

## Hardware Interaction

**Chips Involved:**
- **Blitter** - Hardware collision detection via Col function
- **Denise** - Sprite collision registers read by Blitter
- **CPU** - Frame-based logic, state management

**Collision Detection:**
- Col function reads Blitter collision registers each frame
- Collision mask set by Bob priority/transparency
- Frame check (Bob Image) determines if hit is valid
- State machine prevents collision during invulnerable states

## Common Pitfalls

1. **Collision on all frames:** Attack hitting even during windup looks wrong
2. **No invulnerability:** Single attack causes multiple hits (unfair)
3. **Animation lock:** Can't move after attack starts (frustrating)
4. **Collision check after Bob Update:** Positions already changed, collision one frame late
5. **Forgetting to reset state:** Stuck in "hurt" animation forever

## Extension Ideas

- Different hitboxes per frame (smaller during duck)
- Multi-hit attacks (each active frame is separate hit)
- Counter-attack window (perfect timing blocks)
- Combo system (chain attacks if timed correctly)
- Environmental collision during animation (can't attack through walls)

## Builds Toward

**In This Tier:**
- L21: Complete animated sprite showcase with all systems

**In Next Tier:**
- Fighting game mechanics
- Complex combat systems

## Quick Reference

### Active Frame Pattern
```amos
' Define active frames for animation
If state$="attack"
  frame=Bob Image(playerBob)

  ' Only frames 6-7 deal damage
  If frame>=6 and frame<=7
    If Col(playerBob)=enemyBob
      ' Deal damage
    End If
  End If

  ' End of animation
  If frame=8 Then state$="idle"
End If
```

### Invulnerability Pattern
```amos
' Set invulnerability
invincibleTimer=50  ' 50 frames = 1 second

' Each frame
If invincibleTimer>0 Then Dec invincibleTimer

' Check collision only when vulnerable
If invincibleTimer<=0
  If Col(playerBob)=enemyBob
    ' Take damage
    invincibleTimer=50  ' Reset
  End If
End If
```

### Collision Response
```amos
' Interrupt current animation
If state$<>"hurt" and invincible<=0
  If Col(1)=2
    ' Stop current animation
    Anim Off 1

    ' Switch to hurt state
    state$="hurt"
    hurtTimer=30
    invincible=50
    Anim 1,"9,10,11,12",15
  End If
End If
```

### Frame-Specific Hitboxes
```amos
' Different collision behavior per frame
frame=Bob Image(1)

' Standing (frame 1): normal hitbox
If frame=1 Then hitboxHeight=16

' Ducking (frame 5): smaller hitbox
If frame=5 Then hitboxHeight=8

' Jumping (frame 9): shifted hitbox
If frame=9 Then hitboxHeight=12: hitboxY=y-4
```

### Multi-Hit Attacks
```amos
' Track which frame last dealt damage
lastHitFrame=0

If state$="attack"
  frame=Bob Image(1)

  ' Frames 3, 5, 7 are active
  If frame=3 or frame=5 or frame=7
    ' Only hit if this frame hasn't hit yet
    If frame<>lastHitFrame
      If Col(1)=2
        ' Deal damage
        lastHitFrame=frame
      End If
    End If
  End If

  ' Reset when animation ends
  If frame=8 Then lastHitFrame=0: state$="idle"
End If
```

### Visual Feedback
```amos
' Flash sprite during invulnerability
If invincible>0
  ' Blink every 4 frames
  If (invincible Mod 8)<4
    Bob Off 1  ' Hide
  Else
    Bob On 1   ' Show
  End If
Else
  Bob On 1  ' Always visible when vulnerable
End If
```

---

**Version:** 1.0
**Created:** 2025-10-27
