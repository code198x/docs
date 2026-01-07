# Platform Peril: 64-Unit Outline

**Game:** 8 - Platform Peril
**Platform:** Commodore 64
**Language:** BASIC V2
**Units:** 64 (4 phases)
**Prerequisite:** Memory Match complete
**Concept:** Single-screen platformer pushing BASIC to its limits. The transition motivator.

---

## Overview

Platform Peril is an ambitious single-screen platformer that attempts gravity, jumping, platforms, enemies, and collectibles - all in BASIC. The game works, but the experience demonstrates exactly why assembly language is essential for action games on the C64.

---

## Learning Goals

By completing Platform Peril, learners will:

- Implement gravity simulation in BASIC
- Create platform collision detection
- Build jump mechanics
- Animate enemy movement
- Handle collectible items
- Experience BASIC's performance limits first-hand
- Understand what's possible vs. what's practical
- Be fully prepared for assembly transition

---

## Phase 1: Gravity and Platforms (Units 1-16)
*The physics foundation.*

### Units 1-4: Gravity Concept
- **Unit 1:** Y velocity variable - falling speed
- **Unit 2:** Gravity constant - acceleration
- **Unit 3:** Terminal velocity - maximum fall speed
- **Unit 4:** Falling player - gravity applied

### Units 5-8: Platform Data
- **Unit 5:** Platform positions in DATA
- **Unit 6:** Platform width and Y level
- **Unit 7:** Drawing platforms - POKE blocks
- **Unit 8:** Multiple platforms displayed

### Units 9-12: Platform Collision
- **Unit 9:** Check below player - PEEK
- **Unit 10:** Platform detection - solid surface
- **Unit 11:** Landing - stop falling
- **Unit 12:** Standing on platform

### Units 13-16: Ground and Ceiling
- **Unit 13:** Ground level - floor
- **Unit 14:** Ceiling detection - can't go through
- **Unit 15:** Screen boundaries
- **Unit 16:** Phase 1 complete - gravity with platforms

**Phase Goal:** Player affected by gravity, landing on platforms.

---

## Phase 2: Movement and Jumping (Units 17-32)
*Player control.*

### Units 17-20: Horizontal Movement
- **Unit 17:** Left/right input
- **Unit 18:** X velocity - movement speed
- **Unit 19:** Movement while on ground
- **Unit 20:** Movement while airborne

### Units 21-24: Jump Mechanics
- **Unit 21:** Jump input - spacebar/up
- **Unit 22:** Jump velocity - upward force
- **Unit 23:** Jump only when grounded
- **Unit 24:** Jump arc - rise and fall

### Units 25-28: Control Feel
- **Unit 25:** Input responsiveness
- **Unit 26:** Air control - some movement
- **Unit 27:** Jump height consistency
- **Unit 28:** BASIC limitations appearing

### Units 29-32: Platform Interaction
- **Unit 29:** Landing on platforms from jump
- **Unit 30:** Walking off platforms - fall
- **Unit 31:** Jumping to reach higher platforms
- **Unit 32:** Phase 2 complete - jumping platformer

**Phase Goal:** Controllable jumping between platforms.

---

## Phase 3: Enemies and Collectibles (Units 33-48)
*Things to avoid and collect.*

### Units 33-36: Enemy Movement
- **Unit 33:** Enemy position variables
- **Unit 34:** Patrol movement - left and right
- **Unit 35:** Enemy on platforms
- **Unit 36:** Edge detection - enemy turns

### Units 37-40: Enemy Collision
- **Unit 37:** Player-enemy overlap check
- **Unit 38:** Death on enemy touch
- **Unit 39:** Respawn after death
- **Unit 40:** Lives system

### Units 41-44: Collectibles
- **Unit 41:** Collectible item positions
- **Unit 42:** Drawing collectibles
- **Unit 43:** Collection detection
- **Unit 44:** Score for collecting

### Units 45-48: Level Goal
- **Unit 45:** Exit/goal position
- **Unit 46:** Goal detection
- **Unit 47:** Level complete
- **Unit 48:** Phase 3 complete - gameplay elements working

**Phase Goal:** Enemies to avoid, items to collect.

---

## Phase 4: Polish and Reflection (Units 49-64)
*Completing the BASIC journey.*

### Units 49-52: Multiple Screens
- **Unit 49:** Screen 2 layout
- **Unit 50:** Screen 3 layout
- **Unit 51:** Screen progression
- **Unit 52:** Complete all screens - victory

### Units 53-56: Performance Reality
- **Unit 53:** Object count vs. frame rate
- **Unit 54:** Input lag documentation
- **Unit 55:** Visual stuttering observation
- **Unit 56:** "This is why assembly" moment

### Units 57-60: Doing Our Best
- **Unit 57:** Optimisation attempts - shorter code
- **Unit 58:** Reduced screen updates
- **Unit 59:** Simpler collision - compromises
- **Unit 60:** Best possible BASIC version

### Units 61-64: Graduation
- **Unit 61:** Final game integration
- **Unit 62:** Comparison: what we wanted vs. got
- **Unit 63:** Assembly preview - what it enables
- **Unit 64:** **RELEASE: Platform Peril complete - BASIC curriculum complete**

**Phase Goal:** Complete BASIC journey, ready for assembly.

---

## Summary

**Platform Peril** is the BASIC curriculum capstone:

### Technical Specifications

- **Display:** Character mode (40×25)
- **Physics:** Gravity, jumping
- **Platforms:** 5-8 per screen
- **Enemies:** 2-3 per screen
- **Collectibles:** 3-5 per screen
- **Screens:** 3 levels
- **Performance:** ~5-10 fps

### What We Achieved

- ✓ Gravity simulation
- ✓ Platform collision
- ✓ Jumping mechanics
- ✓ Enemy movement
- ✓ Collectibles
- ✓ Multiple screens

### What We Couldn't Achieve

- ✗ Smooth animation (too slow)
- ✗ Hardware sprites (no access in BASIC)
- ✗ Smooth scrolling (no hardware support)
- ✗ Many enemies (performance collapse)
- ✗ Responsive controls (input lag)
- ✗ Sound effects during gameplay (too slow)

### The Assembly Promise

| BASIC Limitation | Assembly Solution |
|------------------|-------------------|
| ~5-10 fps | 50/60 fps possible |
| Character graphics only | Hardware sprites |
| No scrolling | Hardware scroll registers |
| 2-3 enemies max | 8 sprites + multiplexing |
| Input lag | Immediate response |
| Simple sounds | Full SID chip access |

---

## Graduation

Completing Platform Peril means the learner has:

1. **Mastered BASIC V2** - All core concepts understood
2. **Created 8 complete games** - Real portfolio
3. **Understood hardware** - Screen memory, colours
4. **Hit the wall** - Experienced BASIC's limits
5. **Motivated for assembly** - Knows why it matters

### Next Steps

The 6510 Assembly curriculum awaits. With BASIC foundations established, learners now understand:

- What the C64 can do (glimpsed in BASIC)
- What BASIC can't deliver (experienced first-hand)
- Why assembly is worth learning (the performance promise)

**The journey to real C64 game development begins.**
