# Sprite Storm: 64-Unit Outline

**Game:** 9 of 16
**Platform:** Commodore 64
**Units:** 64
**Concept:** Multi-sprite action game. More enemies than the hardware allows - enter multiplexing. An arena shooter where waves of enemies swarm the player.

---

## Skills Applied from Previous Games

| Skill | Learned In | Application in Sprite Storm |
|-------|-----------|---------------------------|
| SID fundamentals | SID Symphony | Sound effects, music |
| Hardware sprites | Starfield | All game objects |
| Joystick input | Starfield | Player control |
| Shooting mechanics | Starfield | Player weapons |
| Sprite collision | Starfield | Combat system |
| Score display | Starfield | Scoring system |
| Custom characters | Maze Raider | Arena display |
| Gravity/physics | Platform Panic | Particle effects |
| Animation frames | Platform Panic | Enemy animations |
| Object pools | Brick Basher | Bullet management |
| Wave progression | Invader Wave | Enemy waves |
| Raster interrupts | Scroll Runner | Sprite multiplexing timing |
| Performance profiling | Night Raid | Optimization techniques |
| Boss encounters | Night Raid | Wave bosses |

## New Skills Introduced

| Skill | Units | Description |
|-------|-------|-------------|
| Sprite multiplexing theory | 5-8 | Understanding why and how |
| Y-sorted sprite list | 9-12 | Sorting sprites for reuse |
| Raster interrupt timing | 13-16 | Precise IRQ placement |
| Sprite reuse | 17-20 | Same hardware sprite, different object |
| Flicker management | 21-24 | Handling overflow gracefully |
| 16+ sprites | 25-28 | Doubling visible sprites |
| 24+ sprites | 29-32 | Pushing the limits |
| Priority handling | 33-36 | Correct sprite overlap |
| Multiplexer optimization | 49-52 | Maximum performance |

---

## Phase 1: Foundation (Units 1-16)
*Understanding the problem and basic multiplexing.*

### Unit 1: The 8-Sprite Limit

**Learning Objectives:**
- Understand VIC-II sprite limitations
- See the problem firsthand
- Motivation for multiplexing

**Concepts Introduced:**
- VIC-II has 8 hardware sprites (0-7)
- Only 8 objects visible at once
- Games need more than 8
- The challenge defined

**Code Written:**
- Display 8 sprites moving
- Add 9th sprite - nothing appears
- Demonstrate the hard limit
- Document the problem

**What the Learner Sees:**
8 sprites work fine. Try to add a 9th - nothing! Hardware limit demonstrated.

---

### Unit 2: Why Multiplexing Works

**Learning Objectives:**
- Understand raster beam concept
- Learn sprite reuse window
- Conceptual foundation

**Concepts Introduced:**
- VIC-II draws top to bottom
- Each sprite drawn at its Y position
- After drawing, sprite hardware is free
- Can reposition for lower on screen

**Code Written:**
- Document raster beam concept
- Diagram sprite timing windows
- Calculate reuse opportunities
- Foundation for implementation

**What the Learner Sees:**
Understanding WHY multiplexing works - the raster beam creates opportunities.

---

### Unit 3: Simple Multiplexing Concept

**Learning Objectives:**
- Demonstrate basic multiplexing
- Two objects, one sprite
- Prove the concept

**Concepts Introduced:**
- Top-of-screen object
- Bottom-of-screen object
- Same hardware sprite number
- Repositioned mid-frame

**Code Written:**
- Place sprite at Y=50
- Raster interrupt at Y=100
- Reposition same sprite to Y=150
- Two objects, one sprite!

**What the Learner Sees:**
Same sprite appears twice on screen! One near top, one near bottom. Multiplexing works!

---

### Unit 4: The Arena Game Concept

**Learning Objectives:**
- Design the game framework
- Arena shooter concept
- Enemy swarm gameplay

**Concepts Introduced:**
- Fixed arena (no scrolling)
- Player in centre
- Enemies spawn from edges
- Wave-based survival

**Code Written:**
- Arena design
- Player concept
- Enemy swarm concept
- Wave structure

**What the Learner Sees:**
Game concept defined - survive enemy swarms in a fixed arena!

---

### Unit 5: Arena Setup

**Learning Objectives:**
- Create game arena
- Character-based border
- Playing field established

**Concepts Introduced:**
- Arena border graphics
- Play area definition
- Score/status area
- Visual framework

**Code Written:**
- Arena border characters
- Draw border
- Status area layout
- Clear play area

**What the Learner Sees:**
Arena displayed - bordered play area with status display ready.

---

### Unit 6: Player Ship

**Learning Objectives:**
- Create player sprite
- 8-direction movement
- Arena-constrained

**Concepts Introduced:**
- Player sprite (always sprite 0)
- Reserved from multiplexing
- Full movement
- Arena boundaries

**Code Written:**
- Player sprite data
- Movement in 8 directions
- Arena boundary collision
- Smooth control

**What the Learner Sees:**
Player ship in arena - moves freely in all directions!

**Reference to Starfield:**
"Player sprite setup from Starfield, but now moves in all directions within a bounded arena."

---

### Unit 7: Player Shooting

**Learning Objectives:**
- Implement shooting
- 8-direction firing
- Bullet sprites

**Concepts Introduced:**
- Directional firing
- Multiple bullets (4)
- Bullets from sprite pool
- Hit detection

**Code Written:**
- Bullet sprites (4 reserved)
- Fire in facing direction
- Bullet movement
- Edge removal

**What the Learner Sees:**
Press fire - bullets fly in facing direction! Multiple bullets active.

---

### Unit 8: Basic Enemy

**Learning Objectives:**
- Create first enemy type
- Simple movement
- Target for shooting

**Concepts Introduced:**
- Enemy data structure
- Spawn from edge
- Move toward player
- Death on hit

**Code Written:**
- Enemy sprite
- Spawn routine
- Movement toward player
- Collision with bullets

**What the Learner Sees:**
Enemies spawn and approach! Shoot them to survive!

---

### Unit 9: Y-Sorted Sprite List

**Learning Objectives:**
- Understand sprite sorting
- Why Y-order matters
- Implement sorting

**Concepts Introduced:**
- Multiplexing requires Y-order
- Higher Y = processed first
- Insertion sort efficient for nearly-sorted
- Sprite list structure

**Code Written:**
- Sprite list data structure
- Insertion sort routine
- Sort by Y position
- Test sorting

**What the Learner Sees:**
(Internal - sorting happens invisibly. Next unit uses it.)

---

### Unit 10: Sorted List to Sprites

**Learning Objectives:**
- Assign sorted list to hardware
- Top 8 get sprites directly
- Foundation for multiplexing

**Concepts Introduced:**
- Hardware sprite assignment
- Sorted list → sprite mapping
- Handle fewer than 8
- Handle more than 8 (coming)

**Code Written:**
- List-to-sprite assignment
- Position updates
- Pointer updates
- Colour updates

**What the Learner Sees:**
Multiple enemies displayed correctly - sorted and rendered!

---

### Unit 11: Raster Interrupt for Multiplexing

**Learning Objectives:**
- Set up multiplexing interrupt
- Trigger at correct line
- Foundation for sprite reuse

**Concepts Introduced:**
- IRQ for multiplexing
- Trigger below visible sprites
- Prepare for reuse
- Timing requirements

**Code Written:**
- Multiplexer IRQ setup
- Trigger line calculation
- Basic handler
- ACK and return

**What the Learner Sees:**
(Internal - IRQ fires but no visible effect yet.)

**Reference to Scroll Runner:**
"Raster interrupts from Scroll Runner, now used for precise sprite timing."

---

### Unit 12: First Working Multiplexer

**Learning Objectives:**
- Implement basic multiplexing
- Show 9-16 sprites
- Break the barrier!

**Concepts Introduced:**
- Sprite reuse in IRQ
- Second batch of objects
- Same sprites, lower Y
- More than 8 visible!

**Code Written:**
- IRQ repositions sprites
- Process sprites 9-16
- Assign to hardware sprites
- Complete multiplexer v1

**What the Learner Sees:**
MORE THAN 8 SPRITES! 12 enemies on screen at once! The barrier is broken!

---

### Unit 13: Multiplexer Zones

**Learning Objectives:**
- Multiple reuse zones
- Even more sprites
- Zone management

**Concepts Introduced:**
- Multiple IRQ points
- Three zones: top, middle, bottom
- 24 potential objects
- Zone scheduling

**Code Written:**
- Multiple zone IRQs
- Zone assignment
- Object distribution
- Extended multiplexer

**What the Learner Sees:**
Even more sprites! 16+ enemies swarming the player!

---

### Unit 14: Enemy Waves

**Learning Objectives:**
- Implement wave system
- Increasing enemy count
- Progressive challenge

**Concepts Introduced:**
- Wave counter
- Enemies per wave
- Spawn patterns
- Wave completion

**Code Written:**
- Wave system
- Spawn timing
- Count tracking
- Wave transitions

**What the Learner Sees:**
Waves of enemies! Each wave bigger than the last!

**Reference to Invader Wave:**
"Wave system from Invader Wave, now with many more enemies per wave."

---

### Unit 15: Score and Lives

**Learning Objectives:**
- Implement scoring
- Lives system
- Game over flow

**Concepts Introduced:**
- Points per enemy
- Lives counter
- Game over condition
- Restart flow

**Code Written:**
- Score tracking
- Lives display
- Game over screen
- Restart option

**What the Learner Sees:**
Score increases with kills! Lives depleted on hits. Game over when empty.

---

### Unit 16: Complete Basic Game

**Learning Objectives:**
- Integrate all systems
- Playable with multiplexing
- Foundation complete

**Concepts Introduced:**
- Complete game loop
- Title screen
- Working multiplexer
- Playable game

**Code Written:**
- Title screen
- Complete integration
- All systems working
- Playable game

**What the Learner Sees:**
Complete game with multiplexing! Many more enemies than should be possible!

---

## Phase 2: Expansion (Units 17-32)
*More sprites, enemy variety, power-ups.*

### Unit 17: Multiplexer Analysis

**Learning Objectives:**
- Analyse current multiplexer
- Identify limitations
- Plan improvements

**Concepts Introduced:**
- Performance profiling
- Sprite limit per zone
- Flicker conditions
- Improvement targets

**Code Written:**
- Timing analysis
- Document limitations
- Plan improvements
- Benchmark current

**What the Learner Sees:**
Understanding of multiplexer performance - where the limits are.

---

### Unit 18: Flicker Management

**Learning Objectives:**
- Handle sprite overflow
- Graceful degradation
- Priority-based flicker

**Concepts Introduced:**
- More objects than can display
- Rotating which sprites shown
- Flicker distribution
- Priority preservation

**Code Written:**
- Overflow detection
- Rotation system
- Priority sprites (player bullets)
- Even flicker distribution

**What the Learner Sees:**
Even with many enemies, important sprites (player, bullets) never flicker!

---

### Unit 19: Optimized Sorting

**Learning Objectives:**
- Improve sort performance
- Handle many objects
- Frame budget savings

**Concepts Introduced:**
- Sort optimization
- Partial sorting option
- Frame budget recovery
- Algorithm choice

**Code Written:**
- Optimized insertion sort
- Partial sorting for stability
- Benchmark improvement
- Verify correctness

**What the Learner Sees:**
(Performance improvement - more CPU for gameplay.)

---

### Unit 20: Enemy Type - Speeder

**Learning Objectives:**
- Fast enemy type
- Different threat
- Variety introduction

**Concepts Introduced:**
- Fast movement
- Different sprite
- Lower health (one hit)
- Quick reflexes required

**Code Written:**
- Speeder sprite
- Fast movement logic
- Spawn in waves
- Behaviour variation

**What the Learner Sees:**
Fast enemies! Speeders zip across - quick shooting required!

---

### Unit 21: Enemy Type - Tank

**Learning Objectives:**
- Slow, tough enemy
- Multiple hits required
- Blocking threat

**Concepts Introduced:**
- High health points
- Slow movement
- Multiple hits to kill
- Spray strategy

**Code Written:**
- Tank sprite
- Health tracking
- Slow movement
- Damage feedback

**What the Learner Sees:**
Tank enemies! Slow but take multiple hits to destroy!

---

### Unit 22: Enemy Type - Shooter

**Learning Objectives:**
- Enemy that fires back
- Dodging required
- Threat escalation

**Concepts Introduced:**
- Enemy bullets
- Firing patterns
- Player dodging
- Two-way combat

**Code Written:**
- Shooter sprite
- Enemy bullet system
- Firing logic
- Player collision with enemy bullets

**What the Learner Sees:**
Shooters fire back! Dodge their bullets while returning fire!

---

### Unit 23: Enemy Bullets - Multiplexing

**Learning Objectives:**
- Enemy bullets in multiplexer
- Many more projectiles
- Bullet hell possibility

**Concepts Introduced:**
- Bullets as sprites
- Include in multiplexer
- Priority after enemies
- Dense bullet patterns

**Code Written:**
- Enemy bullets in sprite list
- Proper sorting
- Priority handling
- Many bullets possible

**What the Learner Sees:**
Enemy bullets everywhere! Multiplexing handles them all!

---

### Unit 24: Power-Up Framework

**Learning Objectives:**
- Design power-up system
- Dropped from enemies
- Collection mechanic

**Concepts Introduced:**
- Power-up sprites
- Drop chance
- Collection collision
- Effect activation

**Code Written:**
- Power-up sprite
- Drop logic
- Collection detection
- Effect framework

**What the Learner Sees:**
Enemies drop power-ups! Collect for bonuses!

**Reference to Brick Basher:**
"Power-up system from Brick Basher adapted for arena shooter."

---

### Unit 25: Power-Up - Spread Shot

**Learning Objectives:**
- Multi-direction firing
- Powerful upgrade
- Time-limited

**Concepts Introduced:**
- Spread shot pattern
- Multiple bullets per fire
- Duration timer
- Sprite allocation

**Code Written:**
- Spread shot mode
- Multi-bullet firing
- Timer countdown
- Visual indicator

**What the Learner Sees:**
Spread shot! Fire in three directions at once! Limited time.

---

### Unit 26: Power-Up - Shield

**Learning Objectives:**
- Temporary invincibility
- Hit absorption
- Strategic collection

**Concepts Introduced:**
- Shield state
- Visual indicator
- Hit absorption
- Duration

**Code Written:**
- Shield mode
- Visual effect (flashing)
- Hit absorption
- Timer

**What the Learner Sees:**
Shield active! Flash while protected, absorb hits!

---

### Unit 27: Power-Up - Speed Boost

**Learning Objectives:**
- Movement speed increase
- Tactical advantage
- Dodging enhancement

**Concepts Introduced:**
- Speed multiplier
- Movement enhancement
- Tactical repositioning
- Duration

**Code Written:**
- Speed modifier
- Apply to movement
- Visual effect
- Timer

**What the Learner Sees:**
Speed boost! Zip around the arena quickly!

---

### Unit 28: Power-Up - Smart Bomb

**Learning Objectives:**
- Screen-clear weapon
- Emergency save
- Rare and powerful

**Concepts Introduced:**
- Instant kill all enemies
- Screen flash effect
- Limited quantity
- Desperation tool

**Code Written:**
- Smart bomb activation
- All enemy death
- Flash effect
- Sound effect

**What the Learner Sees:**
Smart bomb! All enemies destroyed with dramatic flash!

---

### Unit 29: Wave Bosses

**Learning Objectives:**
- Mini-boss every N waves
- Larger enemy
- Challenge spike

**Concepts Introduced:**
- Boss wave trigger
- Larger sprite (multicolor or compound)
- Health bar
- Pattern attack

**Code Written:**
- Boss spawning
- Health tracking
- Attack patterns
- Defeat handling

**What the Learner Sees:**
Boss wave! Large enemy with health bar - defeat it to continue!

**Reference to Night Raid:**
"Boss encounter structure from Night Raid adapted for arena format."

---

### Unit 30: 24+ Sprites

**Learning Objectives:**
- Push multiplexer to extremes
- Maximum visible objects
- Technical showcase

**Concepts Introduced:**
- Four-zone multiplexer
- 24-32 visible sprites
- Careful timing
- Performance management

**Code Written:**
- Extended multiplexer
- Four zones
- Timing refinement
- Capacity testing

**What the Learner Sees:**
HUGE swarms! 24+ enemies on screen - technical achievement!

---

### Unit 31: Difficulty Scaling

**Learning Objectives:**
- Automatic difficulty
- Fair challenge curve
- Player adaptation

**Concepts Introduced:**
- Difficulty parameters
- Wave-based scaling
- Speed increases
- Count increases

**Code Written:**
- Difficulty curves
- Parameter tables
- Apply per wave
- Balance tuning

**What the Learner Sees:**
Game gets harder naturally - more enemies, faster movement, tougher types.

---

### Unit 32: Endless Mode

**Learning Objectives:**
- Infinite play
- High score focus
- Continuous challenge

**Concepts Introduced:**
- No win condition
- Survival focus
- Score chasing
- Difficulty plateau

**Code Written:**
- Endless wave generation
- Score emphasis
- Difficulty cap
- High score tracking

**What the Learner Sees:**
Endless survival mode! How long can you last? Chase the high score!

---

## Phase 3: Polish (Units 33-48)
*Effects, sound, visual feedback, and "juice".*

### Unit 33: Sprite Priority System

**Learning Objectives:**
- Correct sprite overlap
- Visual consistency
- Priority handling

**Concepts Introduced:**
- Sprite priority register
- Draw order control
- Background vs foreground
- Consistent appearance

**Code Written:**
- Priority management
- Consistent ordering
- Player always on top
- Background enemies

**What the Learner Sees:**
Sprites overlap correctly - player always visible, consistent layering.

---

### Unit 34: Explosion Effects

**Learning Objectives:**
- Satisfying destruction
- Multiple explosion types
- Visual feedback

**Concepts Introduced:**
- Explosion animation
- Size by enemy type
- Chain reactions
- Particle effects

**Code Written:**
- Explosion sprites
- Animation sequences
- Type-based sizing
- Particle system

**What the Learner Sees:**
Satisfying explosions! Big enemies = big explosions! Particles fly!

---

### Unit 35: Sound Design - Combat

**Learning Objectives:**
- Complete combat audio
- Distinctive sounds
- Feedback richness

**Concepts Introduced:**
- Sound palette
- Variation by action
- Priority management
- Mix balance

**Code Written:**
- Player shooting sound
- Enemy death sounds
- Power-up sounds
- Collision sounds

**What the Learner Sees:**
Every action has distinctive sound - rich audio feedback!

**Reference to SID Symphony:**
"Full SID Symphony techniques for complete audio palette."

---

### Unit 36: Sound Design - Music

**Learning Objectives:**
- Action music
- Wave transitions
- Boss themes

**Concepts Introduced:**
- Gameplay music
- Intensity matching
- Boss theme
- Victory fanfares

**Code Written:**
- Main game music
- Boss music
- Fanfares
- Music system

**What the Learner Sees:**
Energetic music drives gameplay! Boss has special theme!

---

### Unit 37: Screen Shake

**Learning Objectives:**
- Impact feedback
- Screen shake effect
- Intensity variation

**Concepts Introduced:**
- Screen shake technique
- Scroll register manipulation
- Intensity by event
- Duration control

**Code Written:**
- Shake routine
- Trigger on impacts
- Intensity parameter
- Smooth recovery

**What the Learner Sees:**
Big explosions shake the screen! Impact feels powerful!

---

### Unit 38: Combo System

**Learning Objectives:**
- Chain kills for bonus
- Risk/reward scoring
- Skill expression

**Concepts Introduced:**
- Combo counter
- Time window
- Score multiplier
- Visual feedback

**Code Written:**
- Combo tracking
- Timer management
- Multiplier display
- Sound escalation

**What the Learner Sees:**
Chain kills for combo multiplier! 5x, 10x, 20x - massive scores!

---

### Unit 39: Near-Miss Bonus

**Learning Objectives:**
- Reward risky play
- Close call detection
- Score bonus

**Concepts Introduced:**
- Proximity detection
- Near-miss definition
- Bonus points
- Adrenaline reward

**Code Written:**
- Near-miss detection
- Bonus award
- Visual flash
- Audio cue

**What the Learner Sees:**
Near miss! Bonus points for close calls! Risk is rewarded!

---

### Unit 40: Spawn Effects

**Learning Objectives:**
- Enemy spawn visuals
- Warning indicators
- Fair gameplay

**Concepts Introduced:**
- Spawn warning
- Appear animation
- Edge indication
- Player preparation

**Code Written:**
- Spawn warning effect
- Edge indicators
- Appear animation
- Timing for fairness

**What the Learner Sees:**
Enemies telegraph spawns! Warning flash before appearing - fair chance to react!

---

### Unit 41: Background Variety

**Learning Objectives:**
- Visual variety
- Arena themes
- Fresh presentation

**Concepts Introduced:**
- Background themes
- Character set variations
- Colour schemes
- Wave-based changes

**Code Written:**
- Multiple backgrounds
- Theme selection
- Colour schemes
- Transition effects

**What the Learner Sees:**
Arena changes appearance every few waves - fresh visuals keep it interesting!

---

### Unit 42: Title Screen

**Learning Objectives:**
- Professional presentation
- Demo mode
- High scores

**Concepts Introduced:**
- Animated title
- Demo gameplay
- Score display
- Options

**Code Written:**
- Title animation
- Demo mode
- High score display
- Option selection

**What the Learner Sees:**
Impressive title with demo gameplay showing off multiplexing!

---

### Unit 43: High Score System

**Learning Objectives:**
- Score tracking
- Name entry
- Persistence

**Concepts Introduced:**
- High score table
- Initial entry
- Save/load
- Competition

**Code Written:**
- Score table
- Entry screen
- Persistence
- Display

**What the Learner Sees:**
High scores saved! Compete for the top spot!

---

### Unit 44: Two-Player Mode

**Learning Objectives:**
- Cooperative play
- Two players simultaneously
- Sprite allocation

**Concepts Introduced:**
- Two player sprites reserved
- Cooperative gameplay
- Shared score or competitive
- Sprite budget adjustment

**Code Written:**
- Two player support
- Input handling
- Score modes
- Sprite allocation

**What the Learner Sees:**
Two-player co-op! Fight together against the swarms!

---

### Unit 45: Statistics

**Learning Objectives:**
- Track achievements
- Lifetime stats
- Progress feedback

**Concepts Introduced:**
- Statistics tracking
- Lifetime totals
- Display screen
- Persistence

**Code Written:**
- Stats tracking
- Display
- Persistence
- Milestones

**What the Learner Sees:**
Statistics show lifetime play - enemies destroyed, waves survived, etc.!

---

### Unit 46: Challenge Modes

**Learning Objectives:**
- Variant game modes
- Different rules
- Replay variety

**Concepts Introduced:**
- Mode selection
- Rule variations
- Leaderboards per mode
- Variety value

**Code Written:**
- Mode framework
- Rule variations
- Separate scores
- Mode selection

**What the Learner Sees:**
Challenge modes! One-life mode, time attack, boss rush!

---

### Unit 47: Visual Polish

**Learning Objectives:**
- Final visual refinements
- Consistency
- Professional quality

**Concepts Introduced:**
- Visual consistency
- Colour harmony
- Effect polish
- Detail refinement

**Code Written:**
- Visual adjustments
- Consistency fixes
- Effect polish
- Final details

**What the Learner Sees:**
Everything polished and consistent - professional appearance.

---

### Unit 48: Audio Polish

**Learning Objectives:**
- Final audio refinements
- Mix balance
- Complete soundscape

**Concepts Introduced:**
- Audio mix review
- Balance adjustments
- Effect/music balance
- Final tuning

**Code Written:**
- Volume adjustments
- Mix refinement
- Final audio touches

**What the Learner Sees:**
Audio perfectly balanced - everything clear and impactful.

---

## Phase 4: Mastery (Units 49-64)
*Optimization, advanced techniques, and professional polish.*

### Unit 49: Multiplexer Optimization - Analysis

**Learning Objectives:**
- Deep performance analysis
- Identify optimization targets
- Document timing

**Concepts Introduced:**
- Cycle-level analysis
- Critical path identification
- Optimization priority
- Documentation

**Code Written:**
- Detailed timing analysis
- Critical path documentation
- Optimization plan
- Benchmark baseline

**What the Learner Sees:**
Understanding exactly where CPU time goes in the multiplexer.

---

### Unit 50: Multiplexer Optimization - Sorting

**Learning Objectives:**
- Optimize sort routine
- Minimize cycles
- Maximum efficiency

**Concepts Introduced:**
- Sort optimization techniques
- Unrolling
- Table lookups
- Register allocation

**Code Written:**
- Optimized sort
- Benchmarking
- Verification
- Documentation

**What the Learner Sees:**
(Performance improvement - more sprites possible.)

---

### Unit 51: Multiplexer Optimization - IRQ

**Learning Objectives:**
- Optimize IRQ handler
- Minimize overhead
- Stable timing

**Concepts Introduced:**
- IRQ optimization
- Fast entry/exit
- Register preservation
- Stable timing

**Code Written:**
- Optimized IRQ handler
- Timing verification
- Stability testing
- Documentation

**What the Learner Sees:**
(Performance improvement - rock-solid multiplexing.)

---

### Unit 52: Maximum Sprites Test

**Learning Objectives:**
- Push to absolute limits
- 32+ sprites
- Technical showcase

**Concepts Introduced:**
- Absolute maximum
- Trade-offs
- Flicker acceptance
- Showcase mode

**Code Written:**
- Maximum sprite test
- Showcase mode
- Document limits
- Configuration options

**What the Learner Sees:**
Test mode with 32+ sprites! Technical showcase of multiplexing power!

---

### Unit 53: Enemy AI Enhancement

**Learning Objectives:**
- Smarter enemy behaviour
- Pattern variety
- Challenge refinement

**Concepts Introduced:**
- AI behaviour types
- Pattern selection
- Group behaviour
- Challenge tuning

**Code Written:**
- Enhanced AI
- Behaviour types
- Group coordination
- Pattern variety

**What the Learner Sees:**
Enemies behave smarter - coordinated attacks, varied patterns!

---

### Unit 54: Boss Enhancement

**Learning Objectives:**
- Elaborate boss encounters
- Multi-phase fights
- Memorable battles

**Concepts Introduced:**
- Multi-phase bosses
- Pattern variety
- Environmental effects
- Satisfying victories

**Code Written:**
- Enhanced boss phases
- New patterns
- Environmental effects
- Victory sequences

**What the Learner Sees:**
Bosses are more elaborate - multiple phases, varied attacks, epic battles!

---

### Unit 55: Particle System Enhancement

**Learning Objectives:**
- More elaborate effects
- Particle variety
- Visual richness

**Concepts Introduced:**
- Particle types
- Physics variations
- Effect triggers
- Performance balance

**Code Written:**
- Enhanced particles
- Variety of types
- Physics options
- Performance-safe

**What the Learner Sees:**
Richer visual effects - varied particles, more satisfying destruction!

---

### Unit 56: Weapon Variety

**Learning Objectives:**
- More weapon types
- Permanent upgrades
- Build variety

**Concepts Introduced:**
- Weapon selection
- Permanent pickups
- Build paths
- Strategy options

**Code Written:**
- Weapon system
- Multiple types
- Upgrade paths
- Selection UI

**What the Learner Sees:**
Choose your weapons! Different builds for different play styles!

---

### Unit 57: Endless Mode Enhancement

**Learning Objectives:**
- Richer endless experience
- Event variety
- Long-term engagement

**Concepts Introduced:**
- Random events
- Special waves
- Variety injection
- Long-term interest

**Code Written:**
- Event system
- Special wave types
- Variety management
- Interest maintenance

**What the Learner Sees:**
Endless mode with events! Special challenges keep runs fresh!

---

### Unit 58: Leaderboard Enhancement

**Learning Objectives:**
- Rich leaderboard system
- Per-mode scores
- Achievement tracking

**Concepts Introduced:**
- Multiple leaderboards
- Mode-specific records
- Achievement system
- Competition features

**Code Written:**
- Extended leaderboards
- Achievement tracking
- Display screens
- Persistence

**What the Learner Sees:**
Comprehensive leaderboards - scores, achievements, records per mode!

---

### Unit 59: Tutorial Mode

**Learning Objectives:**
- Teach game mechanics
- New player onboarding
- Accessibility

**Concepts Introduced:**
- Tutorial design
- Progressive teaching
- Practice environment
- Player guidance

**Code Written:**
- Tutorial framework
- Progressive lessons
- Practice mode
- Skip option

**What the Learner Sees:**
Tutorial teaches the game - great for new players!

---

### Unit 60: Accessibility Options

**Learning Objectives:**
- Difficulty options
- Visual options
- Player accommodation

**Concepts Introduced:**
- Difficulty scaling
- Visual options
- Control options
- Accessibility value

**Code Written:**
- Options menu
- Difficulty settings
- Visual settings
- Save preferences

**What the Learner Sees:**
Options for all players - easy mode, visual settings, control options!

---

### Unit 61: Memory Optimization

**Learning Objectives:**
- Optimize memory usage
- Efficient structures
- Clean architecture

**Concepts Introduced:**
- Memory review
- Structure optimization
- Clean layout
- Documentation

**Code Written:**
- Memory optimization
- Structure cleanup
- Documentation
- Verification

**What the Learner Sees:**
(Internal - efficient memory use.)

---

### Unit 62: Final Testing

**Learning Objectives:**
- Comprehensive testing
- Bug fixing
- Quality assurance

**Concepts Introduced:**
- Test methodology
- Bug tracking
- Quality standards
- Release criteria

**Code Written:**
- Test execution
- Bug fixes
- Quality verification
- Documentation

**What the Learner Sees:**
(Stable, polished game.)

---

### Unit 63: Documentation

**Learning Objectives:**
- Document multiplexer
- Technical reference
- Teaching resource

**Concepts Introduced:**
- Technical documentation
- Implementation reference
- Teaching value
- Knowledge preservation

**Code Written:**
- Multiplexer documentation
- Code comments
- Technical guide
- Example code

**What the Learner Sees:**
Complete documentation of the multiplexer - reference for future projects!

---

### Unit 64: Release Build

**Learning Objectives:**
- Create final release
- Remove debug code
- Distribution ready

**Concepts Introduced:**
- Release process
- Debug removal
- Final packaging
- Distribution

**Code Written:**
- Debug removal
- Optimization pass
- Final integration
- Release PRG

**What the Learner Sees:**
Complete Sprite Storm! Sprite multiplexing mastered, ready for distribution!

---

## Summary

**Sprite Storm** teaches the crucial skill of sprite multiplexing:

**Phase 1 (Foundation):** Understanding the problem - 8-sprite limit, why multiplexing works, basic implementation.

**Phase 2 (Expansion):** More sprites - 24+ sprites, enemy variety, power-ups, bosses.

**Phase 3 (Polish):** Feel - effects, sound, visual feedback, game modes.

**Phase 4 (Mastery):** Optimization - cycle-level optimization, maximum sprites, professional quality.

### Skills Transferred Forward

The following skills debut in Sprite Storm and will be applied in future games:

1. **Sprite multiplexing** → Raster Rider, Parallax Patrol, Mega Blaster, Symphony's End
2. **Y-sorted sprite lists** → All games with many sprites
3. **Raster-precise timing** → Raster Rider (essential), all advanced games
4. **Flicker management** → All games exceeding 8 sprites
5. **Priority handling** → All multiplexed games
6. **Optimized IRQ handlers** → All advanced games

### Game Specifications

- **Multiplexing:** 24-32 visible sprites
- **Player:** 1-2 cooperative
- **Enemy types:** 5+ (basic, speeder, tank, shooter, boss)
- **Power-ups:** 4 types (spread, shield, speed, bomb)
- **Weapons:** 4 types with upgrades
- **Modes:** Normal waves, endless, challenge modes
- **Features:** Combos, near-miss bonuses, statistics, achievements
