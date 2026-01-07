# Stellar Barrage: 64-Unit Outline

**Game:** 3 of 16
**Platform:** Nintendo Entertainment System
**Units:** 64 (4 phases)
**Concept:** Fixed-screen space shooter. Player ship versus descending enemy waves. Classic Space Invaders-style action.

---

## Why This Game Third?

Stellar Barrage introduces multi-object management - essential for action games:

1. **Multiple sprites** - Managing many objects simultaneously
2. **Projectile systems** - Bullets with pooling
3. **Enemy formations** - Coordinated enemy groups
4. **8-sprite limit** - Managing NES scanline limits
5. **Complex collision** - Bullet vs enemy, enemy vs player

This teaches the object management skills needed for all action games.

---

## Skills Applied from Previous Games

| Skill | From | Application in Stellar Barrage |
|-------|------|------------------------------|
| PPU/sprites | Neon Nexus | Ship, enemies, bullets |
| Controller input | Neon Nexus | Ship movement, fire |
| Collision | Both | Bullet and enemy collision |
| Animation | Crate Escape | Enemy animation |

## New Skills Introduced

| Skill | Phase | Description |
|-------|-------|-------------|
| Object pooling | 1 | Reusing sprite slots |
| Projectile management | 2 | Bullet arrays |
| Enemy formations | 2 | Coordinated movement |
| Sprite flickering | 3 | Managing 8-sprite limit |
| Wave systems | 3 | Enemy group spawning |
| Score display | 4 | Multi-digit numbers |

---

## Phase 1: Ship and Display (Units 1-16)
*Player ship and enemy graphics.*

### Units 1-4: Player Ship
- **Unit 1:** Ship sprite design - player spacecraft
- **Unit 2:** Ship positioning - bottom of screen
- **Unit 3:** Ship movement - left/right control
- **Unit 4:** Ship boundaries - screen edge limits

### Units 5-8: Enemy Graphics
- **Unit 5:** Enemy sprite designs - alien invaders
- **Unit 6:** Enemy animation - 2-frame cycle
- **Unit 7:** Multiple enemy types - different graphics
- **Unit 8:** Enemy colours - palette variety

### Units 9-12: Object Management
- **Unit 9:** Object structure - X, Y, type, active
- **Unit 10:** Enemy array - table of all enemies
- **Unit 11:** Active flags - which objects exist
- **Unit 12:** Draw loop - render all active objects

### Units 13-16: Play Area
- **Unit 13:** Starfield background - simple star pattern
- **Unit 14:** Border and HUD area - reserved space
- **Unit 15:** Complete display - ship, enemies, stars
- **Unit 16:** Playable foundation - move ship around

**Phase Goal:** Display player ship and enemy formation.

---

## Phase 2: Shooting Mechanics (Units 17-32)
*Projectiles and enemy behaviour.*

### Units 17-20: Player Bullets
- **Unit 17:** Bullet structure - position, active flag
- **Unit 18:** Bullet pool - fixed array of bullet slots
- **Unit 19:** Fire input - spawn bullet at ship
- **Unit 20:** Bullet movement - travel upward

### Units 21-24: Bullet Collision
- **Unit 21:** Bullet-enemy collision - hit detection
- **Unit 22:** Enemy destruction - remove on hit
- **Unit 23:** Score increment - points per enemy
- **Unit 24:** Bullet removal - deactivate on hit/edge

### Units 25-28: Enemy Movement
- **Unit 25:** Formation movement - group moves together
- **Unit 26:** Horizontal sweep - left-right pattern
- **Unit 27:** Descend step - drop when hitting edge
- **Unit 28:** Enemy reaching bottom - game over threat

### Units 29-32: Enemy Attacks
- **Unit 29:** Enemy bullet pool - separate from player
- **Unit 30:** Enemy firing - random enemies shoot
- **Unit 31:** Enemy bullet movement - travel downward
- **Unit 32:** Player hit detection - ship destruction

**Phase Goal:** Complete shooting gameplay loop.

---

## Phase 3: Sprite Management (Units 33-48)
*Managing NES sprite limits.*

### Units 33-36: 8-Sprite Limit
- **Unit 33:** Scanline limit concept - hardware constraint
- **Unit 34:** Sprite priority - which sprites show
- **Unit 35:** Flickering technique - rotate priorities
- **Unit 36:** OAM cycling - change sprite order per frame

### Units 37-40: Wave System
- **Unit 37:** Wave data - formation definitions
- **Unit 38:** Wave spawning - create wave at top
- **Unit 39:** Wave completion - all enemies destroyed
- **Unit 40:** Next wave - new formation appears

### Units 41-44: Difficulty Progression
- **Unit 41:** Speed increase - faster each wave
- **Unit 42:** More enemies - larger formations
- **Unit 43:** Faster bullets - increased challenge
- **Unit 44:** Difficulty curve - gradual ramp-up

### Units 45-48: Special Enemies
- **Unit 45:** Bonus enemy - high-value target
- **Unit 46:** Diving enemy - breaks formation
- **Unit 47:** Shielded enemy - takes multiple hits
- **Unit 48:** Enemy variety - mixed formations

**Phase Goal:** Robust sprite management with waves.

---

## Phase 4: Polish and Release (Units 49-64)
*Audio, score, and presentation.*

### Units 49-52: Audio
- **Unit 49:** Fire sound - pulse channel
- **Unit 50:** Explosion sound - noise channel
- **Unit 51:** Player hit sound - damage feedback
- **Unit 52:** Background music - simple loop

### Units 53-56: Score System
- **Unit 53:** Score variables - multi-byte number
- **Unit 54:** Score display - digits on screen
- **Unit 55:** High score - best score tracking
- **Unit 56:** Score table - top scores

### Units 57-60: Presentation
- **Unit 57:** Title screen - game logo
- **Unit 58:** Game over screen - final score
- **Unit 59:** Wave indicator - current wave number
- **Unit 60:** Lives display - remaining ships

### Units 61-64: Release
- **Unit 61:** Instructions screen
- **Unit 62:** Balance testing - difficulty tuning
- **Unit 63:** Sprite flicker optimisation
- **Unit 64:** Release build - final iNES ROM

**Phase Goal:** Complete, polished shooter.

---

## Summary

**Stellar Barrage** teaches multi-object management:

**Phase 1 (Display):** Ship, enemies, object arrays.

**Phase 2 (Combat):** Bullets, collision, enemy behaviour.

**Phase 3 (Sprites):** 8-sprite limit management, waves.

**Phase 4 (Polish):** Audio, scoring, presentation.

### Skills Transferred Forward

1. **Object pooling** → Entity management everywhere
2. **Projectile systems** → Any shooting game
3. **Sprite flickering** → Managing hardware limits
4. **Wave systems** → Enemy spawning patterns
5. **Score display** → Multi-digit number rendering

### NES-Specific Learning

| Concept | What Students Learn |
|---------|-------------------|
| 8-sprite limit | Hardware constraint management |
| OAM cycling | Sprite priority rotation |
| Object pools | Efficient entity management |
| Score rendering | BCD or binary to tiles |

### Game Specifications

- **Display:** Fixed screen
- **Player:** 1 ship at bottom
- **Enemies:** 24-30 per formation
- **Bullets:** 3 player, 4 enemy max
- **Waves:** Progressive difficulty
- **Lives:** 3
- **Mapper:** NROM
- **ROM Size:** 16KB PRG + 8KB CHR
- **Controls:** D-pad + A button (fire)
- **Audio:** APU effects + music
- **Distribution:** iNES ROM file
