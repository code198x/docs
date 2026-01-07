# Parallax Patrol: 128-Unit Outline

**Game:** 13 of 16
**Platform:** Commodore 64
**Units:** 128
**Concept:** Advanced side-scrolling shooter with multi-layer parallax. R-Type/Gradius-style shooter with weapon upgrades, option drones, large levels, and epic boss encounters.

---

## Why 128 Units?

Parallax Patrol is the curriculum's most ambitious horizontal shooter:
1. **Multi-layer parallax** - 3+ layers with coordinated scrolling
2. **Advanced weapon system** - 4 weapon types with upgrade paths
3. **Option drone system** - Gradius-style following weapons with formations
4. **7 complete stages** - Each needs unique terrain, enemies, and boss
5. **Epic boss design** - Multi-phase bosses with complex patterns
6. **Level compression** - RLE compression for long levels
7. **Two-player co-op** - Simultaneous play support
8. **Multiple game modes** - Main game, boss rush, sound test

At 64 units, stages 4-5 were compressed into a single unit and stages 6-7 got only 2 units combined. 128 units allows each stage to be properly designed with appropriate bosses.

---

## Skills Applied from Previous Games

| Skill | Learned In | Application in Parallax Patrol |
|-------|-----------|---------------------------|
| SID fundamentals | SID Symphony | Epic stage music, rich SFX |
| Hardware sprites | Starfield | Ship, enemies, bullets, effects |
| Shooting mechanics | Starfield | Advanced weapon systems |
| Sprite collision | Starfield | Complex combat |
| Custom characters | Maze Raider | Terrain graphics |
| Hardware scrolling | Scroll Runner | Main scroll layer |
| Colour RAM scrolling | Scroll Runner | Coloured terrain |
| Double buffering | Scroll Runner | Smooth updates |
| Basic parallax | Scroll Runner | Foundation for multi-layer |
| Terrain collision | Night Raid | Wall collision |
| Level streaming | Night Raid | Long level data |
| Boss encounters | Night Raid | Epic bosses |
| Sprite multiplexing | Sprite Storm | Many enemies/bullets |
| Raster techniques | Raster Rider | Visual effects, layer separation |
| Power-up systems | Brick Basher | Weapon upgrades |
| Combat systems | Dungeon Crawl | Enemy patterns |
| State machines | Arena Fighter | Boss phases |

## New Skills Introduced

| Skill | Phase | Description |
|-------|-------|-------------|
| Multi-layer parallax | 1 | 3+ coordinated scroll layers |
| Layer raster splitting | 1 | Separate layers via raster |
| Weapon upgrade paths | 3 | Progressive weapon power |
| Option drone system | 4 | Following weapons, formations |
| Level compression | 5 | RLE for long level data |
| Checkpoint system | 5 | Mid-level respawn points |
| Charge shot mechanic | 3 | Held fire for power |
| Pattern-based enemies | 2 | Sine, dive, formation paths |
| Multi-phase bosses | 7 | Evolving boss battles |
| Two-player co-op | 8 | Simultaneous play |

---

## Phase 1: Parallax Foundation (Units 1-16)
*Multi-layer scrolling system.*

### Units 1-4: Project Setup
- **Unit 1:** Advanced shooter concept - analysing R-Type, Gradius, Turrican
- **Unit 2:** Parallax layer architecture - how layers will work together
- **Unit 3:** Memory layout - layers, sprites, level data, music
- **Unit 4:** Main loop structure - layer updates, gameplay, rendering

### Units 5-8: Background Layer
- **Unit 5:** Background layer concept - slowest, most distant
- **Unit 6:** Star field/nebula graphics - simple, effective background
- **Unit 7:** Background scroll implementation - very slow rate
- **Unit 8:** Background colour variation - raster colour effects

### Units 9-12: Middle Layer
- **Unit 9:** Middle layer concept - mid-distance mountains/structures
- **Unit 10:** Silhouette graphics - mountains, buildings, forests
- **Unit 11:** Middle scroll implementation - medium speed
- **Unit 12:** Middle-background coordination - speed ratios

### Units 13-16: Foreground Layer
- **Unit 13:** Foreground layer - main gameplay terrain
- **Unit 14:** Terrain graphics - floors, ceilings, obstacles
- **Unit 15:** Foreground scroll - full speed with gameplay
- **Unit 16:** Three-layer integration - all layers working together

**Phase Goal:** Smooth three-layer parallax scrolling with depth.

---

## Phase 2: Player and Combat (Units 17-32)
*Ship, shooting, and basic enemies.*

### Units 17-20: Player Ship
- **Unit 17:** Ship sprite design - main player craft
- **Unit 18:** Ship data structure - position, state, equipment
- **Unit 19:** 8-direction movement - full control
- **Unit 20:** Screen boundaries and ship animation

### Units 21-24: Basic Shooting
- **Unit 21:** Basic weapon - forward shot
- **Unit 22:** Bullet pool management - efficient allocation
- **Unit 23:** Fire rate control - shots per second
- **Unit 24:** Bullet-terrain collision - destruction on walls

### Units 25-28: Basic Enemies
- **Unit 25:** Enemy framework - spawn, move, destroy
- **Unit 26:** Simple enemy type - flies straight
- **Unit 27:** Wave enemy type - sine wave movement
- **Unit 28:** Dive enemy type - swoops at player

### Units 29-32: Combat Foundation
- **Unit 29:** Enemy-bullet collision - shoot to destroy
- **Unit 30:** Enemy-player collision - death on contact
- **Unit 31:** Lives and score system
- **Unit 32:** HUD display - lives, score, weapon indicator

**Phase Goal:** Playable shooter with parallax, shooting, and enemies.

---

## Phase 3: Weapon Systems (Units 33-48)
*Four weapon types with upgrades.*

### Units 33-36: Weapon Framework
- **Unit 33:** Weapon type system - multiple weapons
- **Unit 34:** Current weapon tracking - selection state
- **Unit 35:** Weapon switching - power-up changes weapon
- **Unit 36:** Weapon level system - upgrade progression

### Units 37-40: Weapon Types
- **Unit 37:** Spread weapon - 3-way/5-way shot
- **Unit 38:** Laser weapon - continuous beam
- **Unit 39:** Missile weapon - homing projectiles
- **Unit 40:** Wave weapon - piercing sine shot

### Units 41-44: Weapon Upgrades
- **Unit 41:** Upgrade power-ups - weapon level increase
- **Unit 42:** Level 1-3 progression - power scaling
- **Unit 43:** Maximum level effects - full power visuals
- **Unit 44:** Weapon balance - damage per type

### Units 45-48: Charge Shot
- **Unit 45:** Charge mechanic - hold fire to charge
- **Unit 46:** Charge levels - 3 power stages
- **Unit 47:** Charge indicators - visual feedback
- **Unit 48:** Charge release - powerful shot

**Phase Goal:** Four distinct weapons with upgrade paths and charge shot.

---

## Phase 4: Power-Ups and Options (Units 49-64)
*Shield, bombs, option drones.*

### Units 49-52: Defensive Power-Ups
- **Unit 49:** Shield power-up - hit absorption
- **Unit 50:** Shield display - visual around ship
- **Unit 51:** Shield depletion - hits reduce shield
- **Unit 52:** Speed power-up - movement speed increase

### Units 53-56: Smart Bomb
- **Unit 53:** Bomb power-up - collect bombs
- **Unit 54:** Bomb stock display - HUD indicator
- **Unit 55:** Bomb activation - screen clear effect
- **Unit 56:** Bomb invulnerability - brief protection

### Units 57-60: Option Drones
- **Unit 57:** Option concept - following weapons
- **Unit 58:** Option following algorithm - trail behind ship
- **Unit 59:** Option fire synchronisation - fire with player
- **Unit 60:** Multiple options - up to 4 drones

### Units 61-64: Option Formations
- **Unit 61:** Formation concept - option positioning
- **Unit 62:** Formation modes - spread, focus, rotate
- **Unit 63:** Formation switching - player control
- **Unit 64:** Option integration - complete system

**Phase Goal:** Full power-up system with options and defensive items.

---

## Phase 5: Early Stages (Units 65-80)
*Stages 1-3 with full content.*

### Units 65-68: Stage 1 - Space
- **Unit 65:** Stage 1 terrain design - asteroid field, debris
- **Unit 66:** Stage 1 enemies - space fighters, turrets
- **Unit 67:** Stage 1 boss - large battleship
- **Unit 68:** Stage 1 integration - complete level

### Units 69-72: Stage 2 - Planet Surface
- **Unit 69:** Stage 2 terrain - alien landscape, caves
- **Unit 70:** Stage 2 enemies - ground cannons, flying creatures
- **Unit 71:** Stage 2 boss - burrowing worm creature
- **Unit 72:** Stage 2 integration - complete level

### Units 73-76: Stage 3 - Underwater
- **Unit 73:** Stage 3 terrain - underwater caverns, coral
- **Unit 74:** Stage 3 enemies - sea creatures, mines
- **Unit 75:** Stage 3 boss - giant sea serpent
- **Unit 76:** Stage 3 integration - complete level

### Units 77-80: Level Systems
- **Unit 77:** Checkpoint system - mid-level respawn
- **Unit 78:** Death and respawn - power loss, restart
- **Unit 79:** Level streaming - loading long levels
- **Unit 80:** Level compression - RLE for terrain data

**Phase Goal:** Three complete stages with bosses and checkpoints.

---

## Phase 6: Later Stages (Units 81-96)
*Stages 4-7 with increasing challenge.*

### Units 81-84: Stage 4 - Mechanical
- **Unit 81:** Stage 4 terrain - factory, machinery
- **Unit 82:** Stage 4 enemies - robots, laser turrets
- **Unit 83:** Stage 4 boss - giant mech walker
- **Unit 84:** Stage 4 integration - complete level

### Units 85-88: Stage 5 - Organic
- **Unit 85:** Stage 5 terrain - living walls, flesh caverns
- **Unit 86:** Stage 5 enemies - biological horrors
- **Unit 87:** Stage 5 boss - alien hive queen
- **Unit 88:** Stage 5 integration - complete level

### Units 89-92: Stage 6 - Final Approach
- **Unit 89:** Stage 6 terrain - enemy fortress exterior
- **Unit 90:** Stage 6 enemies - elite guards, heavy defences
- **Unit 91:** Stage 6 boss - defence commander
- **Unit 92:** Stage 6 integration - complete level

### Units 93-96: Stage 7 - Core
- **Unit 93:** Stage 7 terrain - final fortress interior
- **Unit 94:** Stage 7 enemies - ultimate defences
- **Unit 95:** Final boss design - multi-phase ultimate enemy
- **Unit 96:** Stage 7 integration - complete final level

**Phase Goal:** Four more stages completing the main game.

---

## Phase 7: Bosses and Modes (Units 97-112)
*Boss polish, game modes, UI.*

### Units 97-100: Boss Enhancement
- **Unit 97:** Boss phase system - evolving patterns
- **Unit 98:** Boss health display - segmented bar
- **Unit 99:** Boss defeat sequences - dramatic destruction
- **Unit 100:** Mini-boss encounters - mid-stage challenges

### Units 101-104: Game Modes
- **Unit 101:** Title screen design - impressive presentation
- **Unit 102:** Mode selection menu - game modes
- **Unit 103:** Boss rush mode - sequential boss fights
- **Unit 104:** Time attack mode - speedrun tracking

### Units 105-108: Two-Player Mode
- **Unit 105:** Two-player framework - second ship
- **Unit 106:** Two-player input - port 1 and 2
- **Unit 107:** Two-player display - both ships, shared screen
- **Unit 108:** Co-op balance - enemy scaling

### Units 109-112: Additional Features
- **Unit 109:** Continue system - credits for continues
- **Unit 110:** Difficulty options - Easy/Normal/Hard
- **Unit 111:** High score table - persistent leaderboard
- **Unit 112:** Statistics tracking - kills, deaths, completions

**Phase Goal:** Complete game modes and two-player support.

---

## Phase 8: Polish and Release (Units 113-128)
*Effects, audio, balance, release.*

### Units 113-116: Visual Effects
- **Unit 113:** Hit sparks and explosions
- **Unit 114:** Weapon trail effects - laser glow, missile smoke
- **Unit 115:** Boss explosion sequences - epic destruction
- **Unit 116:** Screen effects - flash, shake, fade

### Units 117-120: Audio Design
- **Unit 117:** Stage music - unique theme per stage
- **Unit 118:** Boss music - intense battle themes
- **Unit 119:** Weapon sounds - distinct per weapon type
- **Unit 120:** Sound test mode - music/SFX access

### Units 121-124: Balance and Polish
- **Unit 121:** Weapon balance - damage curves, utility
- **Unit 122:** Enemy balance - health, patterns, placement
- **Unit 123:** Boss balance - difficulty progression
- **Unit 124:** Stage balance - challenge curve

### Units 125-128: Release
- **Unit 125:** Bug hunting and edge cases
- **Unit 126:** Performance optimisation - smooth 50fps
- **Unit 127:** Demo mode - attract screen gameplay
- **Unit 128:** Release build - final distribution

**Phase Goal:** Complete, polished shooter ready for distribution.

---

## Summary

**Parallax Patrol** at 128 units provides proper depth for a commercial-quality shooter:

**Phase 1 (Parallax):** Three-layer parallax scrolling foundation.

**Phase 2 (Combat):** Ship, shooting, basic enemy encounters.

**Phase 3 (Weapons):** Four weapon types with upgrades and charge shot.

**Phase 4 (Power-Ups):** Shield, bombs, option drones with formations.

**Phase 5 (Early Stages):** Stages 1-3 with unique themes and bosses.

**Phase 6 (Later Stages):** Stages 4-7 completing the main game.

**Phase 7 (Modes):** Boss rush, two-player, difficulty options.

**Phase 8 (Polish):** Effects, audio, balance, release.

### Skills Transferred Forward

The following skills are mastered in Parallax Patrol:

1. **Multi-layer parallax** → Mega Blaster (bidirectional), Symphony's End
2. **Weapon upgrade systems** → Mega Blaster (extensive weapons)
3. **Option drone mechanics** → Mega Blaster (orbiting options)
4. **Large level streaming** → Mega Blaster, Isometric Quest
5. **Checkpoint systems** → All remaining games
6. **Epic multi-phase bosses** → Mega Blaster, Symphony's End
7. **Two-player co-op** → Future multiplayer games

### Comparison: 64 vs 128 Units

| System | 64-Unit Depth | 128-Unit Depth |
|--------|---------------|----------------|
| Parallax setup | 5 units | 12 units |
| Player/combat | 4 units | 16 units |
| Weapon types | 4 units | 12 units |
| Weapon upgrades | 2 units | 4 units |
| Options | 3 units | 8 units |
| Stage 1-3 | 4 units | 12 units |
| Stage 4-7 | 3 units | 16 units |
| Bosses | 2 units | 8 units |
| Two-player | 1 unit | 4 units |
| Polish/release | 8 units | 16 units |

### Game Specifications

- **Parallax layers:** 3+ (background, middle, foreground)
- **Weapons:** 4 types (shot, spread, laser, missile) + wave
- **Weapon levels:** 3 per weapon + charge shot
- **Options:** Up to 4 drones, 3 formations
- **Stages:** 7 complete levels with unique themes:
  - Stage 1: Space/asteroid field
  - Stage 2: Alien planet surface
  - Stage 3: Underwater caverns
  - Stage 4: Mechanical factory
  - Stage 5: Organic/biological
  - Stage 6: Final fortress exterior
  - Stage 7: Final fortress core
- **Bosses:** 7 main bosses + mini-bosses
- **Special moves:** Charge shot (3 levels), smart bomb
- **Players:** 1-2 cooperative
- **Modes:** Main game, boss rush, time attack, sound test
- **Features:** Checkpoints, continues, difficulty options, high scores
