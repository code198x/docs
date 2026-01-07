# Echoes of Eponium: 128-Unit Outline

**Game:** 15 of 16
**Platform:** Nintendo Entertainment System
**Units:** 128 (8 phases)
**Concept:** Metroidvania exploration. Connected world, ability-gating, backtracking, upgrades. Explore the ruins of Eponium, where echoes of the past guide your way.

---

## Why This Game Fifteenth?

Echoes of Eponium introduces Metroidvania design and MMC3:

1. **Connected world** - Large interconnected map
2. **Ability-gating** - New powers unlock areas
3. **Non-linear progression** - Player-driven exploration
4. **MMC3 mapper** - Advanced features
5. **Save system** - Password or battery backup

This is the most complex game before the capstone.

---

## Skills Applied from Previous Games

| Skill | From | Application in Echoes |
|-------|------|---------------------|
| Scrolling | Pixel Plains | World navigation |
| Room transitions | Crypt Crawler | Area connections |
| Platforming | Crate Escape | Movement physics |
| Combat | Iron Assault | Enemy fights |
| Boss battles | Thunder Run | Ability-granting bosses |
| Banking | Thunder Run | Extended content |

## New Skills Introduced

| Skill | Phase | Description |
|-------|-------|-------------|
| MMC3 mapper | 2 | Advanced banking |
| Scanline IRQ | 2 | Split effects |
| World map | 3 | Large connected map |
| Ability-gating | 4 | Progress unlocks |
| Non-linear design | 4 | Multiple paths |
| Password system | 6 | Save progress |
| Battery backup | 6 | SRAM saving |

---

## Phase 1: World Foundation (Units 1-16)
*Basic exploration framework.*

### Units 1-4: World Structure
- **Unit 1:** Zone concept - distinct areas
- **Unit 2:** Room connections - how areas link
- **Unit 3:** World map data - overall layout
- **Unit 4:** Room transitions - moving between

### Units 5-8: Player Character
- **Unit 5:** Explorer sprite - armed hero
- **Unit 6:** Movement physics - run, jump
- **Unit 7:** Player animation - full set
- **Unit 8:** Basic combat - simple attack

### Units 9-12: Room Display
- **Unit 9:** Scrolling rooms - multi-screen areas
- **Unit 10:** Room boundaries - where rooms end
- **Unit 11:** Doorways - transition points
- **Unit 12:** Room variety - different sizes

### Units 13-16: Basic Navigation
- **Unit 13:** First zone - starting area
- **Unit 14:** Connected rooms - explorable space
- **Unit 15:** Navigation flow - moving around
- **Unit 16:** Foundation - explore and fight

**Phase Goal:** Basic exploration working.

---

## Phase 2: MMC3 Mapper (Units 17-32)
*Advanced mapper features.*

### Units 17-20: MMC3 Basics
- **Unit 17:** MMC3 overview - vs MMC1
- **Unit 18:** Bank registers - configuration
- **Unit 19:** PRG banking - 8KB switchable
- **Unit 20:** CHR banking - fine control

### Units 21-24: Scanline IRQ
- **Unit 21:** IRQ concept - interrupt rendering
- **Unit 22:** Scanline counter - timing
- **Unit 23:** Status bar - fixed HUD
- **Unit 24:** Split effects - different scroll

### Units 25-28: Extended Content
- **Unit 25:** Zone graphics - per-zone CHR
- **Unit 26:** Enemy graphics - variety
- **Unit 27:** Boss graphics - large sprites
- **Unit 28:** Animation variety - more frames

### Units 29-32: Code Organisation
- **Unit 29:** Bank layout - code organisation
- **Unit 30:** Zone code - per-zone logic
- **Unit 31:** Far calls - cross-bank
- **Unit 32:** Clean architecture - organised

**Phase Goal:** MMC3 fully utilised.

---

## Phase 3: World Map (Units 33-48)
*Large connected world.*

### Units 33-36: Map Structure
- **Unit 33:** Map grid - rooms on grid
- **Unit 34:** Map data - which rooms where
- **Unit 35:** Map display - mini-map
- **Unit 36:** Map reveal - show explored

### Units 37-40: Zone Design
- **Unit 37:** Zone 1 - starting ruins
- **Unit 38:** Zone 2 - underground caves
- **Unit 39:** Zone 3 - ancient temple
- **Unit 40:** Zone 4 - final fortress

### Units 41-44: Zone Connections
- **Unit 41:** Zone transitions - moving between
- **Unit 42:** Shortcuts - unlockable paths
- **Unit 43:** Elevators - vertical movement
- **Unit 44:** Hidden passages - secrets

### Units 45-48: World Population
- **Unit 45:** Enemy placement - per zone
- **Unit 46:** Item placement - powerups
- **Unit 47:** NPC placement - hint givers
- **Unit 48:** Boss placement - guardians

**Phase Goal:** Large connected world.

---

## Phase 4: Ability System (Units 49-64)
*Ability-gating and upgrades.*

### Units 49-52: Core Abilities
- **Unit 49:** Double jump - reach high places
- **Unit 50:** Wall jump - climb walls
- **Unit 51:** Dash - horizontal burst
- **Unit 52:** Swim - water traversal

### Units 53-56: Combat Abilities
- **Unit 53:** Charge attack - powerful shot
- **Unit 54:** Upward attack - hit above
- **Unit 55:** Downward attack - hit below
- **Unit 56:** Projectile upgrade - better weapon

### Units 57-60: Ability-Gating
- **Unit 57:** Gate concept - ability required
- **Unit 58:** High ledges - double jump needed
- **Unit 59:** Wall sections - wall jump needed
- **Unit 60:** Water areas - swim needed

### Units 61-64: Non-Linear Design
- **Unit 61:** Multiple paths - player choice
- **Unit 62:** Sequence breaking - skilled play
- **Unit 63:** Soft gates - skill can bypass
- **Unit 64:** Exploration reward - hidden items

**Phase Goal:** Ability-gated exploration.

---

## Phase 5: Boss Encounters (Units 65-80)
*Ability-granting boss fights.*

### Units 65-68: Boss Framework
- **Unit 65:** Boss arenas - dedicated rooms
- **Unit 66:** Boss data - patterns, health
- **Unit 67:** Boss AI - attack sequences
- **Unit 68:** Boss rewards - ability drops

### Units 69-72: Zone Bosses
- **Unit 69:** Zone 1 boss - grants double jump
- **Unit 70:** Zone 2 boss - grants wall jump
- **Unit 71:** Zone 3 boss - grants dash
- **Unit 72:** Zone 4 boss - final challenge

### Units 73-76: Boss Design
- **Unit 73:** Boss patterns - learnable attacks
- **Unit 74:** Vulnerable windows - when to attack
- **Unit 75:** Phase transitions - harder phases
- **Unit 76:** Boss feedback - damage indication

### Units 77-80: Boss Polish
- **Unit 77:** Boss intros - dramatic entrance
- **Unit 78:** Boss music - unique themes
- **Unit 79:** Boss death - ability acquisition
- **Unit 80:** Boss rematch - optional harder

**Phase Goal:** Memorable bosses with rewards.

---

## Phase 6: Save System (Units 81-96)
*Progress persistence.*

### Units 81-84: Password System
- **Unit 81:** Password data - what to encode
- **Unit 82:** Password encoding - data to letters
- **Unit 83:** Password decoding - letters to data
- **Unit 84:** Password display - show/enter

### Units 85-88: Battery Backup
- **Unit 85:** SRAM concept - save memory
- **Unit 86:** Save data structure - what to save
- **Unit 87:** Save routine - write to SRAM
- **Unit 88:** Load routine - read from SRAM

### Units 89-92: Save Points
- **Unit 89:** Save stations - where to save
- **Unit 90:** Auto-save - checkpoint saves
- **Unit 91:** Save slots - multiple saves
- **Unit 92:** Save integrity - validation

### Units 93-96: Save Features
- **Unit 93:** Map persistence - explored areas
- **Unit 94:** Item persistence - collected items
- **Unit 95:** Ability persistence - gained powers
- **Unit 96:** Completion tracking - percentage

**Phase Goal:** Robust save system.

---

## Phase 7: Polish and Content (Units 97-112)
*Extended content and presentation.*

### Units 97-100: Hidden Content
- **Unit 97:** Secret areas - hidden rooms
- **Unit 98:** Secret items - powerful upgrades
- **Unit 99:** Optional bosses - extra challenges
- **Unit 100:** 100% completion - rewards

### Units 101-104: Audio
- **Unit 101:** Zone themes - per-area music
- **Unit 102:** Boss themes - intense tracks
- **Unit 103:** Item jingles - pickup sounds
- **Unit 104:** Atmosphere - ambient audio

### Units 105-108: Presentation
- **Unit 105:** Title screen - game logo
- **Unit 106:** Intro sequence - story setup
- **Unit 107:** Ending sequences - multiple endings
- **Unit 108:** Credits - completion reward

### Units 109-112: Player Guidance
- **Unit 109:** NPC hints - direction hints
- **Unit 110:** Environmental hints - visual cues
- **Unit 111:** Map markers - objectives
- **Unit 112:** Tutorial area - teach mechanics

**Phase Goal:** Polished content.

---

## Phase 8: Release (Units 113-128)
*Balance and release.*

### Units 113-116: World Balance
- **Unit 113:** Progression balance - fair difficulty
- **Unit 114:** Boss balance - challenging/fair
- **Unit 115:** Ability balance - all useful
- **Unit 116:** Exploration balance - rewarding

### Units 117-120: Testing
- **Unit 117:** Full playthrough - complete game
- **Unit 118:** Sequence break testing - edge cases
- **Unit 119:** Save testing - persistence works
- **Unit 120:** Performance testing - stable

### Units 121-124: Extra Features
- **Unit 121:** Hard mode - increased difficulty
- **Unit 122:** Speed run mode - timer display
- **Unit 123:** Boss rush - sequential bosses
- **Unit 124:** New Game+ - replay value

### Units 125-128: Release
- **Unit 125:** Instructions screen
- **Unit 126:** Credits and thanks
- **Unit 127:** Final testing
- **Unit 128:** Release build - final ROM (MMC3)

**Phase Goal:** Complete Metroidvania.

---

## Summary

**Echoes of Eponium** teaches Metroidvania design and MMC3.

### Game Specifications

- **World:** 4 zones, 100+ rooms
- **Player:** Full animation, multiple abilities
- **Abilities:** 8+ unlockable powers
- **Enemies:** 20+ types
- **Bosses:** 4+ zone bosses + optional
- **Items:** Health, ammo, permanent upgrades
- **Save:** Password + battery backup
- **Mapper:** MMC3
- **ROM Size:** 256KB PRG + 128KB CHR + 8KB SRAM
- **Controls:** D-pad + A (jump) + B (attack) + Select (map)
- **Distribution:** iNES ROM file
