# Game 8: Night Raid - Complete 128-Unit Outline

## Game Overview
**Platform:** Commodore 64
**Genre:** Scramble-style horizontal shooter
**Concept:** Fly your jet through enemy territory, navigate terrain, shoot enemies, bomb ground targets, and manage fuel. A classic Scramble/Super Cobra-style game showcasing the C64's scrolling and sprite capabilities combined.

**Technical Focus:**
- Combined scrolling and shooting mechanics
- Terrain collision with scrolling landscape
- Fuel resource management
- Dual weapons (forward shots and bombs)
- Level streaming from compressed data
- Boss encounters with patterns

---

## Phase 1: Foundation (Units 1-16)
*Establish scrolling terrain display*

### Unit 1: Project Setup
- Create night-raid project structure
- Set up memory map for scrolling game
- Basic initialisation code
- System setup and interrupts
- **Runnable:** Clean startup

### Unit 2: Display Configuration
- Set up character mode display
- Configure VIC-II for scrolling
- Border and background colours
- Screen memory location
- **Runnable:** Display ready

### Unit 3: Colour Scheme
- Night-time palette (dark blues, blacks)
- Terrain colours
- Enemy and player colours
- Atmospheric feel
- **Runnable:** Night atmosphere

### Unit 4: Terrain Concept
- Character-based terrain
- Ground and ceiling design
- Tunnel passages
- Visual variety
- **Runnable:** Terrain concept documented

### Unit 5: Terrain Characters
- Design terrain character set
- Ground tiles (flat, slopes)
- Ceiling tiles
- Transition pieces
- **Runnable:** Terrain charset ready

### Unit 6: Static Terrain Display
- Draw terrain on screen
- Ground at bottom
- Ceiling at top
- Test patterns
- **Runnable:** Static terrain visible

### Unit 7: Level Data Format
- Define level data structure
- Terrain column encoding
- Compression consideration
- Data organisation
- **Runnable:** Data format defined

### Unit 8: Level Data Storage
- Create first level data
- Column-by-column terrain
- Ground and ceiling heights
- Store in memory
- **Runnable:** Level data ready

### Unit 9: Hardware Scroll Setup
- VIC-II horizontal scroll register ($D016)
- Smooth scroll 0-7 pixels
- 38-column mode for scrolling
- Scroll mechanics
- **Runnable:** Scroll register control

### Unit 10: Basic Scrolling
- Increment scroll register
- Wrap at 8 pixels
- Shift screen when wrap
- Continuous scrolling
- **Runnable:** Terrain scrolls

### Unit 11: Screen Shifting
- Move screen data left
- Efficient byte shifting
- Colour RAM shifting
- New column insertion
- **Runnable:** Screen shifts correctly

### Unit 12: Column Streaming
- Read level data for new column
- Insert at right edge
- Terrain appears smoothly
- Continuous level
- **Runnable:** Level streams in

### Unit 13: Colour RAM Scrolling
- Shift colour RAM with screen
- Maintain terrain colours
- Synchronised shifting
- Colour consistency
- **Runnable:** Coloured terrain scrolls

### Unit 14: Scroll Speed Control
- Variable scroll speed
- Timing-based scrolling
- Consistent feel
- Speed adjustment
- **Runnable:** Controlled scroll speed

### Unit 15: Terrain Variety
- Multiple terrain types
- Open areas
- Narrow tunnels
- Visual interest
- **Runnable:** Varied terrain

### Unit 16: Phase 1 Integration
- Smooth scrolling terrain
- Level data streaming
- Night atmosphere
- Foundation complete
- **Runnable:** Scrolling landscape

---

## Phase 2: Core Mechanics (Units 17-32)
*Player ship and basic shooting*

### Unit 17: Player Sprite Design
- Jet/ship sprite design
- Right-facing craft
- Colour choices
- Compact design (single sprite)
- **Runnable:** Player sprite ready

### Unit 18: Player Display
- Position sprite on screen
- Left-centre placement
- Proper priority
- Sprite visible
- **Runnable:** Ship displayed

### Unit 19: Player Movement
- Joystick vertical movement
- Smooth up/down control
- Movement boundaries
- Responsive feel
- **Runnable:** Ship moves vertically

### Unit 20: Horizontal Movement
- Limited horizontal range
- Forward/back within area
- Screen position constraints
- Full movement control
- **Runnable:** Full movement

### Unit 21: Terrain Collision Setup
- Detect ship vs terrain
- Character-based collision
- Check ship corners
- Collision flag
- **Runnable:** Collision detection ready

### Unit 22: Terrain Death
- Crash on terrain contact
- Death animation
- Life lost
- Respawn sequence
- **Runnable:** Terrain kills player

### Unit 23: Bullet Sprite
- Small bullet sprite
- Fast-moving projectile
- Horizontal trajectory
- Multiple bullets
- **Runnable:** Bullet sprite ready

### Unit 24: Bullet Firing
- Fire button detection
- Spawn bullet at ship
- Fire rate limiting
- Bullet pool system
- **Runnable:** Bullets fire

### Unit 25: Bullet Movement
- Move bullets rightward
- Fast speed
- Remove when off-screen
- Efficient updating
- **Runnable:** Bullets travel

### Unit 26: Bullet vs Terrain
- Bullets hit terrain
- Remove on impact
- No terrain damage
- Clean removal
- **Runnable:** Bullets stop at terrain

### Unit 27: Bomb Mechanic
- Second fire button (or down+fire)
- Bomb drops downward
- Gravity arc
- Different from bullets
- **Runnable:** Bombs drop

### Unit 28: Bomb Physics
- Gravity acceleration
- Arc trajectory
- Ground contact
- Explosion on impact
- **Runnable:** Bomb arcs down

### Unit 29: Bomb Animation
- Bomb sprite
- Explosion animation
- Impact effect
- Visual feedback
- **Runnable:** Bombs explode

### Unit 30: Weapon Selection
- Toggle or simultaneous
- Clear weapon indication
- Both weapons usable
- Tactical choice
- **Runnable:** Dual weapons

### Unit 31: Lives System
- Three lives
- Lives display
- Death and respawn
- Game over condition
- **Runnable:** Lives work

### Unit 32: Phase 2 Integration
- Player with movement
- Forward shooting
- Bomb dropping
- Terrain collision
- **Runnable:** Playable shooter base

---

## Phase 3: Game Systems (Units 33-48)
*Enemies and fuel management*

### Unit 33: Fuel System Concept
- Fuel as resource
- Constant depletion
- Fuel gauge display
- Strategic element
- **Runnable:** Fuel concept defined

### Unit 34: Fuel Gauge Display
- Visual fuel bar
- Decreasing display
- Warning at low fuel
- Clear feedback
- **Runnable:** Fuel gauge visible

### Unit 35: Fuel Depletion
- Fuel decreases over time
- Depletion rate
- Empty fuel = death
- Urgency mechanic
- **Runnable:** Fuel depletes

### Unit 36: Fuel Tanks
- Ground-based fuel targets
- Bomb to collect
- Fuel tank sprites
- Placed in level data
- **Runnable:** Fuel tanks in level

### Unit 37: Fuel Collection
- Bomb fuel tank
- Fuel increases
- Collection feedback
- Risk/reward placement
- **Runnable:** Fuel collection works

### Unit 38: Basic Air Enemy
- Flying enemy sprite
- Simple movement pattern
- Positioned in levels
- Collision with player
- **Runnable:** Air enemy appears

### Unit 39: Air Enemy Patterns
- Sine wave movement
- Diving attacks
- Multiple patterns
- Varied behaviour
- **Runnable:** Enemy patterns

### Unit 40: Enemy Shooting
- Bullets fire back
- Aimed or straight
- Player must dodge
- Increased threat
- **Runnable:** Enemies shoot

### Unit 41: Ground Targets
- Stationary ground enemies
- Turrets/installations
- Bomb targets
- Points for destruction
- **Runnable:** Ground targets

### Unit 42: Turret Behaviour
- Ground turrets shoot up
- Timing patterns
- Predictable but dangerous
- Skill to destroy
- **Runnable:** Turrets attack

### Unit 43: Enemy Collision
- Bullet vs enemy
- Bomb vs ground target
- Explosion effects
- Score on kill
- **Runnable:** Enemies die

### Unit 44: Score System
- Points per enemy type
- Fuel tank bonus
- Score display
- Running total
- **Runnable:** Scoring works

### Unit 45: Level Sections
- Multiple terrain sections
- Section transitions
- Variety within level
- Pacing control
- **Runnable:** Section variety

### Unit 46: Difficulty Curve
- More enemies over time
- Tighter terrain
- Less fuel
- Progressive challenge
- **Runnable:** Difficulty increases

### Unit 47: Checkpoint System
- Restart points
- Progress saving
- Reduced frustration
- Fair difficulty
- **Runnable:** Checkpoints work

### Unit 48: Phase 3 Integration
- Fuel management
- Multiple enemy types
- Ground and air targets
- Score system
- **Runnable:** Full Scramble gameplay

---

## Phase 4: Polish & Feel (Units 49-64)
*Visual and audio refinement*

### Unit 49: Raster Background
- Colour splits for sky
- Gradient effect
- Night sky atmosphere
- Raster interrupt
- **Runnable:** Gradient sky

### Unit 50: Starfield Layer
- Background stars
- Different scroll speed
- Parallax effect
- Depth perception
- **Runnable:** Parallax stars

### Unit 51: Terrain Detail
- Additional terrain characters
- Surface detail
- Visual richness
- Improved graphics
- **Runnable:** Detailed terrain

### Unit 52: Explosion Effects
- Multi-frame explosions
- Enemy death animation
- Ship crash animation
- Satisfying destruction
- **Runnable:** Better explosions

### Unit 53: Particle Debris
- Flying debris on explosion
- Small particle sprites
- Brief particle life
- Enhanced destruction
- **Runnable:** Debris particles

### Unit 54: Engine Flame
- Thruster animation
- Sprite overlay or char
- Movement indication
- Ship feels alive
- **Runnable:** Engine flame

### Unit 55: SID Engine Sound
- Constant engine hum
- Filter modulation
- Pitch with speed
- Atmospheric audio
- **Runnable:** Engine sound

### Unit 56: Weapon Sounds
- Bullet fire sound
- Bomb drop sound
- Distinct sounds
- Satisfying feedback
- **Runnable:** Weapon audio

### Unit 57: Explosion Sounds
- Enemy explosion
- Player death
- Ground target destruction
- Impactful audio
- **Runnable:** Explosion audio

### Unit 58: Music System
- In-game music
- Tension building
- SID composition
- Looping track
- **Runnable:** Background music

### Unit 59: Low Fuel Warning
- Audio warning
- Visual flash
- Urgency communication
- Clear feedback
- **Runnable:** Fuel warning

### Unit 60: HUD Polish
- Clean fuel gauge
- Score display
- Lives indicator
- Professional HUD
- **Runnable:** Polished HUD

### Unit 61: Title Screen
- Game title
- Night Raid branding
- Start prompt
- High score display
- **Runnable:** Title screen

### Unit 62: Title Animation
- Animated title elements
- Scrolling demo terrain
- Attract attention
- Professional start
- **Runnable:** Animated title

### Unit 63: Game Over Screen
- Final score
- High score update
- Restart option
- Clean ending
- **Runnable:** Game over screen

### Unit 64: Phase 4 Integration
- Full audiovisual polish
- Atmospheric presentation
- Professional feel
- Polished game
- **Runnable:** Polished Night Raid

---

## Phase 5: Advanced Features (Units 65-80)
*Boss encounters and power-ups*

### Unit 65: Boss Concept
- End-of-level boss
- Large multi-sprite enemy
- Pattern-based attacks
- Climactic encounter
- **Runnable:** Boss designed

### Unit 66: Boss Sprite Assembly
- Multiple sprites combined
- Large boss appearance
- Colour coordination
- Imposing presence
- **Runnable:** Boss sprites ready

### Unit 67: Boss Movement
- Movement patterns
- Attack phases
- Predictable but challenging
- Learnable patterns
- **Runnable:** Boss moves

### Unit 68: Boss Attacks
- Multiple attack types
- Bullet spreads
- Targeted shots
- Dangerous patterns
- **Runnable:** Boss attacks

### Unit 69: Boss Weak Points
- Damageable sections
- Health tracking
- Visual damage indication
- Strategic targeting
- **Runnable:** Boss takes damage

### Unit 70: Boss Death
- Dramatic explosion
- Multi-part destruction
- Victory celebration
- Level complete
- **Runnable:** Boss defeated

### Unit 71: Power-Up System
- Power-up items
- Spawn in level
- Collection mechanic
- Various effects
- **Runnable:** Power-ups appear

### Unit 72: Speed Power-Up
- Faster ship movement
- Temporary boost
- Duration timer
- Speed indication
- **Runnable:** Speed boost

### Unit 73: Rapid Fire
- Faster shooting
- More bullets
- Offensive boost
- Timed duration
- **Runnable:** Rapid fire

### Unit 74: Shield Power-Up
- Temporary invincibility
- Shield visual effect
- Protection from collision
- Strategic use
- **Runnable:** Shield active

### Unit 75: Weapon Upgrades
- Spread shot
- Double bombs
- Enhanced weapons
- Upgrade levels
- **Runnable:** Weapon upgrades

### Unit 76: Level 2 Design
- New terrain theme
- Different enemies
- Fresh challenges
- Extended gameplay
- **Runnable:** Level 2 terrain

### Unit 77: Level 2 Enemies
- New enemy types
- Different patterns
- Increased difficulty
- Variety
- **Runnable:** Level 2 enemies

### Unit 78: Level 2 Boss
- Different boss design
- New attack patterns
- Unique challenge
- Distinct encounter
- **Runnable:** Level 2 boss

### Unit 79: Level Transitions
- Level complete screen
- Score bonus
- Brief celebration
- Smooth transition
- **Runnable:** Level transitions

### Unit 80: Phase 5 Integration
- Boss encounters
- Power-up system
- Multiple levels
- Feature-complete
- **Runnable:** Advanced Night Raid

---

## Phase 6: Content & Variety (Units 81-96)
*Expanded content and modes*

### Unit 81: Level 3 Design
- Underground caves
- Tight passages
- New terrain graphics
- Different atmosphere
- **Runnable:** Level 3 terrain

### Unit 82: Level 3 Enemies
- Cave-specific enemies
- Stalactite hazards
- Unique challenges
- Fresh gameplay
- **Runnable:** Level 3 complete

### Unit 83: Level 4 Design
- Base/factory theme
- Industrial terrain
- More targets
- Different aesthetic
- **Runnable:** Level 4 terrain

### Unit 84: Level 4 Boss
- Final boss
- Most challenging
- Complex patterns
- Epic confrontation
- **Runnable:** Final boss

### Unit 85: Bonus Stages
- Between-level bonus
- Collect items
- No enemies
- Score opportunity
- **Runnable:** Bonus stages

### Unit 86: Secret Areas
- Hidden passages
- Extra fuel/powerups
- Exploration reward
- Discovery element
- **Runnable:** Secrets implemented

### Unit 87: Enemy Variety Pack
- Additional enemy types
- Unique behaviours
- Mix across levels
- Combat variety
- **Runnable:** More enemies

### Unit 88: Difficulty Modes
- Easy/Normal/Hard
- Speed and enemy changes
- Accessibility options
- Replayability
- **Runnable:** Difficulty selection

### Unit 89: Practice Mode
- Level select
- Practice specific areas
- Skill building
- Less frustration
- **Runnable:** Practice mode

### Unit 90: Two-Player Alternating
- Take turns
- Compete for high score
- Social play
- Pass controller
- **Runnable:** Two-player turns

### Unit 91: Achievements
- Milestone tracking
- Special accomplishments
- Hidden achievements
- Replay incentive
- **Runnable:** Achievement system

### Unit 92: Statistics
- Games played
- Enemies destroyed
- Fuel collected
- Distance travelled
- **Runnable:** Statistics tracking

### Unit 93: Sound Options
- Music on/off
- Sound effects volume
- Player preference
- Options menu
- **Runnable:** Sound options

### Unit 94: Control Options
- Sensitivity settings
- Button mapping
- Customisation
- Comfort options
- **Runnable:** Control options

### Unit 95: Extended Ending
- Victory sequence
- Story conclusion
- Credits roll
- Satisfying finale
- **Runnable:** Full ending

### Unit 96: Phase 6 Integration
- All levels complete
- Multiple modes
- Full options
- Content complete
- **Runnable:** Full content

---

## Phase 7: Optimisation & Effects (Units 97-112)
*Performance and advanced effects*

### Unit 97: Performance Analysis
- Measure frame timing
- Identify slowdowns
- Optimisation targets
- Profiling
- **Runnable:** Performance data

### Unit 98: Scroll Optimisation
- Faster screen shifting
- Optimised memory moves
- Reduced CPU time
- Smoother scrolling
- **Runnable:** Fast scrolling

### Unit 99: Sprite Optimisation
- Efficient sprite updates
- Reduced calculations
- Better performance
- More headroom
- **Runnable:** Fast sprites

### Unit 100: Collision Optimisation
- Faster terrain checks
- Optimised enemy collision
- Early exit conditions
- Reduced overhead
- **Runnable:** Fast collision

### Unit 101: Advanced Raster Effects
- Multiple colour splits
- Complex gradients
- Atmospheric effects
- Visual depth
- **Runnable:** Advanced rasters

### Unit 102: Sprite Multiplexing Intro
- More sprites than 8
- Basic multiplexing
- Enemy swarms
- Impressive numbers
- **Runnable:** Extra sprites

### Unit 103: Screen Flash Effects
- Explosion screen flash
- Boss damage flash
- Impact feedback
- Visual punch
- **Runnable:** Flash effects

### Unit 104: Weather Effects
- Rain in some levels
- Weather graphics
- Atmospheric variety
- Visual interest
- **Runnable:** Weather

### Unit 105: High Score Table
- Top 10 scores
- Name entry
- Persistent storage
- Competitive element
- **Runnable:** High score table

### Unit 106: High Score Save
- Save to disk
- Load on start
- Persistent records
- Competition
- **Runnable:** Saved high scores

### Unit 107: Demo Mode
- Attract sequence
- AI plays demo
- Shows gameplay
- Arcade feel
- **Runnable:** Demo mode

### Unit 108: Loading Music
- Music during load
- No silent waiting
- Professional feel
- Patient loading
- **Runnable:** Load music

### Unit 109: Turbo Loader
- Fast loading routine
- Reduced wait time
- User experience
- Technical feature
- **Runnable:** Fast loading

### Unit 110: Memory Optimisation
- Efficient data packing
- Level compression
- More content fits
- Better utilisation
- **Runnable:** Optimised memory

### Unit 111: PAL/NTSC Support
- Timing adjustments
- Both standards
- Wider compatibility
- Regional support
- **Runnable:** Multi-region

### Unit 112: Phase 7 Integration
- All optimisations
- Advanced effects
- High scores
- Demo mode
- **Runnable:** Optimised game

---

## Phase 8: Final Polish & Release (Units 113-128)
*Final quality and release preparation*

### Unit 113: Bug Hunt
- Systematic testing
- Edge case testing
- Bug fixing
- Stable build
- **Runnable:** Bug-free game

### Unit 114: Balance Testing
- Difficulty curve check
- Fuel placement
- Enemy density
- Fair challenge
- **Runnable:** Balanced game

### Unit 115: Control Tuning
- Ship responsiveness
- Weapon feel
- Bomb arc
- Tight controls
- **Runnable:** Tuned controls

### Unit 116: Audio Balance
- Volume levels
- Music/SFX mix
- No distortion
- Pleasant audio
- **Runnable:** Balanced audio

### Unit 117: Visual Polish
- Final sprite tweaks
- Colour refinement
- Consistent style
- Professional look
- **Runnable:** Polished visuals

### Unit 118: Loading Screen
- Attractive loader
- Game branding
- Professional presentation
- First impression
- **Runnable:** Loading screen

### Unit 119: Credits Screen
- Developer credits
- Acknowledgements
- Thanks
- Professional credits
- **Runnable:** Credits

### Unit 120: Instructions Screen
- How to play
- Control explanation
- Game mechanics
- Help available
- **Runnable:** Instructions

### Unit 121: Disk Version
- D64 disk image
- Proper file layout
- Save game support
- Disk-based release
- **Runnable:** Disk version

### Unit 122: Tape Version
- T64/TAP format
- Tape-compatible
- Loader included
- Tape release
- **Runnable:** Tape version

### Unit 123: Cartridge Consideration
- CRT format option
- Instant loading
- Memory mapping
- Cart compatibility
- **Runnable:** Cart version

### Unit 124: Final Testing
- Complete playthrough
- All paths tested
- No remaining bugs
- Release quality
- **Runnable:** Fully tested

### Unit 125: Playtesting
- External feedback
- Fresh perspectives
- Final adjustments
- User validation
- **Runnable:** Playtested

### Unit 126: Documentation
- Game manual
- Technical notes
- Distribution readme
- Complete package
- **Runnable:** Documented

### Unit 127: Release Build
- Final compilation
- All files packaged
- Version numbered
- Release candidate
- **Runnable:** Release ready

### Unit 128: Project Retrospective
- Techniques learned
- Scrolling shooter mastery
- Terrain collision
- Resource management
- **Runnable:** Complete Night Raid

---

## Technical Summary

### Key C64 Features Used
- VIC-II hardware horizontal scrolling
- Character-based terrain with colour RAM
- Sprite player, enemies, bullets, bombs
- Raster interrupts for colour effects
- SID for music and sound effects

### Code Patterns Introduced
```asm
; Terrain collision check
check_terrain:
    lda player_x
    lsr
    lsr
    lsr                 ; Divide by 8 for char column
    sta char_col
    lda player_y
    lsr
    lsr
    lsr                 ; Divide by 8 for char row
    sta char_row
    ; Calculate screen address
    ; Check if character is terrain
    rts

; Scroll and stream new column
do_scroll:
    dec scroll_fine
    bpl .no_shift
    lda #7
    sta scroll_fine
    jsr shift_screen_left
    jsr stream_new_column
.no_shift:
    lda #$08
    ora scroll_fine     ; Combine with 38-col mode
    sta $d016
    rts
```

### Skills Progression
| Phase | Primary Skills |
|-------|---------------|
| 1 | Scrolling terrain, level streaming |
| 2 | Player movement, dual weapons |
| 3 | Fuel management, enemies |
| 4 | Audio, visual polish |
| 5 | Boss battles, power-ups |
| 6 | Multiple levels, modes |
| 7 | Optimisation, effects |
| 8 | Polish, release |

---

## Version History
- v1.0 - Initial 128-unit outline
