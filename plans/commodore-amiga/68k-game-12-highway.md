# Highway: 128-Unit Outline

**Game:** 12 of 16 (68000 Assembly)
**Platform:** Commodore Amiga
**Language:** 68000 Assembly
**Units:** 128 (8 phases)
**Concept:** Pseudo-3D racing with Copper road effects.

---

## Why This Game Twelfth?

Highway introduces pseudo-3D rendering:

1. **Perspective projection** - 3D maths
2. **Copper road rendering** - Line-by-line modification
3. **Sprite scaling** - Size by distance
4. **Road curves** - Segment-based tracks
5. **Split-screen** - Two-player racing

The Amiga's answer to OutRun and Lotus.

---

## Skills Applied from Previous Games

| Skill | From | Application |
|-------|------|-------------|
| Copper effects | Parallax | Road rendering |
| Sprite handling | All | Cars, scenery |
| Two-player | Brawler | Split-screen |
| Fixed-point maths | Shatter Point | 3D projection |
| Smooth scrolling | All | Road movement |

## New Skills Introduced

| Skill | Phase | Description |
|-------|-------|-------------|
| Perspective projection | 1 | 3D to 2D |
| Copper road | 2 | Per-line colours |
| Sprite scaling | 3 | Size simulation |
| Road segments | 4 | Curves, hills |
| Split-screen | 6 | Two views |

---

## Phase 1: Perspective Basics (Units 1-16)
*3D projection fundamentals.*

### Units 1-4: Projection Maths
- **Unit 1:** Perspective concept - far = small
- **Unit 2:** Z-depth - distance from camera
- **Unit 3:** Scale factor - 1/Z relationship
- **Unit 4:** Screen Y from Z - horizon

### Units 5-8: Road Basics
- **Unit 5:** Road centre - screen X
- **Unit 6:** Road width - narrower with distance
- **Unit 7:** Road segments - horizontal strips
- **Unit 8:** Basic road display

### Units 9-12: Road Rendering
- **Unit 9:** Segment drawing - per scanline
- **Unit 10:** Edge calculation - left/right
- **Unit 11:** Road colours - stripes
- **Unit 12:** Road demo - straight road

### Units 13-16: Camera Movement
- **Unit 13:** Camera position - Z movement
- **Unit 14:** Speed effect - Z change rate
- **Unit 15:** Road scrolling - perspective
- **Unit 16:** Moving road demo

**Phase Goal:** Basic perspective road.

---

## Phase 2: Copper Road Effects (Units 17-32)
*Per-scanline road rendering.*

### Units 17-20: Copper Road
- **Unit 17:** Copper for road - per-line changes
- **Unit 18:** Road colour registers
- **Unit 19:** Stripe alternation - pattern
- **Unit 20:** Copper list generation

### Units 21-24: Road Features
- **Unit 21:** Road markings - centre line
- **Unit 22:** Rumble strips - edge colour
- **Unit 23:** Kerbs - side decoration
- **Unit 24:** Road surface variety

### Units 25-28: Horizon and Sky
- **Unit 25:** Horizon line - road meets sky
- **Unit 26:** Sky gradient - Copper colours
- **Unit 27:** Mountains - background sprites
- **Unit 28:** Parallax sky - slow movement

### Units 29-32: Road Polish
- **Unit 29:** Road shimmer - heat haze
- **Unit 30:** Night mode - headlights
- **Unit 31:** Weather effects - rain
- **Unit 32:** Atmospheric rendering

**Phase Goal:** Beautiful road rendering.

---

## Phase 3: Player Car and Scaling (Units 33-48)
*Car handling and sprite scaling.*

### Units 33-36: Player Car
- **Unit 33:** Car sprite - from behind
- **Unit 34:** Car positioning - screen X
- **Unit 35:** Steering input - left/right
- **Unit 36:** Speed control - accelerate/brake

### Units 37-40: Sprite Scaling
- **Unit 37:** Scaling concept - size by distance
- **Unit 38:** Pre-scaled sprites - multiple sizes
- **Unit 39:** Scale selection - by Z
- **Unit 40:** Smooth scaling - interpolation

### Units 41-44: Scenery Objects
- **Unit 41:** Roadside sprites - trees, signs
- **Unit 42:** Scenery placement - alongside road
- **Unit 43:** Scenery scaling - by distance
- **Unit 44:** Scenery streaming - appear/disappear

### Units 45-48: Traffic Cars
- **Unit 45:** Traffic sprites - other vehicles
- **Unit 46:** Traffic positioning - on road
- **Unit 47:** Traffic movement - relative
- **Unit 48:** Multiple traffic - several visible

**Phase Goal:** Scaled sprites on road.

---

## Phase 4: Road Geometry (Units 49-64)
*Curves and hills.*

### Units 49-52: Road Curves
- **Unit 49:** Curve concept - X offset
- **Unit 50:** Curve data - per segment
- **Unit 51:** Curve accumulation - smooth
- **Unit 52:** Sharp curves - hairpins

### Units 53-56: Road Hills
- **Unit 53:** Hill concept - Y offset
- **Unit 54:** Hill data - per segment
- **Unit 55:** Hill rendering - horizon shift
- **Unit 56:** Crests and dips - visibility

### Units 57-60: Track Definition
- **Unit 57:** Track data - segment array
- **Unit 58:** Track length - circuit
- **Unit 59:** Track variety - straight, curved
- **Unit 60:** Track loading

### Units 61-64: Track Features
- **Unit 61:** Tunnels - enclosed
- **Unit 62:** Bridges - elevated
- **Unit 63:** Checkpoints - timing
- **Unit 64:** Finish line - lap complete

**Phase Goal:** Curved, hilly tracks.

---

## Phase 5: Race Mechanics (Units 65-80)
*Racing game features.*

### Units 65-68: Collision
- **Unit 65:** Traffic collision - detection
- **Unit 66:** Collision response - slowdown
- **Unit 67:** Scenery collision - crash
- **Unit 68:** Off-road penalty - grass slowdown

### Units 69-72: Speed System
- **Unit 69:** Speed calculation - physics
- **Unit 70:** Acceleration curve - realistic
- **Unit 71:** Braking - deceleration
- **Unit 72:** Top speed - by car

### Units 73-76: Timing
- **Unit 73:** Race timer - lap time
- **Unit 74:** Best lap - tracking
- **Unit 75:** Checkpoint time - extend
- **Unit 76:** Time display - on screen

### Units 77-80: Position
- **Unit 77:** Position tracking - ranking
- **Unit 78:** Other racers - simulated
- **Unit 79:** Position changes - overtaking
- **Unit 80:** Race completion

**Phase Goal:** Complete race mechanics.

---

## Phase 6: Split-Screen (Units 81-96)
*Two-player mode.*

### Units 81-84: Split Display
- **Unit 81:** Screen division - top/bottom
- **Unit 82:** Two viewports - separate
- **Unit 83:** Two Copper lists - per player
- **Unit 84:** Display timing - VBlank

### Units 85-88: Two Players
- **Unit 85:** Player 2 car - different sprite
- **Unit 86:** Player 2 controls - port 2
- **Unit 87:** Independent positions
- **Unit 88:** Independent speeds

### Units 89-92: Versus Features
- **Unit 89:** Relative position - to each other
- **Unit 90:** Ghost car - other player's position
- **Unit 91:** Victory condition - first finish
- **Unit 92:** Match results

### Units 93-96: Performance
- **Unit 93:** Split-screen optimisation
- **Unit 94:** Reduced detail - if needed
- **Unit 95:** Frame rate maintenance
- **Unit 96:** Two-player testing

**Phase Goal:** Split-screen racing.

---

## Phase 7: Game Modes (Units 97-112)
*Race structure and features.*

### Units 97-100: Game Modes
- **Unit 97:** Time trial - best time
- **Unit 98:** Versus mode - two player
- **Unit 99:** Championship - multiple races
- **Unit 100:** Mode selection

### Units 101-104: Tracks
- **Unit 101:** Track 1 - beginner, coastal
- **Unit 102:** Track 2 - intermediate, forest
- **Unit 103:** Track 3 - expert, mountain
- **Unit 104:** Track unlocking

### Units 105-108: Presentation
- **Unit 105:** Title screen
- **Unit 106:** Track select
- **Unit 107:** Race start - countdown
- **Unit 108:** Results screen

### Units 109-112: Audio
- **Unit 109:** Engine sound - pitch by speed
- **Unit 110:** Tyre screech - cornering
- **Unit 111:** Collision sound
- **Unit 112:** Music - per track

**Phase Goal:** Complete game modes.

---

## Phase 8: Release (Units 113-128)
*Polish and release.*

### Units 113-116: Advanced Features
- **Unit 113:** Car selection - multiple vehicles
- **Unit 114:** Difficulty settings
- **Unit 115:** Ghost replay - time trial
- **Unit 116:** Statistics

### Units 117-120: Balance
- **Unit 117:** Speed tuning
- **Unit 118:** Track difficulty
- **Unit 119:** Traffic density
- **Unit 120:** Overall balance

### Units 121-124: Testing
- **Unit 121:** Single-player test
- **Unit 122:** Two-player test
- **Unit 123:** All tracks
- **Unit 124:** Performance

### Units 125-128: Release
- **Unit 125:** Credits
- **Unit 126:** Documentation
- **Unit 127:** Final testing
- **Unit 128:** Release build - ADF

**Phase Goal:** Complete racing game.

---

## Summary

**Highway** teaches pseudo-3D and Copper road effects.

### Technical Specifications

- **Display:** Copper-rendered road, 320×256
- **Projection:** Perspective with scaling
- **Players:** 1-2 split-screen
- **Cars:** Pre-scaled sprite sets
- **Tracks:** 3 with curves and hills
- **Traffic:** Scaled sprites
- **Modes:** Time trial, versus, championship
- **Audio:** Engine, effects, music
- **Distribution:** Bootable ADF

### Skills for Next Game

- Perspective projection
- Copper per-line effects
- Sprite scaling techniques
- Road segment geometry
- Split-screen rendering
