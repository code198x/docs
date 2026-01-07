# Skyfire: 64-Unit Outline

**Game:** 3 of 16
**Platform:** ZX Spectrum
**Units:** 64 (4 phases)
**Concept:** Fixed-screen space shooter. Player ship versus descending enemy waves. Shoot, dodge, survive.

---

## Why This Game Third?

Skyfire introduces multi-object management - the foundation for any game with enemies:

1. **Multiple moving objects** - Many enemies on screen simultaneously
2. **Projectile management** - Player and enemy bullets
3. **Enemy patterns** - Coordinated movement behaviours
4. **Sprite masking** - Objects overlapping without corruption
5. **Object pooling** - Efficient management of many entities

While Shatter had one ball, Skyfire manages dozens of objects - a significant complexity increase.

---

## Skills Applied from Previous Games

| Skill | From | Application in Skyfire |
|-------|------|----------------------|
| Screen memory | Ink War | All graphics |
| Attributes | Ink War | Colouring ships, enemies |
| Software sprites | Shatter | Ship, enemies, bullets |
| Pixel movement | Shatter | Smooth object motion |
| Collision detection | Shatter | Bullets hitting enemies |
| Frame timing | Shatter | Consistent game speed |
| Beeper sound | Shatter | Expanded effects |
| Game state | Ink War | Score, lives, waves |

## New Skills Introduced

| Skill | Phase | Description |
|-------|-------|-------------|
| Object arrays | 1 | Managing multiple entities |
| Sprite masking | 1 | Clean overlap of sprites |
| Bullet pooling | 2 | Efficient projectile management |
| Enemy waves | 2 | Coordinated enemy spawning |
| Movement patterns | 3 | Sine waves, dive patterns |
| Multiple collision types | 3 | Bullet-enemy, enemy-player |
| Difficulty curves | 4 | Scaling challenge |
| High score persistence | 4 | Saving best score |

---

## Phase 1: Ship and Display (Units 1-16)
*Player ship and enemy graphics.*

### Units 1-4: Player Ship
- **Unit 1:** Ship sprite design - player ship graphics
- **Unit 2:** Ship display routine - draw at position
- **Unit 3:** Ship movement - left/right control
- **Unit 4:** Ship boundaries - stay on screen

### Units 5-8: Enemy Graphics
- **Unit 5:** Enemy sprite designs - multiple enemy types
- **Unit 6:** Enemy display routine - draw single enemy
- **Unit 7:** Sprite masking concept - clean overlaps
- **Unit 8:** Masked sprite routine - draw without corruption

### Units 9-12: Object Management
- **Unit 9:** Object structure - X, Y, type, active flag
- **Unit 10:** Object array - table of all enemies
- **Unit 11:** Active object iteration - process only active objects
- **Unit 12:** Draw all enemies - render from object array

### Units 13-16: Play Area
- **Unit 13:** Border and score area - reserved screen space
- **Unit 14:** Star background - simple starfield
- **Unit 15:** Complete display - ship, enemies, stars, border
- **Unit 16:** Colour scheme - attribute layout for play area

**Phase Goal:** Display player ship and multiple enemies.

---

## Phase 2: Shooting and Enemies (Units 17-32)
*Bullets and enemy behaviour.*

### Units 17-20: Player Bullets
- **Unit 17:** Bullet structure - X, Y, active flag
- **Unit 18:** Bullet pool - fixed array of bullet slots
- **Unit 19:** Fire button - spawn bullet at ship position
- **Unit 20:** Bullet movement - upward travel

### Units 21-24: Bullet Collision
- **Unit 21:** Bullet-enemy collision detection
- **Unit 22:** Enemy destruction - deactivate on hit
- **Unit 23:** Score increment - points per enemy
- **Unit 24:** Bullet deactivation - remove on hit or screen edge

### Units 25-28: Enemy Movement
- **Unit 25:** Basic descent - enemies move downward
- **Unit 26:** Horizontal drift - enemies move side to side
- **Unit 27:** Formation movement - enemies move as group
- **Unit 28:** Enemy reaching bottom - player loses life

### Units 29-32: Enemy Waves
- **Unit 29:** Wave structure - formation of enemies
- **Unit 30:** Wave spawning - create wave at top
- **Unit 31:** Wave completion - all enemies destroyed
- **Unit 32:** Next wave - new wave with variation

**Phase Goal:** Playable shooter - shoot enemies, avoid them reaching bottom.

---

## Phase 3: Combat Depth (Units 33-48)
*Enemy bullets, patterns, and polish.*

### Units 33-36: Enemy Bullets
- **Unit 33:** Enemy bullet pool - separate from player bullets
- **Unit 34:** Enemy firing - random enemies shoot
- **Unit 35:** Enemy bullet movement - downward travel
- **Unit 36:** Player hit detection - bullet hits ship

### Units 37-40: Movement Patterns
- **Unit 37:** Sine wave pattern - enemies weave
- **Unit 38:** Dive pattern - enemy swoops at player
- **Unit 39:** Pattern data - encoded movement sequences
- **Unit 40:** Multiple pattern types per wave

### Units 41-44: Lives and Game Flow
- **Unit 41:** Lives system - start with 3
- **Unit 42:** Death sequence - explosion, respawn
- **Unit 43:** Game over detection - no lives remaining
- **Unit 44:** Continue game flow - wave after wave

### Units 45-48: Sound and Effects
- **Unit 45:** Fire sound - player shooting
- **Unit 46:** Explosion sound - enemy destroyed
- **Unit 47:** Player hit sound - damage feedback
- **Unit 48:** Visual explosion - enemy death effect

**Phase Goal:** Full combat with enemy fire and movement patterns.

---

## Phase 4: Polish and Release (Units 49-64)
*Presentation and mastery.*

### Units 49-52: Difficulty Progression
- **Unit 49:** Wave difficulty scaling - faster, more enemies
- **Unit 50:** Enemy type progression - harder enemies appear
- **Unit 51:** Fire rate increase - enemies shoot more often
- **Unit 52:** Speed ramping - gradual difficulty curve

### Units 53-56: Title and High Score
- **Unit 53:** Title screen design - game logo
- **Unit 54:** High score display - current best
- **Unit 55:** High score entry - initials input
- **Unit 56:** High score persistence - save to memory (or password)

### Units 57-60: Visual Polish
- **Unit 57:** Scrolling starfield - parallax background
- **Unit 58:** Ship thrust animation - engine glow
- **Unit 59:** Enemy variety visuals - distinct enemy types
- **Unit 60:** Screen flash on events - feedback enhancement

### Units 61-64: Release
- **Unit 61:** Instructions screen - controls and gameplay
- **Unit 62:** Bug fixing - collision edge cases
- **Unit 63:** Balance tuning - difficulty curve refinement
- **Unit 64:** Release build - final TAP file

**Phase Goal:** Complete, polished space shooter.

---

## Summary

**Skyfire** teaches multi-object management essential for action games:

**Phase 1 (Display):** Multiple sprites, masking, object arrays.

**Phase 2 (Combat):** Bullets, collision, waves - shooting works.

**Phase 3 (Depth):** Enemy fire, patterns, effects - combat is engaging.

**Phase 4 (Polish):** Difficulty, high scores, presentation - professional game.

### Skills Transferred Forward

The following skills debut in Skyfire:

1. **Object arrays/pooling** → Managing entities in all games
2. **Sprite masking** → Clean overlapping sprites
3. **Projectile management** → Any game with shooting
4. **Enemy wave systems** → Invader Wave, shooters
5. **Movement patterns** → Enemy AI throughout curriculum
6. **Difficulty scaling** → All games with progression
7. **High score systems** → Standard arcade feature

### Comparison to C64 (Starfield)

| Aspect | C64 (Starfield) | Spectrum (Skyfire) |
|--------|----------------|-------------------|
| Sprites | 8 hardware sprites | Unlimited software sprites |
| Collision | Hardware detection | Software calculation |
| Sprite limit | 8 per scanline | CPU-limited only |
| Challenge | Multiplexing for more | Raw CPU management |

The Spectrum can display more sprites (no hardware limit) but every pixel must be calculated in software.

### Game Specifications

- **Play Area:** Full screen minus score area
- **Player Ship:** 16×16 pixels, 3 lives
- **Enemies:** 4 types with different behaviours
- **Player Bullets:** 3 max on screen
- **Enemy Bullets:** 6 max on screen
- **Waves:** Increasing difficulty, new patterns
- **Patterns:** Straight, sine wave, dive, formation
- **Scoring:** 10-50 points per enemy type
- **Controls:** Left/right, fire (customisable)
- **Audio:** Beeper effects throughout
- **Distribution:** TAP file
