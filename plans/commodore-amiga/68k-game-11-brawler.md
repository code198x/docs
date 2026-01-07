# Brawler: 128-Unit Outline

**Game:** 11 of 16 (68000 Assembly)
**Platform:** Commodore Amiga
**Language:** 68000 Assembly
**Units:** 128 (8 phases)
**Concept:** Side-scrolling beat 'em up with Y-depth sorting.

---

## Why This Game Eleventh?

Brawler introduces pseudo-3D depth sorting:

1. **Y-axis depth sorting** - Painter's algorithm
2. **Large sprite animation** - Multi-frame combat
3. **Combo systems** - Attack chains
4. **Two-player cooperative** - Simultaneous play
5. **Multiple enemy coordination** - Group AI

The foundation for isometric games later.

---

## Skills Applied from Previous Games

| Skill | From | Application |
|-------|------|-------------|
| Scrolling | Wanderer | Stage progression |
| Large BOBs | All | Characters |
| Enemy AI | All | Combat behaviours |
| Object management | All | Multiple entities |
| Animation | All | Combat frames |

## New Skills Introduced

| Skill | Phase | Description |
|-------|-------|-------------|
| Y-depth sorting | 1 | Draw order |
| Large animations | 2 | Many frames |
| Combo system | 3 | Attack chains |
| Two-player | 5 | Cooperative |
| Group AI | 4 | Enemy coordination |

---

## Phase 1: Depth Sorting (Units 1-16)
*Y-axis draw order system.*

### Units 1-4: Sorting Concept
- **Unit 1:** Depth concept - Y position = depth
- **Unit 2:** Draw order - far to near
- **Unit 3:** Painter's algorithm - back first
- **Unit 4:** Sorting array - entity list

### Units 5-8: Sort Implementation
- **Unit 5:** Entity structure - X, Y, sprite
- **Unit 6:** Sort routine - by Y position
- **Unit 7:** Efficient sort - insertion sort
- **Unit 8:** Drawing in order - sorted list

### Units 9-12: Movement Plane
- **Unit 9:** Movement area - play zone
- **Unit 10:** X movement - left/right
- **Unit 11:** Y movement - up/down (depth)
- **Unit 12:** Combined movement - 8-directional

### Units 13-16: Basic Display
- **Unit 13:** Player sprite - fighter
- **Unit 14:** Enemy sprites - basic thugs
- **Unit 15:** Depth sorting demo
- **Unit 16:** Multiple entities sorted

**Phase Goal:** Working depth sorting.

---

## Phase 2: Character Animation (Units 17-32)
*Large sprite animation sets.*

### Units 17-20: Animation System
- **Unit 17:** Animation state - current action
- **Unit 18:** Frame sequences - per state
- **Unit 19:** Frame timing - animation speed
- **Unit 20:** State transitions - between actions

### Units 21-24: Player Animations
- **Unit 21:** Idle animation - standing
- **Unit 22:** Walk animation - movement
- **Unit 23:** Attack animations - punches, kicks
- **Unit 24:** Hit/death animations - reactions

### Units 25-28: Enemy Animations
- **Unit 25:** Enemy idle - waiting
- **Unit 26:** Enemy walk - approach
- **Unit 27:** Enemy attack - strike
- **Unit 28:** Enemy defeat - knockdown

### Units 29-32: Animation Polish
- **Unit 29:** Direction facing - flip
- **Unit 30:** Animation blending - smooth
- **Unit 31:** Animation priority - interrupt
- **Unit 32:** Animation demo - full set

**Phase Goal:** Complete animation system.

---

## Phase 3: Combat System (Units 33-48)
*Melee combat mechanics.*

### Units 33-36: Basic Attacks
- **Unit 33:** Punch attack - button A
- **Unit 34:** Kick attack - button B
- **Unit 35:** Attack hitboxes - collision
- **Unit 36:** Attack damage - enemy HP

### Units 37-40: Combo System
- **Unit 37:** Combo concept - chain attacks
- **Unit 38:** Combo timing - input window
- **Unit 39:** Combo chains - punch-punch-kick
- **Unit 40:** Combo finishers - knockdown

### Units 41-44: Special Moves
- **Unit 41:** Jump attack - aerial
- **Unit 42:** Grab attack - throw
- **Unit 43:** Special attack - powerful
- **Unit 44:** Crowd clear - area attack

### Units 45-48: Damage System
- **Unit 45:** Player health - HP bar
- **Unit 46:** Enemy health - per enemy
- **Unit 47:** Knockback - on hit
- **Unit 48:** Invincibility - post-damage

**Phase Goal:** Full combat system.

---

## Phase 4: Enemy AI (Units 49-64)
*Group coordination.*

### Units 49-52: Individual AI
- **Unit 49:** AI states - approach, attack, retreat
- **Unit 50:** Distance checking - to player
- **Unit 51:** Attack decisions - when to strike
- **Unit 52:** Reaction time - not instant

### Units 53-56: Group AI
- **Unit 53:** Group concept - coordinated attacks
- **Unit 54:** Attack slots - limit simultaneous
- **Unit 55:** Surround behaviour - flanking
- **Unit 56:** Group retreat - when damaged

### Units 57-60: Enemy Types
- **Unit 57:** Thug - basic melee
- **Unit 58:** Brawler - heavy hitter
- **Unit 59:** Knife enemy - fast/dangerous
- **Unit 60:** Boss - large, multi-phase

### Units 61-64: Spawning
- **Unit 61:** Spawn triggers - scrolling
- **Unit 62:** Wave spawning - groups
- **Unit 63:** Spawn positions - off-screen
- **Unit 64:** Enemy limits - performance

**Phase Goal:** Coordinated enemy AI.

---

## Phase 5: Two-Player Mode (Units 65-80)
*Cooperative gameplay.*

### Units 65-68: Second Player
- **Unit 65:** Player 2 character - different design
- **Unit 66:** Player 2 controls - port 2
- **Unit 67:** Player 2 animations - full set
- **Unit 68:** Independent actions

### Units 69-72: Cooperative Mechanics
- **Unit 69:** Shared screen - both visible
- **Unit 70:** Scroll management - average position
- **Unit 71:** Friendly fire - option
- **Unit 72:** Revive mechanic - help downed partner

### Units 73-76: Balancing
- **Unit 73:** Two-player enemy count - more enemies
- **Unit 74:** Health distribution - shared pool
- **Unit 75:** Score sharing - or individual
- **Unit 76:** Two-player testing

### Units 77-80: Lives and Continues
- **Unit 77:** Shared lives - pool
- **Unit 78:** Continue system - credits
- **Unit 79:** Game over - both out
- **Unit 80:** Cooperative complete

**Phase Goal:** Two-player cooperative.

---

## Phase 6: Stage Design (Units 81-96)
*Complete stages.*

### Units 81-84: Stage Structure
- **Unit 81:** Stage scrolling - right movement
- **Unit 82:** Stage barriers - fight zones
- **Unit 83:** Stage length - duration
- **Unit 84:** Stage progression

### Units 85-88: Stage 1
- **Unit 85:** Street theme - urban
- **Unit 86:** Street enemies - thugs
- **Unit 87:** Street hazards - breakables
- **Unit 88:** Street boss

### Units 89-92: Stage 2
- **Unit 89:** Warehouse theme - industrial
- **Unit 90:** Warehouse enemies - workers
- **Unit 91:** Warehouse features - crates
- **Unit 92:** Warehouse boss

### Units 93-96: Stage 3
- **Unit 93:** Rooftop theme - finale
- **Unit 94:** Rooftop enemies - elite
- **Unit 95:** Rooftop hazards - edges
- **Unit 96:** Final boss

**Phase Goal:** Three complete stages.

---

## Phase 7: Items and Polish (Units 97-112)
*Pickups and presentation.*

### Units 97-100: Weapon Pickups
- **Unit 97:** Pipe weapon - extended range
- **Unit 98:** Knife weapon - fast attack
- **Unit 99:** Weapon durability - breaks
- **Unit 100:** Weapon drop - on hit

### Units 101-104: Other Pickups
- **Unit 101:** Health food - restore HP
- **Unit 102:** Extra life - 1-up
- **Unit 103:** Points items - score
- **Unit 104:** Pickup spawning - from enemies, breakables

### Units 105-108: Presentation
- **Unit 105:** Title screen
- **Unit 106:** Stage intro - "Stage 1"
- **Unit 107:** Game over screen
- **Unit 108:** Ending sequence

### Units 109-112: Audio
- **Unit 109:** Stage music - per stage
- **Unit 110:** Boss music
- **Unit 111:** Hit sounds - variety
- **Unit 112:** Voice samples - shouts

**Phase Goal:** Polished game.

---

## Phase 8: Release (Units 113-128)
*Testing and release.*

### Units 113-116: Balance
- **Unit 113:** Difficulty curve
- **Unit 114:** Combo balance
- **Unit 115:** Enemy balance
- **Unit 116:** Boss balance

### Units 117-120: Testing
- **Unit 117:** Single-player test
- **Unit 118:** Two-player test
- **Unit 119:** Edge cases
- **Unit 120:** Performance

### Units 121-124: Optimisation
- **Unit 121:** Sort optimisation
- **Unit 122:** Blitter optimisation
- **Unit 123:** AI optimisation
- **Unit 124:** Overall tuning

### Units 125-128: Release
- **Unit 125:** Credits
- **Unit 126:** Documentation
- **Unit 127:** Final testing
- **Unit 128:** Release build - ADF

**Phase Goal:** Complete beat 'em up.

---

## Summary

**Brawler** teaches depth sorting and cooperative play.

### Technical Specifications

- **Display:** Single playfield, 320×256
- **Depth:** Y-sorting painter's algorithm
- **Players:** 1-2 cooperative
- **Characters:** Large animated sprites (30+ frames)
- **Combat:** Combo system, special moves
- **Enemies:** 4+ types with group AI
- **Stages:** 3 with bosses
- **Weapons:** Pipe, knife pickups
- **Audio:** MOD music, voice samples
- **Distribution:** Bootable ADF

### Skills for Next Game

- Depth sorting algorithms
- Large animation sets
- Combo systems
- Two-player handling
- Group AI coordination
