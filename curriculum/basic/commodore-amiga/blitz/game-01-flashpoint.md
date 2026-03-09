# Blitz Game 01: Flashpoint

**Track:** Blitz Basic 2
**Genre:** Fast-paced arena action
**Units:** 64 (4 phases × 16 units)
**Language:** Blitz Basic 2
**Max lines:** ~500

---

## Premise

A fast-paced arena shooter demonstrating compiled Blitz speed from the start. Enemies spawn from the edges, the player shoots in all directions, power-ups drop, the screen fills with action. The compiled executable runs noticeably faster than equivalent AMOS code — same hardware, different tool, measurably different result.

---

## Core Mechanics

### The Arena

A fixed-screen arena (no scrolling). Walls around the edges. The player in the centre. Enemies spawn from doors/gaps in the walls. The player moves in 8 directions and fires in the direction they're moving (or last moved).

### Speed as the Point

The game is deliberately designed to show what compiled code can do: 30+ simultaneous objects (player, bullets, enemies, particles), smooth movement, responsive controls. An equivalent in AMOS would stutter; in Blitz, it's fluid.

### Enemies

| Type | Speed | Behaviour | Points |
|------|-------|-----------|--------|
| Drone | Medium | Moves toward player | 10 |
| Dasher | Fast | Sprints in straight line | 25 |
| Orbiter | Slow | Circles a fixed point | 15 |
| Spawner | Static | Creates drones until destroyed | 50 |
| Tank | Very slow | Takes 3 hits, fires back | 75 |

### Waves

30 waves. Each wave defines enemy spawns over time. Waves get denser and faster. A wave ends when all enemies are destroyed. Brief respite between waves.

---

## Phase Breakdown

### Phase 1: The Engine (Units 1-16)

Blitz environment, display setup, player movement, shooting. Fast from frame one.

| Unit | Title | What the learner builds | Code concepts |
|------|-------|------------------------|---------------|
| 1 | Blitz Basics | BitMap, Slice, Show. Compile and run. The editor, the compiler, the output. | Blitz environment, compilation |
| 2 | Drawing | Cls, Ink, Box, Circle. Draw the arena walls. | Drawing commands, display setup |
| 3 | Shapes | LoadShape or define shapes. Display with Blit/BBlit. Player character on screen. | Shape loading, blitting |
| 4 | Movement | Joyx(1), Joyy(1) for input. Move player shape. Smooth, fast — compiled speed. | Joystick input, position update |
| 5 | VWait and Timing | VWait for frame sync. Consistent 50fps. VBlankCount() for timing. | Frame synchronisation |
| 6 | Double Buffering | Draw to back buffer, swap. No flicker, no tearing. | Double buffer, buffer swap |
| 7 | Bullets | Fire button → bullet shape moves in player's facing direction. Array of active bullets. | Projectile array, lifecycle |
| 8 | Many Bullets | 10+ simultaneous bullets. All moving, all checking bounds. Blitz handles it effortlessly. | Mass object management |
| 9 | One Enemy | A drone shape that moves toward the player. Simple chase: compare positions, move closer. | Enemy AI, chase logic |
| 10 | Collision | ShapeHit or distance check: bullet hits enemy → destroy. Enemy hits player → damage. | Collision detection |
| 11 | Explosions | On enemy death: brief particle burst (4-8 small shapes scatter outward). Compiled speed makes particles smooth. | Particle system |
| 12 | Score and HUD | Score display, lives, wave number. Text rendering in Blitz. | NPrint, Locate, HUD |
| 13 | Enemy Spawning | Enemies spawn from arena edges at timed intervals. Wave data defines spawn timing. | Spawn system, timed events |
| 14 | Five Enemies | Five simultaneous enemies with independent AI. All chasing, all collidable. | Multiple NPC management |
| 15 | Speed Comparison | Count objects per frame. At 15+ objects, measure frame time. Compare to equivalent AMOS code. Blitz wins. | Performance measurement |
| 16 | Arena Polish | Smooth player, responsive shooting, satisfying explosions. The core loop feels tight and fast. | Integration, feel |

### Phase 2: The Swarm (Units 17-32)

Enemy variety, waves, power-ups. The arena fills with action.

| Unit | Title | What the learner builds | Code concepts |
|------|-------|------------------------|---------------|
| 17 | Dashers | Fast enemies that sprint in a straight line. Must be shot before they reach you. | Speed variety, linear movement |
| 18 | Orbiters | Enemies that circle a point. Predictable but block bullet paths. | Orbital movement, SIN/COS |
| 19 | Spawners | Static enemies that create drones. Destroy the spawner to stop the flow. | Spawning enemies, priority targets |
| 20 | Tanks | Slow, multi-hit enemies that fire back. Player must dodge return fire. | Multi-hit enemies, enemy projectiles |
| 21 | Wave Data | NEWTYPE for wave definitions. Each wave: enemy types, counts, spawn delay, speed. | NEWTYPE, structured data |
| 22 | 10 Waves | Design waves 1-10. Escalating from pure drones to mixed types. | Level design |
| 23 | Power-Ups | Dropped by enemies: rapid fire, spread shot, shield, speed boost. NEWTYPE for power-up state. | Power-up system, timed effects |
| 24 | Spread Shot | Power-up: fire 3 bullets in a spread. Triple the firepower, triple the satisfaction. | Multi-bullet fire pattern |
| 25 | Screen Shake | On big explosions: offset the display by ±2 pixels for 3 frames. Compiled code makes this smooth. | Screen shake via display offset |
| 26 | Combo Counter | Kill enemies in quick succession: ×2, ×3, ×4 multiplier. Displayed on screen. Resets after pause. | Combo system, multiplier |
| 27 | Waves 11-20 | Harder waves. Spawners + tanks. More simultaneous enemies. | Mid-game difficulty |
| 28 | Waves 21-30 | Maximum intensity. 20+ enemies on screen. Blitz handles it. | End-game design |
| 29 | Boss Waves | Waves 10, 20, 30: boss enemy (large, multi-hit, pattern attacks). | Boss encounters |
| 30 | MOD Music | Module playback during gameplay. Blitz audio commands. | Music integration |
| 31 | SFX | Sound effects for shots, explosions, power-ups. Channel management alongside music. | Audio mixing |
| 32 | Thirty Waves | Complete wave progression. Balanced, escalating, with three boss encounters. | Content-complete |

### Phase 3-4: Polish and Production (Units 33-64)

Title screen with attract mode, difficulty select, high score table, statistics, visual effects (copper gradients, palette cycling), and final production polish. System-friendly startup/shutdown (OS takeover and restore). Bootable ADF creation. Testing across A500 and A1200.

Key additions:
- Title screen with active arena demo
- Difficulty select (adjusts spawn rates and enemy speed)
- High score table with disk persistence
- Particle effects: more particles, colour variation, trails
- Object count: 30+ simultaneous at peak (compiled speed showcase)
- Bootable ADF executable
- The performance lesson: frame time profiling showing compiled Blitz vs interpreted AMOS

---

## Technical Notes

### NEWTYPE for Entities

```blitz
NEWTYPE .Enemy
  x.q : y.q          ; Position (floating point)
  dx.q : dy.q        ; Velocity
  etype.w             ; Enemy type
  health.w            ; Hit points
  alive.w             ; Active flag
  frame.w             ; Animation frame
End NEWTYPE

Dim enemies.Enemy(50)
```

### Double Buffering

```blitz
BitMap 0, 320, 256, 4    ; Front buffer
BitMap 1, 320, 256, 4    ; Back buffer

Do
  Use BitMap 1            ; Draw to back
  Cls 0
  ; ... draw everything ...

  VWait                   ; Wait for vblank
  Show 1                  ; Swap: back becomes front
  Use BitMap 0            ; Next frame draws to other buffer
  Swap 0, 1              ; Swap buffer IDs
Loop
```

### Compiled Speed

Blitz compiles to native 68000 machine code. A game loop iterating 50 enemies with position updates, collision checks, and rendering runs in ~2ms on a stock A500. The same logic in AMOS takes ~15-20ms. This difference is the entire point of Game 1.

---

## Changelog

- **v1.0 (2026-03-09):** Initial game outline. Replaces old Blitz Game 1 (Reflex) with a fast-paced arena shooter demonstrating compiled speed.
