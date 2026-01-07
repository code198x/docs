# Platform Jump: 64-Unit Outline

**Game:** 8 - Platform Jump
**Platform:** Sinclair ZX Spectrum
**Language:** Sinclair BASIC
**Units:** 64 (4 phases)
**Prerequisite:** Pattern Match complete
**Concept:** Single-screen platformer pushing Sinclair BASIC to its limits. The transition motivator.

---

## Overview

Platform Jump is an ambitious single-screen platformer that attempts gravity, jumping, platforms, enemies, and collectibles - all in Sinclair BASIC. The game works, but the experience demonstrates exactly why Z80 assembly language is essential for action games on the Spectrum.

---

## Learning Goals

By completing Platform Jump, learners will:

- Implement gravity simulation in BASIC
- Create platform collision detection
- Build jump mechanics
- Animate enemy movement
- Handle collectible items
- Experience attribute clash problems
- Encounter BASIC's performance limits
- Be fully prepared for Z80 assembly transition

---

## Phase 1: Gravity and Platforms (Units 1-16)
*The physics foundation.*

### Units 1-4: Gravity Concept
- **Unit 1:** Y velocity variable - falling speed
- **Unit 2:** Gravity constant - acceleration per frame
- **Unit 3:** Terminal velocity - maximum fall speed
- **Unit 4:** Falling player - gravity applied

### Units 5-8: Platform Data
- **Unit 5:** Platform positions in DATA
- **Unit 6:** Platform width and Y level
- **Unit 7:** Drawing platforms - PRINT AT
- **Unit 8:** Multiple platforms displayed

### Units 9-12: Platform Collision
- **Unit 9:** Check below player - SCREEN$
- **Unit 10:** Platform detection - solid surface
- **Unit 11:** Landing - stop falling
- **Unit 12:** Standing on platform

### Units 13-16: Boundaries
- **Unit 13:** Ground level - floor
- **Unit 14:** Ceiling detection
- **Unit 15:** Screen edge boundaries
- **Unit 16:** Phase 1 complete - gravity with platforms

**Phase Goal:** Player affected by gravity, landing on platforms.

---

## Phase 2: Movement and Jumping (Units 17-32)
*Player control.*

### Units 17-20: Horizontal Movement
- **Unit 17:** Left/right INKEY$ input
- **Unit 18:** X velocity - movement speed
- **Unit 19:** Movement on ground
- **Unit 20:** Movement in air

### Units 21-24: Jump Mechanics
- **Unit 21:** Jump input - spacebar
- **Unit 22:** Jump velocity - upward force
- **Unit 23:** Jump only when grounded
- **Unit 24:** Jump arc - rise and fall

### Units 25-28: Control Feel
- **Unit 25:** Input responsiveness
- **Unit 26:** Air control - limited
- **Unit 27:** Jump height consistency
- **Unit 28:** BASIC limitations appearing

### Units 29-32: Platform Interaction
- **Unit 29:** Landing from jump
- **Unit 30:** Walking off platforms
- **Unit 31:** Jumping between platforms
- **Unit 32:** Phase 2 complete - jumping platformer

**Phase Goal:** Controllable jumping between platforms.

---

## Phase 3: Enemies and Items (Units 33-48)
*Things to avoid and collect.*

### Units 33-36: Enemy Movement
- **Unit 33:** Enemy UDG design
- **Unit 34:** Patrol movement - left/right
- **Unit 35:** Enemy on platforms
- **Unit 36:** Edge detection - turn around

### Units 37-40: Enemy Collision
- **Unit 37:** Player-enemy overlap
- **Unit 38:** Death on touch
- **Unit 39:** Respawn mechanics
- **Unit 40:** Lives system

### Units 41-44: Collectibles
- **Unit 41:** Collectible UDG design
- **Unit 42:** Collectible positions
- **Unit 43:** Collection detection
- **Unit 44:** Score for collecting

### Units 45-48: Attribute Clash
- **Unit 45:** Player/enemy colour clash
- **Unit 46:** Collectible colour clash
- **Unit 47:** Working around limitations
- **Unit 48:** Phase 3 complete - gameplay working

**Phase Goal:** Enemies to avoid, items to collect.

---

## Phase 4: Polish and Reflection (Units 49-64)
*Completing the BASIC journey.*

### Units 49-52: Multiple Screens
- **Unit 49:** Screen 2 layout
- **Unit 50:** Screen 3 layout
- **Unit 51:** Screen transitions
- **Unit 52:** Complete all = victory

### Units 53-56: Performance Reality
- **Unit 53:** Object count vs performance
- **Unit 54:** Input lag documentation
- **Unit 55:** Visual stuttering
- **Unit 56:** "This is why assembly" moment

### Units 57-60: Optimisation Attempts
- **Unit 57:** Shorter code - speed gains
- **Unit 58:** Reduced screen updates
- **Unit 59:** Simpler collision - compromises
- **Unit 60:** Best possible BASIC version

### Units 61-64: Graduation
- **Unit 61:** Final game integration
- **Unit 62:** Comparison: wanted vs achieved
- **Unit 63:** Z80 assembly preview
- **Unit 64:** **RELEASE: Platform Jump complete - BASIC curriculum complete**

**Phase Goal:** Complete BASIC journey, ready for Z80.

---

## Summary

**Platform Jump** is the Sinclair BASIC capstone:

### Technical Specifications

- **Display:** Character mode with UDGs
- **Physics:** Gravity, jumping
- **Platforms:** 5-8 per screen
- **Enemies:** 2-3 per screen
- **Collectibles:** 3-5 per screen
- **Screens:** 3 levels
- **Performance:** ~5-10 fps typical

### What We Achieved

- ✓ Gravity simulation
- ✓ Platform collision
- ✓ Jumping mechanics
- ✓ Enemy movement
- ✓ Collectibles
- ✓ Multiple screens

### What We Couldn't Achieve

- ✗ Smooth animation (too slow)
- ✗ Many colours without clash (attribute system)
- ✗ Smooth scrolling (no hardware support)
- ✗ Many enemies (performance collapse)
- ✗ Responsive controls (input lag)
- ✗ Quality sound during play (too slow)

### The Z80 Assembly Promise

| BASIC Limitation | Z80 Solution |
|------------------|--------------|
| ~5-10 fps | 25/50 fps possible |
| Attribute clash | Clever masking, timing |
| Character graphics | Pixel-level control |
| Slow movement | Direct memory writes |
| Input lag | Direct port reading |
| Simple beeps | Complex sound routines |

---

## Graduation

Completing Platform Jump means the learner has:

1. **Mastered Sinclair BASIC** - All core concepts
2. **Created 8 complete games** - Real portfolio
3. **Understood UDGs** - Custom graphics
4. **Hit the wall** - BASIC limits experienced
5. **Seen attribute clash** - Spectrum reality
6. **Motivated for assembly** - Knows why it matters

### Spectrum-Specific Lessons

Unlike the C64, the Spectrum taught:
- **Better built-in graphics** - PLOT, DRAW, CIRCLE
- **Attribute clash** - Colour cell limitations
- **UDG versatility** - 21 custom characters
- **INKEY$ immediacy** - Simpler than C64 GET
- **Different performance profile** - Faster BASIC, different limits

### Next Steps

The Z80 Assembly curriculum awaits. With BASIC foundations established, learners now understand:

- What the Spectrum can do (glimpsed in BASIC)
- What BASIC can't deliver (experienced first-hand)
- Why assembly is worth learning (the performance promise)
- The attribute clash challenge (to be mastered)

**The journey to real Spectrum game development begins.**
