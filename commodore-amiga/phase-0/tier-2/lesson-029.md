# Lesson 029: Tile Collision

**Arc:** Platform Game
**Position:** Lesson 2 of 5 in arc
**Type:** Standard
**Estimated Completion:** 140 lines of code

## Learning Objectives

- Implement tile-based collision detection
- Create platform maps with 2D arrays
- Handle collision response (push-out)
- Optimize collision checks with spatial partitioning

## Prerequisites

**From Previous Lessons:**
- Gravity and jumping (L28)
- Fixed-point math (L22)

**AMOS Knowledge:**
- 2D arrays (Dim map(w,h))
- Point command for pixel checks (alternative method)

## Key Concepts Introduced

### Tile Grid
Level divided into grid (e.g., 16×16 pixel tiles). Map stored as 2D array where 0=empty, 1=solid. Easy to edit, memory-efficient.

### World-to-Tile Conversion
Player position (px,py) → tile coordinates (tx,ty) = (px/tileSize, py/tileSize). Check surrounding tiles for collisions.

### AABB Collision
Player is Axis-Aligned Bounding Box (rectangle). Check if overlaps solid tile. If yes, push player out of tile.

### Collision Order
Check horizontal movement first, then vertical. Prevents getting stuck in corners. Push-out moves player to nearest edge of colliding tile.

## Code Pattern

```amos
Screen Open 0,320,256,16,Lowres
Curs Off: Flash Off: Cls 0

' === TILE MAP ===
tileSize=16
mapWidth=20: mapHeight=16

' Map: 0=empty, 1=solid
Dim map(mapWidth,mapHeight)

' Create simple level
For Y=0 To mapHeight
  For X=0 To mapWidth
    ' Border walls
    If X=0 or X=mapWidth or Y=mapHeight
      map(X,Y)=1
    ' Platform
    Else If Y=12 and X>=5 and X<=15
      map(X,Y)=1
    ' Floating platform
    Else If Y=8 and X>=8 and X<=12
      map(X,Y)=1
    Else
      map(X,Y)=0
    End If
  Next X
Next Y

' Draw map
For Y=0 To mapHeight
  For X=0 To mapWidth
    If map(X,Y)=1
      Ink 7
      Bar X*tileSize,Y*tileSize To X*tileSize+tileSize-1,Y*tileSize+tileSize-1
    End If
  Next X
Next Y

' === PLAYER ===
Ink 2: Box 0,0 To 15,15
Get Bob 1,0,0 To 16,16
Cls 0

px#=80*256: py#=50*256
vx#=0: vy#=0
playerWidth=16: playerHeight=16

gravity#=24
jumpSpeed#=-800
terminalVel#=768
grounded=False

Do
  ' === INPUT ===
  If Jleft(1) Then Dec vx#,32
  If Jright(1) Then Add vx#,32

  ' Friction
  If Not Jleft(1) and Not Jright(1)
    If vx#>0 Then Dec vx#,16
    If vx#<0 Then Add vx#,16
  End If

  If vx#>512 Then vx#=512
  If vx#<-512 Then vx#=-512

  ' Jump
  If Fire(1) and grounded
    vy#=jumpSpeed#
    grounded=False
  End If

  ' === PHYSICS ===
  Add vy#,gravity#
  If vy#>terminalVel# Then vy#=terminalVel#

  ' === COLLISION: HORIZONTAL ===
  Add px#,vx#

  ' Check tiles at player's corners
  ' Top-left and bottom-left
  tx1=px#/256/tileSize
  tx2=(px#/256+playerWidth-1)/tileSize
  ty1=py#/256/tileSize
  ty2=(py#/256+playerHeight-1)/tileSize

  ' Check all tiles player overlaps
  hitX=False
  For ty=ty1 To ty2
    For tx=tx1 To tx2
      If tx>=0 and tx<=mapWidth and ty>=0 and ty<=mapHeight
        If map(tx,ty)=1
          hitX=True
          ' Push out
          If vx#>0  ' Moving right, hit left side of tile
            px#=tx*tileSize*256-playerWidth*256
          Else  ' Moving left, hit right side of tile
            px#=(tx+1)*tileSize*256
          End If
          vx#=0
          Exit  ' Stop checking after first hit
        End If
      End If
    Next tx
    If hitX Then Exit
  Next ty

  ' === COLLISION: VERTICAL ===
  Add py#,vy#

  ' Recalculate tile coordinates after vertical movement
  tx1=px#/256/tileSize
  tx2=(px#/256+playerWidth-1)/tileSize
  ty1=py#/256/tileSize
  ty2=(py#/256+playerHeight-1)/tileSize

  hitY=False
  grounded=False

  For ty=ty1 To ty2
    For tx=tx1 To tx2
      If tx>=0 and tx<=mapWidth and ty>=0 and ty<=mapHeight
        If map(tx,ty)=1
          hitY=True
          If vy#>0  ' Falling, hit top of tile
            py#=ty*tileSize*256-playerHeight*256
            grounded=True
          Else  ' Rising, hit bottom of tile
            py#=(ty+1)*tileSize*256
          End If
          vy#=0
          Exit
        End If
      End If
    Next tx
    If hitY Then Exit
  Next ty

  ' === RENDER ===
  Bob 1,px#/256,py#/256,1

  ' Debug
  Locate 0,0: Print "Tile: ";tx1;",";ty1;"  "
  Locate 0,1: Print "Grounded: ";grounded;"  "

  Wait Vbl
  Bob Update
Loop Until Inkey$<>""
```

## Hardware Interaction

**Chips Involved:**
- **CPU** - Tile collision math (~1-2ms per entity)
- **Blitter** - BOB and tile rendering

**Optimization:**
- Only check tiles near player (4-8 tiles typically)
- Early exit when collision found
- Spatial partitioning: divide world into regions

**Memory:**
- 20×16 map = 320 bytes (tiny!)
- Tile graphics: 16×16×4 bitplanes = 512 bytes per unique tile
- 16 unique tiles = 8KB total

## Common Pitfalls

1. **Checking all tiles every frame:** Wastes CPU, only check nearby tiles
2. **Wrong collision order:** Check X then Y, not both simultaneously
3. **Off-by-one errors:** playerWidth-1 for right edge, not playerWidth
4. **No push-out:** Player gets stuck inside tiles
5. **Floating-point division:** Use integer division (/) for tile coords

## Extension Ideas

- One-way platforms (can jump through from below)
- Slopes and ramps (requires sub-tile collision)
- Ladders and climbable tiles
- Breakable tiles (change map array on hit)
- Tile-based enemies (patrol platforms)

## Builds Toward

**In This Arc:**
- L30: Moving platforms (dynamic collision)
- L31: Level data and tile sets
- L32: Complete platform game

## Quick Reference

### World-to-Tile Conversion
```amos
' Player position → tile coords
tx = px / tileSize
ty = py / tileSize

' Get all tiles player overlaps
tx1 = px / tileSize                    ' Left
tx2 = (px + playerWidth - 1) / tileSize  ' Right
ty1 = py / tileSize                    ' Top
ty2 = (py + playerHeight - 1) / tileSize ' Bottom

' Check each tile
For ty = ty1 To ty2
  For tx = tx1 To tx2
    If map(tx,ty)=1 Then
      ' Collision!
    End If
  Next tx
Next ty
```

### Horizontal Collision Pattern
```amos
' Apply horizontal movement
Add px#, vx#

' Check tiles
For ty = ty1 To ty2
  For tx = tx1 To tx2
    If map(tx,ty) = 1
      ' Push out
      If vx# > 0  ' Moving right
        px# = tx * tileSize * 256 - playerWidth * 256
      Else  ' Moving left
        px# = (tx + 1) * tileSize * 256
      End If
      vx# = 0
      Exit  ' Stop after first hit
    End If
  Next tx
Next ty
```

### Vertical Collision Pattern
```amos
' Apply vertical movement
Add py#, vy#

' Check tiles (recalculate tx/ty after movement!)
For ty = ty1 To ty2
  For tx = tx1 To tx2
    If map(tx,ty) = 1
      If vy# > 0  ' Falling
        py# = ty * tileSize * 256 - playerHeight * 256
        grounded = True
      Else  ' Rising
        py# = (ty + 1) * tileSize * 256
      End If
      vy# = 0
      Exit
    End If
  Next tx
Next ty
```

### One-Way Platform
```amos
' Special tile type: 2 = one-way platform

' Only collide when falling AND coming from above
If map(tx,ty) = 2
  ' Check if player's bottom was above platform's top last frame
  If vy# > 0 and (py# - vy#) / 256 + playerHeight <= ty * tileSize
    ' Landing on platform
    py# = ty * tileSize * 256 - playerHeight * 256
    vy# = 0
    grounded = True
  End If
End If
```

### Spatial Partitioning Optimization
```amos
' Only check tiles in viewport + margin
cameraX = px / 256 - 160  ' Center camera on player
cameraY = py / 256 - 128

tileStartX = (cameraX - 32) / tileSize  ' 32px margin
tileEndX = (cameraX + 320 + 32) / tileSize
tileStartY = (cameraY - 32) / tileSize
tileEndY = (cameraY + 256 + 32) / tileSize

' Clamp to map bounds
If tileStartX < 0 Then tileStartX = 0
If tileEndX > mapWidth Then tileEndX = mapWidth
' ...same for Y

' Only check visible tiles
For ty = tileStartY To tileEndY
  For tx = tileStartX To tileEndX
    ' Collision check here
  Next tx
Next ty
```

### Tile Types
```
0 = Empty (air)
1 = Solid (wall, floor)
2 = One-way platform
3 = Ladder
4 = Hazard (spikes, lava)
5 = Breakable
6 = Collectible (coin, etc.)
```

---

**Version:** 1.0
**Created:** 2025-10-27
