# Lesson 022: Fast BOB Movement

**Arc:** Arcade Action
**Position:** Lesson 1 of 6 in arc
**Type:** Standard
**Estimated Completion:** 80 lines of code

## Learning Objectives

- Achieve fast, smooth sprite movement
- Understand Blitter performance limits
- Implement velocity-based physics
- Use fixed-point math for sub-pixel precision

## Prerequisites

**From Previous Arc:**
- All Animation System concepts (L17-21)

**From Tier 1:**
- BOB movement fundamentals (L12)
- Bob Update synchronization

**AMOS Knowledge:**
- Bob command positioning
- Wait Vbl timing

## Key Concepts Introduced

### Velocity-Based Movement
Instead of moving sprites by fixed amount each frame (Add x,2), store velocity (vx) and apply it (Add x,vx). Allows smooth acceleration, deceleration, and variable speeds.

### Fixed-Point Math
Amiga BASIC uses integers for BOB positions. For smooth slow movement (less than 1 pixel/frame), use fixed-point: store position × 256, then Bob x/256,y/256,image.

### Blitter Performance
The Blitter can move ~8-12 full-screen 32×32 BOBs at 50fps. Smaller BOBs, simple backgrounds, and Bob Off for off-screen sprites improve performance.

### Frame Independence
Game logic shouldn't assume 50fps. Use Timer or frame counters for time-based events, not hardcoded loop counts.

## Code Pattern

```amos
Screen Open 0,320,256,32,Lowres
Curs Off: Flash Off: Cls 0

' Create sprite
Ink 2
Bar 0,0 To 15,15
Get Bob 1,0,0 To 16,16
Cls 0

' Position with fixed-point (×256 for sub-pixel)
px#=160*256  ' Real position
py#=128*256
vx#=0        ' Velocity
vy#=0

' Physics constants
accel#=32    ' Acceleration per frame (32/256 = 0.125 pixels/frame²)
maxSpeed#=512  ' Max velocity (512/256 = 2 pixels/frame)
friction#=8  ' Deceleration (8/256 = 0.03125)

' Main loop
Do
  ' Input
  If Jleft(1) Then Dec vx#,accel#
  If Jright(1) Then Add vx#,accel#
  If Jup(1) Then Dec vy#,accel#
  If Jdown(1) Then Add vy#,accel#

  ' Apply friction when no input
  If Not Jleft(1) and Not Jright(1)
    If vx#>0 Then Dec vx#,friction#
    If vx#<0 Then Add vx#,friction#
  End If

  If Not Jup(1) and Not Jdown(1)
    If vy#>0 Then Dec vy#,friction#
    If vy#<0 Then Add vy#,friction#
  End If

  ' Clamp velocity
  If vx#>maxSpeed# Then vx#=maxSpeed#
  If vx#<-maxSpeed# Then vx#=-maxSpeed#
  If vy#>maxSpeed# Then vy#=maxSpeed#
  If vy#<-maxSpeed# Then vy#=-maxSpeed#

  ' Apply velocity
  Add px#,vx#
  Add py#,vy#

  ' Boundary check
  If px#<0 Then px#=0: vx#=0
  If px#>304*256 Then px#=304*256: vx#=0
  If py#<0 Then py#=0: vy#=0
  If py#>240*256 Then py#=240*256: vy#=0

  ' Render (convert fixed-point to int)
  Bob 1,px#/256,py#/256,1
  Wait Vbl
  Bob Update
Loop Until Inkey$<>""
```

## Hardware Interaction

**Chips Involved:**
- **Blitter** - Copies sprite data to screen each frame
- **CPU** - Calculates physics (6809 @ 7.14 MHz)
- **Agnus** - DMA arbitration for Blitter access

**Performance Factors:**
- **BOB Size:** 16×16 = 4× faster than 32×32
- **Colour Depth:** 4 bitplanes (16 colours) = 2× faster than 32 colours
- **Background:** Static = faster than animated
- **BOB Count:** Each BOB adds ~2-3ms Blitter time

**Optimization:**
- Bob Off for off-screen sprites (saves Blitter cycles)
- Use Bob priority to reduce overdraw
- Smaller sprites for bullets/particles
- Fixed-point math done in CPU (Blitter only copies pixels)

## Common Pitfalls

1. **Integer-only math:** Moving by 1 pixel/frame is too fast, but 0 doesn't move
2. **No velocity clamping:** Speed increases infinitely
3. **Harsh stops:** No friction = feels unresponsive
4. **Boundary collision stops movement:** vx should zero on wall hit
5. **Fixed-point overflow:** Very large px# values (>32767*256) cause errors

## Extension Ideas

- Momentum-based turning (can't instantly change direction at full speed)
- Dash mechanic (temporary speed boost)
- Bullet spray patterns with varied velocities
- Smooth camera following with fixed-point
- Wrap-around screen edges (Asteroids-style)

## Builds Toward

**In This Arc:**
- L23: Blitter optimization techniques
- L24: Bullet management systems
- L25: Enemy wave patterns
- L26: Scrolling backgrounds
- L27: Space shooter synthesis

## Quick Reference

### Fixed-Point Math
```amos
' Setup: multiply by 256
px#=100*256  ' Real position
vx#=128      ' Velocity (128/256 = 0.5 pixels/frame)

' Each frame: add velocity
Add px#,vx#

' Render: divide by 256
Bob 1,px#/256,py#/256,1
```

### Velocity Pattern
```amos
' Constants
accel#=32
maxSpeed#=512
friction#=8

' Input → acceleration
If Jleft(1) Then Dec vx#,accel#

' Clamp speed
If vx#>maxSpeed# Then vx#=maxSpeed#

' Friction when no input
If Not Jleft(1) and Not Jright(1)
  If vx#>0 Then Dec vx#,friction#
  If vx#<0 Then Add vx#,friction#
End If

' Apply velocity
Add px#,vx#
```

### Boundary Collision
```amos
' Stop at walls
If px#<0 Then
  px#=0     ' Clamp position
  vx#=0     ' Zero velocity
End If

' Bounce at walls
If px#<0 Then
  px#=0
  vx#=-vx#*8/10  ' Reverse with 80% energy
End If

' Wrap at edges
If px#<0 Then px#=320*256
If px#>320*256 Then px#=0
```

### Performance Check
```amos
' Measure frame time
startTime=Timer
' ... game loop ...
frameTime=Timer-startTime

' Display FPS
Locate 0,0: Print "Frame: ";frameTime;" ticks"
' 1 tick @50Hz = 20ms, 2 ticks = 40ms (too slow!)
```

### Diagonal Speed Fix
```amos
' Problem: moving diagonally is √2 faster
' Solution: normalize velocity

' After input, before clamping
If vx#<>0 and vy#<>0
  ' Diagonal = multiply by 0.707 (181/256)
  vx#=vx#*181/256
  vy#=vy#*181/256
End If
```

---

**Version:** 1.0
**Created:** 2025-10-27
