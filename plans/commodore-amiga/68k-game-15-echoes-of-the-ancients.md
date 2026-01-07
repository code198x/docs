# Echoes of the Ancients: 256-Unit Outline

**Game:** 15 of 16 (68000 Assembly)
**Platform:** Commodore Amiga
**Language:** 68000 Assembly
**Units:** 256 (16 phases)
**Concept:** Connected world exploration with ability-gating. Metroidvania design on Amiga hardware.

---

## Why This Game Fifteenth?

Echoes of the Ancients combines all advanced techniques:

1. **Large connected world** - 100+ rooms
2. **Ability-gating** - Powers unlock areas
3. **Non-linear progression** - Player-driven
4. **Save system** - Battery backup simulation
5. **Multiple endings** - Player choices matter

The Expert-tier showcase before the capstone.

---

## Skills Applied from Previous Games

| Skill | From | Application |
|-------|------|-------------|
| Scrolling | Wanderer | World navigation |
| Platforming | Ascent/Wanderer | Core movement |
| Exploration | Crypt/Fortress | World design |
| Boss fights | Multiple | Ability guardians |
| Save systems | Multiple | Progress persistence |
| All fundamentals | Games 1-14 | Everything |

## New Skills Introduced

| Skill | Phase | Description |
|-------|-------|-------------|
| Ability-gating | 3-4 | Progress unlocks |
| Non-linear design | 5 | Multiple paths |
| Map system | 6 | Player tracking |
| Battery backup | 8 | NVRAM simulation |
| Multiple endings | 14 | Story branching |

---

## Phase 1: World Foundation (Units 1-16)
*Core world structure.*

### Units 1-4: World Concept
- **Unit 1:** Metroidvania overview - connected world
- **Unit 2:** Zone structure - themed areas
- **Unit 3:** Room connections - doorways
- **Unit 4:** World layout - map design

### Units 5-8: Room System
- **Unit 5:** Room data - tiles, objects
- **Unit 6:** Room rendering - scrolling
- **Unit 7:** Room transitions - seamless
- **Unit 8:** Room variety - sizes, shapes

### Units 9-12: Display Setup
- **Unit 9:** Parallax backgrounds - per zone
- **Unit 10:** HUD overlay - status bar
- **Unit 11:** Display regions - game, HUD
- **Unit 12:** Visual framework

### Units 13-16: Basic Navigation
- **Unit 13:** First zone - starting area
- **Unit 14:** Connected rooms - explorable
- **Unit 15:** Door mechanics - transitions
- **Unit 16:** Navigation demo

**Phase Goal:** Basic world navigation.

---

## Phase 2: Player Character (Units 17-32)
*Movement and combat foundation.*

### Units 17-20: Core Movement
- **Unit 17:** Run physics - acceleration
- **Unit 18:** Jump physics - variable height
- **Unit 19:** Gravity - falling
- **Unit 20:** Platform collision

### Units 21-24: Animation System
- **Unit 21:** Animation framework - states
- **Unit 22:** Movement animations - run, jump
- **Unit 23:** Combat animations - attack
- **Unit 24:** Damage animations - hit, death

### Units 25-28: Basic Combat
- **Unit 25:** Primary attack - beam weapon
- **Unit 26:** Attack hitbox - collision
- **Unit 27:** Attack timing - cooldown
- **Unit 28:** Enemy damage - destruction

### Units 29-32: Health System
- **Unit 29:** Health points - energy
- **Unit 30:** Damage calculation - from enemies
- **Unit 31:** Health display - on HUD
- **Unit 32:** Death handling - respawn

**Phase Goal:** Player with movement and combat.

---

## Phase 3: Movement Abilities (Units 33-48)
*Ability unlocks for navigation.*

### Units 33-36: Double Jump
- **Unit 33:** Double jump concept - mid-air
- **Unit 34:** Double jump implementation
- **Unit 35:** Jump counter - tracking
- **Unit 36:** High ledge access - gates

### Units 37-40: Wall Jump
- **Unit 37:** Wall detection - adjacent walls
- **Unit 38:** Wall slide - slow fall
- **Unit 39:** Wall jump - bounce off
- **Unit 40:** Vertical shaft access - gates

### Units 41-44: Dash Ability
- **Unit 41:** Dash concept - horizontal burst
- **Unit 42:** Dash implementation - speed
- **Unit 43:** Dash cooldown - timing
- **Unit 44:** Gap crossing - gates

### Units 45-48: Swim Ability
- **Unit 45:** Water areas - environment
- **Unit 46:** Swim physics - different
- **Unit 47:** Underwater rooms - design
- **Unit 48:** Water access - gates

**Phase Goal:** Four movement abilities.

---

## Phase 4: Combat Abilities (Units 49-64)
*Weapon upgrades and powers.*

### Units 49-52: Beam Upgrades
- **Unit 49:** Charge beam - hold to power
- **Unit 50:** Ice beam - freeze enemies
- **Unit 51:** Wave beam - pass through walls
- **Unit 52:** Beam stacking - combinations

### Units 53-56: Missiles
- **Unit 53:** Missile weapon - limited ammo
- **Unit 54:** Missile doors - special gates
- **Unit 55:** Super missiles - powerful
- **Unit 56:** Missile management

### Units 57-60: Special Powers
- **Unit 57:** Morph ball - small form
- **Unit 58:** Ball bombs - small explosions
- **Unit 59:** Speed boost - running power
- **Unit 60:** Screw attack - jump attack

### Units 61-64: Defensive Powers
- **Unit 61:** Suit upgrades - damage reduction
- **Unit 62:** Energy tanks - max health
- **Unit 63:** Reserve tanks - emergency
- **Unit 64:** Power collection complete

**Phase Goal:** Full ability set.

---

## Phase 5: Zone Design - Part 1 (Units 65-80)
*First half of world.*

### Units 65-68: Zone 1 - Ancient Ruins
- **Unit 65:** Ruins theme - crumbling structures
- **Unit 66:** Ruins rooms - 20+ rooms
- **Unit 67:** Ruins enemies - basic
- **Unit 68:** Ruins boss - double jump grant

### Units 69-72: Zone 2 - Underground Caverns
- **Unit 69:** Caverns theme - natural caves
- **Unit 70:** Caverns rooms - 20+ rooms
- **Unit 71:** Caverns enemies - creatures
- **Unit 72:** Caverns boss - wall jump grant

### Units 73-76: Zone 3 - Sunken Temple
- **Unit 73:** Temple theme - flooded areas
- **Unit 74:** Temple rooms - water sections
- **Unit 75:** Temple enemies - aquatic
- **Unit 76:** Temple boss - swim grant

### Units 77-80: Zone Connections
- **Unit 77:** Zone 1-2 connection
- **Unit 78:** Zone 2-3 connection
- **Unit 79:** Backtracking paths - with new abilities
- **Unit 80:** First half complete

**Phase Goal:** Zones 1-3 complete.

---

## Phase 6: Map System (Units 81-96)
*Player tracking and navigation.*

### Units 81-84: Map Data
- **Unit 81:** Room positions - world grid
- **Unit 82:** Room discovery - track visited
- **Unit 83:** Item locations - on map
- **Unit 84:** Map data structure

### Units 85-88: Map Display
- **Unit 85:** Map screen - pause menu
- **Unit 86:** Map rendering - grid display
- **Unit 87:** Current position - marker
- **Unit 88:** Zone selection - sub-maps

### Units 89-92: Map Features
- **Unit 89:** Room icons - types
- **Unit 90:** Item markers - collected/not
- **Unit 91:** Save points - on map
- **Unit 92:** Boss rooms - marked

### Units 93-96: Navigation Aids
- **Unit 93:** Objective markers - next goal
- **Unit 94:** Percentage complete - tracking
- **Unit 95:** Map stations - reveal areas
- **Unit 96:** Map complete

**Phase Goal:** Full map system.

---

## Phase 7: Zone Design - Part 2 (Units 97-112)
*Second half of world.*

### Units 97-100: Zone 4 - Volcanic Core
- **Unit 97:** Volcanic theme - lava, heat
- **Unit 98:** Volcanic rooms - 20+ rooms
- **Unit 99:** Volcanic enemies - fire-based
- **Unit 100:** Volcanic boss - dash grant

### Units 101-104: Zone 5 - Sky Citadel
- **Unit 101:** Citadel theme - high structures
- **Unit 102:** Citadel rooms - vertical
- **Unit 103:** Citadel enemies - flying
- **Unit 104:** Citadel boss - speed boost grant

### Units 105-108: Zone 6 - Final Fortress
- **Unit 105:** Fortress theme - hostile
- **Unit 106:** Fortress rooms - challenging
- **Unit 107:** Fortress enemies - elite
- **Unit 108:** Final boss area

### Units 109-112: World Completion
- **Unit 109:** Zone connections - full world
- **Unit 110:** Shortcut elevators - fast travel
- **Unit 111:** 100% items - all collectibles
- **Unit 112:** World complete

**Phase Goal:** Zones 4-6 complete.

---

## Phase 8: Save System (Units 113-128)
*Progress persistence.*

### Units 113-116: Save Data
- **Unit 113:** Save structure - what to store
- **Unit 114:** Player state - position, abilities
- **Unit 115:** World state - items collected
- **Unit 116:** Map state - explored rooms

### Units 117-120: Save Implementation
- **Unit 117:** Save points - in-world stations
- **Unit 118:** Save to disk - file format
- **Unit 119:** Load from disk - restore state
- **Unit 120:** Save slots - multiple saves

### Units 121-124: Battery Backup Simulation
- **Unit 121:** NVRAM concept - persistent storage
- **Unit 122:** Auto-save - at stations
- **Unit 123:** Quick save - option
- **Unit 124:** Save integrity - validation

### Units 125-128: Continue System
- **Unit 125:** Game over - continue option
- **Unit 126:** Respawn mechanics - save point
- **Unit 127:** Death penalty - minimal
- **Unit 128:** Save complete

**Phase Goal:** Robust save system.

---

## Phase 9: Boss Encounters (Units 129-144)
*Major boss fights.*

### Units 129-132: Boss Framework
- **Unit 129:** Boss arena - locked rooms
- **Unit 130:** Boss health - display bar
- **Unit 131:** Boss phases - pattern changes
- **Unit 132:** Boss defeat - ability grant

### Units 133-136: Early Bosses
- **Unit 133:** Boss 1 (Ruins) - pattern
- **Unit 134:** Boss 2 (Caverns) - pattern
- **Unit 135:** Boss 3 (Temple) - pattern
- **Unit 136:** Early boss polish

### Units 137-140: Later Bosses
- **Unit 137:** Boss 4 (Volcanic) - pattern
- **Unit 138:** Boss 5 (Citadel) - pattern
- **Unit 139:** Mini-bosses - ability upgrades
- **Unit 140:** Boss variety

### Units 141-144: Final Boss
- **Unit 141:** Final boss design - multi-phase
- **Unit 142:** Final boss phase 1
- **Unit 143:** Final boss phase 2-3
- **Unit 144:** Final boss defeat

**Phase Goal:** All boss encounters.

---

## Phase 10: Enemy Design (Units 145-160)
*Full enemy roster.*

### Units 145-148: Basic Enemies
- **Unit 145:** Crawler - ground patrol
- **Unit 146:** Flyer - aerial
- **Unit 147:** Shooter - ranged
- **Unit 148:** Jumper - hopping

### Units 149-152: Zone Enemies
- **Unit 149:** Fire enemies - volcanic
- **Unit 150:** Water enemies - temple
- **Unit 151:** Flying enemies - citadel
- **Unit 152:** Elite enemies - fortress

### Units 153-156: Enemy AI
- **Unit 153:** Patrol behaviour
- **Unit 154:** Chase behaviour
- **Unit 155:** Attack patterns
- **Unit 156:** Enemy spawning

### Units 157-160: Enemy Balance
- **Unit 157:** Health values - by zone
- **Unit 158:** Damage values - fair
- **Unit 159:** Drops - health, missiles
- **Unit 160:** Enemy roster complete

**Phase Goal:** Complete enemy system.

---

## Phase 11: Non-Linear Design (Units 161-176)
*Multiple paths and sequence.*

### Units 161-164: Path Design
- **Unit 161:** Critical path - required sequence
- **Unit 162:** Optional paths - rewards
- **Unit 163:** Ability gates - blocking
- **Unit 164:** Soft gates - skill can bypass

### Units 165-168: Sequence Breaking
- **Unit 165:** Intended skips - designed
- **Unit 166:** Tech skips - advanced players
- **Unit 167:** Speedrun routes - optimised
- **Unit 168:** Sequence testing

### Units 169-172: Exploration Rewards
- **Unit 169:** Energy tanks - hidden
- **Unit 170:** Missile expansions - scattered
- **Unit 171:** Bonus abilities - optional
- **Unit 172:** 100% rewards

### Units 173-176: Backtracking
- **Unit 173:** New ability access - old areas
- **Unit 174:** Shortcut unlocks - faster travel
- **Unit 175:** Hidden areas - revealed
- **Unit 176:** Exploration complete

**Phase Goal:** Non-linear world design.

---

## Phase 12: Audio System (Units 177-192)
*Music and sound.*

### Units 177-180: Zone Music
- **Unit 177:** Zone 1 music - mysterious
- **Unit 178:** Zone 2-3 music - atmospheric
- **Unit 179:** Zone 4-5 music - intense
- **Unit 180:** Zone 6 music - final

### Units 181-184: Special Music
- **Unit 181:** Boss music - battle theme
- **Unit 182:** Mini-boss music - shorter
- **Unit 183:** Item fanfare - acquisition
- **Unit 184:** Game over/victory music

### Units 185-188: Sound Effects
- **Unit 185:** Weapon sounds - beam, missiles
- **Unit 186:** Ability sounds - jump, dash
- **Unit 187:** Enemy sounds - variety
- **Unit 188:** Environment sounds - doors, switches

### Units 189-192: Audio Integration
- **Unit 189:** Music transitions - zone changes
- **Unit 190:** Dynamic audio - situation
- **Unit 191:** Audio options - volume
- **Unit 192:** Audio complete

**Phase Goal:** Full audio implementation.

---

## Phase 13: Presentation (Units 193-208)
*Menus and screens.*

### Units 193-196: Title Screen
- **Unit 193:** Title graphics - logo
- **Unit 194:** Title animation
- **Unit 195:** Menu options - new/continue
- **Unit 196:** Title music

### Units 197-200: In-Game UI
- **Unit 197:** Health display - detailed
- **Unit 198:** Ammo display - missiles
- **Unit 199:** Mini-map - corner
- **Unit 200:** Ability indicators

### Units 201-204: Pause Menu
- **Unit 201:** Pause screen - options
- **Unit 202:** Equipment screen - status
- **Unit 203:** Map access - full map
- **Unit 204:** Options menu

### Units 205-208: Story Elements
- **Unit 205:** Intro sequence - backstory
- **Unit 206:** Lore terminals - in-world
- **Unit 207:** Character dialogue - hints
- **Unit 208:** Story complete

**Phase Goal:** Full presentation.

---

## Phase 14: Multiple Endings (Units 209-224)
*Ending variations.*

### Units 209-212: Ending Conditions
- **Unit 209:** Completion percentage - tracking
- **Unit 210:** Time tracking - play time
- **Unit 211:** Secret flags - special actions
- **Unit 212:** Ending selection - logic

### Units 213-216: Ending Variations
- **Unit 213:** Bad ending - low completion
- **Unit 214:** Good ending - medium completion
- **Unit 215:** Best ending - high completion
- **Unit 216:** Secret ending - special conditions

### Units 217-220: Ending Sequences
- **Unit 217:** Ending cutscenes - graphics
- **Unit 218:** Ending text - story conclusion
- **Unit 219:** Credits sequence
- **Unit 220:** Post-credits

### Units 221-224: Replay Value
- **Unit 221:** New Game+ - option
- **Unit 222:** Hard mode - unlockable
- **Unit 223:** Speedrun mode - timer
- **Unit 224:** Endings complete

**Phase Goal:** Multiple endings.

---

## Phase 15: Polish (Units 225-240)
*Final polish pass.*

### Units 225-228: Visual Polish
- **Unit 225:** Animation polish - smooth
- **Unit 226:** Effect polish - explosions
- **Unit 227:** Transition polish - seamless
- **Unit 228:** Visual consistency

### Units 229-232: Gameplay Polish
- **Unit 229:** Control responsiveness
- **Unit 230:** Hit feedback - clear
- **Unit 231:** Collision polish - fair
- **Unit 232:** Gameplay feel

### Units 233-236: Balance Pass
- **Unit 233:** Difficulty curve - zone by zone
- **Unit 234:** Boss difficulty - challenging/fair
- **Unit 235:** Enemy balance - per zone
- **Unit 236:** Item balance - distribution

### Units 237-240: Bug Fixes
- **Unit 237:** Collision bugs - edge cases
- **Unit 238:** Save bugs - data integrity
- **Unit 239:** Sequence bugs - progression
- **Unit 240:** Polish complete

**Phase Goal:** Polished experience.

---

## Phase 16: Release (Units 241-256)
*Testing and distribution.*

### Units 241-244: Full Testing
- **Unit 241:** Complete playthrough - all endings
- **Unit 242:** 100% testing - all items
- **Unit 243:** Speedrun testing - routes
- **Unit 244:** Edge case testing

### Units 245-248: Performance
- **Unit 245:** Frame rate - consistency
- **Unit 246:** Memory usage - limits
- **Unit 247:** Disk access - loading
- **Unit 248:** Optimisation pass

### Units 249-252: Multi-Disk
- **Unit 249:** Disk layout - data split
- **Unit 250:** Disk swapping - zones
- **Unit 251:** Swap prompts - user-friendly
- **Unit 252:** Multi-disk testing

### Units 253-256: Release
- **Unit 253:** Documentation - instructions
- **Unit 254:** Final testing
- **Unit 255:** Release candidate
- **Unit 256:** Release build - multi-disk ADF

**Phase Goal:** Complete Metroidvania.

---

## Summary

**Echoes of the Ancients** demonstrates Expert-level Amiga development.

### Technical Specifications

- **Display:** Scrolling playfield, parallax, 320×256
- **World:** 6 zones, 100+ rooms
- **Abilities:** 12+ unlockable powers
- **Enemies:** 20+ types
- **Bosses:** 6 zone bosses + mini-bosses
- **Map:** Full exploration tracking
- **Save:** Disk-based with battery simulation
- **Endings:** 4 variations
- **Audio:** Full MOD soundtrack per zone
- **Distribution:** Multi-disk ADF set

### Skills for Capstone

- Large world design
- Ability-gating systems
- Non-linear progression
- Multiple endings
- Multi-disk distribution
- All previous techniques mastered
