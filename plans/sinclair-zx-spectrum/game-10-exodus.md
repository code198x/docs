# Exodus: 64-Unit Outline

**Game:** 10 of 16
**Platform:** ZX Spectrum
**Units:** 64 (4 phases)
**Concept:** Scrolling platformer. Run, jump, and fight through side-scrolling levels. Escape the crumbling world.

---

## Why This Game Tenth?

Exodus combines platforming with scrolling - the culmination of foundation skills:

1. **Scrolling platformer** - Gravity and jumping with scrolling world
2. **Camera following** - Scroll tied to player position
3. **Large levels** - Levels bigger than single screen
4. **Enemy AI in scrolling world** - Enemies with world-space behaviour
5. **Checkpoints** - Progress saving within levels

This completes the foundation phase by combining Cavern's platforming with Blitz's scrolling.

---

## Skills Applied from Previous Games

| Skill | From | Application in Exodus |
|-------|------|----------------------|
| Gravity/jumping | Cavern | Core platformer physics |
| Platform collision | Cavern | Standing, landing |
| Tile-based levels | Cavern | Level structure |
| Horizontal scrolling | Blitz | Scrolling world |
| World coordinates | Blitz | Position in large level |
| Object arrays | Skyfire | Enemies, collectibles |
| Collision detection | All | Multiple collision types |

## New Skills Introduced

| Skill | Phase | Description |
|-------|-------|-------------|
| Camera following | 1 | Scroll tracks player |
| Dead zones | 1 | Camera doesn't jerk on small moves |
| Large level maps | 2 | Levels bigger than screen |
| Scroll-aware enemies | 2 | Enemies in world space |
| Checkpoints | 3 | Mid-level restart points |
| Moving platforms | 3 | Platforms that travel |
| Camera boundaries | 3 | Level edges stop scrolling |
| Level streaming | 4 | Loading level chunks |

---

## Phase 1: Scrolling Platformer (Units 1-16)
*Platformer movement with scrolling camera.*

### Units 1-4: Camera System
- **Unit 1:** Camera position - scroll offset tracking
- **Unit 2:** Player-centred camera - scroll follows player
- **Unit 3:** Dead zone - camera tolerance for small movements
- **Unit 4:** Smooth camera - gradual catch-up to player

### Units 5-8: World vs Screen
- **Unit 5:** World coordinates - player position in level
- **Unit 6:** Screen coordinates - converting world to screen
- **Unit 7:** Tile lookup - finding tile at world position
- **Unit 8:** Rendering visible tiles - only draw what's on screen

### Units 9-12: Player Movement
- **Unit 9:** Horizontal movement - left/right in world
- **Unit 10:** Jump mechanics - reusing Cavern physics
- **Unit 11:** World-space collision - collision in world coordinates
- **Unit 12:** Animation while scrolling - walk cycle with camera

### Units 13-16: Basic Level
- **Unit 13:** Extended level data - wider than screen
- **Unit 14:** Level boundaries - left and right edges
- **Unit 15:** Camera bounds - stop at level edges
- **Unit 16:** Playable foundation - scrolling platformer basics

**Phase Goal:** Player runs and jumps through scrolling level.

---

## Phase 2: Enemies and Hazards (Units 17-32)
*Enemies and obstacles in scrolling world.*

### Units 17-20: World-Space Enemies
- **Unit 17:** Enemy world positions - stored in world space
- **Unit 18:** Enemy screen rendering - convert to screen for display
- **Unit 19:** Enemy activation - only update when near camera
- **Unit 20:** Enemy deactivation - sleep when far from camera

### Units 21-24: Enemy Behaviours
- **Unit 21:** Patrol enemy - walks back and forth
- **Unit 22:** Chase enemy - follows player
- **Unit 23:** Jumping enemy - hops toward player
- **Unit 24:** Stationary hazard - spikes, fire

### Units 25-28: Combat
- **Unit 25:** Player attack - jump on enemies or projectile
- **Unit 26:** Enemy damage - enemies hurt player
- **Unit 27:** Health system - multiple hits allowed
- **Unit 28:** Knockback - player pushed back on hit

### Units 29-32: Collectibles
- **Unit 29:** Collectible items - coins, gems
- **Unit 30:** Collection detection - player touches item
- **Unit 31:** World-space persistence - items stay collected
- **Unit 32:** Score tracking - points from collection

**Phase Goal:** Enemies and items in scrolling world.

---

## Phase 3: Advanced Features (Units 33-48)
*Checkpoints, platforms, and polish.*

### Units 33-36: Checkpoint System
- **Unit 33:** Checkpoint markers - locations in level
- **Unit 34:** Checkpoint activation - passing checkpoint
- **Unit 35:** Respawn at checkpoint - restart on death
- **Unit 36:** Checkpoint visuals - flag or indicator

### Units 37-40: Moving Platforms
- **Unit 37:** Platform types - horizontal, vertical, circular
- **Unit 38:** Platform movement - path following
- **Unit 39:** Player on platform - move with platform
- **Unit 40:** Platform timing - synchronised obstacles

### Units 41-44: Sound and Effects
- **Unit 41:** Jump sound - player jumping
- **Unit 42:** Land sound - hitting ground
- **Unit 43:** Collect sound - item pickup
- **Unit 44:** Hurt sound - taking damage

### Units 45-48: Visual Polish
- **Unit 45:** Parallax background - depth layers
- **Unit 46:** Player animations - run, jump, hurt, idle
- **Unit 47:** Enemy animations - movement cycles
- **Unit 48:** Particle effects - dust, sparkles

**Phase Goal:** Polished scrolling platformer with checkpoints.

---

## Phase 4: Levels and Release (Units 49-64)
*Multiple levels and completion.*

### Units 49-52: Level Design
- **Unit 49:** Level 1 - tutorial, basic jumps
- **Unit 50:** Level 2 - enemies introduced
- **Unit 51:** Level 3 - moving platforms
- **Unit 52:** Level 4 - all mechanics combined

### Units 53-56: Progression
- **Unit 53:** Level transitions - completing levels
- **Unit 54:** Lives system - game over on no lives
- **Unit 55:** Continue system - restart from last level
- **Unit 56:** End game sequence - victory screen

### Units 57-60: Presentation
- **Unit 57:** Title screen - game logo
- **Unit 58:** Level intro - stage name/preview
- **Unit 59:** Pause menu - pause functionality
- **Unit 60:** High score display - best scores

### Units 61-64: Release
- **Unit 61:** Instructions screen
- **Unit 62:** Control options - key configuration
- **Unit 63:** Balance testing - difficulty curve
- **Unit 64:** Release build - final TAP file

**Phase Goal:** Complete scrolling platformer.

---

## Summary

**Exodus** combines all foundation skills into a scrolling platformer:

**Phase 1 (Scrolling):** Camera system, world coordinates.

**Phase 2 (Gameplay):** Enemies, hazards, collectibles.

**Phase 3 (Features):** Checkpoints, moving platforms, polish.

**Phase 4 (Levels):** Level variety, progression, release.

### Skills Transferred Forward

1. **Camera following** → All scrolling games
2. **Large level maps** → Open world, exploration
3. **World-space entities** → Standard game architecture
4. **Checkpoint systems** → Progress saving
5. **Moving platforms** → Environmental mechanics
6. **Entity activation** → Performance optimisation

### Foundation Phase Complete

Exodus completes the 10-game foundation phase (640 units total). Students have learnt:

| Category | Skills |
|----------|--------|
| **Display** | Attributes, tiles, sprites, scrolling |
| **Physics** | Gravity, jumping, collision |
| **Entities** | Object arrays, pooling, activation |
| **AI** | Patrol, chase, personalities |
| **Game Systems** | Score, lives, levels, checkpoints |
| **Data** | Ring buffers, grids, world coordinates |

Games 11-16 build on this foundation with larger, more complex projects.

### Game Specifications

- **Levels:** 4 stages, each 4-8 screens wide
- **Player:** 16×16 sprite with full animation set
- **Physics:** Gravity, variable jump, momentum
- **Enemies:** 6+ types with different behaviours
- **Hazards:** Spikes, pits, fire, crushers
- **Collectibles:** Coins, gems, health
- **Checkpoints:** 2-3 per level
- **Lives:** 3
- **Health:** 3 hits per life
- **Controls:** Left, right, jump, attack
- **Audio:** Beeper effects
- **Distribution:** TAP file
