# Game 7: Scroll Runner - Complete 128-Unit Outline

## Game Overview
**Platform:** Commodore 64
**Genre:** Endless horizontal scroller / runner
**Concept:** Runner dodges obstacles in an endless scroll. Introduces VIC-II hardware horizontal scrolling, double buffering, and parallax effects.

**Technical Focus:**
- VIC-II horizontal hardware scrolling ($D016)
- Colour RAM scrolling synchronisation
- Double buffering for smooth updates
- Raster timing for colour splits
- Procedural obstacle spawning
- Parallax background layers

---

## Phase 1: Foundation (Units 1-16)
*Establish scrolling display and player character*

### Unit 1: Project Setup
- Create scroll-runner project structure
- Set up memory map for scrolling game
- Initialise VIC-II for custom screen
- Display static test pattern
- **Runnable:** Screen with test pattern displayed

### Unit 2: Understanding Hardware Scroll
- VIC-II scroll registers explained ($D016)
- Fine scroll range (0-7 pixels)
- Relationship between fine and coarse scroll
- Display scroll register value on screen
- **Runnable:** Screen showing current scroll value

### Unit 3: Horizontal Fine Scroll
- Implement fine scroll (0-7 pixels)
- Smooth pixel-by-pixel movement
- Keyboard control of scroll position
- Understand scroll direction conventions
- **Runnable:** Press keys to fine scroll left/right

### Unit 4: Screen Memory Layout
- 40x25 character screen organisation
- Row-major memory layout
- Calculate screen positions
- Understanding screen wrapping
- **Runnable:** Display showing memory layout diagram

### Unit 5: Coarse Scroll Concept
- When fine scroll wraps (7→0)
- Need to shift screen data
- Character-width (8 pixel) coarse scroll
- Planning the scroll pipeline
- **Runnable:** Manual coarse scroll demonstration

### Unit 6: Player Character Design
- Design running character frames
- 3-frame running animation cycle
- Character-based player (not sprite yet)
- Place player on left side of screen
- **Runnable:** Static player character displayed

### Unit 7: Player Animation Loop
- Cycle through animation frames
- Tie animation to frame counter
- Smooth animation timing
- Player appears to run in place
- **Runnable:** Animated running character

### Unit 8: Ground Line Setup
- Define ground row on screen
- Fill ground with terrain character
- Player positioned above ground
- Establish visual baseline
- **Runnable:** Player running on ground line

### Unit 9: Basic Scroll Loop
- Main loop structure for scrolling
- Fine scroll increment each frame
- Detect wrap point (7→0)
- Placeholder for coarse scroll
- **Runnable:** Fine scroll loops continuously

### Unit 10: Screen Shift Right-to-Left
- Shift character data when wrapping
- Move each row left by one character
- Preserve player position
- Understand shift direction
- **Runnable:** Screen shifts with coarse scroll

### Unit 11: Colour RAM Basics
- Colour RAM at $D800
- Each character has colour byte
- Colour RAM must scroll too
- Display coloured test pattern
- **Runnable:** Coloured scrolling display

### Unit 12: Synchronised Colour Scroll
- Shift colour RAM with screen RAM
- Maintain colour alignment
- Handle colour bleeding issues
- Test with multi-coloured ground
- **Runnable:** Colours scroll correctly with characters

### Unit 13: Scroll Speed Control
- Variable scroll speed
- Skip frames for slower scroll
- Multiple pixels per frame for faster
- Speed control variable
- **Runnable:** Adjustable scroll speed

### Unit 14: Screen Edge Column
- New content enters from right edge
- Column 39 receives new data
- Placeholder column drawing
- Edge column colour handling
- **Runnable:** New column appears during scroll

### Unit 15: Ground Continuity
- Ground continues from edge
- Fill edge column with ground
- Seamless ground scrolling
- Test extended scrolling
- **Runnable:** Continuous ground scrolls smoothly

### Unit 16: Phase 1 Integration
- Combine all scrolling elements
- Player runs while ground scrolls
- Smooth continuous movement
- Performance baseline established
- **Runnable:** Complete scrolling foundation demo

---

## Phase 2: Core Mechanics (Units 17-32)
*Player control and basic obstacles*

### Unit 17: Sprite Player Introduction
- Convert player to hardware sprite
- Sprite advantages for scrolling games
- Define sprite data for runner
- Position sprite over character location
- **Runnable:** Sprite player replaces character

### Unit 18: Running Sprite Animation
- Multiple sprite frames for running
- Sprite pointer switching
- 4-frame running cycle
- Smooth sprite animation
- **Runnable:** Animated sprite runner

### Unit 19: Jump Input Detection
- Read joystick fire button
- Read spacebar as alternative
- Input debouncing
- Jump state flag
- **Runnable:** Detect jump input (no action yet)

### Unit 20: Jump Arc Physics
- Vertical velocity for jump
- Gravity acceleration
- Parabolic arc motion
- Ground detection (return to baseline)
- **Runnable:** Player jumps with realistic arc

### Unit 21: Jump Animation Frames
- Sprite frame for ascending
- Sprite frame for descending
- Frame selection based on velocity
- Transition back to running
- **Runnable:** Jump with appropriate animation

### Unit 22: Obstacle Data Structure
- Define obstacle types
- Position and type storage
- Active obstacle array
- Maximum simultaneous obstacles
- **Runnable:** Obstacle data structure test

### Unit 23: Simple Obstacle Spawning
- Timer-based obstacle creation
- Random position variation
- Add to active obstacle list
- Basic spawn rate
- **Runnable:** Obstacles spawn at regular intervals

### Unit 24: Obstacle Rendering
- Draw obstacles as characters
- Multi-character obstacle blocks
- Position in edge column
- Scroll with terrain
- **Runnable:** Obstacles appear and scroll

### Unit 25: Obstacle Types - Low
- Ground-level obstacles (rocks)
- Player must jump over
- Visual design for low obstacles
- Consistent collision height
- **Runnable:** Low obstacles scroll past

### Unit 26: Obstacle Types - High
- Elevated obstacles (birds, branches)
- Player must duck/slide under
- Duck input (joystick down)
- Visual design for high obstacles
- **Runnable:** High obstacles at different height

### Unit 27: Duck Mechanic
- Ducking state and animation
- Reduced collision height when ducking
- Recovery from duck
- Cannot jump while ducking
- **Runnable:** Player can duck under obstacles

### Unit 28: Collision Box Definition
- Player hitbox rectangle
- Obstacle hitbox rectangles
- Hitbox visualisation (debug)
- Adjust hitboxes for fairness
- **Runnable:** Visible collision boxes (debug mode)

### Unit 29: Collision Detection
- Box overlap testing
- Check player vs all obstacles
- Collision flag system
- Adjust for sprite position
- **Runnable:** Collisions detected and flagged

### Unit 30: Collision Response
- Stop scrolling on hit
- Player hit animation
- Game over state
- Restart mechanism
- **Runnable:** Game ends on obstacle collision

### Unit 31: Obstacle Removal
- Remove obstacles past left edge
- Free slots in obstacle array
- Memory management
- Verify no memory leaks
- **Runnable:** Clean obstacle lifecycle

### Unit 32: Phase 2 Integration
- Complete jump/duck mechanics
- Two obstacle types working
- Collision and game over
- Core gameplay loop complete
- **Runnable:** Playable runner prototype

---

## Phase 3: Game Systems (Units 33-48)
*Scoring, difficulty, and game structure*

### Unit 33: Score System
- Distance-based scoring
- Score variable (16-bit or larger)
- Increment with scroll distance
- Score display on screen
- **Runnable:** Score increases while running

### Unit 34: Score Display Formatting
- Convert binary to decimal
- Right-aligned score display
- Leading zeros or spaces
- Position in safe screen area
- **Runnable:** Formatted score display

### Unit 35: High Score Tracking
- Store best score in memory
- Compare current to high score
- Update high score on beat
- Display high score
- **Runnable:** High score tracked and displayed

### Unit 36: Difficulty Progression
- Speed increases with distance
- Difficulty curve design
- Maximum speed cap
- Distance thresholds
- **Runnable:** Game gets progressively faster

### Unit 37: Obstacle Frequency Scaling
- More obstacles at higher difficulty
- Spawn timer adjustment
- Minimum gap enforcement
- Difficulty-based patterns
- **Runnable:** More obstacles at higher speeds

### Unit 38: Obstacle Pattern Generation
- Predefined obstacle sequences
- Pattern variety
- Fair challenge design
- Random pattern selection
- **Runnable:** Recognisable obstacle patterns

### Unit 39: Safe Gap Calculation
- Ensure jumpable gaps
- Ensure duckable sequences
- No impossible combinations
- Pattern validation
- **Runnable:** All patterns are completable

### Unit 40: Title Screen Design
- Game title display
- Press fire to start
- High score on title
- Basic title layout
- **Runnable:** Title screen displayed

### Unit 41: Title to Game Transition
- Input detection on title
- Initialise game state
- Reset score and position
- Smooth transition
- **Runnable:** Start game from title

### Unit 42: Game Over Screen
- Display game over message
- Show final score
- Compare to high score
- Return to title prompt
- **Runnable:** Game over screen with score

### Unit 43: Lives System
- Multiple lives per game
- Lives display (icons)
- Respawn after hit
- Brief invincibility
- **Runnable:** Three lives, respawn on hit

### Unit 44: Invincibility Flash
- Visual feedback during invincibility
- Sprite flashing effect
- Timer-based recovery
- Return to normal state
- **Runnable:** Flashing invincibility period

### Unit 45: Pickup Items - Coins
- Collectable coin items
- Bonus score for collection
- Coin spawn system
- Coin collision detection
- **Runnable:** Collect coins for bonus points

### Unit 46: Pickup Rendering
- Coin character or sprite
- Animated sparkle effect
- Collection feedback
- Score popup concept
- **Runnable:** Animated collectible coins

### Unit 47: Sound Effects Setup
- SID initialisation for effects
- Jump sound effect
- Collect sound effect
- Simple sound trigger system
- **Runnable:** Sound effects for actions

### Unit 48: Phase 3 Integration
- Complete game loop
- Title → Game → Game Over → Title
- Score, lives, difficulty
- Pickups and sounds
- **Runnable:** Full game structure complete

---

## Phase 4: Polish & Feel (Units 49-64)
*Visual and audio refinements*

### Unit 49: Raster Timing Basics
- Understanding raster beam
- VIC-II raster register ($D012)
- Raster interrupt concept
- Detecting raster position
- **Runnable:** Display current raster line

### Unit 50: Raster Interrupt Setup
- Configure raster interrupt
- IRQ handler for raster
- Acknowledge interrupt
- Stable raster timing
- **Runnable:** Raster interrupt fires reliably

### Unit 51: Sky Colour Gradient
- Split screen at horizon
- Sky colour above ground
- Raster-based colour change
- Clean colour transition
- **Runnable:** Blue sky above brown ground

### Unit 52: Multi-Colour Sky
- Multiple raster splits
- Gradient sky effect
- Dawn/dusk colour schemes
- Smooth colour bands
- **Runnable:** Gradient sky with multiple colours

### Unit 53: Parallax Layer Concept
- Background moves slower than foreground
- Depth illusion through speed difference
- Plan parallax layers
- Layer memory allocation
- **Runnable:** Parallax concept demonstration

### Unit 54: Far Background Layer
- Distant mountains/clouds
- Very slow scroll rate
- Character-based far layer
- Independent scroll counter
- **Runnable:** Distant background scrolls slowly

### Unit 55: Near Background Layer
- Closer background elements
- Medium scroll rate
- Trees or buildings
- Layer between far and ground
- **Runnable:** Two-layer parallax effect

### Unit 56: Parallax Colour Handling
- Each layer has distinct colours
- Colour RAM for each layer
- Raster splits for layers
- Clean layer transitions
- **Runnable:** Coloured parallax layers

### Unit 57: Ground Detail Variation
- Multiple ground tile types
- Random ground variation
- Occasional decorative elements
- Visual interest in terrain
- **Runnable:** Varied ground appearance

### Unit 58: Obstacle Detail Improvement
- More detailed obstacle graphics
- Multiple obstacle variations
- Rock, bush, log varieties
- Colour variations
- **Runnable:** Visually varied obstacles

### Unit 59: Death Animation
- Multi-frame death sequence
- Tumble or trip animation
- Brief pause before restart
- Impact feedback
- **Runnable:** Animated death sequence

### Unit 60: Music Introduction
- Background music for running
- Simple looping tune
- SID music playback
- Music tempo matches gameplay
- **Runnable:** Background music plays during game

### Unit 61: Music Tempo Scaling
- Music speed increases with game
- Dynamic tempo adjustment
- Tension building effect
- Maximum tempo cap
- **Runnable:** Music accelerates with difficulty

### Unit 62: Sound Polish
- Improved jump sound
- Landing sound
- Death sound
- Coin collect variation
- **Runnable:** Full sound effect suite

### Unit 63: Screen Shake Effect
- Brief shake on collision
- Offset screen position
- Rapid return to normal
- Impact feel enhancement
- **Runnable:** Screen shake on hit

### Unit 64: Phase 4 Integration
- All visual effects combined
- Parallax, colours, animations
- Music and sound complete
- Polished presentation
- **Runnable:** Visually polished runner

---

## Phase 5: Advanced Features (Units 65-80)
*Double buffering and advanced scrolling*

### Unit 65: Screen Tearing Analysis
- Understand screen tearing cause
- Visible during fast scroll
- Frame timing issues
- Need for synchronisation
- **Runnable:** Identify tearing in current build

### Unit 66: Double Buffer Concept
- Two screen buffers alternating
- Draw to hidden buffer
- Swap visible buffer
- Tear-free display
- **Runnable:** Double buffer explanation demo

### Unit 67: Memory Layout for Buffers
- Two 1K screen areas
- Bank switching considerations
- Colour RAM handling (single)
- Memory map planning
- **Runnable:** Dual buffer memory setup

### Unit 68: Buffer Swap Mechanism
- VIC-II screen pointer ($D018)
- Swap during vertical blank
- Synchronise with raster
- Clean swap implementation
- **Runnable:** Buffers swap cleanly

### Unit 69: Draw to Back Buffer
- Scroll updates to hidden buffer
- New column to back buffer
- Maintain synchronisation
- Performance considerations
- **Runnable:** Tear-free scrolling achieved

### Unit 70: Variable Scroll Speed
- Sub-pixel scroll accumulator
- Smooth speed transitions
- Fractional pixel movement
- Speed interpolation
- **Runnable:** Smooth speed variations

### Unit 71: Character Set Customisation
- Custom character set for game
- Specialised terrain characters
- Obstacle character designs
- Optimised character set
- **Runnable:** Custom character graphics

### Unit 72: Animated Terrain
- Animated ground characters
- Water or lava effects
- Character frame cycling
- Global animation timer
- **Runnable:** Animated terrain elements

### Unit 73: Sprite Multiplexing Intro
- More sprites than hardware limit
- Reuse sprites per frame
- Raster-based repositioning
- Multiplexer concept
- **Runnable:** Explain multiplexing need

### Unit 74: Basic Sprite Multiplexer
- Sort sprites by Y position
- Reposition during frame
- Two-sprite multiplexing
- Handle overlap cases
- **Runnable:** Extra sprites via multiplexing

### Unit 75: Multiple Sprite Enemies
- Flying enemies (birds)
- Sprite-based obstacles
- Independent movement
- Multiplexed display
- **Runnable:** Multiple flying enemies

### Unit 76: Enemy Movement Patterns
- Sine wave flight path
- Swooping attack pattern
- Varied enemy behaviours
- Pattern data structure
- **Runnable:** Enemies with movement patterns

### Unit 77: Sprite/Character Collision
- Sprite player vs character obstacles
- Mixed collision detection
- Accurate hitbox alignment
- Edge case handling
- **Runnable:** Accurate mixed collisions

### Unit 78: Power-Up System
- Speed boost power-up
- Invincibility power-up
- Magnet power-up (attract coins)
- Power-up duration timer
- **Runnable:** Collectible power-ups

### Unit 79: Power-Up Effects
- Visual effect for speed boost
- Shield effect for invincibility
- Magnet attraction animation
- Effect expiry warning
- **Runnable:** Active power-up visuals

### Unit 80: Phase 5 Integration
- Double buffering active
- Sprite multiplexing working
- Power-ups implemented
- Advanced features complete
- **Runnable:** Technically advanced runner

---

## Phase 6: Content & Variety (Units 81-96)
*Themes, levels, and content depth*

### Unit 81: Theme System Design
- Multiple visual themes
- Theme data structure
- Character set per theme
- Colour palette per theme
- **Runnable:** Theme system architecture

### Unit 82: Forest Theme
- Tree and bush obstacles
- Green/brown colour scheme
- Forest background parallax
- Woodland atmosphere
- **Runnable:** Forest-themed level

### Unit 83: Desert Theme
- Cactus and rock obstacles
- Orange/yellow colour scheme
- Desert background (dunes)
- Heat shimmer effect
- **Runnable:** Desert-themed level

### Unit 84: Night Theme
- Dark colour scheme
- Star background
- Glowing obstacles
- Moon in parallax layer
- **Runnable:** Night-themed level

### Unit 85: Theme Transitions
- Gradual theme change
- Colour fade between themes
- Character set swap timing
- Seamless visual transition
- **Runnable:** Smooth theme transitions

### Unit 86: Milestone Markers
- Distance milestone display
- Visual fanfare at milestones
- Increasing milestone values
- Achievement feedback
- **Runnable:** Milestone celebrations

### Unit 87: Bonus Stages
- Special bonus sections
- Coin-rich opportunities
- Temporary no-death mode
- Bonus stage transitions
- **Runnable:** Bonus stage sequences

### Unit 88: Boss Obstacles
- Large multi-part obstacles
- Requires precise timing
- Dramatic presentation
- Periodic boss appearances
- **Runnable:** Boss obstacle sequences

### Unit 89: Weather Effects
- Rain effect (character animation)
- Snow falling
- Wind visual cues
- Weather impacts gameplay
- **Runnable:** Weather visual effects

### Unit 90: Day/Night Cycle
- Gradual colour shift
- Time-based or distance-based
- Dawn to dusk progression
- Complete cycle
- **Runnable:** Dynamic day/night cycle

### Unit 91: Achievement System
- Track accomplishments
- First 1000 points, first boss, etc.
- Achievement notifications
- Persistence concept
- **Runnable:** Achievement tracking

### Unit 92: Statistics Tracking
- Total distance run
- Total coins collected
- Total deaths
- Best streak without hit
- **Runnable:** Statistics display screen

### Unit 93: Difficulty Modes
- Easy/Normal/Hard selection
- Adjust speeds and spawns
- Mode-specific high scores
- Title screen mode select
- **Runnable:** Multiple difficulty modes

### Unit 94: Practice Mode
- Slower speed option
- Infinite lives
- Learning mode for beginners
- No high score recording
- **Runnable:** Practice mode available

### Unit 95: Secret Features
- Hidden character skins
- Easter egg discovery
- Code input system
- Unlock notifications
- **Runnable:** Secret unlockables

### Unit 96: Phase 6 Integration
- All themes working
- Bonus and boss content
- Weather and cycles
- Full content variety
- **Runnable:** Content-rich experience

---

## Phase 7: Optimisation & Effects (Units 97-112)
*Performance and advanced effects*

### Unit 97: Performance Profiling
- Measure frame time usage
- Identify bottlenecks
- Raster line counter
- Performance display (debug)
- **Runnable:** Performance metrics visible

### Unit 98: Scroll Routine Optimisation
- Unrolled loops for speed
- Self-modifying code for shifts
- Optimised copy routines
- Measurable improvement
- **Runnable:** Faster scroll performance

### Unit 99: Collision Optimisation
- Spatial partitioning concept
- Check only nearby obstacles
- Early exit conditions
- Reduced collision checks
- **Runnable:** Efficient collision detection

### Unit 100: Memory Optimisation
- Compact data structures
- Reduced RAM usage
- Bank switching if needed
- Memory map refinement
- **Runnable:** Optimised memory layout

### Unit 101: Sprite Priority Effects
- Sprite behind/in front of characters
- Priority register ($D01B)
- Dynamic priority changes
- Depth layering effects
- **Runnable:** Sprite priority tricks

### Unit 102: Sprite Stretch Effects
- Sprite scaling tricks
- Y-stretch during raster
- Growth/shrink animations
- Power-up visual feedback
- **Runnable:** Sprite stretching effects

### Unit 103: Border Effects
- Open side borders
- Sprites in border area
- Extended play area feel
- Border colour effects
- **Runnable:** Open border display

### Unit 104: Advanced Raster Effects
- Multiple raster splits
- Complex colour cycling
- Raster bar effects
- Demo-style visuals
- **Runnable:** Advanced raster display

### Unit 105: Screen Flash Effects
- Full screen colour flash
- Flash on special events
- Rapid colour cycling
- Impact emphasis
- **Runnable:** Dramatic flash effects

### Unit 106: Copper-Style Bars
- Horizontal colour bars
- Moving bar animation
- Background decoration
- C64 "copper" equivalent
- **Runnable:** Animated colour bars

### Unit 107: Score Popup Animation
- Numbers float up from collection
- Animated score addition
- Multiple simultaneous popups
- Smooth animation
- **Runnable:** Floating score popups

### Unit 108: Smooth Camera
- Slight player position variation
- Camera lag effect
- Speed-based position
- Enhanced movement feel
- **Runnable:** Dynamic camera position

### Unit 109: Combo System
- Chain obstacle dodges
- Multiplier for chains
- Combo counter display
- Combo break feedback
- **Runnable:** Combo scoring system

### Unit 110: Near Miss Bonus
- Detect close obstacle passes
- Bonus points for near miss
- Visual near-miss feedback
- Risk/reward gameplay
- **Runnable:** Near miss detection

### Unit 111: Turbo Mode
- Maximum speed challenge
- Earned through gameplay
- Extreme difficulty option
- Turbo-specific effects
- **Runnable:** Turbo speed mode

### Unit 112: Phase 7 Integration
- All optimisations applied
- Special effects complete
- Combo and scoring refined
- High-performance build
- **Runnable:** Optimised, polished game

---

## Phase 8: Final Polish & Release (Units 113-128)
*Final quality and release preparation*

### Unit 113: Bug Sweep
- Systematic bug testing
- Edge case identification
- Fix remaining issues
- Stability verification
- **Runnable:** Bug-free gameplay

### Unit 114: Balance Testing
- Difficulty curve analysis
- Fair challenge verification
- Spawn rate tuning
- Speed progression refinement
- **Runnable:** Well-balanced difficulty

### Unit 115: Control Polish
- Input responsiveness check
- Jump timing refinement
- Duck responsiveness
- Tight control feel
- **Runnable:** Responsive controls

### Unit 116: Audio Mix
- Balance music and effects
- Volume levels appropriate
- No audio clipping
- Pleasant audio mix
- **Runnable:** Well-mixed audio

### Unit 117: Loading Screen
- Visual while loading
- Progress indication
- Game branding
- Professional presentation
- **Runnable:** Attractive loading screen

### Unit 118: Credits Screen
- Developer credits
- Thank you messages
- Music credits
- Accessible from title
- **Runnable:** Credits screen

### Unit 119: Instructions Screen
- How to play guide
- Control diagram
- Tips for beginners
- Accessible from title
- **Runnable:** Help/instructions screen

### Unit 120: Save High Scores
- Persist high score to disk
- Load on game start
- Handle missing file
- Optional save feature
- **Runnable:** Persistent high scores

### Unit 121: Tape/Disk Compatibility
- Test on tape loading
- Test on disk systems
- Fast loader consideration
- Media compatibility
- **Runnable:** Works on both media types

### Unit 122: PAL/NTSC Testing
- Verify on both systems
- Timing adjustments if needed
- Speed consistency
- Visual consistency
- **Runnable:** Works on PAL and NTSC

### Unit 123: Memory Clean-Up
- Remove debug code
- Optimise final build
- Strip unused data
- Minimal final footprint
- **Runnable:** Clean release build

### Unit 124: Final Performance Check
- Verify frame rate stability
- No slowdown in gameplay
- Consistent performance
- Release quality
- **Runnable:** Stable 50/60 fps

### Unit 125: Playtesting
- Extended play sessions
- Varied play styles
- Difficulty feedback
- Polish notes
- **Runnable:** Playtested build

### Unit 126: Final Polish Pass
- Address playtesting feedback
- Minor visual tweaks
- Last balance adjustments
- Final improvements
- **Runnable:** Fully polished game

### Unit 127: Release Build
- Create final PRG file
- Verify clean load
- Test fresh start
- Release candidate
- **Runnable:** Release-ready build

### Unit 128: Project Retrospective
- Document techniques learned
- VIC-II scrolling mastery
- Double buffering skills
- Foundation for future scrolling games
- **Runnable:** Complete Scroll Runner

---

## Technical Summary

### Key Hardware Features Used
- VIC-II horizontal scroll register ($D016)
- Raster interrupts for timing
- Sprite multiplexing
- Double buffering (dual screens)
- Custom character set

### Code Patterns Introduced
```asm
; Hardware horizontal scroll
scroll_screen:
    dec fine_scroll
    bpl .no_coarse
    lda #7
    sta fine_scroll
    jsr shift_screen_left
.no_coarse:
    lda fine_scroll
    ora #$C8              ; multicolour mode bits
    sta $D016
    rts

; Double buffer swap
swap_buffers:
    lda current_buffer
    eor #1
    sta current_buffer
    tax
    lda screen_hi_table,x
    sta $D018
    rts
```

### Skills Progression
| Phase | Primary Skills |
|-------|---------------|
| 1 | Hardware scroll basics, screen memory |
| 2 | Sprite control, jumping physics |
| 3 | Scoring, difficulty progression |
| 4 | Raster effects, parallax, music |
| 5 | Double buffering, multiplexing |
| 6 | Themes, content variety |
| 7 | Optimisation, special effects |
| 8 | Polish, release preparation |

---

## Version History
- v1.0 - Initial 128-unit outline
