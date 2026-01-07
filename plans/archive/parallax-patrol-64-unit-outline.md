# Parallax Patrol: 64-Unit Outline

**Game:** 13 of 16
**Platform:** Commodore 64
**Units:** 64
**Concept:** Advanced side-scrolling shooter with multi-layer parallax. R-Type/Gradius-style shooter with weapon upgrades, large levels, and epic boss encounters.

---

## Skills Applied from Previous Games

| Skill | Learned In | Application in Parallax Patrol |
|-------|-----------|---------------------------|
| SID fundamentals | SID Symphony | Epic music, rich SFX |
| Hardware sprites | Starfield | Ship, enemies, bullets |
| Shooting mechanics | Starfield | Advanced weapon systems |
| Sprite collision | Starfield | Complex combat |
| Custom characters | Maze Raider | Terrain graphics |
| Hardware scrolling | Scroll Runner | Main scroll layer |
| Colour RAM scrolling | Scroll Runner | Coloured terrain |
| Double buffering | Scroll Runner | Smooth updates |
| Parallax backgrounds | Scroll Runner | Multi-layer parallax |
| Terrain collision | Night Raid | Wall collision |
| Level streaming | Night Raid | Long level data |
| Boss encounters | Night Raid | Epic bosses |
| Sprite multiplexing | Sprite Storm | Many enemies/bullets |
| Raster techniques | Raster Rider | Visual effects |
| Power-up systems | Various | Weapon upgrades |

## New Skills Introduced

| Skill | Units | Description |
|-------|-------|-------------|
| Multi-layer parallax | 5-8 | 3+ scroll layers |
| Layer management | 9-12 | Coordinating layers |
| Weapon upgrade paths | 17-24 | Branching upgrades |
| Large level memory | 25-28 | Level compression |
| Checkpoint system | 33-36 | Mid-level saves |
| Option drones | 29-32 | Following weapons |
| Charge shot | 41-44 | Held fire mechanic |
| Pattern-based enemies | 45-48 | Complex enemy paths |

---

## Phase 1: Foundation (Units 1-16)
*Core mechanics: multi-layer scrolling, shooting, basic combat.*

### Unit 1: Advanced Shooter Concept

**Learning Objectives:**
- Understand R-Type/Gradius design
- Plan parallax implementation
- Design game structure

**Concepts Introduced:**
- Multi-layer scrolling
- Weapon progression
- Long level design
- Boss-focused structure

**Code Written:**
- Design document
- Layer planning
- Weapon system design
- Level structure plan

**What the Learner Sees:**
Understanding the advanced shooter we're building - layers, weapons, bosses.

---

### Unit 2: Background Layer

**Learning Objectives:**
- Slowest scroll layer
- Distant background
- Star field or clouds

**Concepts Introduced:**
- Background layer concept
- Very slow scroll
- Simple graphics
- Depth foundation

**Code Written:**
- Background scroll setup
- Character graphics
- Slow update rate
- Visual foundation

**What the Learner Sees:**
Distant stars/clouds scroll very slowly - depth foundation.

**Reference to Scroll Runner:**
"Parallax concept from Scroll Runner, now with more layers."

---

### Unit 3: Middle Layer

**Learning Objectives:**
- Medium-speed layer
- Distant terrain
- Depth enhancement

**Concepts Introduced:**
- Middle layer
- Medium scroll speed
- Mountain/building silhouettes
- Enhanced depth

**Code Written:**
- Middle layer scroll
- Silhouette graphics
- Speed relationship
- Layer coordination

**What the Learner Sees:**
Mountains scroll at medium speed behind gameplay - more depth!

---

### Unit 4: Foreground Layer

**Learning Objectives:**
- Main gameplay layer
- Full-speed scroll
- Collision terrain

**Concepts Introduced:**
- Foreground (main) layer
- 1:1 scroll with gameplay
- Collision terrain
- Primary layer

**Code Written:**
- Main scroll layer
- Terrain graphics
- Full-speed scroll
- Collision data

**What the Learner Sees:**
Main terrain scrolls at full speed - this is the gameplay layer!

---

### Unit 5: Three-Layer Parallax

**Learning Objectives:**
- Coordinate three layers
- Different scroll speeds
- Unified appearance

**Concepts Introduced:**
- Layer coordination
- Speed ratios
- Visual coherence
- Performance budget

**Code Written:**
- Layer management
- Coordinated updates
- Speed calculations
- Unified display

**What the Learner Sees:**
Three layers of parallax! Deep, atmospheric scrolling!

---

### Unit 6: Player Ship

**Learning Objectives:**
- Player ship sprite
- 8-direction movement
- Screen positioning

**Concepts Introduced:**
- Ship sprite design
- Full movement
- Screen boundaries
- Player entity

**Code Written:**
- Ship sprite data
- Movement control
- Boundary handling
- Entity structure

**What the Learner Sees:**
Player ship flies freely! Full 8-direction control.

---

### Unit 7: Basic Shooting

**Learning Objectives:**
- Fire button shoots
- Forward bullets
- Bullet management

**Concepts Introduced:**
- Basic weapon
- Bullet pool
- Forward fire
- Fire rate

**Code Written:**
- Bullet sprite
- Fire handling
- Bullet movement
- Pool management

**What the Learner Sees:**
Fire button shoots! Bullets fly forward.

**Reference to Night Raid:**
"Shooting system from Night Raid as foundation for more complex weapons."

---

### Unit 8: Basic Enemy

**Learning Objectives:**
- Simple enemy type
- Movement pattern
- Score target

**Concepts Introduced:**
- Enemy entity
- Simple pattern
- Collision target
- Score value

**Code Written:**
- Enemy sprite
- Movement pattern
- Spawn logic
- Collision handling

**What the Learner Sees:**
Enemies fly in! Shoot them for points!

---

### Unit 9: Enemy Waves

**Learning Objectives:**
- Coordinated enemy groups
- Wave patterns
- Formation flying

**Concepts Introduced:**
- Wave data
- Coordinated spawning
- Formation patterns
- Wave completion

**Code Written:**
- Wave system
- Formation data
- Coordinated spawn
- Wave tracking

**What the Learner Sees:**
Enemies in formations! Coordinated wave attacks!

---

### Unit 10: Terrain Collision

**Learning Objectives:**
- Ship hits walls
- Death on terrain
- Navigation challenge

**Concepts Introduced:**
- Terrain collision
- Death trigger
- Navigation skill
- Tight passages

**Code Written:**
- Collision detection
- Death handling
- Navigation challenge
- Feedback

**What the Learner Sees:**
Hit terrain - death! Must navigate carefully through passages.

---

### Unit 11: Lives and Score

**Learning Objectives:**
- Lives system
- Score tracking
- HUD display

**Concepts Introduced:**
- Lives counter
- Score accumulation
- Display layout
- Game over

**Code Written:**
- Lives tracking
- Score system
- HUD rendering
- Game over handling

**What the Learner Sees:**
Lives and score displayed! Standard shooter HUD.

---

### Unit 12: Enemy Bullets

**Learning Objectives:**
- Enemies shoot back
- Bullet patterns
- Danger from enemies

**Concepts Introduced:**
- Enemy bullet pool
- Fire patterns
- Player collision
- Dodge requirement

**Code Written:**
- Enemy bullets
- Pattern firing
- Player collision
- Pool management

**What the Learner Sees:**
Enemies fire back! Dodge their bullets!

---

### Unit 13: Power-Up Framework

**Learning Objectives:**
- Power-up drops
- Collection mechanic
- Upgrade preparation

**Concepts Introduced:**
- Power-up sprites
- Drop from enemies
- Collection collision
- Effect framework

**Code Written:**
- Power-up system
- Drop logic
- Collection handling
- Framework ready

**What the Learner Sees:**
Power-ups drop from enemies! Collect them for upgrades!

---

### Unit 14: Weapon Upgrade - Speed

**Learning Objectives:**
- First upgrade type
- Faster fire rate
- Power increase

**Concepts Introduced:**
- Fire rate upgrade
- Level tracking
- Maximum level
- Visual indicator

**Code Written:**
- Fire rate levels
- Upgrade handling
- Level display
- Max capping

**What the Learner Sees:**
Collect speed power-up - fire faster! Upgrade levels shown.

---

### Unit 15: Simple Boss

**Learning Objectives:**
- End-of-section boss
- Health bar
- Pattern attack

**Concepts Introduced:**
- Boss entity
- High health
- Attack pattern
- Victory condition

**Code Written:**
- Boss structure
- Health tracking
- Attack patterns
- Defeat handling

**What the Learner Sees:**
Boss battle! Large enemy with health bar - learn the pattern!

**Reference to Night Raid:**
"Boss concepts from Night Raid, now expanded for advanced shooter."

---

### Unit 16: Complete Stage 1

**Learning Objectives:**
- Full first stage
- Boss fight
- Playable completion

**Concepts Introduced:**
- Complete stage
- Beginning to boss
- Victory transition
- Foundation complete

**Code Written:**
- Stage 1 complete
- Boss defeat
- Transition handling
- Stage structure

**What the Learner Sees:**
Complete first stage! Enemies, terrain, boss - full shooter experience!

---

## Phase 2: Expansion (Units 17-32)
*Weapon variety, option drones, multiple stages.*

### Unit 17: Weapon Type - Spread

**Learning Objectives:**
- Spread shot weapon
- Multiple directions
- Different strategy

**Concepts Introduced:**
- Spread weapon type
- 3-way or 5-way fire
- Coverage vs focus
- Weapon choice

**Code Written:**
- Spread weapon
- Multiple bullets
- Angle calculation
- Weapon switching

**What the Learner Sees:**
Spread weapon! Fires in multiple directions - area coverage!

---

### Unit 18: Weapon Type - Laser

**Learning Objectives:**
- Beam weapon
- Continuous fire
- High damage

**Concepts Introduced:**
- Laser weapon
- Beam rendering
- Sustained damage
- Power trade-off

**Code Written:**
- Laser rendering
- Damage over time
- Visual effect
- Weapon balance

**What the Learner Sees:**
Laser weapon! Continuous beam - high focused damage!

---

### Unit 19: Weapon Type - Missile

**Learning Objectives:**
- Homing missiles
- Tracking enemies
- Smart weapon

**Concepts Introduced:**
- Homing missiles
- Target tracking
- Limited fire rate
- Smart targeting

**Code Written:**
- Missile logic
- Tracking algorithm
- Rate limiting
- Target selection

**What the Learner Sees:**
Homing missiles! Seek out enemies automatically!

---

### Unit 20: Weapon Selection System

**Learning Objectives:**
- Choose weapon type
- Power-up selection
- Strategic choice

**Concepts Introduced:**
- Weapon cycling
- Selection input
- Current weapon display
- Strategic depth

**Code Written:**
- Weapon system
- Selection handling
- Display update
- Integration

**What the Learner Sees:**
Cycle weapons! Choose the right tool for each situation!

---

### Unit 21: Weapon Upgrade Levels

**Learning Objectives:**
- Per-weapon upgrades
- Power progression
- Build investment

**Concepts Introduced:**
- Level per weapon
- Upgrade power-ups
- Progressive strength
- Build paths

**Code Written:**
- Per-weapon levels
- Upgrade handling
- Power scaling
- Display

**What the Learner Sees:**
Upgrade each weapon! Max level = devastating power!

---

### Unit 22: Shield System

**Learning Objectives:**
- Defensive power-up
- Hit absorption
- Survival option

**Concepts Introduced:**
- Shield hit points
- Absorb damage
- Visual display
- Strategic resource

**Code Written:**
- Shield system
- Hit absorption
- Display
- Depletion handling

**What the Learner Sees:**
Shield power-up! Absorbs hits - extra survivability!

**Reference to Sprite Storm:**
"Shield concept from Sprite Storm power-ups, expanded for shooter."

---

### Unit 23: Bomb/Smart Bomb

**Learning Objectives:**
- Screen-clear weapon
- Limited stock
- Emergency save

**Concepts Introduced:**
- Smart bomb
- Stock tracking
- Clear effect
- Strategic use

**Code Written:**
- Bomb system
- Stock handling
- Clear effect
- Invulnerability

**What the Learner Sees:**
Smart bomb! Clears screen - limited stock, use wisely!

---

### Unit 24: Death and Power Loss

**Learning Objectives:**
- Death power penalty
- Partial loss
- Recovery challenge

**Concepts Introduced:**
- Power loss on death
- Partial preservation
- Recovery difficulty
- Balance design

**Code Written:**
- Death handling
- Power reduction
- Preservation rules
- Balance

**What the Learner Sees:**
Death costs power! Lose some upgrades - recover to full strength.

---

### Unit 25: Option Drone Framework

**Learning Objectives:**
- Following weapons
- R-Type style options
- Secondary fire

**Concepts Introduced:**
- Option drone concept
- Following behaviour
- Secondary weapon
- Power multiplication

**Code Written:**
- Option structure
- Following algorithm
- Framework ready

**What the Learner Sees:**
(Option framework ready.)

---

### Unit 26: Option Drone Implementation

**Learning Objectives:**
- Options follow ship
- Fire when player fires
- Power doubling

**Concepts Introduced:**
- Trail following
- Synchronized fire
- Multiple options
- Power boost

**Code Written:**
- Option following
- Fire sync
- Multiple handling
- Display

**What the Learner Sees:**
Options follow ship and fire! Double, triple, quadruple firepower!

---

### Unit 27: Option Formations

**Learning Objectives:**
- Option positioning
- Formation modes
- Strategic placement

**Concepts Introduced:**
- Formation modes
- Above/below/front/behind
- Mode switching
- Strategic use

**Code Written:**
- Formation options
- Mode switching
- Position calculation
- Visual update

**What the Learner Sees:**
Switch option formations! Different coverage for different situations!

---

### Unit 28: Level Data Compression

**Learning Objectives:**
- Efficient level storage
- RLE compression
- Long levels possible

**Concepts Introduced:**
- Run-length encoding
- Level compression
- Decompression streaming
- Memory efficiency

**Code Written:**
- Compression format
- Decompression routine
- Streaming integration
- Efficiency verification

**What the Learner Sees:**
(Internal - longer levels possible with compression.)

---

### Unit 29: Stage 2 Design

**Learning Objectives:**
- Second stage content
- Different theme
- Progress expansion

**Concepts Introduced:**
- Stage theming
- Visual variety
- Enemy variety
- Boss variety

**Code Written:**
- Stage 2 terrain
- Stage 2 enemies
- Stage 2 boss
- Integration

**What the Learner Sees:**
Stage 2! Different theme, new enemies, new boss!

---

### Unit 30: Stage 3 Design

**Learning Objectives:**
- Third stage content
- Increasing challenge
- Mid-game difficulty

**Concepts Introduced:**
- Challenge escalation
- Mid-game design
- Complex terrain
- Tougher enemies

**Code Written:**
- Stage 3 content
- Enemy patterns
- Boss encounter
- Challenge tuning

**What the Learner Sees:**
Stage 3! Harder terrain, tougher enemies, intense boss!

---

### Unit 31: Stage 4-5 Design

**Learning Objectives:**
- Later stages
- High difficulty
- Endgame content

**Concepts Introduced:**
- Late-game design
- Maximum difficulty
- Complex patterns
- Epic bosses

**Code Written:**
- Stages 4-5 content
- High difficulty
- Epic bosses
- Endgame tuning

**What the Learner Sees:**
Stages 4 and 5! Maximum challenge, epic battles!

---

### Unit 32: Final Stage

**Learning Objectives:**
- Ultimate stage
- Final boss
- Game climax

**Concepts Introduced:**
- Final stage design
- Ultimate challenge
- Final boss
- Victory condition

**Code Written:**
- Final stage
- Final boss
- Victory handling
- Ending trigger

**What the Learner Sees:**
Final stage! Ultimate challenge, epic final boss, victory!

---

## Phase 3: Polish (Units 33-48)
*Effects, sound, checkpoints, presentation.*

### Unit 33: Checkpoint System

**Learning Objectives:**
- Mid-level saves
- Respawn points
- Difficulty balance

**Concepts Introduced:**
- Checkpoint markers
- Respawn position
- State preservation
- Fair difficulty

**Code Written:**
- Checkpoint system
- Respawn handling
- State management
- Balance

**What the Learner Sees:**
Checkpoints! Respawn at checkpoint after death - fair challenge!

---

### Unit 34: Hit Effects

**Learning Objectives:**
- Visual impact feedback
- Explosion variety
- Satisfaction enhancement

**Concepts Introduced:**
- Hit effects
- Explosion variety
- Screen shake
- Visual feedback

**Code Written:**
- Hit effects
- Explosion sprites
- Screen shake
- Polish

**What the Learner Sees:**
Impacts look amazing! Explosions, sparks, screen shake!

---

### Unit 35: Sound Design - Weapons

**Learning Objectives:**
- Weapon audio
- Distinct per weapon
- Satisfying fire

**Concepts Introduced:**
- Weapon sound palette
- Distinct sounds
- Impact sounds
- Satisfaction

**Code Written:**
- Weapon sounds
- Fire sounds
- Impact sounds
- Complete palette

**What the Learner Sees:**
Each weapon sounds distinct and powerful!

**Reference to SID Symphony:**
"Full SID Symphony techniques for rich weapon audio."

---

### Unit 36: Sound Design - Enemies

**Learning Objectives:**
- Enemy audio
- Death sounds
- Warning sounds

**Concepts Introduced:**
- Enemy sound palette
- Death sounds
- Warning cues
- Audio feedback

**Code Written:**
- Enemy sounds
- Death audio
- Warning sounds
- Integration

**What the Learner Sees:**
Enemies have distinctive audio - warnings and satisfying deaths!

---

### Unit 37: Stage Music

**Learning Objectives:**
- Per-stage music
- Epic compositions
- Mood setting

**Concepts Introduced:**
- Stage themes
- Musical variety
- Boss themes
- Atmosphere

**Code Written:**
- Stage music
- Boss themes
- Music system
- Transitions

**What the Learner Sees:**
Epic music per stage! Boss themes are intense!

---

### Unit 38: Parallax Enhancement

**Learning Objectives:**
- Visual polish
- Additional effects
- Atmosphere enhancement

**Concepts Introduced:**
- Additional parallax effects
- Atmospheric elements
- Visual depth
- Polish details

**Code Written:**
- Enhanced parallax
- Atmospheric effects
- Visual polish
- Integration

**What the Learner Sees:**
Even better parallax! Additional depth effects, atmospheric!

---

### Unit 39: Enemy Pattern Variety

**Learning Objectives:**
- Complex enemy patterns
- Challenging movement
- Pattern recognition

**Concepts Introduced:**
- Complex patterns
- Sine wave movement
- Dive patterns
- Challenge variety

**Code Written:**
- Pattern library
- Complex movements
- Pattern enemies
- Integration

**What the Learner Sees:**
Enemies with complex patterns! Sine waves, dives, formations!

---

### Unit 40: Mini-Boss Encounters

**Learning Objectives:**
- Mid-stage bosses
- Challenge pacing
- Variety injection

**Concepts Introduced:**
- Mini-boss concept
- Mid-stage placement
- Simpler patterns
- Pacing tool

**Code Written:**
- Mini-boss system
- Stage placement
- Pattern design
- Integration

**What the Learner Sees:**
Mini-bosses mid-stage! Pacing variety, checkpoint markers!

---

### Unit 41: Charge Shot

**Learning Objectives:**
- Held fire mechanic
- Powerful charged attack
- Risk/reward

**Concepts Introduced:**
- Charge mechanic
- Hold to charge
- Powerful release
- Timing skill

**Code Written:**
- Charge tracking
- Power levels
- Release handling
- Visual indicator

**What the Learner Sees:**
Hold fire to charge! Massive shot on release!

---

### Unit 42: Title Screen

**Learning Objectives:**
- Professional title
- Mode selection
- Demo mode

**Concepts Introduced:**
- Impressive title
- Mode options
- Demo playback
- Professional look

**Code Written:**
- Title screen
- Mode menu
- Demo system
- Polish

**What the Learner Sees:**
Epic title screen! Demo shows off the game!

---

### Unit 43: High Score System

**Learning Objectives:**
- Score tracking
- Leaderboard
- Competition

**Concepts Introduced:**
- High score table
- Initial entry
- Persistence
- Competition

**Code Written:**
- Score system
- Entry screen
- Persistence
- Display

**What the Learner Sees:**
High scores saved! Compete for the top!

---

### Unit 44: Statistics

**Learning Objectives:**
- Track gameplay
- Lifetime stats
- Achievement tracking

**Concepts Introduced:**
- Statistics tracking
- Lifetime totals
- Display screen
- Progress tracking

**Code Written:**
- Stats system
- Display
- Persistence
- Integration

**What the Learner Sees:**
Statistics track your progress - enemies destroyed, stages beaten!

---

### Unit 45: Difficulty Options

**Learning Objectives:**
- Accessibility settings
- Challenge options
- Player choice

**Concepts Introduced:**
- Difficulty levels
- Parameter adjustment
- Accessibility
- Choice

**Code Written:**
- Difficulty options
- Parameter tables
- Application
- Saving

**What the Learner Sees:**
Choose difficulty! Easy to Hard - play your way!

---

### Unit 46: Continue System

**Learning Objectives:**
- Continue option
- Credit system
- Extended play

**Concepts Introduced:**
- Continue mechanic
- Credit limitation
- Score penalty
- Accessibility

**Code Written:**
- Continue system
- Credit handling
- Score penalty
- Integration

**What the Learner Sees:**
Continue option! Use credits to continue - see the whole game!

---

### Unit 47: Visual Polish

**Learning Objectives:**
- Final visual refinements
- Consistency check
- Professional quality

**Concepts Introduced:**
- Visual review
- Consistency fixes
- Effect polish
- Professional look

**Code Written:**
- Visual polish
- Consistency
- Effect refinement
- Final touches

**What the Learner Sees:**
Everything polished - consistent, beautiful, professional!

---

### Unit 48: Audio Polish

**Learning Objectives:**
- Final audio refinements
- Mix balance
- Complete soundscape

**Concepts Introduced:**
- Audio review
- Mix balance
- Final adjustments
- Complete sound

**Code Written:**
- Audio polish
- Mix adjustments
- Final touches

**What the Learner Sees:**
Audio perfectly balanced - epic music, powerful sounds!

---

## Phase 4: Mastery (Units 49-64)
*Optimization, additional content, polish.*

### Unit 49: Performance Optimization

**Learning Objectives:**
- Optimize all systems
- Smooth performance
- Maximum quality

**Concepts Introduced:**
- Performance profiling
- Bottleneck elimination
- Smooth gameplay
- Quality focus

**Code Written:**
- Optimization passes
- Efficiency improvements
- Verification
- Documentation

**What the Learner Sees:**
(Rock-solid smooth performance.)

---

### Unit 50: Multiplexer Optimization

**Learning Objectives:**
- Maximum sprites
- Optimal multiplexing
- Many objects

**Concepts Introduced:**
- Multiplexer tuning
- Maximum capacity
- Flicker management
- Optimal performance

**Code Written:**
- Multiplexer optimization
- Capacity testing
- Verification

**What the Learner Sees:**
(Maximum objects on screen without issues.)

**Reference to Sprite Storm:**
"Apply Sprite Storm's multiplexer optimization for maximum capacity."

---

### Unit 51: Stage 6-7 (Bonus Stages)

**Learning Objectives:**
- Additional content
- Bonus stages
- Extended game

**Concepts Introduced:**
- Bonus stages
- Different rules
- Score opportunities
- Extended content

**Code Written:**
- Bonus stage content
- Modified rules
- Score focus
- Integration

**What the Learner Sees:**
Bonus stages! Extended content, score opportunities!

---

### Unit 52: Two-Player Mode

**Learning Objectives:**
- Cooperative play
- Two players simultaneously
- Shared experience

**Concepts Introduced:**
- Two-player co-op
- Simultaneous play
- Shared screen
- Competition/cooperation

**Code Written:**
- Two-player support
- Input handling
- Display management
- Integration

**What the Learner Sees:**
Two-player co-op! Fight together through the stages!

---

### Unit 53: Boss Rush Mode

**Learning Objectives:**
- Boss-only mode
- Challenge mode
- Replayability

**Concepts Introduced:**
- Boss rush concept
- Sequential bosses
- Time attack
- Challenge mode

**Code Written:**
- Boss rush mode
- Sequential loading
- Timer
- Integration

**What the Learner Sees:**
Boss rush mode! Fight all bosses in sequence - time attack!

---

### Unit 54: Weapon Mastery

**Learning Objectives:**
- Maxed weapon effects
- Ultimate power
- Achievement reward

**Concepts Introduced:**
- Maximum power weapons
- Visual enhancement
- Achievement tracking
- Power fantasy

**Code Written:**
- Max power effects
- Visual enhancements
- Achievement integration
- Power display

**What the Learner Sees:**
Maxed weapons look incredible! Ultimate power achieved!

---

### Unit 55: Secret Areas

**Learning Objectives:**
- Hidden content
- Exploration reward
- Replay value

**Concepts Introduced:**
- Secret paths
- Hidden power-ups
- Exploration reward
- Discovery

**Code Written:**
- Secret detection
- Hidden areas
- Bonus content
- Discovery tracking

**What the Learner Sees:**
Secret areas! Hidden paths with bonus power-ups!

---

### Unit 56: True Final Boss

**Learning Objectives:**
- Ultimate challenge
- Unlock condition
- True ending

**Concepts Introduced:**
- Hidden boss
- Unlock requirements
- True ending
- Ultimate challenge

**Code Written:**
- True boss
- Unlock checking
- True ending
- Ultimate difficulty

**What the Learner Sees:**
True final boss! Hidden ultimate challenge - true ending!

---

### Unit 57: Gallery Mode

**Learning Objectives:**
- Artwork viewing
- Unlockable content
- Collection reward

**Concepts Introduced:**
- Gallery system
- Art assets
- Unlock tracking
- Collection

**Code Written:**
- Gallery mode
- Asset display
- Unlock system
- Integration

**What the Learner Sees:**
Gallery mode! View art, track unlocks, collection reward!

---

### Unit 58: Sound Test

**Learning Objectives:**
- Music/sound access
- Unlockable feature
- Fan service

**Concepts Introduced:**
- Sound test mode
- Music selection
- SFX playback
- Fan feature

**Code Written:**
- Sound test mode
- Selection interface
- Playback control
- Integration

**What the Learner Sees:**
Sound test! Listen to all music and sounds!

---

### Unit 59: Memory Map Review

**Learning Objectives:**
- Final memory layout
- Documentation
- Future reference

**Concepts Introduced:**
- Memory documentation
- Layout review
- Optimization review
- Reference creation

**Code Written:**
- Documentation
- Layout finalization
- Reference material

**What the Learner Sees:**
(Documentation - professional architecture.)

---

### Unit 60: Bug Hunting

**Learning Objectives:**
- Find and fix bugs
- Edge cases
- Quality assurance

**Concepts Introduced:**
- Testing methodology
- Edge case handling
- Bug fixes
- Quality

**Code Written:**
- Bug fixes
- Edge cases
- Polish
- Verification

**What the Learner Sees:**
(Stable, polished game.)

---

### Unit 61: Balance Pass

**Learning Objectives:**
- Difficulty balance
- Weapon balance
- Fair challenge

**Concepts Introduced:**
- Balance testing
- Difficulty tuning
- Weapon adjustment
- Fairness

**Code Written:**
- Balance adjustments
- Tuning passes
- Verification

**What the Learner Sees:**
(Perfectly balanced challenge.)

---

### Unit 62: Extended Testing

**Learning Objectives:**
- Full playthrough testing
- Quality verification
- Polish verification

**Concepts Introduced:**
- Complete testing
- Quality assurance
- Final verification
- Release criteria

**Code Written:**
- Test fixes
- Final polish
- Verification

**What the Learner Sees:**
(Complete, polished experience.)

---

### Unit 63: Documentation

**Learning Objectives:**
- Document advanced systems
- Technical reference
- Knowledge preservation

**Concepts Introduced:**
- Technical documentation
- System reference
- Code documentation
- Future reference

**Code Written:**
- Documentation
- Code comments
- Reference guide

**What the Learner Sees:**
Complete documentation for advanced shooter systems!

---

### Unit 64: Release Build

**Learning Objectives:**
- Final release
- Debug removal
- Distribution ready

**Concepts Introduced:**
- Release process
- Debug removal
- Final packaging
- Distribution

**Code Written:**
- Debug removal
- Final integration
- Release PRG
- Distribution

**What the Learner Sees:**
Complete Parallax Patrol! Commercial-quality shooter ready for distribution!

---

## Summary

**Parallax Patrol** teaches advanced shooter development:

**Phase 1 (Foundation):** Core systems - multi-layer parallax, shooting, combat.

**Phase 2 (Expansion):** Content - weapons, options, multiple stages.

**Phase 3 (Polish):** Presentation - effects, sound, checkpoints, modes.

**Phase 4 (Mastery):** Excellence - optimization, extra content, release.

### Skills Transferred Forward

The following skills are mastered in Parallax Patrol:

1. **Multi-layer parallax** → Mega Blaster, Symphony's End
2. **Advanced weapon systems** → Mega Blaster
3. **Option drone mechanics** → Mega Blaster
4. **Large level streaming** → Mega Blaster, Isometric Quest
5. **Checkpoint systems** → All remaining games
6. **Epic boss design** → Mega Blaster, Symphony's End

### Game Specifications

- **Parallax layers:** 3+ (background, middle, foreground)
- **Weapons:** 4 types (shot, spread, laser, missile)
- **Options:** Up to 4 option drones
- **Stages:** 7 (5 main + 2 bonus)
- **Bosses:** 7 (1 per stage + true final)
- **Special moves:** Charge shot, smart bomb
- **Players:** 1-2 cooperative
- **Modes:** Main game, boss rush, sound test, gallery
- **Features:** Checkpoints, difficulty options, continues
