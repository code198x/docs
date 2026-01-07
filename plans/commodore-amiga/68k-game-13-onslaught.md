# Onslaught: 128-Unit Outline

**Game:** 13 of 16 (68000 Assembly)
**Platform:** Commodore Amiga
**Language:** 68000 Assembly
**Units:** 128 (8 phases)
**Concept:** Vertical scrolling shooter with bullet patterns.

---

## Why This Game Thirteenth?

Onslaught introduces bullet hell mechanics:

1. **Vertical scrolling** - Different scroll direction
2. **Bullet patterns** - Complex enemy fire
3. **Rank system** - Dynamic difficulty
4. **Multi-phase bosses** - Complex encounters
5. **Weapon upgrade trees** - Progression systems

The pinnacle of shooter design before isometric.

---

## Skills Applied from Previous Games

| Skill | From | Application |
|-------|------|-------------|
| Parallax scrolling | Parallax | Backgrounds |
| Object pools | Multiple | Bullets, enemies |
| Boss patterns | Parallax | Boss fights |
| Collision | All | Hit detection |
| MOD replay | Parallax | Soundtrack |

## New Skills Introduced

| Skill | Phase | Description |
|-------|-------|-------------|
| Vertical scroll | 1 | Top-to-bottom |
| Bullet patterns | 2 | Geometric fire |
| Rank system | 4 | Dynamic difficulty |
| Upgrade trees | 3 | Branching power |
| Multi-phase bosses | 5 | Complex fights |

---

## Phase 1: Vertical Scrolling (Units 1-16)
*Top-down scroll implementation.*

### Units 1-4: Scroll Direction
- **Unit 1:** Vertical vs horizontal - differences
- **Unit 2:** Scroll registers - vertical setup
- **Unit 3:** Modulo calculation - vertical
- **Unit 4:** Basic vertical scroll

### Units 5-8: Level Display
- **Unit 5:** Level tiles - top-down view
- **Unit 6:** Tile updates - new rows
- **Unit 7:** Scroll speed - game pace
- **Unit 8:** Seamless scrolling

### Units 9-12: Parallax Layers
- **Unit 9:** Ground layer - main terrain
- **Unit 10:** Cloud layer - slower
- **Unit 11:** Layer coordination
- **Unit 12:** Vertical parallax demo

### Units 13-16: Player Setup
- **Unit 13:** Ship sprite - top-down
- **Unit 14:** Movement - 8-directional
- **Unit 15:** Ship boundaries
- **Unit 16:** Basic vertical shooter

**Phase Goal:** Vertical scrolling display.

---

## Phase 2: Bullet Systems (Units 17-32)
*Pattern-based enemy fire.*

### Units 17-20: Bullet Pool
- **Unit 17:** Large bullet pool - 100+
- **Unit 18:** Bullet types - sizes, speeds
- **Unit 19:** Pool management - efficient
- **Unit 20:** Bullet rendering - small BOBs

### Units 21-24: Bullet Patterns
- **Unit 21:** Pattern concept - geometric
- **Unit 22:** Spread shot - fan pattern
- **Unit 23:** Circle shot - radial
- **Unit 24:** Aimed shot - toward player

### Units 25-28: Complex Patterns
- **Unit 25:** Spiral pattern - rotating
- **Unit 26:** Wave pattern - sinusoidal
- **Unit 27:** Burst pattern - repeated
- **Unit 28:** Combined patterns

### Units 29-32: Pattern Data
- **Unit 29:** Pattern definition - data tables
- **Unit 30:** Pattern timing - intervals
- **Unit 31:** Pattern triggering - by enemy
- **Unit 32:** Bullet pattern demo

**Phase Goal:** Bullet pattern system.

---

## Phase 3: Weapon System (Units 33-48)
*Player upgrades.*

### Units 33-36: Basic Weapons
- **Unit 33:** Standard shot - single bullet
- **Unit 34:** Power shot - stronger
- **Unit 35:** Rapid fire - faster
- **Unit 36:** Weapon switching

### Units 37-40: Special Weapons
- **Unit 37:** Spread weapon - wide
- **Unit 38:** Laser weapon - continuous
- **Unit 39:** Missile weapon - homing
- **Unit 40:** Bomb weapon - screen clear

### Units 41-44: Upgrade Tree
- **Unit 41:** Upgrade concept - power levels
- **Unit 42:** Power-up collection - from enemies
- **Unit 43:** Upgrade paths - branching
- **Unit 44:** Downgrade on death

### Units 45-48: Weapon Effects
- **Unit 45:** Weapon visuals - different sprites
- **Unit 46:** Weapon sounds - unique
- **Unit 47:** Charge shots - hold to charge
- **Unit 48:** Weapon balance

**Phase Goal:** Complete weapon system.

---

## Phase 4: Dynamic Difficulty (Units 49-64)
*Rank system.*

### Units 49-52: Rank Concept
- **Unit 49:** Rank overview - hidden difficulty
- **Unit 50:** Rank increase - survival, kills
- **Unit 51:** Rank decrease - deaths
- **Unit 52:** Rank display - hidden or shown

### Units 53-56: Rank Effects
- **Unit 53:** Bullet speed - by rank
- **Unit 54:** Bullet density - more bullets
- **Unit 55:** Enemy aggression - behaviour
- **Unit 56:** Power-up frequency - fewer at high rank

### Units 57-60: Enemy Scaling
- **Unit 57:** Enemy health - by rank
- **Unit 58:** Enemy patterns - more complex
- **Unit 59:** Boss patterns - harder
- **Unit 60:** Balanced challenge

### Units 61-64: Ground Targets
- **Unit 61:** Ground units - tanks, turrets
- **Unit 62:** Ground collision - different
- **Unit 63:** Ground destruction - bonus
- **Unit 64:** Air/ground balance

**Phase Goal:** Dynamic difficulty system.

---

## Phase 5: Boss Design (Units 65-80)
*Multi-phase encounters.*

### Units 65-68: Boss Framework
- **Unit 65:** Boss size - large sprites
- **Unit 66:** Boss health - damage tracking
- **Unit 67:** Boss phases - multiple forms
- **Unit 68:** Boss transitions - between phases

### Units 69-72: Stage 1 Boss
- **Unit 69:** Boss 1 design - first boss
- **Unit 70:** Phase 1 - introduction
- **Unit 71:** Phase 2 - escalation
- **Unit 72:** Boss 1 defeat

### Units 73-76: Stage 2-3 Bosses
- **Unit 73:** Boss 2 design - mid-game
- **Unit 74:** Boss 2 phases - complex
- **Unit 75:** Boss 3 design - challenging
- **Unit 76:** Boss 3 phases - intense

### Units 77-80: Final Boss
- **Unit 77:** Final boss design - multi-part
- **Unit 78:** Final boss phases - 4+ phases
- **Unit 79:** Desperation attack - final phase
- **Unit 80:** Victory sequence

**Phase Goal:** Epic boss battles.

---

## Phase 6: Level Content (Units 81-96)
*Full stages.*

### Units 81-84: Stage 1
- **Unit 81:** Stage 1 theme - sky/clouds
- **Unit 82:** Stage 1 enemies - introductory
- **Unit 83:** Stage 1 mid-boss
- **Unit 84:** Stage 1 complete

### Units 85-88: Stage 2
- **Unit 85:** Stage 2 theme - ocean
- **Unit 86:** Stage 2 enemies - water-based
- **Unit 87:** Stage 2 hazards - waves
- **Unit 88:** Stage 2 complete

### Units 89-92: Stage 3
- **Unit 89:** Stage 3 theme - fortress
- **Unit 90:** Stage 3 enemies - military
- **Unit 91:** Stage 3 hazards - turrets
- **Unit 92:** Stage 3 complete

### Units 93-96: Stage 4
- **Unit 93:** Stage 4 theme - space
- **Unit 94:** Stage 4 enemies - alien
- **Unit 95:** Stage 4 intensity - finale
- **Unit 96:** Stage 4 complete

**Phase Goal:** Four complete stages.

---

## Phase 7: Audio and Polish (Units 97-112)
*Music and presentation.*

### Units 97-100: Soundtrack
- **Unit 97:** Stage 1 music - energetic
- **Unit 98:** Stage 2-4 music - varied
- **Unit 99:** Boss music - intense
- **Unit 100:** Victory/game over music

### Units 101-104: Sound Effects
- **Unit 101:** Weapon sounds - per type
- **Unit 102:** Explosion sounds - variety
- **Unit 103:** Enemy sounds - patterns
- **Unit 104:** UI sounds

### Units 105-108: Presentation
- **Unit 105:** Title screen
- **Unit 106:** Stage intro
- **Unit 107:** Score display
- **Unit 108:** Ranking display - letter grade

### Units 109-112: Features
- **Unit 109:** High score system
- **Unit 110:** Replay value - unlocks
- **Unit 111:** Practice mode
- **Unit 112:** Difficulty options

**Phase Goal:** Polished presentation.

---

## Phase 8: Release (Units 113-128)
*Testing and release.*

### Units 113-116: Balance
- **Unit 113:** Rank tuning
- **Unit 114:** Weapon balance
- **Unit 115:** Boss balance
- **Unit 116:** Stage balance

### Units 117-120: Testing
- **Unit 117:** Full playthrough
- **Unit 118:** Rank testing
- **Unit 119:** All weapons
- **Unit 120:** Performance

### Units 121-124: Optimisation
- **Unit 121:** Bullet optimisation
- **Unit 122:** Pattern optimisation
- **Unit 123:** Boss optimisation
- **Unit 124:** Overall tuning

### Units 125-128: Release
- **Unit 125:** Credits
- **Unit 126:** Documentation
- **Unit 127:** Final testing
- **Unit 128:** Release build - ADF

**Phase Goal:** Complete vertical shooter.

---

## Summary

**Onslaught** teaches bullet patterns and dynamic difficulty.

### Technical Specifications

- **Display:** Vertical scroll, parallax, 320×256
- **Bullets:** 100+ simultaneous, pattern-based
- **Weapons:** 4 types with upgrade trees
- **Rank:** Dynamic difficulty system
- **Stages:** 4 with multi-phase bosses
- **Targets:** Air and ground enemies
- **Audio:** Full MOD soundtrack
- **Distribution:** Bootable ADF

### Skills for Next Game

- Vertical scrolling
- Bullet pattern systems
- Dynamic difficulty (rank)
- Multi-phase boss design
- Weapon upgrade trees
