# Bastion: 128-Unit Outline

**Game:** 15 of 16
**Platform:** ZX Spectrum (48K/128K enhanced)
**Units:** 128 (8 phases)
**Concept:** Isometric action-adventure. Explore a vast fortress, solve puzzles, defeat enemies. Knight Lore meets Zelda.

---

## Why This Game Fifteenth?

Bastion introduces isometric projection - complex spatial representation:

1. **Isometric graphics** - 3D illusion on 2D display
2. **Isometric collision** - Depth-aware detection
3. **Room-based world** - Interconnected chambers
4. **Puzzle mechanics** - Block pushing, switches
5. **Inventory and equipment** - Items affect gameplay

The isometric view is one of the Spectrum's signature achievements.

---

## Skills Applied from Previous Games

| Skill | From | Application in Bastion |
|-------|------|----------------------|
| Room transitions | Chambers | Multi-room exploration |
| Inventory system | Chambers | Item management |
| Depth sorting | Knuckle Brawl | Draw order |
| 128K features | Strafe | Enhanced audio/content |
| Enemy AI | Multiple | Enemy behaviours |
| Persistent state | Chambers | World state tracking |

## New Skills Introduced

| Skill | Phase | Description |
|-------|-------|-------------|
| Isometric projection | 1 | Diamond-grid display |
| Isometric tile drawing | 1 | Stacking tiles |
| Isometric collision | 2 | 3D collision in 2D |
| Block puzzle mechanics | 3 | Pushing blocks |
| Switch/trigger systems | 4 | Cause and effect |
| Jump in isometric | 4 | Height handling |
| Multi-height levels | 5 | Stacked platforms |
| Equipment system | 6 | Equip items |

---

## Phase 1: Isometric Foundation (Units 1-16)
*Isometric display system.*

### Units 1-4: Isometric Concept
- **Unit 1:** Isometric projection - 2:1 diamond grid
- **Unit 2:** World coordinates - X, Y, Z axes
- **Unit 3:** Screen coordinates - projecting to display
- **Unit 4:** Tile positioning - where tiles appear

### Units 5-8: Tile System
- **Unit 5:** Floor tiles - base layer
- **Unit 6:** Wall tiles - vertical obstructions
- **Unit 7:** Tile stacking - height variation
- **Unit 8:** Tile draw order - back to front

### Units 9-12: Room Display
- **Unit 9:** Room data structure - tiles and objects
- **Unit 10:** Room rendering - display complete room
- **Unit 11:** Room boundaries - walls contain play area
- **Unit 12:** Room colouring - attribute management

### Units 13-16: Player Character
- **Unit 13:** Isometric sprite - knight/hero
- **Unit 14:** 4-direction views - facing each direction
- **Unit 15:** Player positioning - on isometric grid
- **Unit 16:** Playable foundation - player in isometric room

**Phase Goal:** Isometric room display with player character.

---

## Phase 2: Movement and Collision (Units 17-32)
*Moving in isometric space.*

### Units 17-20: Isometric Movement
- **Unit 17:** Direction mapping - controls to isometric
- **Unit 18:** Diagonal movement - isometric diagonals
- **Unit 19:** Grid-based movement - tile-to-tile
- **Unit 20:** Smooth movement - sub-tile positioning

### Units 21-24: Height Handling
- **Unit 21:** Z-position tracking - height in world
- **Unit 22:** Standing on tiles - detecting floor
- **Unit 23:** Height transitions - slopes and steps
- **Unit 24:** Shadow display - grounding the player

### Units 25-28: Collision Detection
- **Unit 25:** Wall collision - can't walk through walls
- **Unit 26:** Object collision - blocking objects
- **Unit 27:** Height-aware collision - same level only
- **Unit 28:** Pixel-perfect bounds - collision boxes

### Units 29-32: Room Navigation
- **Unit 29:** Room exits - doorways and passages
- **Unit 30:** Exit detection - player at exit
- **Unit 31:** Room transitions - load new room
- **Unit 32:** Entry positioning - appear at correct spot

**Phase Goal:** Movement and collision in isometric world.

---

## Phase 3: Objects and Interaction (Units 33-48)
*Interactive objects.*

### Units 33-36: Collectible Objects
- **Unit 33:** Item objects - keys, potions, treasures
- **Unit 34:** Item display - objects in world
- **Unit 35:** Item pickup - collect on contact
- **Unit 36:** Item persistence - stay collected

### Units 37-40: Pushable Blocks
- **Unit 37:** Block objects - moveable blocks
- **Unit 38:** Push detection - player against block
- **Unit 39:** Block movement - slide in direction
- **Unit 40:** Block collision - blocks hit walls/blocks

### Units 41-44: Block Puzzles
- **Unit 41:** Pressure plates - weight triggers
- **Unit 42:** Plate activation - block on plate
- **Unit 43:** Door linking - plates open doors
- **Unit 44:** Puzzle reset - room reset option

### Units 45-48: Inventory System
- **Unit 45:** Inventory data - items carried
- **Unit 46:** Inventory display - show items
- **Unit 47:** Inventory limit - maximum items
- **Unit 48:** Item use - consume/apply items

**Phase Goal:** Interactive objects and puzzles.

---

## Phase 4: Platforming Elements (Units 49-64)
*Height, jumping, and platforms.*

### Units 49-52: Jumping
- **Unit 49:** Jump input - button press
- **Unit 50:** Jump arc - isometric jump path
- **Unit 51:** Jump collision - landing detection
- **Unit 52:** Jump height - reach higher tiles

### Units 53-56: Elevated Platforms
- **Unit 53:** Platform tiles - raised surfaces
- **Unit 54:** Platform display - stacked visuals
- **Unit 55:** Landing on platforms - height detection
- **Unit 56:** Falling - drop from edges

### Units 57-60: Switches and Triggers
- **Unit 57:** Floor switches - step-on activation
- **Unit 58:** Wall switches - interact to activate
- **Unit 59:** Timer switches - temporary activation
- **Unit 60:** Multi-switch puzzles - combinations

### Units 61-64: Moving Elements
- **Unit 61:** Moving platforms - travelling surfaces
- **Unit 62:** Platform riding - move with platform
- **Unit 63:** Conveyor belts - forced movement
- **Unit 64:** Crushers - timing hazards

**Phase Goal:** Platforming in isometric view.

---

## Phase 5: Combat System (Units 65-80)
*Enemies and combat.*

### Units 65-68: Player Combat
- **Unit 65:** Attack action - swing weapon
- **Unit 66:** Attack range - isometric reach
- **Unit 67:** Attack animation - sword swing
- **Unit 68:** Facing-based attack - direction matters

### Units 69-72: Enemies
- **Unit 69:** Enemy types - guards, creatures
- **Unit 70:** Enemy movement - patrol and chase
- **Unit 71:** Enemy attacks - damage player
- **Unit 72:** Enemy health - hit points

### Units 73-76: Combat Mechanics
- **Unit 73:** Hit detection - attack meets enemy
- **Unit 74:** Damage system - HP reduction
- **Unit 75:** Knockback - push on hit
- **Unit 76:** Enemy death - defeat and drops

### Units 77-80: Player Health
- **Unit 77:** Health display - hearts or bar
- **Unit 78:** Taking damage - enemy attacks
- **Unit 79:** Health recovery - potions
- **Unit 80:** Death and respawn - game over flow

**Phase Goal:** Combat system working.

---

## Phase 6: Equipment and Progression (Units 81-96)
*Items that change gameplay.*

### Units 81-84: Equipment System
- **Unit 81:** Equipment slots - weapon, shield, item
- **Unit 82:** Equipping items - assign to slots
- **Unit 83:** Equipment effects - stat changes
- **Unit 84:** Equipment display - show equipped

### Units 85-88: Weapons
- **Unit 85:** Sword types - different damage/range
- **Unit 86:** Weapon switching - change active weapon
- **Unit 87:** Weapon abilities - special attacks
- **Unit 88:** Weapon upgrades - improve weapons

### Units 89-92: Utility Items
- **Unit 89:** Keys - unlock doors
- **Unit 90:** Boots - increased speed/jump
- **Unit 91:** Shield - block attacks
- **Unit 92:** Magic items - special abilities

### Units 93-96: Progression
- **Unit 93:** Key items - required for progress
- **Unit 94:** Ability gates - need item to proceed
- **Unit 95:** Save points - progress saving
- **Unit 96:** Map system - room overview

**Phase Goal:** Equipment affecting gameplay.

---

## Phase 7: World and Content (Units 97-112)
*Large world with variety.*

### Units 97-100: World Zones
- **Unit 97:** Castle zone - stone fortress
- **Unit 98:** Dungeon zone - dark underground
- **Unit 99:** Tower zone - vertical climb
- **Unit 100:** Boss zone - final area

### Units 101-104: Zone Features
- **Unit 101:** Zone-specific enemies - themed foes
- **Unit 102:** Zone puzzles - unique challenges
- **Unit 103:** Zone items - special equipment
- **Unit 104:** Zone boss - area guardian

### Units 105-108: 128K Enhancements
- **Unit 105:** AY music - per zone
- **Unit 106:** Extra zones - 128K content
- **Unit 107:** Extended animations - more frames
- **Unit 108:** Voice samples - enemy sounds

### Units 109-112: Presentation
- **Unit 109:** Title screen - game logo
- **Unit 110:** Zone intro - area name display
- **Unit 111:** Story scenes - narrative moments
- **Unit 112:** Ending sequence - victory

**Phase Goal:** Large world with zone variety.

---

## Phase 8: Release (Units 113-128)
*Polish and release.*

### Units 113-116: Audio
- **Unit 113:** Sound effects - comprehensive set
- **Unit 114:** Zone music - distinct themes
- **Unit 115:** Boss music - intense track
- **Unit 116:** Ambient sounds - atmosphere

### Units 117-120: Polish
- **Unit 117:** Smooth animations - all actions
- **Unit 118:** Visual effects - magic, explosions
- **Unit 119:** Screen transitions - fade effects
- **Unit 120:** UI refinement - menus, HUD

### Units 121-124: Game Modes
- **Unit 121:** Story mode - full game
- **Unit 122:** Speedrun mode - timer display
- **Unit 123:** Item randomiser - shuffle items (128K)
- **Unit 124:** New Game+ - harder replay

### Units 125-128: Release
- **Unit 125:** Instructions screen
- **Unit 126:** Balance testing - puzzle/combat tuning
- **Unit 127:** 48K/128K testing - both versions
- **Unit 128:** Release build - dual TAP files

**Phase Goal:** Complete isometric adventure.

---

## Summary

**Bastion** teaches isometric graphics and adventure design:

**Phase 1 (Foundation):** Isometric projection, room display.

**Phase 2 (Movement):** Isometric movement, collision.

**Phase 3 (Objects):** Interactive objects, puzzles.

**Phase 4 (Platforming):** Jumping, switches, moving elements.

**Phase 5 (Combat):** Enemies, weapons, health.

**Phase 6 (Equipment):** Items, upgrades, progression.

**Phase 7 (World):** Zones, content, 128K enhancements.

**Phase 8 (Release):** Polish, release.

### Skills Transferred Forward

1. **Isometric projection** → Strategy games, tactics
2. **Isometric collision** → Complex spatial detection
3. **Block puzzles** → Puzzle game mechanics
4. **Equipment systems** → RPG elements
5. **Zone-based worlds** → Large game structure
6. **Save systems** → Long-form games

### Classic Spectrum Heritage

Bastion pays homage to:
- **Knight Lore** (1984) - Ultimate's isometric breakthrough
- **Head Over Heels** (1987) - Isometric puzzle platform
- **Batman** (1986) - Isometric action adventure

These games pioneered isometric graphics on the Spectrum.

### Game Specifications

- **World:** 64+ rooms across 4 zones
- **View:** Isometric 2:1 projection
- **Player:** 16×24 sprite with animations
- **Enemies:** 12+ types
- **Items:** 20+ collectibles and equipment
- **Puzzles:** Block pushing, switches, keys
- **Combat:** Melee with equipment variety
- **Sound:** Beeper (48K) / AY (128K)
- **Zones:** Castle, Dungeon, Tower, Boss
- **Controls:** 4-way + jump + action + inventory
- **Distribution:** 48K TAP + 128K TAP
