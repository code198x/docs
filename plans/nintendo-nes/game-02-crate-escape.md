# Crate Escape: 64-Unit Outline

**Game:** 2 of 16
**Platform:** Nintendo Entertainment System
**Units:** 64 (4 phases)
**Concept:** Single-screen platformer. Jump between crates in a warehouse, avoid hazards, reach the exit. Classic platformer physics introduction.

---

## Why This Game Second?

Crate Escape introduces platformer physics - gravity, jumping, and platform collision:

1. **Gravity** - Constant downward acceleration
2. **Jump physics** - Initial velocity, arc, landing
3. **Platform collision** - Standing on surfaces
4. **Tile collision** - Using background tiles for collision
5. **Animation states** - Walk, jump, idle

The NES is famous for platformers. This game teaches the physics that power them.

---

## Skills Applied from Previous Game

| Skill | From | Application in Crate Escape |
|-------|------|---------------------------|
| PPU setup | Neon Nexus | Background and sprite display |
| OAM sprites | Neon Nexus | Player character |
| Controller input | Neon Nexus | Movement and jump |
| Collision basics | Neon Nexus | Expanded for platforms |
| NMI timing | Neon Nexus | Frame updates |

## New Skills Introduced

| Skill | Phase | Description |
|-------|-------|-------------|
| Gravity | 1 | Downward velocity increase |
| Jump mechanics | 2 | Initial velocity, arc |
| Platform collision | 2 | Detecting and standing |
| Tile-based collision | 2 | Using nametable for collision |
| Player animation | 3 | Multiple sprite frames |
| Level design | 3 | Layout with tiles |
| Hazards | 3 | Instant-death obstacles |

---

## Phase 1: Level Display (Units 1-16)
*Tile-based level rendering.*

### Units 1-4: Level Structure
- **Unit 1:** Level concept - platforms, hazards, exit
- **Unit 2:** Tile types - empty, solid, hazard, exit
- **Unit 3:** Level data format - byte array of tile references
- **Unit 4:** Metatiles - 2×2 tile blocks for efficiency

### Units 5-8: Level Rendering
- **Unit 5:** Nametable writing - level to screen
- **Unit 6:** Attribute setup - colours per area
- **Unit 7:** Tile graphics - crate, floor, wall tiles
- **Unit 8:** Complete level display - playfield visible

### Units 9-12: Player Setup
- **Unit 9:** Player sprite - warehouse worker
- **Unit 10:** Player positioning - starting location
- **Unit 11:** Player variables - X, Y, velocity
- **Unit 12:** Player on level - character in warehouse

### Units 13-16: Basic Movement
- **Unit 13:** Horizontal input - left/right control
- **Unit 14:** Horizontal velocity - smooth acceleration
- **Unit 15:** Wall collision - stop at solid tiles
- **Unit 16:** Walking player - moves on ground

**Phase Goal:** Player walks around level with wall collision.

---

## Phase 2: Jumping and Gravity (Units 17-32)
*Platformer physics.*

### Units 17-20: Gravity System
- **Unit 17:** Vertical velocity - Y speed variable
- **Unit 18:** Gravity constant - downward acceleration
- **Unit 19:** Falling state - apply gravity when airborne
- **Unit 20:** Terminal velocity - maximum fall speed

### Units 21-24: Ground Detection
- **Unit 21:** Tile lookup - find tile at position
- **Unit 22:** Feet position - check tiles below player
- **Unit 23:** Ground collision - stop falling, stand
- **Unit 24:** Grounded state - track if on ground

### Units 25-28: Jumping
- **Unit 25:** Jump input - button press detection
- **Unit 26:** Jump initiation - initial upward velocity
- **Unit 27:** Jump arc - gravity reduces upward speed
- **Unit 28:** Variable jump - tap vs hold for height

### Units 29-32: Platform Collision
- **Unit 29:** Ceiling collision - bump head, stop rising
- **Unit 30:** Landing detection - transition to grounded
- **Unit 31:** Edge detection - don't catch on edges
- **Unit 32:** Complete physics - smooth platforming

**Phase Goal:** Smooth jumping and landing on platforms.

---

## Phase 3: Game Elements (Units 33-48)
*Hazards, goals, and levels.*

### Units 33-36: Player Animation
- **Unit 33:** Walk cycle - 4-frame animation
- **Unit 34:** Jump frame - airborne sprite
- **Unit 35:** Idle frame - standing still
- **Unit 36:** Animation state machine - which frame when

### Units 37-40: Hazards
- **Unit 37:** Hazard tiles - spikes, fire
- **Unit 38:** Hazard collision - player touches hazard
- **Unit 39:** Death sequence - player defeated
- **Unit 40:** Respawn - restart at beginning

### Units 41-44: Level Goals
- **Unit 41:** Exit tile - level completion point
- **Unit 42:** Exit detection - player reaches exit
- **Unit 43:** Collectibles - optional items for score
- **Unit 44:** Level complete - transition sequence

### Units 45-48: Multiple Levels
- **Unit 45:** Level data array - multiple level layouts
- **Unit 46:** Level loading - switch to new level
- **Unit 47:** Level progression - unlock sequence
- **Unit 48:** All levels playable - 4 complete levels

**Phase Goal:** Complete levels with hazards and goals.

---

## Phase 4: Polish and Release (Units 49-64)
*Sound, presentation, and release.*

### Units 49-52: Audio
- **Unit 49:** Jump sound - pulse channel effect
- **Unit 50:** Land sound - impact feedback
- **Unit 51:** Death sound - failure jingle
- **Unit 52:** Victory sound - level complete fanfare

### Units 53-56: Game Flow
- **Unit 53:** Lives system - 3 attempts
- **Unit 54:** Game over - no lives remaining
- **Unit 55:** Score display - points and lives
- **Unit 56:** Continue system - restart level on death

### Units 57-60: Presentation
- **Unit 57:** Title screen - game logo
- **Unit 58:** Level intro - level number display
- **Unit 59:** Game over screen - final score
- **Unit 60:** Victory screen - all levels complete

### Units 61-64: Release
- **Unit 61:** Instructions screen
- **Unit 62:** Level design refinement
- **Unit 63:** Physics tuning - jump feel
- **Unit 64:** Release build - final iNES ROM

**Phase Goal:** Complete single-screen platformer.

---

## Summary

**Crate Escape** teaches platformer physics fundamentals:

**Phase 1 (Levels):** Tile-based level display.

**Phase 2 (Physics):** Gravity, jumping, platform collision.

**Phase 3 (Game):** Hazards, goals, multiple levels.

**Phase 4 (Polish):** Sound, game flow, release.

### Skills Transferred Forward

1. **Gravity simulation** → All platformers
2. **Jump physics** → Essential for action games
3. **Tile-based collision** → Using background for collision
4. **Player animation** → State-based sprite selection
5. **Level data** → Efficient level storage
6. **Hazard systems** → Danger throughout curriculum

### NES-Specific Learning

| Concept | What Students Learn |
|---------|-------------------|
| Tile collision | Using nametable data for physics |
| Metatiles | Efficient level building |
| Fixed-point | Sub-pixel positioning |
| State machines | Animation and physics states |

### Game Specifications

- **Display:** Single fixed screen per level
- **Levels:** 8 unique layouts
- **Player:** 8×16 sprite with animations
- **Physics:** Gravity, variable jump
- **Hazards:** Spikes, pits
- **Lives:** 3
- **Mapper:** NROM
- **ROM Size:** 16KB PRG + 8KB CHR
- **Controls:** D-pad + A button (jump)
- **Audio:** APU sound effects
- **Distribution:** iNES ROM file
