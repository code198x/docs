# Game 9: Sprite Storm - Complete 256-Unit Outline

## Game Overview
**Platform:** Commodore 64
**Genre:** Arena shooter with sprite multiplexing
**Concept:** More enemies than hardware allows. The C64 has 8 sprites - this game displays 24-32 using raster interrupt multiplexing. Master THE defining C64 technique.

**Technical Focus:**
- Sprite multiplexing (8→32 sprites)
- Raster interrupt timing and chaining
- Y-sorted sprite lists
- Flicker management strategies
- IRQ-stable code
- Performance optimisation

---

## Phase 1: Foundation (Units 1-16)
*Basic display and single sprites*

### Unit 1: Project Setup
- Arena shooter concept
- Memory layout for multiplexing
- System setup
- **Runnable:** Clean startup

### Unit 2: Display Setup
- Screen configuration
- Border/background colours
- Play area definition
- **Runnable:** Display ready

### Unit 3: Sprite Basics Review
- VIC-II sprite registers
- Sprite pointers
- Enable and position
- **Runnable:** Single sprite

### Unit 4: All 8 Hardware Sprites
- Enable all 8 sprites
- Position across screen
- Different colours
- **Runnable:** 8 sprites displayed

### Unit 5: Sprite Data Design
- Player ship sprite
- Enemy sprite designs
- Projectile sprites
- **Runnable:** Game sprites ready

### Unit 6: Player Movement
- Joystick control
- Smooth movement
- Screen boundaries
- **Runnable:** Player moves

### Unit 7: Player Sprite Assignment
- Dedicate sprite 0 to player
- Always visible priority
- Consistent rendering
- **Runnable:** Player sprite stable

### Unit 8: Static Enemies
- Place enemy sprites
- Fixed positions
- Using sprites 1-7
- **Runnable:** Enemies displayed

### Unit 9: Enemy Movement
- Simple movement patterns
- Bounce off walls
- Independent motion
- **Runnable:** Enemies move

### Unit 10: Basic Collision
- Sprite-sprite collision register
- Player vs enemy detection
- Collision response
- **Runnable:** Collisions detected

### Unit 11: Shooting Basics
- Fire button detection
- Projectile sprite
- Movement and bounds
- **Runnable:** Player shoots

### Unit 12: Projectile Collision
- Bullet vs enemy
- Enemy destruction
- Bullet removal
- **Runnable:** Enemies destroyed

### Unit 13: Score System
- Points per enemy
- Score display
- Running total
- **Runnable:** Scoring works

### Unit 14: Lives System
- Three lives
- Death on collision
- Lives display
- **Runnable:** Lives tracking

### Unit 15: Game Loop
- Title screen
- Game state
- Game over
- **Runnable:** Complete loop

### Unit 16: Phase 1 Integration
- 8-sprite arena shooter
- Foundation complete
- Ready for multiplexing
- **Runnable:** Basic arena game

---

## Phase 2: Raster Interrupts (Units 17-32)
*Understanding raster timing*

### Unit 17: Raster Concept
- How the VIC-II draws
- Raster line counter
- 312 lines (PAL)
- **Runnable:** Concept understood

### Unit 18: Reading Raster Position
- $D012 raster register
- $D011 bit 7 (line 256+)
- Polling raster
- **Runnable:** Raster read

### Unit 19: Raster Interrupt Setup
- $D012 trigger line
- $D01A interrupt enable
- Acknowledge with $D019
- **Runnable:** IRQ triggers

### Unit 20: Basic Raster IRQ
- Set raster line
- IRQ handler
- Change border colour
- **Runnable:** Border colour change

### Unit 21: IRQ Handler Structure
- Save registers
- Do work
- Acknowledge
- Restore and RTI
- **Runnable:** Proper handler

### Unit 22: Stable Raster Basics
- Jitter problem
- Why timing varies
- Cycle counting intro
- **Runnable:** Jitter observed

### Unit 23: Double IRQ Technique
- First IRQ sets second
- Second is cycle-exact
- Stable timing achieved
- **Runnable:** Stable raster

### Unit 24: Multiple Raster Splits
- Chain multiple IRQs
- Different screen zones
- Multiple colour changes
- **Runnable:** Multi-split screen

### Unit 25: Sprite Y Timing
- When VIC reads sprite Y
- Badlines and timing
- Sprite fetch cycles
- **Runnable:** Timing documented

### Unit 26: Sprite Register Timing
- When to change registers
- Safe update windows
- Avoiding glitches
- **Runnable:** Clean updates

### Unit 27: Two Zones Demo
- Top half: sprites 0-3
- Bottom half: sprites 4-7
- Reuse sprites
- **Runnable:** Basic multiplex

### Unit 28: Zone Boundary
- Change at raster line
- Update Y positions
- Update pointers
- **Runnable:** Zone switch works

### Unit 29: IRQ Timing Precision
- Cycle counting
- NOP padding
- Exact timing
- **Runnable:** Precise timing

### Unit 30: Badline Awareness
- What badlines are
- When they occur
- Working around them
- **Runnable:** Badline handling

### Unit 31: Performance Measurement
- Cycle budget
- Border colour debug
- Measuring IRQ time
- **Runnable:** Performance visible

### Unit 32: Phase 2 Integration
- Raster interrupts mastered
- Stable timing achieved
- Ready for multiplexing
- **Runnable:** 2-zone multiplexing

---

## Phase 3: Basic Multiplexing (Units 33-48)
*First multiplexer implementation*

### Unit 33: Multiplexing Concept
- Virtual sprites (24-32)
- Map to 8 hardware sprites
- Y-position sorting
- **Runnable:** Concept clear

### Unit 34: Virtual Sprite Table
- X, Y, pointer, colour
- 24 virtual sprites
- Data structure design
- **Runnable:** Table created

### Unit 35: Y-Position Sorting
- Why Y-sort matters
- Simple bubble sort
- Sorted list output
- **Runnable:** Sorting works

### Unit 36: Sort Optimisation
- Insertion sort better
- Nearly-sorted data
- Faster sorting
- **Runnable:** Faster sort

### Unit 37: Sprite Slot Assignment
- Map virtual to hardware
- Track which slot free
- Slot allocation
- **Runnable:** Slots assigned

### Unit 38: First 8 Sprites
- Display top 8 virtual sprites
- No multiplexing yet
- Foundation verified
- **Runnable:** Top 8 display

### Unit 39: IRQ at First Reuse
- Find first reuse point
- Set IRQ there
- Prepare for switch
- **Runnable:** IRQ positioned

### Unit 40: Sprite Reuse Logic
- Free slot when sprite passed
- Assign to next virtual
- Update registers
- **Runnable:** Basic reuse

### Unit 41: 12 Sprites Working
- 8 hardware, 12 virtual
- Single reuse zone
- Verify display
- **Runnable:** 12 sprites

### Unit 42: 16 Sprites Working
- More reuse
- Multiple switches
- Performance check
- **Runnable:** 16 sprites

### Unit 43: Dynamic IRQ Positioning
- IRQ line from sort data
- Changes each frame
- Adapts to content
- **Runnable:** Dynamic IRQs

### Unit 44: Multiple IRQ Chain
- Several IRQs per frame
- Chain together
- Handle all zones
- **Runnable:** IRQ chain

### Unit 45: 20 Sprites Working
- Complex multiplexing
- Multiple zones
- Stable display
- **Runnable:** 20 sprites

### Unit 46: 24 Sprites Target
- Full arena's worth
- Stress testing
- Performance tuning
- **Runnable:** 24 sprites

### Unit 47: Flicker Analysis
- When flicker occurs
- Too many same Y
- Flicker strategies
- **Runnable:** Flicker understood

### Unit 48: Phase 3 Integration
- 24-sprite multiplexer
- Sorted and allocated
- Dynamic IRQs
- **Runnable:** Working multiplexer

---

## Phase 4: Advanced Multiplexing (Units 49-64)
*Optimisation and edge cases*

### Unit 49: Bucket Sort
- Y-position buckets
- O(n) sorting
- Much faster
- **Runnable:** Bucket sort

### Unit 50: Unrolled IRQ Handler
- No loops in IRQ
- Unrolled register writes
- Maximum speed
- **Runnable:** Fast handler

### Unit 51: Self-Modifying Code
- Modify IRQ inline
- Change values directly
- Avoid table lookups
- **Runnable:** Self-mod IRQ

### Unit 52: 28 Sprites
- Push the limit
- More zones
- Tighter timing
- **Runnable:** 28 sprites

### Unit 53: 32 Sprites
- Maximum practical
- Heavy multiplexing
- Performance edge
- **Runnable:** 32 sprites

### Unit 54: Flicker Reduction
- Distribute across Y
- Priority rotation
- Even coverage
- **Runnable:** Less flicker

### Unit 55: Priority System
- Player never flickers
- Important enemies stable
- Flicker on expendables
- **Runnable:** Priority flicker

### Unit 56: Sprite Crunch Avoidance
- The sprite crunch bug
- When it triggers
- Safe Y positions
- **Runnable:** No crunch

### Unit 57: Expanded Sprites
- Y-expanded sprites
- Multiplexing with expansion
- Double-height handling
- **Runnable:** Expanded multiplex

### Unit 58: X-Expanded Sprites
- X-expansion handling
- Register differences
- Mixed expansion
- **Runnable:** X-expand works

### Unit 59: Multicolour Sprites
- Multicolour mode
- Shared colours
- Per-sprite colours
- **Runnable:** Multicolour

### Unit 60: Mixed Sprite Modes
- Some hires, some multi
- Mode per sprite
- Flexible rendering
- **Runnable:** Mixed modes

### Unit 61: Behind Background
- Sprite priority bit
- Behind characters
- Visual depth
- **Runnable:** Priority layers

### Unit 62: Sprite-Background Collision
- $D01F register
- Collision with chars
- Gameplay use
- **Runnable:** BG collision

### Unit 63: Full Multiplexer
- All features combined
- 32 sprites capable
- Production ready
- **Runnable:** Complete multiplexer

### Unit 64: Phase 4 Integration
- Advanced multiplexing
- Optimised code
- All edge cases
- **Runnable:** Pro multiplexer

---

## Phase 5: Arena Game Core (Units 65-80)
*Building the arena shooter*

### Unit 65: Arena Design
- Play area bounds
- Visual border
- Safe zones
- **Runnable:** Arena displayed

### Unit 66: Player Integration
- Player in multiplexer
- High priority slot
- Stable display
- **Runnable:** Player in arena

### Unit 67: Enemy Types
- Basic enemy (moves, bounces)
- Chaser (follows player)
- Shooter (fires back)
- **Runnable:** Enemy variety

### Unit 68: Enemy Data Structure
- Type, position, state
- Health, behaviour
- Efficient storage
- **Runnable:** Enemy data

### Unit 69: Enemy Spawning
- Spawn points
- Wave spawning
- Entry animations
- **Runnable:** Enemies spawn

### Unit 70: Wave System
- Wave definitions
- Enemy composition
- Difficulty curve
- **Runnable:** Waves work

### Unit 71: Wave Completion
- All enemies destroyed
- Wave complete message
- Next wave prep
- **Runnable:** Wave progression

### Unit 72: Player Weapons
- Single shot
- Rapid fire
- Spread shot
- **Runnable:** Weapon types

### Unit 73: Weapon Power-Ups
- Power-up drops
- Weapon switching
- Visual feedback
- **Runnable:** Power-ups

### Unit 74: Enemy Projectiles
- Enemies shoot back
- Projectile pooling
- Collision with player
- **Runnable:** Enemy fire

### Unit 75: Projectile Multiplexing
- Bullets in multiplexer
- Many projectiles
- Bullet hell lite
- **Runnable:** Many bullets

### Unit 76: Screen Shake
- Impact feedback
- Shake on damage
- Intensity scaling
- **Runnable:** Screen shake

### Unit 77: Explosions
- Sprite explosions
- Animation frames
- Particle feel
- **Runnable:** Explosions

### Unit 78: Combo System
- Rapid kills bonus
- Combo counter
- Multiplier display
- **Runnable:** Combos

### Unit 79: Difficulty Scaling
- Enemies per wave
- Speed increase
- More shooters
- **Runnable:** Scaling difficulty

### Unit 80: Phase 5 Integration
- Full arena gameplay
- Multiple enemies
- Waves and weapons
- **Runnable:** Arena shooter core

---

## Phase 6: Polish & Audio (Units 81-96)
*Visual and audio refinement*

### Unit 81: SID Setup
- Sound effect system
- Channel allocation
- Effect triggers
- **Runnable:** Audio ready

### Unit 82: Shoot Sound
- Player fire sound
- Satisfying feedback
- Quick and punchy
- **Runnable:** Shoot SFX

### Unit 83: Explosion Sound
- Enemy destruction
- Impact sound
- Varied pitch
- **Runnable:** Explosion SFX

### Unit 84: Player Death Sound
- Death audio
- Dramatic effect
- Clear feedback
- **Runnable:** Death SFX

### Unit 85: Power-Up Sound
- Collection jingle
- Positive feedback
- Distinctive sound
- **Runnable:** Power-up SFX

### Unit 86: Background Music
- In-game music
- Energetic tempo
- Loop seamlessly
- **Runnable:** Music playing

### Unit 87: Music During IRQs
- Music player timing
- Work with multiplexer
- No audio glitches
- **Runnable:** Stable music

### Unit 88: Title Screen Design
- Attractive title
- High score display
- Controls info
- **Runnable:** Title screen

### Unit 89: Title Animation
- Animated sprites
- Colour cycling
- Eye-catching
- **Runnable:** Animated title

### Unit 90: HUD Design
- Score display
- Lives icons
- Wave counter
- **Runnable:** HUD layout

### Unit 91: Character Graphics
- Custom font
- Number graphics
- Clean HUD
- **Runnable:** Custom chars

### Unit 92: Colour Scheme
- Cohesive palette
- Per-wave colours
- Visual variety
- **Runnable:** Colour polish

### Unit 93: Spawn Effects
- Enemy entry animation
- Teleport effect
- Warning indication
- **Runnable:** Spawn effects

### Unit 94: Death Sequences
- Player death animation
- Life lost sequence
- Respawn effect
- **Runnable:** Death sequence

### Unit 95: Wave Transitions
- Wave complete display
- Brief pause
- Next wave intro
- **Runnable:** Transitions

### Unit 96: Phase 6 Integration
- Full audio
- Visual polish
- Transitions complete
- **Runnable:** Polished game

---

## Phase 7: Boss Battles (Units 97-112)
*Multi-sprite bosses*

### Unit 97: Boss Concept
- Large multi-sprite boss
- Composite enemy
- Special waves
- **Runnable:** Boss design

### Unit 98: Boss Sprite Composition
- 4-6 sprites combined
- Relative positioning
- Move as unit
- **Runnable:** Composite boss

### Unit 99: Boss in Multiplexer
- Boss sprite priority
- Reserved slots
- Stable boss display
- **Runnable:** Boss displayed

### Unit 100: Boss Movement
- Boss movement patterns
- Predictable for fairness
- Menacing motion
- **Runnable:** Boss moves

### Unit 101: Boss Attack Patterns
- Phase 1 attacks
- Bullet patterns
- Aimed shots
- **Runnable:** Boss attacks

### Unit 102: Boss Vulnerability
- Weak point targeting
- Damage feedback
- Health indication
- **Runnable:** Boss takes damage

### Unit 103: Boss Health Display
- Health bar
- Damage visible
- Progress feedback
- **Runnable:** Health bar

### Unit 104: Boss Phases
- Multiple phases
- Pattern changes
- Increasing danger
- **Runnable:** Multi-phase boss

### Unit 105: Boss 1 Complete
- First boss finished
- Wave 5 boss
- Tuned difficulty
- **Runnable:** Boss 1 done

### Unit 106: Boss 2 Design
- Different boss
- New patterns
- Visual distinction
- **Runnable:** Boss 2 design

### Unit 107: Boss 2 Attacks
- Unique attacks
- More complex
- Wave 10 boss
- **Runnable:** Boss 2 attacks

### Unit 108: Boss 2 Complete
- Second boss finished
- Harder than boss 1
- Satisfying challenge
- **Runnable:** Boss 2 done

### Unit 109: Final Boss Design
- Largest boss
- Most complex
- Ultimate challenge
- **Runnable:** Final boss design

### Unit 110: Final Boss Phases
- Three+ phases
- Pattern escalation
- Epic encounter
- **Runnable:** Final boss phases

### Unit 111: Final Boss Complete
- Final boss finished
- Wave 15 boss
- Game climax
- **Runnable:** Final boss done

### Unit 112: Phase 7 Integration
- Three bosses complete
- Boss waves working
- Epic encounters
- **Runnable:** Bosses complete

---

## Phase 8: Content & Modes (Units 113-128)
*Game modes and content*

### Unit 113: Normal Mode
- Standard progression
- 15 waves + bosses
- Default experience
- **Runnable:** Normal mode

### Unit 114: Endless Mode
- Infinite waves
- Score attack
- Increasing difficulty
- **Runnable:** Endless mode

### Unit 115: Boss Rush
- Bosses only
- Quick play
- Practice mode
- **Runnable:** Boss rush

### Unit 116: Two-Player Co-op
- Simultaneous play
- Shared screen
- Both in multiplexer
- **Runnable:** Co-op mode

### Unit 117: Two-Player Versus
- Competitive mode
- Separate scores
- Steal kills
- **Runnable:** Versus mode

### Unit 118: Difficulty Settings
- Easy/Normal/Hard
- Enemy speed/count
- Accessibility
- **Runnable:** Difficulty options

### Unit 119: High Score Table
- Top 10 scores
- Name entry
- Persistent storage
- **Runnable:** High scores

### Unit 120: Statistics
- Enemies killed
- Accuracy
- Games played
- **Runnable:** Statistics

### Unit 121: Pause Menu
- Pause game
- Options access
- Resume/quit
- **Runnable:** Pause menu

### Unit 122: Options Screen
- Music toggle
- SFX toggle
- Controls info
- **Runnable:** Options

### Unit 123: Attract Mode
- Demo on title
- Shows gameplay
- Auto-play
- **Runnable:** Attract mode

### Unit 124: Performance Profiling
- Measure all systems
- Optimise bottlenecks
- Smooth 50fps
- **Runnable:** Profiled

### Unit 125: Bug Fixing
- Test all modes
- Fix edge cases
- Stable build
- **Runnable:** Bug-free

### Unit 126: Final Balance
- Difficulty curve
- Boss tuning
- Fair challenge
- **Runnable:** Balanced

### Unit 127: Release Build
- Final version
- All features
- Complete package
- **Runnable:** Release ready

### Unit 128: Phase 8 Integration
- All modes complete
- Full content
- Polished game
- **Runnable:** Complete game

---

## Phase 9: Multiplexer Mastery (Units 129-144)
*Advanced multiplexer techniques*

### Unit 129: Multiplexer Review
- Current implementation
- Performance analysis
- Improvement targets
- **Runnable:** Analysis done

### Unit 130: Zero-Page Optimisation
- Critical vars in ZP
- Faster access
- More ZP usage
- **Runnable:** ZP optimised

### Unit 131: Table Alignment
- Page-aligned tables
- No page-cross penalty
- Faster lookups
- **Runnable:** Aligned tables

### Unit 132: Unrolled Sorting
- Unrolled sort loop
- Fixed sprite count
- Maximum speed
- **Runnable:** Fast sorting

### Unit 133: IRQ Nesting
- Nested interrupts
- More flexibility
- Complex timing
- **Runnable:** Nested IRQs

### Unit 134: Flexible Sprite Count
- Variable virtual sprites
- Adapt to gameplay
- Dynamic allocation
- **Runnable:** Flexible count

### Unit 135: Sprite Pooling
- Sprite object pools
- No allocation
- Reuse efficiently
- **Runnable:** Sprite pools

### Unit 136: Animation Integration
- Animated sprites
- Frame changes
- Pointer updates
- **Runnable:** Animated multiplex

### Unit 137: Colour Animation
- Colour cycling
- Per-sprite colours
- Flash effects
- **Runnable:** Colour animation

### Unit 138: Priority Animation
- Change priorities
- Depth sorting
- Visual layers
- **Runnable:** Priority changes

### Unit 139: Smooth Scrolling Prep
- Multiplexing + scrolling
- Combined techniques
- Future games prep
- **Runnable:** Scroll prep

### Unit 140: Optimised Collision
- Fast collision checks
- Bounding boxes
- Spatial partitioning
- **Runnable:** Fast collision

### Unit 141: Memory Optimisation
- Reduce memory use
- Sprite data packing
- Efficient storage
- **Runnable:** Memory efficient

### Unit 142: Cycle Counting
- Document all cycles
- IRQ budget
- Headroom analysis
- **Runnable:** Cycle documented

### Unit 143: Maximum Sprites Test
- Push to 36+ sprites
- Stress test
- Find true limits
- **Runnable:** Max sprites

### Unit 144: Phase 9 Integration
- Optimised multiplexer
- Production quality
- Reusable code
- **Runnable:** Pro multiplexer

---

## Phase 10: Advanced Enemies (Units 145-160)
*Complex enemy behaviours*

### Unit 145: Enemy AI Framework
- Behaviour system
- State machines
- AI types
- **Runnable:** AI framework

### Unit 146: Chaser AI
- Follow player
- Prediction
- Smooth pursuit
- **Runnable:** Chaser AI

### Unit 147: Flanker AI
- Circle player
- Attack angles
- Tactical movement
- **Runnable:** Flanker AI

### Unit 148: Swarm AI
- Group behaviour
- Flocking
- Coordinated attack
- **Runnable:** Swarm AI

### Unit 149: Bomber AI
- Approach and retreat
- Drop explosives
- Hit and run
- **Runnable:** Bomber AI

### Unit 150: Turret Enemy
- Stationary shooter
- Aimed fire
- Pattern shots
- **Runnable:** Turret enemy

### Unit 151: Shield Enemy
- Directional shield
- Vulnerable side
- Requires strategy
- **Runnable:** Shield enemy

### Unit 152: Split Enemy
- Splits on death
- Smaller children
- Chain reactions
- **Runnable:** Split enemy

### Unit 153: Teleporter Enemy
- Blink movement
- Unpredictable
- Surprise attacks
- **Runnable:** Teleporter

### Unit 154: Mini-Boss Enemy
- Strong regular enemy
- More health
- Complex pattern
- **Runnable:** Mini-boss

### Unit 155: Enemy Formations
- Formation patterns
- Coordinated entry
- Group attacks
- **Runnable:** Formations

### Unit 156: Dynamic Spawning
- React to player
- Adaptive waves
- Fair challenge
- **Runnable:** Dynamic spawns

### Unit 157: Enemy Variety Balance
- Right mix per wave
- Interesting combinations
- Varied gameplay
- **Runnable:** Balanced variety

### Unit 158: Elite Enemies
- Palette-swapped stronger
- More dangerous
- Later waves
- **Runnable:** Elite enemies

### Unit 159: Enemy Polish
- All enemies animated
- Death effects
- Visual feedback
- **Runnable:** Enemy polish

### Unit 160: Phase 10 Integration
- 10+ enemy types
- Complex AI
- Varied gameplay
- **Runnable:** Enemy complete

---

## Phase 11: Weapon Systems (Units 161-176)
*Advanced weapons and power-ups*

### Unit 161: Weapon Framework
- Weapon data structure
- Switch system
- Upgrade tracking
- **Runnable:** Weapon framework

### Unit 162: Weapon Levels
- Level 1-3 per weapon
- Increasing power
- Visual change
- **Runnable:** Weapon levels

### Unit 163: Rapid Fire
- Fast shooting
- Projectile management
- Ammo consideration
- **Runnable:** Rapid fire

### Unit 164: Spread Shot
- 3-way spread
- 5-way at max
- Area coverage
- **Runnable:** Spread shot

### Unit 165: Laser Weapon
- Piercing beam
- Through enemies
- Visual effect
- **Runnable:** Laser

### Unit 166: Homing Missiles
- Seeking projectiles
- Target acquisition
- Limited ammo
- **Runnable:** Homing

### Unit 167: Bomb Weapon
- Screen clear
- Limited bombs
- Emergency use
- **Runnable:** Bombs

### Unit 168: Shield Power-Up
- Temporary shield
- Hit absorption
- Visual indicator
- **Runnable:** Shield

### Unit 169: Speed Power-Up
- Movement speed
- Duration limited
- Risk/reward
- **Runnable:** Speed boost

### Unit 170: Score Multiplier
- Points multiplier
- Timed bonus
- Score attack
- **Runnable:** Multiplier

### Unit 171: Weapon Drop System
- Enemy drops
- Random/fixed drops
- Fair distribution
- **Runnable:** Drop system

### Unit 172: Power-Up Visuals
- Distinct icons
- Colour coding
- Easy recognition
- **Runnable:** Clear power-ups

### Unit 173: Weapon Switch UI
- Current weapon display
- Level indicator
- Ammo/power
- **Runnable:** Weapon UI

### Unit 174: Weapon Balance
- DPS balancing
- Situational use
- No dominant choice
- **Runnable:** Balanced weapons

### Unit 175: Weapon Effects
- Muzzle flash
- Impact effects
- Visual feedback
- **Runnable:** Weapon effects

### Unit 176: Phase 11 Integration
- Complete weapon system
- Multiple weapons
- Power-up economy
- **Runnable:** Weapons complete

---

## Phase 12: Advanced Bosses (Units 177-192)
*Epic boss encounters*

### Unit 177: Boss Framework Review
- Current boss system
- Expansion plans
- Modular design
- **Runnable:** Framework review

### Unit 178: Boss 1 Enhancement
- Add phases
- More attacks
- Greater challenge
- **Runnable:** Boss 1 enhanced

### Unit 179: Boss 1 Desperation
- Low health phase
- Dangerous patterns
- Exciting finale
- **Runnable:** Boss 1 desperate

### Unit 180: Boss 2 Enhancement
- Expand boss 2
- Unique mechanics
- Memorable fight
- **Runnable:** Boss 2 enhanced

### Unit 181: Boss 2 Minions
- Boss spawns enemies
- Multi-threat
- Complex battle
- **Runnable:** Boss 2 minions

### Unit 182: Mid-Boss 1
- Wave 3 mini-boss
- Easier boss intro
- Boss practice
- **Runnable:** Mid-boss 1

### Unit 183: Mid-Boss 2
- Wave 7 mini-boss
- Different pattern
- Variety
- **Runnable:** Mid-boss 2

### Unit 184: Final Boss Expansion
- More phases
- Epic scale
- Ultimate test
- **Runnable:** Final boss expanded

### Unit 185: Final Boss Form 2
- Transformation
- New sprite config
- Escalation
- **Runnable:** Final boss form 2

### Unit 186: Final Boss Form 3
- Final form
- Maximum danger
- True finale
- **Runnable:** Final boss form 3

### Unit 187: Boss Patterns Polish
- Fair patterns
- Learnable attacks
- Skill-based
- **Runnable:** Fair patterns

### Unit 188: Boss Music
- Unique boss track
- Intense music
- Atmosphere
- **Runnable:** Boss music

### Unit 189: Boss Victory
- Celebration
- Big explosion
- Score bonus
- **Runnable:** Boss victory

### Unit 190: Boss Retry
- Quick restart
- Practice friendly
- Less frustration
- **Runnable:** Boss retry

### Unit 191: Boss Gallery
- View defeated bosses
- Bestiary
- Completion tracking
- **Runnable:** Boss gallery

### Unit 192: Phase 12 Integration
- 6+ boss fights
- Epic encounters
- Memorable battles
- **Runnable:** Bosses complete

---

## Phase 13: Game Modes & Content (Units 193-208)
*Expanded modes and replayability*

### Unit 193: Challenge Mode
- Specific challenges
- Par scores
- Skill tests
- **Runnable:** Challenges

### Unit 194: Daily Challenge
- Seeded random
- Global competition
- Fresh content
- **Runnable:** Daily mode

### Unit 195: Wave Editor Data
- Wave data format
- Custom waves
- User content
- **Runnable:** Wave data format

### Unit 196: Preset Wave Packs
- Multiple campaigns
- Different themes
- Extended content
- **Runnable:** Wave packs

### Unit 197: Achievements
- Track accomplishments
- Unlock rewards
- Goals
- **Runnable:** Achievements

### Unit 198: Unlockables
- Unlock weapons
- Unlock modes
- Progression
- **Runnable:** Unlockables

### Unit 199: Ship Variants
- Different player ships
- Stat differences
- Visual variety
- **Runnable:** Ship variants

### Unit 200: Leaderboards
- Per-mode scores
- Competition
- Replay value
- **Runnable:** Leaderboards

### Unit 201: Tutorial Mode
- Guided introduction
- Teach mechanics
- New player friendly
- **Runnable:** Tutorial

### Unit 202: Practice Mode
- Select enemy types
- Boss practice
- Skill building
- **Runnable:** Practice mode

### Unit 203: Hardcore Mode
- One life
- No continues
- Ultimate challenge
- **Runnable:** Hardcore

### Unit 204: Speed Run Mode
- Timer
- Fast completion
- Optimal routes
- **Runnable:** Speed run

### Unit 205: Content Statistics
- Completion percentage
- All modes tracked
- Collection status
- **Runnable:** Content stats

### Unit 206: Replay System
- Record gameplay
- Playback
- Share runs
- **Runnable:** Replay

### Unit 207: Content Polish
- All modes refined
- Consistent quality
- Complete package
- **Runnable:** Content polished

### Unit 208: Phase 13 Integration
- All modes complete
- Rich content
- High replayability
- **Runnable:** Modes complete

---

## Phase 14: Optimisation (Units 209-224)
*Maximum performance*

### Unit 209: Performance Audit
- Profile all systems
- Find bottlenecks
- Prioritise fixes
- **Runnable:** Audit complete

### Unit 210: Main Loop Optimisation
- Streamline game loop
- Reduce overhead
- Faster frame
- **Runnable:** Loop optimised

### Unit 211: Collision Optimisation
- Spatial hashing
- Early rejection
- Minimal checks
- **Runnable:** Fast collision

### Unit 212: Rendering Optimisation
- Minimise draws
- Dirty rectangles
- Smart updates
- **Runnable:** Fast rendering

### Unit 213: Memory Layout
- Optimal data placement
- Cache-friendly
- Fast access
- **Runnable:** Memory optimised

### Unit 214: IRQ Streamlining
- Minimal IRQ work
- Deferred processing
- Stable timing
- **Runnable:** IRQ optimised

### Unit 215: AI Optimisation
- Faster AI updates
- Skip distant
- LOD for AI
- **Runnable:** Fast AI

### Unit 216: Audio Optimisation
- Efficient music player
- Minimal CPU
- Stable playback
- **Runnable:** Fast audio

### Unit 217: 50fps Lock
- Consistent framerate
- No drops
- Smooth gameplay
- **Runnable:** Locked 50fps

### Unit 218: Worst Case Testing
- Maximum sprites
- Maximum bullets
- Stress test
- **Runnable:** Stress tested

### Unit 219: NTSC Compatibility
- 60Hz timing
- NTSC machines
- International
- **Runnable:** NTSC works

### Unit 220: Memory Usage
- Minimise RAM
- Fit in 64K
- Efficient code
- **Runnable:** Memory fit

### Unit 221: Load Time
- Fast startup
- Minimal loading
- Quick play
- **Runnable:** Fast load

### Unit 222: Save System
- Save progress
- High scores
- Persistent data
- **Runnable:** Save works

### Unit 223: Code Cleanup
- Remove dead code
- Clean structure
- Maintainable
- **Runnable:** Clean code

### Unit 224: Phase 14 Integration
- Maximum performance
- Stable 50fps
- Optimised code
- **Runnable:** Optimised game

---

## Phase 15: Final Polish (Units 225-240)
*Release quality*

### Unit 225: Visual Polish Pass
- All graphics reviewed
- Consistent style
- Professional look
- **Runnable:** Visual polish

### Unit 226: Audio Polish Pass
- Sound levels
- Music mix
- Balanced audio
- **Runnable:** Audio polish

### Unit 227: Gameplay Polish
- Feel refinement
- Control tweaks
- Satisfying play
- **Runnable:** Gameplay polish

### Unit 228: Difficulty Polish
- Fair curve
- Accessible start
- Challenging end
- **Runnable:** Difficulty polish

### Unit 229: UI Polish
- Clean menus
- Clear information
- Easy navigation
- **Runnable:** UI polish

### Unit 230: Bug Hunt
- Systematic testing
- Edge cases
- Fix all bugs
- **Runnable:** Bug-free

### Unit 231: Playtesting Round 1
- External testers
- Gather feedback
- Note issues
- **Runnable:** Playtest 1

### Unit 232: Feedback Integration 1
- Address feedback
- Improve weak areas
- Iterate
- **Runnable:** Feedback applied

### Unit 233: Playtesting Round 2
- More testing
- Verify fixes
- New feedback
- **Runnable:** Playtest 2

### Unit 234: Feedback Integration 2
- Final adjustments
- Polish details
- Near-final
- **Runnable:** Final feedback

### Unit 235: Accessibility Review
- Control options
- Difficulty options
- Inclusive design
- **Runnable:** Accessible

### Unit 236: Documentation
- Instructions
- Controls
- Tips
- **Runnable:** Documented

### Unit 237: Credits
- Full credits
- Acknowledgements
- Thank you
- **Runnable:** Credits done

### Unit 238: Loading/Saving Polish
- Smooth loading
- Save reliability
- User experience
- **Runnable:** Load/save polish

### Unit 239: Final Build Prep
- Version number
- Build process
- Release ready
- **Runnable:** Build ready

### Unit 240: Phase 15 Integration
- Release quality
- Fully polished
- Professional game
- **Runnable:** Polished game

---

## Phase 16: Release (Units 241-256)
*Distribution and retrospective*

### Unit 241: Disk Mastering
- Create master disk
- Verify boot
- Distribution ready
- **Runnable:** Master disk

### Unit 242: Tape Version
- Tape distribution option
- Loader setup
- Tape master
- **Runnable:** Tape version

### Unit 243: Cartridge Consideration
- Cartridge feasibility
- ROM layout
- Alternative format
- **Runnable:** Cart evaluated

### Unit 244: Manual Creation
- Game manual
- Story/background
- Complete docs
- **Runnable:** Manual done

### Unit 245: Box Art Concept
- Cover design
- Retro aesthetic
- Marketing ready
- **Runnable:** Art concept

### Unit 246: Release Testing
- Final verification
- Multiple machines
- Release candidate
- **Runnable:** RC tested

### Unit 247: Distribution Package
- All files ready
- Documentation
- Complete package
- **Runnable:** Package ready

### Unit 248: Release Announcement
- Release notes
- Feature list
- Promotion
- **Runnable:** Announced

### Unit 249: Community Release
- Make available
- Gather reactions
- Support users
- **Runnable:** Released

### Unit 250: Post-Release Support
- Bug reports
- Quick fixes
- User assistance
- **Runnable:** Supported

### Unit 251: Multiplexer Documentation
- Document technique
- Reusable code
- Knowledge sharing
- **Runnable:** Documented

### Unit 252: Code Library
- Reusable modules
- Future games
- Asset library
- **Runnable:** Library created

### Unit 253: Retrospective
- What worked
- What didn't
- Lessons learned
- **Runnable:** Retrospective

### Unit 254: Skill Assessment
- Multiplexing mastery
- Raster expertise
- C64 proficiency
- **Runnable:** Skills assessed

### Unit 255: Future Planning
- Next game prep
- Apply learnings
- Continued growth
- **Runnable:** Future planned

### Unit 256: Course Completion
- Sprite Storm complete
- Multiplexing mastered
- Ready for more
- **Runnable:** Complete

---

## Technical Summary

### Key C64 Features Used
- Sprite multiplexing (8→32 sprites)
- Raster interrupts and chaining
- Y-sorted sprite allocation
- Cycle-exact timing
- VIC-II sprite registers
- SID audio integration

### Code Patterns Introduced
```asm
; Y-sorted sprite multiplexer core
multiplex_irq:
    pha
    txa
    pha

    ldx next_sprite_index
.reuse_loop:
    lda virtual_y,x
    cmp #$ff          ; End marker
    beq .done

    ldy slot_free     ; Get free hardware slot
    sta VIC_SPRITE_Y,y
    lda virtual_x,x
    sta VIC_SPRITE_X,y
    lda virtual_ptr,x
    sta SPRITE_PTRS,y

    inx
    ; Continue until next IRQ line
    lda virtual_y,x
    cmp next_irq_line
    bcc .reuse_loop

.done:
    stx next_sprite_index
    ; Set next IRQ
    pla
    tax
    pla
    asl $d019
    rti

; Bucket sort for Y positions
bucket_sort:
    ; Clear buckets
    ldx #0
    txa
.clear:
    sta bucket_count,x
    inx
    bne .clear

    ; Count per Y
    ldx #NUM_SPRITES-1
.count:
    ldy virtual_y,x
    inc bucket_count,y
    dex
    bpl .count

    ; Distribute to sorted list
    ; ...
    rts
```

### Skills Progression
| Phase | Primary Skills |
|-------|---------------|
| 1-2 | Sprites, raster interrupts |
| 3-4 | Multiplexing techniques |
| 5-6 | Arena gameplay, audio |
| 7-8 | Bosses, game modes |
| 9-10 | Advanced multiplexing, AI |
| 11-12 | Weapons, boss systems |
| 13-14 | Content, optimisation |
| 15-16 | Polish, release |

---

## Version History
- v1.0 - Initial 256-unit outline
