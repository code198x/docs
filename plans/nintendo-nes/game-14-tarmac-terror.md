# Tarmac Terror: 128-Unit Outline

**Game:** 14 of 16
**Platform:** Nintendo Entertainment System
**Units:** 128 (8 phases)
**Concept:** Pseudo-3D racing game. Road rushing toward you, dodge traffic, survive the terror of the tarmac. Rad Racer territory.

---

## Why This Game Fourteenth?

Tarmac Terror introduces pseudo-3D road rendering:

1. **Perspective projection** - 3D illusion on 2D
2. **Road rendering** - Segment-based roads
3. **Sprite scaling** - Objects at different sizes
4. **Speed simulation** - Faster = more movement
5. **Split-screen** - Two-player racing

This teaches the maths behind 3D-style games.

---

## Skills Applied from Previous Games

| Skill | From | Application in Tarmac Terror |
|-------|------|----------------------------|
| Vertical scrolling | Thunder Run | Road movement |
| Sprite management | All | Cars, obstacles |
| Object pools | All | Traffic management |
| CHR banking | Thunder Run | Multiple sprite sizes |
| Frame timing | All | Speed control |

## New Skills Introduced

| Skill | Phase | Description |
|-------|-------|-------------|
| Perspective maths | 1 | Distance scaling |
| Road segments | 2 | Drawing curved roads |
| Sprite scaling | 3 | Size by distance |
| Speed effects | 3 | Visual speed cues |
| Hill rendering | 5 | Vertical curves |
| Split-screen | 7 | Two-player display |

---

## Phase 1: Perspective Foundation (Units 1-16)
*Basic perspective rendering.*

### Units 1-4: Projection Maths
- **Unit 1:** Perspective concept - near big, far small
- **Unit 2:** Z-depth - distance from camera
- **Unit 3:** Scale factor - size from distance
- **Unit 4:** Screen position - 3D to 2D

### Units 5-8: Road Basics
- **Unit 5:** Road centre - where road goes
- **Unit 6:** Road width - narrower with distance
- **Unit 7:** Road segments - strips
- **Unit 8:** Basic road display - straight road

### Units 9-12: Player Car
- **Unit 9:** Car sprite - player vehicle
- **Unit 10:** Car positioning - left/right
- **Unit 11:** Steering input - move sideways
- **Unit 12:** Car on road - car over road

### Units 13-16: Basic Racing
- **Unit 13:** Forward movement - down road
- **Unit 14:** Speed control - accelerate/brake
- **Unit 15:** Road edges - off-road
- **Unit 16:** Foundation - drive straight road

**Phase Goal:** Basic road rendering.

---

## Phase 2: Curved Roads (Units 17-32)
*Road curves and track definition.*

### Units 17-20: Road Curvature
- **Unit 17:** Curve data - bend values
- **Unit 18:** Curve rendering - shift segments
- **Unit 19:** Curve accumulation - smooth transition
- **Unit 20:** Sharp curves - hairpins

### Units 21-24: Track Definition
- **Unit 21:** Track data - segment sequence
- **Unit 22:** Segment properties - curve, width
- **Unit 23:** Track progression - through data
- **Unit 24:** Track looping - circuit

### Units 25-28: Road Decoration
- **Unit 25:** Road markings - lines
- **Unit 26:** Rumble strips - edge colour
- **Unit 27:** Kerbs - edge decoration
- **Unit 28:** Road surface - texture effect

### Units 29-32: Roadside Objects
- **Unit 29:** Scenery sprites - trees, signs
- **Unit 30:** Scenery placement - alongside
- **Unit 31:** Scenery scaling - size by distance
- **Unit 32:** Scenery variety - different types

**Phase Goal:** Curved roads with scenery.

---

## Phase 3: Speed and Traffic (Units 33-48)
*Speed mechanics and rival cars.*

### Units 33-36: Speed System
- **Unit 33:** Speed variable - velocity
- **Unit 34:** Acceleration - speed increase
- **Unit 35:** Braking - speed decrease
- **Unit 36:** Top speed - maximum

### Units 37-40: Speed Effects
- **Unit 37:** Segment density - more at speed
- **Unit 38:** Scenery speed - faster passing
- **Unit 39:** Engine sound - pitch by speed
- **Unit 40:** Speed display - speedometer

### Units 41-44: Traffic Cars
- **Unit 41:** Traffic sprite - other vehicles
- **Unit 42:** Traffic positioning - on road
- **Unit 43:** Traffic scaling - size by distance
- **Unit 44:** Multiple traffic - several visible

### Units 45-48: Traffic Behaviour
- **Unit 45:** Traffic movement - follow road
- **Unit 46:** Passing traffic - overtake
- **Unit 47:** Traffic collision - crash
- **Unit 48:** Collision response - slowdown

**Phase Goal:** Speed with traffic.

---

## Phase 4: Environment (Units 49-64)
*Horizon, sky, and atmosphere.*

### Units 49-52: Horizon and Sky
- **Unit 49:** Horizon line - road meets sky
- **Unit 50:** Sky gradient - colour variation
- **Unit 51:** Mountains - background
- **Unit 52:** Sky scrolling - parallax

### Units 53-56: Time and Weather
- **Unit 53:** Daytime - bright colours
- **Unit 54:** Sunset - orange tones
- **Unit 55:** Night - dark with lights
- **Unit 56:** Time progression - cycle

### Units 57-60: Weather
- **Unit 57:** Clear - default
- **Unit 58:** Rain effect - visual
- **Unit 59:** Rain grip - reduced traction
- **Unit 60:** Weather changes - transitions

### Units 61-64: Audio
- **Unit 61:** Engine loop - continuous
- **Unit 62:** Tyre screech - cornering
- **Unit 63:** Collision sound - crash
- **Unit 64:** Music - racing theme

**Phase Goal:** Atmospheric racing.

---

## Phase 5: Hills and Depth (Units 65-80)
*Vertical road curves.*

### Units 65-68: Hill Rendering
- **Unit 65:** Hill data - vertical curves
- **Unit 66:** Hill projection - up/down
- **Unit 67:** Horizon shift - with hills
- **Unit 68:** Crests and dips - terrain

### Units 69-72: Visibility
- **Unit 69:** Draw distance - how far
- **Unit 70:** Fog effect - fade
- **Unit 71:** Hidden segments - over hills
- **Unit 72:** Optimised drawing - skip occluded

### Units 73-76: Road Variations
- **Unit 73:** Narrow roads - mountain
- **Unit 74:** Wide roads - highway
- **Unit 75:** Splits - forks
- **Unit 76:** Tunnels - enclosed

### Units 77-80: Features
- **Unit 77:** Bridges - elevated
- **Unit 78:** Underpasses - below
- **Unit 79:** Checkpoints - timing
- **Unit 80:** Finish line - lap marker

**Phase Goal:** Hills and terrain.

---

## Phase 6: Race Structure (Units 81-96)
*Timing and progression.*

### Units 81-84: Timing
- **Unit 81:** Race timer - countdown
- **Unit 82:** Lap timing - per lap
- **Unit 83:** Best lap - fastest
- **Unit 84:** Time display - on-screen

### Units 85-88: Race Format
- **Unit 85:** Checkpoint racing - reach in time
- **Unit 86:** Time extension - bonus at checkpoint
- **Unit 87:** Race completion - finish
- **Unit 88:** Race failure - out of time

### Units 89-92: Position
- **Unit 89:** Position tracking - rank
- **Unit 90:** Position display - current
- **Unit 91:** Position changes - overtaking
- **Unit 92:** Finish position - final

### Units 93-96: Multiple Tracks
- **Unit 93:** Track 1 - beginner
- **Unit 94:** Track 2 - intermediate
- **Unit 95:** Track 3 - expert
- **Unit 96:** Track selection - choose

**Phase Goal:** Complete race structure.

---

## Phase 7: Two-Player Mode (Units 97-112)
*Split-screen racing.*

### Units 97-100: Split-Screen Setup
- **Unit 97:** Screen division - half each
- **Unit 98:** Two cameras - independent
- **Unit 99:** Separate controls - two inputs
- **Unit 100:** Position comparison - relative

### Units 101-104: Split-Screen Rendering
- **Unit 101:** Dual road rendering - both views
- **Unit 102:** Reduced detail - performance
- **Unit 103:** Sprite sharing - divided OAM
- **Unit 104:** Optimised display - smooth

### Units 105-108: Two-Player Features
- **Unit 105:** Ghost rival - other's position
- **Unit 106:** Same track - direct competition
- **Unit 107:** Victory conditions - who wins
- **Unit 108:** Results - comparison

### Units 109-112: Game Modes
- **Unit 109:** Time trial - solo best time
- **Unit 110:** Versus mode - two player
- **Unit 111:** Championship - multiple races
- **Unit 112:** Options - settings

**Phase Goal:** Split-screen racing.

---

## Phase 8: Release (Units 113-128)
*Polish and release.*

### Units 113-116: Advanced Features
- **Unit 113:** Car upgrades - performance
- **Unit 114:** Difficulty settings - traffic
- **Unit 115:** Ghost replay - race best time
- **Unit 116:** Statistics - career stats

### Units 117-120: Presentation
- **Unit 117:** Title screen - logo
- **Unit 118:** Title music - theme
- **Unit 119:** Victory/failure screens
- **Unit 120:** Attract mode - demo

### Units 121-124: Balance
- **Unit 121:** Speed balance - fair
- **Unit 122:** Track balance - varied
- **Unit 123:** Traffic balance - challenging
- **Unit 124:** Overall tuning

### Units 125-128: Release
- **Unit 125:** Instructions screen
- **Unit 126:** Performance testing
- **Unit 127:** Final testing
- **Unit 128:** Release build - final ROM

**Phase Goal:** Complete racing game.

---

## Summary

**Tarmac Terror** teaches pseudo-3D and split-screen.

### Game Specifications

- **Tracks:** 3+ courses
- **Road:** Segment-based pseudo-3D
- **Player Car:** Multiple sprite sizes
- **Traffic:** Up to 4 visible
- **Speed:** 0-200+ simulation
- **Modes:** Time trial, vs, championship
- **Weather:** Clear, rain, day/night
- **Players:** 1-2 split-screen
- **Mapper:** MMC1
- **ROM Size:** 128KB PRG + 64KB CHR
- **Controls:** D-pad + A (accel) + B (brake)
- **Distribution:** iNES ROM file
