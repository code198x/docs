# Night Raid: 64-Unit Outline

**Game:** 8 of 16
**Platform:** Commodore 64
**Units:** 64
**Concept:** Scramble-style side-scroller. Fly through terrain, shoot enemies, bomb ground targets, manage fuel.

---

## Skills Applied from Previous Games

| Skill | Learned In | Application in Night Raid |
|-------|-----------|---------------------------|
| SID fundamentals | SID Symphony | Engine sound, explosions, music |
| Hardware sprites | Starfield | Player ship, enemies, bullets |
| Joystick input | Starfield | Flight control |
| Shooting mechanics | Starfield | Forward laser |
| Sprite collision | Starfield | All combat collision |
| Score display | Starfield | Score and fuel display |
| Tile-based maps | Maze Raider | Terrain design |
| Tile collision | Maze Raider | Terrain collision |
| Gravity simulation | Platform Panic | Bomb drop physics |
| Animation frames | Platform Panic | Ship tilt, explosions |
| Grid destruction | Brick Basher | Destructible ground targets |
| Speed ramping | Brick Basher | Difficulty progression |
| Wave progression | Invader Wave | Stage progression |
| Hardware scrolling | Scroll Runner | Terrain scrolling |
| Colour RAM scrolling | Scroll Runner | Coloured terrain |
| Double buffering | Scroll Runner | Smooth updates |
| Raster splits | Scroll Runner | Visual zones |
| Procedural elements | Scroll Runner | Terrain variety |

## New Skills Introduced

| Skill | Units | Description |
|-------|-------|-------------|
| Terrain collision | 9-12 | Ship collision with scrolling walls |
| Bombing mechanic | 13-16 | Gravity-affected ground attack |
| Resource management | 17-20 | Fuel system with depletion |
| Ground targets | 21-24 | Destructible fuel tanks and bases |
| Vertical terrain variation | 25-28 | Cave systems, narrow passages |
| Level streaming | 33-36 | Loading level data during play |
| Designed levels | 37-40 | Hand-crafted vs procedural |
| Boss encounters | 49-52 | End-of-stage bosses |

---

## Phase 1: Foundation (Units 1-16)
*Core mechanics: scrolling terrain, flight, shooting, and a playable game.*

### Unit 1: Scramble Analysis

**Learning Objectives:**
- Understand Scramble-style games
- Analyse gameplay elements
- Plan game structure

**Concepts Introduced:**
- Scramble (Konami 1981) as template
- Horizontal scroll shooter
- Terrain navigation
- Dual weapons (laser + bomb)
- Resource management (fuel)

**Code Written:**
- Design document
- Gameplay element list
- Stage structure plan
- Control scheme design

**What the Learner Sees:**
Understanding of the game we're building - Scramble's mechanics analysed and documented.

---

### Unit 2: Terrain Scrolling Setup

**Learning Objectives:**
- Apply Scroll Runner techniques
- Set up terrain display
- Establish scroll framework

**Concepts Introduced:**
- Scroll Runner skills applied
- Terrain as ceiling and floor
- Scrolling infrastructure
- VIC-II register setup

**Code Written:**
- Screen setup for terrain game
- Scroll register handling
- Screen shift routine
- Basic terrain characters

**What the Learner Sees:**
Scrolling terrain framework - empty space with ground below and ceiling above.

**Reference to Scroll Runner:**
"Direct application of Scroll Runner's scrolling techniques - we're building on that foundation."

---

### Unit 3: Terrain Data Format

**Learning Objectives:**
- Design terrain data structure
- Define ceiling and floor heights
- Create level data format

**Concepts Introduced:**
- Per-column terrain data
- Ceiling height per column
- Floor height per column
- Terrain character mapping

**Code Written:**
- Terrain data structure
- Column format (ceiling, floor, objects)
- Sample terrain data
- Data-to-screen conversion

**What the Learner Sees:**
(Data format ready - terrain will appear next unit.)

---

### Unit 4: Terrain Rendering

**Learning Objectives:**
- Draw terrain from data
- Fill ceiling and floor
- Create cave appearance

**Concepts Introduced:**
- Ceiling fill (top down)
- Floor fill (bottom up)
- Sky/cave between
- Terrain characters

**Code Written:**
- Column rendering routine
- Ceiling fill logic
- Floor fill logic
- Integration with scroll

**What the Learner Sees:**
Scrolling terrain! Rocky ceiling above, ground below, flyable space between.

---

### Unit 5: Terrain Character Set

**Learning Objectives:**
- Design terrain graphics
- Create rock/ground characters
- Visual variety

**Concepts Introduced:**
- Terrain character types
- Edge characters (smooth edges)
- Fill characters (solid rock)
- Colour choices

**Code Written:**
- Custom terrain characters
- Edge character set
- Fill characters
- Colour definitions

**What the Learner Sees:**
Beautiful terrain with smooth edges and solid fill - looks like a cave system!

---

### Unit 6: The Player Ship

**Learning Objectives:**
- Create player ship sprite
- Full 8-direction movement
- Position on left side of screen

**Concepts Introduced:**
- Ship sprite design
- Free movement (not fixed axis)
- Screen boundary constraints
- Ship positioning

**Code Written:**
- Player ship sprite data
- Enable sprite
- Position at left-centre
- Movement boundaries defined

**What the Learner Sees:**
Player ship hovering in the cave - ready to fly!

**Reference to Starfield:**
"Ship sprite setup like Starfield, but now with 8-direction movement in a scrolling world."

---

### Unit 7: Ship Flight Controls

**Learning Objectives:**
- 8-direction movement
- Speed appropriate for terrain
- Smooth control feel

**Concepts Introduced:**
- All-direction movement (unlike runner)
- Speed balance (not too fast for terrain)
- Acceleration option
- Tight controls

**Code Written:**
- Joystick reading (8 directions)
- Position updates
- Screen boundary clamping
- Movement speed tuning

**What the Learner Sees:**
Ship flies freely in all directions! Responsive, smooth controls.

---

### Unit 8: Ship Tilt Animation

**Learning Objectives:**
- Animate ship based on movement
- Up = nose up, down = nose down
- Visual feedback

**Concepts Introduced:**
- Movement-based animation
- Tilt frames (up, level, down)
- Frame selection logic
- Responsive feel

**Code Written:**
- Ship tilt sprite frames
- Select frame from Y movement
- Smooth frame transitions
- Apply to sprite pointer

**What the Learner Sees:**
Ship tilts with movement - nose up when climbing, down when diving!

---

### Unit 9: Terrain Collision Detection

**Learning Objectives:**
- Detect ship touching terrain
- Check ceiling and floor
- Death on collision

**Concepts Introduced:**
- Sprite-to-character collision
- Check ship's corners
- Terrain character detection
- Collision = death

**Code Written:**
- Get ship's pixel position
- Convert to character positions
- Check characters at corners
- Detect terrain characters

**What the Learner Sees:**
Fly into wall - ship crashes! Must navigate carefully.

**Reference to Maze Raider:**
"Tile collision from Maze Raider, now applied to a scrolling environment."

---

### Unit 10: Forward Laser

**Learning Objectives:**
- Fire laser on button press
- Rapid fire capability
- Bullet moves right

**Concepts Introduced:**
- Laser bullet sprite
- Fire rate limiting
- Bullet movement (rightward + scroll)
- Multiple bullets

**Code Written:**
- Laser bullet sprites (3)
- Fire on button press
- Move bullets right
- Remove at screen edge

**What the Learner Sees:**
Press fire - laser shoots right! Can fire rapidly.

**Reference to Starfield:**
"Shooting mechanics from Starfield applied to scrolling context - bullets must account for scroll."

---

### Unit 11: Laser-Terrain Collision

**Learning Objectives:**
- Laser stops at terrain
- Visual impact effect
- Limited penetration

**Concepts Introduced:**
- Bullet terrain collision
- Destruction effect
- Bullet removal
- Impact sprite

**Code Written:**
- Check bullet against terrain
- Impact effect on hit
- Remove bullet
- Brief explosion sprite

**What the Learner Sees:**
Lasers stop when hitting walls - spark effect on impact!

---

### Unit 12: Air Enemy - Basic

**Learning Objectives:**
- Add flying enemy
- Simple movement pattern
- Target for laser

**Concepts Introduced:**
- Enemy sprite
- Movement pattern (simple)
- Collision with laser
- Points for destruction

**Code Written:**
- Enemy sprite data
- Simple movement (drift left)
- Laser-enemy collision
- Destruction and score

**What the Learner Sees:**
Flying enemies appear! Shoot them for points!

---

### Unit 13: Bomb Weapon

**Learning Objectives:**
- Implement bomb drop
- Gravity-affected projectile
- Ground attack capability

**Concepts Introduced:**
- Bomb sprite
- Gravity on bomb
- Diagonal trajectory
- Separate fire button (down+fire)

**Code Written:**
- Bomb sprite data
- Drop on down+fire
- Apply gravity each frame
- Arc trajectory

**What the Learner Sees:**
Drop bombs! They arc downward with gravity - perfect for ground targets!

**Reference to Platform Panic:**
"Gravity simulation from Platform Panic applied to projectile - same physics, different context."

---

### Unit 14: Ground Target - Fuel Tank

**Learning Objectives:**
- Destructible ground target
- Bomb destroys it
- Essential for fuel mechanic

**Concepts Introduced:**
- Ground target characters
- Bomb collision detection
- Target destruction
- Score for destruction

**Code Written:**
- Fuel tank characters
- Bomb-target collision
- Destruction animation
- Score award

**What the Learner Sees:**
Fuel tanks on ground - bomb them for points and (soon) fuel!

---

### Unit 15: Death and Lives

**Learning Objectives:**
- Handle death sequences
- Lives system
- Respawn mechanics

**Concepts Introduced:**
- Death triggers (terrain, enemy)
- Death animation
- Lives decrement
- Respawn position

**Code Written:**
- Death animation
- Lives tracking
- Respawn at safe position
- Game over check

**What the Learner Sees:**
Crash into terrain or enemy - dramatic explosion! Lose a life, respawn, or game over.

---

### Unit 16: Complete Basic Game

**Learning Objectives:**
- Integrate all systems
- Add title screen
- Playable game

**Concepts Introduced:**
- Game state machine
- Title presentation
- Score display
- Basic playable loop

**Code Written:**
- Title screen
- Game states
- Score and lives display
- Complete game loop

**What the Learner Sees:**
Complete Scramble-style game! Title, fly through terrain, shoot enemies, bomb targets.

---

## Phase 2: Expansion (Units 17-32)
*Content: fuel management, enemy variety, stages, difficulty.*

### Unit 17: Fuel System - Display

**Learning Objectives:**
- Display fuel gauge
- Understand fuel as resource
- Create tension through scarcity

**Concepts Introduced:**
- Fuel as life resource
- Gauge display
- Fuel quantity tracking
- Visual representation

**Code Written:**
- Fuel variable
- Fuel gauge display
- Update routine
- Gauge graphics

**What the Learner Sees:**
Fuel gauge shows fuel level - currently doesn't deplete yet.

---

### Unit 18: Fuel Consumption

**Learning Objectives:**
- Fuel depletes over time
- Death when empty
- Resource pressure

**Concepts Introduced:**
- Constant fuel drain
- Depletion rate
- Empty = death
- Time pressure

**Code Written:**
- Fuel decrement routine
- Rate configuration
- Empty detection
- Death on empty

**What the Learner Sees:**
Fuel constantly drains! Run out and crash - must find more!

---

### Unit 19: Fuel Collection

**Learning Objectives:**
- Destroying fuel tanks gives fuel
- Risk/reward bombing
- Resource loop complete

**Concepts Introduced:**
- Fuel tank destruction = fuel
- Fuel amount per tank
- Strategic bombing
- Survival loop

**Code Written:**
- Fuel award on tank destroy
- Amount configuration
- Cap at maximum
- Visual feedback

**What the Learner Sees:**
Bomb fuel tanks to refuel! The survival loop is complete - must keep destroying tanks.

---

### Unit 20: Fuel Balancing

**Learning Objectives:**
- Balance fuel economy
- Fair but tense
- Tune parameters

**Concepts Introduced:**
- Consumption rate tuning
- Tank placement frequency
- Award amount tuning
- Difficulty through scarcity

**Code Written:**
- Configuration parameters
- Test and tune values
- Balance documentation
- Fair challenge

**What the Learner Sees:**
(Tuned experience - tense but fair fuel management.)

---

### Unit 21: Ground Target - Rocket

**Learning Objectives:**
- Add active ground target
- Rockets launch at player
- Priority threat

**Concepts Introduced:**
- Rocket launcher target
- Rockets fire upward
- Must destroy or dodge
- Higher threat level

**Code Written:**
- Rocket launcher characters
- Rocket sprite
- Launch trigger
- Rocket movement (homing lite)

**What the Learner Sees:**
Ground rocket launchers! They fire at you - bomb them fast or dodge!

---

### Unit 22: Ground Target - Base

**Learning Objectives:**
- High-value targets
- Multiple hits required
- Bonus points

**Concepts Introduced:**
- Base structure (multi-char)
- Hit points system
- Big point reward
- Priority target

**Code Written:**
- Base target characters
- HP tracking
- Progressive damage display
- Big score on destroy

**What the Learner Sees:**
Enemy bases - take multiple hits but worth big points!

---

### Unit 23: Air Enemy - Fighter

**Learning Objectives:**
- Aggressive air enemy
- Moves toward player
- Higher threat

**Concepts Introduced:**
- Tracking movement
- Collision damage
- Shoot to destroy
- Pattern variety

**Code Written:**
- Fighter sprite
- Movement toward player
- Collision with player
- Destruction handling

**What the Learner Sees:**
Fighter jets pursue you! Shoot them before they hit!

---

### Unit 24: Air Enemy - Missile

**Learning Objectives:**
- Fast-moving threat
- Straight line attack
- Reaction test

**Concepts Introduced:**
- High-speed enemy
- Predictable path
- Brief warning
- Quick destruction needed

**Code Written:**
- Missile sprite
- Fast horizontal movement
- Spawn from right
- Brief warning indicator

**What the Learner Sees:**
Missiles streak across! Fast reaction needed to shoot or dodge!

---

### Unit 25: Terrain Variety - Wide Cave

**Learning Objectives:**
- Open terrain sections
- Enemy focus areas
- Pacing variety

**Concepts Introduced:**
- Wide cave = less terrain
- More enemy room
- Combat focus sections
- Terrain pacing

**Code Written:**
- Wide cave terrain data
- Appropriate enemy spawning
- Section transitions
- Visual distinction

**What the Learner Sees:**
Cave opens up - room to manoeuvre but more enemies!

---

### Unit 26: Terrain Variety - Narrow Pass

**Learning Objectives:**
- Tight squeeze sections
- Precision flying
- Navigation focus

**Concepts Introduced:**
- Narrow passages
- Navigation challenge
- Reduced combat
- Skill testing

**Code Written:**
- Narrow terrain data
- Navigation challenge
- Enemy reduction
- Fair passage width

**What the Learner Sees:**
Narrow passage ahead - careful flying required! Squeeze through.

---

### Unit 27: Terrain Variety - Vertical Maze

**Learning Objectives:**
- Up-and-down terrain
- Varied ceiling/floor
- Complex navigation

**Concepts Introduced:**
- Variable heights
- Must fly up and down
- Stalactites and stalagmites
- 3D cave feeling

**Code Written:**
- Varying height terrain
- Obstacle characters
- Navigation complexity
- Visual variety

**What the Learner Sees:**
Terrain varies wildly - must weave up and down through obstacles!

---

### Unit 28: Stage Structure

**Learning Objectives:**
- Define game stages
- Each stage has theme
- Progression structure

**Concepts Introduced:**
- 6 stages (like Scramble)
- Theme per stage
- Difficulty per stage
- Stage completion

**Code Written:**
- Stage definition structure
- Stage loading
- Stage themes
- Transition handling

**What the Learner Sees:**
Stage 1 complete! Progress to Stage 2 with new challenges.

---

### Unit 29: Stage 1 - Caverns

**Learning Objectives:**
- Design first stage
- Introduction difficulty
- Establish mechanics

**Concepts Introduced:**
- Beginner-friendly design
- All mechanics introduced
- Fair challenge
- Tutorial through play

**Code Written:**
- Stage 1 terrain data
- Enemy placement
- Fuel tank placement
- Target placement

**What the Learner Sees:**
Stage 1: Caverns - introductory challenge, learn the mechanics.

---

### Unit 30: Stage 2 - Meteors

**Learning Objectives:**
- Asteroids/meteors theme
- New obstacle type
- Increased challenge

**Concepts Introduced:**
- Meteor obstacles
- Destructible/indestructible mix
- More chaotic
- Visual theme change

**Code Written:**
- Stage 2 terrain/objects
- Meteor sprites
- Destruction handling
- Theme colours

**What the Learner Sees:**
Stage 2: Meteors - dodge or destroy falling rocks! New visual theme.

---

### Unit 31: Stage 3 - Defense Grid

**Learning Objectives:**
- Heavy ground defenses
- Bombing focus
- Strategic challenge

**Concepts Introduced:**
- Dense ground targets
- Anti-aircraft emphasis
- Bombing priority
- Defense saturation

**Code Written:**
- Stage 3 layout
- Dense ground targets
- AA patterns
- Challenge tuning

**What the Learner Sees:**
Stage 3: Defense Grid - ground bristling with defenses! Bomb them all!

---

### Unit 32: Stage 4-6 Preview

**Learning Objectives:**
- Outline remaining stages
- Plan variety
- Complete structure

**Concepts Introduced:**
- Stage 4: Maze (tight navigation)
- Stage 5: Fortress (boss focus)
- Stage 6: Base (final assault)
- Complete game arc

**Code Written:**
- Stage structure placeholders
- Outline data
- Placeholder enemies
- Framework for completion

**What the Learner Sees:**
All 6 stages outlined - complete game structure in place!

---

## Phase 3: Polish (Units 33-48)
*Effects, sound, visual feedback, and "juice".*

### Unit 33: Parallax Stars

**Learning Objectives:**
- Background star field
- Multiple layers
- Depth perception

**Concepts Introduced:**
- Star layers behind terrain
- Different scroll rates
- Depth enhancement
- Performance consideration

**Code Written:**
- Star layer rendering
- Slower scroll rate
- Multiple star layers
- Integration with terrain

**What the Learner Sees:**
Stars scroll behind terrain at different speeds - space depth!

**Reference to Scroll Runner:**
"Parallax from Scroll Runner applied in different context - stars instead of mountains."

---

### Unit 34: Engine Sound

**Learning Objectives:**
- Continuous engine audio
- Pitch varies with speed
- Atmospheric sound

**Concepts Introduced:**
- Continuous sound effect
- Pitch modulation
- Audio atmosphere
- Voice allocation

**Code Written:**
- Engine noise generation
- Pitch variation
- Integration with gameplay
- Mix with other sounds

**What the Learner Sees:**
Engine hum while flying! Pitch changes with movement - immersive audio.

**Reference to SID Symphony:**
"Using SID Symphony's noise generation for engine sound - continuous atmosphere."

---

### Unit 35: Sound Design - Combat

**Learning Objectives:**
- Laser and bomb sounds
- Explosion sounds
- Audio feedback

**Concepts Introduced:**
- Laser zap sound
- Bomb drop sound
- Explosion variations
- Sound priority

**Code Written:**
- Combat sound effects
- Priority handling
- Variation per source
- Mix balance

**What the Learner Sees:**
Every action has sound - lasers zap, bombs whoosh, explosions boom!

---

### Unit 36: Level Streaming

**Learning Objectives:**
- Load level data during play
- Stream ahead of view
- Handle large levels

**Concepts Introduced:**
- Level data larger than RAM
- Load-ahead streaming
- Buffer management
- Seamless loading

**Code Written:**
- Level streaming routine
- Load-ahead logic
- Buffer rotation
- Error handling

**What the Learner Sees:**
(Internal - long levels load seamlessly during play.)

---

### Unit 37: Designed Levels - Stage 1

**Learning Objectives:**
- Hand-craft Stage 1
- Paced challenge
- Fair introduction

**Concepts Introduced:**
- Level design principles
- Pacing and rhythm
- Challenge curves
- Player guidance

**Code Written:**
- Detailed Stage 1 data
- Carefully placed elements
- Pacing refinement
- Test and iterate

**What the Learner Sees:**
Stage 1 feels designed - carefully paced, fair, teaching through play.

---

### Unit 38: Designed Levels - Stage 2-3

**Learning Objectives:**
- Complete Stage 2-3 design
- Theme consistency
- Challenge escalation

**Concepts Introduced:**
- Theme-appropriate design
- Escalating difficulty
- Variety within theme
- Player skill curve

**Code Written:**
- Stage 2 complete design
- Stage 3 complete design
- Theme implementation
- Difficulty tuning

**What the Learner Sees:**
Stages 2 and 3 fully designed - each feels distinct and fair.

---

### Unit 39: Designed Levels - Stage 4-6

**Learning Objectives:**
- Complete remaining stages
- Final stage special
- Complete game arc

**Concepts Introduced:**
- Late-game challenge
- Final stage design
- Climax creation
- Satisfying conclusion

**Code Written:**
- Stages 4-6 complete design
- Final stage special elements
- Boss preparation
- Complete level set

**What the Learner Sees:**
All 6 stages fully designed - complete game journey ready!

---

### Unit 40: Background Music

**Learning Objectives:**
- In-game music
- Stage themes
- Audio atmosphere

**Concepts Introduced:**
- Gameplay music
- Per-stage themes
- Music/effect balance
- Tension building

**Code Written:**
- Compose stage music
- Music system integration
- Stage-based selection
- Mix balancing

**What the Learner Sees:**
Music plays during stages - each stage has its own theme! Enhances atmosphere.

---

### Unit 41: HUD Enhancement

**Learning Objectives:**
- Polish UI display
- Clear information
- Visual design

**Concepts Introduced:**
- HUD layout design
- Information hierarchy
- Visual clarity
- Aesthetic polish

**Code Written:**
- Enhanced HUD graphics
- Improved layout
- Clear readability
- Consistent styling

**What the Learner Sees:**
Polished HUD - score, lives, fuel, stage all clearly displayed!

---

### Unit 42: Stage Transitions

**Learning Objectives:**
- Smooth stage changes
- Transition effects
- Stage announcement

**Concepts Introduced:**
- Stage complete fanfare
- Transition animation
- Next stage intro
- Brief pause

**Code Written:**
- Stage complete detection
- Transition sequence
- Stage announcement
- Next stage loading

**What the Learner Sees:**
Stage complete! Fanfare plays, "Stage 2" announced, brief pause before action resumes.

---

### Unit 43: Death Animation Polish

**Learning Objectives:**
- Elaborate death sequence
- Satisfying explosion
- Emotional impact

**Concepts Introduced:**
- Multi-frame explosion
- Debris particles
- Screen shake
- Sound accompaniment

**Code Written:**
- Elaborate explosion frames
- Particle effects
- Screen shake
- Death sound

**What the Learner Sees:**
Death is dramatic - big explosion, debris flies, screen shakes!

---

### Unit 44: Near-Miss System

**Learning Objectives:**
- Detect close calls
- Reward risk
- Enhance tension

**Concepts Introduced:**
- Proximity detection
- Near-miss scoring
- Visual feedback
- Psychological reward

**Code Written:**
- Near-miss detection
- Bonus points
- Flash effect
- Audio cue

**What the Learner Sees:**
Graze terrain closely - near miss bonus! Risk/reward for skilled flying.

---

### Unit 45: Title Screen Polish

**Learning Objectives:**
- Professional title
- Demo playback
- High score display

**Concepts Introduced:**
- Animated title
- Attract mode demo
- High scores
- Options

**Code Written:**
- Title animation
- Demo playback
- Score display
- Option selection

**What the Learner Sees:**
Impressive title screen with animation, demo, and high scores!

---

### Unit 46: High Score System

**Learning Objectives:**
- Track and save high scores
- Initial entry
- Persistence

**Concepts Introduced:**
- Score table
- Initial entry
- File operations
- Persistence

**Code Written:**
- High score table
- Entry screen
- Save/load
- Error handling

**What the Learner Sees:**
High scores saved! Beat the best - enter your initials!

---

### Unit 47: Difficulty Options

**Learning Objectives:**
- Selectable difficulty
- Accessibility
- Challenge options

**Concepts Introduced:**
- Difficulty levels
- Parameter adjustment
- Player choice
- Score modifier

**Code Written:**
- Difficulty selection
- Parameter tables
- Apply settings
- Score multiplier

**What the Learner Sees:**
Choose difficulty - Easy to learn, Normal for fun, Hard for challenge!

---

### Unit 48: Continue System

**Learning Objectives:**
- Continue option
- Score penalty
- Extended play

**Concepts Introduced:**
- Continue mechanic
- Stage checkpoint
- Score penalty
- Accessibility

**Code Written:**
- Continue detection
- Checkpoint resume
- Score handling
- Continue count

**What the Learner Sees:**
Game over? Continue from last stage! Score reduced but progress kept.

---

## Phase 4: Mastery (Units 49-64)
*Optimization, advanced mechanics, and professional polish.*

### Unit 49: Boss Framework

**Learning Objectives:**
- Design boss encounter system
- Different from normal gameplay
- End-of-stage challenge

**Concepts Introduced:**
- Boss mode flag
- Boss-specific rules
- Health bar display
- Pattern-based combat

**Code Written:**
- Boss mode infrastructure
- Boss health system
- Health bar display
- Pattern framework

**What the Learner Sees:**
(Framework ready for boss implementation.)

---

### Unit 50: Stage 3 Boss - Defense Platform

**Learning Objectives:**
- Create first boss
- Multiple attack patterns
- Satisfying defeat

**Concepts Introduced:**
- Large enemy sprite
- Attack pattern cycle
- Vulnerable points
- Phase transitions

**Code Written:**
- Defense Platform boss
- Attack patterns
- Vulnerability windows
- Defeat sequence

**What the Learner Sees:**
Stage 3 Boss - Defense Platform! Multiple weapons, find the pattern, destroy it!

---

### Unit 51: Stage 5 Boss - Fortress Core

**Learning Objectives:**
- Complex boss encounter
- Multiple phases
- Climactic mid-game

**Concepts Introduced:**
- Multi-phase boss
- Changing patterns
- Environmental interaction
- Dramatic encounter

**Code Written:**
- Fortress Core boss
- Phase transitions
- Complex patterns
- Defeat celebration

**What the Learner Sees:**
Stage 5 Boss - Fortress Core! Three phases, intense combat, satisfying victory!

---

### Unit 52: Final Boss - Enemy Base

**Learning Objectives:**
- Ultimate challenge
- All skills tested
- Triumphant ending

**Concepts Introduced:**
- Final boss design
- Ultimate challenge
- Victory sequence
- Game completion

**Code Written:**
- Final boss encounter
- Ultimate attack patterns
- Victory handling
- Ending sequence

**What the Learner Sees:**
Final Boss! Destroy the enemy base - all skills tested! Victory means game complete!

---

### Unit 53: Performance Profiling

**Learning Objectives:**
- Analyse performance
- Identify bottlenecks
- Optimization targets

**Concepts Introduced:**
- Raster timing
- Frame budget analysis
- Hotspot identification
- Optimization planning

**Code Written:**
- Timing display
- Routine measurement
- Documentation
- Optimization plan

**What the Learner Sees:**
Debug display shows performance - learn where time goes!

---

### Unit 54: Scroll Optimization

**Learning Objectives:**
- Optimize scroll routines
- Apply Scroll Runner lessons
- Maximum efficiency

**Concepts Introduced:**
- Scroll optimization techniques
- Self-modifying code
- Cache-friendly access
- Tight loops

**Code Written:**
- Optimized scroll
- Performance improvements
- Measurement verification

**What the Learner Sees:**
(Smoother performance - rock-solid scrolling.)

---

### Unit 55: Collision Optimization

**Learning Objectives:**
- Optimize collision detection
- Reduce checks
- Maintain accuracy

**Concepts Introduced:**
- Spatial partitioning
- Early-out checks
- Efficient algorithms
- Accuracy verification

**Code Written:**
- Optimized collision
- Spatial checks
- Verification tests

**What the Learner Sees:**
(Better performance with many objects.)

---

### Unit 56: Two-Player Mode

**Learning Objectives:**
- Alternating two-player
- Competitive scoring
- Social play

**Concepts Introduced:**
- Two-player alternating
- Separate scores
- Turn management
- Winner determination

**Code Written:**
- Player selection
- Score tracking
- Turn alternation
- Winner display

**What the Learner Sees:**
Two-player mode! Take turns, compete for best score!

---

### Unit 57: Special Weapons

**Learning Objectives:**
- Power-up weapons
- Limited ammunition
- Strategic choice

**Concepts Introduced:**
- Weapon power-ups
- Special weapon modes
- Ammo limitation
- Strategic use

**Code Written:**
- Power-up spawning
- Special weapon modes
- Ammo tracking
- Weapon effects

**What the Learner Sees:**
Grab power-ups for special weapons - spread shot, homing missiles, mega bombs!

---

### Unit 58: Statistics Tracking

**Learning Objectives:**
- Track play statistics
- Lifetime achievements
- Progress tracking

**Concepts Introduced:**
- Statistics system
- Running totals
- Display screen
- Persistence

**Code Written:**
- Stats tracking
- Display screen
- Save/load
- Milestone detection

**What the Learner Sees:**
Statistics screen shows lifetime play - enemies destroyed, stages beaten, etc.!

---

### Unit 59: Leaderboard Design

**Learning Objectives:**
- Enhanced high scores
- Per-stage records
- Achievement tracking

**Concepts Introduced:**
- Multiple leaderboards
- Stage best times
- Achievement list
- Comprehensive tracking

**Code Written:**
- Multiple score tables
- Stage records
- Achievement system
- Display formatting

**What the Learner Sees:**
Comprehensive leaderboards - overall scores, stage records, achievements!

---

### Unit 60: Visual Effects Polish

**Learning Objectives:**
- Final visual refinements
- Particle effects
- Polish details

**Concepts Introduced:**
- Visual consistency
- Effect refinement
- Detail polish
- Professional look

**Code Written:**
- Effect improvements
- Detail additions
- Consistency fixes
- Final polish

**What the Learner Sees:**
Everything looks polished - consistent, detailed, professional!

---

### Unit 61: Audio Polish

**Learning Objectives:**
- Final audio refinements
- Mix balancing
- Complete soundscape

**Concepts Introduced:**
- Audio mix review
- Balance adjustments
- Effect refinement
- Final tuning

**Code Written:**
- Volume adjustments
- Mix refinement
- Final audio touches

**What the Learner Sees:**
Audio perfectly balanced - engine, weapons, music all clear!

---

### Unit 62: Ending Sequence

**Learning Objectives:**
- Game completion reward
- Credits display
- Satisfying conclusion

**Concepts Introduced:**
- Ending sequence
- Credits roll
- Final statistics
- Replay motivation

**Code Written:**
- Ending trigger
- Credits display
- Final stats
- New game plus option

**What the Learner Sees:**
Beat the game - triumphant ending! Credits roll, stats display, play again?

---

### Unit 63: Memory Optimization

**Learning Objectives:**
- Optimize memory usage
- Clean architecture
- Future-proof design

**Concepts Introduced:**
- Memory map review
- Optimization opportunities
- Clean layout
- Documentation

**Code Written:**
- Memory optimization
- Architecture cleanup
- Documentation update

**What the Learner Sees:**
(Internal - clean, efficient memory use.)

---

### Unit 64: Release Build

**Learning Objectives:**
- Create final release
- Remove debug code
- Distribution ready

**Concepts Introduced:**
- Release build process
- Debug removal
- Final testing
- Package creation

**Code Written:**
- Debug code removal
- Startup optimization
- Final integration
- Release PRG

**What the Learner Sees:**
Complete Night Raid! A commercial-quality Scramble clone ready for distribution!

---

## Summary

**Night Raid** combines scrolling with shooting for a complete side-scrolling shooter:

**Phase 1 (Foundation):** Core mechanics - scrolling terrain, flight, shooting, bombing.

**Phase 2 (Expansion):** Content - fuel management, enemy variety, 6 stages.

**Phase 3 (Polish):** Feel - parallax, sound design, level streaming, transitions.

**Phase 4 (Mastery):** Professional quality - boss encounters, optimization, release build.

### Skills Transferred Forward

The following skills debut or are significantly enhanced in Night Raid:

1. **Scrolling + shooting combination** → Parallax Patrol, Mega Blaster
2. **Terrain collision in scrolling** → Parallax Patrol, all scrolling games
3. **Resource management (fuel)** → Dungeon Crawl (items), many others
4. **Level streaming** → Parallax Patrol, Mega Blaster, Isometric Quest
5. **Boss encounters** → Sprite Storm, Arena Fighter, Mega Blaster
6. **Designed levels** → All subsequent games
7. **Multiple weapon types** → Mega Blaster, many others

### Game Specifications

- **Stages:** 6 distinct themed stages
- **Weapons:** Laser (forward), Bomb (gravity-affected)
- **Enemies:** 6+ types (fighters, missiles, rockets, bases)
- **Bosses:** 3 (Stages 3, 5, Final)
- **Resource:** Fuel (constant drain, refilled by tanks)
- **Ground targets:** Fuel tanks, rockets, bases
- **Players:** 1-2 alternating
- **Features:** High scores, difficulty options, special weapons, statistics
