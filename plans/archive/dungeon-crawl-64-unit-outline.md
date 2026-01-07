# Dungeon Crawl: 64-Unit Outline

**Game:** 11 of 16
**Platform:** Commodore 64
**Units:** 64
**Concept:** Top-down adventure. Explore rooms, collect keys, unlock doors, find treasure. A Zelda-inspired dungeon exploration game.

---

## Skills Applied from Previous Games

| Skill | Learned In | Application in Dungeon Crawl |
|-------|-----------|---------------------------|
| SID fundamentals | SID Symphony | Music, sound effects |
| Hardware sprites | Starfield | Player, enemies, items |
| Joystick input | Starfield | 8-direction movement |
| Sprite collision | Starfield | Combat, item collection |
| Custom characters | Maze Raider | Dungeon tiles |
| Tile-based maps | Maze Raider | Room layouts |
| Tile collision | Maze Raider | Wall collision |
| Animation frames | Platform Panic | Character animation |
| Power-up collection | Brick Basher | Item pickup |
| Object management | Sprite Storm | Enemy management |
| Resource tracking | Night Raid | Health, keys, items |
| Boss encounters | Night Raid | Dungeon bosses |
| Multiplexing | Sprite Storm | Multiple enemies |
| Room data | Various | Room layouts |

## New Skills Introduced

| Skill | Units | Description |
|-------|-------|-------------|
| Multi-room maps | 5-8 | Connected room structure |
| Room transitions | 9-12 | Screen-edge room changes |
| Door/lock mechanics | 13-16 | Keys unlock doors |
| Inventory system | 17-20 | Item collection and use |
| Save/password system | 41-44 | State persistence |
| NPC dialogue | 25-28 | Simple text interactions |
| Quest structure | 33-36 | Objective-based progress |
| Dungeon generation | 49-52 | Procedural rooms (optional) |

---

## Phase 1: Foundation (Units 1-16)
*Core mechanics: rooms, movement, basic interaction.*

### Unit 1: Top-Down Adventure Concept

**Learning Objectives:**
- Understand adventure game structure
- Analyse Zelda-style gameplay
- Plan game design

**Concepts Introduced:**
- Top-down perspective
- Room-based exploration
- Item collection
- Lock/key puzzles

**Code Written:**
- Design document
- Room structure planning
- Gameplay elements list
- UI design

**What the Learner Sees:**
Understanding the adventure game we're building - exploration, items, puzzles.

---

### Unit 2: Room Layout

**Learning Objectives:**
- Design room data format
- Tile-based room structure
- Wall and floor tiles

**Concepts Introduced:**
- Room as tile grid
- Wall tiles (collision)
- Floor tiles (walkable)
- Exit tiles (room change)

**Code Written:**
- Room data format
- Tile type definitions
- Sample room data
- Format documentation

**What the Learner Sees:**
Room data format defined - ready to render rooms.

**Reference to Maze Raider:**
"Tile concepts from Maze Raider expanded for adventure game rooms."

---

### Unit 3: Room Rendering

**Learning Objectives:**
- Draw room from data
- Character set for dungeon
- Visual appearance

**Concepts Introduced:**
- Tile-to-character mapping
- Room drawing routine
- Character graphics
- Colour application

**Code Written:**
- Dungeon character set
- Room drawing routine
- Tile type rendering
- Colour assignment

**What the Learner Sees:**
Dungeon room displayed! Stone walls, floor tiles, exits visible.

---

### Unit 4: Player Character

**Learning Objectives:**
- Create player sprite
- Position in room
- Visual representation

**Concepts Introduced:**
- Hero sprite design
- Starting position
- Sprite-tile alignment
- Player state

**Code Written:**
- Hero sprite data
- Initial positioning
- Sprite enabling
- State structure

**What the Learner Sees:**
Hero character in dungeon room - ready for adventure!

---

### Unit 5: 8-Direction Movement

**Learning Objectives:**
- Smooth movement in all directions
- Tile-aligned or free movement
- Movement speed

**Concepts Introduced:**
- 8-direction input
- Movement options (free/aligned)
- Speed configuration
- Animation sync

**Code Written:**
- Movement routine
- Direction detection
- Position updates
- Speed control

**What the Learner Sees:**
Hero moves in all directions! Smooth, responsive control.

---

### Unit 6: Wall Collision

**Learning Objectives:**
- Prevent walking through walls
- Tile collision detection
- Smooth collision response

**Concepts Introduced:**
- Movement validation
- Tile type checking
- Collision points
- Slide along walls

**Code Written:**
- Collision detection
- Tile type check
- Position validation
- Slide behavior

**What the Learner Sees:**
Can't walk through walls! Slides along wall edges smoothly.

**Reference to Maze Raider:**
"Same tile collision principles from Maze Raider, refined for free movement."

---

### Unit 7: Walking Animation

**Learning Objectives:**
- Animate character while moving
- Direction-based animation
- Idle when stopped

**Concepts Introduced:**
- Walk cycle frames
- Direction determines sprite
- Animation timer
- Idle frame

**Code Written:**
- Animation frames (4 directions × 2 walk frames + idle)
- Animation update routine
- Direction-based selection
- Smooth cycling

**What the Learner Sees:**
Hero animates while walking! Faces direction of movement.

---

### Unit 8: Room Exit Detection

**Learning Objectives:**
- Detect reaching room edge
- Identify exit tiles
- Prepare for transitions

**Concepts Introduced:**
- Room boundary detection
- Exit tile recognition
- Direction of exit
- Transition trigger

**Code Written:**
- Edge detection
- Exit tile check
- Direction recording
- Transition flag

**What the Learner Sees:**
Walk to room edge - transition will occur (next unit).

---

### Unit 9: Map Structure

**Learning Objectives:**
- Connect rooms together
- Map coordinate system
- Room connectivity

**Concepts Introduced:**
- Map as room grid
- Room coordinates (X, Y)
- Neighbour connections
- Map data format

**Code Written:**
- Map data structure
- Room coordinate tracking
- Neighbour lookup
- Map definition

**What the Learner Sees:**
(Map structure ready - rooms connected.)

---

### Unit 10: Room Transitions

**Learning Objectives:**
- Change rooms on exit
- Load new room
- Position player correctly

**Concepts Introduced:**
- Room unloading
- New room loading
- Player repositioning
- Opposite edge entry

**Code Written:**
- Transition routine
- Room loading
- Player position reset
- Smooth transition

**What the Learner Sees:**
Walk through exit - new room loads! Player appears at opposite edge.

---

### Unit 11: Basic Items

**Learning Objectives:**
- Items in rooms
- Item sprites
- Collection mechanic

**Concepts Introduced:**
- Item data per room
- Item sprites
- Collection detection
- Item removal

**Code Written:**
- Item data structure
- Item rendering
- Collection collision
- Removal handling

**What the Learner Sees:**
Items in rooms! Walk over to collect.

---

### Unit 12: Treasure Collection

**Learning Objectives:**
- Collect treasure for points
- Score tracking
- Collection feedback

**Concepts Introduced:**
- Treasure item type
- Score increment
- Sound effect
- Visual feedback

**Code Written:**
- Treasure handling
- Score addition
- Collection sound
- Feedback effect

**What the Learner Sees:**
Collect treasure - score increases! Satisfying collection feedback.

---

### Unit 13: Key Items

**Learning Objectives:**
- Keys as special items
- Key counter
- Door interaction prep

**Concepts Introduced:**
- Key item type
- Key counter
- Counter display
- Key inventory

**Code Written:**
- Key item handling
- Counter increment
- Display update
- Key tracking

**What the Learner Sees:**
Collect keys - key counter increases! Keys for doors...

---

### Unit 14: Locked Doors

**Learning Objectives:**
- Doors as obstacles
- Lock/key mechanic
- Door opening

**Concepts Introduced:**
- Door tile type
- Locked state
- Key consumption
- Door opening

**Code Written:**
- Door tile handling
- Lock check
- Key use
- Door state change

**What the Learner Sees:**
Locked door blocks path! Have a key? Door opens!

---

### Unit 15: HUD Display

**Learning Objectives:**
- Status display
- Health, keys, score
- Clear information

**Concepts Introduced:**
- HUD layout
- Status variables
- Display formatting
- Update routine

**Code Written:**
- HUD drawing
- Status display
- Update on change
- Clear layout

**What the Learner Sees:**
HUD shows hearts, keys, score - clear status at a glance!

---

### Unit 16: Complete Basic Game

**Learning Objectives:**
- Integrate all systems
- Multiple rooms
- Playable exploration

**Concepts Introduced:**
- Complete game loop
- Multi-room map
- Win condition (find goal)
- Title screen

**Code Written:**
- Integration
- Sample dungeon
- Win condition
- Title/game over

**What the Learner Sees:**
Complete exploration game! Navigate rooms, collect keys, open doors, find goal!

---

## Phase 2: Expansion (Units 17-32)
*Combat, enemies, items, quests.*

### Unit 17: Inventory Framework

**Learning Objectives:**
- Design inventory system
- Item storage
- Selection mechanism

**Concepts Introduced:**
- Inventory data structure
- Item slots
- Current selection
- Use mechanic

**Code Written:**
- Inventory structure
- Add/remove items
- Selection tracking
- Framework ready

**What the Learner Sees:**
(Inventory framework ready.)

---

### Unit 18: Inventory Display

**Learning Objectives:**
- Show inventory on screen
- Item icons
- Selection indicator

**Concepts Introduced:**
- Inventory UI
- Item icons
- Selection highlight
- Open/close mechanic

**Code Written:**
- Inventory screen
- Item icon display
- Selection cursor
- Toggle display

**What the Learner Sees:**
Press button - inventory opens! Shows collected items, select with cursor.

---

### Unit 19: Usable Items

**Learning Objectives:**
- Items with effects
- Use from inventory
- Effect application

**Concepts Introduced:**
- Item use function
- Effect per item type
- Consumption
- Feedback

**Code Written:**
- Item use handling
- Effect per type
- Consumption logic
- Use feedback

**What the Learner Sees:**
Use item from inventory - effect applies! Potion heals, etc.

---

### Unit 20: Health Potion

**Learning Objectives:**
- Health restoration item
- Consumable healing
- Strategic resource

**Concepts Introduced:**
- Potion item type
- Health restoration
- Consumption on use
- Limited resource

**Code Written:**
- Potion handling
- Health increment
- Inventory removal
- Effect feedback

**What the Learner Sees:**
Use potion - health restored! Strategic healing option.

**Reference to Night Raid:**
"Resource management concepts from Night Raid (fuel) applied to consumables."

---

### Unit 21: Basic Enemy

**Learning Objectives:**
- Enemy presence in rooms
- Simple movement
- Threat introduction

**Concepts Introduced:**
- Enemy data structure
- Simple AI movement
- Room-specific enemies
- Threat presence

**Code Written:**
- Enemy structure
- Simple movement AI
- Per-room enemies
- Sprite rendering

**What the Learner Sees:**
Enemies in dungeons! They wander around - threatening!

---

### Unit 22: Enemy-Player Collision

**Learning Objectives:**
- Damage on contact
- Health reduction
- Knockback

**Concepts Introduced:**
- Collision damage
- Health decrement
- Brief invulnerability
- Knockback effect

**Code Written:**
- Collision detection
- Damage application
- Invulnerability timer
- Knockback

**What the Learner Sees:**
Touch enemy - take damage! Brief flashing invulnerability, knockback.

---

### Unit 23: Player Attack

**Learning Objectives:**
- Attack mechanic
- Sword swing
- Damage enemies

**Concepts Introduced:**
- Attack button
- Attack animation
- Damage area
- Enemy health

**Code Written:**
- Attack routine
- Animation display
- Damage area check
- Enemy damage

**What the Learner Sees:**
Press attack - sword swings! Damages enemies in front.

---

### Unit 24: Enemy Defeat

**Learning Objectives:**
- Enemy destruction
- Drops on defeat
- Combat reward

**Concepts Introduced:**
- Enemy health tracking
- Defeat detection
- Item drops
- Score reward

**Code Written:**
- Health tracking
- Defeat handling
- Drop spawning
- Score increment

**What the Learner Sees:**
Defeat enemy - drops treasure or heart! Rewarding combat.

---

### Unit 25: NPC Framework

**Learning Objectives:**
- Non-hostile characters
- Interaction trigger
- Dialogue prep

**Concepts Introduced:**
- NPC data structure
- Interaction detection
- Dialogue trigger
- Helpful characters

**Code Written:**
- NPC structure
- Interaction zone
- Trigger detection
- Framework ready

**What the Learner Sees:**
Friendly NPCs in rooms - can interact with them!

---

### Unit 26: Simple Dialogue

**Learning Objectives:**
- Text display for NPCs
- Message display
- Player reading

**Concepts Introduced:**
- Dialogue text storage
- Text display box
- Multi-line text
- Dismiss on button

**Code Written:**
- Text storage
- Display box rendering
- Text printing
- Input handling

**What the Learner Sees:**
Talk to NPC - dialogue box appears! "The treasure lies in the northern chamber..."

---

### Unit 27: Quest Hints

**Learning Objectives:**
- NPCs give hints
- Guide player
- Story elements

**Concepts Introduced:**
- Hint dialogue
- Quest clues
- Guidance through NPCs
- Story integration

**Code Written:**
- Hint text content
- Context-aware hints
- Quest integration
- Story elements

**What the Learner Sees:**
NPCs provide hints! "You'll need the silver key for the locked chamber."

---

### Unit 28: Special Tiles

**Learning Objectives:**
- Hazard tiles
- Traps
- Environmental danger

**Concepts Introduced:**
- Damage tiles
- Trigger tiles
- Hazard avoidance
- Environmental challenge

**Code Written:**
- Tile type effects
- Damage on step
- Visual distinction
- Avoidance gameplay

**What the Learner Sees:**
Spikes on floor! Step on them - damage! Environmental hazards.

---

### Unit 29: Pushable Blocks

**Learning Objectives:**
- Puzzle elements
- Block pushing
- Environmental puzzles

**Concepts Introduced:**
- Pushable block type
- Push mechanic
- Path clearing
- Puzzle design

**Code Written:**
- Block interaction
- Push detection
- Movement handling
- Target detection

**What the Learner Sees:**
Push block onto switch - door opens! Environmental puzzles!

---

### Unit 30: Switches and Triggers

**Learning Objectives:**
- Trigger mechanisms
- State changes
- Puzzle solutions

**Concepts Introduced:**
- Switch tiles
- Trigger effects
- State tracking
- Door linkage

**Code Written:**
- Switch handling
- Effect triggering
- State management
- Visual feedback

**What the Learner Sees:**
Step on switch - something happens elsewhere! Connected puzzles.

---

### Unit 31: Hidden Passages

**Learning Objectives:**
- Secret areas
- Exploration reward
- Discover mechanics

**Concepts Introduced:**
- Hidden wall type
- Reveal mechanic
- Bonus areas
- Exploration reward

**Code Written:**
- Hidden wall handling
- Reveal on bomb/push
- Secret rooms
- Bonus content

**What the Learner Sees:**
Bomb wall - secret passage revealed! Hidden treasure room!

---

### Unit 32: Mini-Boss Encounter

**Learning Objectives:**
- Stronger enemy
- Special combat
- Progress gate

**Concepts Introduced:**
- Mini-boss enemy type
- Health bar
- Special patterns
- Key/item drop

**Code Written:**
- Mini-boss AI
- Health display
- Attack patterns
- Reward drop

**What the Learner Sees:**
Mini-boss blocks path! Defeat for key to continue.

**Reference to Night Raid:**
"Boss encounter concepts from Night Raid adapted for adventure format."

---

## Phase 3: Polish (Units 33-48)
*Quests, story, visual/audio polish.*

### Unit 33: Quest System Framework

**Learning Objectives:**
- Multiple objectives
- Quest tracking
- Progress display

**Concepts Introduced:**
- Quest data structure
- Objective tracking
- Completion detection
- Progress display

**Code Written:**
- Quest structure
- Objective tracking
- Status checking
- Framework ready

**What the Learner Sees:**
(Quest system ready.)

---

### Unit 34: Main Quest

**Learning Objectives:**
- Primary game objective
- Quest stages
- Final goal

**Concepts Introduced:**
- Main quest design
- Stage progression
- Win condition
- Narrative arc

**Code Written:**
- Main quest data
- Stage detection
- Progress tracking
- Victory condition

**What the Learner Sees:**
Main quest tracked! "Find the three sacred crystals" - objectives displayed.

---

### Unit 35: Side Quests

**Learning Objectives:**
- Optional objectives
- Additional content
- Rewards

**Concepts Introduced:**
- Optional quests
- NPC-given quests
- Bonus rewards
- Extended content

**Code Written:**
- Side quest data
- Accept/complete flow
- Bonus rewards
- Optional tracking

**What the Learner Sees:**
NPC offers side quest! Optional content for bonus rewards.

---

### Unit 36: Quest Items

**Learning Objectives:**
- Quest-specific items
- Objective items
- Collection goals

**Concepts Introduced:**
- Quest item type
- Objective linkage
- Collection tracking
- Quest progress

**Code Written:**
- Quest item handling
- Objective updates
- Collection feedback
- Progress integration

**What the Learner Sees:**
Quest items! "Sacred Crystal obtained - 1 of 3 collected!"

---

### Unit 37: Sound Design - Ambiance

**Learning Objectives:**
- Dungeon atmosphere
- Environmental audio
- Mood creation

**Concepts Introduced:**
- Ambient sounds
- Room-based audio
- Atmosphere creation
- Subtle effects

**Code Written:**
- Ambient audio
- Room triggers
- Sound selection
- Mood setting

**What the Learner Sees:**
Dungeon ambiance! Dripping water, distant echoes - atmospheric!

**Reference to SID Symphony:**
"SID techniques for atmospheric sound effects."

---

### Unit 38: Sound Design - Actions

**Learning Objectives:**
- Action feedback sounds
- Combat audio
- Interaction sounds

**Concepts Introduced:**
- Action sound palette
- Combat sounds
- Interaction sounds
- Feedback importance

**Code Written:**
- Action sounds
- Combat audio
- Pickup sounds
- Complete palette

**What the Learner Sees:**
Every action has sound - sword swing, item collect, door open!

---

### Unit 39: Background Music

**Learning Objectives:**
- Dungeon music
- Area themes
- Atmosphere enhancement

**Concepts Introduced:**
- Area music
- Theme per zone
- Music system
- Mood matching

**Code Written:**
- Music composition
- Area triggers
- Music playback
- Transitions

**What the Learner Sees:**
Atmospheric music per area - dungeon theme, safe room theme, boss theme!

---

### Unit 40: Visual Polish

**Learning Objectives:**
- Enhance visuals
- Consistent style
- Professional appearance

**Concepts Introduced:**
- Visual consistency
- Character refinement
- Animation polish
- Professional look

**Code Written:**
- Visual improvements
- Animation refinement
- Consistency fixes
- Polish details

**What the Learner Sees:**
Everything looks polished - consistent dungeon aesthetic!

---

### Unit 41: Save System - Password

**Learning Objectives:**
- State serialization
- Password generation
- State restoration

**Concepts Introduced:**
- Game state encoding
- Password format
- State restoration
- Continue progress

**Code Written:**
- State collection
- Password generation
- Input handling
- State restoration

**What the Learner Sees:**
Get password to save progress! Enter password to continue!

---

### Unit 42: Save System - Polish

**Learning Objectives:**
- Reliable state save
- User-friendly display
- Error handling

**Concepts Introduced:**
- Error checking
- User interface
- Validation
- Friendly display

**Code Written:**
- Error handling
- Friendly UI
- Validation
- Polish

**What the Learner Sees:**
Save/load password system polished and reliable!

---

### Unit 43: Map Display

**Learning Objectives:**
- Show explored map
- Navigation aid
- Progress visualization

**Concepts Introduced:**
- Map tracking
- Explored rooms
- Map display
- Player position

**Code Written:**
- Exploration tracking
- Map rendering
- Toggle display
- Position marker

**What the Learner Sees:**
Press button - map shows explored rooms! Navigate large dungeon.

---

### Unit 44: Title Screen

**Learning Objectives:**
- Professional title
- Options
- Polish

**Concepts Introduced:**
- Title design
- Option menu
- New/continue
- Professional appearance

**Code Written:**
- Title screen
- Menu system
- Password entry
- Polish

**What the Learner Sees:**
Professional title screen with new game and continue options!

---

### Unit 45: Dungeon Design - Layout

**Learning Objectives:**
- Design full dungeon
- Zone planning
- Progress flow

**Concepts Introduced:**
- Dungeon design principles
- Zone themes
- Progress gating
- Exploration flow

**Code Written:**
- Dungeon layout
- Zone definitions
- Room data
- Connection planning

**What the Learner Sees:**
Full dungeon designed - multiple themed areas, logical flow!

---

### Unit 46: Dungeon Design - Population

**Learning Objectives:**
- Place enemies
- Place items
- Balance challenge

**Concepts Introduced:**
- Enemy placement
- Item distribution
- Challenge balance
- Reward pacing

**Code Written:**
- Enemy placement data
- Item distribution
- Balance tuning
- Testing

**What the Learner Sees:**
Dungeon populated - enemies, items, treasures appropriately placed!

---

### Unit 47: Final Boss

**Learning Objectives:**
- Ultimate challenge
- Multi-phase fight
- Victory reward

**Concepts Introduced:**
- Final boss design
- Multiple phases
- Challenge climax
- Victory sequence

**Code Written:**
- Final boss AI
- Phase system
- Victory handling
- Ending trigger

**What the Learner Sees:**
Final boss battle! Multiple phases, ultimate challenge, victory!

---

### Unit 48: Ending Sequence

**Learning Objectives:**
- Victory celebration
- Story conclusion
- Satisfying ending

**Concepts Introduced:**
- Ending sequence
- Story conclusion
- Statistics display
- Replay invitation

**Code Written:**
- Ending display
- Story text
- Stats summary
- Credits

**What the Learner Sees:**
Victory! Ending story plays, statistics shown, credits roll!

---

## Phase 4: Mastery (Units 49-64)
*Advanced features, optimization, polish.*

### Unit 49: Procedural Elements

**Learning Objectives:**
- Procedural room variation
- Replay variety
- Dynamic content

**Concepts Introduced:**
- Procedural tweaks
- Enemy variation
- Item randomization
- Fresh replays

**Code Written:**
- Variation systems
- Random elements
- Seed-based generation
- Replay value

**What the Learner Sees:**
Some variety on replays - different item placements, enemy positions!

---

### Unit 50: Additional Enemies

**Learning Objectives:**
- More enemy types
- Behaviour variety
- Challenge variety

**Concepts Introduced:**
- New enemy designs
- Different behaviours
- Zone-appropriate
- Visual variety

**Code Written:**
- New enemy types
- Varied AI patterns
- Zone assignment
- Integration

**What the Learner Sees:**
More enemy variety! Bats, skeletons, slimes - different behaviours!

---

### Unit 51: Additional Items

**Learning Objectives:**
- More item types
- Equipment variety
- Strategic depth

**Concepts Introduced:**
- Weapon upgrades
- Defensive items
- Special abilities
- Equipment depth

**Code Written:**
- New item types
- Equipment handling
- Effect implementation
- Integration

**What the Learner Sees:**
More items! Stronger sword, shield, special tools for puzzles!

---

### Unit 52: Performance Optimization

**Learning Objectives:**
- Optimize room rendering
- Smooth performance
- Efficient code

**Concepts Introduced:**
- Rendering optimization
- Update efficiency
- Collision optimization
- Smooth gameplay

**Code Written:**
- Rendering optimization
- Update refinement
- Collision efficiency
- Verification

**What the Learner Sees:**
(Smooth, responsive gameplay.)

---

### Unit 53: Multiple Dungeons

**Learning Objectives:**
- Additional dungeon content
- Extended game
- More exploration

**Concepts Introduced:**
- Multiple dungeon areas
- Overworld connection (simple)
- Extended content
- Replayability

**Code Written:**
- Additional dungeon data
- Area connections
- Extended content
- Integration

**What the Learner Sees:**
More dungeons! Extended content for longer adventure!

---

### Unit 54: New Game Plus

**Learning Objectives:**
- Replay with bonuses
- Harder difficulty
- Replay incentive

**Concepts Introduced:**
- NG+ concept
- Carryover items
- Increased difficulty
- Replay value

**Code Written:**
- NG+ detection
- Difficulty adjustment
- Item carryover
- Implementation

**What the Learner Sees:**
Beat the game - New Game Plus unlocked! Harder, keep some items!

---

### Unit 55: Achievements

**Learning Objectives:**
- Optional goals
- Recognition system
- Completionist appeal

**Concepts Introduced:**
- Achievement tracking
- Detection triggers
- Display system
- Long-term goals

**Code Written:**
- Achievement system
- Trigger detection
- Display integration
- Persistence

**What the Learner Sees:**
Achievements! "Defeated 100 enemies" - optional goals to chase!

---

### Unit 56: Statistics

**Learning Objectives:**
- Track gameplay stats
- Progress display
- Data tracking

**Concepts Introduced:**
- Statistics system
- Lifetime tracking
- Display screen
- Data persistence

**Code Written:**
- Stats tracking
- Display screen
- Persistence
- Integration

**What the Learner Sees:**
Statistics screen - enemies defeated, rooms explored, treasures found!

---

### Unit 57: Accessibility Options

**Learning Objectives:**
- Difficulty options
- Player accommodation
- Accessibility

**Concepts Introduced:**
- Difficulty settings
- Visual options
- Control options
- Inclusive design

**Code Written:**
- Options menu
- Settings application
- Save preferences
- Integration

**What the Learner Sees:**
Options for all players - easier modes, visual settings!

---

### Unit 58: Tutorial Integration

**Learning Objectives:**
- Teach mechanics
- Early game guidance
- New player support

**Concepts Introduced:**
- Tutorial design
- Progressive teaching
- In-game guidance
- Skip option

**Code Written:**
- Tutorial messages
- Trigger points
- Progressive reveal
- Skip option

**What the Learner Sees:**
First time playing - helpful hints appear! Skip if experienced.

---

### Unit 59: Audio Polish

**Learning Objectives:**
- Final audio refinements
- Mix balance
- Complete soundscape

**Concepts Introduced:**
- Audio review
- Balance adjustments
- Effect refinement
- Final tuning

**Code Written:**
- Audio adjustments
- Mix refinement
- Final touches

**What the Learner Sees:**
Audio perfectly balanced - music, effects, ambiance all clear!

---

### Unit 60: Bug Hunting

**Learning Objectives:**
- Find and fix bugs
- Edge cases
- Polish

**Concepts Introduced:**
- Systematic testing
- Edge case handling
- Bug fixes
- Quality assurance

**Code Written:**
- Bug fixes
- Edge case handling
- Polish fixes
- Verification

**What the Learner Sees:**
(Stable, polished experience.)

---

### Unit 61: Memory Optimization

**Learning Objectives:**
- Efficient memory use
- Data compression
- Room for content

**Concepts Introduced:**
- Memory review
- Data compression
- Efficient storage
- Documentation

**Code Written:**
- Memory optimization
- Data compression
- Layout documentation
- Verification

**What the Learner Sees:**
(Internal - more room for dungeon content.)

---

### Unit 62: Extended Testing

**Learning Objectives:**
- Full playthrough testing
- Balance verification
- Quality assurance

**Concepts Introduced:**
- Full testing
- Balance check
- Bug tracking
- Polish verification

**Code Written:**
- Test fixes
- Balance adjustments
- Polish fixes
- Documentation

**What the Learner Sees:**
(Complete, balanced, polished game.)

---

### Unit 63: Documentation

**Learning Objectives:**
- Document systems
- Technical reference
- Future reference

**Concepts Introduced:**
- System documentation
- Code comments
- Design documentation
- Reference value

**Code Written:**
- Documentation
- Code comments
- Design notes
- Reference guide

**What the Learner Sees:**
Complete documentation for adventure game systems!

---

### Unit 64: Release Build

**Learning Objectives:**
- Final release
- Debug removal
- Distribution ready

**Concepts Introduced:**
- Release process
- Debug removal
- Final testing
- Distribution prep

**Code Written:**
- Debug removal
- Final integration
- Release PRG
- Distribution

**What the Learner Sees:**
Complete Dungeon Crawl! Full adventure game ready for distribution!

---

## Summary

**Dungeon Crawl** teaches adventure game development:

**Phase 1 (Foundation):** Core systems - rooms, movement, keys/doors, basic exploration.

**Phase 2 (Expansion):** Content - combat, inventory, NPCs, puzzles, quests.

**Phase 3 (Polish):** Feel - story, audio, save system, full dungeon.

**Phase 4 (Mastery):** Advanced - optimization, extra content, polish, release.

### Skills Transferred Forward

The following skills debut in Dungeon Crawl and will be applied in future games:

1. **Multi-room map structure** → Isometric Quest, Mega Blaster (world navigation)
2. **Inventory system** → Arena Fighter (character loadout), many others
3. **Quest/objective tracking** → Isometric Quest, Symphony's End
4. **Save/password system** → All subsequent complex games
5. **NPC dialogue** → Isometric Quest
6. **Push puzzles** → Isometric Quest

### Game Specifications

- **Rooms:** 64+ connected rooms
- **Zones:** 4+ themed areas (dungeon, caves, forest, castle)
- **Items:** Keys, potions, quest items, equipment
- **Enemies:** 6+ types with different behaviours
- **Bosses:** 3+ mini-bosses, 1 final boss
- **Puzzles:** Keys/locks, switches, push blocks, hidden passages
- **NPCs:** 10+ with dialogue and hints
- **Save:** Password system for progress
- **Features:** Map display, inventory, quest tracking, achievements
