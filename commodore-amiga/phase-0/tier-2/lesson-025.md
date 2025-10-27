# Lesson 025: Enemy Wave Patterns

**Arc:** Arcade Action
**Position:** Lesson 4 of 6 in arc
**Type:** Standard
**Estimated Completion:** 160 lines of code

## Learning Objectives

- Create enemy formation flights
- Implement wave spawn systems
- Combine movement patterns with AI
- Manage enemy lifecycle and difficulty scaling

## Prerequisites

**From Previous Lessons:**
- Sprite pools and optimization (L23)
- Bullet patterns (L24)
- Enemy AI basics (L15)

**AMOS Knowledge:**
- Procedures for organization
- Timer for wave scheduling

## Key Concepts Introduced

### Formation Flying
Enemies move in coordinated patterns: V-formations, sine waves, circular arcs. Each enemy follows mathematical path relative to wave spawn point.

### Wave Spawner
System that triggers enemy groups at intervals. Tracks current wave number, enemies remaining, and difficulty progression.

### Enemy States
Each enemy has lifecycle: SPAWNING → ACTIVE → ATTACKING → DESTROYED. State determines behavior (invulnerable during spawn, can shoot when active).

### Difficulty Scaling
Later waves have more enemies, faster movement, more aggressive attacks. Multiply base stats by wave multiplier.

## Code Pattern

```amos
Screen Open 0,320,256,32,Lowres
Curs Off: Flash Off: Cls 0

' Create sprites
Ink 2: Bar 0,0 To 11,11: Get Bob 1,0,0 To 12,12  ' Enemy
Ink 3: Bar 0,0 To 3,3: Get Bob 2,0,0 To 4,4      ' Bullet
Cls 0

' Enemy pool
maxEnemies=30
Dim eactive(maxEnemies)
Dim ex#(maxEnemies),ey#(maxEnemies)
Dim evx#(maxEnemies),evy#(maxEnemies)
Dim estate$(maxEnemies)  ' "spawn", "active", "attack"
Dim etime(maxEnemies)    ' State timer
Dim epath$(maxEnemies)   ' Movement pattern

' Initialize enemy pool
For I=1 To maxEnemies
  Bob I+10,-100,-100,1  ' BOBs 11-40 for enemies
  Bob Off I+10
  eactive(I)=0
Next I

' Wave system
waveNumber=1
waveTimer=0
waveDelay=200  ' Frames between waves
enemiesLeft=0

' Player
px=160: py=200

Do
  ' Player movement
  If Jleft(1) Then Dec px,3
  If Jright(1) Then Add px,3

  ' Wave spawner
  Inc waveTimer
  If waveTimer>=waveDelay and enemiesLeft=0
    waveTimer=0
    SpawnWave[waveNumber]
    Inc waveNumber
  End If

  ' Update enemies
  For I=1 To maxEnemies
    If eactive(I)=1
      Inc etime(I)

      ' State machine
      If estate$(I)="spawn"
        ' Spawn animation: slide in from top
        Add ey#(I),128  ' 0.5 pixels/frame
        If etime(I)>60
          estate$(I)="active"
          etime(I)=0
        End If
      End If

      If estate$(I)="active"
        ' Follow movement pattern
        If epath$(I)="sine"
          ' Sine wave path
          Add ex#(I),evx#(I)
          ey#(I)=ey#(I)+128+64*Sin(etime(I)*5)
        End If

        If epath$(I)="circle"
          ' Circular arc
          angle=etime(I)*3
          ex#(I)=ex#(I)+256*Cos(angle)
          Add ey#(I),evy#(I)
        End If

        If epath$(I)="dive"
          ' Dive at player
          Add ex#(I),evx#(I)
          Add ey#(I),evy#(I)
        End If

        ' Attack timer
        If etime(I) Mod 50=0
          ' Fire bullet (use global bullet system from L24)
          ' FireAimed[ex#(I)/256, ey#(I)/256, px, py, 3*256]
        End If

        ' Off-screen = deactivate
        x=ex#(I)/256: y=ey#(I)/256
        If x<-20 or x>340 or y>280
          eactive(I)=0
          Bob Off I+10
          Dec enemiesLeft
        End If
      End If

      ' Render
      Bob I+10,ex#(I)/256,ey#(I)/256,1
      Bob On I+10
    End If
  Next I

  ' Display
  Locate 0,0: Print "Wave: ";waveNumber;" Enemies: ";enemiesLeft

  Wait Vbl
  Bob Update
Loop Until Inkey$=Chr$(27)

' ================================================
' WAVE PATTERNS
' ================================================

Procedure SpawnWave[wave]
  ' Difficulty scaling
  enemyCount=5+wave*2  ' More enemies each wave
  speed#=128+wave*16   ' Faster movement

  If wave=1 Then SpawnLine[enemyCount,speed#]
  If wave=2 Then SpawnVFormation[enemyCount,speed#]
  If wave=3 Then SpawnSineWave[enemyCount,speed#]
  If wave>=4 Then SpawnCircle[enemyCount,speed#]
End Proc

Procedure SpawnLine[count,speed#]
  ' Horizontal line across top
  spacing=280/count
  For I=0 To count-1
    SpawnEnemy[20+I*spacing, -20, 0, speed#, "sine"]
  Next I
End Proc

Procedure SpawnVFormation[count,speed#]
  ' V-shape formation
  halfCount=count/2
  For I=0 To halfCount-1
    ' Left arm
    SpawnEnemy[80-I*16, -20-I*12, 0, speed#, "dive"]
    ' Right arm
    SpawnEnemy[240+I*16, -20-I*12, 0, speed#, "dive"]
  Next I
End Proc

Procedure SpawnSineWave[count,speed#]
  ' Enemies follow sine wave path
  spacing=320/count
  For I=0 To count-1
    SpawnEnemy[I*spacing, -20, speed#, 0, "sine"]
  Next I
End Proc

Procedure SpawnCircle[count,speed#]
  ' Circle formation
  angleStep=360/count
  For I=0 To count-1
    angle=I*angleStep
    x=160+80*Cos(angle)
    y=64+40*Sin(angle)
    SpawnEnemy[x, y, 0, speed#, "circle"]
  Next I
End Proc

Procedure SpawnEnemy[startX,startY,vx#,vy#,path$]
  ' Find inactive slot
  For I=1 To maxEnemies
    If eactive(I)=0
      eactive(I)=1
      ex#(I)=startX*256
      ey#(I)=startY*256
      evx#(I)=vx#
      evy#(I)=vy#
      estate$(I)="spawn"
      etime(I)=0
      epath$(I)=path$
      Inc enemiesLeft
      Exit
    End If
  Next I
End Proc
```

## Hardware Interaction

**Chips Involved:**
- **CPU** - Wave spawning, formation math, AI (~3-4ms for 30 enemies)
- **Blitter** - Rendering enemies (~0.3ms for 12×12 sprite)
- **Paula** - Wave spawn sound, enemy fire sounds

**Performance:**
- 30 enemies × 12×12 = 144 bytes each = ~4.3KB
- At 50fps: 215KB/s (comfortable)
- Sin/Cos for paths: ~10μs each (negligible)

## Common Pitfalls

1. **Spawning all at once:** No formation, just mob of enemies
2. **No state management:** Enemies shoot during spawn (unfair)
3. **Fixed patterns only:** Boring after first wave
4. **No difficulty scaling:** Game doesn't get harder
5. **Forgetting to decrement enemiesLeft:** Wave never ends

## Extension Ideas

- Boss waves (single tough enemy with phases)
- Escort patterns (some enemies protect others)
- Kamikaze enemies (dive directly at player)
- Split on death (one enemy becomes two)
- Power-up drops when enemy destroyed

## Builds Toward

**In This Arc:**
- L26: Scrolling backgrounds for depth
- L27: Complete space shooter synthesis

## Quick Reference

### Wave Spawner Pattern
```amos
' Global state
waveNumber=1
waveTimer=0
waveDelay=200
enemiesLeft=0

' Each frame
Inc waveTimer
If waveTimer>=waveDelay and enemiesLeft=0
  waveTimer=0
  SpawnWave[waveNumber]
  Inc waveNumber
End If
```

### Formation Patterns
```amos
' Horizontal line
For I=0 To count-1
  SpawnEnemy[20+I*spacing, yPos, 0, speed#, "straight"]
Next I

' V formation
halfCount=count/2
For I=0 To halfCount-1
  SpawnEnemy[centerX-I*gap, yPos-I*vGap, vx#, vy#, "path"]
  SpawnEnemy[centerX+I*gap, yPos-I*vGap, -vx#, vy#, "path"]
Next I

' Circle
angleStep=360/count
For I=0 To count-1
  angle=I*angleStep
  x=centerX+radius*Cos(angle)
  y=centerY+radius*Sin(angle)
  SpawnEnemy[x, y, 0, 0, "circle"]
Next I
```

### Movement Patterns
```amos
' Sine wave
Add ex#,evx#
ey#=startY# + amplitude*Sin(etime*frequency)

' Circular arc
angle=startAngle + etime*angularSpeed
ex#=centerX# + radius*Cos(angle)
ey#=centerY# + radius*Sin(angle)

' Dive at player
dx=px-ex#/256: dy=py-ey#/256
dist=Sqr(dx*dx+dy*dy)
evx#=speed#*dx/dist
evy#=speed#*dy/dist
```

### Difficulty Scaling
```amos
' Base stats
baseSpeed#=128
baseHp=1
baseFireRate=50

' Per wave
speed#=baseSpeed# * (1 + waveNumber*0.2)
hp=baseHp + waveNumber/3
fireRate=baseFireRate - waveNumber*2  ' Faster shooting

' Enemy count
enemyCount=5 + waveNumber*2
```

### Enemy Lifecycle States
```amos
' State machine
If estate$(I)="spawn"
  ' Invulnerable, slide into position
  If etime(I)>60 Then estate$(I)="active"
End If

If estate$(I)="active"
  ' Follow path, can shoot, vulnerable
  ' Attack logic here
End If

If estate$(I)="dying"
  ' Death animation, no collision
  If etime(I)>30 Then eactive(I)=0: Bob Off I
End If
```

---

**Version:** 1.0
**Created:** 2025-10-27
