# Blast Zone: 64-Unit Outline

**Game:** 2 of 16 (68000 Assembly)
**Platform:** Commodore Amiga
**Language:** 68000 Assembly
**Units:** 64 (4 phases)
**Concept:** Fixed-screen space shooter. Player ship versus enemy waves.

---

## Why This Game Second?

Blast Zone expands on hardware sprite and Blitter usage:

1. **Sprite multiplexing** - More sprites than hardware allows
2. **BOB management** - Multiple Blitter objects
3. **Projectile pooling** - Efficient object management
4. **Enemy formations** - Coordinated patterns
5. **Blitter text** - Score display

Builds on Signal's foundation with more complex sprite/BOB handling.

---

## Skills Applied from Game 1

| Skill | Application in Blast Zone |
|-------|--------------------------|
| 68000 assembly | Core programming |
| Copper lists | Display setup |
| Hardware sprites | Player ship, enemies |
| Blitter basics | Projectiles, effects |
| Paula audio | Shoot, explode sounds |

## New Skills Introduced

| Skill | Phase | Description |
|-------|-------|-------------|
| Sprite multiplexing | 1 | Copper sprite reuse |
| Object pools | 2 | Bullet management |
| Formation patterns | 3 | Enemy coordination |
| Blitter text | 4 | Score rendering |

---

## Phase 1: Player Ship (Units 1-16)
*Ship control and shooting.*

### Units 1-4: Ship Sprite
- **Unit 1:** Ship design - sprite graphics
- **Unit 2:** Ship display - hardware sprite
- **Unit 3:** Ship movement - left/right
- **Unit 4:** Ship boundaries - screen limits

### Units 5-8: Shooting
- **Unit 5:** Fire button - joystick reading
- **Unit 6:** Bullet sprite - projectile design
- **Unit 7:** Bullet spawning - from ship position
- **Unit 8:** Bullet movement - upward travel

### Units 9-12: Multiple Bullets
- **Unit 9:** Bullet array - tracking active
- **Unit 10:** Bullet pool - reuse inactive
- **Unit 11:** Fire rate - cooldown timing
- **Unit 12:** Off-screen cleanup

### Units 13-16: Ship Polish
- **Unit 13:** Ship animation - thrust effect
- **Unit 14:** Shoot sound - Paula playback
- **Unit 15:** Muzzle flash - visual feedback
- **Unit 16:** Player demo - ship shooting

**Phase Goal:** Player ship firing bullets.

---

## Phase 2: Enemy Forces (Units 17-32)
*Enemy sprites and formations.*

### Units 17-20: Sprite Multiplexing
- **Unit 17:** Multiplexing concept - Copper repositioning
- **Unit 18:** Sprite reuse - same sprite, different Y
- **Unit 19:** Multiplexing Copper list
- **Unit 20:** More sprites than hardware

### Units 21-24: Enemy Sprites
- **Unit 21:** Enemy designs - multiple types
- **Unit 22:** Enemy array - tracking all
- **Unit 23:** Enemy display - multiplexed sprites
- **Unit 24:** Enemy animation - frame cycling

### Units 25-28: Formation Movement
- **Unit 25:** Formation data - positions
- **Unit 26:** Formation sweep - left/right
- **Unit 27:** Direction change - at edges
- **Unit 28:** Descend step - move down

### Units 29-32: Enemy Behaviour
- **Unit 29:** Enemy types - different stats
- **Unit 30:** Dive attacks - break formation
- **Unit 31:** Enemy shooting - return fire
- **Unit 32:** Formation demo - moving enemies

**Phase Goal:** Enemy formation with multiplexing.

---

## Phase 3: Combat System (Units 33-48)
*Collision and destruction.*

### Units 33-36: Bullet Collision
- **Unit 33:** Bullet/enemy collision - detection
- **Unit 34:** Enemy hit points - damage
- **Unit 35:** Enemy destruction - removal
- **Unit 36:** Explosion effect - sprite swap

### Units 37-40: Enemy Attacks
- **Unit 37:** Enemy bullets - downward
- **Unit 38:** Player collision - enemy bullets
- **Unit 39:** Dive collision - ramming
- **Unit 40:** Player death - explosion

### Units 41-44: Wave System
- **Unit 41:** Wave complete - all destroyed
- **Unit 42:** Wave data - formations
- **Unit 43:** Wave transition - next wave
- **Unit 44:** Difficulty scaling - speed, count

### Units 45-48: Scoring
- **Unit 45:** Points per enemy - by type
- **Unit 46:** Bonus scoring - combos
- **Unit 47:** Wave bonus - clear bonus
- **Unit 48:** High score tracking

**Phase Goal:** Complete combat loop.

---

## Phase 4: Polish and Release (Units 49-64)
*Presentation and completion.*

### Units 49-52: Blitter Text
- **Unit 49:** Font design - character set
- **Unit 50:** Character rendering - Blitter copy
- **Unit 51:** String display - multiple chars
- **Unit 52:** Score display - on screen

### Units 53-56: Audio
- **Unit 53:** Shoot sound - variations
- **Unit 54:** Explosion sounds - enemy, player
- **Unit 55:** Wave clear sound
- **Unit 56:** Background music - simple loop

### Units 57-60: Game States
- **Unit 57:** Title screen - logo, start
- **Unit 58:** Playing state - main game
- **Unit 59:** Game over - final score
- **Unit 60:** High score entry

### Units 61-64: Release
- **Unit 61:** Lives display - remaining
- **Unit 62:** Difficulty options
- **Unit 63:** Full testing
- **Unit 64:** Release build - ADF

**Phase Goal:** Complete space shooter.

---

## Summary

**Blast Zone** teaches sprite multiplexing and object pools.

### Technical Specifications

- **Display:** 320×256, 5 bitplanes
- **Player:** Hardware sprite
- **Enemies:** Multiplexed sprites (16+ visible)
- **Bullets:** BOBs or sprites
- **Audio:** Multiple sound effects
- **Copper:** Sprite multiplexing
- **Distribution:** Bootable ADF

### Skills for Next Game

- Sprite multiplexing via Copper
- Object pool management
- Formation pattern systems
- Blitter text rendering
- Wave-based progression
