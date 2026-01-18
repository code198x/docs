# Game 9: Blitz - Complete 256-Unit Outline

## Game Overview
**Platform:** Sinclair ZX Spectrum
**Genre:** Side-scrolling shooter
**Concept:** Horizontal scrolling shooter on hardware with NO scroll support. Everything is software - shifting every byte. Master THE hardest Spectrum technique while building a complete R-Type style shooter.

**Technical Focus:**
- Software horizontal scrolling
- Pixel-level scroll (not just character)
- Unrolled/self-modifying scroll routines
- Contended memory timing
- Attribute clash management during scroll
- Tile map level streaming

---

## Phase 1: Foundation (Units 1-16)
*Static shooter foundation*

### Unit 1: Project Setup
- Side-scroller concept
- Memory layout planning
- No scrolling yet
- **Runnable:** Clean startup

### Unit 2: Display Setup
- Screen mode selection
- Play area definition
- Border colour
- **Runnable:** Display ready

### Unit 3: Player Ship Design
- Ship sprite graphics
- UDG or sprite routine
- Clear visuals
- **Runnable:** Ship graphics

### Unit 4: Draw Player
- Display ship on screen
- Fixed position for now
- XOR or masked
- **Runnable:** Ship displayed

### Unit 5: Player Movement
- Vertical movement only
- Joystick/keyboard
- Screen bounds
- **Runnable:** Ship moves

### Unit 6: Static Background
- Background graphics
- Stars or pattern
- Play area filled
- **Runnable:** Background drawn

### Unit 7: Enemy Design
- Basic enemy sprite
- Simple graphics
- Clear silhouette
- **Runnable:** Enemy graphics

### Unit 8: Static Enemies
- Place enemies on screen
- Fixed positions
- Multiple enemies
- **Runnable:** Enemies displayed

### Unit 9: Enemy Movement
- Move left towards player
- Simple patterns
- Wraparound or respawn
- **Runnable:** Enemies move

### Unit 10: Shooting Basics
- Fire button
- Projectile sprite
- Move right
- **Runnable:** Player shoots

### Unit 11: Projectile Collision
- Bullet vs enemy
- Simple collision
- Enemy destroyed
- **Runnable:** Enemies destroyed

### Unit 12: Player Collision
- Enemy vs player
- Death detection
- Game over trigger
- **Runnable:** Player can die

### Unit 13: Score System
- Points per kill
- Score display
- Simple HUD
- **Runnable:** Scoring works

### Unit 14: Lives System
- Three lives
- Lives display
- Respawn
- **Runnable:** Lives work

### Unit 15: Game Loop
- Title, game, game over
- State machine
- Complete flow
- **Runnable:** Game loop

### Unit 16: Phase 1 Integration
- Static shooter complete
- No scrolling yet
- Foundation solid
- **Runnable:** Static shooter

---

## Phase 2: Character Scrolling (Units 17-32)
*Coarse scrolling first*

### Unit 17: Scroll Concept
- No hardware scroll
- Must move bytes
- Character vs pixel
- **Runnable:** Concept understood

### Unit 18: Screen Memory Layout
- Display file structure
- Third layout
- Address calculation
- **Runnable:** Layout documented

### Unit 19: Character Scroll Left
- Move one character
- LDIR approach
- Whole screen
- **Runnable:** Character scroll

### Unit 20: Scroll Timing
- Measure cycles
- Too slow?
- Optimisation needed
- **Runnable:** Timing measured

### Unit 21: Unrolled Scroll
- Unroll the loop
- Faster execution
- More code size
- **Runnable:** Faster scroll

### Unit 22: Attribute Scroll
- Move attributes too
- Colour follows
- Synced scroll
- **Runnable:** Attributes scroll

### Unit 23: Right Edge Update
- New column appears
- Draw from map data
- Seamless edge
- **Runnable:** Edge updates

### Unit 24: Tile Map Basics
- Level as tile map
- Tile definitions
- Map data format
- **Runnable:** Tile map defined

### Unit 25: Map Streaming
- Load map as needed
- Column by column
- Memory efficient
- **Runnable:** Map streams

### Unit 26: Player in Scroll
- Player moves with world
- Relative position
- Stay on screen
- **Runnable:** Player stable

### Unit 27: Enemies in Scroll
- Enemies scroll with world
- World coordinates
- Screen position calc
- **Runnable:** Enemies scroll

### Unit 28: Scroll Speed
- Consistent speed
- Frame-based timing
- Smooth motion
- **Runnable:** Consistent scroll

### Unit 29: Flicker Reduction
- Draw during retrace
- Minimise tear
- Cleaner display
- **Runnable:** Less flicker

### Unit 30: Character Scroll Polish
- Smooth operation
- Stable enemies
- Working shooter
- **Runnable:** Polish pass

### Unit 31: Performance Check
- Current frame rate
- Cycle budget
- Pixel scroll room?
- **Runnable:** Performance known

### Unit 32: Phase 2 Integration
- Character scrolling works
- Tile map streaming
- Foundation for pixel
- **Runnable:** Character scroll game

---

## Phase 3: Pixel Scrolling (Units 33-48)
*Sub-character smooth scroll*

### Unit 33: Pixel Scroll Concept
- 8 pixel steps
- Shift bits within bytes
- Much harder
- **Runnable:** Concept clear

### Unit 34: Single Line Shift
- Shift one line left
- Carry between bytes
- Bit operations
- **Runnable:** Line shifts

### Unit 35: Screen Line Shift
- All 192 lines
- Very slow naive
- Need optimisation
- **Runnable:** Screen shifts

### Unit 36: ROL/RR Chain
- Carry propagation
- Efficient shifting
- Z80 approach
- **Runnable:** Efficient shift

### Unit 37: Unrolled Pixel Scroll
- Unroll completely
- No loops
- Maximum speed
- **Runnable:** Unrolled shift

### Unit 38: Self-Modifying Scroll
- Modify addresses
- Modify shift counts
- Dynamic code
- **Runnable:** Self-mod scroll

### Unit 39: Scroll Buffer
- Off-screen buffer
- Scroll buffer, copy to screen
- Double buffer lite
- **Runnable:** Buffered scroll

### Unit 40: Pixel Counter
- Track sub-pixel
- 0-7 pixel position
- Character on overflow
- **Runnable:** Pixel tracking

### Unit 41: Combined Scroll
- Pixel + character
- Seamless combination
- Full smooth scroll
- **Runnable:** Full smooth scroll

### Unit 42: Contended Memory
- ULA steals cycles
- Timing varies
- Work around it
- **Runnable:** Contention handled

### Unit 43: Optimal Memory Use
- Avoid contended
- Use uncontended RAM
- Faster execution
- **Runnable:** Memory optimised

### Unit 44: Stack Trick Scroll
- PUSH/POP scrolling
- Fastest method
- SP manipulation
- **Runnable:** Stack scroll

### Unit 45: Attribute Sync
- Attributes at character boundary
- Manage clash
- Acceptable visuals
- **Runnable:** Attribute managed

### Unit 46: Scroll Speed Options
- Multiple speeds
- Variable rate
- Gameplay control
- **Runnable:** Speed control

### Unit 47: Performance Verify
- Stable frame rate
- Smooth scrolling
- Playable game
- **Runnable:** Performance stable

### Unit 48: Phase 3 Integration
- Pixel-smooth scrolling
- Optimised routines
- Ready for game
- **Runnable:** Pixel scroll complete

---

## Phase 4: Scrolling Shooter (Units 49-64)
*Complete scrolling gameplay*

### Unit 49: Player in Pixel Scroll
- Player position
- Smooth with scroll
- No judder
- **Runnable:** Smooth player

### Unit 50: Player Full Movement
- 8-way movement
- Free positioning
- Scroll-relative
- **Runnable:** Full movement

### Unit 51: Scrolling Collision
- Collision in scroll world
- World coordinates
- Accurate detection
- **Runnable:** Scroll collision

### Unit 52: Terrain Tiles
- Solid terrain
- Collision tiles
- Level hazards
- **Runnable:** Terrain defined

### Unit 53: Terrain Collision
- Player vs terrain
- Instant death
- Navigate carefully
- **Runnable:** Terrain kills

### Unit 54: Enemy Spawning
- Spawn from map data
- Triggered by scroll
- World positions
- **Runnable:** Map-based spawn

### Unit 55: Enemy Patterns
- Movement patterns
- Sine waves
- Attack runs
- **Runnable:** Enemy patterns

### Unit 56: Enemy Bullets
- Enemies shoot
- Aimed or pattern
- Player danger
- **Runnable:** Enemy fire

### Unit 57: Bullet Management
- Bullet pooling
- Many bullets
- Performance managed
- **Runnable:** Bullet pool

### Unit 58: Power-Up Items
- Weapon upgrades
- Speed boosts
- Shields
- **Runnable:** Power-ups

### Unit 59: Power-Up Effects
- Visual feedback
- Weapon change
- Stat modification
- **Runnable:** Power-up effects

### Unit 60: Score Integration
- Points for kills
- Bonus items
- Score display
- **Runnable:** Scoring complete

### Unit 61: Lives and Continues
- Life system
- Continue option
- Fair difficulty
- **Runnable:** Lives system

### Unit 62: Level End
- Level completion
- Boss trigger
- Transition
- **Runnable:** Level end

### Unit 63: Inter-Level
- Score tally
- Brief break
- Next level prep
- **Runnable:** Between levels

### Unit 64: Phase 4 Integration
- Complete scrolling shooter
- All mechanics
- Full gameplay
- **Runnable:** Scrolling shooter

---

## Phase 5: Level Design (Units 65-80)
*Content and stages*

### Unit 65: Level 1 Design
- First level map
- Gentle introduction
- Learn mechanics
- **Runnable:** Level 1

### Unit 66: Level 1 Enemies
- Enemy placement
- Fair difficulty
- Learning curve
- **Runnable:** Level 1 enemies

### Unit 67: Level 1 Polish
- Visual consistency
- Flow tuning
- Complete level
- **Runnable:** Level 1 complete

### Unit 68: Level 2 Design
- Second level map
- New terrain type
- Increased challenge
- **Runnable:** Level 2

### Unit 69: Level 2 Enemies
- New enemy types
- Harder patterns
- More bullets
- **Runnable:** Level 2 enemies

### Unit 70: Level 2 Polish
- Visual theme
- Difficulty balance
- Complete level
- **Runnable:** Level 2 complete

### Unit 71: Level 3 Design
- Third level
- Complex terrain
- Technical challenge
- **Runnable:** Level 3

### Unit 72: Level 3 Enemies
- Elite enemies
- Swarm tactics
- Bullet patterns
- **Runnable:** Level 3 enemies

### Unit 73: Level 3 Polish
- Theme consistency
- Fair challenge
- Complete level
- **Runnable:** Level 3 complete

### Unit 74: Level 4 Design
- Fourth level
- Near-end difficulty
- Mastery required
- **Runnable:** Level 4

### Unit 75: Level 4 Enemies
- All enemy types
- Complex waves
- Intense action
- **Runnable:** Level 4 enemies

### Unit 76: Level 4 Polish
- Climactic feel
- High tension
- Complete level
- **Runnable:** Level 4 complete

### Unit 77: Level 5 Design
- Final level
- Ultimate challenge
- Everything combined
- **Runnable:** Level 5

### Unit 78: Level 5 Enemies
- Hardest enemies
- Boss gauntlet
- Final test
- **Runnable:** Level 5 enemies

### Unit 79: Level 5 Polish
- Epic finale
- Maximum intensity
- Complete level
- **Runnable:** Level 5 complete

### Unit 80: Phase 5 Integration
- Five complete levels
- Progression curve
- Full campaign
- **Runnable:** All levels

---

## Phase 6: Boss Battles (Units 81-96)
*Epic boss encounters*

### Unit 81: Boss Concept
- Large multi-part boss
- Level-end challenge
- Pattern-based
- **Runnable:** Boss design

### Unit 82: Boss Graphics
- Large boss sprite
- Multiple parts
- Imposing presence
- **Runnable:** Boss graphics

### Unit 83: Boss 1 Design
- First boss
- Simple patterns
- Learn boss mechanics
- **Runnable:** Boss 1 design

### Unit 84: Boss 1 Attacks
- Attack patterns
- Bullet spreads
- Avoidable attacks
- **Runnable:** Boss 1 attacks

### Unit 85: Boss 1 Vulnerability
- Weak point
- Damage feedback
- Health system
- **Runnable:** Boss 1 damageable

### Unit 86: Boss 1 Complete
- Full boss fight
- Victory condition
- Satisfying defeat
- **Runnable:** Boss 1 complete

### Unit 87: Boss 2 Design
- Second boss
- Different style
- New patterns
- **Runnable:** Boss 2 design

### Unit 88: Boss 2 Attacks
- Unique attacks
- Complex patterns
- Greater challenge
- **Runnable:** Boss 2 attacks

### Unit 89: Boss 2 Complete
- Full boss 2 fight
- Harder than boss 1
- Complete encounter
- **Runnable:** Boss 2 complete

### Unit 90: Boss 3-4 Design
- Mid-game bosses
- Varied mechanics
- Different approaches
- **Runnable:** Bosses 3-4 design

### Unit 91: Boss 3-4 Complete
- Both bosses done
- Tested and balanced
- Complete encounters
- **Runnable:** Bosses 3-4 complete

### Unit 92: Final Boss Design
- Ultimate boss
- Multiple phases
- Epic scale
- **Runnable:** Final boss design

### Unit 93: Final Boss Phases
- Phase transitions
- Escalating danger
- True finale
- **Runnable:** Final boss phases

### Unit 94: Final Boss Complete
- Complete final boss
- Satisfying conclusion
- Game-ending fight
- **Runnable:** Final boss complete

### Unit 95: Boss Polish
- All bosses refined
- Fair patterns
- Great encounters
- **Runnable:** Bosses polished

### Unit 96: Phase 6 Integration
- Five bosses complete
- One per level
- Epic encounters
- **Runnable:** All bosses

---

## Phase 7: Audio & Effects (Units 97-112)
*Sound and visual polish*

### Unit 97: Beeper Audio Setup
- 1-bit audio system
- Effect framework
- Trigger system
- **Runnable:** Audio ready

### Unit 98: Shoot Sound
- Player fire
- Satisfying effect
- Quick playback
- **Runnable:** Shoot sound

### Unit 99: Explosion Sound
- Enemy destruction
- Impact effect
- Variety
- **Runnable:** Explosion sound

### Unit 100: Power-Up Sound
- Collection jingle
- Positive feedback
- Distinctive
- **Runnable:** Power-up sound

### Unit 101: Death Sound
- Player death
- Dramatic effect
- Clear feedback
- **Runnable:** Death sound

### Unit 102: Boss Music
- Boss encounter music
- Beeper music
- Tension building
- **Runnable:** Boss music

### Unit 103: Title Music
- Title screen tune
- Catchy melody
- Sets mood
- **Runnable:** Title music

### Unit 104: AY Sound Option
- 128K AY support
- Better audio
- Enhanced version
- **Runnable:** AY option

### Unit 105: Explosion Animation
- Visual explosion
- Frame animation
- Satisfying destruction
- **Runnable:** Explosions

### Unit 106: Power-Up Animation
- Item collection
- Visual feedback
- Clear indication
- **Runnable:** Power-up animation

### Unit 107: Player Effects
- Shield visual
- Weapon change
- Status feedback
- **Runnable:** Player effects

### Unit 108: Boss Effects
- Boss damage flash
- Phase transition
- Dramatic effects
- **Runnable:** Boss effects

### Unit 109: Screen Flash
- Impact feedback
- Boss attacks
- Dramatic moments
- **Runnable:** Screen flash

### Unit 110: Colour Cycling
- Animated colours
- Background effects
- Visual interest
- **Runnable:** Colour cycling

### Unit 111: Starfield Background
- Parallax stars
- Multiple speeds
- Depth illusion
- **Runnable:** Starfield

### Unit 112: Phase 7 Integration
- Full audio
- Visual effects
- Polished presentation
- **Runnable:** Audio/effects complete

---

## Phase 8: Weapons & Power-Ups (Units 113-128)
*Weapon variety and upgrades*

### Unit 113: Weapon System
- Multiple weapons
- Switch system
- Current weapon
- **Runnable:** Weapon system

### Unit 114: Standard Shot
- Default weapon
- Reliable
- Upgradeable
- **Runnable:** Standard shot

### Unit 115: Spread Shot
- Multi-direction
- Area coverage
- Power-up weapon
- **Runnable:** Spread shot

### Unit 116: Laser Weapon
- Piercing beam
- Through enemies
- High damage
- **Runnable:** Laser

### Unit 117: Missiles
- Seeking missiles
- Homing ability
- Limited ammo
- **Runnable:** Missiles

### Unit 118: Weapon Levels
- Upgrade levels
- Increasing power
- Visual change
- **Runnable:** Weapon levels

### Unit 119: Speed Power-Up
- Movement speed
- Cumulative
- Visual indicator
- **Runnable:** Speed

### Unit 120: Shield Power-Up
- Damage absorption
- Limited hits
- Visual shield
- **Runnable:** Shield

### Unit 121: Option Drones
- Following drones
- Additional firepower
- R-Type style
- **Runnable:** Options

### Unit 122: Bomb Weapon
- Screen clear
- Limited use
- Emergency
- **Runnable:** Bombs

### Unit 123: Power-Up Balance
- Drop rates
- Weapon balance
- Fair economy
- **Runnable:** Balanced

### Unit 124: Power-Up Spawning
- Where drops appear
- When to drop
- Fair distribution
- **Runnable:** Spawn balanced

### Unit 125: Weapon Visuals
- Each weapon distinct
- Clear feedback
- Easy recognition
- **Runnable:** Weapon visuals

### Unit 126: HUD Updates
- Show current weapon
- Show level
- Show options
- **Runnable:** HUD complete

### Unit 127: Weapon Polish
- All weapons feel good
- Balanced power
- Fun to use
- **Runnable:** Weapons polished

### Unit 128: Phase 8 Integration
- Complete weapon system
- Multiple power-ups
- Varied gameplay
- **Runnable:** Weapons complete

---

## Phase 9: Advanced Scrolling (Units 129-144)
*Scroll technique mastery*

### Unit 129: Scroll Review
- Current implementation
- Performance analysis
- Improvement areas
- **Runnable:** Review done

### Unit 130: Faster Pixel Scroll
- More optimisation
- Squeeze cycles
- Maximum speed
- **Runnable:** Faster scroll

### Unit 131: Multi-Speed Scroll
- Variable scroll speed
- Slow/fast sections
- Dramatic effect
- **Runnable:** Variable speed

### Unit 132: Scroll Direction Changes
- Slow down
- Speed up
- Stop sections
- **Runnable:** Direction changes

### Unit 133: Vertical Scroll Prep
- Y scrolling concept
- Different challenges
- Future use
- **Runnable:** V-scroll concept

### Unit 134: Parallax Layer
- Background layer
- Slower scroll
- Depth illusion
- **Runnable:** Parallax

### Unit 135: Attribute Tricks
- Attribute-only effects
- Colour changes
- Fast updates
- **Runnable:** Attribute effects

### Unit 136: Split Screen
- Fixed HUD area
- Scrolling game area
- Split rendering
- **Runnable:** Split screen

### Unit 137: Optimised Tile Draw
- Faster tile drawing
- Edge updates
- Efficient rendering
- **Runnable:** Fast tiles

### Unit 138: Map Compression
- Compress level data
- RLE or similar
- Memory savings
- **Runnable:** Compressed maps

### Unit 139: Large Levels
- Longer levels
- More content
- Memory managed
- **Runnable:** Large levels

### Unit 140: Scroll Smoothness
- Eliminate judder
- Consistent timing
- Perfect scroll
- **Runnable:** Smooth scroll

### Unit 141: 128K Scroll
- Use extra RAM
- Double buffer
- Enhanced version
- **Runnable:** 128K scroll

### Unit 142: Frame Rate Lock
- Consistent 25/50 fps
- No slowdown
- Stable gameplay
- **Runnable:** Locked rate

### Unit 143: Scroll Documentation
- Document techniques
- Reusable code
- Knowledge capture
- **Runnable:** Documented

### Unit 144: Phase 9 Integration
- Advanced scrolling
- Maximum performance
- Professional quality
- **Runnable:** Scroll mastered

---

## Phase 10: Advanced Enemies (Units 145-160)
*Complex enemy systems*

### Unit 145: Enemy Framework
- Behaviour system
- Multiple types
- Modular design
- **Runnable:** Enemy framework

### Unit 146: Wave Enemies
- Sine wave motion
- Classic shooter pattern
- Swooping attack
- **Runnable:** Wave enemies

### Unit 147: Formation Enemies
- Group movement
- Break formation
- Attack pattern
- **Runnable:** Formations

### Unit 148: Turret Enemies
- Stationary shooter
- Aimed fire
- Terrain mounted
- **Runnable:** Turrets

### Unit 149: Chase Enemies
- Follow player
- Pursuit AI
- Aggressive
- **Runnable:** Chasers

### Unit 150: Heavy Enemies
- More health
- Bigger target
- Dangerous
- **Runnable:** Heavy enemies

### Unit 151: Speed Enemies
- Fast movement
- Quick attack
- Hard to hit
- **Runnable:** Speed enemies

### Unit 152: Spawner Enemies
- Create smaller enemies
- Priority target
- Strategic element
- **Runnable:** Spawners

### Unit 153: Shield Enemies
- Directional shield
- Weak point
- Requires skill
- **Runnable:** Shielded

### Unit 154: Split Enemies
- Split on death
- Chain reaction
- Risk/reward
- **Runnable:** Splitters

### Unit 155: Bullet Patterns
- Complex bullet patterns
- Danmaku lite
- Avoidance challenge
- **Runnable:** Bullet patterns

### Unit 156: Enemy Coordination
- Group AI
- Coordinated attacks
- Pack tactics
- **Runnable:** Coordination

### Unit 157: Elite Variants
- Colour variations
- Stronger versions
- Late game
- **Runnable:** Elite enemies

### Unit 158: Enemy Variety Pass
- Balance enemy mix
- Interesting waves
- Varied gameplay
- **Runnable:** Variety balanced

### Unit 159: Enemy Polish
- All enemies refined
- Good visual feedback
- Fair to fight
- **Runnable:** Enemies polished

### Unit 160: Phase 10 Integration
- 12+ enemy types
- Complex behaviours
- Rich combat
- **Runnable:** Enemies complete

---

## Phase 11: Game Modes (Units 161-176)
*Modes and replayability*

### Unit 161: Normal Mode
- Standard campaign
- Five levels
- Default experience
- **Runnable:** Normal mode

### Unit 162: Easy Mode
- Reduced difficulty
- More lives
- Slower enemies
- **Runnable:** Easy mode

### Unit 163: Hard Mode
- Increased difficulty
- Faster enemies
- More bullets
- **Runnable:** Hard mode

### Unit 164: Boss Rush
- Bosses only
- Quick mode
- Practice/challenge
- **Runnable:** Boss rush

### Unit 165: Score Attack
- High score focus
- Single credit
- Leaderboard
- **Runnable:** Score attack

### Unit 166: Time Attack
- Speed completion
- Timer display
- Fastest time
- **Runnable:** Time attack

### Unit 167: Endless Mode
- Infinite waves
- Survival focus
- How long can you last
- **Runnable:** Endless mode

### Unit 168: Practice Mode
- Select level
- Select boss
- Skill building
- **Runnable:** Practice

### Unit 169: Two-Player Mode
- Alternating turns
- Competitive score
- Social play
- **Runnable:** Two-player

### Unit 170: High Score Table
- Top 10 scores
- Name entry
- Per-mode scores
- **Runnable:** High scores

### Unit 171: Save System
- Save progress
- Save high scores
- 128K tape save
- **Runnable:** Save system

### Unit 172: Options Menu
- Difficulty select
- Controls config
- Sound options
- **Runnable:** Options

### Unit 173: Statistics
- Games played
- Enemies killed
- Time played
- **Runnable:** Statistics

### Unit 174: Achievements
- Track accomplishments
- Skill challenges
- Completion goals
- **Runnable:** Achievements

### Unit 175: Mode Polish
- All modes refined
- Consistent quality
- Good variety
- **Runnable:** Modes polished

### Unit 176: Phase 11 Integration
- Multiple game modes
- High replayability
- Rich content
- **Runnable:** Modes complete

---

## Phase 12: 128K Enhancement (Units 177-192)
*128K Spectrum features*

### Unit 177: 128K Detection
- Detect 128K
- Feature toggle
- Graceful fallback
- **Runnable:** Detection

### Unit 178: Extra RAM Usage
- Use extra banks
- Level storage
- Asset storage
- **Runnable:** Extra RAM

### Unit 179: Bank Switching
- Page RAM banks
- Asset loading
- Efficient use
- **Runnable:** Bank switching

### Unit 180: AY Sound Effects
- 128K sound effects
- Better audio
- Three channels
- **Runnable:** AY SFX

### Unit 181: AY Music
- Full music tracks
- In-game music
- Professional audio
- **Runnable:** AY music

### Unit 182: Enhanced Graphics
- More tile variety
- Extra sprites
- Visual upgrade
- **Runnable:** Enhanced graphics

### Unit 183: More Levels
- Additional levels
- 128K exclusive
- Extended game
- **Runnable:** More levels

### Unit 184: Better Scrolling
- Double buffer
- Smoother scroll
- No flicker
- **Runnable:** Better scroll

### Unit 185: More Enemies
- Additional types
- 128K exclusive
- More variety
- **Runnable:** More enemies

### Unit 186: More Bosses
- Additional bosses
- Extended campaign
- More content
- **Runnable:** More bosses

### Unit 187: Enhanced Effects
- Better explosions
- More particles
- Visual upgrade
- **Runnable:** Better effects

### Unit 188: 128K Polish
- All enhancements
- Cohesive experience
- Premium version
- **Runnable:** 128K polished

### Unit 189: 48K Verification
- Test 48K version
- Still complete
- Still fun
- **Runnable:** 48K verified

### Unit 190: Feature Comparison
- Document differences
- Clear messaging
- User expectation
- **Runnable:** Comparison

### Unit 191: 128K Testing
- Full 128K test
- All features
- Stable
- **Runnable:** 128K tested

### Unit 192: Phase 12 Integration
- Complete 128K version
- Enhanced experience
- Both versions solid
- **Runnable:** 128K complete

---

## Phase 13: Optimisation (Units 193-208)
*Maximum performance*

### Unit 193: Performance Audit
- Profile all systems
- Find bottlenecks
- Prioritise
- **Runnable:** Audit done

### Unit 194: Scroll Final Optimisation
- Last scroll speed gains
- Every cycle counts
- Maximum speed
- **Runnable:** Scroll optimised

### Unit 195: Sprite Optimisation
- Faster sprite drawing
- Clipping optimised
- Efficient rendering
- **Runnable:** Sprites optimised

### Unit 196: Collision Optimisation
- Faster collision
- Early exit
- Spatial checks
- **Runnable:** Collision optimised

### Unit 197: Enemy AI Optimisation
- Faster AI
- Batch processing
- Efficient updates
- **Runnable:** AI optimised

### Unit 198: Memory Optimisation
- Reduce memory use
- Efficient storage
- Room for content
- **Runnable:** Memory optimised

### Unit 199: Loading Optimisation
- Faster loading
- Turbo loader
- Quick start
- **Runnable:** Fast loading

### Unit 200: Frame Rate Stability
- Rock solid frame rate
- No drops ever
- Consistent feel
- **Runnable:** Stable rate

### Unit 201: Worst Case Testing
- Maximum enemies
- Maximum bullets
- Stress test
- **Runnable:** Stress tested

### Unit 202: Memory Map Final
- Final memory layout
- Optimal placement
- Documented
- **Runnable:** Memory final

### Unit 203: Code Size Optimisation
- Reduce code size
- Fit more content
- Efficient code
- **Runnable:** Code optimised

### Unit 204: Data Optimisation
- Compress data
- Efficient formats
- Space savings
- **Runnable:** Data optimised

### Unit 205: Load Distribution
- Even CPU load
- Spread work
- Smooth performance
- **Runnable:** Load balanced

### Unit 206: Final Performance
- All optimisations
- Best possible performance
- Production quality
- **Runnable:** Performance final

### Unit 207: Performance Documentation
- Document techniques
- Cycle counts
- Knowledge capture
- **Runnable:** Documented

### Unit 208: Phase 13 Integration
- Maximum performance
- Optimised code
- Fast and smooth
- **Runnable:** Optimised game

---

## Phase 14: Polish (Units 209-224)
*Final quality pass*

### Unit 209: Visual Polish Pass
- All graphics reviewed
- Consistent style
- Professional look
- **Runnable:** Visual polish

### Unit 210: Audio Polish Pass
- All sounds balanced
- Music levels
- Clean audio
- **Runnable:** Audio polish

### Unit 211: Gameplay Polish
- Feel refinement
- Control tweaks
- Satisfying play
- **Runnable:** Gameplay polish

### Unit 212: Difficulty Polish
- Fair progression
- Learnable patterns
- Achievable challenge
- **Runnable:** Difficulty polish

### Unit 213: UI Polish
- Clean menus
- Clear text
- Easy navigation
- **Runnable:** UI polish

### Unit 214: Bug Hunt
- Systematic testing
- Find all bugs
- Fix everything
- **Runnable:** Bug-free

### Unit 215: Playtest Round 1
- External testers
- Fresh eyes
- Gather feedback
- **Runnable:** Playtest 1

### Unit 216: Feedback Integration 1
- Address issues
- Improve weak areas
- Iterate
- **Runnable:** Feedback 1

### Unit 217: Playtest Round 2
- More testing
- Verify fixes
- Final feedback
- **Runnable:** Playtest 2

### Unit 218: Feedback Integration 2
- Final changes
- Polish details
- Near-final
- **Runnable:** Feedback 2

### Unit 219: Accessibility
- Control options
- Difficulty options
- Inclusive
- **Runnable:** Accessible

### Unit 220: Instructions
- How to play
- Controls
- Tips
- **Runnable:** Instructions

### Unit 221: Credits
- Full credits
- Acknowledgements
- Thank you
- **Runnable:** Credits

### Unit 222: Title Screen Final
- Polished title
- All options
- Professional
- **Runnable:** Title final

### Unit 223: Game Over Screen
- Final game over
- Score display
- Replay option
- **Runnable:** Game over final

### Unit 224: Phase 14 Integration
- Fully polished
- Professional quality
- Release candidate
- **Runnable:** Polished game

---

## Phase 15: Testing & QA (Units 225-240)
*Thorough testing*

### Unit 225: Full Playthrough 48K
- Complete game
- 48K version
- Start to finish
- **Runnable:** 48K playthrough

### Unit 226: Full Playthrough 128K
- Complete game
- 128K version
- All enhancements
- **Runnable:** 128K playthrough

### Unit 227: All Modes Test
- Every game mode
- Full coverage
- All working
- **Runnable:** Modes tested

### Unit 228: All Weapons Test
- Every weapon
- All levels
- All working
- **Runnable:** Weapons tested

### Unit 229: All Enemies Test
- Every enemy type
- All behaviours
- Working correctly
- **Runnable:** Enemies tested

### Unit 230: All Bosses Test
- Every boss
- All phases
- Defeatable
- **Runnable:** Bosses tested

### Unit 231: Edge Case Testing
- Unusual situations
- Corner cases
- Robust game
- **Runnable:** Edge cases

### Unit 232: Memory Stress Test
- Maximum usage
- No corruption
- Stable
- **Runnable:** Memory tested

### Unit 233: Long Session Test
- Extended play
- Memory leaks
- Stability
- **Runnable:** Long session

### Unit 234: Multiple Machine Test
- Different Spectrums
- 48K/128K/+2/+3
- Compatibility
- **Runnable:** Multi-machine

### Unit 235: Emulator Testing
- Multiple emulators
- Compatibility
- Accurate behaviour
- **Runnable:** Emulator tested

### Unit 236: Save/Load Testing
- Save reliability
- Load correctly
- Data integrity
- **Runnable:** Save tested

### Unit 237: Regression Testing
- Previous bugs
- Stay fixed
- No regressions
- **Runnable:** Regression tested

### Unit 238: Final Bug Fixes
- Last issues
- Complete fixes
- Clean build
- **Runnable:** Bugs fixed

### Unit 239: Sign-Off Testing
- Final verification
- Release ready
- Approved
- **Runnable:** Signed off

### Unit 240: Phase 15 Integration
- Thoroughly tested
- All issues resolved
- Production ready
- **Runnable:** Tested game

---

## Phase 16: Release (Units 241-256)
*Distribution and completion*

### Unit 241: Tape Mastering
- Create master tape
- Turbo loader
- Reliable loading
- **Runnable:** Tape master

### Unit 242: Disk Version
- +3 disk version
- Fast loading
- Disk distribution
- **Runnable:** Disk version

### Unit 243: TZX Creation
- Standard TZX format
- Preservation
- Emulator compatible
- **Runnable:** TZX created

### Unit 244: Snapshot Version
- SNA/Z80 snapshot
- Instant load
- Emulator friendly
- **Runnable:** Snapshot

### Unit 245: Manual Creation
- Game manual
- Instructions
- Story
- **Runnable:** Manual

### Unit 246: Cover Art
- Inlay design
- Retro aesthetic
- Professional look
- **Runnable:** Cover art

### Unit 247: Distribution Package
- All files
- All versions
- Complete package
- **Runnable:** Package ready

### Unit 248: Release Announcement
- Feature list
- Screenshots
- Promotion
- **Runnable:** Announced

### Unit 249: Community Release
- Make available
- Distribution
- User access
- **Runnable:** Released

### Unit 250: Post-Release Support
- Bug reports
- Quick fixes
- User help
- **Runnable:** Supported

### Unit 251: Scroll Code Release
- Share scroll routines
- Educational
- Community benefit
- **Runnable:** Code shared

### Unit 252: Technique Documentation
- Document all techniques
- Software scrolling guide
- Knowledge sharing
- **Runnable:** Documented

### Unit 253: Retrospective
- What worked
- Lessons learned
- Future improvements
- **Runnable:** Retrospective

### Unit 254: Skill Assessment
- Scroll mastery
- Spectrum expertise
- Professional skills
- **Runnable:** Skills assessed

### Unit 255: Future Planning
- Next project
- Apply learnings
- Continue growth
- **Runnable:** Future planned

### Unit 256: Course Completion
- Blitz complete
- Software scrolling mastered
- Ready for more
- **Runnable:** Complete

---

## Technical Summary

### Key Spectrum Features Used
- Software pixel scrolling
- Stack-based scroll tricks
- Self-modifying code
- Contended memory management
- Attribute clash handling
- 128K bank switching
- AY sound (128K)

### Code Patterns Introduced
```z80
; Pixel scroll left using stack
pixel_scroll_left:
    di
    ld (sp_store+1),sp
    ld sp,screen_end

    ; Unrolled scroll for speed
    pop hl
    ld a,l
    rla
    ld l,a
    ld a,h
    rla
    ld h,a
    push hl
    ; ... repeat for all screen

sp_store:
    ld sp,0
    ei
    ret

; Self-modifying tile draw
draw_tile:
    ld a,(tile_number)
    add a,a
    add a,a
    add a,a      ; x8 for tile data
    ld l,a
    ld h,tiles/256

    ; Modify LD instructions
    ld a,(hl)
    ld (line0+1),a
    inc hl
    ld a,(hl)
    ld (line1+1),a
    ; ... etc

    ; Execute modified code
line0:
    ld a,0
    ld (de),a
line1:
    ld a,0
    ; ...
    ret
```

### Skills Progression
| Phase | Primary Skills |
|-------|---------------|
| 1-2 | Static shooter, character scroll |
| 3-4 | Pixel scrolling, gameplay |
| 5-6 | Level design, bosses |
| 7-8 | Audio, weapons |
| 9-10 | Advanced scroll, enemies |
| 11-12 | Game modes, 128K |
| 13-14 | Optimisation, polish |
| 15-16 | Testing, release |

---

## Version History
- v1.0 - Initial 256-unit outline
