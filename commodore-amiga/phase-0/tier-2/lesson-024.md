# Lesson 024: Bullet Hell Patterns

**Arc:** Arcade Action
**Position:** Lesson 3 of 6 in arc
**Type:** Standard
**Estimated Completion:** 140 lines of code

## Learning Objectives

- Create arcade bullet spray patterns
- Use trigonometry for circular patterns
- Manage large numbers of projectiles
- Implement bullet lifetime and recycling

## Prerequisites

**From Previous Lessons:**
- Fast BOB movement and fixed-point (L22)
- Blitter optimization and sprite pools (L23)

**AMOS Knowledge:**
- Sin/Cos functions for angles
- Degree/radian conversion (360° = 2π radians)

## Key Concepts Introduced

### Circular Bullet Patterns
Use Sin/Cos to calculate velocity components for bullets fired in all directions. `vx = speed × Cos(angle)`, `vy = speed × Sin(angle)`.

### Pattern Types
- **Radial:** Bullets spread outward in circle (boss attacks)
- **Spiral:** Angle increments each frame (rotating spray)
- **Aimed:** Calculate angle toward player position
- **Wave:** Sinusoidal path (weaving bullets)

### Angle Math
AMOS Sin/Cos use degrees (0-360°). For full circle spray: angle += 360/bulletCount. For spiral: angle += rotationSpeed each frame.

### Bullet Lifetime
Track age in frames. Auto-deactivate old bullets prevents off-screen bullets consuming resources forever.

## Code Pattern

```amos
Screen Open 0,320,256,32,Lowres
Curs Off: Flash Off: Cls 0

' Create bullet sprite
Ink 3
Bar 0,0 To 3,3
Get Bob 1,0,0 To 4,4
Cls 0

' Bullet pool
maxBullets=100
Dim active(maxBullets)
Dim bx#(maxBullets),by#(maxBullets)
Dim bvx#(maxBullets),bvy#(maxBullets)
Dim bage(maxBullets)  ' Age in frames

' Initialize pool
For I=1 To maxBullets
  Bob I,-100,-100,1
  Bob Off I
  active(I)=0
Next I

' Enemy position (bullet source)
ex=160: ey=64

' Pattern state
patternAngle=0
fireTimer=0

' Player
px=160: py=200

Do
  ' Player movement
  If Jleft(1) Then Dec px,3
  If Jright(1) Then Add px,3
  If Jup(1) Then Dec py,3
  If Jdown(1) Then Add py,3

  ' Fire pattern every 20 frames
  Inc fireTimer
  If fireTimer>=20
    fireTimer=0

    ' Choose pattern
    If Inkey$="1" Then FireRadial[ex,ey,8,3*256]
    If Inkey$="2" Then FireSpiral[ex,ey,patternAngle,3*256]
    If Inkey$="3" Then FireAimed[ex,ey,px,py,4*256]

    patternAngle+=15  ' Rotate spiral
    If patternAngle>=360 Then patternAngle=0
  End If

  ' Update bullets
  For I=1 To maxBullets
    If active(I)=1
      ' Move
      Add bx#(I),bvx#(I)
      Add by#(I),bvy#(I)

      ' Age
      Inc bage(I)

      ' Deactivate if old or off-screen
      x=bx#(I)/256: y=by#(I)/256
      If bage(I)>200 or x<-16 or x>336 or y<-16 or y>272
        active(I)=0
        Bob Off I
      Else
        Bob I,x,y,1
        Bob On I
      End If
    End If
  Next I

  ' Display
  Locate 0,0: Print "1=Radial 2=Spiral 3=Aimed"
  Ink 2
  Box ex-8,ey-8 To ex+8,ey+8  ' Enemy

  Wait Vbl
  Bob Update
  Cls 0
Loop Until Inkey$=Chr$(27)

' ================================================
' BULLET PATTERNS
' ================================================

Procedure FireRadial[ox,oy,count,speed#]
  ' Spray bullets in circle
  angleStep=360/count
  For A=0 To 359 Step angleStep
    SpawnBullet[ox,oy,speed#*Cos(A),speed#*Sin(A)]
  Next A
End Proc

Procedure FireSpiral[ox,oy,startAngle,speed#]
  ' Rotating spray
  For A=startAngle To startAngle+360 Step 45
    SpawnBullet[ox,oy,speed#*Cos(A),speed#*Sin(A)]
  Next A
End Proc

Procedure FireAimed[ox,oy,tx,ty,speed#]
  ' Aimed at target
  dx=tx-ox: dy=ty-oy
  dist=Sqr(dx*dx+dy*dy)
  If dist>0
    vx#=speed#*dx/dist
    vy#=speed#*dy/dist
    SpawnBullet[ox,oy,vx#,vy#]
  End If
End Proc

Procedure SpawnBullet[ox,oy,vx#,vy#]
  ' Find inactive bullet
  For I=1 To maxBullets
    If active(I)=0
      active(I)=1
      bx#(I)=ox*256
      by#(I)=oy*256
      bvx#(I)=vx#
      bvy#(I)=vy#
      bage(I)=0
      Exit
    End If
  Next I
End Proc
```

## Hardware Interaction

**Chips Involved:**
- **CPU** - Sin/Cos math, bullet logic (~2ms per 100 bullets)
- **Blitter** - Renders active bullets (~0.02ms per 4×4 bullet)
- **Paula** - Sound effect on bullet spawn (Sam Play)

**Performance:**
- Small 4×4 bullets = 8 bytes each
- 100 active bullets = 800 bytes copied by Blitter
- At 50fps: 40KB/s (very manageable)
- Sin/Cos are fast (lookup table in AMOS ROM)

## Common Pitfalls

1. **No bullet lifetime:** Off-screen bullets stay active forever
2. **Expensive distance calc every frame:** Use age instead when possible
3. **Division by zero:** Check dist>0 before normalizing aim vector
4. **Angle overflow:** patternAngle can grow unbounded, wrap at 360°
5. **Too many bullets:** Exceeding pool size silently fails, no new bullets

## Extension Ideas

- Homing bullets (recalculate aim each frame)
- Bullet waves (sinusoidal paths: y += Sin(frameCount) )
- Multi-stage bullets (change velocity after N frames)
- Gravity-affected bullets (Add vy#,gravity each frame)
- Bullet types with different sprites and behaviors

## Builds Toward

**In This Arc:**
- L25: Enemy wave patterns combining movement + bullets
- L27: Complete shooter with varied attacks

## Quick Reference

### Radial Pattern (Circle Spray)
```amos
Procedure FireRadial[ox,oy,bulletCount,speed#]
  angleStep=360/bulletCount
  For angle=0 To 359 Step angleStep
    vx#=speed#*Cos(angle)
    vy#=speed#*Sin(angle)
    SpawnBullet[ox,oy,vx#,vy#]
  Next angle
End Proc
```

### Spiral Pattern (Rotating)
```amos
' Global: spiralAngle=0

Procedure FireSpiral[ox,oy,armCount,speed#]
  angleStep=360/armCount
  For I=0 To armCount-1
    angle=spiralAngle+I*angleStep
    vx#=speed#*Cos(angle)
    vy#=speed#*Sin(angle)
    SpawnBullet[ox,oy,vx#,vy#]
  Next I
  Add spiralAngle,10  ' Rotation speed
  If spiralAngle>=360 Then spiralAngle=0
End Proc
```

### Aimed Pattern (At Player)
```amos
Procedure FireAimed[ox,oy,targetX,targetY,speed#]
  dx=targetX-ox
  dy=targetY-oy
  dist=Sqr(dx*dx+dy*dy)
  If dist>0
    vx#=speed#*dx/dist
    vy#=speed#*dy/dist
    SpawnBullet[ox,oy,vx#,vy#]
  End If
End Proc
```

### Wave Pattern (Sinusoidal)
```amos
' In bullet update loop
If waveType(I)=1
  ' Horizontal wave
  Add bvy#(I),32*Sin(bage(I)*10)  ' Oscillate Y velocity
End If
```

### Homing Pattern
```amos
' In bullet update loop
If homing(I)=1
  ' Recalculate aim toward player
  dx=px-bx#(I)/256
  dy=py-by#(I)/256
  dist=Sqr(dx*dx+dy*dy)
  If dist>0
    turnSpeed#=16  ' How fast bullet turns
    bvx#(I)=bvx#(I)*7/8 + (turnSpeed#*dx/dist)
    bvy#(I)=bvy#(I)*7/8 + (turnSpeed#*dy/dist)
  End If
End If
```

### Lifetime Management
```amos
' Spawn
bage(I)=0
lifetime(I)=100  ' 2 seconds @50fps

' Update
Inc bage(I)
If bage(I)>lifetime(I)
  active(I)=0
  Bob Off I
End If
```

### Velocity from Angle/Speed
```amos
' Angle in degrees, speed in fixed-point (×256)
angle=45
speed#=512  ' 2 pixels/frame

vx#=speed#*Cos(angle)
vy#=speed#*Sin(angle)

' Result: vx# ≈ 362 (√2/2 * 512)
'         vy# ≈ 362
```

---

**Version:** 1.0
**Created:** 2025-10-27
