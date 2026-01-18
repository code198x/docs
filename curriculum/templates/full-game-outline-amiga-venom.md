# Game 7: Venom - Complete 128-Unit Outline

## Game Overview
**Platform:** Commodore Amiga
**Genre:** Snake / Growing entity game
**Concept:** Classic snake game with Amiga hardware rendering. Uses ring buffer data structure for efficient body management. Showcases Blitter for smooth segment rendering.

**Technical Focus:**
- Ring buffer implementation in 68000
- Blitter-based segment rendering
- Grid-based movement system
- Self-collision detection
- Speed scaling mechanics
- Copper colour effects

---

## Phase 1: Foundation (Units 1-16)
*Establish display and snake head*

### Unit 1: Project Setup
- Create venom project structure
- Set up Amiga memory layout
- Initialise custom chips
- System takeover setup
- **Runnable:** Clean startup achieved

### Unit 2: Display Configuration
- Set up bitplane display
- Choose colour depth (4-8 colours)
- Configure display dimensions
- Playfield setup
- **Runnable:** Display initialised

### Unit 3: Colour Palette Design
- Snake colours (head/body)
- Background colour
- Food and wall colours
- Copper list for palette
- **Runnable:** Game palette set

### Unit 4: Play Area Layout
- Define grid boundaries
- Border wall design
- Calculate screen positions
- Grid to pixel mapping
- **Runnable:** Play area concept

### Unit 5: Border Rendering
- Draw play area border
- Use Blitter for lines
- Solid boundary walls
- Clear interior
- **Runnable:** Bordered play area

### Unit 6: Grid System
- Grid cell size (8x8 or 16x16 pixels)
- Grid coordinate system
- Total grid dimensions
- Coordinate conversion routines
- **Runnable:** Grid system tested

### Unit 7: Snake Head Design
- Head graphic (small bob or tile)
- Four directional variants
- Distinct head appearance
- Blitter-friendly format
- **Runnable:** Head graphics ready

### Unit 8: Draw Snake Head
- Position head on grid
- Blitter copy to screen
- Initial position (centre)
- Head visible on screen
- **Runnable:** Snake head displayed

### Unit 9: Movement Variables
- Current X, Y grid position
- Current direction (0-3)
- Movement speed/timing
- State variables initialised
- **Runnable:** Variables ready

### Unit 10: Input Detection
- Joystick reading
- Direction mapping
- Keyboard alternative
- Input polling routine
- **Runnable:** Input detected

### Unit 11: Direction Control
- Change direction on input
- Prevent 180-degree turn
- Direction state machine
- Smooth direction changes
- **Runnable:** Direction changes work

### Unit 12: Basic Movement
- Move head each tick
- Clear old position
- Draw at new position
- Grid-aligned movement
- **Runnable:** Head moves on grid

### Unit 13: Movement Timing
- VBlank-based timing
- Frame counter for speed
- Consistent movement rate
- Adjustable tick rate
- **Runnable:** Timed movement

### Unit 14: Wall Collision
- Detect head vs border
- Grid boundary check
- Stop on collision
- Game over state
- **Runnable:** Wall collision works

### Unit 15: Game Over State
- Freeze on collision
- Display game over
- Wait for restart
- State management
- **Runnable:** Game over handling

### Unit 16: Phase 1 Integration
- Complete head movement
- Direction control
- Wall collision
- Foundation complete
- **Runnable:** Moving snake head

---

## Phase 2: Core Mechanics (Units 17-32)
*Ring buffer and snake body*

### Unit 17: Ring Buffer Concept
- Why ring buffer for snake
- Fixed memory allocation
- Head and tail pointers
- Efficient add/remove
- **Runnable:** Concept explained

### Unit 18: Buffer Data Structure
- Body X coordinate array
- Body Y coordinate array
- Head index variable
- Tail index variable
- **Runnable:** Structure defined

### Unit 19: Buffer Size Planning
- Maximum snake length
- Array sizing
- Memory allocation
- Index wrap calculation
- **Runnable:** Buffer allocated

### Unit 20: Add Segment Operation
- Increment head index
- Handle wrap-around
- Store new position
- Index management
- **Runnable:** Add operation works

### Unit 21: Remove Segment Operation
- Increment tail index
- Handle wrap-around
- Clear old position
- Tail follows head
- **Runnable:** Remove operation works

### Unit 22: Snake Length Tracking
- Current length variable
- Length calculation from indices
- Growth affects length
- Length display
- **Runnable:** Length tracked

### Unit 23: Body Segment Graphics
- Body segment design
- Uniform body appearance
- Blitter-compatible format
- Distinct from head
- **Runnable:** Body graphics ready

### Unit 24: Render Full Snake
- Loop through buffer
- Draw each segment
- Tail to head order
- Complete snake visible
- **Runnable:** Full snake rendered

### Unit 25: Movement with Buffer
- Add new head to buffer
- Remove old tail (no growth)
- Efficient screen update
- Smooth movement
- **Runnable:** Snake moves correctly

### Unit 26: Food System
- Food position variables
- Single food item
- Random placement
- Food graphic design
- **Runnable:** Food displayed

### Unit 27: Valid Food Placement
- Not on snake body
- Not on walls
- Grid-aligned position
- Retry on invalid
- **Runnable:** Valid food spawns

### Unit 28: Food Collision
- Head position vs food
- Simple coordinate check
- Eat detection flag
- Food disappears
- **Runnable:** Food eaten

### Unit 29: Growth Mechanic
- Skip tail removal on eat
- Snake extends by one
- Length increases
- Growth feedback
- **Runnable:** Snake grows

### Unit 30: Food Respawn
- New food after eating
- Random new position
- Continuous supply
- Game continues
- **Runnable:** Food respawns

### Unit 31: Self-Collision
- Head vs body check
- Loop through segments
- Game over on hit
- Increasing difficulty
- **Runnable:** Self-collision works

### Unit 32: Phase 2 Integration
- Ring buffer complete
- Growth mechanic working
- Self-collision active
- Core snake gameplay
- **Runnable:** Complete snake game

---

## Phase 3: Game Systems (Units 33-48)
*Scoring, speed, and structure*

### Unit 33: Score System
- Points per food
- Score variable (long)
- Score accumulation
- Score tracking
- **Runnable:** Score increments

### Unit 34: Score Display
- Score position on screen
- Number rendering routine
- Decimal conversion
- Formatted display
- **Runnable:** Score displayed

### Unit 35: High Score
- Best score tracking
- Compare on game over
- Update if beaten
- Persist in memory
- **Runnable:** High score tracked

### Unit 36: Speed Progression
- Faster with length
- Reduce frame delay
- Speed curve design
- Maximum speed cap
- **Runnable:** Speed increases

### Unit 37: Speed Implementation
- Variable tick rate
- Speed lookup table
- Smooth progression
- Playable at all speeds
- **Runnable:** Speed scaling works

### Unit 38: Level System
- Multiple levels
- Target length per level
- Level progression
- Level counter
- **Runnable:** Level tracking

### Unit 39: Level Completion
- Reach target length
- Level complete message
- Brief celebration
- Advance to next
- **Runnable:** Level completion

### Unit 40: Level Reset
- Reset snake position
- Keep score
- Reset length to minimum
- New level layout
- **Runnable:** Level transition

### Unit 41: Maze Obstacles
- Interior walls
- Level-specific layouts
- Obstacle data structure
- Render obstacles
- **Runnable:** Maze walls displayed

### Unit 42: Maze Collision
- Head vs maze walls
- Additional collision check
- Game over on hit
- Navigation challenge
- **Runnable:** Maze collision works

### Unit 43: Title Screen
- Game title display
- Start prompt
- High score shown
- Attractive title
- **Runnable:** Title screen

### Unit 44: Title Animation
- Animated snake on title
- Copper colour effects
- Eye-catching display
- Attract mode feel
- **Runnable:** Animated title

### Unit 45: Lives System
- Three lives per game
- Lives display
- Death reduces lives
- Game over at zero
- **Runnable:** Lives system

### Unit 46: Respawn
- Brief invincibility
- Reset position
- Keep score and level
- Continue playing
- **Runnable:** Respawn works

### Unit 47: Pause Feature
- Pause key detection
- Freeze gameplay
- Pause message
- Resume function
- **Runnable:** Pause implemented

### Unit 48: Phase 3 Integration
- Speed progression
- Multiple levels
- Lives and scoring
- Complete game structure
- **Runnable:** Full game loop

---

## Phase 4: Polish & Feel (Units 49-64)
*Visual and audio refinement*

### Unit 49: Copper Background
- Gradient background
- Copper colour changes
- Atmospheric effect
- Visual depth
- **Runnable:** Copper background

### Unit 50: Animated Background
- Moving gradient
- Copper list animation
- Subtle movement
- Living background
- **Runnable:** Animated copper

### Unit 51: Snake Colour Gradient
- Body colour varies
- Head to tail gradient
- Ring buffer colour index
- Visual length indication
- **Runnable:** Gradient snake

### Unit 52: Improved Head Graphics
- Detailed head sprite
- Directional variants
- Eye detail
- Personality
- **Runnable:** Detailed head

### Unit 53: Body Segment Variety
- Corner pieces
- Straight pieces
- Direction-aware segments
- Smooth connections
- **Runnable:** Varied body

### Unit 54: Tail Graphics
- Distinct tail piece
- Points in direction
- Completes snake look
- Visual endpoint
- **Runnable:** Tail graphics

### Unit 55: Food Animation
- Pulsing food item
- Frame animation
- Eye-catching movement
- Encourages collection
- **Runnable:** Animated food

### Unit 56: Eat Animation
- Flash on eat
- Growth visual feedback
- Quick colour change
- Satisfying feedback
- **Runnable:** Eat animation

### Unit 57: Death Animation
- Snake blinks/flashes
- Segment fade or explosion
- Dramatic effect
- Clear death feedback
- **Runnable:** Death animation

### Unit 58: Paula Sound Setup
- Audio channel allocation
- Sample playback setup
- Sound effect system
- Trigger mechanism
- **Runnable:** Sound ready

### Unit 59: Movement Sound
- Subtle movement sound
- Optional slither sound
- Not annoying
- Ambient feedback
- **Runnable:** Movement audio

### Unit 60: Eat Sound Effect
- Satisfying crunch
- Pitched variation
- Positive feedback
- Encouraging audio
- **Runnable:** Eat sound

### Unit 61: Death Sound
- Dramatic death sound
- Failure feedback
- Distinct from other sounds
- Impact sound
- **Runnable:** Death sound

### Unit 62: Background Music
- Module playback
- Puzzle game music
- Looping track
- Tempo consideration
- **Runnable:** Background music

### Unit 63: HUD Polish
- Clean score display
- Level indicator
- Lives display
- Professional layout
- **Runnable:** Polished HUD

### Unit 64: Phase 4 Integration
- All visuals polished
- Sound effects complete
- Music playing
- Professional presentation
- **Runnable:** Polished game

---

## Phase 5: Advanced Features (Units 65-80)
*Advanced mechanics and modes*

### Unit 65: Bonus Food
- Special bonus items
- Higher point value
- Timed appearance
- Risk/reward
- **Runnable:** Bonus food spawns

### Unit 66: Bonus Timer
- Countdown display
- Item disappears
- Urgency mechanic
- Timer visual
- **Runnable:** Timed bonus

### Unit 67: Power-Up System
- Multiple power-up types
- Power-up data structure
- Spawn system
- Duration tracking
- **Runnable:** Power-up framework

### Unit 68: Speed Power-Up
- Slow-down effect
- Temporary relief
- Duration timer
- Visual indicator
- **Runnable:** Speed power-up

### Unit 69: Ghost Power-Up
- Pass through body
- Temporary invincibility
- Ghost visual effect
- Strategic use
- **Runnable:** Ghost power-up

### Unit 70: Score Multiplier
- 2x score power-up
- Duration-based
- Multiplier display
- Point bonuses
- **Runnable:** Score multiplier

### Unit 71: Two-Player Design
- Split screen concept
- Competitive mode
- Independent controls
- Win condition
- **Runnable:** Two-player design

### Unit 72: Two-Player Split Screen
- Divided display
- Two play areas
- Controller mapping
- Visual separation
- **Runnable:** Split screen display

### Unit 73: Two-Player Gameplay
- Simultaneous play
- Independent snakes
- Compete for food
- Score comparison
- **Runnable:** Two-player game

### Unit 74: AI Snake
- Computer opponent
- Basic pathfinding
- Food seeking
- Avoidance logic
- **Runnable:** AI snake moves

### Unit 75: AI Difficulty
- Easy/Medium/Hard AI
- Decision quality varies
- Selectable opponent
- Fair challenge
- **Runnable:** AI difficulty levels

### Unit 76: Wrap-Around Mode
- Screen edges connect
- No wall death
- Different strategy
- Optional mode
- **Runnable:** Wrap mode

### Unit 77: Survival Mode
- Endless play
- No level targets
- Score focus only
- High score chase
- **Runnable:** Survival mode

### Unit 78: Time Attack
- Time limit
- Eat fastest
- Time bonus items
- Frantic gameplay
- **Runnable:** Time attack mode

### Unit 79: Mode Selection
- Mode menu
- Clear descriptions
- Easy selection
- Mode variety
- **Runnable:** Mode menu

### Unit 80: Phase 5 Integration
- All power-ups working
- Multiple modes
- Two-player option
- Feature-complete
- **Runnable:** Advanced snake game

---

## Phase 6: Content & Variety (Units 81-96)
*Themes, levels, and content*

### Unit 81: Level Pack 1
- Levels 1-5 design
- Increasing maze complexity
- Fair progression
- Balanced difficulty
- **Runnable:** First level pack

### Unit 82: Level Pack 2
- Levels 6-10
- More complex mazes
- New obstacle patterns
- Greater challenge
- **Runnable:** Second level pack

### Unit 83: Level Pack 3
- Levels 11-15
- Expert difficulty
- Tight navigation
- Mastery required
- **Runnable:** Advanced levels

### Unit 84: Moving Obstacles
- Mobile hazards
- Pattern movement
- Timing challenge
- Dynamic levels
- **Runnable:** Moving obstacles

### Unit 85: Teleport Portals
- Portal pairs
- Enter one, exit other
- Strategic shortcuts
- Disorientation risk
- **Runnable:** Portals work

### Unit 86: Theme System
- Multiple visual themes
- Graphics per theme
- Colour palette per theme
- Theme data
- **Runnable:** Theme framework

### Unit 87: Jungle Theme
- Green palette
- Vine/leaf graphics
- Nature aesthetic
- Themed snake
- **Runnable:** Jungle theme

### Unit 88: Tech Theme
- Neon colours
- Circuit board style
- Digital aesthetic
- Futuristic feel
- **Runnable:** Tech theme

### Unit 89: Desert Theme
- Sand colours
- Desert snake style
- Warm palette
- Atmospheric
- **Runnable:** Desert theme

### Unit 90: Theme Selection
- Choose before game
- Theme preview
- Save preference
- Easy access
- **Runnable:** Theme menu

### Unit 91: Achievement System
- Track accomplishments
- Milestone achievements
- Achievement data
- Progress tracking
- **Runnable:** Achievements

### Unit 92: Achievement Display
- Achievement list
- Unlock status
- Achievement notification
- Progress view
- **Runnable:** Achievement screen

### Unit 93: Statistics
- Games played
- Food eaten total
- Distance travelled
- Best performances
- **Runnable:** Statistics screen

### Unit 94: Challenge Mode
- Specific challenges
- Pre-set scenarios
- Goal-based play
- Variety
- **Runnable:** Challenge mode

### Unit 95: Tutorial
- Guided introduction
- Basic controls
- Demonstrate growth
- Welcoming start
- **Runnable:** Tutorial mode

### Unit 96: Phase 6 Integration
- All levels complete
- Themes working
- Achievements and stats
- Content complete
- **Runnable:** Full content

---

## Phase 7: Optimisation & Effects (Units 97-112)
*Performance and effects*

### Unit 97: Performance Analysis
- Measure frame timing
- Identify bottlenecks
- Ring buffer efficiency
- Rendering speed
- **Runnable:** Performance data

### Unit 98: Ring Buffer Optimisation
- 68000 efficient code
- Minimise memory access
- Index calculations
- Faster operations
- **Runnable:** Optimised buffer

### Unit 99: Collision Optimisation
- Early exit checks
- Efficient loop
- Spatial shortcuts
- Faster collision
- **Runnable:** Fast collision

### Unit 100: Blitter Optimisation
- Efficient blit setup
- Minimise Blitter waits
- Batch operations
- Faster rendering
- **Runnable:** Optimised Blitter

### Unit 101: Trail Effect
- Ghost trail behind snake
- Fading segments
- Visual speed indicator
- Optional effect
- **Runnable:** Trail effect

### Unit 102: Rainbow Effect
- Colour-cycling body
- Copper colour changes
- Celebratory effect
- Power-up visual
- **Runnable:** Rainbow snake

### Unit 103: Screen Transitions
- Wipe effects between screens
- Fade transitions
- Professional flow
- Smooth changes
- **Runnable:** Screen transitions

### Unit 104: Particle Effects
- Food collection particles
- Death explosion
- Blitter particles
- Visual flair
- **Runnable:** Particle system

### Unit 105: Score Popup
- Floating score numbers
- Rise and fade
- Collection feedback
- Satisfying visuals
- **Runnable:** Score popups

### Unit 106: Combo System
- Chain food collection
- Score multiplier
- Combo counter
- Skill reward
- **Runnable:** Combo system

### Unit 107: High Score Entry
- Name input
- Keyboard handling
- Character limit
- Save with score
- **Runnable:** Name entry

### Unit 108: High Score Table
- Top 10 display
- Names and scores
- New entry highlight
- Sorted list
- **Runnable:** Score table

### Unit 109: Score Persistence
- Save to disk
- Load on start
- Handle missing file
- Reliable storage
- **Runnable:** Persistent scores

### Unit 110: Demo Mode
- Automated gameplay
- AI plays on title
- Attract mode
- Shows features
- **Runnable:** Demo mode

### Unit 111: Copper Tricks
- Advanced copper effects
- Raster bars
- Dynamic palette
- Amiga showcase
- **Runnable:** Copper effects

### Unit 112: Phase 7 Integration
- All optimisations
- Effects complete
- High scores working
- Polished build
- **Runnable:** Optimised game

---

## Phase 8: Final Polish & Release (Units 113-128)
*Final quality and release*

### Unit 113: Bug Testing
- Systematic testing
- Edge cases
- Fix all issues
- Stable build
- **Runnable:** Bug-free game

### Unit 114: Balance Testing
- Difficulty progression
- Speed curve
- Fair challenge
- Tuned gameplay
- **Runnable:** Balanced game

### Unit 115: Control Polish
- Input responsiveness
- Direction timing
- Comfortable feel
- Tight controls
- **Runnable:** Responsive controls

### Unit 116: Audio Balance
- Sound levels
- Music volume
- No clipping
- Pleasant mix
- **Runnable:** Balanced audio

### Unit 117: Loading Screen
- Attractive loader
- Progress indication
- Branding
- Professional start
- **Runnable:** Loading screen

### Unit 118: Credits
- Developer credits
- Acknowledgements
- Music credits
- Thank you
- **Runnable:** Credits screen

### Unit 119: Instructions
- How to play
- Controls
- Tips
- Help available
- **Runnable:** Instructions

### Unit 120: Options Menu
- Sound toggle
- Music toggle
- Theme selection
- Preferences
- **Runnable:** Options menu

### Unit 121: Chip RAM Check
- Verify memory usage
- Chip RAM requirements
- Fast RAM optimisation
- Memory efficient
- **Runnable:** Memory verified

### Unit 122: A500 Compatibility
- Test on A500 specs
- 512K chip RAM
- OCS compatibility
- Wide compatibility
- **Runnable:** A500 compatible

### Unit 123: Disk Format
- Create bootable ADF
- Proper boot block
- File structure
- Disk-ready
- **Runnable:** ADF created

### Unit 124: Final Performance
- Stable 50fps
- No slowdown
- Consistent timing
- Release quality
- **Runnable:** Stable performance

### Unit 125: Playtesting
- Extended sessions
- Multiple testers
- Feedback gathering
- Final notes
- **Runnable:** Playtested

### Unit 126: Final Polish
- Address feedback
- Last tweaks
- Complete polish
- Final version
- **Runnable:** Polished game

### Unit 127: Release Build
- Final disk image
- Verify boot
- Complete testing
- Release candidate
- **Runnable:** Release ADF

### Unit 128: Project Retrospective
- Techniques learned
- Ring buffer mastery
- Blitter skills
- Future foundations
- **Runnable:** Complete Venom

---

## Technical Summary

### Key Amiga Features Used
- Blitter for segment rendering
- Copper for colour effects
- Paula for sound/music
- Efficient 68000 code

### Code Patterns Introduced
```asm
; Ring buffer add (68000)
add_segment:
    move.w  head_index,d0
    addq.w  #1,d0
    cmp.w   #MAX_LENGTH,d0
    blt.s   .no_wrap
    clr.w   d0
.no_wrap:
    move.w  d0,head_index
    lea     body_x,a0
    add.w   d0,d0              ; word index
    move.w  snake_x,(a0,d0.w)
    lea     body_y,a0
    move.w  snake_y,(a0,d0.w)
    rts

; Self-collision check
check_self_collision:
    move.w  snake_length,d7
    subq.w  #1,d7              ; don't check head
    move.w  tail_index,d0
.loop:
    ; compare position at index d0 with head
    ; return if collision
    addq.w  #1,d0
    cmp.w   #MAX_LENGTH,d0
    blt.s   .no_wrap
    clr.w   d0
.no_wrap:
    dbf     d7,.loop
    rts
```

### Skills Progression
| Phase | Primary Skills |
|-------|---------------|
| 1 | Display setup, grid system |
| 2 | Ring buffer, growth |
| 3 | Scoring, speed, levels |
| 4 | Copper effects, audio |
| 5 | Power-ups, multiplayer |
| 6 | Themes, content |
| 7 | Optimisation, effects |
| 8 | Polish, release |

---

## Version History
- v1.0 - Initial 128-unit outline
