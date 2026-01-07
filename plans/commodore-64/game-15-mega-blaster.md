# Mega Blaster: 128-Unit Outline

**Game:** 15 of 16
**Platform:** Commodore 64
**Units:** 128 (Advanced game)
**Concept:** Turrican-style run'n'gun. Large scrolling world, multiple weapons, special abilities, epic bosses. The culmination of platforming and shooting skills before the capstone.

---

## Why 128 Units?

Mega Blaster is a Turrican-class game - one of the most technically demanding genres on the C64:

1. **Multi-directional scrolling** with parallax
2. **Complex player mechanics** (run, jump, shoot, grapple, transform)
3. **Extensive weapon systems** with upgrades
4. **Large explorable levels** with secrets
5. **Epic multi-sprite bosses**
6. **Integration of nearly all curriculum skills**

This is the penultimate game, preparing learners for Symphony's End. It deserves the depth to produce something rivalling Turrican II.

---

## Skills Applied from Previous Games

**Mega Blaster integrates virtually ALL skills from the curriculum:**

| Skill Category | Applied Skills | Source Games |
|---------------|---------------|--------------|
| **Platforming** | Gravity, jumping, platform collision, variable jump | Platform Panic |
| **Shooting** | Weapons, bullets, enemy health, aiming | Starfield, Parallax Patrol |
| **Scrolling** | Hardware scroll, colour RAM, multi-direction | Scroll Runner, Night Raid |
| **Parallax** | Multi-layer backgrounds | Scroll Runner, Parallax Patrol |
| **Sprites** | Multiplexing, animation, priority | Sprite Storm |
| **Audio** | SID music, rich SFX, multi-voice | SID Symphony |
| **Memory** | Level streaming, compression | Night Raid, Parallax Patrol |
| **Combat** | Hit detection, damage, health | Arena Fighter, Dungeon Crawl |
| **Systems** | Lives, score, power-ups, checkpoints | All games |
| **Boss Fights** | Patterns, phases, weak points | Night Raid, Parallax Patrol |
| **Exploration** | Non-linear levels, secrets | Dungeon Crawl, Isometric Quest |

## New Skills Introduced

| Skill | Phase | Description |
|-------|-------|-------------|
| Multi-directional scrolling | 1 | Scroll in any direction smoothly |
| Camera system | 1 | Smart camera with lead and boundaries |
| Grappling hook physics | 3 | Rope attachment and swinging |
| Player transformation | 3 | Wheel mode with different physics |
| Weapon wheel system | 2 | Quick weapon switching |
| Large multi-sprite bosses | 5 | Bosses composed of many sprites |
| Exploration mapping | 4 | Metroidvania-style revealed map |
| Secret hunting | 4 | Hidden areas and collectibles |
| Demo-scene polish | 7 | Visual tricks for professional look |

---

## Phase 1: Core Engine (Units 1-16)
*Multi-directional scrolling and player foundation.*

### Unit 1: Mega Blaster Vision

**Learning Objectives:**
- Understand Turrican-style game design
- Plan technical requirements
- Design game structure

**Concepts Introduced:**
- Turrican as genre template (Factor 5, 1990)
- Large explorable worlds
- Weapon variety and upgrades
- Technical ambition

**What the Learner Sees:**
Design document for the most ambitious game yet.

---

### Unit 2: Multi-Direction Scroll - Theory

**Learning Objectives:**
- Understand bidirectional scrolling
- Plan scroll implementation
- Design memory layout

**Concepts Introduced:**
- Horizontal + vertical scrolling combined
- $D016 and $D011 scroll registers
- Screen buffer requirements
- Performance considerations

**What the Learner Sees:**
Technical plan for scrolling in any direction.

**Reference to Scroll Runner:**
"Scroll Runner taught horizontal scrolling. Now we add vertical and combine them."

---

### Unit 3: Multi-Direction Scroll - Horizontal

**Learning Objectives:**
- Implement horizontal scroll component
- Apply Scroll Runner techniques
- Prepare for vertical addition

**Concepts Introduced:**
- $D016 horizontal scroll
- Screen shift routine
- Column update routine
- Horizontal foundation

**Code Written:**
- Horizontal scroll implementation
- Screen buffer management
- Column streaming

**What the Learner Sees:**
Smooth horizontal scrolling working.

---

### Unit 4: Multi-Direction Scroll - Vertical

**Learning Objectives:**
- Implement vertical scroll component
- $D011 vertical scroll register
- Row-based updates

**Concepts Introduced:**
- $D011 vertical scroll bits
- Row shift vs column shift
- Top/bottom screen updates
- Vertical scrolling mechanics

**Code Written:**
- Vertical scroll implementation
- Row shift routine
- Row streaming

**What the Learner Sees:**
Smooth vertical scrolling added!

---

### Unit 5: Combined Scrolling

**Learning Objectives:**
- Combine horizontal and vertical
- Diagonal scrolling
- Unified scroll system

**Concepts Introduced:**
- Combined scroll register updates
- Diagonal movement handling
- Buffer management for both axes
- Performance optimization

**Code Written:**
- Combined scroll system
- Diagonal handling
- Unified buffer management

**What the Learner Sees:**
Scroll in any direction - horizontal, vertical, diagonal!

---

### Unit 6: Colour RAM Scrolling

**Learning Objectives:**
- Colour RAM for multi-direction
- Sync with character scroll
- Coloured terrain

**Concepts Introduced:**
- Colour RAM both directions
- Sync with screen scroll
- Performance impact
- Optimisation strategies

**Code Written:**
- Bidirectional colour RAM scroll
- Sync with screen
- Optimised routines

**What the Learner Sees:**
Coloured terrain scrolls correctly in all directions!

---

### Unit 7: Camera System - Basic

**Learning Objectives:**
- Camera follows player
- Dead zone concept
- Smooth following

**Concepts Introduced:**
- Camera vs player position
- Dead zone (no scroll region)
- Scroll triggers
- Smooth camera movement

**Code Written:**
- Camera position tracking
- Dead zone implementation
- Scroll triggering

**What the Learner Sees:**
Camera smoothly follows player with comfortable dead zone.

---

### Unit 8: Camera System - Advanced

**Learning Objectives:**
- Camera lead (look ahead)
- Vertical camera handling
- Camera boundaries

**Concepts Introduced:**
- Lead camera (bias in movement direction)
- Different vertical handling
- Level boundary clamping
- Professional camera feel

**Code Written:**
- Camera lead system
- Vertical camera logic
- Boundary handling

**What the Learner Sees:**
Professional camera that anticipates player movement!

---

### Unit 9: Parallax Layer - Background

**Learning Objectives:**
- Distant background layer
- Slow scroll rate
- Depth foundation

**Concepts Introduced:**
- Background parallax in 2D scroll
- Speed ratios for X and Y
- Simple background graphics
- Depth perception

**Code Written:**
- Background layer
- 2D parallax calculation
- Integration with main scroll

**What the Learner Sees:**
Distant stars/mountains scroll slowly - depth!

**Reference to Parallax Patrol:**
"Parallax Patrol's layers, now working in all directions."

---

### Unit 10: Parallax Layer - Midground

**Learning Objectives:**
- Middle parallax layer
- Medium scroll rate
- Enhanced depth

**Concepts Introduced:**
- Midground layer
- Intermediate scroll speed
- Layer coordination
- Three-layer parallax

**Code Written:**
- Midground layer
- Speed calculation
- Layer management

**What the Learner Sees:**
Three layers of parallax scrolling in any direction!

---

### Unit 11: Player Character - Standing and Running

**Learning Objectives:**
- Create player sprite
- Running animation
- Facing direction

**Concepts Introduced:**
- Player sprite design
- Run cycle animation
- Direction facing
- Sprite positioning in scrolling world

**Code Written:**
- Player sprite data
- Animation system
- Direction handling

**What the Learner Sees:**
Player character runs with smooth animation!

---

### Unit 12: Player Character - Jumping

**Learning Objectives:**
- Jump mechanics
- Variable jump height
- Gravity system

**Concepts Introduced:**
- Jump physics
- Variable height (hold for higher)
- Gravity constant
- Air control

**Code Written:**
- Jump implementation
- Variable height logic
- Gravity application

**What the Learner Sees:**
Responsive jumping with variable height!

**Reference to Platform Panic:**
"Platform Panic's jump physics, refined for action gameplay."

---

### Unit 13: Platform Collision

**Learning Objectives:**
- Collision with terrain
- One-way platforms
- Solid walls

**Concepts Introduced:**
- Tile-based collision
- One-way platform detection
- Wall stopping
- Collision response

**Code Written:**
- Collision detection
- Platform landing
- Wall collision

**What the Learner Sees:**
Player lands on platforms, stops at walls!

---

### Unit 14: Terrain Tiles

**Learning Objectives:**
- Create terrain tileset
- Visual variety
- Collision mapping

**Concepts Introduced:**
- Terrain tile design
- Collision flags per tile
- Visual variety
- Tileset organisation

**Code Written:**
- Terrain tileset
- Collision map
- Tile rendering

**What the Learner Sees:**
Beautiful terrain with varied tiles!

---

### Unit 15: Level Data Format

**Learning Objectives:**
- Design level format
- Efficient storage
- Streaming preparation

**Concepts Introduced:**
- Level data structure
- Tile indices
- Object placement
- Format efficiency

**Code Written:**
- Level format definition
- Level loading routine
- Format documentation

**What the Learner Sees:**
Level data system ready for content.

---

### Unit 16: Playable Foundation

**Learning Objectives:**
- Integrate all Phase 1 systems
- Basic playable level
- Foundation complete

**Concepts Introduced:**
- System integration
- Test level design
- Foundation verification
- Ready for expansion

**Code Written:**
- Full integration
- Test level
- Basic game loop

**What the Learner Sees:**
Run and jump through a scrolling world - foundation complete!

---

## Phase 2: Weapons and Combat (Units 17-32)
*Complete weapon system and basic enemies.*

### Unit 17: Basic Shooting

**Learning Objectives:**
- Fire button shoots
- Bullet in facing direction
- Bullet pool

**Concepts Introduced:**
- Basic weapon fire
- Bullet entity pool
- Direction-based fire
- Fire rate limiting

**Code Written:**
- Bullet system
- Fire handling
- Bullet movement

**What the Learner Sees:**
Press fire - bullets fly in facing direction!

---

### Unit 18: 8-Direction Aiming

**Learning Objectives:**
- Aim in 8 directions
- Lock position while aiming
- Visual feedback

**Concepts Introduced:**
- Directional aiming
- Aim lock (hold fire + direction)
- Aim indicator
- 8-direction coverage

**Code Written:**
- Aim direction detection
- Aim lock mechanic
- Visual indicator

**What the Learner Sees:**
Hold fire + direction to aim - shoot any direction!

---

### Unit 19: Weapon Framework

**Learning Objectives:**
- Multiple weapon types
- Weapon data structure
- Switching mechanism

**Concepts Introduced:**
- Weapon enumeration
- Weapon properties (damage, rate, pattern)
- Current weapon tracking
- Switch input

**Code Written:**
- Weapon system structure
- Property tables
- Switch handling

**What the Learner Sees:**
Framework for multiple weapons ready.

---

### Unit 20: Weapon - Spread Gun

**Learning Objectives:**
- Multi-direction spread shot
- Coverage vs focus trade-off
- Upgrade levels

**Concepts Introduced:**
- Spread pattern (3-way, 5-way, 7-way)
- Angle calculation
- Upgrade progression
- Strategic use

**Code Written:**
- Spread gun implementation
- Level variations
- Pattern generation

**What the Learner Sees:**
Spread gun fires in multiple directions!

---

### Unit 21: Weapon - Laser

**Learning Objectives:**
- Beam weapon
- Continuous fire
- High damage

**Concepts Introduced:**
- Beam rendering
- Sustained damage
- Resource cost (optional)
- Visual effect

**Code Written:**
- Laser beam rendering
- Damage application
- Visual effect

**What the Learner Sees:**
Laser cuts through enemies!

---

### Unit 22: Weapon - Bounce

**Learning Objectives:**
- Bouncing projectiles
- Ricochet physics
- Area coverage

**Concepts Introduced:**
- Bounce physics
- Surface reflection
- Bounce count limit
- Chaos weapon

**Code Written:**
- Bounce projectile
- Reflection logic
- Bounce counting

**What the Learner Sees:**
Bounce shots ricochet off walls!

---

### Unit 23: Weapon - Homing

**Learning Objectives:**
- Tracking missiles
- Target acquisition
- Limited fire rate

**Concepts Introduced:**
- Homing algorithm
- Target selection
- Turn rate limitation
- Smart weapon

**Code Written:**
- Homing missile
- Tracking logic
- Target priority

**What the Learner Sees:**
Homing missiles seek out enemies!

---

### Unit 24: Weapon - Lightning Whip

**Learning Objectives:**
- Rotating beam weapon
- 360° coverage
- Signature weapon

**Concepts Introduced:**
- Rotation control
- Beam at angle
- Continuous rotation
- Iconic Turrican weapon

**Code Written:**
- Rotation mechanic
- Beam at angle rendering
- Control system

**What the Learner Sees:**
Lightning whip rotates around player - iconic!

---

### Unit 25: Weapon Selection UI

**Learning Objectives:**
- Quick weapon switching
- Visual weapon indicator
- Intuitive selection

**Concepts Introduced:**
- Weapon selector input
- Current weapon display
- Quick switch
- Visual feedback

**Code Written:**
- Selection input
- Display rendering
- Switch handling

**What the Learner Sees:**
Cycle weapons quickly - indicator shows current!

---

### Unit 26: Weapon Upgrades

**Learning Objectives:**
- Power levels per weapon
- Upgrade collection
- Progressive power

**Concepts Introduced:**
- Per-weapon power levels
- Upgrade power-ups
- Visual power indicator
- Max power state

**Code Written:**
- Level tracking per weapon
- Upgrade handling
- Power display

**What the Learner Sees:**
Collect upgrades - weapons get stronger!

---

### Unit 27: Basic Enemy - Walker

**Learning Objectives:**
- Ground enemy type
- Patrol behaviour
- Combat target

**Concepts Introduced:**
- Enemy entity structure
- Patrol AI
- Collision target
- Health and death

**Code Written:**
- Walker enemy
- Patrol behaviour
- Death handling

**What the Learner Sees:**
Walker enemies patrol platforms!

---

### Unit 28: Basic Enemy - Flyer

**Learning Objectives:**
- Flying enemy type
- Aerial movement
- Different threat

**Concepts Introduced:**
- Flying enemy
- Sine wave or direct movement
- Aerial combat
- Threat variety

**Code Written:**
- Flyer enemy
- Movement pattern
- Combat handling

**What the Learner Sees:**
Flying enemies attack from the air!

---

### Unit 29: Basic Enemy - Shooter

**Learning Objectives:**
- Ranged enemy
- Enemy bullets
- Return fire threat

**Concepts Introduced:**
- Enemy shooting
- Enemy bullet pool
- Fire patterns
- Two-way combat

**Code Written:**
- Shooter enemy
- Enemy bullet system
- Fire timing

**What the Learner Sees:**
Enemies shoot back - dodge their fire!

---

### Unit 30: Enemy Spawning

**Learning Objectives:**
- Spawn enemies from level data
- Respawn rules
- Performance management

**Concepts Introduced:**
- Level-based spawning
- Off-screen spawning
- Respawn conditions
- Entity limits

**Code Written:**
- Spawn system
- Level integration
- Entity management

**What the Learner Sees:**
Enemies spawn as player explores!

---

### Unit 31: Player Health System

**Learning Objectives:**
- Health bar display
- Damage from enemies
- Death handling

**Concepts Introduced:**
- Health points
- Damage calculation
- Invulnerability frames
- Death sequence

**Code Written:**
- Health tracking
- Damage handling
- Death sequence

**What the Learner Sees:**
Health bar - take damage, die if depleted!

---

### Unit 32: Combat Polish

**Learning Objectives:**
- Hit effects
- Death effects
- Combat feel

**Concepts Introduced:**
- Hit feedback (flash, shake)
- Enemy explosions
- Sound effects
- Combat satisfaction

**Code Written:**
- Hit effects
- Explosion sprites
- Sound integration

**What the Learner Sees:**
Combat feels satisfying - hits have impact!

---

## Phase 3: Special Mechanics (Units 33-48)
*Grappling hook, wheel transform, advanced movement.*

### Unit 33: Grappling Hook - Concept

**Learning Objectives:**
- Understand grapple mechanic
- Plan implementation
- Design hook behaviour

**Concepts Introduced:**
- Grapple as traversal tool
- Attach points in level
- Swing physics concept
- Level design implications

**What the Learner Sees:**
Design for grappling hook mechanic.

---

### Unit 34: Grappling Hook - Firing

**Learning Objectives:**
- Fire grapple projectile
- Detect attach points
- Hook projectile physics

**Concepts Introduced:**
- Hook projectile
- Attach point tiles
- Attachment detection
- Fire angle

**Code Written:**
- Hook firing
- Attachment detection
- Projectile physics

**What the Learner Sees:**
Fire grapple - attaches to ceilings!

---

### Unit 35: Grappling Hook - Rope Rendering

**Learning Objectives:**
- Draw rope to attach point
- Rope visuals
- Dynamic line

**Concepts Introduced:**
- Line rendering
- Dynamic rope visual
- Sprite or character rope
- Visual connection

**Code Written:**
- Rope rendering
- Dynamic update
- Visual quality

**What the Learner Sees:**
Rope draws from player to attach point!

---

### Unit 36: Grappling Hook - Swinging

**Learning Objectives:**
- Pendulum physics
- Swing on rope
- Momentum transfer

**Concepts Introduced:**
- Pendulum physics
- Angular velocity
- Rope length
- Momentum on release

**Code Written:**
- Swing physics
- Player position on rope
- Release momentum

**What the Learner Sees:**
Swing on grapple - release with momentum!

---

### Unit 37: Grappling Hook - Polish

**Learning Objectives:**
- Rope length adjustment
- Sound effects
- Feel refinement

**Concepts Introduced:**
- Retract/extend rope
- Audio feedback
- Control refinement
- Level integration

**Code Written:**
- Length control
- Sound effects
- Polish details

**What the Learner Sees:**
Polished grappling hook - extend, retract, swing!

---

### Unit 38: Wheel Transform - Concept

**Learning Objectives:**
- Alternative player form
- Different physics
- Access new areas

**Concepts Introduced:**
- Transform mechanic
- Wheel form properties
- Tight space access
- Form-specific abilities

**What the Learner Sees:**
Design for wheel transformation.

---

### Unit 39: Wheel Transform - Implementation

**Learning Objectives:**
- Transform input
- Wheel sprite
- Different collision shape

**Concepts Introduced:**
- Transform trigger
- Sprite swap
- Collision shape change
- Form toggle

**Code Written:**
- Transform mechanic
- Sprite management
- Collision adjustment

**What the Learner Sees:**
Press button - transform to wheel!

---

### Unit 40: Wheel Physics

**Learning Objectives:**
- Wheel movement physics
- Roll and bounce
- Speed characteristics

**Concepts Introduced:**
- Roll physics
- Momentum preservation
- Bounce off walls
- Fast movement

**Code Written:**
- Wheel physics
- Roll mechanics
- Bounce handling

**What the Learner Sees:**
Wheel rolls fast, bounces off walls!

---

### Unit 41: Wheel Abilities

**Learning Objectives:**
- Wheel-specific actions
- Bomb dropping
- Tight space traversal

**Concepts Introduced:**
- Wheel bombs (drop mines)
- Tight tunnel access
- Speed boost
- Form advantages

**Code Written:**
- Wheel bombs
- Space detection
- Speed boost

**What the Learner Sees:**
Wheel drops bombs, accesses tight spaces!

---

### Unit 42: Smart Bomb

**Learning Objectives:**
- Screen-clear weapon
- Limited stock
- Emergency tool

**Concepts Introduced:**
- Smart bomb mechanic
- Stock tracking
- Clear effect
- Strategic use

**Code Written:**
- Smart bomb
- Stock system
- Clear effect

**What the Learner Sees:**
Smart bomb clears screen - limited stock!

---

### Unit 43: Shield Power-Up

**Learning Objectives:**
- Temporary protection
- Hit absorption
- Strategic collection

**Concepts Introduced:**
- Shield mechanic
- Hit absorption
- Duration or hits
- Visual indicator

**Code Written:**
- Shield system
- Absorption handling
- Display

**What the Learner Sees:**
Shield absorbs hits - temporary protection!

---

### Unit 44: Extra Life and 1-Ups

**Learning Objectives:**
- Extra life pickups
- Hidden 1-ups
- Reward exploration

**Concepts Introduced:**
- Extra life items
- Hidden placement
- Discovery reward
- Collection tracking

**Code Written:**
- Extra life handling
- Hidden item placement
- Collection feedback

**What the Learner Sees:**
Find hidden 1-ups - extra lives!

---

### Unit 45: Checkpoint System

**Learning Objectives:**
- Mid-level saves
- Respawn points
- Fair difficulty

**Concepts Introduced:**
- Checkpoint markers
- Respawn position
- State preservation
- Checkpoint activation

**Code Written:**
- Checkpoint system
- Respawn handling
- State save

**What the Learner Sees:**
Checkpoints save progress!

---

### Unit 46: Health Pickups

**Learning Objectives:**
- Health restoration
- Pickup placement
- Resource management

**Concepts Introduced:**
- Health items (small, large)
- Placement strategy
- Resource tension
- Visual distinction

**Code Written:**
- Health pickup handling
- Size variations
- Placement integration

**What the Learner Sees:**
Health pickups restore damage!

---

### Unit 47: Special Movement - Wall Slide

**Learning Objectives:**
- Slide down walls
- Wall jump potential
- Vertical mobility

**Concepts Introduced:**
- Wall detection
- Slide state
- Reduced fall speed
- Wall jump option

**Code Written:**
- Wall slide mechanic
- Wall detection
- Optional wall jump

**What the Learner Sees:**
Slide down walls for control!

---

### Unit 48: Movement Polish

**Learning Objectives:**
- Refine all movement
- Feel improvement
- Response tuning

**Concepts Introduced:**
- Movement feel refinement
- Response curves
- Animation polish
- Control satisfaction

**Code Written:**
- Tuning passes
- Animation refinement
- Feel polish

**What the Learner Sees:**
All movement feels responsive and satisfying!

---

## Phase 4: Exploration Systems (Units 49-64)
*Map, secrets, non-linear progression.*

### Unit 49: Level Design Philosophy

**Learning Objectives:**
- Non-linear level design
- Exploration encouragement
- Secret placement

**Concepts Introduced:**
- Metroidvania influences
- Multiple paths
- Gated progression
- Reward exploration

**What the Learner Sees:**
Understanding of exploration-focused design.

---

### Unit 50: Mini-Map Framework

**Learning Objectives:**
- Map data structure
- Revealed areas tracking
- Display system

**Concepts Introduced:**
- Map data per room/sector
- Fog of war
- Current position marker
- Map display toggle

**Code Written:**
- Map data structure
- Reveal tracking
- Basic display

**What the Learner Sees:**
Map framework ready.

---

### Unit 51: Mini-Map Display

**Learning Objectives:**
- Visual map rendering
- Room/sector shapes
- Player position

**Concepts Introduced:**
- Map rendering
- Sector visual representation
- Position indicator
- Pause screen integration

**Code Written:**
- Map rendering
- Sector display
- Position marker

**What the Learner Sees:**
Pause shows map of explored areas!

---

### Unit 52: Secret Areas

**Learning Objectives:**
- Hidden room design
- Discovery mechanics
- Reward placement

**Concepts Introduced:**
- Hidden passages
- Destructible walls
- Secret indicators (subtle)
- Reward contents

**Code Written:**
- Hidden room handling
- Wall destruction
- Secret tracking

**What the Learner Sees:**
Hidden areas with valuable rewards!

---

### Unit 53: Collectible System

**Learning Objectives:**
- Trackable collectibles
- Completion percentage
- Long-term goals

**Concepts Introduced:**
- Collectible items
- Tracking per level
- Percentage display
- Completionist reward

**Code Written:**
- Collectible tracking
- Persistence
- Percentage calculation

**What the Learner Sees:**
Collectibles tracked - aim for 100%!

---

### Unit 54: Key Items

**Learning Objectives:**
- Items that unlock areas
- Gated progression
- Item-based puzzles

**Concepts Introduced:**
- Key item concept
- Lock and key design
- Item persistence
- Progression gating

**Code Written:**
- Key item handling
- Lock detection
- Gate opening

**What the Learner Sees:**
Find keys to unlock new areas!

**Reference to Dungeon Crawl:**
"Key/lock mechanics from Dungeon Crawl in action context."

---

### Unit 55: Level Streaming

**Learning Objectives:**
- Load level data during play
- Seamless large levels
- Memory management

**Concepts Introduced:**
- Level streaming
- Load-ahead buffering
- Seamless transitions
- Memory efficiency

**Code Written:**
- Streaming system
- Buffer management
- Seamless loading

**What the Learner Sees:**
Huge levels load seamlessly!

**Reference to Night Raid:**
"Night Raid's streaming for even larger levels."

---

### Unit 56: Level Compression

**Learning Objectives:**
- Compress level data
- More content in memory
- RLE and dictionary

**Concepts Introduced:**
- Level data compression
- RLE for terrain
- Decompression routine
- Space efficiency

**Code Written:**
- Compression format
- Decompression
- Integration

**What the Learner Sees:**
(Internal - more levels possible.)

---

### Unit 57: Stage 1 Design

**Learning Objectives:**
- Complete first stage
- Tutorial through design
- Introduce mechanics

**Concepts Introduced:**
- Stage design principles
- Gradual introduction
- Challenge curve
- Stage theme

**Code Written:**
- Stage 1 complete level data
- Enemy placement
- Secret placement

**What the Learner Sees:**
Stage 1: Forest - introduction to all mechanics!

---

### Unit 58: Stage 2 Design

**Learning Objectives:**
- Second stage content
- New challenges
- Theme variation

**Concepts Introduced:**
- Theme variation
- New enemy combinations
- Increased challenge
- Grapple focus areas

**Code Written:**
- Stage 2 level data
- Theme graphics
- Enemy configuration

**What the Learner Sees:**
Stage 2: Caves - grappling hook challenges!

---

### Unit 59: Stage 3 Design

**Learning Objectives:**
- Third stage content
- Mid-game challenge
- Wheel focus

**Concepts Introduced:**
- Mid-game difficulty
- Wheel transform areas
- Complex layouts
- Vertical emphasis

**Code Written:**
- Stage 3 level data
- Wheel areas
- Vertical sections

**What the Learner Sees:**
Stage 3: Factory - wheel transformation puzzles!

---

### Unit 60: Stage 4 Design

**Learning Objectives:**
- Fourth stage content
- High challenge
- Combined mechanics

**Concepts Introduced:**
- High difficulty
- All mechanics required
- Complex enemy combinations
- Pre-finale intensity

**Code Written:**
- Stage 4 level data
- Enemy combinations
- Challenge tuning

**What the Learner Sees:**
Stage 4: Sky Fortress - all skills tested!

---

### Unit 61: Stage 5 Design

**Learning Objectives:**
- Final stage content
- Ultimate challenge
- Lead to final boss

**Concepts Introduced:**
- Final stage design
- Maximum challenge
- Boss approach
- Climax building

**Code Written:**
- Stage 5 level data
- Final approach
- Intensity building

**What the Learner Sees:**
Stage 5: Enemy Base - final approach!

---

### Unit 62: Stage Transitions

**Learning Objectives:**
- Between-stage handling
- Score tally
- Breather moments

**Concepts Introduced:**
- Stage clear handling
- Score/stats display
- Brief celebration
- Next stage loading

**Code Written:**
- Transition screens
- Stats display
- Loading handling

**What the Learner Sees:**
Stage clear! Stats shown, brief celebration, next stage loads.

---

### Unit 63: Difficulty Scaling

**Learning Objectives:**
- Per-stage difficulty
- Enemy parameters
- Fair challenge curve

**Concepts Introduced:**
- Difficulty progression
- Enemy health/damage scaling
- Spawn rate adjustment
- Balance

**Code Written:**
- Difficulty parameters
- Per-stage tuning
- Balance adjustment

**What the Learner Sees:**
Challenge increases appropriately through game.

---

### Unit 64: Exploration Polish

**Learning Objectives:**
- Refine exploration feel
- Map polish
- Secret balancing

**Concepts Introduced:**
- Exploration refinement
- Map improvements
- Secret visibility tuning
- Reward balancing

**Code Written:**
- Polish passes
- Map improvements
- Balance adjustments

**What the Learner Sees:**
Exploration feels rewarding and well-paced!

---

## Phase 5: Boss Battles (Units 65-80)
*Epic multi-sprite bosses.*

### Unit 65: Boss Framework

**Learning Objectives:**
- Boss encounter structure
- Health bar display
- Phase system

**Concepts Introduced:**
- Boss data structure
- Large health pools
- Phase transitions
- Health bar rendering

**Code Written:**
- Boss framework
- Health display
- Phase handling

**What the Learner Sees:**
Boss framework ready for epic encounters!

---

### Unit 66: Multi-Sprite Boss Rendering

**Learning Objectives:**
- Large bosses from multiple sprites
- Coordinated movement
- Hitbox management

**Concepts Introduced:**
- Composite sprite boss
- Part coordination
- Per-part collision
- Visual coherence

**Code Written:**
- Multi-sprite boss rendering
- Part management
- Collision handling

**What the Learner Sees:**
Large bosses composed of multiple sprites!

**Reference to Sprite Storm:**
"Multiplexing mastery enables huge bosses."

---

### Unit 67: Boss Attack Patterns

**Learning Objectives:**
- Design attack patterns
- Pattern cycling
- Learnable behaviour

**Concepts Introduced:**
- Attack pattern data
- Pattern sequencing
- Telegraph signals
- Fair but challenging

**Code Written:**
- Pattern system
- Attack execution
- Telegraph system

**What the Learner Sees:**
Bosses have learnable attack patterns!

---

### Unit 68: Boss 1 - Ground Assault

**Learning Objectives:**
- First boss implementation
- Ground-based boss
- Introduction difficulty

**Concepts Introduced:**
- Ground boss design
- Simple patterns
- Weak point concept
- First boss victory

**Code Written:**
- Boss 1 complete
- Attack patterns
- Defeat sequence

**What the Learner Sees:**
Boss 1: Ground Assault Tank! First boss challenge.

---

### Unit 69: Boss 2 - Aerial Hunter

**Learning Objectives:**
- Flying boss
- Aerial combat
- Increased challenge

**Concepts Introduced:**
- Flying boss design
- Movement patterns
- Missile attacks
- Mid-game difficulty

**Code Written:**
- Boss 2 complete
- Flight patterns
- Attack types

**What the Learner Sees:**
Boss 2: Aerial Hunter! Flying boss challenge.

---

### Unit 70: Boss 3 - Giant Mech

**Learning Objectives:**
- Large multi-part boss
- Multiple weak points
- Complex patterns

**Concepts Introduced:**
- Multi-part boss
- Destroy parts strategy
- Complex patterns
- Visual spectacle

**Code Written:**
- Boss 3 with parts
- Part destruction
- Pattern complexity

**What the Learner Sees:**
Boss 3: Giant Mech! Multiple parts to destroy!

---

### Unit 71: Boss 4 - Shape Shifter

**Learning Objectives:**
- Phase-changing boss
- Form changes
- Pattern variety

**Concepts Introduced:**
- Form-changing boss
- Different phases
- Adaptation required
- Challenging variety

**Code Written:**
- Boss 4 with forms
- Phase transitions
- Per-form patterns

**What the Learner Sees:**
Boss 4: Shape Shifter! Changes form mid-fight!

---

### Unit 72: Final Boss - Design

**Learning Objectives:**
- Design ultimate boss
- Multi-phase epic
- Climactic encounter

**Concepts Introduced:**
- Final boss design
- Three-phase structure
- Ultimate challenge
- Narrative climax

**What the Learner Sees:**
Final boss design complete.

---

### Unit 73: Final Boss - Phase 1

**Learning Objectives:**
- First phase implementation
- Opening patterns
- Phase transition

**Concepts Introduced:**
- Opening phase
- Introduction patterns
- Transition trigger
- Building intensity

**Code Written:**
- Phase 1 complete
- Opening patterns
- Transition

**What the Learner Sees:**
Final boss Phase 1 working!

---

### Unit 74: Final Boss - Phase 2

**Learning Objectives:**
- Second phase
- Escalated patterns
- Increased intensity

**Concepts Introduced:**
- Escalation phase
- Harder patterns
- Environmental effects
- Rising tension

**Code Written:**
- Phase 2 complete
- Escalated patterns
- Effects

**What the Learner Sees:**
Phase 2 intensifies the battle!

---

### Unit 75: Final Boss - Phase 3

**Learning Objectives:**
- Final phase
- Ultimate patterns
- Victory sequence

**Concepts Introduced:**
- Desperate phase
- Ultimate attacks
- Victory trigger
- Climax resolution

**Code Written:**
- Phase 3 complete
- Ultimate patterns
- Victory handling

**What the Learner Sees:**
Final phase - defeat for ultimate victory!

---

### Unit 76: Boss Sound Design

**Learning Objectives:**
- Boss-specific audio
- Impact sounds
- Music integration

**Concepts Introduced:**
- Boss sound palette
- Attack sounds
- Impact feedback
- Boss music

**Code Written:**
- Boss sounds
- Music integration
- Audio mix

**What the Learner Sees:**
Bosses sound powerful and impactful!

---

### Unit 77: Boss Visual Effects

**Learning Objectives:**
- Boss-specific effects
- Explosions
- Impact feedback

**Concepts Introduced:**
- Boss explosions
- Hit effects
- Screen effects
- Visual drama

**Code Written:**
- Boss effects
- Explosions
- Screen shake

**What the Learner Sees:**
Boss battles look spectacular!

---

### Unit 78: Boss Music

**Learning Objectives:**
- Per-boss music
- Intensity matching
- Epic themes

**Concepts Introduced:**
- Boss themes
- Intensity progression
- Final boss theme
- Victory music

**Code Written:**
- Boss music tracks
- Trigger handling
- Victory transition

**What the Learner Sees:**
Epic boss music for each encounter!

---

### Unit 79: Boss Balance

**Learning Objectives:**
- Fair boss difficulty
- Pattern balance
- Health tuning

**Concepts Introduced:**
- Boss balance testing
- Difficulty adjustment
- Pattern fairness
- Health values

**Code Written:**
- Balance adjustments
- Testing
- Verification

**What the Learner Sees:**
Bosses are challenging but fair!

---

### Unit 80: Boss Polish

**Learning Objectives:**
- Final boss refinement
- Feel improvement
- Complete boss system

**Concepts Introduced:**
- Boss polish
- Animation refinement
- Feel improvement
- Complete system

**Code Written:**
- Polish passes
- Refinements
- Final touches

**What the Learner Sees:**
All bosses polished and epic!

---

## Phase 6: Audio and Effects (Units 81-96)
*Complete audio and visual polish.*

### Unit 81: Stage Music Composition

**Learning Objectives:**
- Music for each stage
- Theme consistency
- Energy matching

**Concepts Introduced:**
- Stage music design
- Theme development
- Energy levels
- SID composition

**Code Written:**
- 5 stage music tracks
- Music system integration

**What the Learner Sees:**
Each stage has unique music!

**Reference to SID Symphony:**
"Full SID Symphony skills for rich stage music."

---

### Unit 82: Music System

**Learning Objectives:**
- Music playback system
- Track switching
- Seamless looping

**Concepts Introduced:**
- Music player
- Track management
- Loop points
- Transition handling

**Code Written:**
- Music system
- Track switching
- Loop handling

**What the Learner Sees:**
Music plays seamlessly throughout!

---

### Unit 83: Sound Effect Design

**Learning Objectives:**
- Complete SFX palette
- Per-action sounds
- Audio feedback

**Concepts Introduced:**
- SFX categories
- Weapon sounds
- Enemy sounds
- UI sounds

**Code Written:**
- Complete SFX set
- Trigger system
- Priority handling

**What the Learner Sees:**
Every action has satisfying sound!

---

### Unit 84: Audio Mixing

**Learning Objectives:**
- Balance music and SFX
- Voice allocation
- Clean mix

**Concepts Introduced:**
- Audio mixing
- Voice priority
- Balance tuning
- Clean audio

**Code Written:**
- Mix settings
- Priority system
- Balance adjustment

**What the Learner Sees:**
Audio perfectly balanced!

---

### Unit 85: Hit Effects System

**Learning Objectives:**
- Comprehensive hit effects
- Feedback variety
- Visual satisfaction

**Concepts Introduced:**
- Hit effect types
- Spark variations
- Flash effects
- Feedback layers

**Code Written:**
- Hit effect system
- Variation handling
- Integration

**What the Learner Sees:**
Hits look and feel impactful!

---

### Unit 86: Explosion Effects

**Learning Objectives:**
- Varied explosions
- Size by enemy
- Visual spectacle

**Concepts Introduced:**
- Explosion sizes
- Enemy-appropriate scaling
- Particle effects
- Chain explosions

**Code Written:**
- Explosion system
- Size variants
- Particles

**What the Learner Sees:**
Satisfying explosions everywhere!

---

### Unit 87: Screen Effects

**Learning Objectives:**
- Screen-wide effects
- Shake, flash, fade
- Drama enhancement

**Concepts Introduced:**
- Screen shake
- Flash effects
- Fade transitions
- Drama tools

**Code Written:**
- Screen effect system
- Trigger integration
- Smooth effects

**What the Learner Sees:**
Screen effects enhance dramatic moments!

---

### Unit 88: Particle System

**Learning Objectives:**
- Particle effects
- Environmental particles
- Visual richness

**Concepts Introduced:**
- Particle spawning
- Particle physics
- Effect variety
- Performance management

**Code Written:**
- Particle system
- Effect library
- Management

**What the Learner Sees:**
Particles add visual richness!

---

### Unit 89: Environmental Animation

**Learning Objectives:**
- Animated level elements
- Water, lava, machinery
- Living world feel

**Concepts Introduced:**
- Tile animation
- Water effects
- Machinery movement
- Atmosphere

**Code Written:**
- Animated tiles
- Effect cycles
- Integration

**What the Learner Sees:**
Levels feel alive with animation!

---

### Unit 90: Weather Effects

**Learning Objectives:**
- Rain, snow effects
- Stage atmosphere
- Performance-safe

**Concepts Introduced:**
- Weather particles
- Stage-appropriate weather
- Performance management
- Atmosphere enhancement

**Code Written:**
- Weather system
- Stage integration
- Performance tuning

**What the Learner Sees:**
Weather effects add atmosphere!

---

### Unit 91: Lighting Effects

**Learning Objectives:**
- Flicker, glow effects
- Torches, machinery
- Visual interest

**Concepts Introduced:**
- Colour cycling
- Flicker effects
- Glow simulation
- Light sources

**Code Written:**
- Lighting effects
- Colour cycling
- Integration

**What the Learner Sees:**
Lighting effects enhance visuals!

---

### Unit 92: UI Sound Effects

**Learning Objectives:**
- Menu sounds
- Feedback sounds
- UI feel

**Concepts Introduced:**
- UI sound palette
- Cursor sounds
- Selection sounds
- Feedback importance

**Code Written:**
- UI sounds
- Integration
- Polish

**What the Learner Sees:**
UI sounds complete the experience!

---

### Unit 93: Demo-Scene Polish - FLD

**Learning Objectives:**
- FLD effect for logos
- Title screen enhancement
- Demo-scene technique

**Concepts Introduced:**
- FLD (Flexible Line Distance)
- Logo rendering
- Raster trick
- Visual impact

**Code Written:**
- FLD implementation
- Title integration
- Effect polish

**What the Learner Sees:**
Demo-scene quality title effects!

---

### Unit 94: Demo-Scene Polish - Raster Bars

**Learning Objectives:**
- Raster bar effects
- Visual polish
- Technical showcase

**Concepts Introduced:**
- Raster bars
- Colour cycling
- Integration opportunities
- Technical flair

**Code Written:**
- Raster bar effects
- Integration points
- Polish

**What the Learner Sees:**
Raster bar effects add flair!

---

### Unit 95: Visual Polish Pass

**Learning Objectives:**
- Complete visual review
- Consistency check
- Final polish

**Concepts Introduced:**
- Visual consistency
- Style coherence
- Detail polish
- Professional look

**Code Written:**
- Visual fixes
- Consistency improvements
- Final details

**What the Learner Sees:**
Everything looks polished and consistent!

---

### Unit 96: Audio Polish Pass

**Learning Objectives:**
- Complete audio review
- Mix finalization
- Audio excellence

**Concepts Introduced:**
- Audio review process
- Final balancing
- Quality verification
- Excellence standard

**Code Written:**
- Audio fixes
- Final mix
- Quality check

**What the Learner Sees:**
Audio is excellent throughout!

---

## Phase 7: Presentation (Units 97-112)
*Title, menus, game flow.*

### Unit 97: Title Screen Design

**Learning Objectives:**
- Professional title screen
- Visual impact
- Mode selection

**Concepts Introduced:**
- Title design
- Logo presentation
- Menu system
- Professional appearance

**Code Written:**
- Title screen
- Logo display
- Menu basics

**What the Learner Sees:**
Impressive title screen!

---

### Unit 98: Title Animation

**Learning Objectives:**
- Animated title elements
- Demo-scene polish
- Attract mode

**Concepts Introduced:**
- Title animation
- Effect integration
- Attract loop
- Visual interest

**Code Written:**
- Title animations
- Effects
- Loop timing

**What the Learner Sees:**
Animated title with demo effects!

---

### Unit 99: Demo Mode

**Learning Objectives:**
- Attract mode gameplay
- Auto-play demonstration
- Idle showcase

**Concepts Introduced:**
- Input recording/playback
- Demo loop
- Return to title
- Attract function

**Code Written:**
- Demo system
- Playback
- Loop handling

**What the Learner Sees:**
Leave title - game plays itself!

---

### Unit 100: Options Menu

**Learning Objectives:**
- Configuration options
- Difficulty settings
- Audio settings

**Concepts Introduced:**
- Options menu
- Setting persistence
- Player configuration
- Accessibility

**Code Written:**
- Options menu
- Settings handling
- Persistence

**What the Learner Sees:**
Options for difficulty, audio, controls!

---

### Unit 101: High Score System

**Learning Objectives:**
- Score tracking
- Leaderboard
- Name entry

**Concepts Introduced:**
- High score table
- Entry system
- Persistence
- Competition

**Code Written:**
- High score system
- Entry screen
- Save/load

**What the Learner Sees:**
High scores saved - compete!

---

### Unit 102: Statistics System

**Learning Objectives:**
- Track gameplay stats
- Lifetime records
- Achievement data

**Concepts Introduced:**
- Statistics tracking
- Display formatting
- Persistence
- Progress visualization

**Code Written:**
- Stats system
- Display
- Persistence

**What the Learner Sees:**
Statistics track your play history!

---

### Unit 103: HUD Design

**Learning Objectives:**
- In-game HUD
- Clear information
- Minimal intrusion

**Concepts Introduced:**
- HUD layout
- Information hierarchy
- Update efficiency
- Visual design

**Code Written:**
- HUD rendering
- Update system
- Polish

**What the Learner Sees:**
Clean, informative HUD!

---

### Unit 104: Pause Menu

**Learning Objectives:**
- Pause functionality
- Map access
- Options access

**Concepts Introduced:**
- Pause system
- Menu in pause
- Resume handling
- Quick access

**Code Written:**
- Pause handling
- Pause menu
- Map integration

**What the Learner Sees:**
Pause accesses map, options!

---

### Unit 105: Game Over Screen

**Learning Objectives:**
- Game over handling
- Stats display
- Continue/retry

**Concepts Introduced:**
- Game over flow
- Final stats
- Options presentation
- Flow handling

**Code Written:**
- Game over screen
- Stats display
- Flow options

**What the Learner Sees:**
Game over shows stats, options!

---

### Unit 106: Victory Screen

**Learning Objectives:**
- Game completion
- Victory celebration
- Stats summary

**Concepts Introduced:**
- Victory detection
- Celebration effect
- Stats summary
- Achievement unlock

**Code Written:**
- Victory sequence
- Stats display
- Unlock handling

**What the Learner Sees:**
Victory! Celebration and final stats!

---

### Unit 107: Credits Sequence

**Learning Objectives:**
- Credits roll
- Development acknowledgment
- Professional closing

**Concepts Introduced:**
- Credits design
- Scroll or pages
- Music selection
- Professional feel

**Code Written:**
- Credits display
- Scroll handling
- Music integration

**What the Learner Sees:**
Professional credits sequence!

---

### Unit 108: Ending Sequence

**Learning Objectives:**
- Story conclusion
- Visual ending
- Emotional closure

**Concepts Introduced:**
- Ending narrative
- Visual presentation
- Music selection
- Satisfaction

**Code Written:**
- Ending display
- Story presentation
- Music

**What the Learner Sees:**
Satisfying story ending!

---

### Unit 109: Flow Polish

**Learning Objectives:**
- Smooth game flow
- Transition polish
- Complete experience

**Concepts Introduced:**
- Flow review
- Transition smoothness
- Loading handling
- Complete arc

**Code Written:**
- Flow polish
- Transition fixes
- Loading screens

**What the Learner Sees:**
Smooth flow throughout!

---

### Unit 110: Loading Screens

**Learning Objectives:**
- Loading presentation
- Wait time use
- Tips display

**Concepts Introduced:**
- Loading screen design
- Progress indication
- Tips/hints
- Wait disguise

**Code Written:**
- Loading screens
- Progress display
- Tips system

**What the Learner Sees:**
Loading screens with tips!

---

### Unit 111: Intro Sequence

**Learning Objectives:**
- Story setup
- Opening narrative
- Mood setting

**Concepts Introduced:**
- Intro design
- Story presentation
- Skip option
- Mood establishment

**Code Written:**
- Intro sequence
- Story display
- Skip handling

**What the Learner Sees:**
Story intro sets the scene!

---

### Unit 112: Presentation Polish

**Learning Objectives:**
- Complete presentation review
- Final polish
- Professional quality

**Concepts Introduced:**
- Presentation review
- Polish pass
- Quality standard
- Complete package

**Code Written:**
- Final polish
- Fixes
- Verification

**What the Learner Sees:**
Professional presentation throughout!

---

## Phase 8: Mastery (Units 113-128)
*Optimization, extras, release.*

### Unit 113: Performance Profiling

**Learning Objectives:**
- Identify bottlenecks
- Measure frame budget
- Target optimization

**Concepts Introduced:**
- Performance profiling
- Timing measurement
- Bottleneck identification
- Optimization targets

**Code Written:**
- Profiling tools
- Measurement
- Documentation

**What the Learner Sees:**
Understanding of performance profile.

---

### Unit 114: Scroll Optimization

**Learning Objectives:**
- Optimize scroll system
- Maximum efficiency
- Stable performance

**Concepts Introduced:**
- Scroll optimization
- Cache optimization
- Self-modifying code
- Efficiency

**Code Written:**
- Scroll optimization
- Efficiency improvements
- Verification

**What the Learner Sees:**
(Rock-solid scroll performance.)

---

### Unit 115: Sprite Optimization

**Learning Objectives:**
- Optimize multiplexer
- Maximum capacity
- Minimal flicker

**Concepts Introduced:**
- Multiplexer optimization
- Sorting efficiency
- IRQ optimization
- Maximum sprites

**Code Written:**
- Multiplexer optimization
- Efficiency improvements

**What the Learner Sees:**
(Maximum sprites, minimal flicker.)

**Reference to Sprite Storm:**
"Applying all Sprite Storm optimizations."

---

### Unit 116: Memory Optimization

**Learning Objectives:**
- Efficient memory use
- Data compression
- Maximum content

**Concepts Introduced:**
- Memory review
- Compression improvements
- Efficient structures
- Content capacity

**Code Written:**
- Memory optimization
- Compression
- Layout refinement

**What the Learner Sees:**
(Maximum content in memory.)

---

### Unit 117: Two-Player Mode

**Learning Objectives:**
- Cooperative play
- Two-player handling
- Shared experience

**Concepts Introduced:**
- Two-player input
- Screen sharing
- Cooperative design
- Balance for two

**Code Written:**
- Two-player support
- Shared screen
- Balance

**What the Learner Sees:**
Two-player co-op mode!

---

### Unit 118: Time Attack Mode

**Learning Objectives:**
- Speedrun mode
- Timer system
- Best times

**Concepts Introduced:**
- Time attack design
- Per-stage times
- Leaderboards
- Speedrun support

**Code Written:**
- Time attack mode
- Timer system
- Records

**What the Learner Sees:**
Time attack for speedrunners!

---

### Unit 119: Boss Rush Mode

**Learning Objectives:**
- Boss-only mode
- Challenge variant
- Replayability

**Concepts Introduced:**
- Boss rush design
- Sequential bosses
- Scoring
- Challenge mode

**Code Written:**
- Boss rush mode
- Sequential handling
- Scoring

**What the Learner Sees:**
Boss rush mode!

---

### Unit 120: New Game Plus

**Learning Objectives:**
- Replay with bonuses
- Increased challenge
- Extended life

**Concepts Introduced:**
- NG+ design
- Carryover rules
- Difficulty increase
- Replay value

**Code Written:**
- NG+ system
- Carryover
- Difficulty scaling

**What the Learner Sees:**
New Game Plus for replay!

---

### Unit 121: Achievements

**Learning Objectives:**
- Achievement system
- Optional goals
- Long-term engagement

**Concepts Introduced:**
- Achievement design
- Trigger detection
- Display
- Persistence

**Code Written:**
- Achievement system
- Triggers
- Display

**What the Learner Sees:**
Achievements to earn!

---

### Unit 122: Gallery/Sound Test

**Learning Objectives:**
- Unlockable content
- Fan service
- Collection reward

**Concepts Introduced:**
- Gallery design
- Sound test
- Unlock system
- Bonus content

**Code Written:**
- Gallery mode
- Sound test
- Unlock handling

**What the Learner Sees:**
Gallery and sound test unlocked!

---

### Unit 123: Bug Hunting

**Learning Objectives:**
- Systematic testing
- Bug finding and fixing
- Quality assurance

**Concepts Introduced:**
- Testing methodology
- Bug tracking
- Fix verification
- Quality standard

**Code Written:**
- Bug fixes
- Edge cases
- Verification

**What the Learner Sees:**
(Stable, bug-free game.)

---

### Unit 124: Balance Testing

**Learning Objectives:**
- Difficulty balance
- Fair challenge
- Player experience

**Concepts Introduced:**
- Balance testing
- Difficulty tuning
- Fairness verification
- Experience optimization

**Code Written:**
- Balance adjustments
- Tuning
- Verification

**What the Learner Sees:**
(Fair, balanced challenge.)

---

### Unit 125: Accessibility Options

**Learning Objectives:**
- Accessibility features
- Player accommodation
- Inclusive design

**Concepts Introduced:**
- Accessibility options
- Control options
- Visual options
- Inclusive design

**Code Written:**
- Accessibility options
- Implementation
- Testing

**What the Learner Sees:**
Accessibility options for all players!

---

### Unit 126: Documentation

**Learning Objectives:**
- Technical documentation
- Code comments
- Reference material

**Concepts Introduced:**
- Documentation practices
- Code documentation
- Reference creation
- Knowledge preservation

**Code Written:**
- Documentation
- Comments
- Reference guide

**What the Learner Sees:**
Complete technical documentation!

---

### Unit 127: Final Testing

**Learning Objectives:**
- Complete playthrough
- Quality verification
- Release readiness

**Concepts Introduced:**
- Final testing process
- Quality checklist
- Release criteria
- Sign-off

**Code Written:**
- Final fixes
- Quality verification
- Release preparation

**What the Learner Sees:**
(Release-ready quality.)

---

### Unit 128: Release Build

**Learning Objectives:**
- Create final release
- Distribution preparation
- Professional package

**Concepts Introduced:**
- Release build process
- Debug removal
- Distribution format
- Professional release

**Code Written:**
- Release build
- Debug removal
- Final package

**What the Learner Sees:**
Complete Mega Blaster - Turrican-class quality!

---

## Summary

**Mega Blaster** at 128 units delivers Turrican-class quality:

**Phases 1-2:** Core engine - multi-directional scrolling, weapons, combat
**Phases 3-4:** Special mechanics - grapple, transform, exploration
**Phases 5-6:** Content - 5 stages, epic bosses, audio/visual polish
**Phases 7-8:** Presentation and mastery - complete package

### Skills Mastered

Mega Blaster integrates nearly all curriculum skills:
- Multi-directional parallax scrolling
- Complete weapon systems
- Platforming and combat
- Large level exploration
- Epic multi-sprite bosses
- Demo-scene visual polish
- Professional presentation

### Ready for Symphony's End

After completing Mega Blaster, learners have the integration skills needed for the 256-unit capstone.

### Game Specifications

- **Scrolling:** Multi-directional with 3-layer parallax
- **Weapons:** 5 types with upgrade levels + lightning whip
- **Mechanics:** Grappling hook, wheel transform, wall slide
- **Stages:** 5 complete stages with exploration
- **Bosses:** 5 stage bosses + final boss
- **Collectibles:** Secrets, 1-ups, completion tracking
- **Players:** 1-2 cooperative
- **Modes:** Story, Time Attack, Boss Rush, New Game+
- **Features:** Map, checkpoints, achievements, gallery
