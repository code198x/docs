# Game 9: Parallax - Complete 256-Unit Outline

## Game Overview
**Platform:** Commodore Amiga
**Genre:** Horizontal parallax shooter
**Concept:** THE quintessential Amiga showcase. Multi-layer parallax scrolling with dual playfield mode, Copper effects, and epic shooter gameplay. Master the techniques that made Shadow of the Beast famous.

**Technical Focus:**
- Dual playfield mode
- Multi-layer parallax (4+ layers)
- Bitplane DMA timing
- Copper palette and effects
- Hardware scrolling registers
- Blitter buffer management
- MOD replay integration

---

## Phase 1: Foundation (Units 1-16)
*Single playfield scrolling basics*

### Unit 1: Project Setup
- Parallax shooter concept
- Memory layout for dual playfield
- System setup
- **Runnable:** Clean startup

### Unit 2: Display Configuration
- Bitplane setup
- Initial colour depth
- Screen dimensions
- **Runnable:** Display ready

### Unit 3: Single Playfield Scroll
- BPLCON1 scroll
- Hardware scroll register
- Smooth motion
- **Runnable:** Basic scroll

### Unit 4: Scroll Registers Deep Dive
- Fine scroll (0-15)
- Coarse scroll via display start
- Combined scrolling
- **Runnable:** Scroll understood

### Unit 5: Bitplane Pointers
- BPLxPT registers
- Modulo setup
- Pointer management
- **Runnable:** Pointers work

### Unit 6: Player Ship Setup
- Sprite for player
- Hardware sprite basics
- Positioned on screen
- **Runnable:** Player sprite

### Unit 7: Player Movement
- Joystick control
- 8-way movement
- Screen bounds
- **Runnable:** Player moves

### Unit 8: Scrolling Background
- Tile-based background
- Single layer
- Continuous scroll
- **Runnable:** BG scrolls

### Unit 9: Background Tiles
- Tile graphics
- Tile map data
- Column updates
- **Runnable:** Tiles display

### Unit 10: Blitter Tile Copy
- Blitter for tile copy
- Off-screen updates
- Seamless scrolling
- **Runnable:** Blitter tiles

### Unit 11: Basic Shooting
- Fire button
- Bullet sprite
- Move right
- **Runnable:** Player shoots

### Unit 12: Static Enemies
- Enemy BOBs
- Fixed positions
- Collision targets
- **Runnable:** Enemies displayed

### Unit 13: Basic Collision
- Bullet vs enemy
- Bounding box
- Destruction
- **Runnable:** Collision works

### Unit 14: Score System
- Points per kill
- Score tracking
- Display later
- **Runnable:** Scoring

### Unit 15: Game Loop Basics
- Title placeholder
- Game state
- Game over
- **Runnable:** Game loop

### Unit 16: Phase 1 Integration
- Single layer scroll shooter
- Foundation for dual playfield
- Ready to expand
- **Runnable:** Single layer shooter

---

## Phase 2: Dual Playfield Basics (Units 17-32)
*Introduction to dual playfield mode*

### Unit 17: Dual Playfield Concept
- Two independent playfields
- Separate scroll registers
- Layer compositing
- **Runnable:** Concept understood

### Unit 18: BPLCON0 Configuration
- DBLPF bit
- Enable dual playfield
- Mode switch
- **Runnable:** Mode enabled

### Unit 19: Bitplane Assignment
- Odd planes = PF1
- Even planes = PF2
- 2+2 or 3+3 split
- **Runnable:** Planes assigned

### Unit 20: Separate Scroll Registers
- PF1 scroll in BPLCON1
- PF2 scroll via modulo trick
- Independent control
- **Runnable:** Separate scrolls

### Unit 21: Priority Control
- PF1/PF2 priority
- BPLCON2 settings
- Visual layering
- **Runnable:** Priority works

### Unit 22: Colour Allocation
- PF1 colours 0-7
- PF2 colours 8-15
- Shared colour 0
- **Runnable:** Colours split

### Unit 23: Two Layer Display
- Foreground (PF1)
- Background (PF2)
- Both visible
- **Runnable:** Two layers

### Unit 24: Layer Testing
- Verify separation
- Scroll independently
- Confirm dual mode
- **Runnable:** Layers tested

### Unit 25: Foreground Scroll
- PF1 game speed
- Main gameplay layer
- Player interaction
- **Runnable:** FG scrolls

### Unit 26: Background Scroll
- PF2 slower
- First parallax effect
- Depth illusion
- **Runnable:** BG scrolls slower

### Unit 27: Speed Ratios
- 2:1 speed ratio
- Parallax calculation
- Smooth difference
- **Runnable:** Ratio set

### Unit 28: Dual Playfield Blitting
- Blitter for both layers
- Separate buffers
- Independent updates
- **Runnable:** Both layers blit

### Unit 29: Memory Layout
- PF1 buffer
- PF2 buffer
- Efficient layout
- **Runnable:** Memory planned

### Unit 30: Performance Check
- DMA timing
- Bandwidth usage
- Room for more?
- **Runnable:** Performance OK

### Unit 31: Visual Testing
- Verify parallax
- Check for glitches
- Smooth motion
- **Runnable:** Visual check

### Unit 32: Phase 2 Integration
- Two-layer parallax
- Dual playfield working
- Ready for expansion
- **Runnable:** Dual playfield shooter

---

## Phase 3: Multi-Layer Parallax (Units 33-48)
*Adding more parallax layers*

### Unit 33: Multi-Layer Concept
- More than 2 speeds
- Copper colour tricks
- Pseudo-layers
- **Runnable:** Concept clear

### Unit 34: Copper List Basics
- Copper instructions
- WAIT and MOVE
- Timing to raster
- **Runnable:** Copper basics

### Unit 35: Copper Palette Changes
- Change colours mid-screen
- Different palettes per zone
- More apparent layers
- **Runnable:** Palette change

### Unit 36: Star Layer (Background)
- Distant stars
- Very slow scroll
- Deepest layer
- **Runnable:** Stars layer

### Unit 37: Mountain Layer
- Mid-ground mountains
- Medium scroll
- Silhouette graphics
- **Runnable:** Mountains

### Unit 38: Near Ground Layer
- Near terrain
- Faster scroll
- Main gameplay
- **Runnable:** Near layer

### Unit 39: Foreground Layer
- Closest elements
- Fastest scroll
- Overlay effect
- **Runnable:** Foreground

### Unit 40: Four Speed Parallax
- Stars (1x)
- Mountains (2x)
- Terrain (4x)
- Foreground (6x)
- **Runnable:** Four speeds

### Unit 41: Copper Gradient Sky
- Sky gradient
- Colour cycling
- Atmospheric
- **Runnable:** Sky gradient

### Unit 42: Horizon Effects
- Horizon line
- Split between layers
- Depth cues
- **Runnable:** Horizon

### Unit 43: Parallax Tuning
- Speed adjustments
- Visual balance
- Pleasing effect
- **Runnable:** Tuned parallax

### Unit 44: Layer Transitions
- Blend between zones
- Copper colour fades
- Smooth changes
- **Runnable:** Transitions

### Unit 45: Memory Management
- Multiple layer buffers
- Efficient storage
- Bank management
- **Runnable:** Memory managed

### Unit 46: Performance Optimisation
- DMA efficiency
- Copper timing
- Smooth performance
- **Runnable:** Optimised

### Unit 47: Visual Polish
- All layers refined
- Cohesive look
- Professional quality
- **Runnable:** Layers polished

### Unit 48: Phase 3 Integration
- Full multi-layer parallax
- Copper effects
- Impressive visuals
- **Runnable:** Multi-layer complete

---

## Phase 4: Scrolling Shooter Core (Units 49-64)
*Complete gameplay on parallax background*

### Unit 49: Player in Parallax World
- Player position
- World vs screen
- Camera system
- **Runnable:** Player positioned

### Unit 50: Enemy System
- Enemy data structure
- Spawn system
- World coordinates
- **Runnable:** Enemy system

### Unit 51: Enemy Types
- Basic fighters
- Multiple types
- Varied behaviour
- **Runnable:** Enemy types

### Unit 52: Enemy Movement
- Patterns in world
- Scroll-relative
- Smooth motion
- **Runnable:** Enemies move

### Unit 53: Bullet System
- Player bullets
- Enemy bullets
- Pooling
- **Runnable:** Bullet system

### Unit 54: Bullet Rendering
- BOBs for bullets
- Many bullets
- Performance
- **Runnable:** Bullets render

### Unit 55: Collision System
- Comprehensive collision
- Bullet-enemy
- Enemy-player
- **Runnable:** Collision complete

### Unit 56: Terrain Collision
- Solid terrain
- Player death
- Terrain definition
- **Runnable:** Terrain collision

### Unit 57: Power-Up System
- Power-up drops
- Collection
- Effects
- **Runnable:** Power-ups

### Unit 58: Score Display
- HUD area
- Score rendering
- Lives display
- **Runnable:** HUD

### Unit 59: Copper Split Screen
- Fixed HUD
- Scrolling game
- Clean split
- **Runnable:** Split screen

### Unit 60: Lives and Death
- Player lives
- Death animation
- Respawn
- **Runnable:** Lives work

### Unit 61: Game Over
- End condition
- Game over display
- Restart
- **Runnable:** Game over

### Unit 62: Title Screen
- Title display
- Start prompt
- High score
- **Runnable:** Title screen

### Unit 63: Title Parallax
- Parallax on title
- Impressive opening
- Mood setting
- **Runnable:** Title parallax

### Unit 64: Phase 4 Integration
- Complete shooter on parallax
- All core mechanics
- Ready for content
- **Runnable:** Core shooter

---

## Phase 5: Level Design (Units 65-80)
*Creating stages*

### Unit 65: Level Data Format
- Level structure
- Terrain data
- Enemy spawns
- **Runnable:** Format defined

### Unit 66: Level 1 Design
- First level
- Introduction
- Gentle start
- **Runnable:** Level 1 design

### Unit 67: Level 1 Graphics
- Level 1 tiles
- Theme graphics
- Cohesive look
- **Runnable:** Level 1 graphics

### Unit 68: Level 1 Enemies
- Enemy placement
- Fair challenge
- Learning curve
- **Runnable:** Level 1 enemies

### Unit 69: Level 1 Complete
- Full level 1
- Balanced
- Polished
- **Runnable:** Level 1 complete

### Unit 70: Level 2 Design
- New environment
- Increased challenge
- New enemies
- **Runnable:** Level 2 design

### Unit 71: Level 2 Graphics
- Different theme
- New tiles
- Visual variety
- **Runnable:** Level 2 graphics

### Unit 72: Level 2 Complete
- Full level 2
- Harder than level 1
- Complete
- **Runnable:** Level 2 complete

### Unit 73: Level 3 Design
- Mid-game challenge
- Complex terrain
- Technical
- **Runnable:** Level 3 design

### Unit 74: Level 3 Complete
- Full level 3
- Skill test
- Complete
- **Runnable:** Level 3 complete

### Unit 75: Level 4 Design
- Late game
- High difficulty
- Expert play
- **Runnable:** Level 4 design

### Unit 76: Level 4 Complete
- Full level 4
- Very challenging
- Complete
- **Runnable:** Level 4 complete

### Unit 77: Level 5 Design
- Final level
- Ultimate challenge
- Climactic
- **Runnable:** Level 5 design

### Unit 78: Level 5 Complete
- Full level 5
- Maximum difficulty
- Complete
- **Runnable:** Level 5 complete

### Unit 79: Level Transitions
- Between levels
- Score display
- Brief break
- **Runnable:** Transitions

### Unit 80: Phase 5 Integration
- Five complete levels
- Progressive difficulty
- Full campaign
- **Runnable:** Levels complete

---

## Phase 6: Boss Battles (Units 81-96)
*Epic boss encounters*

### Unit 81: Boss Framework
- Large boss structure
- Multi-sprite
- Health system
- **Runnable:** Boss framework

### Unit 82: Boss Rendering
- Multiple BOBs
- Composite boss
- Large presence
- **Runnable:** Boss rendering

### Unit 83: Boss 1 Design
- First boss
- Learnable patterns
- Introduction
- **Runnable:** Boss 1 design

### Unit 84: Boss 1 Attacks
- Attack patterns
- Bullet spreads
- Fair challenge
- **Runnable:** Boss 1 attacks

### Unit 85: Boss 1 Complete
- Full boss 1
- Satisfying defeat
- Level 1 end
- **Runnable:** Boss 1 complete

### Unit 86: Boss 2 Design
- Second boss
- New mechanics
- Harder
- **Runnable:** Boss 2 design

### Unit 87: Boss 2 Complete
- Full boss 2
- Complex patterns
- Complete
- **Runnable:** Boss 2 complete

### Unit 88: Boss 3 Design
- Mid-game boss
- Technical fight
- Unique mechanic
- **Runnable:** Boss 3 design

### Unit 89: Boss 3 Complete
- Full boss 3
- Challenging
- Complete
- **Runnable:** Boss 3 complete

### Unit 90: Boss 4 Design
- Late game boss
- Very hard
- Near-final
- **Runnable:** Boss 4 design

### Unit 91: Boss 4 Complete
- Full boss 4
- Expert required
- Complete
- **Runnable:** Boss 4 complete

### Unit 92: Final Boss Design
- Ultimate boss
- Multiple phases
- Epic scale
- **Runnable:** Final boss design

### Unit 93: Final Boss Phases
- Phase transitions
- Escalating danger
- Climactic
- **Runnable:** Final boss phases

### Unit 94: Final Boss Complete
- Full final boss
- Ultimate challenge
- Complete
- **Runnable:** Final boss complete

### Unit 95: Boss Polish
- All bosses refined
- Fair patterns
- Great fights
- **Runnable:** Bosses polished

### Unit 96: Phase 6 Integration
- Five epic bosses
- One per level
- Complete
- **Runnable:** Bosses complete

---

## Phase 7: Audio (Units 97-112)
*Sound and music*

### Unit 97: Paula Setup
- Audio channels
- Sample playback
- System ready
- **Runnable:** Audio ready

### Unit 98: SFX System
- Sound effect player
- Trigger system
- Channel allocation
- **Runnable:** SFX system

### Unit 99: Shoot Sound
- Player fire
- Satisfying effect
- Quick playback
- **Runnable:** Shoot sound

### Unit 100: Explosion Sound
- Enemy destruction
- Impact effect
- Variety
- **Runnable:** Explosion

### Unit 101: Power-Up Sound
- Collection
- Positive feedback
- Distinctive
- **Runnable:** Power-up sound

### Unit 102: Death Sound
- Player death
- Dramatic
- Clear feedback
- **Runnable:** Death sound

### Unit 103: Boss Sounds
- Boss attacks
- Impact sounds
- Epic scale
- **Runnable:** Boss sounds

### Unit 104: MOD Player Integration
- Module replay
- ProTracker format
- Background music
- **Runnable:** MOD player

### Unit 105: Title Music
- Title theme
- Atmospheric
- Sets mood
- **Runnable:** Title music

### Unit 106: Level 1-2 Music
- Early game BGM
- Energetic
- Driving
- **Runnable:** Early music

### Unit 107: Level 3-4 Music
- Mid-game BGM
- Different feel
- Variety
- **Runnable:** Mid music

### Unit 108: Level 5 Music
- Final level BGM
- Intense
- Climactic
- **Runnable:** Final music

### Unit 109: Boss Music
- Boss theme
- Tension
- Epic
- **Runnable:** Boss music

### Unit 110: Victory Music
- Stage clear
- Celebration
- Triumph
- **Runnable:** Victory music

### Unit 111: Audio Balance
- Mix levels
- SFX vs music
- Balanced
- **Runnable:** Balanced audio

### Unit 112: Phase 7 Integration
- Complete audio
- Full soundtrack
- Professional
- **Runnable:** Audio complete

---

## Phase 8: Weapons & Power-Ups (Units 113-128)
*Weapon variety*

### Unit 113: Weapon System
- Multiple weapons
- Current weapon
- Switching
- **Runnable:** Weapon system

### Unit 114: Standard Shot
- Default weapon
- Upgradeable
- Reliable
- **Runnable:** Standard shot

### Unit 115: Spread Shot
- Multi-direction
- Area coverage
- Power-up
- **Runnable:** Spread

### Unit 116: Laser Weapon
- Piercing beam
- High damage
- Visual effect
- **Runnable:** Laser

### Unit 117: Wave Weapon
- Sine wave bullets
- Area denial
- Unique
- **Runnable:** Wave

### Unit 118: Homing Missiles
- Seeking projectiles
- Auto-target
- Limited
- **Runnable:** Homing

### Unit 119: Weapon Levels
- Upgrade levels
- Increasing power
- Visual change
- **Runnable:** Levels

### Unit 120: Speed Power-Up
- Movement speed
- Cumulative
- Ship upgrade
- **Runnable:** Speed

### Unit 121: Shield Power-Up
- Damage absorption
- Limited hits
- Protection
- **Runnable:** Shield

### Unit 122: Option Drones
- Following drones
- Extra firepower
- R-Type style
- **Runnable:** Options

### Unit 123: Bomb Weapon
- Screen clear
- Limited use
- Emergency
- **Runnable:** Bombs

### Unit 124: Power-Up Visuals
- Clear icons
- Easy recognition
- Visual feedback
- **Runnable:** Visuals

### Unit 125: Power Balance
- Fair drops
- Weapon balance
- Viable options
- **Runnable:** Balanced

### Unit 126: Weapon Polish
- All weapons feel good
- Satisfying
- Fun
- **Runnable:** Polished

### Unit 127: HUD Updates
- Show weapon
- Show power
- Clear display
- **Runnable:** HUD complete

### Unit 128: Phase 8 Integration
- Complete weapon system
- Full variety
- Strategic depth
- **Runnable:** Weapons complete

---

## Phase 9: Advanced Parallax (Units 129-144)
*Parallax mastery*

### Unit 129: Parallax Review
- Current implementation
- Enhancement targets
- More effects
- **Runnable:** Review done

### Unit 130: More Layers
- Additional pseudo-layers
- Copper tricks
- Maximum depth
- **Runnable:** More layers

### Unit 131: Vertical Parallax
- Y-axis parallax
- Height variation
- 3D illusion
- **Runnable:** Vertical parallax

### Unit 132: Colour Cycling Layers
- Animated colours
- Moving without scroll
- Pseudo-motion
- **Runnable:** Colour cycling

### Unit 133: Raster Bar Effects
- Classic Amiga effect
- Copper raster bars
- Visual flair
- **Runnable:** Raster bars

### Unit 134: Water Reflections
- Water level effect
- Inverted reflection
- Copper manipulation
- **Runnable:** Reflections

### Unit 135: Cloud Layers
- Floating clouds
- Slow drift
- Atmospheric
- **Runnable:** Clouds

### Unit 136: Per-Line Effects
- Different scroll per line
- Complex copper
- Advanced technique
- **Runnable:** Per-line scroll

### Unit 137: Dynamic Speed
- Variable parallax speed
- Speed changes
- Level events
- **Runnable:** Dynamic speed

### Unit 138: Transition Effects
- Palette fades
- Layer transitions
- Scene changes
- **Runnable:** Transitions

### Unit 139: Performance Tuning
- DMA efficiency
- Copper optimisation
- Smooth performance
- **Runnable:** Performance tuned

### Unit 140: Visual Consistency
- All effects cohesive
- Unified look
- Professional
- **Runnable:** Visual consistency

### Unit 141: Level-Specific Effects
- Per-level effects
- Unique visuals
- Variety
- **Runnable:** Level effects

### Unit 142: Copper Documentation
- Document techniques
- Timing info
- Knowledge capture
- **Runnable:** Documented

### Unit 143: Effect Library
- Reusable effects
- Modular code
- Future use
- **Runnable:** Effect library

### Unit 144: Phase 9 Integration
- Advanced parallax mastery
- Maximum visual impact
- Professional quality
- **Runnable:** Parallax mastered

---

## Phase 10: Advanced Enemies (Units 145-160)
*Complex enemy systems*

### Unit 145: Enemy Framework Enhancement
- Better AI
- More behaviours
- Modular system
- **Runnable:** Framework enhanced

### Unit 146: Wave Formations
- Group patterns
- Coordinated movement
- Classic shooter
- **Runnable:** Formations

### Unit 147: Attack Patterns
- Complex approaches
- Bullet patterns
- Challenging
- **Runnable:** Attack patterns

### Unit 148: Heavy Enemies
- High health
- Mini-bosses
- Mid-level challenge
- **Runnable:** Heavy enemies

### Unit 149: Ground Enemies
- Terrain-based
- Turrets
- Environmental
- **Runnable:** Ground enemies

### Unit 150: Flying Enemies
- Air-based
- Mobile threats
- Varied patterns
- **Runnable:** Flying enemies

### Unit 151: Spawner Enemies
- Create smaller enemies
- Priority targets
- Strategic
- **Runnable:** Spawners

### Unit 152: Shield Enemies
- Directional shields
- Require positioning
- Tactical
- **Runnable:** Shield enemies

### Unit 153: Bullet Hell Lite
- Dense patterns
- Avoidance focus
- Skill test
- **Runnable:** Dense bullets

### Unit 154: Adaptive AI
- React to player
- Dynamic challenge
- Fair but tough
- **Runnable:** Adaptive AI

### Unit 155: Elite Variants
- Stronger versions
- Late game
- More dangerous
- **Runnable:** Elites

### Unit 156: Enemy Coordination
- Group tactics
- Pincer attacks
- Coordinated
- **Runnable:** Coordination

### Unit 157: Enemy Effects
- Death animations
- Damage feedback
- Visual polish
- **Runnable:** Enemy effects

### Unit 158: Enemy Balance
- Fair health values
- Point values
- Challenge curve
- **Runnable:** Balanced

### Unit 159: Variety Pass
- Good enemy mix
- Interesting combinations
- Varied gameplay
- **Runnable:** Variety

### Unit 160: Phase 10 Integration
- Advanced enemy systems
- Rich combat
- Professional quality
- **Runnable:** Enemies advanced

---

## Phase 11: Game Modes (Units 161-176)
*Modes and replayability*

### Unit 161: Normal Mode
- Standard campaign
- Default experience
- Five levels
- **Runnable:** Normal mode

### Unit 162: Easy Mode
- Reduced difficulty
- More power-ups
- Accessible
- **Runnable:** Easy mode

### Unit 163: Hard Mode
- Increased difficulty
- Expert play
- True challenge
- **Runnable:** Hard mode

### Unit 164: Boss Rush
- Bosses only
- Quick play
- Practice
- **Runnable:** Boss rush

### Unit 165: Score Attack
- High score focus
- No continues
- Competitive
- **Runnable:** Score attack

### Unit 166: Time Attack
- Speed completion
- Timer
- Optimal routes
- **Runnable:** Time attack

### Unit 167: Two-Player Mode
- Alternating
- Shared game
- Social
- **Runnable:** Two-player

### Unit 168: Practice Mode
- Stage select
- Boss practice
- Learning
- **Runnable:** Practice

### Unit 169: High Score Table
- Top 10
- Name entry
- Per-mode
- **Runnable:** High scores

### Unit 170: Save System
- Disk save
- Progress save
- High scores
- **Runnable:** Save system

### Unit 171: Options Menu
- Difficulty
- Sound options
- Controls
- **Runnable:** Options

### Unit 172: Unlockables
- Extra content
- Achievements
- Goals
- **Runnable:** Unlockables

### Unit 173: Second Loop
- Harder replay
- True ending
- Expert content
- **Runnable:** Second loop

### Unit 174: Gallery Mode
- View graphics
- Enemy gallery
- Bonus content
- **Runnable:** Gallery

### Unit 175: Mode Polish
- All modes refined
- Consistent
- Quality
- **Runnable:** Modes polished

### Unit 176: Phase 11 Integration
- Multiple game modes
- High replayability
- Feature complete
- **Runnable:** Modes complete

---

## Phase 12: Advanced Bosses (Units 177-192)
*Enhanced boss encounters*

### Unit 177: Boss Enhancement Review
- Current bosses
- Enhancement plans
- More epic
- **Runnable:** Review done

### Unit 178: Boss 1 Enhancement
- Additional phase
- More attacks
- Better fight
- **Runnable:** Boss 1 enhanced

### Unit 179: Boss 2 Enhancement
- Extended encounter
- New patterns
- More epic
- **Runnable:** Boss 2 enhanced

### Unit 180: Boss 3 Enhancement
- Complex phases
- Technical fight
- Challenging
- **Runnable:** Boss 3 enhanced

### Unit 181: Boss 4 Enhancement
- Near-final difficulty
- Expert patterns
- Intense
- **Runnable:** Boss 4 enhanced

### Unit 182: Final Boss Expansion
- More forms
- Ultimate scale
- Epic finale
- **Runnable:** Final boss expanded

### Unit 183: Boss Weak Points
- Strategic targeting
- Skill element
- Depth
- **Runnable:** Weak points

### Unit 184: Boss Minions
- Spawned enemies
- Multi-threat
- Complex
- **Runnable:** Minions

### Unit 185: Boss Terrain
- Environmental hazards
- Combined challenge
- Unique
- **Runnable:** Boss terrain

### Unit 186: Boss Parallax
- Boss-specific effects
- Dramatic background
- Epic visuals
- **Runnable:** Boss parallax

### Unit 187: Boss Music Integration
- Music to phases
- Dramatic timing
- Impact
- **Runnable:** Music integration

### Unit 188: Boss Death
- Epic destruction
- Satisfying defeat
- Big finish
- **Runnable:** Boss death

### Unit 189: Boss Gallery
- View bosses
- Stats
- Collection
- **Runnable:** Boss gallery

### Unit 190: Boss Balance
- Fair difficulty
- Achievable
- Satisfying
- **Runnable:** Balanced

### Unit 191: Boss Polish
- All refined
- Great encounters
- Memorable
- **Runnable:** Polished

### Unit 192: Phase 12 Integration
- Enhanced bosses
- Epic encounters
- Professional
- **Runnable:** Bosses enhanced

---

## Phase 13: Optimisation (Units 193-208)
*Maximum performance*

### Unit 193: Performance Audit
- Profile systems
- Find bottlenecks
- Priorities
- **Runnable:** Audit done

### Unit 194: DMA Optimisation
- Efficient DMA
- Timing alignment
- Maximum bandwidth
- **Runnable:** DMA optimised

### Unit 195: Copper Optimisation
- Efficient copper list
- Minimal instructions
- Faster execution
- **Runnable:** Copper optimised

### Unit 196: Blitter Optimisation
- Faster blits
- Efficient setup
- Less waiting
- **Runnable:** Blitter optimised

### Unit 197: BOB Optimisation
- Faster BOB drawing
- Cookie-cut efficiency
- Less overdraw
- **Runnable:** BOBs optimised

### Unit 198: Collision Optimisation
- Fast collision
- Early rejection
- Efficient
- **Runnable:** Collision optimised

### Unit 199: Enemy Optimisation
- Faster AI
- Batch processing
- Efficient
- **Runnable:** Enemies optimised

### Unit 200: Memory Optimisation
- Efficient storage
- Optimal layout
- Less waste
- **Runnable:** Memory optimised

### Unit 201: 50fps Lock
- Consistent framerate
- No drops
- Smooth
- **Runnable:** Locked 50fps

### Unit 202: Worst Case Test
- Maximum load
- Still stable
- Verified
- **Runnable:** Stress tested

### Unit 203: A500 Compatibility
- 512K chip RAM
- OCS compatible
- Mass market
- **Runnable:** A500 compatible

### Unit 204: Code Cleanup
- Clean structure
- Maintainable
- Professional
- **Runnable:** Clean code

### Unit 205: ROM Size
- Efficient data
- Fit on disk
- Good storage
- **Runnable:** Size efficient

### Unit 206: Load Time
- Fast loading
- Quick start
- Good UX
- **Runnable:** Fast load

### Unit 207: Documentation
- Technique docs
- Code comments
- Knowledge
- **Runnable:** Documented

### Unit 208: Phase 13 Integration
- Maximum performance
- Optimised code
- Production quality
- **Runnable:** Optimised

---

## Phase 14: Polish (Units 209-224)
*Final quality*

### Unit 209: Visual Polish
- Graphics refined
- Consistent style
- Professional
- **Runnable:** Visual polish

### Unit 210: Parallax Polish
- All effects perfect
- Smooth motion
- Impressive
- **Runnable:** Parallax polish

### Unit 211: Audio Polish
- Balanced mix
- Clean audio
- Professional
- **Runnable:** Audio polish

### Unit 212: Gameplay Polish
- Feel refinement
- Control tweaks
- Satisfying
- **Runnable:** Gameplay polish

### Unit 213: Difficulty Polish
- Fair curve
- Achievable
- Challenging
- **Runnable:** Difficulty polish

### Unit 214: UI Polish
- Clean menus
- Clear info
- Easy navigation
- **Runnable:** UI polish

### Unit 215: Bug Hunt
- Find all bugs
- Fix everything
- Stable
- **Runnable:** Bug-free

### Unit 216: Playtest Round 1
- External testers
- Feedback
- Issues noted
- **Runnable:** Playtest 1

### Unit 217: Feedback Integration 1
- Address feedback
- Improve
- Iterate
- **Runnable:** Feedback 1

### Unit 218: Playtest Round 2
- More testing
- Verify fixes
- Final feedback
- **Runnable:** Playtest 2

### Unit 219: Feedback Integration 2
- Final changes
- Last polish
- Near-final
- **Runnable:** Feedback 2

### Unit 220: Accessibility
- Difficulty options
- Control options
- Inclusive
- **Runnable:** Accessible

### Unit 221: Instructions
- How to play
- Controls
- Tips
- **Runnable:** Instructions

### Unit 222: Credits
- Full credits
- Acknowledgements
- Thank you
- **Runnable:** Credits

### Unit 223: Title Polish
- Final title
- All options
- Professional
- **Runnable:** Title polished

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
- All levels
- All bosses
- **Runnable:** Full playthrough

### Unit 226: All Modes Test
- Every mode
- Full coverage
- Working
- **Runnable:** Modes tested

### Unit 227: All Weapons Test
- Every weapon
- All levels
- Working
- **Runnable:** Weapons tested

### Unit 228: All Enemies Test
- Every enemy
- Correct behaviour
- Balanced
- **Runnable:** Enemies tested

### Unit 229: All Bosses Test
- Every boss
- All phases
- Defeatable
- **Runnable:** Bosses tested

### Unit 230: Parallax Testing
- All effects
- No glitches
- Smooth
- **Runnable:** Parallax tested

### Unit 231: Edge Cases
- Unusual situations
- Corner cases
- Robust
- **Runnable:** Edge cases

### Unit 232: Memory Testing
- No corruption
- Stable
- Clean
- **Runnable:** Memory tested

### Unit 233: Long Session
- Extended play
- No degradation
- Stable
- **Runnable:** Long session

### Unit 234: Hardware Testing
- Real Amiga
- Multiple models
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

### Unit 237: Regression Testing
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

### Unit 241: Disk Mastering
- Final ADF
- Bootable
- Complete
- **Runnable:** Disk mastered

### Unit 242: Multi-Disk Check
- Fit on disk
- Or handle multi-disk
- User experience
- **Runnable:** Disk verified

### Unit 243: A1200 Version
- AGA enhanced
- Extra colours
- Bonus version
- **Runnable:** A1200 version

### Unit 244: Manual Creation
- Game manual
- Story
- Instructions
- **Runnable:** Manual

### Unit 245: Box Art
- Cover design
- Retro aesthetic
- Professional
- **Runnable:** Box art

### Unit 246: Distribution Package
- All files
- All versions
- Complete
- **Runnable:** Package ready

### Unit 247: Release Announcement
- Feature list
- Screenshots
- Promotion
- **Runnable:** Announced

### Unit 248: Community Release
- Make available
- Distribution
- Access
- **Runnable:** Released

### Unit 249: Post-Release
- Bug reports
- Support
- Community
- **Runnable:** Supported

### Unit 250: Parallax Code Release
- Share techniques
- Dual playfield code
- Educational
- **Runnable:** Code shared

### Unit 251: Technique Documentation
- Parallax guide
- Copper techniques
- Knowledge sharing
- **Runnable:** Techniques documented

### Unit 252: Code Library
- Reusable modules
- Future games
- Asset library
- **Runnable:** Library

### Unit 253: Retrospective
- What worked
- Lessons learned
- Growth
- **Runnable:** Retrospective

### Unit 254: Skill Assessment
- Parallax mastery
- Dual playfield expertise
- Amiga proficiency
- **Runnable:** Skills assessed

### Unit 255: Future Planning
- Next project
- Apply learnings
- Continue growth
- **Runnable:** Future planned

### Unit 256: Course Completion
- Parallax complete
- Dual playfield mastered
- Amiga expertise
- **Runnable:** Complete

---

## Technical Summary

### Key Amiga Features Used
- Dual playfield mode
- Multi-layer parallax scrolling
- Copper list programming
- Hardware scroll registers
- Blitter buffer management
- BOB rendering
- Paula MOD replay

### Code Patterns Introduced
```asm
; Dual playfield scroll setup
setup_dual_playfield:
    move.w  #$0200,BPLCON0    ; DBLPF enable
    move.w  #$0024,BPLCON2    ; PF2 priority

    ; PF1 scroll (foreground)
    move.w  pf1_scroll,d0
    and.w   #$000f,d0
    lsl.w   #4,d0             ; Low nibble
    move.w  d0,BPLCON1

    ; PF2 scroll via BPLxPT adjustment
    move.w  pf2_scroll,d0
    lsr.w   #4,d0             ; Coarse scroll
    mulu    #40,d0            ; Bytes per line
    add.l   #pf2_buffer,d0
    move.l  d0,BPL2PT
    rts

; Copper parallax effect
copper_list:
    dc.w    $2c01,$fffe       ; Wait line 44
    dc.w    COLOR00,$0248     ; Sky colour
    dc.w    $4001,$fffe       ; Wait line 64
    dc.w    COLOR00,$0359     ; Lighter sky
    dc.w    $8001,$fffe       ; Wait line 128
    dc.w    COLOR00,$046a     ; Horizon
    dc.w    $ffff,$fffe       ; End
```

### Skills Progression
| Phase | Primary Skills |
|-------|---------------|
| 1-2 | Single/dual playfield |
| 3-4 | Multi-layer parallax |
| 5-6 | Levels, bosses |
| 7-8 | Audio, weapons |
| 9-10 | Advanced parallax, enemies |
| 11-12 | Modes, boss enhancement |
| 13-14 | Optimisation, polish |
| 15-16 | Testing, release |

---

## Version History
- v1.0 - Initial 256-unit outline
