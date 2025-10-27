# Lesson 030: Moving Platforms & Hazards

**Arc:** Platform Game
**Position:** Lesson 3 of 5 in arc
**Type:** Standard
**Estimated Completion:** 160 lines of code

## Learning Objectives

- Create moving platforms with predictable patterns
- Implement player-on-platform physics
- Add hazards with collision response
- Manage dynamic entity collision

## Prerequisites

**From Previous Lessons:**
- Gravity and jumping (L28)
- Tile collision (L29)
- AMAL movement (L17) or manual patterns

**AMOS Knowledge:**
- Entity management arrays
- Collision detection with Col function

## Key Concepts Introduced

### Platform Movement Patterns
Platforms follow paths: horizontal slide, vertical lift, circular orbit, pendulum swing. Use Sin/Cos or AMAL for smooth motion.

### Rider Physics
When player stands on moving platform, inherit platform's velocity. Player moves with platform automatically.

### Hazard Types
Instant-death hazards (spikes, pits) vs. damage hazards (fire, enemies). Different collision responses (game over vs. knockback + invulnerability).

### Entity Layers
Platforms behind player, hazards in front. Use Bob Priority for correct Z-order.

## Code Pattern

```amos
Screen Open 0,320,256,16,Lowres
Curs Off: Flash Off: Cls 0

' === SPRITES ===
' Player
Ink 2: Bar 0,0 To 15,15: Get Bob 1,0,0 To 16,16: Cls 0

' Platform (32×8)
Ink 7: Bar 0,0 To 31,7: Get Bob 2,0,0 To 32,8: Cls 0

' Hazard (spike)
Ink 4: Bar 0,0 To 15,7: Get Bob 3,0,0 To 16,8: Cls 0

' === PLATFORMS ===
maxPlatforms=5
Dim plat#(maxPlatforms,6)  ' [id]: x#, y#, vx#, vy#, type, time

' Platform types: 1=horizontal, 2=vertical, 3=circle
' Type 1: Horizontal slider
plat#(1,0)=100*256: plat#(1,1)=150*256  ' Start position
plat#(1,2)=128: plat#(1,3)=0            ' Velocity (0.5 px/frame right)
plat#(1,4)=1: plat#(1,5)=0              ' Type=horizontal, timer

' Type 2: Vertical lift
plat#(2,0)=200*256: plat#(2,1)=180*256
plat#(2,2)=0: plat#(2,3)=-64            ' Moving up
plat#(2,4)=2: plat#(2,5)=0

' Type 3: Circular orbit
plat#(3,0)=160*256: plat#(3,1)=120*256  ' Center point
plat#(3,2)=0: plat#(3,3)=0
plat#(3,4)=3: plat#(3,5)=0

For I=1 To maxPlatforms
  Bob I+10,-100,-100,2
  Bob Priority I+10,5  ' Behind player
  If plat#(I,4)>0 Then Bob On I+10
Next I

' === HAZARDS ===
maxHazards=3
Dim hazX(maxHazards),hazY(maxHazards),hazActive(maxHazards)

hazX(1)=150: hazY(1)=200: hazActive(1)=1
hazX(2)=200: hazY(2)=200: hazActive(2)=1

For I=1 To maxHazards
  Bob I+50,-100,-100,3
  Bob Priority I+50,15  ' In front of player
  If hazActive(I)=1 Then Bob On I+50
Next I

' === PLAYER ===
px#=80*256: py#=50*256
vx#=0: vy#=0
playerWidth=16: playerHeight=16

gravity#=24
jumpSpeed#=-800
terminalVel#=768
grounded=False
onPlatform=-1  ' Platform ID player is standing on (-1=none)

playerHp=3
invincible=0

' Draw ground
Ink 7: Bar 0,220 To 320,256

Do
  ' === INPUT ===
  If Jleft(1) Then Dec vx#,32
  If Jright(1) Then Add vx#,32

  If Not Jleft(1) and Not Jright(1)
    If vx#>0 Then Dec vx#,16
    If vx#<0 Then Add vx#,16
  End If

  If vx#>512 Then vx#=512
  If vx#<-512 Then vx#=-512

  If Fire(1) and grounded
    vy#=jumpSpeed#
    grounded=False
    onPlatform=-1
  End If

  ' === PLATFORM UPDATE ===
  For I=1 To maxPlatforms
    If plat#(I,4)>0  ' Active platform
      ptype=plat#(I,4)
      Inc plat#(I,5)  ' Increment timer

      If ptype=1  ' Horizontal slider
        Add plat#(I,0),plat#(I,2)
        ' Bounce at edges
        If plat#(I,0)<80*256 or plat#(I,0)>220*256
          plat#(I,2)=-plat#(I,2)
        End If
      End If

      If ptype=2  ' Vertical lift
        Add plat#(I,1),plat#(I,3)
        ' Bounce at edges
        If plat#(I,1)<100*256 or plat#(I,1)>200*256
          plat#(I,3)=-plat#(I,3)
        End If
      End If

      If ptype=3  ' Circular orbit
        angle=plat#(I,5)*2  ' Rotation speed
        plat#(I,0)=(160+60*Cos(angle))*256
        plat#(I,1)=(120+40*Sin(angle))*256
      End If
    End If
  Next I

  ' === PHYSICS ===
  Add vy#,gravity#
  If vy#>terminalVel# Then vy#=terminalVel#

  ' === HORIZONTAL MOVEMENT ===
  Add px#,vx#

  ' Boundary check
  If px#<0 Then px#=0: vx#=0
  If px#>304*256 Then px#=304*256: vx#=0

  ' === VERTICAL MOVEMENT ===
  Add py#,vy#

  ' Ground collision
  grounded=False
  onPlatform=-1

  If py#>=204*256  ' Ground level (220-16)
    py#=204*256
    vy#=0
    grounded=True
  End If

  ' === PLATFORM COLLISION ===
  For I=1 To maxPlatforms
    If plat#(I,4)>0
      px=px#/256: py=py#/256
      platX=plat#(I,0)/256: platY=plat#(I,1)/256
      platW=32: platH=8

      ' Check if player's bottom is on platform's top
      If vy#>=0  ' Falling or standing
        If px+playerWidth > platX and px < platX+platW
          If py+playerHeight >= platY and py+playerHeight <= platY+platH+4
            ' Landing on platform
            py#=platY*256-playerHeight*256
            vy#=0
            grounded=True
            onPlatform=I

            ' Inherit platform velocity for types 1 and 2
            If plat#(I,4)=1  ' Horizontal
              px#=px#+plat#(I,2)
            End If

            If plat#(I,4)=2  ' Vertical
              py#=py#+plat#(I,3)
            End If

            Exit
          End If
        End If
      End If
    End If
  Next I

  ' === HAZARD COLLISION ===
  If invincible=0
    For I=1 To maxHazards
      If hazActive(I)=1
        px=px#/256: py=py#/256

        ' Simple box collision
        If px+playerWidth > hazX(I) and px < hazX(I)+16
          If py+playerHeight > hazY(I) and py < hazY(I)+8
            ' Hit hazard!
            Dec playerHp
            invincible=100  ' 2 seconds
            ' Knockback
            vy#=-400
            If px < hazX(I) Then vx#=-256 Else vx#=256
            If playerHp<=0 Then Exit  ' Game over
          End If
        End If
      End If
    Next I
  Else
    Dec invincible
  End If

  ' === RENDER ===
  ' Platforms
  For I=1 To maxPlatforms
    If plat#(I,4)>0
      Bob I+10,plat#(I,0)/256,plat#(I,1)/256,2
    End If
  Next I

  ' Hazards
  For I=1 To maxHazards
    If hazActive(I)=1
      Bob I+50,hazX(I),hazY(I),3
    End If
  Next I

  ' Player (flash when invincible)
  If invincible>0 and(invincible Mod 8)<4
    Bob Off 1
  Else
    Bob 1,px#/256,py#/256,1
    Bob On 1
  End If

  ' UI
  Locate 0,0: Print "HP: ";playerHp;"  Platform: ";onPlatform;"  "

  Wait Vbl
  Bob Update
Loop Until Inkey$<>"" or playerHp<=0
```

## Hardware Interaction

**Chips Involved:**
- **CPU** - Platform motion, rider physics, collision (~3-4ms)
- **Blitter** - Rendering platforms, player, hazards

**Performance:**
- 5 moving platforms: ~1ms
- 10 hazards: ~0.5ms
- Plenty of CPU for more entities

## Common Pitfalls

1. **Player slides off moving platform:** Forgetting to add platform velocity
2. **Jittery platform riding:** Adding velocity every frame (should only when standing)
3. **No hazard invulnerability:** Taking damage every frame = instant death
4. **Platform collision too strict:** 1-pixel tolerance helps (platY+platH+4)
5. **Circular platforms teleport:** Needs interpolation or smaller time step

## Extension Ideas

- Crumbling platforms (break after N seconds of standing)
- Springboards (launch player upward)
- Conveyor belts (force horizontal velocity)
- Rotating platforms (change player orientation)
- Crushing hazards (moving walls)

## Builds Toward

**In This Arc:**
- L31: Level data and tile graphics
- L32: Complete platform game synthesis

## Quick Reference

### Moving Platform Pattern
```amos
' Horizontal slider
Add platX#, platVX#
If platX# < minX# or platX# > maxX# Then
  platVX# = -platVX#  ' Reverse direction
End If

' Vertical lift
Add platY#, platVY#
If platY# < minY# or platY# > maxY# Then
  platVY# = -platVY#
End If

' Circular orbit
angle = time * rotationSpeed
platX# = (centerX + radius * Cos(angle)) * 256
platY# = (centerY + radius * Sin(angle)) * 256
```

### Rider Physics
```amos
' Check if player is ON platform
onPlatform = -1

For I = 1 To maxPlatforms
  If vy# >= 0  ' Falling or standing
    If px + playerWidth > platX and px < platX + platW
      If py + playerHeight >= platY and py + playerHeight <= platY + platH + 4
        ' Standing on platform
        py# = platY * 256 - playerHeight * 256
        vy# = 0
        grounded = True
        onPlatform = I

        ' Inherit platform velocity
        Add px#, platVX#(I)
        Add py#, platVY#(I)

        Exit
      End If
    End If
  End If
Next I
```

### Hazard Collision with Knockback
```amos
If invincible = 0
  ' Check hazard collision
  If BoxCollision(player, hazard)
    Dec playerHp
    invincible = 100

    ' Knockback away from hazard
    If px < hazX Then
      vx# = -256  ' Push left
    Else
      vx# = 256   ' Push right
    End If
    vy# = -400  ' Pop up

    If playerHp <= 0 Then
      ' Game over
    End If
  End If
Else
  Dec invincible
End If
```

### One-Way Platform (Can Jump Through)
```amos
' Only collide when coming from above AND falling
If vy# > 0  ' Falling
  If (py# - vy#) / 256 + playerHeight <= platY  ' Was above last frame
    If px + playerWidth > platX and px < platX + platW
      ' Land on platform
      py# = platY * 256 - playerHeight * 256
      vy# = 0
      grounded = True
    End If
  End If
End If
```

### Crumbling Platform
```amos
' Per-platform state
Dim platCrumbleTimer(maxPlatforms)

' When player stands on platform
If onPlatform = I
  Inc platCrumbleTimer(I)
  If platCrumbleTimer(I) > 50  ' 1 second
    ' Platform crumbles
    plat#(I,4) = 0  ' Deactivate
    Bob Off I+10
    grounded = False  ' Player falls
  End If
Else
  ' Reset timer when not standing
  platCrumbleTimer(I) = 0
End If
```

### Conveyor Belt Platform
```amos
' Platform has direction: -1 (left), +1 (right)
conveyorSpeed# = 64

If onPlatform = I
  ' Force player to move with belt
  Add px#, conveyorSpeed# * conveyorDir(I)
End If
```

---

**Version:** 1.0
**Created:** 2025-10-27
