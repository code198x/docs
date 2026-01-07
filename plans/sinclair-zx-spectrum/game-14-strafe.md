# Strafe: 128-Unit Outline

**Game:** 14 of 16
**Platform:** ZX Spectrum (48K/128K enhanced)
**Units:** 128 (8 phases)
**Concept:** Vertical scrolling shooter with 128K enhancements. Fight through waves of enemies with AY music and extended content.

---

## Why This Game Fourteenth?

Strafe introduces 128K Spectrum features:

1. **AY-3-8912 sound** - 3-channel music and effects
2. **Bank switching** - Extended memory for content
3. **Vertical scrolling** - Different scroll direction
4. **Sub-weapons** - Secondary fire systems
5. **Shield/power systems** - Resource management

This is the first 128K-enhanced game in the curriculum.

---

## Skills Applied from Previous Games

| Skill | From | Application in Strafe |
|-------|------|---------------------|
| Horizontal scrolling | Blitz | Adapted to vertical |
| Object pooling | Skyfire | Bullet management |
| Enemy waves | Skyfire | Formation attacks |
| Boss patterns | Recoil | Multi-phase bosses |
| Power-ups | Blitz/Recoil | Weapon upgrades |
| Frame timing | All | Smooth scrolling |

## New Skills Introduced

| Skill | Phase | Description |
|-------|-------|-------------|
| Vertical scrolling | 1 | Top-to-bottom screen movement |
| AY sound chip | 3 | 128K sound hardware |
| AY music | 3 | Multi-channel music |
| Bank switching | 6 | 128K memory paging |
| Dual-mode game | 6 | 48K/128K versions |
| Sub-weapons | 4 | Secondary fire |
| Charge attacks | 4 | Hold-to-charge mechanics |
| Score multipliers | 5 | Combo scoring |

---

## Phase 1: Vertical Scrolling (Units 1-16)
*Vertical scroll engine.*

### Units 1-4: Scroll Direction
- **Unit 1:** Vertical scroll concept - downward enemy approach
- **Unit 2:** Tile column updates - efficient vertical scroll
- **Unit 3:** Scroll speed control - variable rates
- **Unit 4:** Smooth scrolling - pixel-level vertical

### Units 5-8: Background System
- **Unit 5:** Tile-based background - scrolling tiles
- **Unit 6:** Background variety - terrain types
- **Unit 7:** Star field layer - parallax background
- **Unit 8:** Cloud layer - additional parallax

### Units 9-12: Player Ship
- **Unit 9:** Ship sprite design - spacecraft
- **Unit 10:** 8-way movement - full mobility
- **Unit 11:** Movement boundaries - screen limits
- **Unit 12:** Ship on scrolling background - layered display

### Units 13-16: Basic Play
- **Unit 13:** Auto-scroll - continuous vertical movement
- **Unit 14:** Scroll triggers - variable speed zones
- **Unit 15:** Level structure - scroll-based progression
- **Unit 16:** Playable foundation - fly through scrolling level

**Phase Goal:** Smooth vertical scrolling with player ship.

---

## Phase 2: Combat System (Units 17-32)
*Shooting and enemies.*

### Units 17-20: Primary Weapon
- **Unit 17:** Basic shot - standard projectile
- **Unit 18:** Bullet pool - efficient management
- **Unit 19:** Fire rate - shots per second
- **Unit 20:** Rapid fire - hold button to fire

### Units 21-24: Enemy Basics
- **Unit 21:** Enemy types - small, medium, large
- **Unit 22:** Enemy spawning - appear at top
- **Unit 23:** Enemy patterns - movement behaviours
- **Unit 24:** Enemy bullets - shoot at player

### Units 25-28: Combat Flow
- **Unit 25:** Bullet-enemy collision - hitting enemies
- **Unit 26:** Enemy-player collision - taking damage
- **Unit 27:** Score system - points per enemy
- **Unit 28:** Lives/shields - damage tolerance

### Units 29-32: Formation Attacks
- **Unit 29:** Formation data - enemy groupings
- **Unit 30:** Formation entry - coordinated appearance
- **Unit 31:** Formation patterns - synchronised movement
- **Unit 32:** Formation bonus - extra points for complete kill

**Phase Goal:** Core shooting gameplay.

---

## Phase 3: 128K Sound (Units 33-48)
*AY-3-8912 sound chip.*

### Units 33-36: AY Hardware
- **Unit 33:** AY chip overview - 3 tone, 1 noise channel
- **Unit 34:** AY registers - control interface
- **Unit 35:** 128K detection - which machine?
- **Unit 36:** Sound chip initialisation - setup routine

### Units 37-40: Sound Effects
- **Unit 37:** Shoot sound - weapon fire
- **Unit 38:** Explosion sound - enemy destroyed
- **Unit 39:** Power-up sound - item collected
- **Unit 40:** Player hit sound - damage taken

### Units 41-44: Music System
- **Unit 41:** Music data format - pattern/track structure
- **Unit 42:** Music player - interrupt-driven playback
- **Unit 43:** Title music - main theme
- **Unit 44:** In-game music - background track

### Units 45-48: 48K Fallback
- **Unit 45:** Beeper effects - 48K sound mode
- **Unit 46:** Conditional sound - check hardware
- **Unit 47:** Beeper music - simplified 48K music
- **Unit 48:** Dual audio system - unified interface

**Phase Goal:** Full AY sound with 48K fallback.

---

## Phase 4: Weapons Depth (Units 49-64)
*Sub-weapons and power levels.*

### Units 49-52: Power-Up System
- **Unit 49:** Power-up drops - enemies drop items
- **Unit 50:** Weapon power levels - upgrades
- **Unit 51:** Power-up types - different weapons
- **Unit 52:** Power-up visuals - distinct items

### Units 53-56: Weapon Types
- **Unit 53:** Spread shot - wide coverage
- **Unit 54:** Laser - piercing damage
- **Unit 55:** Homing missiles - tracking projectiles
- **Unit 56:** Wave beam - oscillating shot

### Units 57-60: Sub-Weapons
- **Unit 57:** Sub-weapon concept - secondary fire
- **Unit 58:** Bombs - screen-clearing attack
- **Unit 59:** Options/drones - helper ships
- **Unit 60:** Shield - temporary protection

### Units 61-64: Charge Mechanics
- **Unit 61:** Charge input - hold to charge
- **Unit 62:** Charge levels - power accumulation
- **Unit 63:** Charge release - powerful attack
- **Unit 64:** Charge visuals - charging indicator

**Phase Goal:** Deep weapon system.

---

## Phase 5: Scoring and Progression (Units 65-80)
*Combo systems and difficulty.*

### Units 65-68: Scoring Depth
- **Unit 65:** Base scores - enemy values
- **Unit 66:** Combo multiplier - consecutive kills
- **Unit 67:** Combo timer - maintain chain
- **Unit 68:** Bonus items - hidden point items

### Units 69-72: Rank System
- **Unit 69:** Dynamic difficulty - hidden rank
- **Unit 70:** Rank increase - performance raises difficulty
- **Unit 71:** Rank effects - enemy behaviour changes
- **Unit 72:** Rank display - optional visibility

### Units 73-76: Level Structure
- **Unit 73:** Level sections - themed areas
- **Unit 74:** Mid-boss encounters - mini-boss fights
- **Unit 75:** Boss warnings - alert before boss
- **Unit 76:** Level transitions - area changes

### Units 77-80: Difficulty Modes
- **Unit 77:** Easy mode - reduced enemies
- **Unit 78:** Normal mode - standard game
- **Unit 79:** Hard mode - increased challenge
- **Unit 80:** Expert mode - no continues

**Phase Goal:** Scoring depth and difficulty variety.

---

## Phase 6: 128K Memory (Units 81-96)
*Bank switching for extended content.*

### Units 81-84: Memory Banking
- **Unit 81:** 128K memory map - available banks
- **Unit 82:** Bank switching - page selection
- **Unit 83:** Contended memory - timing considerations
- **Unit 84:** Bank usage planning - data organisation

### Units 85-88: Extended Content
- **Unit 85:** Music in banks - more tracks
- **Unit 86:** Graphics in banks - more sprites
- **Unit 87:** Level data in banks - more levels
- **Unit 88:** Bank loading - runtime access

### Units 89-92: 48K Compatibility
- **Unit 89:** 48K version - reduced content
- **Unit 90:** Conditional loading - detect and branch
- **Unit 91:** Memory compression - fit in 48K
- **Unit 92:** Unified build - single binary for both

### Units 93-96: 128K Enhancements
- **Unit 93:** Extra levels - 128K exclusive content
- **Unit 94:** Extra music - more background tracks
- **Unit 95:** Extra graphics - sprite variations
- **Unit 96:** Shadow screen - double buffering option

**Phase Goal:** Full 128K utilisation with 48K compatibility.

---

## Phase 7: Boss Battles (Units 97-112)
*Epic boss encounters.*

### Units 97-100: Boss Structure
- **Unit 97:** Boss data - health, patterns, parts
- **Unit 98:** Boss sprites - large multi-sprite bosses
- **Unit 99:** Boss health bar - visual HP display
- **Unit 100:** Boss arena - scroll stops for battle

### Units 101-104: Boss Patterns
- **Unit 101:** Pattern phases - different attack modes
- **Unit 102:** Bullet patterns - danmaku-style
- **Unit 103:** Movement patterns - boss mobility
- **Unit 104:** Rage mode - low health intensifies

### Units 105-108: Boss Variety
- **Unit 105:** Level 1 boss - mechanical enemy
- **Unit 106:** Level 2 boss - organic creature
- **Unit 107:** Level 3 boss - mothership
- **Unit 108:** Final boss - ultimate challenge

### Units 109-112: Boss Polish
- **Unit 109:** Boss music - dedicated tracks
- **Unit 110:** Boss damage effects - visual feedback
- **Unit 111:** Boss explosions - destruction sequence
- **Unit 112:** Boss victory - rewards and transition

**Phase Goal:** Memorable boss battles.

---

## Phase 8: Release (Units 113-128)
*Polish and release.*

### Units 113-116: Presentation
- **Unit 113:** Title screen - game logo with music
- **Unit 114:** Attract mode - demo gameplay
- **Unit 115:** High score table - best scores
- **Unit 116:** Ending sequence - victory scenes

### Units 117-120: Game Modes
- **Unit 117:** Story mode - sequential levels
- **Unit 118:** Boss rush - bosses only
- **Unit 119:** Practice mode - level select
- **Unit 120:** Options menu - settings

### Units 121-124: Visual Polish
- **Unit 121:** Explosion variety - multiple effects
- **Unit 122:** Screen effects - flash, shake
- **Unit 123:** Score popups - earned points
- **Unit 124:** Particle effects - debris, sparks

### Units 125-128: Release
- **Unit 125:** Instructions screen
- **Unit 126:** Balance testing - difficulty tuning
- **Unit 127:** Performance testing - maintaining frame rate
- **Unit 128:** Release build - 48K/128K TAP files

**Phase Goal:** Complete shooter with 128K enhancements.

---

## Summary

**Strafe** teaches 128K development and vertical shooters:

**Phase 1 (Scrolling):** Vertical scroll engine.

**Phase 2 (Combat):** Shooting, enemies, formations.

**Phase 3 (Sound):** AY chip, music, effects.

**Phase 4 (Weapons):** Sub-weapons, upgrades.

**Phase 5 (Scoring):** Combos, rank system.

**Phase 6 (Memory):** Bank switching, 128K content.

**Phase 7 (Bosses):** Epic boss battles.

**Phase 8 (Release):** Polish, dual release.

### Skills Transferred Forward

1. **AY sound chip** → All 128K-enhanced games
2. **Bank switching** → Large games
3. **Vertical scrolling** → Different game types
4. **48K/128K compatibility** → Multi-version releases
5. **Rank systems** → Dynamic difficulty
6. **Bullet patterns** → Shooter depth

### 128K vs 48K Feature Comparison

| Feature | 48K Version | 128K Version |
|---------|-------------|--------------|
| Levels | 4 | 6 |
| Music | Beeper | AY-3-8912 |
| Sound FX | Beeper | AY-3-8912 |
| Music tracks | 2 | 6 |
| Boss music | None | Dedicated |
| Sprite banks | 1 | 3 |

### Game Specifications

- **Levels:** 4 (48K) / 6 (128K)
- **Scroll:** Vertical, variable speed
- **Player:** 16×16 ship, options
- **Weapons:** 4 main + 3 sub
- **Enemies:** 15+ types
- **Bosses:** 1 per level + final
- **Sound:** Beeper (48K) / AY (128K)
- **Music:** In-game + boss themes
- **Lives:** 3
- **Controls:** 8-way + fire + sub-weapon
- **Distribution:** 48K TAP + 128K TAP
