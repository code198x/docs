# Scroll Quest: 64-Unit Outline

**Game:** 8 of 8 (AMOS BASIC)
**Platform:** Commodore Amiga
**Language:** AMOS BASIC
**Units:** 64 (4 phases)
**Concept:** Side-scrolling platformer. A scrolling world built in AMOS - seeing both capabilities and limitations.

---

## Why This Game Last?

Scroll Quest demonstrates AMOS's boundaries:

1. **SCREEN OFFSET** - AMOS scrolling commands
2. **Large levels** - Extended world design
3. **Camera systems** - Player following
4. **Performance limits** - Where AMOS struggles
5. **Assembly motivation** - Why 68000 is needed

The perfect transition point to assembly.

---

## Skills Applied from Previous Games

| Skill | From | Application in Scroll Quest |
|-------|------|----------------------------|
| Platforming | Crate Stack | Movement physics |
| Tile rendering | Maze Runner | Level graphics |
| Enemy AI | Maze Runner | Scrolling enemies |
| Level data | All | Large world storage |
| State management | Dungeon Doors | Progress tracking |

## New Skills Introduced

| Skill | Phase | Description |
|-------|-------|-------------|
| SCREEN OFFSET | 1 | AMOS scrolling |
| Large level storage | 2 | Extended data |
| Camera following | 2 | Smooth tracking |
| Parallax attempt | 3 | Multi-layer scroll |
| Performance analysis | 4 | Understanding limits |

---

## Phase 1: Scrolling Basics (Units 1-16)
*AMOS scrolling mechanics.*

### Units 1-4: SCREEN OFFSET
- **Unit 1:** Scrolling concept - moving view
- **Unit 2:** SCREEN OFFSET - X offset
- **Unit 3:** Pixel scrolling - smooth movement
- **Unit 4:** Scroll limits - range

### Units 5-8: Scrolling Display
- **Unit 5:** Large screen - oversized buffer
- **Unit 6:** Visible area - what player sees
- **Unit 7:** Scroll direction - left/right
- **Unit 8:** Basic scroll demo

### Units 9-12: Player and Scroll
- **Unit 9:** Player position - world vs screen
- **Unit 10:** Screen tracking - follow player
- **Unit 11:** Scroll margins - when to scroll
- **Unit 12:** Combined movement

### Units 13-16: Scroll Mechanics
- **Unit 13:** Scroll speed - matching player
- **Unit 14:** Scroll boundaries - level edges
- **Unit 15:** Scroll smoothness
- **Unit 16:** Scrolling foundation

**Phase Goal:** Smooth horizontal scrolling.

---

## Phase 2: Large Levels (Units 17-32)
*Extended world design.*

### Units 17-20: Level Data
- **Unit 17:** Level width - extended size
- **Unit 18:** Tile data - large arrays
- **Unit 19:** Data organisation - sections
- **Unit 20:** Memory usage - considerations

### Units 21-24: Level Rendering
- **Unit 21:** Visible tiles - only on screen
- **Unit 22:** Tile streaming - load as needed
- **Unit 23:** Render optimisation
- **Unit 24:** Large level display

### Units 25-28: Camera System
- **Unit 25:** Camera position - independent
- **Unit 26:** Camera following - smooth
- **Unit 27:** Dead zone - no scroll area
- **Unit 28:** Look ahead - scroll direction

### Units 29-32: Level Design
- **Unit 29:** Level structure - start to end
- **Unit 30:** Platform placement - scrolling world
- **Unit 31:** Collectible placement
- **Unit 32:** Checkpoint placement

**Phase Goal:** Large scrolling levels.

---

## Phase 3: Scrolling World (Units 33-48)
*Enemies, hazards, parallax.*

### Units 33-36: Scrolling Enemies
- **Unit 33:** Enemy placement - world position
- **Unit 34:** Enemy activation - when visible
- **Unit 35:** Enemy movement - in scrolling
- **Unit 36:** Enemy deactivation - off screen

### Units 37-40: Scrolling Hazards
- **Unit 37:** Static hazards - spikes, pits
- **Unit 38:** Moving hazards - platforms
- **Unit 39:** Hazard collision - with scroll
- **Unit 40:** Hazard variety

### Units 41-44: Parallax Attempt
- **Unit 41:** Background layer - slower scroll
- **Unit 42:** Foreground layer - faster scroll
- **Unit 43:** AMOS parallax - what's possible
- **Unit 44:** Performance impact - slowdown

### Units 45-48: Level Progression
- **Unit 45:** Level 1 - learning
- **Unit 46:** Level 2 - challenging
- **Unit 47:** Level 3 - expert
- **Unit 48:** Level transitions

**Phase Goal:** Complete scrolling platformer.

---

## Phase 4: Limits and Completion (Units 49-64)
*Performance analysis and transition prep.*

### Units 49-52: AMOS Limitations
- **Unit 49:** Performance profiling - frame rate
- **Unit 50:** Sprite limits - too many objects
- **Unit 51:** Scroll speed - maximum smooth
- **Unit 52:** Memory constraints - level size

### Units 53-56: Why Assembly?
- **Unit 53:** Hardware scrolling - Agnus/Copper
- **Unit 54:** Blitter efficiency - vs AMOS bobs
- **Unit 55:** Sprite control - hardware registers
- **Unit 56:** The assembly advantage

### Units 57-60: Game Polish
- **Unit 57:** Title screen
- **Unit 58:** Sound effects - jump, collect
- **Unit 59:** Background music
- **Unit 60:** HUD and scoring

### Units 61-64: Completion
- **Unit 61:** Full level design
- **Unit 62:** High scores
- **Unit 63:** Full testing
- **Unit 64:** Release build - transition ready

**Phase Goal:** Complete game + assembly motivation.

---

## Summary

**Scroll Quest** demonstrates AMOS limits and motivates assembly.

### Game Specifications

- **Player:** Animated runner, full physics
- **Scrolling:** SCREEN OFFSET horizontal
- **Levels:** 3 extended stages
- **Enemies:** Scrolling world placement
- **Hazards:** Static and moving
- **Parallax:** Basic attempt (limited)
- **Checkpoints:** Progress saving
- **Display:** AMOS oversized screen
- **Sound:** Effects and music
- **Distribution:** AMOS source + compiled

### Transition to 68000 Assembly

After completing Scroll Quest, learners will understand:

| AMOS Limitation | 68000 Solution |
|-----------------|----------------|
| Slow scrolling | Hardware scroll registers |
| Limited sprites | Direct hardware sprites |
| No Copper | Full Copper control |
| Blitter inefficiency | Direct Blitter programming |
| Audio limitations | Paula registers |
| Memory constraints | Bank switching, optimisation |

The 68000 Assembly curriculum (2,048 units) teaches these solutions from the ground up.
