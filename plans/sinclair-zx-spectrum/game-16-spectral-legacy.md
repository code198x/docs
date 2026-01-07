# Spectral Legacy: 256-Unit Outline

**Game:** 16 of 16
**Platform:** ZX Spectrum (48K/128K enhanced)
**Units:** 256 (16 phases)
**Concept:** Epic action RPG. A vast world, deep combat, compelling story, and multiple endings. The ultimate Spectrum game.

---

## Why This Game Last?

Spectral Legacy is the capstone - combining everything:

1. **Every technique** - All skills from 15 games
2. **Largest scope** - Multi-load epic adventure
3. **Production quality** - Commercial-grade polish
4. **Advanced distribution** - Turbo tape, multi-load
5. **Portfolio piece** - Demonstrable mastery

This game proves total platform mastery.

---

## Curriculum Integration

Every previous game contributes to Spectral Legacy:

| Game | Contribution |
|------|-------------|
| Ink War | Attribute mastery, screen design |
| Shatter | Smooth sprite movement |
| Skyfire | Object pooling, enemy waves |
| Cavern | Platforming physics |
| Chambers | Multi-room exploration |
| Chomp | AI personalities |
| Slither | Data structures |
| Stack | Grid manipulation |
| Blitz | Horizontal scrolling |
| Exodus | Scrolling platformer |
| Redline | Pseudo-3D, scaling |
| Recoil | Combat depth, weapons |
| Knuckle Brawl | Melee combat, depth |
| Strafe | 128K features, AY sound |
| Bastion | Isometric, equipment |

---

## Phase 1: Core Engine (Units 1-16)
*Fundamental engine systems.*

### Units 1-4: Engine Architecture
- **Unit 1:** Engine design - modular structure
- **Unit 2:** Memory map - how data is organised
- **Unit 3:** Main loop - frame structure
- **Unit 4:** State machine - game states

### Units 5-8: Rendering Pipeline
- **Unit 5:** Layer system - background, sprites, UI
- **Unit 6:** Draw priority - depth management
- **Unit 7:** Dirty rectangles - efficient updates
- **Unit 8:** Double buffering - smooth display

### Units 9-12: Input System
- **Unit 9:** Input abstraction - unified controls
- **Unit 10:** Key mapping - customisable controls
- **Unit 11:** Input buffering - responsive controls
- **Unit 12:** Menu navigation - UI input handling

### Units 13-16: Resource Management
- **Unit 13:** Resource loading - data from tape/128K
- **Unit 14:** Resource caching - keep loaded data
- **Unit 15:** Memory pools - efficient allocation
- **Unit 16:** Engine foundation - all systems integrated

**Phase Goal:** Robust game engine architecture.

---

## Phase 2: World System (Units 17-32)
*Large world management.*

### Units 17-20: World Structure
- **Unit 17:** Zone concept - distinct areas
- **Unit 18:** Zone data format - tiles, entities, connections
- **Unit 19:** Zone transitions - moving between areas
- **Unit 20:** World map - zone interconnections

### Units 21-24: Area Types
- **Unit 21:** Side-scroll areas - platforming sections
- **Unit 22:** Top-down areas - exploration sections
- **Unit 23:** Isometric areas - puzzle/combat sections
- **Unit 24:** View switching - seamless transitions

### Units 25-28: Environment
- **Unit 25:** Tile system - versatile tile engine
- **Unit 26:** Decoration layers - visual depth
- **Unit 27:** Environmental hazards - world dangers
- **Unit 28:** Interactive elements - levers, doors

### Units 29-32: Persistence
- **Unit 29:** World state - what's changed
- **Unit 30:** Entity states - enemy positions, deaths
- **Unit 31:** Container states - chests, items
- **Unit 32:** State serialisation - save/load ready

**Phase Goal:** Multi-view world system.

---

## Phase 3: Player Character (Units 33-48)
*Deep player mechanics.*

### Units 33-36: Movement System
- **Unit 33:** Multi-view movement - consistent feel
- **Unit 34:** Platformer physics - jumping, falling
- **Unit 35:** Top-down movement - 8-way
- **Unit 36:** Swimming/climbing - alternate movement

### Units 37-40: Animation System
- **Unit 37:** Animation data - sprite sequences
- **Unit 38:** Animation states - idle, walk, action
- **Unit 39:** Animation blending - smooth transitions
- **Unit 40:** Procedural animation - reactive movement

### Units 41-44: Health and Status
- **Unit 41:** Health system - HP and max HP
- **Unit 42:** Magic/energy system - MP resource
- **Unit 43:** Status effects - poison, slow, etc.
- **Unit 44:** Status display - HUD elements

### Units 45-48: Character Growth
- **Unit 45:** Experience points - XP from combat
- **Unit 46:** Level system - stat improvements
- **Unit 47:** Skill unlocks - new abilities
- **Unit 48:** Growth display - progress tracking

**Phase Goal:** Deep player character system.

---

## Phase 4: Combat Foundation (Units 49-64)
*Combat mechanics.*

### Units 49-52: Melee Combat
- **Unit 49:** Attack system - weapon swings
- **Unit 50:** Attack combos - chained attacks
- **Unit 51:** Blocking - defensive action
- **Unit 52:** Counter attacks - timing-based

### Units 53-56: Ranged Combat
- **Unit 53:** Projectile weapons - bows, thrown
- **Unit 54:** Magic attacks - spell projectiles
- **Unit 55:** Aiming system - targeting
- **Unit 56:** Ammunition - limited projectiles

### Units 57-60: Damage System
- **Unit 57:** Damage calculation - attack vs defence
- **Unit 58:** Damage types - physical, magical, elemental
- **Unit 59:** Resistances - reduce damage types
- **Unit 60:** Critical hits - bonus damage

### Units 61-64: Combat Flow
- **Unit 61:** Stagger system - interrupt attacks
- **Unit 62:** Invincibility frames - recovery time
- **Unit 63:** Death handling - player death sequence
- **Unit 64:** Combat feel - responsive, satisfying

**Phase Goal:** Satisfying combat system.

---

## Phase 5: Enemy System (Units 65-80)
*Enemy variety and AI.*

### Units 65-68: Enemy Framework
- **Unit 65:** Enemy data structure - stats, behaviour
- **Unit 66:** Enemy spawning - placement system
- **Unit 67:** Enemy states - idle, alert, combat
- **Unit 68:** Enemy pooling - efficient management

### Units 69-72: AI Behaviours
- **Unit 69:** Patrol AI - route following
- **Unit 70:** Chase AI - pursue player
- **Unit 71:** Attack AI - combat decisions
- **Unit 72:** Group AI - coordinated enemies

### Units 73-76: Enemy Types
- **Unit 73:** Melee enemies - close combat
- **Unit 74:** Ranged enemies - projectile attacks
- **Unit 75:** Magic enemies - spell casters
- **Unit 76:** Boss framework - complex encounters

### Units 77-80: Enemy Feedback
- **Unit 77:** Hit reactions - visual feedback
- **Unit 78:** Death animations - defeat sequences
- **Unit 79:** Loot drops - enemy rewards
- **Unit 80:** Enemy sounds - audio feedback

**Phase Goal:** Varied, intelligent enemies.

---

## Phase 6: Equipment System (Units 81-96)
*Items and inventory.*

### Units 81-84: Inventory
- **Unit 81:** Inventory structure - item storage
- **Unit 82:** Inventory UI - item display
- **Unit 83:** Item categories - weapons, armour, items
- **Unit 84:** Item stacking - consumables stack

### Units 85-88: Equipment Slots
- **Unit 85:** Slot system - head, body, weapon, etc.
- **Unit 86:** Equipment stats - item attributes
- **Unit 87:** Equipping/unequipping - slot management
- **Unit 88:** Equipment display - show equipped

### Units 89-92: Weapons
- **Unit 89:** Weapon types - swords, axes, bows
- **Unit 90:** Weapon stats - damage, speed, range
- **Unit 91:** Weapon abilities - special attacks
- **Unit 92:** Weapon upgrades - improvement system

### Units 93-96: Armour and Accessories
- **Unit 93:** Armour pieces - body protection
- **Unit 94:** Shield system - active blocking
- **Unit 95:** Accessories - rings, amulets
- **Unit 96:** Set bonuses - matching equipment

**Phase Goal:** Deep equipment system.

---

## Phase 7: Magic System (Units 97-112)
*Spells and abilities.*

### Units 97-100: Magic Framework
- **Unit 97:** Spell data - effects, costs, timing
- **Unit 98:** MP management - casting costs
- **Unit 99:** Spell casting - input and animation
- **Unit 100:** Spell effects - visual feedback

### Units 101-104: Spell Types
- **Unit 101:** Attack spells - damage magic
- **Unit 102:** Defence spells - protection, healing
- **Unit 103:** Utility spells - teleport, light
- **Unit 104:** Summon spells - temporary allies

### Units 105-108: Magic Progression
- **Unit 105:** Spell learning - acquire new spells
- **Unit 106:** Spell levels - improve spells
- **Unit 107:** Spell requirements - level gates
- **Unit 108:** Magic specialisation - focus areas

### Units 109-112: Magic UI
- **Unit 109:** Spell menu - selection interface
- **Unit 110:** Quick cast - shortcut system
- **Unit 111:** Spell icons - visual identifiers
- **Unit 112:** Cooldown display - timing feedback

**Phase Goal:** Complete magic system.

---

## Phase 8: NPCs and Dialogue (Units 113-128)
*Characters and story.*

### Units 113-116: NPC System
- **Unit 113:** NPC data - dialogue, schedules
- **Unit 114:** NPC display - character sprites
- **Unit 115:** NPC interaction - talk action
- **Unit 116:** NPC states - respond to events

### Units 117-120: Dialogue System
- **Unit 117:** Dialogue data - text and flow
- **Unit 118:** Dialogue display - text boxes
- **Unit 119:** Dialogue choices - branching conversations
- **Unit 120:** Dialogue effects - trigger events

### Units 121-124: Quest System
- **Unit 121:** Quest data - objectives, rewards
- **Unit 122:** Quest tracking - progress display
- **Unit 123:** Quest stages - multi-step quests
- **Unit 124:** Quest completion - rewards and effects

### Units 125-128: Story Integration
- **Unit 125:** Main quest - core story line
- **Unit 126:** Side quests - optional content
- **Unit 127:** Story flags - narrative state
- **Unit 128:** Cutscenes - story presentation

**Phase Goal:** NPCs, dialogue, and quests.

---

## Phase 9: Boss Battles (Units 129-144)
*Epic boss encounters.*

### Units 129-132: Boss Framework
- **Unit 129:** Boss data - extended enemy data
- **Unit 130:** Boss arena - dedicated areas
- **Unit 131:** Boss health - large HP pools
- **Unit 132:** Boss phases - multiple stages

### Units 133-136: Boss Patterns
- **Unit 133:** Attack patterns - sequenced attacks
- **Unit 134:** Vulnerable windows - when to attack
- **Unit 135:** Rage modes - phase changes
- **Unit 136:** Pattern variety - unpredictability

### Units 137-140: Boss Types
- **Unit 137:** Guardian boss - area defender
- **Unit 138:** Puzzle boss - requires strategy
- **Unit 139:** Rush boss - intense action
- **Unit 140:** Final boss - ultimate challenge

### Units 141-144: Boss Polish
- **Unit 141:** Boss intros - dramatic entrances
- **Unit 142:** Boss music - dedicated themes
- **Unit 143:** Boss death - dramatic defeat
- **Unit 144:** Boss rewards - major rewards

**Phase Goal:** Memorable boss battles.

---

## Phase 10: World Content (Units 145-160)
*Zones and locations.*

### Units 145-148: Zone 1 - Starting Village
- **Unit 145:** Village layout - safe starting area
- **Unit 146:** Tutorial integration - teaching mechanics
- **Unit 147:** Village NPCs - shopkeepers, quest givers
- **Unit 148:** Village story - opening narrative

### Units 149-152: Zone 2 - Ancient Forest
- **Unit 149:** Forest layout - exploration area
- **Unit 150:** Forest enemies - wildlife, bandits
- **Unit 151:** Forest puzzles - environmental challenges
- **Unit 152:** Forest boss - nature guardian

### Units 153-156: Zone 3 - Mountain Fortress
- **Unit 153:** Fortress layout - dungeon crawl
- **Unit 154:** Fortress enemies - soldiers, monsters
- **Unit 155:** Fortress traps - dangerous obstacles
- **Unit 156:** Fortress boss - warlord

### Units 157-160: Zone 4 - Shadow Realm
- **Unit 157:** Shadow layout - final area
- **Unit 158:** Shadow enemies - demons, spirits
- **Unit 159:** Shadow challenges - ultimate tests
- **Unit 160:** Final boss - main antagonist

**Phase Goal:** Four distinct zones.

---

## Phase 11: Expanded Content (Units 161-176)
*Additional areas and content.*

### Units 161-164: Optional Zones
- **Unit 161:** Hidden cave - secret area
- **Unit 162:** Floating island - bonus zone
- **Unit 163:** Underworld - challenging zone
- **Unit 164:** Secret boss - ultimate challenge

### Units 165-168: Side Content
- **Unit 165:** Mini-games - diversions
- **Unit 166:** Arena challenges - combat trials
- **Unit 167:** Treasure hunting - hidden items
- **Unit 168:** Achievement system - completion tracking

### Units 169-172: New Game Plus
- **Unit 169:** NG+ design - replay value
- **Unit 170:** NG+ scaling - harder difficulty
- **Unit 171:** NG+ content - new items/enemies
- **Unit 172:** NG+ endings - alternate conclusions

### Units 173-176: Endings
- **Unit 173:** Standard ending - main conclusion
- **Unit 174:** Good ending - optimal outcome
- **Unit 175:** Secret ending - hidden conclusion
- **Unit 176:** Ending conditions - what triggers each

**Phase Goal:** Expansive content with replay value.

---

## Phase 12: 128K Features (Units 177-192)
*128K enhancements.*

### Units 177-180: AY Sound System
- **Unit 177:** AY music engine - multi-channel
- **Unit 178:** Zone themes - per-area music
- **Unit 179:** Boss themes - intense tracks
- **Unit 180:** Sound effects - comprehensive set

### Units 181-184: Bank Switching
- **Unit 181:** Bank organisation - content layout
- **Unit 182:** Dynamic loading - swap content
- **Unit 183:** Cross-bank calls - code organisation
- **Unit 184:** Bank optimisation - efficient use

### Units 185-188: 128K Exclusive Content
- **Unit 185:** Extra zones - 128K areas
- **Unit 186:** Extra bosses - 128K challenges
- **Unit 187:** Extra equipment - 128K items
- **Unit 188:** Extended story - 128K narrative

### Units 189-192: 48K Compatibility
- **Unit 189:** 48K version - reduced content
- **Unit 190:** 48K audio - beeper sounds
- **Unit 191:** 48K optimisation - fit in memory
- **Unit 192:** Dual build - both versions

**Phase Goal:** Full 128K utilisation.

---

## Phase 13: Save System (Units 193-208)
*Game saving and loading.*

### Units 193-196: Save Data
- **Unit 193:** Save structure - what to save
- **Unit 194:** Data serialisation - pack save data
- **Unit 195:** Save validation - check integrity
- **Unit 196:** Save size - minimise footprint

### Units 197-200: Save Methods
- **Unit 197:** Password system - encoded progress
- **Unit 198:** Tape save - save to tape
- **Unit 199:** Quick save - bookmark system
- **Unit 200:** Multiple slots - save management

### Units 201-204: Load System
- **Unit 201:** Load detection - find save
- **Unit 202:** Load process - restore state
- **Unit 203:** Load validation - verify save
- **Unit 204:** Error handling - corrupt save recovery

### Units 205-208: Save UI
- **Unit 205:** Save menu - save options
- **Unit 206:** Load menu - load options
- **Unit 207:** Confirmation dialogs - prevent accidents
- **Unit 208:** Save/load feedback - progress indication

**Phase Goal:** Robust save/load system.

---

## Phase 14: Multi-Load System (Units 209-224)
*Loading large content from tape.*

### Units 209-212: Multi-Load Design
- **Unit 209:** Content segmentation - divide into parts
- **Unit 210:** Load points - when to load
- **Unit 211:** Load sequence - order of loading
- **Unit 212:** Memory reuse - overwrite old content

### Units 213-216: Loading Screens
- **Unit 213:** Load screen graphics - per-zone images
- **Unit 214:** Load progress - visual indicator
- **Unit 215:** Load music - audio during load
- **Unit 216:** Load optimisation - minimise wait

### Units 217-220: Turbo Tape Loader
- **Unit 217:** Turbo tape concept - faster loading
- **Unit 218:** Custom loader - pilot tone, data
- **Unit 219:** Load routine - decode data
- **Unit 220:** Error recovery - handle tape issues

### Units 221-224: Multi-Load Flow
- **Unit 221:** Zone transitions - load triggers
- **Unit 222:** Seamless loading - minimise disruption
- **Unit 223:** Load caching - avoid reloads
- **Unit 224:** Multi-load testing - reliability

**Phase Goal:** Efficient multi-load system.

---

## Phase 15: Polish (Units 225-240)
*Presentation and refinement.*

### Units 225-228: Title and Menus
- **Unit 225:** Title screen - impressive intro
- **Unit 226:** Main menu - game options
- **Unit 227:** Options menu - settings
- **Unit 228:** Credits screen - acknowledgements

### Units 229-232: In-Game UI
- **Unit 229:** HUD design - health, MP, etc.
- **Unit 230:** Status screens - detailed info
- **Unit 231:** Map screen - world overview
- **Unit 232:** Pause menu - in-game options

### Units 233-236: Visual Effects
- **Unit 233:** Particle system - debris, magic
- **Unit 234:** Screen effects - flash, shake
- **Unit 235:** Transition effects - fades, wipes
- **Unit 236:** Weather effects - rain, fog

### Units 237-240: Audio Polish
- **Unit 237:** Sound balance - levels tuning
- **Unit 238:** Music transitions - seamless changes
- **Unit 239:** Ambient audio - environment sounds
- **Unit 240:** Audio cues - feedback sounds

**Phase Goal:** Professional presentation.

---

## Phase 16: Release (Units 241-256)
*Final preparation and distribution.*

### Units 241-244: Testing
- **Unit 241:** Playthrough testing - complete game test
- **Unit 242:** Balance testing - difficulty curve
- **Unit 243:** Bug fixing - comprehensive fixes
- **Unit 244:** Edge cases - unusual situations

### Units 245-248: Performance
- **Unit 245:** Frame rate optimisation - consistent speed
- **Unit 246:** Memory optimisation - efficient use
- **Unit 247:** Load time optimisation - faster loads
- **Unit 248:** Platform testing - 48K and 128K

### Units 249-252: Distribution
- **Unit 249:** Tape mastering - final TAP creation
- **Unit 250:** Multi-file structure - organised release
- **Unit 251:** Instructions - physical or on-tape
- **Unit 252:** Cover art - release presentation

### Units 253-256: Release
- **Unit 253:** Version numbering - release tracking
- **Unit 254:** Change log - document changes
- **Unit 255:** Release announcement - marketing
- **Unit 256:** Final release - complete game

**Phase Goal:** Complete commercial-quality release.

---

## Summary

**Spectral Legacy** is the culmination of the ZX Spectrum curriculum:

**Phases 1-4:** Engine, world, player, combat foundations.

**Phases 5-8:** Enemies, equipment, magic, NPCs.

**Phases 9-12:** Bosses, content, expanded content, 128K.

**Phases 13-16:** Saving, multi-load, polish, release.

### Curriculum Demonstration

This game demonstrates mastery of:

| Category | Skills Demonstrated |
|----------|-------------------|
| **Graphics** | Attributes, sprites, scrolling, isometric, scaling |
| **Audio** | Beeper, AY-3-8912, music engine |
| **Systems** | Object pools, state machines, serialisation |
| **AI** | Patrol, chase, group, boss patterns |
| **Game Design** | Combat, progression, quests, puzzles |
| **Distribution** | Multi-load, turbo tape, 48K/128K |

### Game Specifications

- **World:** 4+ major zones, 100+ rooms
- **Views:** Side-scroll, top-down, isometric
- **Player:** Full RPG progression system
- **Combat:** Melee, ranged, magic
- **Enemies:** 30+ types plus bosses
- **Bosses:** 8+ unique encounters
- **Items:** 50+ equipment pieces
- **Spells:** 15+ magic abilities
- **Quests:** Main story + side quests
- **NPCs:** 20+ characters
- **Endings:** Multiple conclusions
- **Save:** Password + tape save
- **Sound:** Beeper (48K) / AY (128K)
- **Load:** Turbo tape multi-load
- **Distribution:** 48K + 128K TAP files
- **Play Time:** 8-15+ hours

### Portfolio Value

Spectral Legacy proves:
1. Complete ZX Spectrum mastery
2. Large project management
3. Commercial-quality production
4. Professional release preparation
5. Full curriculum completion

This is a portfolio piece suitable for demonstrating professional capability.
