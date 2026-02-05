# Game 9: Ion Trail - Complete 256-Unit Outline

## Game Overview
**Platform:** Nintendo Entertainment System
**Genre:** Side-scrolling shooter (Gradius-style)
**Concept:** Horizontal scrolling shooter with Gradius-inspired power-up system. Options trail behind you, weapons upgrade through levels, and epic bosses await. The definitive NES shmup experience.

**Technical Focus:**
- Horizontal scrolling for shooters
- Option trail following algorithm
- Power-up progression system
- Complex boss patterns
- Sprite management for bullets
- Split screen (scrolling game, fixed HUD)

---

## Phase 1: Foundation (Units 1-16)
*Basic scrolling shooter setup*

### Unit 1: Project Setup
- Shmup project structure
- Memory layout
- Bank configuration
- **Runnable:** Clean startup

### Unit 2: Display Setup
- Background setup
- Sprite setup
- Palette selection
- **Runnable:** Display ready

### Unit 3: Scrolling Basics
- PPUSCROLL usage
- Horizontal scroll
- Smooth motion
- **Runnable:** Screen scrolls

### Unit 4: Nametable Setup
- Two nametables
- Scroll between them
- Seamless wrap
- **Runnable:** Nametables work

### Unit 5: Player Ship
- Ship sprite design
- Metasprite (2x2)
- Positioned on screen
- **Runnable:** Ship displayed

### Unit 6: Player Movement
- D-pad control
- 8-way movement
- Screen bounds
- **Runnable:** Ship moves

### Unit 7: Scroll-Relative Position
- Player in world space
- Camera following
- Relative positioning
- **Runnable:** Position correct

### Unit 8: Basic Shooting
- B button fires
- Bullet sprite
- Move right
- **Runnable:** Player shoots

### Unit 9: Bullet Management
- Bullet pool
- Spawn/despawn
- Active tracking
- **Runnable:** Bullet pool

### Unit 10: Static Enemy
- Enemy sprite
- Fixed position
- Collision target
- **Runnable:** Enemy displayed

### Unit 11: Enemy Collision
- Bullet hits enemy
- Destruction
- Remove both
- **Runnable:** Enemy destroyed

### Unit 12: Score System
- Points per kill
- Score counter
- Display prep
- **Runnable:** Scoring works

### Unit 13: Player Death
- Enemy collision
- Death state
- Life lost
- **Runnable:** Player dies

### Unit 14: Lives System
- Three lives
- Respawn
- Game over
- **Runnable:** Lives work

### Unit 15: Game Loop
- Title/game/over states
- State machine
- Flow complete
- **Runnable:** Game loop

### Unit 16: Phase 1 Integration
- Basic scrolling shooter
- Foundation complete
- Ready to expand
- **Runnable:** Basic shmup

---

## Phase 2: Scrolling System (Units 17-32)
*Advanced scrolling mechanics*

### Unit 17: Column Loading
- Load new column
- As scroll reveals
- Seamless world
- **Runnable:** Column loading

### Unit 18: Level Data Format
- Metatile-based
- Compressed data
- Efficient storage
- **Runnable:** Level format

### Unit 19: Tile Streaming
- Stream from ROM
- During scroll
- No hitches
- **Runnable:** Streaming

### Unit 20: Attribute Updates
- Attribute streaming
- Colour correct
- Synced with tiles
- **Runnable:** Attributes stream

### Unit 21: Split Screen
- Fixed HUD area
- Scrolling game area
- Sprite 0 split
- **Runnable:** Split screen

### Unit 22: HUD Design
- Score display
- Lives display
- Power meter
- **Runnable:** HUD displayed

### Unit 23: HUD Updates
- Score rendering
- Lives icons
- Real-time updates
- **Runnable:** HUD updates

### Unit 24: Scroll Speed Control
- Variable speed
- Slow/fast sections
- Level design tool
- **Runnable:** Speed control

### Unit 25: Enemy Spawning
- Spawn from level data
- Triggered by scroll
- World positions
- **Runnable:** Enemy spawning

### Unit 26: Enemy Movement
- Move patterns
- Scroll-relative
- Screen bounds
- **Runnable:** Enemies move

### Unit 27: Terrain Tiles
- Solid terrain
- Collision tiles
- Level hazards
- **Runnable:** Terrain defined

### Unit 28: Terrain Collision
- Ship vs terrain
- Instant death
- Careful navigation
- **Runnable:** Terrain kills

### Unit 29: Background Variety
- Multiple tile sets
- Visual themes
- Level identity
- **Runnable:** Visual variety

### Unit 30: Scroll Polish
- Smooth motion
- No glitches
- Professional scroll
- **Runnable:** Scroll polished

### Unit 31: Performance Check
- Sprite limits
- CPU budget
- Optimise if needed
- **Runnable:** Performance OK

### Unit 32: Phase 2 Integration
- Complete scroll system
- Level streaming
- Ready for gameplay
- **Runnable:** Scroll complete

---

## Phase 3: Power-Up System (Units 33-48)
*Gradius-style upgrade system*

### Unit 33: Power-Up Concept
- Gradius power bar
- Collect capsules
- Choose upgrade
- **Runnable:** Concept clear

### Unit 34: Power Capsule
- Capsule item
- Enemy drops
- Collection
- **Runnable:** Capsules drop

### Unit 35: Power Meter
- Selection bar
- Current position
- Visual display
- **Runnable:** Power meter

### Unit 36: Meter Advancement
- Collect to advance
- Cursor moves
- Clear feedback
- **Runnable:** Meter advances

### Unit 37: Speed Upgrade
- First option
- Faster movement
- Stacks twice
- **Runnable:** Speed up

### Unit 38: Missile Upgrade
- Second option
- Downward missiles
- Ground targets
- **Runnable:** Missiles

### Unit 39: Double Shot
- Third option
- Two-way fire
- Up and forward
- **Runnable:** Double

### Unit 40: Laser Upgrade
- Fourth option
- Powerful beam
- Replaces shot
- **Runnable:** Laser

### Unit 41: Option Drone
- Fifth option
- Following drone
- Additional firepower
- **Runnable:** Option

### Unit 42: Shield
- Sixth option
- Hit absorption
- Limited protection
- **Runnable:** Shield

### Unit 43: Power Selection
- A button selects
- Apply upgrade
- Reset meter
- **Runnable:** Selection works

### Unit 44: Upgrade Visuals
- Visual feedback
- Ship changes
- Clear indication
- **Runnable:** Upgrade visuals

### Unit 45: Power Balance
- Drop rates
- Capsule spawning
- Fair progression
- **Runnable:** Balanced

### Unit 46: Death Penalty
- Lose upgrades
- Start fresh
- High stakes
- **Runnable:** Death penalty

### Unit 47: Power-Up Polish
- Smooth interface
- Clear feedback
- Satisfying upgrades
- **Runnable:** Power polished

### Unit 48: Phase 3 Integration
- Complete Gradius-style system
- All upgrades
- Core mechanic
- **Runnable:** Power-ups complete

---

## Phase 4: Option System (Units 49-64)
*Following drone mechanics*

### Unit 49: Option Concept
- Following drones
- Trail behind ship
- Fire with player
- **Runnable:** Concept clear

### Unit 50: Option Sprite
- Option graphic
- Animated glow
- Distinct look
- **Runnable:** Option sprite

### Unit 51: Position Recording
- Record ship positions
- History buffer
- Trail data
- **Runnable:** Position history

### Unit 52: Follow Delay
- Options follow delayed
- Smooth trail
- Natural motion
- **Runnable:** Follow delay

### Unit 53: First Option
- Single option
- Follows correctly
- Fires bullets
- **Runnable:** One option

### Unit 54: Second Option
- Two options
- Spaced apart
- Both follow
- **Runnable:** Two options

### Unit 55: Third Option
- Maximum three
- (or four)
- Full complement
- **Runnable:** Three options

### Unit 56: Fourth Option
- Four options
- Maximum power
- Impressive display
- **Runnable:** Four options

### Unit 57: Option Firing
- Options shoot
- Sync with player
- Same weapon
- **Runnable:** Options fire

### Unit 58: Option Weapons
- Options use upgrades
- Laser options
- Spread options
- **Runnable:** Option weapons

### Unit 59: Option Formation
- Formation control
- Fixed or trailing
- Player choice
- **Runnable:** Formations

### Unit 60: Option Collision
- Options don't die
- Pass through
- Always active
- **Runnable:** Option invincible

### Unit 61: Option Limits
- Sprite limits
- Flicker management
- Performance
- **Runnable:** Limits managed

### Unit 62: Option Polish
- Smooth following
- Visual appeal
- Satisfying
- **Runnable:** Options polished

### Unit 63: Sprite Budget
- Player + options + bullets
- Manage limits
- No excessive flicker
- **Runnable:** Sprite budget

### Unit 64: Phase 4 Integration
- Complete option system
- Iconic mechanic
- Core gameplay
- **Runnable:** Options complete

---

## Phase 5: Enemy Design (Units 65-80)
*Varied enemy types*

### Unit 65: Enemy Framework
- Enemy data structure
- Type-based behaviour
- Spawn system
- **Runnable:** Framework

### Unit 66: Basic Fighter
- Standard enemy
- Straight flight
- Cannon fodder
- **Runnable:** Basic fighter

### Unit 67: Wave Fighter
- Sine wave motion
- Classic pattern
- Swooping attack
- **Runnable:** Wave fighter

### Unit 68: Dive Bomber
- Approach then dive
- Attack run
- Dangerous
- **Runnable:** Dive bomber

### Unit 69: Turret Enemy
- Stationary
- Aimed shots
- Terrain mounted
- **Runnable:** Turret

### Unit 70: Heavy Fighter
- More health
- Bigger target
- More points
- **Runnable:** Heavy fighter

### Unit 71: Speed Fighter
- Fast movement
- Quick pass
- Hard to hit
- **Runnable:** Speed fighter

### Unit 72: Spawner Enemy
- Releases smaller
- Priority target
- Strategic
- **Runnable:** Spawner

### Unit 73: Shield Enemy
- Frontal shield
- Weak from behind
- Requires position
- **Runnable:** Shield enemy

### Unit 74: Missile Enemy
- Fires homing
- Dangerous projectile
- Priority target
- **Runnable:** Missile enemy

### Unit 75: Formation Group
- Group movement
- Break and attack
- Coordinated
- **Runnable:** Formations

### Unit 76: Ground Target
- Terrain object
- Destructible
- Bonus points
- **Runnable:** Ground targets

### Unit 77: Capsule Carrier
- Drops power-up
- Important target
- Risk/reward
- **Runnable:** Carrier

### Unit 78: Enemy Bullets
- Enemy fire
- Various patterns
- Player danger
- **Runnable:** Enemy bullets

### Unit 79: Enemy Balance
- Health values
- Point values
- Fair challenge
- **Runnable:** Balanced

### Unit 80: Phase 5 Integration
- 12+ enemy types
- Varied challenge
- Rich combat
- **Runnable:** Enemies complete

---

## Phase 6: Level Design (Units 81-96)
*Stage creation*

### Unit 81: Stage 1 Concept
- Space setting
- Introduction
- Learn mechanics
- **Runnable:** Stage 1 concept

### Unit 82: Stage 1 Layout
- Tile design
- Enemy placement
- Terrain layout
- **Runnable:** Stage 1 layout

### Unit 83: Stage 1 Polish
- Visual refinement
- Balance tuning
- Complete stage
- **Runnable:** Stage 1 complete

### Unit 84: Stage 2 Concept
- New environment
- Harder challenge
- New enemies
- **Runnable:** Stage 2 concept

### Unit 85: Stage 2 Layout
- Different terrain
- Complex navigation
- More enemies
- **Runnable:** Stage 2 layout

### Unit 86: Stage 2 Polish
- Visual theme
- Difficulty curve
- Complete stage
- **Runnable:** Stage 2 complete

### Unit 87: Stage 3 Concept
- Mid-game challenge
- Technical terrain
- Mastery test
- **Runnable:** Stage 3 concept

### Unit 88: Stage 3 Layout
- Complex layout
- Heavy enemies
- Precision required
- **Runnable:** Stage 3 layout

### Unit 89: Stage 3 Polish
- Polish pass
- Fair difficulty
- Complete stage
- **Runnable:** Stage 3 complete

### Unit 90: Stage 4 Concept
- Late game
- Maximum challenge
- Expert play
- **Runnable:** Stage 4 concept

### Unit 91: Stage 4 Layout
- Dense enemies
- Tight terrain
- Intense action
- **Runnable:** Stage 4 layout

### Unit 92: Stage 4 Polish
- Final balance
- Near-end intensity
- Complete stage
- **Runnable:** Stage 4 complete

### Unit 93: Stage 5 Concept
- Final stage
- Ultimate test
- Boss gauntlet
- **Runnable:** Stage 5 concept

### Unit 94: Stage 5 Layout
- Epic finale
- All elements
- Lead to boss
- **Runnable:** Stage 5 layout

### Unit 95: Stage 5 Polish
- Maximum polish
- Climactic feel
- Complete stage
- **Runnable:** Stage 5 complete

### Unit 96: Phase 6 Integration
- Five complete stages
- Progressive difficulty
- Full campaign
- **Runnable:** Stages complete

---

## Phase 7: Boss Battles (Units 97-112)
*Epic boss encounters*

### Unit 97: Boss Framework
- Large enemy system
- Multi-sprite boss
- Health system
- **Runnable:** Boss framework

### Unit 98: Boss 1 Design
- First boss
- Simple patterns
- Intro boss
- **Runnable:** Boss 1 design

### Unit 99: Boss 1 Patterns
- Attack patterns
- Bullet spreads
- Fair attacks
- **Runnable:** Boss 1 patterns

### Unit 100: Boss 1 Complete
- Full encounter
- Satisfying defeat
- Stage 1 end
- **Runnable:** Boss 1 complete

### Unit 101: Boss 2 Design
- Second boss
- New mechanics
- Harder challenge
- **Runnable:** Boss 2 design

### Unit 102: Boss 2 Patterns
- Complex patterns
- Multiple phases
- Escalation
- **Runnable:** Boss 2 patterns

### Unit 103: Boss 2 Complete
- Full encounter
- Greater challenge
- Stage 2 end
- **Runnable:** Boss 2 complete

### Unit 104: Boss 3 Design
- Mid-game boss
- Unique mechanics
- Technical fight
- **Runnable:** Boss 3 design

### Unit 105: Boss 3 Complete
- Full encounter
- Skill test
- Stage 3 end
- **Runnable:** Boss 3 complete

### Unit 106: Boss 4 Design
- Late game boss
- Hard patterns
- Near-final
- **Runnable:** Boss 4 design

### Unit 107: Boss 4 Complete
- Full encounter
- Expert required
- Stage 4 end
- **Runnable:** Boss 4 complete

### Unit 108: Final Boss Design
- Ultimate boss
- Epic scale
- Multiple forms
- **Runnable:** Final boss design

### Unit 109: Final Boss Phase 1
- First form
- Learnable patterns
- Initial challenge
- **Runnable:** Final phase 1

### Unit 110: Final Boss Phase 2
- Second form
- Harder patterns
- Escalation
- **Runnable:** Final phase 2

### Unit 111: Final Boss Phase 3
- Final form
- Ultimate challenge
- True ending
- **Runnable:** Final phase 3

### Unit 112: Phase 7 Integration
- Five bosses complete
- Epic encounters
- Memorable fights
- **Runnable:** Bosses complete

---

## Phase 8: Audio (Units 113-128)
*Sound and music*

### Unit 113: Audio Setup
- APU configuration
- Sound system
- Channel allocation
- **Runnable:** Audio ready

### Unit 114: Shoot Sound
- Player fire
- Satisfying effect
- Pulse channel
- **Runnable:** Shoot sound

### Unit 115: Explosion Sound
- Destruction effect
- Noise channel
- Impact feel
- **Runnable:** Explosion

### Unit 116: Power-Up Sound
- Collection effect
- Positive feedback
- Distinctive
- **Runnable:** Power-up sound

### Unit 117: Player Death
- Death sound
- Dramatic effect
- Clear feedback
- **Runnable:** Death sound

### Unit 118: Boss Warning
- Boss approach
- Alert sound
- Tension build
- **Runnable:** Boss warning

### Unit 119: Music System
- Music player
- Multi-channel
- Pattern-based
- **Runnable:** Music system

### Unit 120: Title Music
- Title theme
- Catchy melody
- Sets mood
- **Runnable:** Title music

### Unit 121: Stage 1 Music
- First stage BGM
- Energetic
- Driving beat
- **Runnable:** Stage 1 music

### Unit 122: Stage 2-3 Music
- Mid-game BGM
- Different feel
- Variety
- **Runnable:** Mid music

### Unit 123: Stage 4-5 Music
- Late stage BGM
- Intense
- Climactic
- **Runnable:** Late music

### Unit 124: Boss Music
- Boss theme
- Tension
- Epic feel
- **Runnable:** Boss music

### Unit 125: Victory Music
- Stage clear
- Celebration
- Relief
- **Runnable:** Victory music

### Unit 126: Game Over Music
- Defeat theme
- Appropriate mood
- Motivating
- **Runnable:** Game over

### Unit 127: Audio Balance
- Mix levels
- No clipping
- Clear audio
- **Runnable:** Balanced audio

### Unit 128: Phase 8 Integration
- Complete audio
- Full soundtrack
- Professional sound
- **Runnable:** Audio complete

---

## Phase 9: Weapon Variety (Units 129-144)
*Expanded weapon systems*

### Unit 129: Weapon Review
- Current weapons
- Expansion plans
- Balance goals
- **Runnable:** Review done

### Unit 130: Shot Levels
- Upgrade levels
- Level 1-3 shot
- Progressive power
- **Runnable:** Shot levels

### Unit 131: Laser Levels
- Laser upgrades
- Thicker beam
- More damage
- **Runnable:** Laser levels

### Unit 132: Missile Types
- Homing missiles
- Photon torpedoes
- Variety
- **Runnable:** Missile types

### Unit 133: Special Weapons
- Screen-clear bomb
- Limited use
- Emergency
- **Runnable:** Special weapons

### Unit 134: Weapon Switching
- Multiple weapon slots
- Switch active
- Strategic choice
- **Runnable:** Weapon switch

### Unit 135: Charge Shot
- Hold to charge
- Powerful release
- Risk/reward
- **Runnable:** Charge shot

### Unit 136: Spread Upgrade
- Wide spread shot
- Area coverage
- Alternative
- **Runnable:** Spread

### Unit 137: Ripple Laser
- Wave beam
- Passes terrain
- Unique utility
- **Runnable:** Ripple laser

### Unit 138: Option Weapons
- Options match weapon
- Coordinated fire
- Maximum power
- **Runnable:** Option weapons

### Unit 139: Shield Upgrade
- Force field
- Block bullets
- Projectile shield
- **Runnable:** Force field

### Unit 140: Weapon Visuals
- Distinct graphics
- Clear feedback
- Visual variety
- **Runnable:** Weapon visuals

### Unit 141: Weapon Balance
- DPS balancing
- Situational use
- All viable
- **Runnable:** Balanced

### Unit 142: Power Meter Update
- Show all options
- Clear selection
- Updated UI
- **Runnable:** UI updated

### Unit 143: Weapon Polish
- All weapons feel good
- Satisfying use
- Fun variety
- **Runnable:** Weapons polished

### Unit 144: Phase 9 Integration
- Complete weapon variety
- Many options
- Strategic depth
- **Runnable:** Weapons expanded

---

## Phase 10: Advanced Enemies (Units 145-160)
*Complex enemy behaviors*

### Unit 145: AI Enhancement
- Smarter enemies
- Better patterns
- More challenge
- **Runnable:** Better AI

### Unit 146: Formation Attacks
- Coordinated waves
- Group patterns
- Impressive display
- **Runnable:** Formations

### Unit 147: Bullet Patterns
- Complex patterns
- Aimed spreads
- Danmaku lite
- **Runnable:** Bullet patterns

### Unit 148: Mini-Boss Enemies
- Strong regular enemy
- Mini-boss role
- Mid-stage challenge
- **Runnable:** Mini-bosses

### Unit 149: Environmental Enemies
- Wall-mounted
- Terrain integrated
- Level hazards
- **Runnable:** Environment

### Unit 150: Destructible Terrain
- Breakable walls
- Reveal secrets
- Strategic destruction
- **Runnable:** Destructible

### Unit 151: Secret Areas
- Hidden paths
- Bonus items
- Exploration reward
- **Runnable:** Secrets

### Unit 152: Rank System
- Dynamic difficulty
- Performance-based
- Adaptive challenge
- **Runnable:** Rank system

### Unit 153: Enemy Density
- More enemies
- Sprite management
- Performance maintained
- **Runnable:** High density

### Unit 154: Priority System
- Visible enemies priority
- Off-screen culling
- Smart sprite use
- **Runnable:** Priority

### Unit 155: Attack Coordination
- Enemies work together
- Pincer attacks
- Tactical challenge
- **Runnable:** Coordination

### Unit 156: Elite Enemies
- Stronger variants
- Late-game challenge
- More dangerous
- **Runnable:** Elites

### Unit 157: Enemy Variety Polish
- All enemies balanced
- Interesting mix
- Good challenge
- **Runnable:** Variety polish

### Unit 158: Enemy Effects
- Death animations
- Damage feedback
- Visual polish
- **Runnable:** Enemy effects

### Unit 159: Spawn Balance
- Fair spawning
- Manageable waves
- Challenging but fair
- **Runnable:** Spawn balance

### Unit 160: Phase 10 Integration
- Advanced enemy systems
- Complex challenges
- Rich combat
- **Runnable:** Enemies advanced

---

## Phase 11: Game Modes (Units 161-176)
*Modes and features*

### Unit 161: Normal Mode
- Standard campaign
- Default experience
- Five stages
- **Runnable:** Normal mode

### Unit 162: Easy Mode
- Reduced difficulty
- More power-ups
- Accessible
- **Runnable:** Easy mode

### Unit 163: Hard Mode
- Increased challenge
- Faster enemies
- Expert play
- **Runnable:** Hard mode

### Unit 164: Boss Rush
- Bosses only
- Quick play
- Practice mode
- **Runnable:** Boss rush

### Unit 165: Score Attack
- High score focus
- No continues
- Competitive
- **Runnable:** Score attack

### Unit 166: Time Attack
- Speed completion
- Fast play
- Optimal routes
- **Runnable:** Time attack

### Unit 167: Two-Player Mode
- Alternating play
- Shared game
- Social
- **Runnable:** Two-player

### Unit 168: Co-op Mode
- Simultaneous play
- Sprite intensive
- Optional feature
- **Runnable:** Co-op

### Unit 169: Practice Mode
- Stage select
- Skill building
- Learning tool
- **Runnable:** Practice

### Unit 170: High Score Table
- Top scores
- Initials entry
- Per-mode
- **Runnable:** High scores

### Unit 171: Save System
- Battery backup
- Save progress
- Persistent data
- **Runnable:** Save system

### Unit 172: Options Menu
- Difficulty select
- Sound test
- Controls
- **Runnable:** Options

### Unit 173: Unlockables
- Unlock extras
- Achievements
- Goals
- **Runnable:** Unlockables

### Unit 174: Second Loop
- Harder replay
- True ending
- Expert content
- **Runnable:** Second loop

### Unit 175: Mode Polish
- All modes refined
- Consistent quality
- Good variety
- **Runnable:** Modes polished

### Unit 176: Phase 11 Integration
- Multiple game modes
- High replayability
- Feature complete
- **Runnable:** Modes complete

---

## Phase 12: Advanced Bosses (Units 177-192)
*Boss enhancements*

### Unit 177: Boss Review
- Current bosses
- Enhancement plans
- More phases
- **Runnable:** Review done

### Unit 178: Boss 1 Enhancement
- Additional phase
- More attacks
- Greater challenge
- **Runnable:** Boss 1 enhanced

### Unit 179: Boss 2 Enhancement
- Extended fight
- New patterns
- More epic
- **Runnable:** Boss 2 enhanced

### Unit 180: Boss 3 Enhancement
- Complex patterns
- Multiple phases
- Technical fight
- **Runnable:** Boss 3 enhanced

### Unit 181: Boss 4 Enhancement
- Near-final difficulty
- Expert patterns
- Intense fight
- **Runnable:** Boss 4 enhanced

### Unit 182: Final Boss Expansion
- More forms
- Epic scale
- Ultimate challenge
- **Runnable:** Final boss expanded

### Unit 183: Boss Weak Points
- Multiple weak points
- Strategic targeting
- Skill element
- **Runnable:** Weak points

### Unit 184: Boss Minions
- Bosses spawn enemies
- Multi-threat
- Complex battles
- **Runnable:** Minions

### Unit 185: Boss Terrain
- Boss + terrain
- Environmental hazard
- Combined challenge
- **Runnable:** Boss terrain

### Unit 186: Boss Telegraphing
- Attack warnings
- Fair patterns
- Learnable fights
- **Runnable:** Telegraphing

### Unit 187: Boss Music Sync
- Music to phases
- Dramatic timing
- Emotional impact
- **Runnable:** Music sync

### Unit 188: Boss Death
- Epic destruction
- Satisfying defeat
- Big explosion
- **Runnable:** Boss death

### Unit 189: Boss Practice
- Boss practice mode
- Learn patterns
- Skill building
- **Runnable:** Practice mode

### Unit 190: Boss Balance
- Fair difficulty
- Achievable
- Satisfying
- **Runnable:** Balanced

### Unit 191: Boss Polish
- All bosses refined
- Great encounters
- Memorable
- **Runnable:** Polished

### Unit 192: Phase 12 Integration
- Enhanced bosses
- Epic encounters
- Professional quality
- **Runnable:** Bosses enhanced

---

## Phase 13: Optimisation (Units 193-208)
*Performance maximisation*

### Unit 193: Performance Audit
- Profile systems
- Find bottlenecks
- Priorities
- **Runnable:** Audit done

### Unit 194: Sprite Optimisation
- Efficient sprites
- Reduce flicker
- Smart allocation
- **Runnable:** Sprites optimised

### Unit 195: Scroll Optimisation
- Faster streaming
- Efficient updates
- Smooth scroll
- **Runnable:** Scroll optimised

### Unit 196: Collision Optimisation
- Fast checks
- Early exit
- Efficient detection
- **Runnable:** Collision optimised

### Unit 197: Enemy Optimisation
- Faster AI
- Batch processing
- Efficient updates
- **Runnable:** Enemies optimised

### Unit 198: Audio Optimisation
- Efficient player
- Minimal CPU
- Clean audio
- **Runnable:** Audio optimised

### Unit 199: Memory Optimisation
- Efficient storage
- Bank usage
- Optimal layout
- **Runnable:** Memory optimised

### Unit 200: Frame Rate Lock
- Consistent 60fps
- No drops
- Smooth play
- **Runnable:** Locked rate

### Unit 201: Worst Case Testing
- Maximum load
- Stress test
- Still stable
- **Runnable:** Stress tested

### Unit 202: Sprite Flicker Reduction
- Better allocation
- Priority system
- Minimal flicker
- **Runnable:** Less flicker

### Unit 203: ROM Space
- Efficient data
- Bank planning
- Room for content
- **Runnable:** ROM efficient

### Unit 204: Code Clean-up
- Remove dead code
- Clean structure
- Maintainable
- **Runnable:** Clean code

### Unit 205: Load Time
- Fast startup
- Quick to play
- Good UX
- **Runnable:** Fast load

### Unit 206: Documentation
- Code documented
- Techniques explained
- Knowledge preserved
- **Runnable:** Documented

### Unit 207: Optimisation Polish
- Final tweaks
- Maximum performance
- Production ready
- **Runnable:** Fully optimised

### Unit 208: Phase 13 Integration
- Maximum performance
- Stable 60fps
- Optimised game
- **Runnable:** Optimised

---

## Phase 14: Polish (Units 209-224)
*Final quality*

### Unit 209: Visual Polish
- Graphics refined
- Consistent style
- Professional look
- **Runnable:** Visual polish

### Unit 210: Audio Polish
- Sound balanced
- Music levels
- Clean mix
- **Runnable:** Audio polish

### Unit 211: Gameplay Polish
- Feel refinement
- Control tweaks
- Satisfying play
- **Runnable:** Gameplay polish

### Unit 212: Difficulty Polish
- Fair curve
- Achievable
- Challenging
- **Runnable:** Difficulty polish

### Unit 213: UI Polish
- Clean menus
- Clear text
- Easy navigation
- **Runnable:** UI polish

### Unit 214: Bug Hunt
- Find all bugs
- Fix everything
- Stable game
- **Runnable:** Bug-free

### Unit 215: Playtest Round 1
- External testing
- Gather feedback
- Note issues
- **Runnable:** Playtest 1

### Unit 216: Feedback Integration 1
- Address feedback
- Improve issues
- Iterate
- **Runnable:** Feedback 1

### Unit 217: Playtest Round 2
- More testing
- Verify fixes
- Final feedback
- **Runnable:** Playtest 2

### Unit 218: Feedback Integration 2
- Final changes
- Last polish
- Near-final
- **Runnable:** Feedback 2

### Unit 219: Accessibility
- Difficulty options
- Control options
- Inclusive
- **Runnable:** Accessible

### Unit 220: Instructions
- How to play
- Controls
- Power-up guide
- **Runnable:** Instructions

### Unit 221: Credits
- Full credits
- Acknowledgements
- Thank you
- **Runnable:** Credits

### Unit 222: Title Polish
- Polished title
- All options
- Professional
- **Runnable:** Title polished

### Unit 223: Ending Polish
- Victory ending
- Satisfying conclusion
- Complete story
- **Runnable:** Ending polished

### Unit 224: Phase 14 Integration
- Fully polished
- Professional quality
- Release candidate
- **Runnable:** Polished game

---

## Phase 15: Testing (Units 225-240)
*Thorough QA*

### Unit 225: Full Playthrough
- Complete game
- All stages
- Start to finish
- **Runnable:** Full playthrough

### Unit 226: All Modes Test
- Every mode
- Full coverage
- Working
- **Runnable:** Modes tested

### Unit 227: All Weapons Test
- Every weapon
- All levels
- Functioning
- **Runnable:** Weapons tested

### Unit 228: All Enemies Test
- Every enemy
- Behaviours correct
- Balanced
- **Runnable:** Enemies tested

### Unit 229: All Bosses Test
- Every boss
- All phases
- Defeatable
- **Runnable:** Bosses tested

### Unit 230: Co-op Testing
- Two-player
- Full campaign
- Stable
- **Runnable:** Co-op tested

### Unit 231: Edge Cases
- Unusual situations
- Corner cases
- Robust
- **Runnable:** Edge cases

### Unit 232: Memory Testing
- No corruption
- Stable RAM
- Clean state
- **Runnable:** Memory tested

### Unit 233: Long Session
- Extended play
- No degradation
- Stable
- **Runnable:** Long session

### Unit 234: Hardware Testing
- Real NES
- Multiple units
- Compatible
- **Runnable:** Hardware tested

### Unit 235: Emulator Testing
- Multiple emulators
- Accurate
- Compatible
- **Runnable:** Emulators tested

### Unit 236: Save Testing
- Save/load
- Data integrity
- Reliable
- **Runnable:** Save tested

### Unit 237: Regression Test
- Previous bugs
- Stay fixed
- No regression
- **Runnable:** Regression

### Unit 238: Final Fixes
- Last bugs
- Complete
- Clean
- **Runnable:** Bugs fixed

### Unit 239: Sign-Off
- Final approval
- Release ready
- Verified
- **Runnable:** Signed off

### Unit 240: Phase 15 Integration
- Thoroughly tested
- Quality assured
- Production ready
- **Runnable:** QA complete

---

## Phase 16: Release (Units 241-256)
*Distribution and completion*

### Unit 241: ROM Finalisation
- Final ROM
- Version number
- Complete build
- **Runnable:** ROM final

### Unit 242: Mapper Verification
- Mapper correct
- Bank switching
- Compatible
- **Runnable:** Mapper verified

### Unit 243: Cart Format
- Cartridge specs
- Physical release
- Manufacturing ready
- **Runnable:** Cart format

### Unit 244: Manual Creation
- Game manual
- Story
- Instructions
- **Runnable:** Manual

### Unit 245: Box Art
- Cover design
- Marketing art
- Professional
- **Runnable:** Box art

### Unit 246: Digital Distribution
- ROM distribution
- Emulator friendly
- Accessible
- **Runnable:** Digital ready

### Unit 247: Release Package
- All materials
- Complete package
- Distribution ready
- **Runnable:** Package ready

### Unit 248: Announcement
- Release notes
- Feature list
- Promotion
- **Runnable:** Announced

### Unit 249: Community Release
- Make available
- Distribution
- Access
- **Runnable:** Released

### Unit 250: Post-Release
- Bug reports
- Support
- Community
- **Runnable:** Supported

### Unit 251: Code Library
- Reusable code
- Shmup library
- Future use
- **Runnable:** Library

### Unit 252: Documentation
- Technique docs
- Knowledge sharing
- Educational
- **Runnable:** Documented

### Unit 253: Retrospective
- What worked
- Lessons learned
- Growth
- **Runnable:** Retrospective

### Unit 254: Skill Assessment
- Shmup mastery
- NES expertise
- Professional level
- **Runnable:** Skills assessed

### Unit 255: Future Planning
- Next project
- Apply learnings
- Continue growth
- **Runnable:** Future planned

### Unit 256: Course Completion
- Ion Trail complete
- Shmup mastered
- Ready for more
- **Runnable:** Complete

---

## Technical Summary

### Key NES Features Used
- Horizontal scrolling
- Nametable management
- Sprite 0 split
- APU sound/music
- Battery save (optional)
- Efficient sprite allocation

### Code Patterns Introduced
```asm
; Option following (position history)
record_position:
    ldx history_write
    lda player_x
    sta history_x,x
    lda player_y
    sta history_y,x
    inx
    cpx #HISTORY_SIZE
    bne @no_wrap
    ldx #0
@no_wrap:
    stx history_write
    rts

update_options:
    ldx #0
@loop:
    lda option_active,x
    beq @next
    ; Get delayed position
    ldy option_delay,x
    lda history_read
    clc
    adc option_offset,x
    tay
    lda history_x,y
    sta option_x,x
    lda history_y,y
    sta option_y,x
@next:
    inx
    cpx #MAX_OPTIONS
    bne @loop
    rts
```

### Skills Progression
| Phase | Primary Skills |
|-------|---------------|
| 1-2 | Scrolling, basics |
| 3-4 | Power-ups, options |
| 5-6 | Levels, bosses |
| 7-8 | Audio, weapons |
| 9-10 | Advanced systems |
| 11-12 | Modes, boss enhancement |
| 13-14 | Optimisation, polish |
| 15-16 | Testing, release |

---

## Version History
- v1.0 - Initial 256-unit outline
