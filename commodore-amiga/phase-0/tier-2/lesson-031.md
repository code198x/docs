# Lesson 031: Level Data & Loading

**Arc:** Platform Game
**Position:** Lesson 4 of 5 in arc
**Type:** Standard
**Estimated Completion:** 120 lines of code

## Learning Objectives

- Organize level data in structured format
- Load levels from DATA statements or files
- Create tile sets with multiple graphics
- Implement level transitions

## Prerequisites

**From Previous Lessons:**
- Tile collision (L29)
- Moving platforms (L30)

**AMOS Knowledge:**
- READ and DATA statements
- Screen Copy for tile rendering
- Load/Save commands (optional)

## Key Concepts Introduced

### Level Data Format
Store maps as compact DATA: tile indices, platform positions, enemy spawns, collectibles. Each level is self-contained structure.

### Tile Sets
Graphics bank with multiple tile types (grass, stone, metal, water). Map array stores tile ID, rendering looks up graphic from bank.

### Level Loader
Procedure that reads level data, builds map array, spawns entities. Can load from DATA statements (simple) or external files (advanced).

### Level Transitions
When player reaches exit, save progress, load next level. Smooth transition with fade or wipe effect.

## Code Pattern

```amos
Screen Open 0,320,256,16,Lowres
Curs Off: Flash Off: Cls 0

' === TILE SET ===
tileSize=16
maxTileTypes=8

' Create tile graphics (0=empty, 1-7=solid variations)
Screen 1  ' Temp screen for drawing
For T=1 To maxTileTypes-1
  Ink T+1
  Bar 0,0 To tileSize-1,tileSize-1
  Get Bob T,0,0 To tileSize,tileSize
Next T
Screen 0

' === LEVEL DATA ===
' Format: width, height, then tiles row-by-row
' Then: platform count, [x,y,vx,vy,type] per platform
' Then: hazard count, [x,y] per hazard
' Then: spawn point x,y
' Then: exit point x,y

currentLevel=1

' === LEVEL 1 DATA ===
' 20×16 map, simplified for clarity
Data 20,16
' Row 0 (top)
Data 1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1
' Rows 1-14 (mostly empty, some platforms)
Data 1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1
Data 1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1
Data 1,0,0,0,0,2,2,2,0,0,0,0,0,0,0,0,0,0,0,1
Data 1,0,0,0,0,0,0,0,0,0,0,0,0,3,3,3,0,0,0,1
Data 1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1
Data 1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1
Data 1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1
Data 1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1
Data 1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1
Data 1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1
Data 1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1
Data 1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1
Data 1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1
Data 1,0,4,4,4,0,0,0,0,0,0,0,0,0,0,0,5,5,5,1
' Row 15 (bottom/ground)
Data 1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1
' Platforms: count, then [x,y,vx,vy,type]
Data 2
Data 100,100,128,0,1  ' Horizontal slider
Data 200,150,0,-64,2  ' Vertical lift
' Hazards: count, then [x,y]
Data 3
Data 50,220, 100,220, 150,220
' Spawn point
Data 32,32
' Exit point
Data 280,200

' === MAP STORAGE ===
Dim map(20,16)

' === GAME STATE ===
px#=0: py#=0  ' Set by spawn point
playerHp=3
score=0

' === LEVEL LOADING ===
Procedure LoadLevel[levelNum]
  ' Position data pointer
  If levelNum=1 Then Restore Level1Data

  ' Read dimensions
  Read mapWidth,mapHeight

  ' Read tile map
  For Y=0 To mapHeight-1
    For X=0 To mapWidth-1
      Read map(X,Y)
    Next X
  Next Y

  ' Read platforms
  Read platformCount
  For I=1 To platformCount
    Read platX,platY,platVX,platVY,platType
    ' Store in platform array
    plat#(I,0)=platX*256
    plat#(I,1)=platY*256
    plat#(I,2)=platVX
    plat#(I,3)=platVY
    plat#(I,4)=platType
    plat#(I,5)=0
  Next I

  ' Read hazards
  Read hazardCount
  For I=1 To hazardCount
    Read hazX(I),hazY(I)
    hazActive(I)=1
  Next I

  ' Read spawn point
  Read spawnX,spawnY
  px#=spawnX*256
  py#=spawnY*256
  vy#=0
  vx#=0

  ' Read exit point
  Read exitX,exitY
End Proc

' === RENDERING ===
Procedure DrawLevel
  Cls 0
  For Y=0 To mapHeight-1
    For X=0 To mapWidth-1
      tile=map(X,Y)
      If tile>0
        ' Paste tile graphic
        Paste Bob X*tileSize,Y*tileSize,tile
      End If
    Next X
  Next Y
End Proc

' === MAIN GAME LOOP ===
LoadLevel[currentLevel]
DrawLevel

Do
  ' [... game loop from L30 ...]

  ' Check exit collision
  If px#/256 > exitX-16 and px#/256 < exitX+16
    If py#/256 > exitY-16 and py#/256 < exitY+16
      ' Reached exit!
      Inc currentLevel
      If currentLevel>3 Then
        ' Game complete!
        Exit
      Else
        ' Load next level
        LoadLevel[currentLevel]
        DrawLevel
      End If
    End If
  End If

  Wait Vbl
  Bob Update
Loop Until Inkey$<>"" or playerHp<=0

' === LEVEL DATA LABELS ===
Level1Data:
' [DATA statements from above]
```

## Hardware Interaction

**Chips Involved:**
- **CPU** - Level loading, data parsing (~5-10ms per level)
- **Blitter** - Tile rendering (Paste Bob)
- **Disk** - Optional: load levels from files

**Memory:**
- 20×16 map = 320 bytes
- 3 levels = 960 bytes
- Tile graphics: 8 tiles × 512 bytes = 4KB
- Platform/hazard data: ~1KB per level

**Performance:**
- Loading from DATA: instant (already in RAM)
- Loading from disk: 0.5-1 second per level
- Drawing level: ~10ms (done once, not every frame)

## Common Pitfalls

1. **DATA out of sync:** Forgetting to update DATA count when adding entities
2. **No Restore before Read:** Reads continue from wrong position
3. **Redrawing level every frame:** Wastes Blitter time (draw once!)
4. **Hard-coded entity limits:** Use DATA counts to size arrays dynamically
5. **No level validation:** Bad DATA crashes program

## Extension Ideas

- RLE compression for sparse maps
- External level editor (save/load binary format)
- Multiple tile layers (background, foreground)
- Animated tiles (waterfalls, torches)
- Secret areas and alternate paths

## Builds Toward

**In This Arc:**
- L32: Complete platform game with multiple levels

**Future Tiers:**
- Procedural level generation
- Tile-based AI pathfinding

## Quick Reference

### Level Data Format
```amos
' Level structure
Data width, height
Data tile, tile, tile... (width × height tiles)
Data platformCount
Data platX, platY, platVX, platVY, platType  ' × platformCount
Data hazardCount
Data hazX, hazY  ' × hazardCount
Data spawnX, spawnY
Data exitX, exitY
```

### Level Loader Pattern
```amos
Procedure LoadLevel[num]
  ' Position DATA pointer
  If num = 1 Then Restore Level1Data
  If num = 2 Then Restore Level2Data

  ' Read map
  Read w, h
  For y = 0 To h - 1
    For x = 0 To w - 1
      Read map(x, y)
    Next x
  Next y

  ' Read entities
  Read entityCount
  For i = 1 To entityCount
    Read entityData...
  Next i

  ' Read spawn/exit
  Read spawnX, spawnY
  Read exitX, exitY

  ' Initialize player
  px# = spawnX * 256
  py# = spawnY * 256
End Proc
```

### Tile Rendering
```amos
' Draw level once
Procedure DrawLevel
  Cls 0
  For y = 0 To mapHeight - 1
    For x = 0 To mapWidth - 1
      tile = map(x, y)
      If tile > 0
        Paste Bob x * tileSize, y * tileSize, tile
      End If
    Next x
  Next y
End Proc

' In main loop: DON'T redraw every frame!
' Only redraw when loading new level
```

### Level Transition
```amos
' Check exit collision
If Distance(player, exit) < threshold
  ' Fade out
  For fade = 15 To 0 Step -1
    Fade fade
    Wait Vbl
  Next fade

  ' Load next level
  Inc currentLevel
  LoadLevel[currentLevel]
  DrawLevel

  ' Fade in
  For fade = 0 To 15
    Fade fade
    Wait Vbl
  Next fade
End If
```

### File-Based Levels (Advanced)
```amos
' Save level to disk
Procedure SaveLevel[filename$]
  Open Out 1, filename$
  ' Write dimensions
  Print #1, mapWidth; ","; mapHeight

  ' Write map
  For y = 0 To mapHeight - 1
    For x = 0 To mapWidth - 1
      Print #1, map(x, y); ",";
    Next x
  Next y

  ' Write entities...
  Close 1
End Proc

' Load level from disk
Procedure LoadLevelFile[filename$]
  Open In 1, filename$
  Input #1, mapWidth, mapHeight

  For y = 0 To mapHeight - 1
    For x = 0 To mapWidth - 1
      Input #1, map(x, y)
    Next x
  Next y

  ' Read entities...
  Close 1
End Proc
```

### RLE Compression (Simple)
```amos
' Compress: count, tile, count, tile...
' Example: 5 zeros, 3 ones, 2 zeros = "5,0,3,1,2,0"

Procedure LoadCompressedLevel
  Read mapWidth, mapHeight
  x = 0: y = 0

  Repeat
    Read count, tile
    For i = 1 To count
      map(x, y) = tile
      Inc x
      If x >= mapWidth Then x = 0: Inc y
    Next i
  Until y >= mapHeight
End Proc
```

---

**Version:** 1.0
**Created:** 2025-10-27
