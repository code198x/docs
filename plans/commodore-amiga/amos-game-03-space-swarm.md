# Space Swarm: 64-Unit Outline

**Game:** 3 of 8 (AMOS BASIC)
**Platform:** Commodore Amiga
**Language:** AMOS BASIC
**Units:** 64 (4 phases)
**Concept:** Fixed-screen shooter. Player ship versus descending enemy waves. Classic arcade action.

---

## Why This Game Third?

Space Swarm introduces shooter mechanics:

1. **Projectiles** - Spawning and managing bullets
2. **Enemy formations** - Coordinated movement
3. **Sprite arrays** - Managing multiple objects
4. **Wave progression** - Escalating difficulty
5. **High score persistence** - File operations

Builds on sprites and collision from previous games.

---

## Skills Applied from Previous Games

| Skill | From | Application in Space Swarm |
|-------|------|---------------------------|
| Sprites | Star Catcher | Player, enemies, bullets |
| Collision | Star Catcher | Hit detection |
| Animation | Crate Stack | Ship and explosion |
| Sound effects | Both | Shooting, explosions |
| Score display | Crate Stack | Points system |

## New Skills Introduced

| Skill | Phase | Description |
|-------|-------|-------------|
| Sprite arrays | 1 | Multiple projectiles |
| Object pooling | 1 | Reusing sprites |
| Formation patterns | 2 | Enemy coordination |
| Wave system | 3 | Level progression |
| File I/O | 4 | High score saving |

---

## Phase 1: Player and Projectiles (Units 1-16)
*Ship and shooting mechanics.*

### Units 1-4: Player Ship
- **Unit 1:** Ship sprite - design
- **Unit 2:** Ship movement - left/right
- **Unit 3:** Ship boundaries - screen edges
- **Unit 4:** Ship animation - thrust flame

### Units 5-8: Shooting
- **Unit 5:** Fire button - triggering shots
- **Unit 6:** Bullet sprite - small projectile
- **Unit 7:** Bullet movement - upward travel
- **Unit 8:** Bullet off-screen - cleanup

### Units 9-12: Multiple Bullets
- **Unit 9:** Bullet array - tracking active
- **Unit 10:** Bullet spawning - from ship position
- **Unit 11:** Fire rate limiting - cooldown
- **Unit 12:** Bullet pooling - reuse sprites

### Units 13-16: Shooting Polish
- **Unit 13:** Shoot sound effect
- **Unit 14:** Muzzle flash - visual feedback
- **Unit 15:** Multiple bullet types concept
- **Unit 16:** Shooting demo - player fires

**Phase Goal:** Player shooting bullets.

---

## Phase 2: Enemy Forces (Units 17-32)
*Enemy formations and movement.*

### Units 17-20: Basic Enemies
- **Unit 17:** Enemy sprite - alien design
- **Unit 18:** Enemy positioning - grid formation
- **Unit 19:** Enemy array - tracking all
- **Unit 20:** Enemy display - formation on screen

### Units 21-24: Formation Movement
- **Unit 21:** Horizontal sweep - left/right
- **Unit 22:** Direction reversal - edge hit
- **Unit 23:** Descend step - move down
- **Unit 24:** Formation cohesion - move together

### Units 25-28: Enemy Types
- **Unit 25:** Enemy type 1 - basic
- **Unit 26:** Enemy type 2 - faster
- **Unit 27:** Enemy type 3 - tougher
- **Unit 28:** Formation composition - mixed types

### Units 29-32: Enemy Animation
- **Unit 29:** Enemy animation - wiggle/pulse
- **Unit 30:** Movement animation - frame sync
- **Unit 31:** Visual variety - per type
- **Unit 32:** Formation demo - moving enemies

**Phase Goal:** Animated enemy formation.

---

## Phase 3: Combat and Waves (Units 33-48)
*Hit detection and progression.*

### Units 33-36: Player vs Enemy
- **Unit 33:** Bullet/enemy collision - detection
- **Unit 34:** Enemy destruction - removal
- **Unit 35:** Explosion effect - sprite swap
- **Unit 36:** Explosion sound - audio feedback

### Units 37-40: Enemy vs Player
- **Unit 37:** Enemy reaches bottom - invasion
- **Unit 38:** Enemy projectiles - shooting back
- **Unit 39:** Player hit detection - damage
- **Unit 40:** Player death - explosion, respawn

### Units 41-44: Wave System
- **Unit 41:** Wave complete - all enemies gone
- **Unit 42:** Wave transition - next wave
- **Unit 43:** Wave difficulty - speed increase
- **Unit 44:** Wave variety - different formations

### Units 45-48: Scoring
- **Unit 45:** Points per enemy - by type
- **Unit 46:** Combo bonus - rapid kills
- **Unit 47:** Wave clear bonus
- **Unit 48:** Score display - prominent

**Phase Goal:** Complete combat loop.

---

## Phase 4: Game Structure (Units 49-64)
*High scores, presentation, polish.*

### Units 49-52: High Score System
- **Unit 49:** High score tracking - top 5
- **Unit 50:** OPEN, PRINT#, INPUT# - file I/O
- **Unit 51:** Save high scores - to disk
- **Unit 52:** Load high scores - from disk

### Units 53-56: Game States
- **Unit 53:** Title screen - logo, high scores
- **Unit 54:** Game start - wave 1
- **Unit 55:** Game over - score entry
- **Unit 56:** State machine - transitions

### Units 57-60: Presentation
- **Unit 57:** Starfield background - scrolling
- **Unit 58:** UI elements - lives, wave number
- **Unit 59:** Sound variety - different enemies
- **Unit 60:** Music - gameplay theme

### Units 61-64: Completion
- **Unit 61:** Difficulty options - easy/normal/hard
- **Unit 62:** Two-player alternating
- **Unit 63:** Full testing
- **Unit 64:** Release build

**Phase Goal:** Complete shooter with high scores.

---

## Summary

**Space Swarm** teaches shooter mechanics in AMOS.

### Game Specifications

- **Player:** Ship sprite, horizontal movement
- **Weapons:** Single shot, fire rate limited
- **Enemies:** 3 types in formation
- **Formation:** Classic descending pattern
- **Waves:** Increasing difficulty
- **Scoring:** Points by type, bonuses
- **High Scores:** Top 5, saved to disk
- **Lives:** 3
- **Display:** AMOS screen, sprites
- **Sound:** Shoot, explode, music
- **Distribution:** AMOS source + compiled
