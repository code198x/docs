# Thunder Run: 128-Unit Outline

**Game:** 11 of 16
**Platform:** Nintendo Entertainment System
**Units:** 128 (8 phases)
**Concept:** Vertical scrolling shooter. 1942-style aerial combat with formations, bullet patterns, and dramatic boss encounters. The thunder of engines fills the sky.

---

## Why This Game Eleventh?

Thunder Run introduces vertical scrolling and NES mappers:

1. **Vertical scrolling** - Different scroll direction
2. **MMC1 mapper** - First use of bank switching
3. **Extended CHR** - More graphics via banking
4. **Bullet patterns** - Enemy fire patterns
5. **Large bosses** - Multi-sprite boss construction

This is the first advanced game, introducing mappers.

---

## Skills Applied from Previous Games

| Skill | From | Application in Thunder Run |
|-------|------|--------------------------|
| Horizontal scrolling | Pixel Plains | Adapted to vertical |
| Shooter mechanics | Ion Trail | Combat foundation |
| Enemy waves | Stellar Barrage | Formation attacks |
| Boss patterns | Ion Trail | Enhanced boss fights |
| Object pooling | All | Bullet management |

## New Skills Introduced

| Skill | Phase | Description |
|-------|-------|-------------|
| Vertical scrolling | 1 | Top-to-bottom scroll |
| MMC1 mapper | 2 | Bank switching basics |
| CHR banking | 2 | Graphics bank switching |
| PRG banking | 3 | Code/data bank switching |
| Bullet patterns | 4 | Geometric enemy fire |
| Multi-sprite bosses | 5 | Large sprite constructs |
| Ground targets | 6 | Dual target types |

---

## Phase 1: Vertical Scrolling (Units 1-16)
*Vertical scroll engine.*

### Units 1-4: Scroll Direction
- **Unit 1:** Vertical scroll concept - Y scroll register
- **Unit 2:** Nametable for vertical - arrangement
- **Unit 3:** Scroll speed - rate control
- **Unit 4:** Smooth scrolling - seamless vertical

### Units 5-8: Background System
- **Unit 5:** Terrain tiles - sky, clouds, ground
- **Unit 6:** Row updates - new rows at top
- **Unit 7:** Level data - column format adapted
- **Unit 8:** Attribute handling - vertical attributes

### Units 9-12: Player Aircraft
- **Unit 9:** Plane sprite - fighter aircraft
- **Unit 10:** 8-way movement - full mobility
- **Unit 11:** Screen boundaries - play area limits
- **Unit 12:** Plane on scrolling - layered display

### Units 13-16: Basic Play
- **Unit 13:** Auto-scroll - continuous vertical
- **Unit 14:** Basic shooting - upward bullets
- **Unit 15:** Simple enemies - first targets
- **Unit 16:** Playable foundation - fly and shoot vertically

**Phase Goal:** Vertical scrolling shooter basics.

---

## Phase 2: MMC1 Mapper Basics (Units 17-32)
*Introduction to bank switching.*

### Units 17-20: Mapper Concept
- **Unit 17:** Why mappers - exceeding NROM limits
- **Unit 18:** MMC1 overview - capabilities
- **Unit 19:** Mapper registers - configuration
- **Unit 20:** iNES header - mapper identification

### Units 21-24: CHR Banking
- **Unit 21:** CHR bank concept - multiple tile sets
- **Unit 22:** Bank switching - selecting CHR bank
- **Unit 23:** Graphics variety - more sprites/tiles
- **Unit 24:** Animation via banking - tile swap animation

### Units 25-28: Level Variety
- **Unit 25:** Multiple tilesets - different environments
- **Unit 26:** Environment 1 - sky/clouds
- **Unit 27:** Environment 2 - ocean
- **Unit 28:** Environment switching - bank per level

### Units 29-32: Extended Graphics
- **Unit 29:** More enemy types - expanded sprites
- **Unit 30:** More terrain - varied backgrounds
- **Unit 31:** Effect graphics - explosions variety
- **Unit 32:** Visual variety - rich graphics

**Phase Goal:** MMC1 CHR banking working.

---

## Phase 3: PRG Banking (Units 33-48)
*Code and data bank switching.*

### Units 33-36: PRG Bank Switching
- **Unit 33:** PRG bank concept - code/data banks
- **Unit 34:** Fixed bank - always-accessible code
- **Unit 35:** Switchable bank - swappable code/data
- **Unit 36:** Bank organisation - what goes where

### Units 37-40: Level Data Banking
- **Unit 37:** Level data in banks - per-level data
- **Unit 38:** Bank loading - switch for level
- **Unit 39:** Level transitions - bank changes
- **Unit 40:** Memory efficiency - larger game

### Units 41-44: Code Organisation
- **Unit 41:** Fixed routines - critical code
- **Unit 42:** Banked routines - level-specific
- **Unit 43:** Far calls - calling banked code
- **Unit 44:** Clean architecture - organised banking

### Units 45-48: Enemy Management
- **Unit 45:** Enemy data per level - in banks
- **Unit 46:** Pattern data - movement patterns
- **Unit 47:** Formation data - group definitions
- **Unit 48:** Rich enemy variety - many types

**Phase Goal:** Full PRG banking utilised.

---

## Phase 4: Bullet Patterns (Units 49-64)
*Geometric enemy fire patterns.*

### Units 49-52: Basic Patterns
- **Unit 49:** Aimed shot - bullet toward player
- **Unit 50:** Spread shot - multiple angles
- **Unit 51:** Ring pattern - circular burst
- **Unit 52:** Pattern variety - different enemies

### Units 53-56: Complex Patterns
- **Unit 53:** Stream pattern - continuous fire
- **Unit 54:** Spiral pattern - rotating fire
- **Unit 55:** Wall pattern - horizontal barrier
- **Unit 56:** Mixed patterns - combined types

### Units 57-60: Pattern Management
- **Unit 57:** Pattern timing - when to fire
- **Unit 58:** Pattern density - difficulty control
- **Unit 59:** Pattern pools - bullet management
- **Unit 60:** Screen clearing - too many bullets

### Units 61-64: Player Defence
- **Unit 61:** Small hitbox - player precision
- **Unit 62:** Grazing bonus - near misses
- **Unit 63:** Bomb system - clear screen
- **Unit 64:** Pattern reading - player skill

**Phase Goal:** Rich bullet pattern system.

---

## Phase 5: Boss Construction (Units 65-80)
*Large multi-sprite bosses.*

### Units 65-68: Multi-Sprite Bosses
- **Unit 65:** Boss sprite layout - many sprites
- **Unit 66:** Boss assembly - constructing large enemy
- **Unit 67:** Boss parts - destroyable sections
- **Unit 68:** Boss display - managing sprites

### Units 69-72: Boss Behaviour
- **Unit 69:** Boss entry - dramatic entrance
- **Unit 70:** Boss patterns - attack sequences
- **Unit 71:** Boss phases - changing behaviour
- **Unit 72:** Weak points - where to attack

### Units 73-76: Boss Variety
- **Unit 73:** Stage 1 boss - fighter squadron
- **Unit 74:** Stage 2 boss - battleship
- **Unit 75:** Stage 3 boss - flying fortress
- **Unit 76:** Final boss - ultimate challenge

### Units 77-80: Boss Polish
- **Unit 77:** Boss health display - visual HP
- **Unit 78:** Boss damage feedback - hit reactions
- **Unit 79:** Boss death - dramatic explosion
- **Unit 80:** Boss rewards - points, continues

**Phase Goal:** Epic boss encounters.

---

## Phase 6: Ground and Air (Units 81-96)
*Dual target systems.*

### Units 81-84: Ground Targets
- **Unit 81:** Ground enemy concept - static/moving
- **Unit 82:** Ground collision - bombs only
- **Unit 83:** Bomb weapon - downward attack
- **Unit 84:** Ground destruction - remove targets

### Units 85-88: Mixed Combat
- **Unit 85:** Air enemies - standard targets
- **Unit 86:** Dual targeting - air and ground
- **Unit 87:** Strategic choice - what to prioritise
- **Unit 88:** Score bonuses - ground targets

### Units 89-92: Stage Design
- **Unit 89:** Stage 1 design - introduction
- **Unit 90:** Stage 2 design - ocean assault
- **Unit 91:** Stage 3 design - enemy base
- **Unit 92:** Stage progression - difficulty curve

### Units 93-96: Power-Ups
- **Unit 93:** Weapon upgrades - spread, laser
- **Unit 94:** Speed upgrades - faster movement
- **Unit 95:** Bomb stock - limited bombs
- **Unit 96:** Power progression - upgrade path

**Phase Goal:** Complete dual-target combat.

---

## Phase 7: Polish and Features (Units 97-112)
*Audio, presentation, and modes.*

### Units 97-100: Audio System
- **Unit 97:** Sound effects - comprehensive set
- **Unit 98:** Stage music - per-level themes
- **Unit 99:** Boss music - intense tracks
- **Unit 100:** Victory music - stage clear

### Units 101-104: Presentation
- **Unit 101:** Title screen - game logo
- **Unit 102:** Stage intro - level name
- **Unit 103:** Boss warning - alert display
- **Unit 104:** Results screen - stage stats

### Units 105-108: Game Modes
- **Unit 105:** Normal mode - standard game
- **Unit 106:** Hard mode - increased difficulty
- **Unit 107:** Two-player - alternating turns
- **Unit 108:** Options menu - settings

### Units 109-112: Polish
- **Unit 109:** Visual effects - explosions, flashes
- **Unit 110:** Screen shake - impact feedback
- **Unit 111:** Attract mode - demo play
- **Unit 112:** High scores - best scores

**Phase Goal:** Polished presentation.

---

## Phase 8: Release (Units 113-128)
*Final polish and release.*

### Units 113-116: Balance
- **Unit 113:** Difficulty tuning - fair challenge
- **Unit 114:** Pattern balance - learnable patterns
- **Unit 115:** Boss balance - achievable fights
- **Unit 116:** Progression curve - smooth difficulty

### Units 117-120: Testing
- **Unit 117:** Playthrough testing - complete game
- **Unit 118:** Mapper testing - banking works
- **Unit 119:** Edge cases - unusual situations
- **Unit 120:** Performance - consistent frame rate

### Units 121-124: Extra Content
- **Unit 121:** Hidden stage - secret level
- **Unit 122:** Extra ship - unlockable
- **Unit 123:** Score attack - high score focus
- **Unit 124:** Achievements - completion markers

### Units 125-128: Release
- **Unit 125:** Instructions screen
- **Unit 126:** Credits screen
- **Unit 127:** Final testing
- **Unit 128:** Release build - final iNES ROM (MMC1)

**Phase Goal:** Complete vertical shooter.

---

## Summary

**Thunder Run** teaches vertical scrolling and MMC1 mapper:

**Phase 1 (Vertical):** Vertical scroll engine.

**Phase 2 (CHR):** CHR bank switching.

**Phase 3 (PRG):** PRG bank switching.

**Phase 4 (Patterns):** Bullet patterns.

**Phase 5 (Bosses):** Multi-sprite bosses.

**Phase 6 (Combat):** Ground and air targets.

**Phase 7 (Polish):** Audio, presentation.

**Phase 8 (Release):** Balance, release.

### Skills Transferred Forward

1. **Vertical scrolling** → Different scroll contexts
2. **MMC1 mapper** → Bank switching foundation
3. **CHR banking** → Extended graphics
4. **PRG banking** → Larger games
5. **Bullet patterns** → Shooter depth
6. **Multi-sprite bosses** → Large enemies

### Game Specifications

- **Levels:** 4-6 stages
- **Scroll:** Vertical auto-scroll
- **Player:** Fighter with bombs
- **Weapons:** 3 types with upgrades
- **Enemies:** 20+ types
- **Bosses:** 1 per stage + final
- **Lives:** 3
- **Mapper:** MMC1
- **ROM Size:** 128KB PRG + 64KB CHR
- **Controls:** 8-way + A (fire) + B (bomb)
- **Audio:** APU effects + music
- **Distribution:** iNES ROM file
