# Space Dodge: 64-Unit Outline

**Game:** 6 - Space Dodge
**Platform:** Commodore 64
**Language:** BASIC V2
**Units:** 64 (4 phases)
**Prerequisite:** Snake Trail complete
**Concept:** Vertical scrolling avoidance game. Dodge obstacles moving down the screen - exploring BASIC's limits.

---

## Overview

Space Dodge puts the player's ship at the bottom of the screen as obstacles scroll downward. The player must weave through gaps to survive as long as possible. This game explores simulated scrolling and multiple object management, revealing BASIC's performance limitations.

---

## Learning Goals

By completing Space Dodge, learners will:

- Implement simulated vertical scrolling
- Manage many simultaneous objects
- Create difficulty ramping systems
- Track and display high scores
- Understand custom character concepts
- Recognise BASIC performance limits
- Optimise BASIC code for speed
- Prepare mentally for assembly transition

---

## Phase 1: Scrolling Concept (Units 1-16)
*Objects moving downward.*

### Units 1-4: Object Movement
- **Unit 1:** Objects moving down the screen
- **Unit 2:** Y position increment each frame
- **Unit 3:** Multiple Y positions tracked
- **Unit 4:** Objects reaching bottom

### Units 5-8: Object Respawn
- **Unit 5:** Respawn at top when reaching bottom
- **Unit 6:** Random X position on respawn
- **Unit 7:** Continuous flow of objects
- **Unit 8:** Illusion of forward movement

### Units 9-12: Object Rows
- **Unit 9:** Row concept - obstacles with gaps
- **Unit 10:** Gap position randomisation
- **Unit 11:** Gap width - playable space
- **Unit 12:** Row generation

### Units 13-16: Scroll Effect
- **Unit 13:** Multiple rows at different Y
- **Unit 14:** Staggered row spacing
- **Unit 15:** Continuous scroll feeling
- **Unit 16:** Phase 1 complete - scrolling obstacles

**Phase Goal:** Objects scrolling downward with gaps.

---

## Phase 2: Player and Collision (Units 17-32)
*Dodge the obstacles.*

### Units 17-20: Player Ship
- **Unit 17:** Ship position at bottom
- **Unit 18:** Ship character(s) - multi-char design
- **Unit 19:** Left/right movement
- **Unit 20:** Smooth responsive controls

### Units 21-24: Collision Detection
- **Unit 21:** Ship hitbox definition
- **Unit 22:** PEEK for collision checking
- **Unit 23:** Collision with obstacles
- **Unit 24:** Death on collision

### Units 25-28: Game Loop
- **Unit 25:** Main loop structure
- **Unit 26:** Input processing
- **Unit 27:** Object updates
- **Unit 28:** Collision checks each frame

### Units 29-32: Game State
- **Unit 29:** Lives system
- **Unit 30:** Invulnerability after hit
- **Unit 31:** Game over condition
- **Unit 32:** Phase 2 complete - playable dodge game

**Phase Goal:** Complete dodge gameplay with collision.

---

## Phase 3: Scoring and Difficulty (Units 33-48)
*Progressive challenge.*

### Units 33-36: Scoring System
- **Unit 33:** Distance/time scoring
- **Unit 34:** Score increment per frame
- **Unit 35:** Bonus for close calls
- **Unit 36:** Score display

### Units 37-40: Difficulty Ramping
- **Unit 37:** Speed increase over time
- **Unit 38:** Narrower gaps as score rises
- **Unit 39:** More obstacles per row
- **Unit 40:** Difficulty plateau - maximum

### Units 41-44: High Score
- **Unit 41:** High score variable
- **Unit 42:** New high score detection
- **Unit 43:** High score display
- **Unit 44:** Name entry for high score

### Units 45-48: Visual Feedback
- **Unit 45:** Speed visual effects
- **Unit 46:** Close call indicator
- **Unit 47:** Death animation
- **Unit 48:** Phase 3 complete - full scoring system

**Phase Goal:** Progressive difficulty with high scores.

---

## Phase 4: Performance and Limits (Units 49-64)
*Pushing BASIC to the edge.*

### Units 49-52: Performance Analysis
- **Unit 49:** Counting objects - how many before slowdown
- **Unit 50:** Frame rate observation
- **Unit 51:** Input lag awareness
- **Unit 52:** The BASIC bottleneck

### Units 53-56: Optimisation Attempts
- **Unit 53:** Shorter variable names
- **Unit 54:** Calculated POKE addresses
- **Unit 55:** Reduced PEEK checks
- **Unit 56:** Limits of optimisation

### Units 57-60: Custom Characters Intro
- **Unit 57:** Character set pointer - POKE 53272
- **Unit 58:** Character RAM location
- **Unit 59:** Designing custom shapes
- **Unit 60:** Simple custom character example

### Units 61-64: Final Game and Reflection
- **Unit 61:** All features integrated
- **Unit 62:** Performance documentation
- **Unit 63:** "Why assembly matters" discussion
- **Unit 64:** **RELEASE: Space Dodge complete**

**Phase Goal:** Understand BASIC limits through experience.

---

## Summary

**Space Dodge** reveals BASIC's performance boundaries:

### Technical Specifications

- **Display:** Character mode (40×25)
- **Objects:** 8-12 obstacle rows
- **Input:** Real-time keyboard
- **Scroll:** Simulated vertical
- **Features:** Progressive difficulty, high scores
- **Performance:** ~10-15 fps typical

### Skills Learned

- Simulated scrolling technique
- Multiple object management
- Difficulty progression design
- High score systems
- BASIC optimisation techniques
- Custom character introduction
- Performance awareness
- Transition motivation

### Performance Observations

| Objects | Frame Rate | Playability |
|---------|-----------|-------------|
| 4 rows | Good | Smooth |
| 8 rows | Fair | Acceptable |
| 12 rows | Poor | Sluggish |
| 16+ rows | Bad | Unplayable |

### Why Assembly Is Needed

This game demonstrates:
- **Slow execution** - interpreted BASIC can't keep up
- **No hardware scroll** - must redraw everything
- **Limited objects** - can't handle many moving items
- **Input lag** - controls feel sluggish

### Progression

This game prepares learners for **Memory Match** where they'll create custom characters for card graphics and implement turn-based gameplay that doesn't suffer from speed issues.
