# Amiga AMOS & Blitz Basic Curriculum

**Purpose:** Define BASIC-based curriculum tracks for Commodore Amiga using AMOS and Blitz Basic - languages that produced real commercial games.

**Last Updated:** 2026-01-18

---

## Overview

| Track | Language | Games | Target |
|-------|----------|-------|--------|
| **AMOS Track** | AMOS Professional | 8 | Beginners, hobbyists |
| **Blitz Track** | Blitz Basic 2 | 8 | Intermediate, performance |

Both tracks can lead to the Assembly track or stand alone as complete curricula.

---

## Why AMOS and Blitz?

### Commercial Proof

These weren't toy languages - real games shipped:

| Game | Language | Developer |
|------|----------|-----------|
| **Worms** | Blitz Basic | Team17 |
| **Skidmarks** | Blitz Basic | Acid Software |
| **Super Skidmarks** | Blitz Basic | Acid Software |
| **Ultimate Soccer Manager** | AMOS | Impressions |
| **Guardian** | AMOS | Acid Software |
| **Scorched Tanks** | AMOS | Various |

If Worms could be made in Blitz Basic, students can make great games too.

### AMOS vs Blitz: When to Use Which

| Factor | AMOS | Blitz Basic |
|--------|------|-------------|
| **Learning curve** | Gentler | Steeper |
| **Speed** | Good (compiled) | Excellent |
| **Documentation** | Extensive | Good |
| **Community (historical)** | Huge | Large |
| **Modern use** | Emulation | Emulation |
| **Best for** | Learning, rapid dev | Performance games |

---

## Part 1: AMOS Track (8 Games)

### Track Overview

| Aspect | Details |
|--------|---------|
| **Language** | AMOS Professional |
| **Games** | 8 |
| **Prerequisite** | Basic programming concepts |
| **Units per game** | 4-16 (varies by complexity) |
| **Outcome** | Complete Amiga games |

### Game 1: Target Practice
**"Pixel Hunter"**

| Aspect | Details |
|--------|---------|
| **Units** | 4 |
| **Genre** | Click targets |
| **Concepts** | Mouse input, sprites, scoring |

**What You Build:**
- Targets appear randomly
- Click to score
- Timer countdown
- High score

**Skills Introduced:**
- AMOS environment
- Screen setup
- Mouse reading
- Sprite display
- Timer/scoring

**Sample Code:**
```basic
' PIXEL HUNTER - AMOS
Screen Open 0,320,256,32,Lowres
Flash Off : Curs Off : Cls 0
Load "targets.abk",1

SCORE=0 : TIME=30

Do
  TARGETX=Rnd(280)+20
  TARGETY=Rnd(200)+20
  Sprite 1,TARGETX,TARGETY,1

  Repeat
    If Mouse Key=1
      MX=X Screen(X Mouse)
      MY=Y Screen(Y Mouse)
      If Abs(MX-TARGETX)<16 And Abs(MY-TARGETY)<16
        Inc SCORE : Exit
      End If
    End If
  Until Timer>50*TIME

  Dec TIME
Loop Until TIME=0

Print "FINAL SCORE: ";SCORE
```

---

### Game 2: Maze Explorer
**"Labyrinth"**

| Aspect | Details |
|--------|---------|
| **Units** | 8 |
| **Genre** | Maze navigation |
| **Concepts** | Tile maps, collision, bob graphics |

**What You Build:**
- Generated or designed mazes
- Player movement
- Wall collision
- Exit goal

**Skills Introduced:**
- Bob (blitter object) graphics
- Tile-based collision
- Map arrays
- Keyboard input (joystick)

---

### Game 3: Breakout Clone
**"Barrier Bash"**

| Aspect | Details |
|--------|---------|
| **Units** | 8 |
| **Genre** | Breakout |
| **Concepts** | Physics, brick arrays, power-ups |

**What You Build:**
- Paddle control
- Ball physics
- Destructible bricks
- Simple power-ups

**Skills Introduced:**
- Bob collision
- Ball reflection
- Array manipulation (bricks)
- Game states

---

### Game 4: Shoot 'Em Up
**"Nebula Strike"**

| Aspect | Details |
|--------|---------|
| **Units** | 8 |
| **Genre** | Vertical shooter |
| **Concepts** | Scrolling, multiple enemies, bullets |

**What You Build:**
- Scrolling starfield
- Player ship
- Enemy waves
- Shooting/collision

**Skills Introduced:**
- Hardware scrolling
- Multiple sprites
- Bullet management
- Wave patterns
- Screen wrapping

---

### Game 5: Platform Game
**"Hop Island"**

| Aspect | Details |
|--------|---------|
| **Units** | 16 |
| **Genre** | Platformer |
| **Concepts** | Gravity, jumping, level design |

**What You Build:**
- Platform levels
- Jump physics
- Collectibles
- Enemies

**Skills Introduced:**
- Gravity/physics
- Tile collision (platforms)
- Level data
- Enemy AI (simple)
- Lives/continues

---

### Game 6: Puzzle Game
**"Match Gems"**

| Aspect | Details |
|--------|---------|
| **Units** | 8 |
| **Genre** | Match-3 puzzle |
| **Concepts** | Grid logic, cascades, scoring |

**What You Build:**
- Gem grid
- Match detection
- Cascade/refill
- Score combos

**Skills Introduced:**
- 2D array manipulation
- Pattern matching
- Cascade logic
- Animation timing

---

### Game 7: Racing Game
**"Speed Demon"**

| Aspect | Details |
|--------|---------|
| **Units** | 8 |
| **Genre** | Top-down racing |
| **Concepts** | Track, AI opponents, laps |

**What You Build:**
- Scrolling track
- Car physics
- AI racers
- Lap system

**Skills Introduced:**
- Dual playfield (track/sprites)
- Car handling
- Simple AI
- Checkpoint system

---

### Game 8: Adventure Game
**"Treasure Quest"**

| Aspect | Details |
|--------|---------|
| **Units** | 16 |
| **Genre** | Action-adventure |
| **Concepts** | Inventory, NPCs, quests |

**What You Build:**
- Multi-screen world
- Inventory system
- NPC interaction
- Quest completion

**Skills Introduced:**
- Screen transitions
- Inventory management
- Dialogue system
- Save/load (optional)
- Game structure

**Capstone project** - combines everything learned.

---

## Part 2: Blitz Basic Track (8 Games)

### Track Overview

| Aspect | Details |
|--------|---------|
| **Language** | Blitz Basic 2 |
| **Games** | 8 |
| **Prerequisite** | Some programming experience |
| **Units per game** | 4-16 (varies by complexity) |
| **Focus** | Performance, professional techniques |
| **Outcome** | Commercial-quality games |

### Why Blitz After/Instead of AMOS?

| Scenario | Recommendation |
|----------|----------------|
| **Complete beginner** | AMOS first |
| **Some programming experience** | Can start Blitz |
| **Want fastest games** | Blitz |
| **After AMOS track** | Blitz for next level |

### Game 1: Reaction Test
**"Reflex"**

| Aspect | Details |
|--------|---------|
| **Units** | 4 |
| **Genre** | Reaction timer |
| **Concepts** | Blitz environment, timing, display |

**Skills Introduced:**
- Blitz Basic syntax
- Compilation
- VBlank timing
- Display setup

---

### Game 2: Snake
**"Venom"**

| Aspect | Details |
|--------|---------|
| **Units** | 8 |
| **Genre** | Snake |
| **Concepts** | Shape drawing, growth, speed |

**Skills Introduced:**
- Blitz shapes
- List/queue data structures
- Speed management
- Clean game loops

---

### Game 3: Asteroids
**"Rock Hazard"**

| Aspect | Details |
|--------|---------|
| **Units** | 8 |
| **Genre** | Asteroids |
| **Concepts** | Rotation, thrust, wrapping |

**Skills Introduced:**
- Angle/rotation maths
- Thrust physics
- Object splitting
- Screen wrapping

---

### Game 4: Defence Game
**"Tower Guard"**

| Aspect | Details |
|--------|---------|
| **Units** | 8 |
| **Genre** | Fixed defender |
| **Concepts** | Aiming, waves, upgrades |

**Skills Introduced:**
- Angle calculation
- Wave spawning
- Upgrade systems
- Resource management

---

### Game 5: Driving Game
**"Road Rage"**

| Aspect | Details |
|--------|---------|
| **Units** | 16 |
| **Genre** | Racing (Skidmarks-style) |
| **Concepts** | Car physics, tracks, multiplayer |

**What You Build:**
- Top-down racing
- Skid/drift physics
- Track system
- 2-player split screen

**Skills Introduced:**
- Advanced car physics
- Track collision
- Split-screen display
- Blitz bitmap manipulation

This game type is what Blitz is famous for!

---

### Game 6: Action Platformer
**"Metal Warrior"**

| Aspect | Details |
|--------|---------|
| **Units** | 16 |
| **Genre** | Run and gun |
| **Concepts** | Turrican-style action |

**What You Build:**
- Large scrolling levels
- Multiple weapons
- Boss battles
- Power-ups

**Skills Introduced:**
- Large level handling
- Weapon systems
- Boss patterns
- Scrolling optimisation

---

### Game 7: Strategy Game
**"Battle Grid"**

| Aspect | Details |
|--------|---------|
| **Units** | 8 |
| **Genre** | Turn-based tactics |
| **Concepts** | Grid movement, units, combat |

**Skills Introduced:**
- Turn-based structure
- Unit management
- Combat calculation
- AI opponents

---

### Game 8: Worms-Style Game
**"Artillery Duel"**

| Aspect | Details |
|--------|---------|
| **Units** | 16 |
| **Genre** | Artillery/Worms style |
| **Concepts** | Terrain, projectiles, destruction |

**What You Build:**
- Destructible terrain
- Angle/power shooting
- Multiple weapons
- Turn-based multiplayer

**Skills Introduced:**
- Terrain manipulation
- Projectile physics
- Pixel-level collision
- Multiplayer turns

**Capstone** - this is the style of game that made Blitz famous (Worms).

---

## AMOS Technical Reference

### Essential Commands

| Category | Commands |
|----------|----------|
| **Display** | Screen Open, Screen Copy, Cls |
| **Sprites** | Sprite, Sprite Off, X Sprite, Y Sprite |
| **Bobs** | Bob, Bob Off, Paste Bob |
| **Input** | Joy, Jup, Jdown, Fire, Mouse Key |
| **Sound** | Sam Play, Track Play |
| **Collision** | Spritebob Col, Bob Col |

### Screen Setup

```basic
Screen Open 0,320,256,32,Lowres
Flash Off : Curs Off : Cls 0
Hide On  ' Hide mouse
Double Buffer
```

### Sprite Handling

```basic
Load "sprites.abk",1  ' Load sprite bank
Sprite 1,160,128,1    ' Sprite 1, position, image 1
X Sprite(1)=X Sprite(1)+2  ' Move sprite
```

### Game Loop Pattern

```basic
Do
  ' Input
  If Jleft(1) Then Dec PLAYERX
  If Jright(1) Then Inc PLAYERX
  If Fire(1) Then Gosub SHOOT

  ' Update
  Gosub MOVE_ENEMIES
  Gosub CHECK_COLLISION

  ' Draw
  Sprite 1,PLAYERX,PLAYERY,1

  ' Sync
  Wait Vbl
Loop
```

---

## Blitz Basic Technical Reference

### Essential Commands

| Category | Commands |
|----------|----------|
| **Display** | BitMap, Use BitMap, VWait |
| **Shapes** | LoadShapes, Blit, QBlit |
| **Input** | Joyb, Joyx, Joyy |
| **Sound** | Sound, Sample |
| **Collision** | ShapeHit, RectsHit |

### Blitz Game Structure

```blitz
; Blitz Basic 2 structure
DEFTYPE .w  ; Default to word

; Constants
#SCREENW = 320
#SCREENH = 256

; Initialisation
BitMap 0,#SCREENW,#SCREENH,4
LoadShapes 0,"sprites.shp"

; Main loop
While NOT done
  VWait

  ; Input
  If Joyb(1) Then Gosub Shoot

  ; Update
  Gosub MovePlayer
  Gosub MoveEnemies

  ; Draw
  Cls 0
  Blit 0,playerx,playery

Wend
```

### Performance Tips

| Tip | Reason |
|-----|--------|
| **Use DEFTYPE** | Avoid slow floats |
| **QBlit vs Blit** | Faster, no clipping |
| **Precalculate** | Tables faster than maths |
| **VWait sync** | Consistent timing |

---

## Tool Setup

### AMOS Professional

| Tool | Location |
|------|----------|
| **AMOS Pro** | Aminet, original disks |
| **Sprite Editor** | Built into AMOS |
| **Sample Editor** | AMOS includes |

### Blitz Basic 2

| Tool | Location |
|------|----------|
| **Blitz Basic 2** | Acid Software, Aminet |
| **Shape Editor** | Included |
| **Debugger** | Built in |

### Emulator Configuration

**WinUAE/FS-UAE setup:**
- A500 or A1200 configuration
- 1MB+ RAM
- Workbench 1.3 or 3.0
- Hard drive for convenience

---

## Comparison to Assembly Track

| Aspect | AMOS/Blitz | Assembly |
|--------|------------|----------|
| **Development speed** | Fast | Slow |
| **Execution speed** | Good | Best |
| **Learning curve** | Gentle | Steep |
| **Hardware access** | Abstracted | Direct |
| **Commercial viable** | Yes (proven) | Yes |
| **Understanding depth** | Surface | Complete |

### Progression Path

```
AMOS Track (8 games)
       ↓
Blitz Track (8 games) ← Can skip AMOS if experienced
       ↓
Assembly Track (16 games)
```

Or stay with AMOS/Blitz - they're complete environments for making real games.

---

## Summary

### AMOS Track
- **8 games** from simple to complex
- **Beginner-friendly** syntax
- **Rapid development** cycle
- **Historical significance** - huge community
- **Commercial games** were made in AMOS

### Blitz Track
- **8 games** focused on performance
- **Compiled** for speed
- **Professional** results
- **Worms was made in Blitz** - proof of capability
- **Advanced** techniques

Both tracks prove BASIC can make real games - not just toys.

---

## Vault Entries

| Entry | Type |
|-------|------|
| `amos-curriculum` | Curriculum |
| `blitz-curriculum` | Curriculum |
| `amos-commercial-games` | Culture |
| `blitz-commercial-games` | Culture |

**New entries: 4**
