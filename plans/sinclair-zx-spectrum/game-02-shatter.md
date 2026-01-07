# Shatter: 64-Unit Outline

**Game:** 2 of 16
**Platform:** ZX Spectrum
**Units:** 64 (4 phases)
**Concept:** Breakout clone with polish focus. Paddle, ball, bricks - with custom font, smooth pixel movement, and audio feedback.

---

## Why This Game Second?

Shatter introduces smooth movement and collision - fundamental skills for action games - while building on Ink War's attribute knowledge:

1. **Pixel-level movement** - Ball and paddle move smoothly, not cell-by-cell
2. **Software sprites** - Drawing and erasing moving objects (no hardware help)
3. **Physics** - Velocity, reflection angles, predictable ball behaviour
4. **Collision detection** - Ball vs paddle, ball vs bricks, ball vs walls
5. **Custom graphics** - Beyond plain attributes to designed visuals

The Spectrum has no hardware sprites, so this game teaches the software rendering that underpins all Spectrum action games.

---

## Skills Applied from Previous Game

| Skill | From | Application in Shatter |
|-------|------|----------------------|
| Screen memory | Ink War | Drawing paddle, ball, bricks |
| Attribute memory | Ink War | Colouring bricks and play area |
| Z80 basics | Ink War | All game logic |
| Keyboard input | Ink War | Paddle control |
| Game state | Ink War | Score, lives, level tracking |
| Beeper basics | Ink War | Expanded sound effects |

## New Skills Introduced

| Skill | Phase | Description |
|-------|-------|-------------|
| Custom font/UDG | 1 | User-defined graphics for game elements |
| Software sprites | 1 | Draw, erase, redraw moving objects |
| Pixel movement | 2 | Sub-character smooth movement |
| Velocity vectors | 2 | X and Y speed components |
| Reflection physics | 2 | Ball bouncing off surfaces |
| Collision detection | 2 | Pixel and box-based collision |
| Frame timing | 3 | Consistent game speed |
| Power-up systems | 3 | Collectible modifiers |

---

## Phase 1: Graphics Foundation (Units 1-16)
*Custom graphics and drawing routines.*

### Units 1-4: Custom Graphics
- **Unit 1:** User-defined graphics (UDG) concept - redefining character shapes
- **Unit 2:** Designing game graphics - paddle, ball, brick shapes
- **Unit 3:** Installing UDGs - copying to character RAM
- **Unit 4:** Displaying UDGs - PRINT vs direct screen writes

### Units 5-8: Drawing Routines
- **Unit 5:** Print at position - placing characters anywhere
- **Unit 6:** Drawing the paddle - multi-character paddle display
- **Unit 7:** Drawing bricks - brick grid layout
- **Unit 8:** Drawing the ball - single character or pixel ball

### Units 9-12: Erase and Redraw
- **Unit 9:** The XOR technique - drawing and erasing sprites
- **Unit 10:** Background restoration - clean erasing
- **Unit 11:** Flicker reduction - draw order matters
- **Unit 12:** Complete static display - paddle, bricks, borders visible

### Units 13-16: Play Area Setup
- **Unit 13:** Border drawing - walls of the play area
- **Unit 14:** Brick layout data - defining brick patterns
- **Unit 15:** Multiple brick colours - using attributes for variety
- **Unit 16:** Level display routine - complete level rendering

**Phase Goal:** Display game elements with custom graphics and colour.

---

## Phase 2: Movement and Physics (Units 17-32)
*Smooth movement and ball physics.*

### Units 17-20: Paddle Control
- **Unit 17:** Paddle data structure - position, width
- **Unit 18:** Keyboard reading for paddle - left/right keys
- **Unit 19:** Smooth paddle movement - pixel-level positioning
- **Unit 20:** Paddle boundaries - stay within play area

### Units 21-24: Ball Movement
- **Unit 21:** Ball data structure - X, Y, velocity X, velocity Y
- **Unit 22:** Ball update loop - move by velocity each frame
- **Unit 23:** Wall collision - bounce off sides and top
- **Unit 24:** Bottom collision - ball lost, lose life

### Units 25-28: Paddle Collision
- **Unit 25:** Ball-paddle collision detection
- **Unit 26:** Basic reflection - ball bounces up
- **Unit 27:** Angle variation - paddle position affects bounce angle
- **Unit 28:** Edge hits - sharp angles from paddle edges

### Units 29-32: Brick Collision
- **Unit 29:** Brick collision detection - which brick was hit
- **Unit 30:** Brick destruction - remove hit brick
- **Unit 31:** Ball reflection from bricks - bounce direction
- **Unit 32:** Score increment - points per brick

**Phase Goal:** Playable Breakout with ball physics and collision.

---

## Phase 3: Game Systems (Units 33-48)
*Lives, levels, power-ups, sound.*

### Units 33-36: Lives and Scoring
- **Unit 33:** Lives system - 3 lives, lose one when ball falls
- **Unit 34:** Lives display - show remaining lives
- **Unit 35:** Score display - formatted score with leading zeros
- **Unit 36:** High score tracking - remember best score

### Units 37-40: Level Progression
- **Unit 37:** Level complete detection - all bricks destroyed
- **Unit 38:** Level transition - clear screen, load new level
- **Unit 39:** Multiple level layouts - different brick patterns
- **Unit 40:** Difficulty progression - faster ball, fewer lives

### Units 41-44: Sound Design
- **Unit 41:** Beeper pitch control - frequency calculation
- **Unit 42:** Paddle hit sound - mid-tone blip
- **Unit 43:** Brick break sound - higher pitched, satisfying
- **Unit 44:** Ball lost sound - descending tone

### Units 45-48: Power-Ups
- **Unit 45:** Power-up spawning - drop from destroyed bricks
- **Unit 46:** Power-up falling - downward movement
- **Unit 47:** Power-up collection - paddle catches power-up
- **Unit 48:** Power-up effects - wider paddle, slower ball, multi-ball

**Phase Goal:** Complete game loop with progression and power-ups.

---

## Phase 4: Polish and Release (Units 49-64)
*Presentation and final polish.*

### Units 49-52: Title and Menus
- **Unit 49:** Title screen design - game logo
- **Unit 50:** Title screen display - attract mode
- **Unit 51:** Start game prompt - press key to begin
- **Unit 52:** Game over screen - final score, play again

### Units 53-56: Frame Timing
- **Unit 53:** Frame counter - consistent timing
- **Unit 54:** HALT instruction - sync to screen refresh
- **Unit 55:** Speed consistency - same speed on all Spectrums
- **Unit 56:** Difficulty timing - speed increases per level

### Units 57-60: Visual Polish
- **Unit 57:** Ball trail effect - brief afterimage
- **Unit 58:** Brick explosion - particle effect on destruction
- **Unit 59:** Screen flash - on power-up collection
- **Unit 60:** Smooth animations - level start countdown

### Units 61-64: Release
- **Unit 61:** Instructions display - controls and rules
- **Unit 62:** Bug hunting - edge cases in collision
- **Unit 63:** Balance tuning - ball speed, paddle size, angles
- **Unit 64:** Release build - final TAP file

**Phase Goal:** Polished, professional Breakout clone.

---

## Summary

**Shatter** teaches the fundamentals of action games on the Spectrum:

**Phase 1 (Graphics):** Custom characters, drawing routines - game looks good.

**Phase 2 (Physics):** Movement, velocity, collision - ball behaves correctly.

**Phase 3 (Systems):** Lives, levels, power-ups, sound - game is complete.

**Phase 4 (Polish):** Presentation, timing, effects - game feels professional.

### Skills Transferred Forward

The following skills debut in Shatter:

1. **Software sprites (XOR drawing)** → All action games
2. **Pixel-level movement** → Smooth animation throughout curriculum
3. **Velocity and physics** → Platform Panic (gravity), all movement
4. **Collision detection** → Every action game
5. **Frame timing (HALT)** → Consistent speed in all games
6. **Power-up systems** → Many subsequent games
7. **Level progression** → Standard game structure

### Comparison to C64

| Aspect | C64 (Brick Basher) | Spectrum (Shatter) |
|--------|-------------------|-------------------|
| Sprites | Hardware sprites | Software XOR sprites |
| Movement | Hardware positioning | Pixel calculation |
| Collision | Hardware detection | Software calculation |
| Sound | SID chip | Beeper only |
| Challenge | Using hardware | Everything in software |

The Spectrum version requires more work for the same result - but teaches deeper understanding of how graphics actually work.

### Game Specifications

- **Play Area:** 256×176 pixels (borders reserved)
- **Bricks:** 10×5 grid per level (50 bricks)
- **Ball Speed:** Increases each level
- **Paddle:** 3 sizes (normal, wide, narrow)
- **Lives:** 3 (configurable)
- **Levels:** 8 unique layouts
- **Power-ups:** Wide paddle, slow ball, multi-ball, catch
- **Controls:** Keyboard left/right (Q/A or O/P)
- **Audio:** Beeper effects for all interactions
- **Distribution:** TAP file
