# Lesson 019: Animation Synchronization

**Arc:** Animation System
**Position:** Lesson 3 of 5 in arc
**Type:** Standard
**Estimated Completion:** 100 lines of code

## Learning Objectives

- Synchronize animations with game events
- Control animation state programmatically
- Trigger animations based on conditions
- Chain animation sequences

## Prerequisites

**From Previous Lessons:**
- Multi-frame animation (L18)
- AMAL movement (L17)
- Collision detection (L13)
- Timer usage (L14)

**AMOS Knowledge:**
- Anim command and sequences
- Bob Image for frame detection
- Procedure structure

## Key Concepts Introduced

### State-Based Animation
Different animations for different states (idle, walking, jumping). Change which Anim sequence is active based on player state.

### Animation Callbacks
Detect when animation completes by checking frame number. Trigger next action when sequence finishes.

### Frame-Perfect Timing
Use Timer or frame counters to ensure animations play for exact duration before transitioning to next state.

### Animation Layers
Multiple BOBs with synchronized animations (e.g., character body + weapon overlay) to create complex composite sprites.

## Code Pattern

```amos
Screen Open 0,320,256,32,Lowres
Curs Off: Flash Off: Cls 0

' Create animation frames
' Frames 1-4: Walk cycle
' Frames 5-8: Jump sequence
For F=1 To 8
  Ink 2
  Bar 0,0 To 15,15
  ' Draw appropriate pose for frame
  Get Bob F,0,0 To 16,16
  Cls 0
Next F

Bob 1,160,128,1
x=160: y=128: state$="idle"

' Main loop
Do
  ' Input handling
  If Jleft(1) Then Dec x,2: state$="walk"
  If Jright(1) Then Add x,2: state$="walk"
  If Fire(1) and state$<>"jump" Then state$="jump": jumpTimer=30

  ' No input = idle
  If Not Jleft(1) and Not Jright(1) and state$="walk" Then state$="idle"

  ' Update animation based on state
  If state$="idle"
    Anim Freeze 1  ' Stop on current frame
  End If

  If state$="walk"
    Anim 1,"1,2,3,4,3,2",10  ' Walking animation
  End If

  If state$="jump"
    Anim 1,"5,6,7,8",15      ' Jump animation
    Dec jumpTimer
    If jumpTimer<=0 Then state$="idle"
  End If

  Bob 1,x,y,Bob Image(1)
  Wait Vbl
  Bob Update
Loop Until Inkey$<>""
```

## Hardware Interaction

**Chips Involved:**
- **Blitter** - Updates sprite frames each Vbl
- **CPU** - State machine logic, Anim control
- **Paula** - Can trigger sounds on state changes

**Synchronization Techniques:**
- State machine runs each frame before Bob Update
- Anim command changed immediately when state changes
- Timer ensures minimum duration for time-based states
- Frame checking allows event triggers on specific frames

## Common Pitfalls

1. **Animation stutter:** Changing Anim every frame causes restart, use state tracking
2. **State thrashing:** Rapid state changes look glitchy, add minimum duration
3. **Frame desync:** Anim continues after state change, must Anim Freeze or set new sequence
4. **No transition frames:** Jarring jumps between animations, design smooth transitions
5. **Forgetting to reset state:** Jump animation plays forever if no completion check

## Extension Ideas

- Add attack animation that overrides movement
- Create damage flash animation with invulnerability period
- Sync sound effects to specific animation frames
- Multi-BOB composite characters (body + weapon + effects)
- Animation priority system (damage > attack > move > idle)

## Builds Toward

**In This Tier:**
- L20: Collision detection during animation
- L21: Complete animated sprite showcase

**In Next Tier:**
- Complex character controllers
- Enemy AI with animated states

## Quick Reference

### Animation State Pattern
```amos
' State machine structure
If state$="idle"
  Anim Freeze bob
End If

If state$="walk"
  Anim bob,"1,2,3,4",10
End If

If state$="jump"
  Anim bob,"5,6,7,8",15
  ' Check for completion
  If Bob Image(bob)=8 Then state$="idle"
End If
```

### Frame Detection
```amos
' Get current frame
frame=Bob Image(bob)

' Wait for specific frame
If Bob Image(bob)=4 Then
  ' Trigger event on frame 4
End If

' Detect animation completion
If Bob Image(bob)=lastFrame Then
  ' Sequence finished
End If
```

### Timer-Based States
```amos
' Enter timed state
state$="invincible"
stateTimer=100  ' 2 seconds at 50fps

' Each frame
Dec stateTimer
If stateTimer<=0 Then
  state$="normal"
End If
```

### Animation Priorities
```amos
' Priority system (higher = more important)
priority=0

If state$="idle" Then priority=1
If state$="walk" Then priority=2
If state$="jump" Then priority=3
If state$="hurt" Then priority=4

' Only change animation if priority increased
If newPriority>priority Then
  state$=newState$
  priority=newPriority
End If
```

### Composite Sprites
```amos
' Body BOB
Bob 1,x,y,bodyFrame

' Weapon BOB (follows body)
Bob 2,x+8,y+4,weaponFrame

' Both animated separately
Anim 1,"1,2,3,4",10      ' Body walk
Anim 2,"11,12,11,12",20  ' Weapon swing
```

### State Transitions
```amos
' Clean transition between states
Procedure ChangeState[newState$]
  ' Exit old state
  If state$="jump" Then jumpTimer=0
  If state$="attack" Then Anim Freeze 2  ' Stop weapon

  ' Enter new state
  state$=newState$
  If state$="jump" Then jumpTimer=30: Anim 1,"5,6,7,8",15
  If state$="attack" Then attackTimer=20: Anim 2,"11,12,13",20
End Proc
```

---

**Version:** 1.0
**Created:** 2025-10-27
