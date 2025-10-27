# Lesson 028: Gravity and Jumping

**Arc:** Platform Game
**Position:** Lesson 1 of 5 in arc
**Type:** Standard
**Estimated Completion:** 80 lines of code

## Learning Objectives

- Implement gravity physics
- Create responsive jump mechanics
- Understand terminal velocity
- Handle grounded state detection

## Prerequisites

**From Previous Arcs:**
- Fast BOB movement and velocity (L22)
- Animation states (L19)

**AMOS Knowledge:**
- Bob positioning
- Fixed-point math
- State machines

## Key Concepts Introduced

### Gravity Constant
Each frame, add downward velocity (e.g., `Add vy#,gravity#`). Typical values: 16-32 (0.0625-0.125 pixels/frame²). Feels natural, not floaty.

### Jump Input
On button press, set upward velocity (e.g., `vy#=-800` = -3.125 pixels/frame). Gravity brings player back down naturally.

### Terminal Velocity
Clamp downward speed to prevent infinite acceleration. Typical max fall speed: 512-768 (2-3 pixels/frame).

### Grounded Detection
Track whether player is on floor. Only allow jump when grounded. Reset vertical velocity to zero when landing.

## Code Pattern

```amos
Screen Open 0,320,256,16,Lowres
Curs Off: Flash Off: Cls 0

' Create player sprite
Ink 2: Bar 0,0 To 15,15
Get Bob 1,0,0 To 16,16: Cls 0

' Draw ground platform
Ink 7: Bar 0,200 To 320,256

' Player physics
px#=160*256: py#=100*256
vx#=0: vy#=0

' Physics constants (all fixed-point)
gravity#=24          ' 0.09375 pixels/frame²
jumpSpeed#=-800      ' -3.125 pixels/frame
terminalVel#=768     ' 3 pixels/frame max fall
groundY#=184*256     ' Ground level (200-16 for sprite height)

grounded=False
canJump=True

Do
  ' === INPUT ===
  ' Horizontal movement
  If Jleft(1) Then Dec vx#,32
  If Jright(1) Then Add vx#,32

  ' Friction when no input
  If Not Jleft(1) and Not Jright(1)
    If vx#>0 Then Dec vx#,16
    If vx#<0 Then Add vx#,16
  End If

  ' Clamp horizontal speed
  If vx#>512 Then vx#=512
  If vx#<-512 Then vx#=-512

  ' Jump input (only when grounded)
  If Fire(1) and grounded and canJump
    vy#=jumpSpeed#
    grounded=False
    canJump=False  ' Prevent double-jump
  End If

  ' Release jump button = can jump again when landing
  If Not Fire(1) Then canJump=True

  ' === PHYSICS ===
  ' Apply gravity (only when airborne)
  If Not grounded
    Add vy#,gravity#
    ' Terminal velocity
    If vy#>terminalVel# Then vy#=terminalVel#
  End If

  ' Apply velocity
  Add px#,vx#
  Add py#,vy#

  ' === COLLISION ===
  ' Boundary check
  If px#<0 Then px#=0: vx#=0
  If px#>304*256 Then px#=304*256: vx#=0

  ' Ground collision
  If py#>=groundY#
    py#=groundY#
    vy#=0
    grounded=True
  Else
    grounded=False
  End If

  ' === RENDER ===
  Bob 1,px#/256,py#/256,1

  ' Debug display
  Locate 0,0: Print "Grounded: ";grounded;"  "
  Locate 0,1: Print "VY: ";vy#/256;"    "

  Wait Vbl
  Bob Update
  Cls 0
Loop Until Inkey$<>""
```

## Hardware Interaction

**Chips Involved:**
- **CPU** - Physics calculations (~0.5ms per entity)
- **Blitter** - BOB rendering

**Fixed-Point Precision:**
- Gravity 24 = 0.09375 pixels/frame² (smooth acceleration)
- Jump -800 = -3.125 pixels/frame (feels snappy)
- Terminal 768 = 3 pixels/frame (fast enough, not blurry)

**Performance:**
- Physics for 1 player: ~0.1ms
- Physics for 20 entities: ~2ms
- Plenty of CPU headroom for more game logic

## Common Pitfalls

1. **No terminal velocity:** Player accelerates infinitely, falls through floor
2. **Gravity too strong:** Feels like moon gravity, floaty jumps
3. **Jump while airborne:** Double-jump without intending to
4. **Integer-only math:** Gravity rounds to zero, player doesn't fall
5. **No grounded check:** Can jump in mid-air

## Extension Ideas

- Variable jump height (release button early = shorter jump)
- Coyote time (can jump briefly after leaving platform)
- Jump buffering (press jump slightly before landing)
- Wall jump mechanics
- Double jump power-up

## Builds Toward

**In This Arc:**
- L29: Tile collision for platforms
- L30: Moving platforms and hazards
- L31: Level data structures
- L32: Complete platform game

## Quick Reference

### Gravity Pattern
```amos
' Constants
gravity#=24          ' Acceleration downward
terminalVel#=768     ' Max fall speed

' Each frame (when airborne)
If Not grounded
  Add vy#,gravity#
  If vy#>terminalVel# Then vy#=terminalVel#
End If

Add py#,vy#
```

### Jump Input
```amos
' Jump only when grounded
If Fire(1) and grounded and canJump
  vy#=jumpSpeed#       ' Set upward velocity
  grounded=False       ' Now airborne
  canJump=False        ' Prevent re-trigger
End If

' Allow re-jump when button released
If Not Fire(1) Then canJump=True
```

### Ground Detection
```amos
' Simple: fixed Y coordinate
groundY#=200*256
If py#>=groundY#
  py#=groundY#  ' Snap to ground
  vy#=0         ' Stop falling
  grounded=True
Else
  grounded=False
End If
```

### Variable Jump Height
```amos
' Jump starts same as before
If Fire(1) and grounded
  vy#=jumpSpeed#
  jumping=True
End If

' Each frame: if released early, reduce upward velocity
If jumping and Not Fire(1) and vy#<0
  vy#=vy#/2  ' Cut jump short
  jumping=False
End If

' Still apply gravity
Add vy#,gravity#
```

### Coyote Time (Forgiving Jump)
```amos
' Track time since left ground
Dim coyoteTimer

' When leaving ground (not from jump)
If Not grounded and vy#>=0
  coyoteTimer=8  ' 8 frames grace period
End If

' Each frame
If coyoteTimer>0 Then Dec coyoteTimer

' Allow jump if recently grounded
If Fire(1) and(grounded or coyoteTimer>0)
  vy#=jumpSpeed#
  coyoteTimer=0  ' Consume grace period
End If
```

### Jump Buffer
```amos
' Buffer early jump input
jumpBuffer=0

' Press jump anytime
If Fire(1) Then jumpBuffer=10  ' 10-frame buffer

' Each frame
If jumpBuffer>0 Then Dec jumpBuffer

' Execute jump when landing
If grounded and jumpBuffer>0
  vy#=jumpSpeed#
  jumpBuffer=0
End If
```

### Typical Physics Values
```
Gravity:        16-32   (0.06-0.12 px/frame²)
Jump Speed:     -600 to -1000  (-2.3 to -3.9 px/frame)
Terminal Vel:   512-1024  (2-4 px/frame)
Ground Y:       Variable per level

Feels:
- Low gravity (16): Floaty, moon-like
- Medium (24): Balanced, Mario-esque
- High (32): Heavy, fast-paced
```

---

**Version:** 1.0
**Created:** 2025-10-27
