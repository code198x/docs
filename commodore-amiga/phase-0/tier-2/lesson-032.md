# Lesson 032: Platform Game Synthesis

**Arc:** Platform Game
**Position:** Lesson 5 of 5 in arc (DELIVERABLE)
**Type:** Synthesis
**Estimated Completion:** 600-700 lines of code

## Learning Objectives

- Synthesize all Phase 0 Tier 2 concepts
- Create complete multi-level platform game
- Implement progression and scoring system
- Deliver polished, playable game

## Prerequisites

**From All Previous Arcs:**
- Animation System (L17-21)
- Arcade Action (L22-27)
- Platform Game (L28-31)

**Complete Skill Set:**
- AMAL animation
- Sprite optimization
- Gravity physics
- Tile collision
- Moving platforms
- Level loading
- Game state management

## Key Concepts Introduced

### Complete Game Architecture
Title → Level Select → Gameplay → Results → Next Level. Full game loop with save system, high scores, and progression tracking.

### Camera System
Scrolling viewport follows player. Level larger than screen, camera keeps player centered (with screen boundaries).

### Collectibles & Scoring
Coins, gems, power-ups. Track collection for level completion percentage. Combo multipliers for consecutive pickups.

### Polish Suite
Particle effects, screen transitions, animated UI elements, sound effects synchronized to actions. Professional-feeling game experience.

## Code Pattern

This is a complete platform game synthesizing all Tier 2 concepts. Due to size, showing key architectural pieces:

```amos
' ================================================
' PLATFORM ADVENTURE - COMPLETE GAME
' Synthesizes: Gravity, tiles, platforms, levels,
' animation, scoring, polish
' ================================================

Screen Open 0,640,512,16,Hires  ' Large level buffer
Screen Open 1,320,256,16,Lowres  ' Display viewport
Curs Off: Flash Off

' ================================================
' GAME STATE
' ================================================
Dim gameState$(1)  ' "title", "playing", "levelComplete", "gameOver"
gameState$="title"

currentLevel=1
maxLevel=5

playerHp=5
maxHp=5
lives=3
score=0
coins=0
totalCoins=0

' High score
highScore=0

' ================================================
' TILE & SPRITE LOADING
' ================================================
Procedure LoadAssets
  Screen 0  ' Level buffer

  ' Tile set (16x16)
  ' 0=empty, 1=grass, 2=stone, 3=metal, 4=coin, 5=spike, 6=exit
  For T=1 To 10
    Ink T+1
    Bar 0,0 To 15,15
    ' Draw tile-specific details
    Get Bob T,0,0 To 16,16
  Next T

  ' Player sprites (32 frames: idle, walk, jump, fall, hurt)
  For F=1 To 32
    Ink 2+F Mod 3
    Bar 0,0 To 15,15
    Get Bob 100+F,0,0 To 16,16
  Next F

  ' Enemy sprites
  ' Collectible sprites
  ' Effect sprites (particles, etc.)

  Screen 1  ' Return to display screen
End Proc

' ================================================
' CAMERA SYSTEM
' ================================================
cameraX=0: cameraY=0
cameraW=320: cameraH=256

Procedure UpdateCamera
  ' Center camera on player
  targetCamX=px#/256 - cameraW/2
  targetCamY=py#/256 - cameraH/2

  ' Smooth follow (lerp)
  cameraX=cameraX+(targetCamX-cameraX)/8
  cameraY=cameraY+(targetCamY-cameraY)/8

  ' Clamp to level bounds
  If cameraX<0 Then cameraX=0
  If cameraX>levelWidth*tileSize-cameraW Then cameraX=levelWidth*tileSize-cameraW
  If cameraY<0 Then cameraY=0
  If cameraY>levelHeight*tileSize-cameraH Then cameraY=levelHeight*tileSize-cameraH

  ' Update display (screen 0 to screen 1)
  Screen Copy 0,cameraX,cameraY To cameraX+cameraW-1,cameraY+cameraH-1 To 1,0,0
End Proc

' ================================================
' LEVEL DATA & LOADING
' ================================================
Dim map(100,64)  ' Large level support
maxPlatforms=20
maxEnemies=30
maxCollectibles=100

Dim plat#(maxPlatforms,6)
Dim enemy#(maxEnemies,8)
Dim collect(maxCollectibles,4)  ' x,y,type,active

Procedure LoadLevel[num]
  ' [Load from DATA as in L31]
  ' Initialize all entities
  ' Set spawn point
  ' Reset timers

  ' Draw level to screen 0 (large buffer)
  Screen 0
  Cls 0
  For Y=0 To levelHeight-1
    For X=0 To levelWidth-1
      tile=map(X,Y)
      If tile>0
        Paste Bob X*tileSize,Y*tileSize,tile
      End If
    Next X
  Next Y
  Screen 1
End Proc

' ================================================
' PLAYER CONTROLLER
' ================================================
' State machine: idle, walk, jump, fall, hurt, dead
playerState$="idle"
animFrame=0
animTimer=0

' Physics (from L28)
px#=0: py#=0
vx#=0: vy#=0
gravity#=24
jumpSpeed#=-800
terminalVel#=768
grounded=False

' Animation (from L19)
walkFrames=8  ' Frames 101-108
jumpFrame=109
fallFrame=110
hurtFrame=111

Procedure UpdatePlayer
  ' === INPUT ===
  If playerState$<>"hurt"
    If Jleft(1) Then Dec vx#,32: facing=-1
    If Jright(1) Then Add vx#,32: facing=1

    If Not Jleft(1) and Not Jright(1)
      If vx#>0 Then Dec vx#,16
      If vx#<0 Then Add vx#,16
    End If

    If vx#>512 Then vx#=512
    If vx#<-512 Then vx#=-512

    If Fire(1) and grounded and playerState$<>"jump"
      vy#=jumpSpeed#
      playerState$="jump"
      ' Sam Play "jump.wav"
    End If
  End If

  ' === PHYSICS ===
  ' [Full physics from L28]

  ' === COLLISION ===
  ' [Tile collision from L29]
  ' [Platform collision from L30]

  ' === STATE MACHINE ===
  If grounded
    If Abs(vx#)<16 Then playerState$="idle" Else playerState$="walk"
  Else
    If vy#<0 Then playerState$="jump" Else playerState$="fall"
  End If

  ' === ANIMATION ===
  Inc animTimer
  If animTimer>5
    animTimer=0
    Inc animFrame
  End If

  If playerState$="idle" Then animFrame=100
  If playerState$="walk" Then animFrame=100+(animFrame Mod walkFrames)
  If playerState$="jump" Then animFrame=jumpFrame
  If playerState$="fall" Then animFrame=fallFrame
  If playerState$="hurt" Then animFrame=hurtFrame

  ' === COLLECTIBLES ===
  For I=1 To totalCoins
    If collect(I,3)=1  ' Active
      cx=collect(I,0): cy=collect(I,1)
      If Distance(px#/256,py#/256,cx,cy)<16
        collect(I,3)=0  ' Collected
        Inc coins
        Add score,100
        ' Sam Play "coin.wav"
        ' SpawnParticles[cx,cy,10]
      End If
    End If
  Next I

  ' === HAZARDS ===
  ' [Hazard collision from L30]

  ' === EXIT ===
  If Distance(px#/256,py#/256,exitX,exitY)<16
    gameState$="levelComplete"
  End If
End Proc

' ================================================
' ENEMY AI
' ================================================
Procedure UpdateEnemies
  For I=1 To maxEnemies
    If enemy#(I,0)=1  ' Active
      ' [Chase AI from L15]
      ' [Animation states]
      ' [Attack patterns from L24]

      ' Collision with player
      If Distance(px#/256,py#/256,enemy#(I,1)/256,enemy#(I,2)/256)<16
        If invincible=0
          Dec playerHp
          invincible=100
          playerState$="hurt"
          ' Knockback
          ' Sam Play "hurt.wav"
          If playerHp<=0 Then Dec lives: gameState$="dead"
        End If
      End If
    End If
  Next I
End Proc

' ================================================
' MAIN GAME LOOP
' ================================================
Procedure GameLoop
  LoadLevel[currentLevel]

  Do
    ' === UPDATE PHASE ===
    UpdatePlayer
    UpdateEnemies
    ' UpdatePlatforms (from L30)
    ' UpdateParticles
    UpdateCamera

    ' === RENDER PHASE ===
    ' Player BOB at screen position (world pos - camera)
    screenX=px#/256-cameraX
    screenY=py#/256-cameraY
    Bob 1,screenX,screenY,animFrame

    ' Enemies at screen positions
    ' Platforms at screen positions
    ' Collectibles at screen positions

    ' === UI ===
    Locate 0,0: Print "HP:";playerHp;" Lives:";lives;" Score:";score;" Coins:";coins;"/";totalCoins

    Wait Vbl
    Bob Update

    ' === STATE TRANSITIONS ===
    If gameState$="levelComplete" Then Exit
    If gameState$="dead" and lives<=0 Then Exit
    If gameState$="dead" and lives>0 Then
      ' Respawn
      LoadLevel[currentLevel]
      gameState$="playing"
    End If
  Loop Until Inkey$=Chr$(27)
End Proc

' ================================================
' LEVEL COMPLETE SCREEN
' ================================================
Procedure LevelComplete
  Cls 0
  Locate 8,8: Print "LEVEL COMPLETE!"
  Locate 6,10: Print "Coins: ";coins;"/";totalCoins
  bonus=coins*100
  Locate 6,11: Print "Bonus: ";bonus
  Add score,bonus
  Locate 6,12: Print "Total Score: ";score

  Wait 150

  Inc currentLevel
  If currentLevel>maxLevel Then
    GameComplete
  Else
    gameState$="playing"
  End If
End Proc

' ================================================
' TITLE SCREEN
' ================================================
Procedure TitleScreen
  Cls 0
  Locate 7,6: Print "PLATFORM ADVENTURE"
  Locate 8,10: Print "Press FIRE to Start"
  Locate 6,12: Print "High Score: ";highScore
  Locate 8,16: Print "Controls:"
  Locate 8,17: Print "Arrows = Move"
  Locate 8,18: Print "Fire = Jump"

  Repeat
    Wait Vbl
  Until Fire(1)

  gameState$="playing"
End Proc

' ================================================
' GAME COMPLETE
' ================================================
Procedure GameComplete
  Cls 0
  Locate 7,8: Print "CONGRATULATIONS!"
  Locate 5,10: Print "You completed all levels!"
  Locate 7,12: Print "Final Score: ";score
  If score>highScore Then
    highScore=score
    Locate 6,14: Print "NEW HIGH SCORE!"
  End If

  Wait 200
  gameState$="title"
  currentLevel=1
  score=0
  coins=0
  lives=3
End Proc

' ================================================
' MAIN
' ================================================
LoadAssets

Repeat
  If gameState$="title" Then TitleScreen
  If gameState$="playing" Then GameLoop
  If gameState$="levelComplete" Then LevelComplete
Until False
```

## Hardware Interaction

**Full Amiga Capability:**
- **Blitter** - Scrolling, BOB rendering (100+ sprites possible)
- **Copper** - Palette effects, raster bars for UI
- **Paula** - 4-channel music + sound effects
- **CPU** - Game logic, physics, AI (~15ms per frame)

**Memory Management:**
- Level buffer (640×512×4 bitplanes) = 160KB
- Display screen (320×256×4 bitplanes) = 40KB
- Tile graphics = ~10KB
- Sprite graphics = ~20KB
- Code + data = ~50KB
- Total: ~280KB (fits in 512KB Amiga)

## Common Pitfalls

1. **Scope creep:** Trying to add everything, never finishing
2. **No save/checkpoints:** Players lose all progress on death
3. **Unfair difficulty spikes:** Level 2 harder than level 5
4. **Poor camera:** Jerky or delayed following feels bad
5. **No playtesting:** Bugs and imbalance invisible until others play

## Extension Ideas

- Multiple playable characters (different abilities)
- Secret levels and alternate paths
- Boss fights with multiple phases
- Time attack mode (speedrun timer)
- Co-op multiplayer
- Level editor built-in

## Builds Toward

**Phase 1 (Advanced):**
- Procedural level generation
- Network multiplayer
- Advanced AI (pathfinding, formations)
- Scripting system for events

## Quick Reference

### Camera Follow Pattern
```amos
Procedure UpdateCamera
  ' Target position (center on player)
  targetX = px# / 256 - cameraW / 2
  targetY = py# / 256 - cameraH / 2

  ' Smooth lerp (adjust divisor for responsiveness)
  cameraX = cameraX + (targetX - cameraX) / 8
  cameraY = cameraY + (targetY - cameraY) / 8

  ' Clamp to level
  If cameraX < 0 Then cameraX = 0
  If cameraX > maxCameraX Then cameraX = maxCameraX
  ' ...same for Y

  ' Copy visible region to display
  Screen Copy 0, cameraX, cameraY To cameraX + 319, cameraY + 255 To 1, 0, 0
End Proc
```

### World-to-Screen Conversion
```amos
' Entity world position → screen position
screenX = worldX - cameraX
screenY = worldY - cameraY

' Only render if on-screen
If screenX >= -32 and screenX <= 352
  If screenY >= -32 and screenY <= 288
    Bob bobNum, screenX, screenY, frame
  End If
End If
```

### Game State Machine
```
TITLE → PLAYING ⇄ PAUSED
          ↓
      LEVEL_COMPLETE → next level
          ↓
       GAME_OVER → TITLE
```

### Polish Checklist
- [ ] Screen transitions (fade, wipe)
- [ ] Particle effects (coin sparkles, explosion debris)
- [ ] Sound effects synchronized to actions
- [ ] Background music tracks per level
- [ ] Animated UI elements (HUD, menus)
- [ ] Screen shake on damage/explosion
- [ ] Invulnerability flash effect
- [ ] Smooth camera follow
- [ ] Level intro text
- [ ] Score popups on collectibles

---

**Version:** 1.0
**Created:** 2025-10-27
**Note:** This is the FINAL DELIVERABLE for Phase 0 Tier 2. Students create a complete, multi-level platform game demonstrating mastery of all Tier 2 concepts across animation, arcade action, and platform mechanics. This is a portfolio-quality project.
