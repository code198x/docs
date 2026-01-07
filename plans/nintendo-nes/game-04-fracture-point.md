# Fracture Point: 64-Unit Outline

**Game:** 4 of 16
**Platform:** Nintendo Entertainment System
**Units:** 64 (4 phases)
**Concept:** Breakout clone. Control a paddle, bounce the ball, destroy bricks. The tension builds to the fracture point.

---

## Why This Game Fourth?

Fracture Point teaches ball physics and background modification:

1. **Ball physics** - Velocity, angles, reflection
2. **Background updates** - Modifying nametable mid-game
3. **Angle calculation** - Where paddle hits affects angle
4. **Brick destruction** - Removing background tiles
5. **APU depth** - More sophisticated sound design

This introduces modifying the playfield during gameplay.

---

## Skills Applied from Previous Games

| Skill | From | Application in Fracture Point |
|-------|------|------------------------------|
| PPU/sprites | All | Paddle, ball |
| Collision | All | Ball vs paddle, ball vs bricks |
| Object management | Stellar Barrage | Ball tracking |
| Controller input | All | Paddle movement |

## New Skills Introduced

| Skill | Phase | Description |
|-------|-------|-------------|
| Ball velocity | 1 | X and Y speed components |
| Reflection physics | 2 | Angle calculation on bounce |
| Background modification | 2 | Updating nametable tiles |
| Brick data tracking | 2 | Which bricks remain |
| Power-ups | 3 | Ball and paddle modifiers |
| APU channels | 4 | Multiple sound channel use |

---

## Phase 1: Paddle and Ball (Units 1-16)
*Basic ball and paddle display.*

### Units 1-4: Play Area
- **Unit 1:** Playfield layout - brick area, play area, border
- **Unit 2:** Brick tiles - various brick graphics
- **Unit 3:** Brick arrangement - rows and columns
- **Unit 4:** Initial nametable - complete playfield

### Units 5-8: Paddle
- **Unit 5:** Paddle sprite - horizontal bar
- **Unit 6:** Paddle positioning - bottom of screen
- **Unit 7:** Paddle input - left/right control
- **Unit 8:** Paddle movement - smooth motion

### Units 9-12: Ball
- **Unit 9:** Ball sprite - small square
- **Unit 10:** Ball velocity - X and Y components
- **Unit 11:** Ball movement - apply velocity each frame
- **Unit 12:** Ball on screen - moving ball visible

### Units 13-16: Basic Bouncing
- **Unit 13:** Wall collision - left, right, top walls
- **Unit 14:** Wall reflection - reverse appropriate velocity
- **Unit 15:** Ball speed - consistent after reflection
- **Unit 16:** Bouncing ball - ball bounces off walls

**Phase Goal:** Ball bounces off walls.

---

## Phase 2: Game Mechanics (Units 17-32)
*Paddle bounce and brick destruction.*

### Units 17-20: Paddle Collision
- **Unit 17:** Paddle hitbox - collision area
- **Unit 18:** Ball-paddle collision - detection
- **Unit 19:** Basic reflection - bounce upward
- **Unit 20:** Angle variation - hit position affects angle

### Units 21-24: Brick Collision
- **Unit 21:** Brick data - which bricks exist
- **Unit 22:** Ball-brick collision - tile lookup
- **Unit 23:** Brick destruction - mark as destroyed
- **Unit 24:** Background update - change tile to empty

### Units 25-28: Game Rules
- **Unit 25:** Ball lost - passes paddle
- **Unit 26:** Lives system - multiple attempts
- **Unit 27:** Level clear - all bricks destroyed
- **Unit 28:** Score increment - points per brick

### Units 29-32: Advanced Physics
- **Unit 29:** Brick bounce direction - which side hit
- **Unit 30:** Corner hits - diagonal reflection
- **Unit 31:** Spin effect - paddle movement affects ball
- **Unit 32:** Physics polish - satisfying bouncing

**Phase Goal:** Complete brick-breaking gameplay.

---

## Phase 3: Features and Variety (Units 33-48)
*Power-ups and level design.*

### Units 33-36: Brick Types
- **Unit 33:** Normal bricks - one hit
- **Unit 34:** Hard bricks - two hits
- **Unit 35:** Indestructible bricks - permanent obstacles
- **Unit 36:** Bonus bricks - extra points

### Units 37-40: Power-Ups
- **Unit 37:** Power-up drops - from certain bricks
- **Unit 38:** Wide paddle - temporary expansion
- **Unit 39:** Multi-ball - multiple balls active
- **Unit 40:** Slow ball - reduced speed

### Units 41-44: Level Design
- **Unit 41:** Level data format - brick arrangements
- **Unit 42:** Level 1 design - simple introduction
- **Unit 43:** Level 2-4 designs - increasing complexity
- **Unit 44:** Level progression - advance on clear

### Units 45-48: Game Flow
- **Unit 45:** Ball launch - start from paddle
- **Unit 46:** Pause between lives - brief delay
- **Unit 47:** Level transition - clear and load
- **Unit 48:** Difficulty scaling - faster ball per level

**Phase Goal:** Multiple levels with variety.

---

## Phase 4: Polish and Release (Units 49-64)
*Sound design and presentation.*

### Units 49-52: APU Sound Design
- **Unit 49:** Paddle hit sound - pulse channel
- **Unit 50:** Brick break sound - noise burst
- **Unit 51:** Wall bounce sound - subtle tick
- **Unit 52:** Power-up sound - reward jingle

### Units 53-56: Music
- **Unit 53:** Title music - catchy theme
- **Unit 54:** Gameplay music - background tune
- **Unit 55:** Victory jingle - level complete
- **Unit 56:** Game over music - defeat theme

### Units 57-60: Presentation
- **Unit 57:** Title screen - game logo
- **Unit 58:** Score and lives display - HUD
- **Unit 59:** High score - best score tracking
- **Unit 60:** Game over screen - final score

### Units 61-64: Release
- **Unit 61:** Instructions screen
- **Unit 62:** Balance testing - level difficulty
- **Unit 63:** Physics refinement - ball behaviour
- **Unit 64:** Release build - final iNES ROM

**Phase Goal:** Complete, polished breakout clone.

---

## Summary

**Fracture Point** teaches physics and background modification:

**Phase 1 (Basics):** Paddle, ball, wall bouncing.

**Phase 2 (Mechanics):** Paddle bounce, brick destruction.

**Phase 3 (Features):** Power-ups, brick types, levels.

**Phase 4 (Polish):** Sound design, presentation.

### Skills Transferred Forward

1. **Ball physics** → Any physics-based game
2. **Background modification** → Dynamic playfield changes
3. **Reflection angles** → Realistic bouncing
4. **Power-up systems** → Temporary abilities
5. **APU multi-channel** → Richer audio

### Game Specifications

- **Display:** Fixed screen
- **Paddle:** 24 pixels wide (expandable)
- **Ball:** 8×8 sprite
- **Bricks:** 13×8 grid typical
- **Power-ups:** 4 types
- **Levels:** 8+
- **Lives:** 3
- **Mapper:** NROM
- **ROM Size:** 16KB PRG + 8KB CHR
- **Controls:** D-pad (paddle), A (launch)
- **Audio:** APU effects + music
- **Distribution:** iNES ROM file
