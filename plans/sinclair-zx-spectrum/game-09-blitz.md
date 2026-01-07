# Blitz: 64-Unit Outline

**Game:** 9 of 16
**Platform:** ZX Spectrum
**Units:** 64 (4 phases)
**Concept:** Side-scrolling shooter. Fly through scrolling terrain, destroy enemies, survive the assault.

---

## Why This Game Ninth?

Blitz introduces horizontal scrolling - a major technical advancement:

1. **Horizontal scrolling** - Smooth terrain scrolling
2. **Scroll-relative positioning** - Objects in world space
3. **Terrain generation** - Procedural or data-driven landscapes
4. **Parallax layers** - Depth through different scroll speeds
5. **Wave timing** - Enemies relative to scroll position

This is the first scrolling game, preparing for scrolling platformers.

---

## Skills Applied from Previous Games

| Skill | From | Application in Blitz |
|-------|------|---------------------|
| Object arrays | Skyfire | Enemies, bullets |
| Sprite masking | Skyfire | Clean sprite overlaps |
| Projectile management | Skyfire | Player/enemy bullets |
| Movement patterns | Skyfire | Enemy behaviours |
| Collision detection | All | Terrain, enemies |
| Frame timing | All | Scroll speed control |

## New Skills Introduced

| Skill | Phase | Description |
|-------|-------|-------------|
| Horizontal scrolling | 1 | Moving play field |
| Tile-based terrain | 1 | Scrolling tile map |
| World coordinates | 2 | Position relative to scroll |
| Screen-relative sprites | 2 | Converting world to screen |
| Terrain collision | 2 | Hitting the ground/ceiling |
| Parallax scrolling | 3 | Background layers |
| Scroll-triggered spawns | 3 | Enemies at scroll positions |
| Power-up drops | 4 | Enemy loot |

---

## Phase 1: Scrolling Foundation (Units 1-16)
*Horizontal scrolling terrain.*

### Units 1-4: Terrain Data
- **Unit 1:** Tile-based terrain - terrain as tile columns
- **Unit 2:** Terrain tile set - ground, ceiling, obstacles
- **Unit 3:** Level data format - column-by-column terrain
- **Unit 4:** Terrain colouring - attribute variety

### Units 5-8: Scrolling Engine
- **Unit 5:** Scroll position - current view offset
- **Unit 6:** Character scrolling - scroll by 8 pixels
- **Unit 7:** Pixel scrolling - smooth sub-character scroll
- **Unit 8:** Complete scroll - seamless terrain movement

### Units 9-12: Player Ship
- **Unit 9:** Ship sprite - fighter design
- **Unit 10:** Ship movement - 8-way control
- **Unit 11:** Ship bounds - keep on screen
- **Unit 12:** Ship on scrolling background - layered display

### Units 13-16: Basic Flight
- **Unit 13:** Auto-scroll - terrain moves continuously
- **Unit 14:** Scroll speed control - base speed setting
- **Unit 15:** Terrain variation - changing landscape
- **Unit 16:** Playable foundation - fly through terrain

**Phase Goal:** Smooth horizontal scrolling with player ship.

---

## Phase 2: Combat and Collision (Units 17-32)
*Shooting and terrain collision.*

### Units 17-20: Player Weapons
- **Unit 17:** Bullet spawning - fire from ship position
- **Unit 18:** Bullet movement - scroll-relative travel
- **Unit 19:** Bullet pool - manage active bullets
- **Unit 20:** Rapid fire - hold to continue firing

### Units 21-24: Terrain Collision
- **Unit 21:** Ship hitbox - collision bounds
- **Unit 22:** Terrain collision check - ship hits ground/ceiling
- **Unit 23:** Death on terrain - instant destruction
- **Unit 24:** Narrow passages - precision flying required

### Units 25-28: Enemies
- **Unit 25:** Enemy types - ground, air, stationary
- **Unit 26:** Enemy spawning - appear at scroll positions
- **Unit 27:** Enemy movement - patterns relative to scroll
- **Unit 28:** Enemy-bullet collision - destroy enemies

### Units 29-32: Enemy Attacks
- **Unit 29:** Enemy bullets - shoot at player
- **Unit 30:** Player damage - hit by enemy fire
- **Unit 31:** Lives system - multiple attempts
- **Unit 32:** Complete combat - shooting gallery gameplay

**Phase Goal:** Full combat with terrain and enemy collision.

---

## Phase 3: Polish and Features (Units 33-48)
*Parallax, waves, and enhancements.*

### Units 33-36: Parallax Background
- **Unit 33:** Background layer - slower scrolling layer
- **Unit 34:** Star field - distant background
- **Unit 35:** Layer composition - foreground, midground, background
- **Unit 36:** Depth effect - parallax creates depth

### Units 37-40: Wave System
- **Unit 37:** Wave definitions - enemy formations
- **Unit 38:** Wave triggers - spawn at scroll positions
- **Unit 39:** Wave patterns - coordinated enemy entry
- **Unit 40:** Boss markers - end-of-section challenges

### Units 41-44: Sound Effects
- **Unit 41:** Engine sound - continuous hum
- **Unit 42:** Fire sound - weapon discharge
- **Unit 43:** Explosion sound - enemy destroyed
- **Unit 44:** Death sound - player destroyed

### Units 45-48: Visual Effects
- **Unit 45:** Explosion animation - enemy destruction
- **Unit 46:** Ship thrust - engine animation
- **Unit 47:** Bullet trails - enhanced projectiles
- **Unit 48:** Screen shake - impact feedback

**Phase Goal:** Polished shooter with parallax and effects.

---

## Phase 4: Levels and Release (Units 49-64)
*Level variety and completion.*

### Units 49-52: Level Structure
- **Unit 49:** Level 1 - open terrain, basic enemies
- **Unit 50:** Level 2 - cave sections, more enemies
- **Unit 51:** Level 3 - complex terrain, advanced enemies
- **Unit 52:** Level progression - advance after boss

### Units 53-56: Power-ups
- **Unit 53:** Power-up drops - enemies drop items
- **Unit 54:** Weapon upgrades - spread shot, rapid fire
- **Unit 55:** Shield power-up - temporary protection
- **Unit 56:** Power-up management - current upgrade state

### Units 57-60: Presentation
- **Unit 57:** Title screen - game logo
- **Unit 58:** Level intro - stage name display
- **Unit 59:** Boss warning - alert before boss
- **Unit 60:** Victory screen - level complete

### Units 61-64: Release
- **Unit 61:** Instructions display
- **Unit 62:** Difficulty settings - easy, normal, hard
- **Unit 63:** Balance testing - enemy placement
- **Unit 64:** Release build - final TAP file

**Phase Goal:** Complete side-scrolling shooter.

---

## Summary

**Blitz** teaches horizontal scrolling fundamentals:

**Phase 1 (Scrolling):** Tile-based terrain, smooth scrolling.

**Phase 2 (Combat):** Shooting, terrain collision, enemies.

**Phase 3 (Polish):** Parallax, waves, effects.

**Phase 4 (Levels):** Level variety, power-ups, release.

### Skills Transferred Forward

1. **Horizontal scrolling** → Scrolling platformers, racing games
2. **World coordinates** → All scrolling games
3. **Parallax layers** → Depth in 2D games
4. **Terrain collision** → Platformers, any terrain games
5. **Scroll-triggered events** → Scripted sequences
6. **Power-up systems** → Upgrades in action games

### Technical Notes

The Spectrum's attribute system makes smooth scrolling challenging - colour clash can occur when scrolling. Solutions include:

1. **Monochrome scrolling** - Single colour avoids clash
2. **Character-aligned scrolling** - Scroll by 8 pixels only
3. **Attribute-aware design** - Design terrain to minimise clash

Blitz uses a combination: smooth pixel scrolling with carefully designed terrain that minimises attribute boundaries.

### Game Specifications

- **Scroll:** Horizontal, auto-scroll with player influence
- **Terrain:** Tile-based, procedural elements
- **Player:** 16×16 ship, 8-way movement
- **Weapons:** Primary + upgrades (spread, rapid)
- **Enemies:** 8+ types with different behaviours
- **Levels:** 4 distinct stages
- **Bosses:** End-of-level challenges
- **Lives:** 3
- **Power-ups:** Weapon, shield, bonus
- **Controls:** 8-way + fire
- **Audio:** Beeper effects
- **Distribution:** TAP file
