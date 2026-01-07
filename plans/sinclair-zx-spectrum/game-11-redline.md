# Redline: 128-Unit Outline

**Game:** 11 of 16
**Platform:** ZX Spectrum
**Units:** 128 (8 phases)
**Concept:** Pseudo-3D racing game. Speed through tracks, overtake rivals, beat the clock. Outrun-style racing.

---

## Why This Game Eleventh?

Redline introduces pseudo-3D projection - creating depth on a 2D display:

1. **Perspective projection** - Objects scale with distance
2. **Road rendering** - Curved roads using segments
3. **Speed simulation** - Faster = more screen movement
4. **Sprite scaling** - Rivals and objects at different distances
5. **Track data** - Defining road curves and hills

This is a significant technical leap, using maths for 3D illusion.

---

## Skills Applied from Previous Games

| Skill | From | Application in Redline |
|-------|------|----------------------|
| Frame timing | All | Smooth animation |
| Object arrays | Skyfire | Rival cars, obstacles |
| Collision detection | All | Car collisions |
| Parallax | Blitz | Roadside scenery |
| Difficulty scaling | All | Speed progression |
| Sound effects | All | Engine, effects |

## New Skills Introduced

| Skill | Phase | Description |
|-------|-------|-------------|
| Perspective projection | 1 | Distance scaling |
| Road segment rendering | 2 | Drawing curved roads |
| Sprite scaling | 3 | Objects at different sizes |
| Track data structures | 2 | Defining road shape |
| Speed/distance mapping | 3 | Speed affects visuals |
| Horizon drawing | 4 | Sky meets road |
| Hill rendering | 5 | Vertical road curves |
| Split-screen | 7 | Two-player racing |

---

## Phase 1: Perspective Foundation (Units 1-16)
*Basic perspective rendering.*

### Units 1-4: Projection Maths
- **Unit 1:** Perspective concept - near things big, far things small
- **Unit 2:** Z-depth tracking - distance from camera
- **Unit 3:** Scale factor - calculate size from distance
- **Unit 4:** Screen position - project 3D to 2D

### Units 5-8: Road Basics
- **Unit 5:** Road centre line - where road goes
- **Unit 6:** Road width at distance - narrower further away
- **Unit 7:** Road segments - dividing road into strips
- **Unit 8:** Basic road rendering - straight road display

### Units 9-12: Player Car
- **Unit 9:** Car sprite design - player vehicle
- **Unit 10:** Car positioning - left/right on road
- **Unit 11:** Steering input - move car sideways
- **Unit 12:** Car on road - car over road graphics

### Units 13-16: Basic Racing
- **Unit 13:** Forward movement - advancing down road
- **Unit 14:** Speed control - accelerate/brake
- **Unit 15:** Road edges - off-road detection
- **Unit 16:** Playable foundation - drive down straight road

**Phase Goal:** Basic road rendering with player car.

---

## Phase 2: Curved Roads (Units 17-32)
*Road curves and track definition.*

### Units 17-20: Road Curvature
- **Unit 17:** Curve data - road bend values
- **Unit 18:** Curve rendering - shift segments for curves
- **Unit 19:** Curve accumulation - smooth curve transition
- **Unit 20:** Sharp curves - hairpin bends

### Units 21-24: Track Definition
- **Unit 21:** Track data structure - sequence of segments
- **Unit 22:** Segment properties - curve, hill, width
- **Unit 23:** Track progression - advancing through data
- **Unit 24:** Track looping - completing a circuit

### Units 25-28: Road Decoration
- **Unit 25:** Road markings - centre line, edges
- **Unit 26:** Rumble strips - alternating colours
- **Unit 27:** Kerbs - edge decoration
- **Unit 28:** Road surface - tarmac texture effect

### Units 29-32: Roadside Objects
- **Unit 29:** Scenery sprites - trees, signs, barriers
- **Unit 30:** Scenery placement - alongside road
- **Unit 31:** Scenery scaling - size by distance
- **Unit 32:** Scenery variety - different object types

**Phase Goal:** Curved roads with decoration and scenery.

---

## Phase 3: Speed and Rivals (Units 33-48)
*Speed mechanics and opponent cars.*

### Units 33-36: Speed Simulation
- **Unit 33:** Speed variable - current velocity
- **Unit 34:** Acceleration - speed increase rate
- **Unit 35:** Braking - speed decrease rate
- **Unit 36:** Top speed - maximum velocity

### Units 37-40: Speed Effects
- **Unit 37:** Segment density - more segments at speed
- **Unit 38:** Scenery speed - faster passing objects
- **Unit 39:** Engine sound - pitch by speed
- **Unit 40:** Speed display - speedometer

### Units 41-44: Rival Cars
- **Unit 41:** Rival sprite - opponent vehicle
- **Unit 42:** Rival positioning - place on road
- **Unit 43:** Rival scaling - size by distance
- **Unit 44:** Multiple rivals - several cars visible

### Units 45-48: Rival Behaviour
- **Unit 45:** Rival movement - they follow road
- **Unit 46:** Passing rivals - overtake mechanics
- **Unit 47:** Rival collision - crash detection
- **Unit 48:** Collision response - slowdown, spin

**Phase Goal:** Speed mechanics with rival cars.

---

## Phase 4: Sky and Environment (Units 49-64)
*Horizon, weather, and atmosphere.*

### Units 49-52: Horizon and Sky
- **Unit 49:** Horizon line - where road meets sky
- **Unit 50:** Sky gradient - colour variation
- **Unit 51:** Distant mountains - background scenery
- **Unit 52:** Sky scrolling - parallax with steering

### Units 53-56: Time of Day
- **Unit 53:** Daytime palette - bright colours
- **Unit 54:** Sunset palette - orange/red tones
- **Unit 55:** Night mode - dark with headlights
- **Unit 56:** Time progression - day cycle through race

### Units 57-60: Weather Effects
- **Unit 57:** Clear weather - default state
- **Unit 58:** Rain effect - visual overlay
- **Unit 59:** Rain grip - reduced traction
- **Unit 60:** Weather transitions - changing conditions

### Units 61-64: Sound Design
- **Unit 61:** Engine loop - continuous engine sound
- **Unit 62:** Tyre screech - hard cornering
- **Unit 63:** Collision sound - crash effect
- **Unit 64:** Music - racing theme (beeper)

**Phase Goal:** Atmospheric racing with environment variety.

---

## Phase 5: Hills and Depth (Units 65-80)
*Vertical road curves and depth perception.*

### Units 65-68: Hill Rendering
- **Unit 65:** Hill data - vertical curve values
- **Unit 66:** Hill projection - road going up/down
- **Unit 67:** Horizon shift - sky position with hills
- **Unit 68:** Crests and dips - dramatic terrain

### Units 69-72: Visibility
- **Unit 69:** Draw distance - how far to render
- **Unit 70:** Fog effect - distant fade
- **Unit 71:** Hidden segments - over hill obscuring
- **Unit 72:** Optimised drawing - skip occluded segments

### Units 73-76: Road Variations
- **Unit 73:** Narrow roads - mountain passes
- **Unit 74:** Wide roads - highways
- **Unit 75:** Split paths - forks in road
- **Unit 76:** Tunnels - enclosed sections

### Units 77-80: Bridges and Features
- **Unit 77:** Bridge structures - elevated road
- **Unit 78:** Underpasses - road going under
- **Unit 79:** Start/finish line - lap marker
- **Unit 80:** Checkpoint gates - timing points

**Phase Goal:** Hills and terrain variety.

---

## Phase 6: Race Structure (Units 81-96)
*Laps, timing, and progression.*

### Units 81-84: Timing System
- **Unit 81:** Race timer - counting up/down
- **Unit 82:** Lap timing - individual lap times
- **Unit 83:** Best lap - tracking fastest
- **Unit 84:** Time display - on-screen timer

### Units 85-88: Race Format
- **Unit 85:** Checkpoint racing - reach checkpoint in time
- **Unit 86:** Time extension - bonus time at checkpoint
- **Unit 87:** Race completion - finish the course
- **Unit 88:** Race failure - out of time

### Units 89-92: Positioning
- **Unit 89:** Position tracking - rank among rivals
- **Unit 90:** Position display - current place
- **Unit 91:** Position changes - overtaking affects rank
- **Unit 92:** Finish position - final result

### Units 93-96: Multiple Tracks
- **Unit 93:** Track 1 design - beginner course
- **Unit 94:** Track 2 design - intermediate course
- **Unit 95:** Track 3 design - expert course
- **Unit 96:** Track selection - choose course

**Phase Goal:** Complete race structure with timing.

---

## Phase 7: Polish and Modes (Units 97-112)
*Two-player and presentation.*

### Units 97-100: Two-Player Mode
- **Unit 97:** Split-screen setup - divide display
- **Unit 98:** Two cameras - independent views
- **Unit 99:** Separate controls - two sets of inputs
- **Unit 100:** Position comparison - relative performance

### Units 101-104: Two-Player Features
- **Unit 101:** Ghost rival - other player's car
- **Unit 102:** Collision between players - contact rules
- **Unit 103:** Split-screen optimisation - maintaining speed
- **Unit 104:** Victory conditions - who wins

### Units 105-108: Game Modes
- **Unit 105:** Time trial mode - best time focus
- **Unit 106:** Championship mode - multiple races
- **Unit 107:** Points system - championship standings
- **Unit 108:** Cup progression - unlock new cups

### Units 109-112: Presentation
- **Unit 109:** Title screen - game logo
- **Unit 110:** Car selection - choose vehicle
- **Unit 111:** Results screen - race summary
- **Unit 112:** High score table - best times

**Phase Goal:** Two-player mode and game structure.

---

## Phase 8: Release (Units 113-128)
*Final polish and release.*

### Units 113-116: Advanced Features
- **Unit 113:** Car upgrades - improve performance
- **Unit 114:** Difficulty settings - rival aggression
- **Unit 115:** Ghost replay - race against best time
- **Unit 116:** Statistics tracking - career stats

### Units 117-120: Audio Polish
- **Unit 117:** Title music - attract mode
- **Unit 118:** Victory jingle - winning fanfare
- **Unit 119:** Failure sound - game over
- **Unit 120:** Menu sounds - navigation feedback

### Units 121-124: Visual Polish
- **Unit 121:** Attract mode - demo gameplay
- **Unit 122:** Intro sequence - race start animation
- **Unit 123:** Podium finish - victory celebration
- **Unit 124:** Track preview - show course before race

### Units 125-128: Release
- **Unit 125:** Instructions screen
- **Unit 126:** Performance testing - consistent frame rate
- **Unit 127:** Balance tuning - rival difficulty
- **Unit 128:** Release build - final TAP file

**Phase Goal:** Complete racing game.

---

## Summary

**Redline** teaches pseudo-3D rendering and racing mechanics:

**Phase 1 (Projection):** Perspective maths, basic road.

**Phase 2 (Curves):** Road curves, track data, scenery.

**Phase 3 (Racing):** Speed, rivals, collisions.

**Phase 4 (Environment):** Sky, weather, atmosphere.

**Phase 5 (Hills):** Vertical curves, depth.

**Phase 6 (Structure):** Timing, laps, tracks.

**Phase 7 (Modes):** Two-player, championships.

**Phase 8 (Release):** Polish, release.

### Skills Transferred Forward

1. **Perspective projection** → 3D-style games
2. **Sprite scaling** → Size-based depth
3. **Road segment rendering** → Track-based games
4. **Speed simulation** → Vehicle games
5. **Split-screen** → Multiplayer modes
6. **Championship systems** → Career modes

### Technical Notes

Pseudo-3D racing on the Spectrum requires careful optimisation:

1. **Limited draw distance** - Render fewer segments
2. **Simplified scaling** - Pre-calculated sprite sizes
3. **Attribute-aware design** - Minimise colour clash
4. **Unrolled loops** - Speed-critical rendering

### Game Specifications

- **Tracks:** 3+ unique courses
- **Road:** Segment-based pseudo-3D
- **Player Car:** Multiple sprites for scaling
- **Rivals:** Up to 4 on screen
- **Speed:** 0-200+ mph simulation
- **Modes:** Time trial, championship, two-player
- **Weather:** Clear, rain, day/night
- **Controls:** Left, right, accelerate, brake
- **Audio:** Beeper engine + effects
- **Distribution:** TAP file
