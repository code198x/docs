# Wanderer: 128-Unit Outline

**Game:** 10 of 16 (68000 Assembly)
**Platform:** Commodore Amiga
**Language:** 68000 Assembly
**Units:** 128 (8 phases)
**Concept:** Scrolling platformer. Large world exploration.

---

## Why This Game Tenth?

Wanderer applies scrolling to platformer design:

1. **Horizontal scrolling platformer** - Camera following
2. **Large level data** - Compression techniques
3. **Moving platforms** - Dynamic collision
4. **Parallax backgrounds** - Depth layers
5. **Extended enemy AI** - Complex behaviours

Building on both Ascent and Parallax.

---

## Skills Applied from Previous Games

| Skill | From | Application |
|-------|------|-------------|
| Platformer physics | Ascent | Movement |
| Parallax scrolling | Parallax | Backgrounds |
| Hardware scroll | Parallax | Level display |
| Enemy AI | Multiple | Various behaviours |
| BOB rendering | All | Player, objects |

## New Skills Introduced

| Skill | Phase | Description |
|-------|-------|-------------|
| Camera systems | 1 | Player following |
| Level compression | 2 | RLE/dictionary |
| Moving platforms | 3 | Dynamic collision |
| Checkpoint system | 4 | Progress saving |
| Extended AI | 5 | Complex enemies |

---

## Phase 1: Scrolling Platformer (Units 1-16)
*Camera and basic scrolling.*

### Units 1-4: Camera Concept
- **Unit 1:** Camera position - separate from player
- **Unit 2:** Camera following - track player
- **Unit 3:** Dead zone - no scroll area
- **Unit 4:** Look ahead - scroll direction

### Units 5-8: Scroll Implementation
- **Unit 5:** Single playfield scroll - platformer
- **Unit 6:** Player-relative scroll - smooth
- **Unit 7:** Scroll boundaries - level edges
- **Unit 8:** Tile updates - new columns

### Units 9-12: Player in Scroll
- **Unit 9:** Screen position - player on display
- **Unit 10:** World position - in level
- **Unit 11:** Collision in scroll - world coords
- **Unit 12:** Player/scroll demo

### Units 13-16: Basic Level
- **Unit 13:** Level tiles - platforms, walls
- **Unit 14:** Level rendering - scrolling
- **Unit 15:** Platform collision - with scroll
- **Unit 16:** Scrolling platformer demo

**Phase Goal:** Basic scrolling platformer.

---

## Phase 2: Level Data (Units 17-32)
*Large levels and compression.*

### Units 17-20: Level Structure
- **Unit 17:** Level width - extended size
- **Unit 18:** Tile columns - level data
- **Unit 19:** Level height - vertical extent
- **Unit 20:** Multi-screen levels

### Units 21-24: Data Compression
- **Unit 21:** RLE concept - run-length encoding
- **Unit 22:** RLE implementation - compress tiles
- **Unit 23:** Decompression - on demand
- **Unit 24:** Memory savings - comparison

### Units 25-28: Level Streaming
- **Unit 25:** Streaming concept - load as needed
- **Unit 26:** Column loading - ahead of scroll
- **Unit 27:** Buffer management - ring buffer
- **Unit 28:** Seamless loading

### Units 29-32: Level Design Tools
- **Unit 29:** Level format - data structure
- **Unit 30:** Level building - from data
- **Unit 31:** Level testing - verification
- **Unit 32:** Level 1 complete

**Phase Goal:** Large compressed levels.

---

## Phase 3: Platform Mechanics (Units 33-48)
*Moving and special platforms.*

### Units 33-36: Moving Platforms
- **Unit 33:** Moving platform concept - dynamic
- **Unit 34:** Platform data - path, speed
- **Unit 35:** Platform movement - waypoints
- **Unit 36:** Player on platform - carry

### Units 37-40: Platform Types
- **Unit 37:** Horizontal platforms - left/right
- **Unit 38:** Vertical platforms - up/down
- **Unit 39:** Falling platforms - collapse
- **Unit 40:** One-way platforms - jump through

### Units 41-44: Environmental Hazards
- **Unit 41:** Spike hazards - instant death
- **Unit 42:** Water areas - swimming
- **Unit 43:** Lava/acid - damage zones
- **Unit 44:** Crushing hazards - timed

### Units 45-48: Collectibles
- **Unit 45:** Coins/gems - scattered
- **Unit 46:** Health pickups - restoration
- **Unit 47:** Extra lives - 1-ups
- **Unit 48:** Secret items - hidden

**Phase Goal:** Rich platform mechanics.

---

## Phase 4: Progress System (Units 49-64)
*Checkpoints and saves.*

### Units 49-52: Checkpoint System
- **Unit 49:** Checkpoint concept - respawn points
- **Unit 50:** Checkpoint activation - touch
- **Unit 51:** Checkpoint respawn - on death
- **Unit 52:** Checkpoint visuals - flags

### Units 53-56: Progress Saving
- **Unit 53:** Save data - what to store
- **Unit 54:** Level progress - which complete
- **Unit 55:** Save format - structured
- **Unit 56:** Load/save - disk I/O

### Units 57-60: Level Transitions
- **Unit 57:** Level exit - goal reached
- **Unit 58:** Level select - world map
- **Unit 59:** Level unlocking - progression
- **Unit 60:** World structure - 3 worlds

### Units 61-64: Scoring
- **Unit 61:** Score tracking - collectibles
- **Unit 62:** Time bonus - fast completion
- **Unit 63:** Perfect bonus - 100% items
- **Unit 64:** Score display

**Phase Goal:** Complete progress system.

---

## Phase 5: Enemy System (Units 65-80)
*Extended AI behaviours.*

### Units 65-68: Basic Enemies
- **Unit 65:** Walker enemy - patrol
- **Unit 66:** Flyer enemy - aerial
- **Unit 67:** Jumper enemy - hopping
- **Unit 68:** Shooter enemy - ranged

### Units 69-72: Complex AI
- **Unit 69:** Chase behaviour - follow player
- **Unit 70:** Patrol routes - defined paths
- **Unit 71:** Alert states - notice player
- **Unit 72:** Attack patterns - varied

### Units 73-76: Boss Enemies
- **Unit 73:** World 1 boss - simple pattern
- **Unit 74:** World 2 boss - multi-phase
- **Unit 75:** World 3 boss - complex
- **Unit 76:** Boss arenas - locked scroll

### Units 77-80: Enemy Management
- **Unit 77:** Spawn triggers - in level data
- **Unit 78:** Enemy limits - on screen
- **Unit 79:** Despawn - off screen
- **Unit 80:** Enemy balance

**Phase Goal:** Varied enemy system.

---

## Phase 6: Parallax and Effects (Units 81-96)
*Visual polish.*

### Units 81-84: Parallax Backgrounds
- **Unit 81:** Background layer - slow scroll
- **Unit 82:** Midground layer - medium
- **Unit 83:** Layer separation - design
- **Unit 84:** Depth illusion

### Units 85-88: Visual Effects
- **Unit 85:** Water reflection - Copper
- **Unit 86:** Clouds - scrolling
- **Unit 87:** Weather effects - rain, snow
- **Unit 88:** Day/night - palette

### Units 89-92: Animation Polish
- **Unit 89:** Player animations - full set
- **Unit 90:** Enemy animations - smooth
- **Unit 91:** Effect animations - explosions
- **Unit 92:** Environmental animation

### Units 93-96: Audio
- **Unit 93:** World themes - per world music
- **Unit 94:** Boss music - intense
- **Unit 95:** Sound effects - full set
- **Unit 96:** Audio integration

**Phase Goal:** Polished presentation.

---

## Phase 7: Level Content (Units 97-112)
*Full game content.*

### Units 97-100: World 1
- **Unit 97:** World 1 theme - grassland
- **Unit 98:** World 1 levels - 4 stages
- **Unit 99:** World 1 enemies
- **Unit 100:** World 1 boss

### Units 101-104: World 2
- **Unit 101:** World 2 theme - caves
- **Unit 102:** World 2 levels - 4 stages
- **Unit 103:** World 2 enemies
- **Unit 104:** World 2 boss

### Units 105-108: World 3
- **Unit 105:** World 3 theme - castle
- **Unit 106:** World 3 levels - 4 stages
- **Unit 107:** World 3 enemies
- **Unit 108:** World 3 boss - final

### Units 109-112: Secret Content
- **Unit 109:** Hidden areas - secret rooms
- **Unit 110:** Bonus levels - unlockable
- **Unit 111:** 100% completion - reward
- **Unit 112:** Content complete

**Phase Goal:** Full game content.

---

## Phase 8: Release (Units 113-128)
*Polish and release.*

### Units 113-116: Presentation
- **Unit 113:** Title screen
- **Unit 114:** Intro sequence
- **Unit 115:** Ending sequence
- **Unit 116:** Credits

### Units 117-120: Balance
- **Unit 117:** Difficulty curve
- **Unit 118:** Enemy balance
- **Unit 119:** Platform balance
- **Unit 120:** Overall tuning

### Units 121-124: Testing
- **Unit 121:** Full playthrough
- **Unit 122:** 100% testing
- **Unit 123:** Edge cases
- **Unit 124:** Performance

### Units 125-128: Release
- **Unit 125:** Instructions
- **Unit 126:** Documentation
- **Unit 127:** Final testing
- **Unit 128:** Release build - ADF

**Phase Goal:** Complete platformer.

---

## Summary

**Wanderer** teaches scrolling platformer design.

### Technical Specifications

- **Display:** Single playfield + parallax, 320×256
- **Levels:** 12 stages across 3 worlds
- **Scroll:** Hardware with tile streaming
- **Compression:** RLE level data
- **Platforms:** Static, moving, falling, one-way
- **Enemies:** 8+ types with varied AI
- **Bosses:** 3 world bosses
- **Save:** Checkpoint + disk save
- **Audio:** MOD music per world
- **Distribution:** Bootable ADF

### Skills for Next Game

- Camera following systems
- Level data compression
- Moving platform handling
- Extended enemy AI
- Multi-world structure
