# Phase 1: Assembly + Hardware Fundamentals (Lessons 1-512)

**Total:** 512 lessons across 16 tiers (32 lessons per tier)

**Phase Goal:** Learn 6510 assembly language and C64 hardware through building 16 classic arcade games. Start with your first sprite in Pong and progress to multi-element complex games like Centipede.

**Prerequisites:** Phase 0 (BASIC) recommended but optional for students with programming experience.

**Phase Philosophy:**
- Assembly and hardware taught together from day 1
- Every lesson builds toward complete games
- No text-only games or abstract exercises
- Progressive complexity: Pong → Centipede
- Real C64 hardware, real game techniques

**Game Progression:**
- **Tier 1-4:** Single-screen games (Pong, Breakout, Space Invaders, Galaxian)
- **Tier 5-8:** Movement and enemies (Asteroids, Missile Command, Defender, Scramble)
- **Tier 9-12:** Advanced mechanics (Zaxxon, Dig Dug, Q*bert, Frogger)
- **Tier 13-16:** Complex systems (Donkey Kong, Mario Bros, Pac-Man, Centipede)

**What Students Master:**
- 6510 assembly fundamentals (all addressing modes, common instructions)
- VIC-II basics (sprites, colors, collision detection, simple raster effects)
- CIA basics (joystick input, keyboard scanning, simple timers)
- SID basics (simple sound effects and tones)
- Game loop architecture
- Basic physics (velocity, acceleration, bouncing)
- AABB collision detection
- Score and lives systems
- Simple scrolling
- Multi-element games (many enemies, projectiles)

---

## Phase 1 Overview

| Tier | Game | Deliverable | Key Skills |
|------|------|-------------|------------|
| 1 | Pong | 2-player paddle game | First sprite, joystick, collision, scoring |
| 2 | Breakout | Brick-breaking | Arrays of objects, bounce angles, power-ups |
| 3 | Space Invaders | Fixed shooter | Enemy grid, formation movement, shields |
| 4 | Galaxian | Diving enemies | Enemy AI, swooping patterns, attack waves |
| 5 | Asteroids | Vector-style | Rotation, momentum, wrapping, splitting |
| 6 | Missile Command | Defense | Trajectory, explosions, multiple targets |
| 7 | Defender | Side-scrolling | Scrolling, radar, enemy variety, rescue |
| 8 | Scramble | Terrain flying | Fuel system, terrain collision, bombing |
| 9 | Zaxxon | Isometric view | Altitude, shadows, 3D-effect positioning |
| 10 | Dig Dug | Underground | Tunnel digging, enemy inflation, rock dropping |
| 11 | Q*bert | Isometric hopping | Diamond grid, isometric movement, falling |
| 12 | Frogger | Lane crossing | Timing, platforms, multiple hazards |
| 13 | Donkey Kong | Multi-screen platformer | Jumping, ladders, level progression, barrels |
| 14 | Mario Bros | Arena platformer | POW block, platforms, enemy bouncing, 2-player |
| 15 | Pac-Man | Maze chase | Ghost AI, pellet eating, power pellets, tunnels |
| 16 | Centipede | Mushroom field | Segmented enemies, mushrooms, multi-threats |

**Technical Progression:**
- Tiers 1-4: Sprite basics, simple collision, arrays
- Tiers 5-8: Physics, scrolling, multiple object types
- Tiers 9-12: Isometric views, grid systems, advanced collision
- Tiers 13-16: Platforming, AI, complex multi-element games

---

## Tier 1: Pong (Lessons 1-32)

**Goal:** Build 2-player Pong with paddles, ball, collision, and scoring.

**Why this game:** Simplest possible complete game. Introduces sprites, joystick, collision, and game loop without overwhelming complexity.

**Game Requirements:**
- 2 paddles (sprites) controlled by joystick ports 1 & 2
- Ball (sprite) that bounces off paddles and walls
- Score display for both players
- Ball resets when it goes off screen
- First to 11 points wins

**Skills Introduced:**
- Your first assembly program
- Your first sprite
- VIC-II sprite registers ($D000-$D01E, $D015, $D027)
- Joystick reading (CIA $DC00)
- Simple collision detection (overlapping rectangles)
- Game loop structure
- Score tracking and display
- Simple sound effects (SID $D400)

### Lesson Structure Preview

**Lessons 1-8: Assembly and Your First Sprite**
- L1-2: Assembly basics (LDA, STA, LDX, STX)
- L3-4: Memory layout, sprite data location
- L5-6: Sprite shape design (24×21 pixels)
- L7-8: Enable sprite, set position and color

**Lessons 9-16: Movement and Input**
- L9-10: Joystick reading basics
- L11-12: Paddle movement (up/down)
- L13-14: Ball movement (velocity)
- L15-16: Screen boundaries

**Lessons 17-24: Collision and Game Logic**
- L17-18: Ball-paddle collision detection
- L19-20: Ball bounce physics
- L21-22: Ball-wall collision
- L23-24: Scoring when ball goes off screen

**Lessons 25-32: Polish and Completion**
- L25-26: Score display
- L27-28: Ball reset and serve
- L29-30: Win condition (first to 11)
- L31: Simple sound effects
- L32: Game over screen

### Example Code Pattern (Lesson 10)

```assembly
; Read joystick port 2 (player 1)
MOVE_PADDLE_1:
    LDA $DC00       ; CIA port A
    AND #$01        ; Check UP bit
    BEQ MOVE_P1_UP  ; If 0, joystick up

    LDA $DC00
    AND #$02        ; Check DOWN bit
    BEQ MOVE_P1_DOWN
    RTS

MOVE_P1_UP:
    LDA $D001       ; Sprite 0 Y position
    SEC
    SBC #2          ; Move up by 2 pixels
    STA $D001
    RTS

MOVE_P1_DOWN:
    LDA $D001
    CLC
    ADC #2          ; Move down by 2 pixels
    STA $D001
    RTS
```

---

## Tier 2: Breakout (Lessons 33-64)

**Goal:** Build Breakout with paddle, ball, brick array, and power-ups.

**Skills Introduced:**
- Arrays of objects (brick grid)
- Character-based graphics for bricks
- Point-to-brick mapping (screen coordinates → brick array)
- Bounce angle based on paddle hit position
- Lives system
- Level progression
- Power-up system

---

## Tier 3: Space Invaders (Lessons 65-96)

**Goal:** Build Space Invaders with enemy grid, shields, and player cannon.

**Skills Introduced:**
- Grid-based enemy formations
- Formation movement (all enemies move together)
- Multiple bullet management (object pooling)
- Shield destruction (character erosion)
- Dynamic difficulty (speed increases)

---

## Tier 4: Galaxian (Lessons 97-128)

**Goal:** Build Galaxian with diving enemies and attack waves.

**Skills Introduced:**
- Individual enemy AI (state machines)
- Swooping flight paths (Bézier-like curves)
- Formation management (enemies leave and return)
- Attack wave patterns

---

## Tier 5: Asteroids (Lessons 129-160)

**Goal:** Build Asteroids with rotation, momentum, wrapping, and splitting.

**Skills Introduced:**
- Sprite rotation (8 directions)
- Momentum physics (velocity persists)
- Screen wrapping
- Object splitting (1 large → 2 medium)
- Sine/cosine approximation

---

## Tier 6: Missile Command (Lessons 161-192)

**Goal:** Build Missile Command with trajectory targeting and explosions.

**Skills Introduced:**
- Trajectory calculation (point A → point B)
- Explosion animation (expanding circle)
- Multiple simultaneous projectiles
- Defensive gameplay
- Resource management

---

## Tier 7: Defender (Lessons 193-224)

**Goal:** Build Defender with side-scrolling, radar, and rescue.

**Skills Introduced:**
- **Smooth horizontal scrolling**
- Hardware scrolling registers ($D016)
- Radar/minimap rendering
- Enemy variety
- Rescue mechanics

---

## Tier 8: Scramble (Lessons 225-256)

**Goal:** Build Scramble with terrain-following and fuel system.

**Skills Introduced:**
- Terrain representation (height map)
- Terrain collision
- Resource management (fuel)
- Auto-scrolling
- Bombing mechanics

---

## Tier 9: Zaxxon (Lessons 257-288)

**Goal:** Build Zaxxon with isometric view and altitude system.

**Skills Introduced:**
- Isometric graphics (diamond projection)
- Altitude as gameplay variable
- Shadow positioning
- 3D-style collision (altitude-aware)

---

## Tier 10: Dig Dug (Lessons 289-320)

**Goal:** Build Dig Dug with tunnel digging and enemy inflation.

**Skills Introduced:**
- Dynamic playfield modification
- Grid-based digging
- Unique weapon mechanic (inflation)
- Falling object physics
- Enemy pathfinding through tunnels

---

## Tier 11: Q*bert (Lessons 321-352)

**Goal:** Build Q*bert with isometric hopping and color-changing tiles.

**Skills Introduced:**
- Diamond/hex grid navigation
- Isometric hopping physics
- Tile state changes
- Grid-based pathfinding (Coily AI)

---

## Tier 12: Frogger (Lessons 353-384)

**Goal:** Build Frogger with lane-crossing and moving platforms.

**Skills Introduced:**
- Lane-based movement
- Moving platforms (logs, turtles)
- Platform riding
- Periodic state changes
- Time limit pressure

---

## Tier 13: Donkey Kong (Lessons 385-416)

**Goal:** Build Donkey Kong with jumping, ladders, and multiple screens.

**Skills Introduced:**
- **Jump physics (gravity, apex)**
- Ladder climbing
- Platform collision
- Rolling object physics
- Multi-screen games

---

## Tier 14: Mario Bros (Lessons 417-448)

**Goal:** Build Mario Bros arena platformer with POW block and 2-player.

**Skills Introduced:**
- Arena platforming (bounded space)
- Platform wraparound
- Enemy phase system (normal → flipped → defeated)
- Kick mechanic
- POW block (affects all entities)
- 2-player simultaneous

---

## Tier 15: Pac-Man (Lessons 449-480)

**Goal:** Build Pac-Man with ghost AI and maze navigation.

**Skills Introduced:**
- **Maze representation (grid)**
- **Pathfinding AI (ghost chasing)**
- State-based AI (mode changes)
- Individual AI personalities (4 different targeting strategies)
- Pellet management (240 pellets)

---

## Tier 16: Centipede (Lessons 481-512)

**Goal:** Build Centipede with segmented enemies and mushroom field.

**Skills Introduced:**
- **Segmented enemy (chain of sprites)**
- Multi-element game (many systems interacting)
- Complex enemy behaviors (4 enemy types)
- Mushroom field management
- Segments becoming independent centipedes
- Everything Phase 1 synthesized

---

## Phase 1 Outcome

Students have built **16 complete arcade games** and mastered:

**Assembly Language:**
- All common 6510 instructions
- All addressing modes
- Loops, branches, subroutines
- Binary math, bit manipulation

**VIC-II:**
- Sprite basics (enable, position, color, multi-color)
- Sprite collision detection
- Simple raster effects
- Character graphics
- Screen memory manipulation

**CIA:**
- Joystick reading (both ports)
- Keyboard scanning
- Basic timer usage

**SID:**
- Simple sound effects
- Tone generation

**Game Development:**
- Game loop architecture
- State management
- Collision detection (AABB)
- Physics (velocity, acceleration, gravity, bouncing)
- Array management
- Score and lives systems
- AI basics (pathfinding, state machines)
- Multi-element games

**Ready for Phase 2:** Students are prepared to tackle more complex action games with advanced combat systems, sophisticated AI, and professional-quality animation.

---

**Version:** 3.0
**Date:** 2025-10-20
**Status:** Complete restructure for 512-lesson phase
**Focus:** 16 arcade classics building from Pong to Centipede
