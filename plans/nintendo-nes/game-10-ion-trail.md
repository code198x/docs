# Ion Trail: 64-Unit Outline

**Game:** 10 of 16
**Platform:** Nintendo Entertainment System
**Units:** 64 (4 phases)
**Concept:** Side-scrolling shooter. Horizontal scroll through space, blast enemies, navigate terrain. Gradius territory - leave a trail of ions.

---

## Why This Game Tenth?

Ion Trail applies scrolling to the shooter genre, completing the foundation:

1. **Shooter scrolling** - Auto-scroll with player control
2. **Terrain collision** - Hitting the environment
3. **Weapon upgrades** - Power-up systems
4. **Enemy waves** - Scroll-triggered spawning
5. **Boss encounters** - End-of-level challenges

This combines scrolling with combat for the final foundation game.

---

## Skills Applied from Previous Games

| Skill | From | Application in Ion Trail |
|-------|------|------------------------|
| Hardware scrolling | Pixel Plains | Auto-scroll background |
| Projectile management | Stellar Barrage | Player bullets |
| Enemy waves | Stellar Barrage | Formation attacks |
| Object pooling | Stellar Barrage | Bullet pools |
| Power-ups | Fracture Point | Weapon upgrades |

## New Skills Introduced

| Skill | Phase | Description |
|-------|-------|-------------|
| Auto-scroll | 1 | Continuous scroll |
| Terrain collision | 2 | Ship vs environment |
| Scroll-triggered spawns | 2 | Enemies at positions |
| Weapon power levels | 3 | Upgrade system |
| Options/pods | 3 | Helper ships |
| Mid-boss encounters | 4 | Mini-boss fights |

---

## Phase 1: Scrolling Shooter (Units 1-16)
*Auto-scrolling background with player.*

### Units 1-4: Auto-Scroll System
- **Unit 1:** Continuous scroll - always moving
- **Unit 2:** Scroll speed - rate control
- **Unit 3:** Background terrain - space environment
- **Unit 4:** Parallax stars - depth layers

### Units 5-8: Player Ship
- **Unit 5:** Ship sprite - fighter craft
- **Unit 6:** 8-way movement - full mobility
- **Unit 7:** Ship boundaries - keep on screen
- **Unit 8:** Ship on scrolling - layered display

### Units 9-12: Basic Combat
- **Unit 9:** Fire button - spawn projectile
- **Unit 10:** Bullet movement - scroll-relative travel
- **Unit 11:** Bullet pool - manage active bullets
- **Unit 12:** Fire rate - shooting speed

### Units 13-16: Play Area
- **Unit 13:** HUD area - score, lives, weapons
- **Unit 14:** Terrain tiles - cave/space elements
- **Unit 15:** Complete display - ship, terrain, stars
- **Unit 16:** Playable foundation - fly and shoot

**Phase Goal:** Auto-scrolling shooter foundation.

---

## Phase 2: Enemies and Terrain (Units 17-32)
*Terrain collision and enemy waves.*

### Units 17-20: Terrain Collision
- **Unit 17:** Terrain data - solid vs empty
- **Unit 18:** Ship collision box - hitbox
- **Unit 19:** Terrain hit detection - ship vs terrain
- **Unit 20:** Death on collision - instant kill

### Units 21-24: Enemy Basics
- **Unit 21:** Enemy types - various ships
- **Unit 22:** Enemy spawning - scroll-triggered
- **Unit 23:** Enemy movement - patterns
- **Unit 24:** Enemy destruction - bullet collision

### Units 25-28: Enemy Attacks
- **Unit 25:** Enemy bullets - shoot at player
- **Unit 26:** Enemy bullet pool - separate pool
- **Unit 27:** Player hit - take damage
- **Unit 28:** Lives system - multiple ships

### Units 29-32: Formations
- **Unit 29:** Formation data - enemy groups
- **Unit 30:** Formation spawn - coordinated entry
- **Unit 31:** Formation patterns - synchronised movement
- **Unit 32:** Wave progression - different formations

**Phase Goal:** Terrain and enemy combat working.

---

## Phase 3: Power-Ups and Weapons (Units 33-48)
*Weapon upgrades and options.*

### Units 33-36: Power-Up System
- **Unit 33:** Power-up drops - from enemies
- **Unit 34:** Power-up types - different icons
- **Unit 35:** Power-up collection - touch to collect
- **Unit 36:** Power meter - accumulating power

### Units 37-40: Weapon Upgrades
- **Unit 37:** Default weapon - basic shot
- **Unit 38:** Spread shot - wide coverage
- **Unit 39:** Laser - piercing beam
- **Unit 40:** Missile - homing projectiles

### Units 41-44: Options/Helpers
- **Unit 41:** Option concept - helper pods
- **Unit 42:** Option positioning - follow player
- **Unit 43:** Option firing - duplicate shots
- **Unit 44:** Multiple options - up to 2

### Units 45-48: Shield and Speed
- **Unit 45:** Shield power-up - temporary protection
- **Unit 46:** Speed power-up - faster movement
- **Unit 47:** Power-down on death - lose upgrades
- **Unit 48:** Balanced progression - fair difficulty

**Phase Goal:** Complete weapon system.

---

## Phase 4: Bosses and Release (Units 49-64)
*Boss encounters and polish.*

### Units 49-52: Boss Fights
- **Unit 49:** Boss structure - large enemy
- **Unit 50:** Boss health bar - visual HP
- **Unit 51:** Boss patterns - attack sequences
- **Unit 52:** Boss defeat - destruction sequence

### Units 53-56: Level Structure
- **Unit 53:** Level sections - themed areas
- **Unit 54:** Mid-boss - mini-boss encounters
- **Unit 55:** Level end - boss arena
- **Unit 56:** Level transition - next stage

### Units 57-60: Audio and Presentation
- **Unit 57:** Fire sounds - weapon effects
- **Unit 58:** Explosion sounds - destruction
- **Unit 59:** Boss music - intense theme
- **Unit 60:** Level music - stage themes

### Units 61-64: Release
- **Unit 61:** Title screen - game logo
- **Unit 62:** Balance testing - difficulty curve
- **Unit 63:** Sprite flicker management
- **Unit 64:** Release build - final iNES ROM

**Phase Goal:** Complete side-scrolling shooter.

---

## Summary

**Ion Trail** combines scrolling and combat for the foundation finale:

**Phase 1 (Scrolling):** Auto-scroll, player ship.

**Phase 2 (Combat):** Terrain, enemies, formations.

**Phase 3 (Weapons):** Power-ups, upgrades, options.

**Phase 4 (Bosses):** Boss fights, release.

### Foundation Phase Complete

Ion Trail completes the 10-game foundation (640 units). Students have learnt:

| Category | Skills |
|----------|--------|
| **PPU** | Nametables, sprites, scrolling |
| **Physics** | Gravity, jumping, collision |
| **Objects** | Arrays, pooling, activation |
| **AI** | Patrol, chase, personalities |
| **Systems** | Score, lives, levels |
| **Data** | Ring buffers, grids, metatiles |

Games 11-16 build on this with larger, more complex projects and mappers.

### Game Specifications

- **Levels:** 4 stages
- **Scroll:** Horizontal auto-scroll
- **Player:** 16×16 ship with options
- **Weapons:** 4 types with upgrades
- **Enemies:** 10+ types
- **Bosses:** 1 per level + mid-bosses
- **Lives:** 3
- **Mapper:** NROM
- **ROM Size:** 32KB PRG + 8KB CHR
- **Controls:** 8-way + A (fire)
- **Audio:** APU effects + music
- **Distribution:** iNES ROM file
