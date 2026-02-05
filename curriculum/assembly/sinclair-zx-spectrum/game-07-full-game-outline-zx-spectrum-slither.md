# Game 7: Slither - Complete 128-Unit Outline

## Game Overview
**Platform:** Sinclair ZX Spectrum
**Genre:** Snake / Growing entity game
**Concept:** Classic snake game - eat food, grow longer, avoid hitting yourself or walls. Teaches ring buffer data structure and self-collision detection.

**Technical Focus:**
- Ring buffer for body segment storage
- Grid-based movement system
- Self-collision detection algorithms
- Growing entity management
- Speed progression mechanics
- Maze obstacle integration

---

## Phase 1: Foundation (Units 1-16)
*Establish game display and snake head*

### Unit 1: Project Setup
- Create slither project structure
- Set up memory map for snake game
- Initialise screen mode
- Clear screen to play area
- **Runnable:** Clean game screen displayed

### Unit 2: Play Area Design
- Define play area boundaries
- Border wall characters
- Draw rectangular border
- Establish coordinate system
- **Runnable:** Bordered play area displayed

### Unit 3: Grid System
- Define grid cell size (character cells)
- X and Y grid coordinates
- Grid to screen conversion
- Screen to grid conversion
- **Runnable:** Grid coordinate demonstration

### Unit 4: Snake Head Design
- Design snake head character
- UDG definition for head
- Four directions (up/down/left/right)
- Direction-specific head graphics
- **Runnable:** Snake head character displayed

### Unit 5: Head Position Variables
- X and Y position storage
- Current direction variable
- Initialise starting position
- Display head at position
- **Runnable:** Snake head at start position

### Unit 6: Input Detection
- Keyboard input reading
- QAOP or cursor keys
- Direction key mapping
- Input polling loop
- **Runnable:** Direction keys detected

### Unit 7: Direction State Machine
- Change direction on input
- Prevent 180-degree reversal
- Direction state variable
- Valid direction transitions
- **Runnable:** Direction changes correctly

### Unit 8: Basic Movement
- Move head each frame
- Update position based on direction
- Clear old position
- Draw at new position
- **Runnable:** Snake head moves with input

### Unit 9: Movement Timing
- Movement speed control
- Frame counter for timing
- Delay between moves
- Consistent movement rate
- **Runnable:** Controlled movement speed

### Unit 10: Wall Collision
- Detect head vs border
- Check boundary coordinates
- Stop game on wall hit
- Collision flag
- **Runnable:** Game stops at walls

### Unit 11: Game Over State
- Game over detection
- Display game over message
- Freeze gameplay
- Press key to restart
- **Runnable:** Game over on wall collision

### Unit 12: Restart Mechanism
- Reset snake position
- Clear game state
- Return to gameplay
- Fresh start each time
- **Runnable:** Game restarts properly

### Unit 13: Body Segment Concept
- Snake has head and body
- Body follows head
- Plan data structure for body
- Understand following mechanic
- **Runnable:** Concept demonstration

### Unit 14: Single Body Segment
- One segment follows head
- Store previous head position
- Draw body segment
- Two-part snake
- **Runnable:** Head with one body segment

### Unit 15: Body Segment Graphics
- Design body segment character
- UDG for body
- Distinguish from head
- Visual snake appearance
- **Runnable:** Visual head and body distinction

### Unit 16: Phase 1 Integration
- Complete movement system
- Wall collision working
- Head and one body segment
- Foundation complete
- **Runnable:** Basic moving snake

---

## Phase 2: Core Mechanics (Units 17-32)
*Ring buffer and growing snake*

### Unit 17: Ring Buffer Concept
- Why ring buffer for snake
- Fixed memory, variable length
- Head and tail pointers
- Circular array concept
- **Runnable:** Ring buffer explanation

### Unit 18: Ring Buffer Data Structure
- Body X array (fixed size)
- Body Y array (fixed size)
- Head index pointer
- Tail index pointer
- **Runnable:** Data structure initialised

### Unit 19: Ring Buffer Operations
- Add segment at head
- Remove segment at tail
- Index wrapping logic
- Length calculation
- **Runnable:** Ring buffer operations test

### Unit 20: Snake Length Variable
- Current length counter
- Maximum length constant
- Length determines visible segments
- Growth increments length
- **Runnable:** Length tracking

### Unit 21: Full Body Rendering
- Loop through ring buffer
- Draw each body segment
- Start from tail to head
- Complete snake display
- **Runnable:** Multi-segment snake displayed

### Unit 22: Movement with Ring Buffer
- Add new head position to buffer
- Move tail pointer (no growth)
- Clear old tail position
- Efficient update
- **Runnable:** Snake moves via ring buffer

### Unit 23: Food Item Basics
- Food position variables
- Single food on screen
- Random position generation
- Display food character
- **Runnable:** Food item displayed

### Unit 24: Food Placement Rules
- Not on snake body
- Not on walls
- Valid grid positions only
- Retry if invalid
- **Runnable:** Valid food placement

### Unit 25: Food Collision Detection
- Head position vs food position
- Simple coordinate comparison
- Eat detection flag
- Food disappears on eat
- **Runnable:** Food eaten detection

### Unit 26: Growth Mechanic
- On food eat, skip tail move
- Tail stays, head extends
- Length increases
- Snake grows by one
- **Runnable:** Snake grows when eating

### Unit 27: Food Respawn
- Spawn new food after eat
- New random position
- Immediate or delayed respawn
- Continuous food supply
- **Runnable:** Food respawns after eaten

### Unit 28: Self-Collision Concept
- Snake cannot hit its body
- Must check head vs all segments
- Game over on self-collision
- Challenge increases with length
- **Runnable:** Self-collision explained

### Unit 29: Self-Collision Detection
- Loop through body positions
- Compare head to each segment
- Skip head position itself
- Efficient collision check
- **Runnable:** Self-collision detected

### Unit 30: Self-Collision Response
- Trigger game over
- Same as wall collision response
- Clear collision state on restart
- Consistent game over handling
- **Runnable:** Game over on self-collision

### Unit 31: Score System
- Points per food eaten
- Score variable
- Score display on screen
- Running total
- **Runnable:** Score tracks food eaten

### Unit 32: Phase 2 Integration
- Ring buffer fully working
- Growth mechanic complete
- Self-collision active
- Core snake gameplay
- **Runnable:** Complete snake mechanics

---

## Phase 3: Game Systems (Units 33-48)
*Speed progression and game structure*

### Unit 33: Speed Increase Design
- Faster after eating
- Gradual speed curve
- Maximum speed cap
- Speed creates challenge
- **Runnable:** Speed progression design

### Unit 34: Speed Implementation
- Reduce movement delay
- Speed based on length or score
- Minimum delay value
- Smooth speed increase
- **Runnable:** Game speeds up as you grow

### Unit 35: Level System Concept
- Multiple play areas
- Increasing difficulty
- Level completion conditions
- Progressive challenges
- **Runnable:** Level system design

### Unit 36: Level Completion
- Reach target length
- Target displayed on screen
- Level complete message
- Advance to next level
- **Runnable:** Level completion detection

### Unit 37: Level Data Structure
- Level configuration data
- Target length per level
- Starting speed per level
- Level-specific parameters
- **Runnable:** Level data loaded

### Unit 38: Level Transition
- Brief celebration
- Reset snake position
- Keep score, reset length
- Load next level config
- **Runnable:** Smooth level transitions

### Unit 39: Maze Obstacles
- Interior walls in play area
- Block certain paths
- Level-specific layouts
- Obstacle collision detection
- **Runnable:** Maze walls displayed

### Unit 40: Maze Collision
- Head vs maze wall collision
- Same response as border
- Game over on maze hit
- Adds navigation challenge
- **Runnable:** Maze collision working

### Unit 41: Maze Level Designs
- Level 1: Open field
- Level 2: Central obstacle
- Level 3: Corner walls
- Progressive complexity
- **Runnable:** Multiple maze layouts

### Unit 42: Title Screen
- Game title display
- Press key to start
- High score display
- Basic title presentation
- **Runnable:** Title screen displayed

### Unit 43: Title Screen Polish
- Animated snake on title
- Colour cycling effects
- Attract mode concept
- Professional appearance
- **Runnable:** Polished title screen

### Unit 44: High Score Tracking
- Track best score
- Update when beaten
- Display on game over
- Display on title
- **Runnable:** High score tracked

### Unit 45: Pause Feature
- Pause key detection
- Freeze gameplay
- Display pause message
- Resume on key press
- **Runnable:** Pausable game

### Unit 46: Lives System
- Multiple lives per game
- Lives display
- Respawn on death
- Game over when lives exhausted
- **Runnable:** Three lives system

### Unit 47: Respawn Mechanic
- Brief invincibility
- Reset snake position and length
- Keep score and level
- Visual respawn feedback
- **Runnable:** Respawn after death

### Unit 48: Phase 3 Integration
- Speed progression active
- Multiple levels with mazes
- Lives and respawning
- Full game structure
- **Runnable:** Complete game loop

---

## Phase 4: Polish & Feel (Units 49-64)
*Visual and audio improvements*

### Unit 49: Snake Body Variety
- Different body segment types
- Corner pieces
- Straight pieces
- Tail piece
- **Runnable:** Varied body graphics

### Unit 50: Direction-Aware Body
- Body knows entry/exit directions
- Select appropriate piece
- Smooth visual connections
- No jarring transitions
- **Runnable:** Smooth body rendering

### Unit 51: Animated Food
- Food pulses or sparkles
- Frame-based animation
- Eye-catching movement
- Encourages collection
- **Runnable:** Animated food item

### Unit 52: Colour Scheme Design
- Platform colour palette
- Snake colours
- Food colours
- Wall colours
- **Runnable:** Colour scheme applied

### Unit 53: Attribute Colour Effects
- ZX Spectrum colour attributes
- Colour per character cell
- Snake colour gradient
- Head distinct colour
- **Runnable:** Coloured snake

### Unit 54: Screen Flash on Eat
- Brief colour flash
- Positive feedback
- Flash colour change
- Quick restoration
- **Runnable:** Flash effect on food

### Unit 55: Death Animation
- Snake blinks or flashes
- Segment-by-segment fade
- Dramatic death effect
- Brief pause before restart
- **Runnable:** Animated death sequence

### Unit 56: Growth Animation
- Visual feedback on growth
- Brief stretch effect
- New segment highlight
- Growth satisfaction
- **Runnable:** Growth visual feedback

### Unit 57: Sound Effects Setup
- BEEPER sound initialisation
- Eat sound effect
- Move sound (optional subtle)
- Death sound
- **Runnable:** Basic sound effects

### Unit 58: Sound Variety
- Different eat sounds
- Pitch based on score
- Level complete fanfare
- Sound adds satisfaction
- **Runnable:** Varied sound effects

### Unit 59: Background Music Attempt
- Simple melody loop
- Interleaved with gameplay
- Performance consideration
- Optional music toggle
- **Runnable:** Basic background music

### Unit 60: Score Display Polish
- Large score numbers
- Score position prominent
- Length display
- Level indicator
- **Runnable:** Polished HUD display

### Unit 61: Level Introduction
- Brief level name display
- Maze preview
- "Get Ready" message
- Countdown to start
- **Runnable:** Level intro sequence

### Unit 62: Speed Indicator
- Visual speed display
- Progress bar or number
- Player awareness of speed
- Warning at high speeds
- **Runnable:** Speed indicator shown

### Unit 63: Border Animation
- Animated border pattern
- Subtle movement
- Colour cycling
- Arcade-style presentation
- **Runnable:** Animated border

### Unit 64: Phase 4 Integration
- All visual polish complete
- Sound effects working
- Professional presentation
- Polished snake game
- **Runnable:** Polished gameplay

---

## Phase 5: Advanced Features (Units 65-80)
*Advanced mechanics and game modes*

### Unit 65: Bonus Food Types
- Special food worth more points
- Rare appearance
- Time-limited availability
- Risk/reward element
- **Runnable:** Bonus food spawns

### Unit 66: Bonus Food Timer
- Countdown for bonus food
- Disappears after time
- Timer display
- Urgency mechanic
- **Runnable:** Timed bonus items

### Unit 67: Power-Up System Design
- Speed slow-down power-up
- Invincibility power-up
- Score multiplier
- Power-up data structure
- **Runnable:** Power-up system designed

### Unit 68: Speed Power-Up
- Temporary speed reduction
- Collect for breathing room
- Duration timer
- Visual indicator
- **Runnable:** Slow-down power-up

### Unit 69: Ghost Power-Up
- Pass through own body
- Temporary invincibility
- Ghost visual effect
- Strategic use
- **Runnable:** Ghost mode power-up

### Unit 70: Shrink Power-Up
- Reduce snake length
- Emergency escape option
- Minimum length enforced
- Risky trade-off
- **Runnable:** Shrink power-up

### Unit 71: Two-Player Mode Design
- Split screen or alternating
- Competitive or co-op
- Turn-based option
- Design considerations
- **Runnable:** Two-player design doc

### Unit 72: Alternating Two-Player
- Players take turns
- Compare scores
- Handoff between players
- Winner determination
- **Runnable:** Two-player alternating mode

### Unit 73: AI Snake Concept
- Computer-controlled snake
- Simple pathfinding
- Challenge mode
- Competitive AI
- **Runnable:** AI concept explained

### Unit 74: Basic AI Pathfinding
- Find path to food
- Avoid walls
- Avoid own body
- Simple decision making
- **Runnable:** Basic AI snake

### Unit 75: AI Difficulty Levels
- Easy AI makes mistakes
- Hard AI optimal paths
- Selectable difficulty
- Fair competition
- **Runnable:** AI difficulty settings

### Unit 76: Wrap-Around Mode
- Screen edges connect
- No border death
- Altered strategy
- Mode selection
- **Runnable:** Wrap-around gameplay

### Unit 77: Survival Mode
- No target length
- Endless play
- Score-only objective
- High score focus
- **Runnable:** Survival mode option

### Unit 78: Time Attack Mode
- Limited time
- Eat as much as possible
- Time extension pickups
- Frantic gameplay
- **Runnable:** Time attack mode

### Unit 79: Mode Selection Menu
- Game mode selection screen
- Clear mode descriptions
- Easy navigation
- Mode confirmation
- **Runnable:** Mode selection menu

### Unit 80: Phase 5 Integration
- All power-ups working
- Multiple game modes
- Two-player option
- Advanced feature set
- **Runnable:** Feature-rich snake game

---

## Phase 6: Content & Variety (Units 81-96)
*Levels, themes, and depth*

### Unit 81: Advanced Maze Designs
- Complex maze patterns
- Multiple paths
- Dead ends
- Strategic navigation
- **Runnable:** Advanced maze levels

### Unit 82: Moving Obstacles
- Obstacles that move
- Pattern-based movement
- Additional hazard
- Timing challenge
- **Runnable:** Moving obstacles in maze

### Unit 83: Teleport Portals
- Enter one, exit another
- Portal pairs
- Strategic shortcuts
- Disorientation factor
- **Runnable:** Teleport portals working

### Unit 84: Destructible Walls
- Some walls can be eaten
- Special food required
- Opens new paths
- Puzzle element
- **Runnable:** Breakable wall blocks

### Unit 85: Theme System
- Multiple visual themes
- Desert snake, water snake, space snake
- UDG sets per theme
- Colour schemes per theme
- **Runnable:** Theme system architecture

### Unit 86: Classic Theme
- Green snake
- Red food
- Blue walls
- Traditional appearance
- **Runnable:** Classic theme applied

### Unit 87: Cyber Theme
- Neon colours
- Digital snake
- Grid-style walls
- Futuristic feel
- **Runnable:** Cyber theme applied

### Unit 88: Nature Theme
- Brown/green palette
- Worm/caterpillar style
- Organic walls
- Natural appearance
- **Runnable:** Nature theme applied

### Unit 89: Theme Selection
- Choose theme before game
- Theme preview
- Saved preference
- Easy switching
- **Runnable:** Theme selection menu

### Unit 90: Achievement System
- Track accomplishments
- Length milestones
- Score milestones
- Level completion
- **Runnable:** Achievement tracking

### Unit 91: Achievement Display
- Show earned achievements
- Achievement notification
- Achievement gallery
- Progress towards next
- **Runnable:** Achievement display screen

### Unit 92: Statistics Tracking
- Total games played
- Total food eaten
- Total distance travelled
- Best performances
- **Runnable:** Statistics display

### Unit 93: Difficulty Modifiers
- Starting length option
- Speed modifier
- Lives modifier
- Custom difficulty
- **Runnable:** Difficulty customisation

### Unit 94: Daily Challenge Concept
- Seeded random level
- Same challenge for all
- Compare scores
- Date-based seed
- **Runnable:** Daily challenge mode

### Unit 95: Tutorial Mode
- Guided first game
- Explain controls
- Demonstrate growth
- Gentle introduction
- **Runnable:** Interactive tutorial

### Unit 96: Phase 6 Integration
- All content complete
- Themes working
- Achievements tracking
- Comprehensive game
- **Runnable:** Content-complete snake

---

## Phase 7: Optimisation & Effects (Units 97-112)
*Performance and special effects*

### Unit 97: Performance Analysis
- Measure game loop time
- Identify slow sections
- Frame timing check
- Establish baseline
- **Runnable:** Performance metrics

### Unit 98: Ring Buffer Optimisation
- Efficient index calculation
- Minimise memory access
- Lookup tables
- Faster buffer operations
- **Runnable:** Faster ring buffer

### Unit 99: Collision Optimisation
- Early exit on collision found
- Spatial shortcuts
- Optimised loop structure
- Faster collision checks
- **Runnable:** Optimised collision

### Unit 100: Rendering Optimisation
- Only update changed cells
- Dirty rectangle concept
- Minimise screen writes
- Faster display updates
- **Runnable:** Optimised rendering

### Unit 101: Special Effects - Trail
- Brief trail behind snake
- Fading ghost segments
- Visual speed indicator
- Optional effect
- **Runnable:** Trail effect

### Unit 102: Special Effects - Rainbow
- Colour-cycling snake body
- BRIGHT and colour rotation
- Celebratory effect
- Power-up indicator
- **Runnable:** Rainbow snake effect

### Unit 103: Screen Wipe Effects
- Level transition wipes
- Various wipe styles
- Smooth transitions
- Professional feel
- **Runnable:** Screen wipe transitions

### Unit 104: Particle Effects
- Food collection particles
- Death explosion particles
- Particle system basics
- Visual flair
- **Runnable:** Particle effects

### Unit 105: High Score Entry
- Name entry for high score
- Keyboard input
- Character limit
- Save with score
- **Runnable:** High score name entry

### Unit 106: High Score Table
- Top 10 scores
- Names and scores displayed
- Sorted list
- New entry highlight
- **Runnable:** High score table display

### Unit 107: Score Save/Load
- Persist scores to tape/disk
- Load on game start
- Handle missing file
- Verify data integrity
- **Runnable:** Persistent high scores

### Unit 108: Combo System
- Food eaten in succession
- Score multiplier
- Combo counter display
- Combo break
- **Runnable:** Combo scoring

### Unit 109: Chain Bonus
- Chain multiple food items
- Bonus for speed eating
- Visual chain indicator
- Risk/reward gameplay
- **Runnable:** Chain bonus system

### Unit 110: Perfect Level Bonus
- Bonus for no deaths in level
- Perfect play reward
- Encourages skill
- Significant bonus
- **Runnable:** Perfect level bonus

### Unit 111: Demo Mode
- Automated gameplay
- AI plays on title screen
- Attract mode loop
- Shows game features
- **Runnable:** Demo/attract mode

### Unit 112: Phase 7 Integration
- All optimisations applied
- Special effects working
- Scoring systems complete
- High performance build
- **Runnable:** Optimised, polished game

---

## Phase 8: Final Polish & Release (Units 113-128)
*Final quality and release*

### Unit 113: Bug Testing
- Systematic bug search
- Edge case testing
- Fix identified issues
- Stability verification
- **Runnable:** Bug-free gameplay

### Unit 114: Balance Testing
- Level difficulty progression
- Speed curve verification
- Fair challenge throughout
- Tuning adjustments
- **Runnable:** Balanced difficulty

### Unit 115: Control Responsiveness
- Input lag minimisation
- Consistent response
- Direction change timing
- Tight controls
- **Runnable:** Responsive controls

### Unit 116: Audio Balance
- Sound effect volume levels
- Music balance (if present)
- No harsh sounds
- Pleasant audio
- **Runnable:** Balanced audio

### Unit 117: Loading Screen
- Attractive loading visual
- Loading progress
- Game branding
- Professional presentation
- **Runnable:** Loading screen

### Unit 118: Credits Screen
- Developer credits
- Acknowledgements
- Music/sound credits
- Accessible from menu
- **Runnable:** Credits display

### Unit 119: Instructions Screen
- How to play
- Control reference
- Game mode explanations
- Tips for success
- **Runnable:** Help screen

### Unit 120: Accessibility Options
- Control remapping concept
- Speed options for beginners
- Colour-blind considerations
- Inclusive design
- **Runnable:** Accessibility features

### Unit 121: 48K/128K Compatibility
- Test on 48K Spectrum
- Test on 128K
- Handle memory differences
- Compatible build
- **Runnable:** Cross-model compatible

### Unit 122: Tape/Disk Testing
- Verify tape loading
- Verify disk loading
- Handle both formats
- Reliable loading
- **Runnable:** Format compatible

### Unit 123: Memory Cleanup
- Remove debug code
- Optimise memory usage
- Strip unused data
- Lean final build
- **Runnable:** Clean build

### Unit 124: Final Performance
- Verify smooth gameplay
- No slowdown
- Consistent frame rate
- Release quality
- **Runnable:** Stable performance

### Unit 125: Playtesting
- Extended play sessions
- Fresh player testing
- Gather feedback
- Note improvements
- **Runnable:** Playtested build

### Unit 126: Final Polish
- Implement playtest feedback
- Final visual tweaks
- Last balance adjustments
- Complete polish
- **Runnable:** Fully polished game

### Unit 127: Release Build
- Create final SNA/TAP file
- Verify clean load
- Document release
- Release candidate
- **Runnable:** Release-ready build

### Unit 128: Project Retrospective
- Document techniques learned
- Ring buffer mastery
- Grid-based game skills
- Foundation for future games
- **Runnable:** Complete Slither

---

## Technical Summary

### Key Data Structures
- Ring buffer for snake body
- Grid-based coordinate system
- Level configuration arrays
- High score table

### Code Patterns Introduced
```z80
; Ring buffer add (new head position)
add_to_buffer:
    ld a,(head_index)
    inc a
    cp MAX_LENGTH
    jr c,no_wrap
    xor a                   ; wrap to 0
no_wrap:
    ld (head_index),a
    ld e,a
    ld d,0
    ld hl,body_x_array
    add hl,de
    ld a,(snake_x)
    ld (hl),a
    ld hl,body_y_array
    add hl,de
    ld a,(snake_y)
    ld (hl),a
    ret

; Self-collision check
check_self_collision:
    ld a,(snake_length)
    ld b,a
    ld a,(tail_index)
    ld c,a                  ; c = current index
.loop:
    ; get body position at index c
    ; compare with head position
    ; return if collision found
    inc c                   ; next segment
    djnz .loop
    ret                     ; no collision
```

### Skills Progression
| Phase | Primary Skills |
|-------|---------------|
| 1 | Grid system, basic movement |
| 2 | Ring buffer, growth mechanics |
| 3 | Levels, speed progression |
| 4 | Visual polish, sound |
| 5 | Power-ups, game modes |
| 6 | Themes, content depth |
| 7 | Optimisation, effects |
| 8 | Polish, release |

---

## Version History
- v1.0 - Initial 128-unit outline
