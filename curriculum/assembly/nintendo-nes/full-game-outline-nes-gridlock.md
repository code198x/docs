# Game 7: Gridlock - Complete 128-Unit Outline

## Game Overview
**Platform:** Nintendo Entertainment System
**Genre:** Falling blocks puzzle (Tetris-style)
**Concept:** Tetromino pieces fall into a grid. Rotate and position them to clear lines. Game ends when the grid fills up - you're locked.

**Technical Focus:**
- Piece rotation mathematics (4 orientations)
- Grid collision detection
- Line clearing with row shifting
- Timer-based falling mechanics
- Next piece preview system
- Ghost piece projection

---

## Phase 1: Foundation (Units 1-16)
*Establish playfield and piece basics*

### Unit 1: Project Setup
- Create gridlock project structure
- Set up NES memory map
- Initialise PPU for puzzle game
- Clear screen to black
- **Runnable:** Clean game screen

### Unit 2: Playfield Design
- Standard 10x20 grid design
- Calculate screen position
- Border tile selection
- Playfield boundaries defined
- **Runnable:** Playfield concept shown

### Unit 3: Background Tile Setup
- Design border tiles
- Empty cell tile
- Nametable layout planning
- Attribute table considerations
- **Runnable:** Tile graphics loaded

### Unit 4: Draw Playfield Border
- Render playfield border
- Left and right walls
- Bottom floor
- Top opening (entry point)
- **Runnable:** Empty playfield displayed

### Unit 5: Grid Data Structure
- 10x20 byte array for grid
- Cell states (empty/filled/piece type)
- Row-major organisation
- Grid initialisation to empty
- **Runnable:** Grid memory allocated

### Unit 6: Piece Definition Concept
- Seven standard tetrominoes
- I, O, T, S, Z, J, L pieces
- Piece as 4 connected blocks
- Rotation states
- **Runnable:** Piece concepts explained

### Unit 7: Piece Data Format
- 4x4 grid per piece/rotation
- Bit patterns or coordinate lists
- Four rotations per piece
- Data table organisation
- **Runnable:** Piece data tables created

### Unit 8: I-Piece Definition
- Horizontal and vertical forms
- 4 rotation states
- Data encoding
- Verify data correctness
- **Runnable:** I-piece data defined

### Unit 9: O-Piece Definition
- Single rotation (or 4 identical)
- Square shape
- Simple encoding
- Verify data
- **Runnable:** O-piece data defined

### Unit 10: T, S, Z Piece Definitions
- Three more pieces
- Four rotations each
- Asymmetric rotations
- Data verification
- **Runnable:** T, S, Z data defined

### Unit 11: J, L Piece Definitions
- Final two pieces
- Mirror images of each other
- Four rotations each
- Complete piece set
- **Runnable:** All 7 pieces defined

### Unit 12: Piece Colour Assignment
- Each piece type has colour
- Attribute table mapping
- Limited colour per area
- Distinct visual identity
- **Runnable:** Piece colours assigned

### Unit 13: Draw Single Piece
- Render piece at position
- Read from piece data
- Draw to screen
- Test with one piece
- **Runnable:** Single piece displayed

### Unit 14: Current Piece State
- Current piece type variable
- Current rotation variable
- Current X, Y position
- Active piece tracking
- **Runnable:** Piece state variables

### Unit 15: Spawn New Piece
- Select piece type
- Set initial rotation (0)
- Set spawn position (top centre)
- Initialise piece state
- **Runnable:** Piece spawns at top

### Unit 16: Phase 1 Integration
- Playfield rendering
- All piece definitions
- Single piece display
- Spawn mechanism
- **Runnable:** Piece in playfield

---

## Phase 2: Core Mechanics (Units 17-32)
*Movement, rotation, and collision*

### Unit 17: Input Reading
- Controller input polling
- D-pad for movement
- Button A for rotate
- Input state tracking
- **Runnable:** Input detection working

### Unit 18: Horizontal Movement
- Left/right input detection
- Update piece X position
- Input repeat delay
- Smooth movement feel
- **Runnable:** Piece moves left/right

### Unit 19: Boundary Collision - Walls
- Check piece vs left wall
- Check piece vs right wall
- Block invalid movement
- Piece stays in bounds
- **Runnable:** Wall collision working

### Unit 20: Rotation Input
- A button rotates clockwise
- B button rotates counter-clockwise
- Increment/decrement rotation
- Wrap rotation (0-3)
- **Runnable:** Rotation input detected

### Unit 21: Rotation Collision
- Check if rotated piece fits
- Test against walls
- Test against floor
- Block invalid rotation
- **Runnable:** Rotation collision working

### Unit 22: Wall Kick Concept
- Rotation blocked by wall
- Try shifting piece away from wall
- Enable more rotations
- Basic wall kick
- **Runnable:** Basic wall kicks

### Unit 23: Gravity Timer
- Frame counter for falling
- Adjustable fall speed
- Reset timer after move
- Gravity interval variable
- **Runnable:** Timer counts frames

### Unit 24: Automatic Falling
- Move piece down on timer
- Reset timer after fall
- Continuous downward movement
- Visible falling
- **Runnable:** Piece falls automatically

### Unit 25: Floor Collision
- Detect piece at bottom
- Check against grid floor
- Stop at floor level
- Prevent falling through
- **Runnable:** Piece stops at floor

### Unit 26: Lock Piece to Grid
- Copy piece to grid array
- Mark cells as filled
- Record piece type for colour
- Piece becomes permanent
- **Runnable:** Piece locks into grid

### Unit 27: Grid Rendering
- Draw grid contents
- Empty vs filled cells
- Colour based on piece type
- Update after lock
- **Runnable:** Locked pieces visible

### Unit 28: Stack Collision
- Check piece vs existing blocks
- Compare with grid contents
- Block downward into stack
- Lock when resting on stack
- **Runnable:** Pieces stack on each other

### Unit 29: Soft Drop
- Down input speeds falling
- Faster drop while held
- Extra points for soft drop
- Release returns to normal
- **Runnable:** Soft drop working

### Unit 30: Hard Drop
- Instant drop to bottom
- Up or dedicated button
- Immediate lock
- Maximum points
- **Runnable:** Hard drop feature

### Unit 31: Lock Delay
- Brief pause before locking
- Can still move during delay
- Delay resets on movement
- Strategic sliding
- **Runnable:** Lock delay mechanic

### Unit 32: Phase 2 Integration
- Full movement and rotation
- Collision detection complete
- Gravity and locking working
- Core tetris mechanics
- **Runnable:** Playable piece placement

---

## Phase 3: Game Systems (Units 33-48)
*Line clearing and scoring*

### Unit 33: Line Detection
- Scan each row for full line
- All 10 cells filled
- Mark line for clearing
- Count lines to clear
- **Runnable:** Full lines detected

### Unit 34: Line Clear Animation
- Flash filled lines
- Colour change animation
- Brief pause for effect
- Dramatic feedback
- **Runnable:** Line clear animation

### Unit 35: Remove Cleared Lines
- Delete line data
- Shift rows above down
- Fill top with empty
- Grid compaction
- **Runnable:** Lines removed, rows fall

### Unit 36: Multiple Line Clears
- Handle 1, 2, 3, or 4 lines
- Simultaneous clearing
- Special Tetris clear (4 lines)
- Clear count tracking
- **Runnable:** Multi-line clears

### Unit 37: Score System Design
- Points per line clear
- Multiplier for multiple lines
- Tetris bonus (4 lines)
- Score accumulation
- **Runnable:** Score design documented

### Unit 38: Score Implementation
- Score variable (multi-byte)
- Add points on clear
- Different points per clear count
- Score updates
- **Runnable:** Score tracks clears

### Unit 39: Score Display
- Score position on screen
- Binary to decimal conversion
- Right-aligned display
- Leading zeros
- **Runnable:** Score displayed

### Unit 40: Level System
- Level increases with lines
- Lines per level threshold
- Level counter
- Level display
- **Runnable:** Level tracking

### Unit 41: Speed Progression
- Gravity increases with level
- Level to speed mapping
- Gradual difficulty increase
- Maximum speed cap
- **Runnable:** Speed increases per level

### Unit 42: Next Piece Preview
- Show upcoming piece
- Preview box display
- Update on spawn
- Strategic planning aid
- **Runnable:** Next piece shown

### Unit 43: Next Piece Queue
- Generate pieces ahead
- Random selection
- Bag randomiser concept
- Fair distribution
- **Runnable:** Piece queue system

### Unit 44: Game Over Detection
- New piece can't spawn
- Stack reaches top
- Game over state
- Stop gameplay
- **Runnable:** Game over detected

### Unit 45: Game Over Screen
- Display game over message
- Show final score
- Show level reached
- Option to restart
- **Runnable:** Game over screen

### Unit 46: Title Screen
- Game title display
- Press start prompt
- High score display
- Basic title
- **Runnable:** Title screen

### Unit 47: Game State Machine
- Title, playing, game over states
- State transitions
- Clean state management
- Proper flow
- **Runnable:** State machine working

### Unit 48: Phase 3 Integration
- Line clearing complete
- Scoring working
- Levels and speed progression
- Full game loop
- **Runnable:** Complete puzzle game

---

## Phase 4: Polish & Feel (Units 49-64)
*Visual and audio refinement*

### Unit 49: Piece Colour Refinement
- Distinct colours per piece
- Palette optimisation
- Visibility on playfield
- Pleasant colour scheme
- **Runnable:** Refined piece colours

### Unit 50: Block Detail
- Multi-tile blocks
- Shading and highlights
- 3D effect on pieces
- Visual depth
- **Runnable:** Detailed block graphics

### Unit 51: Ghost Piece Concept
- Preview where piece lands
- Transparent or dotted outline
- Aids placement accuracy
- Optional feature
- **Runnable:** Ghost piece concept

### Unit 52: Ghost Piece Rendering
- Calculate drop position
- Draw ghost at target
- Distinct from active piece
- Update with movement
- **Runnable:** Ghost piece displayed

### Unit 53: Lock Animation
- Flash when piece locks
- Colour pulse effect
- Impact feedback
- Brief animation
- **Runnable:** Lock animation

### Unit 54: Clear Animation Improvement
- Row-by-row clear
- Fancy clear effect
- Tetris clear special animation
- Dramatic 4-line clear
- **Runnable:** Improved clear animations

### Unit 55: Level Background
- Background changes per level
- Different visuals
- Palette shifts
- Variety over time
- **Runnable:** Level-based backgrounds

### Unit 56: Sound Effects Setup
- APU initialisation
- Square channel for effects
- Sound effect system
- Trigger mechanism
- **Runnable:** Sound system ready

### Unit 57: Movement Sounds
- Move left/right sound
- Rotation sound
- Distinct sounds
- Subtle feedback
- **Runnable:** Movement sounds

### Unit 58: Drop and Lock Sounds
- Soft drop sound
- Hard drop impact
- Lock confirmation sound
- Satisfying feedback
- **Runnable:** Drop/lock sounds

### Unit 59: Line Clear Sounds
- Single line clear sound
- Multi-line clear sounds
- Tetris fanfare
- Escalating feedback
- **Runnable:** Clear sounds

### Unit 60: Background Music
- Puzzle game music
- Looping track
- Tempo matching gameplay
- Triangle/square channels
- **Runnable:** Background music plays

### Unit 61: Music Speed Variation
- Faster music at higher levels
- Tension building
- Speed-based tempo
- Dynamic music
- **Runnable:** Music tempo changes

### Unit 62: HUD Polish
- Clean HUD layout
- Score, level, lines display
- Next piece box styled
- Professional appearance
- **Runnable:** Polished HUD

### Unit 63: Screen Border
- Decorative border
- Consistent visual frame
- NES-appropriate styling
- Complete look
- **Runnable:** Bordered display

### Unit 64: Phase 4 Integration
- All visual polish complete
- Sound effects working
- Music playing
- Polished presentation
- **Runnable:** Polished puzzle game

---

## Phase 5: Advanced Features (Units 65-80)
*Advanced mechanics and modes*

### Unit 65: T-Spin Detection
- Detect T-piece spin into place
- T-spin clear bonus
- T-spin conditions
- Advanced technique
- **Runnable:** T-spin detected

### Unit 66: T-Spin Scoring
- Bonus points for T-spin
- T-spin single/double/triple
- Skill reward
- Score boost
- **Runnable:** T-spin scoring

### Unit 67: Back-to-Back Bonus
- Consecutive difficult clears
- Tetris after Tetris bonus
- T-spin chains
- Combo tracking
- **Runnable:** Back-to-back bonus

### Unit 68: Hold Piece Feature
- Store current piece
- Swap with held piece
- Once per piece limit
- Strategic depth
- **Runnable:** Hold piece working

### Unit 69: Hold Display
- Show held piece
- Hold box on screen
- Swap animation
- Clear visual
- **Runnable:** Hold display

### Unit 70: Extended Preview
- Show next 3-5 pieces
- Queue visibility
- Better planning
- Advanced preview
- **Runnable:** Extended queue preview

### Unit 71: 7-Bag Randomiser
- Each piece once per bag
- Guaranteed distribution
- Fair randomness
- Standard Tetris rules
- **Runnable:** Bag randomiser

### Unit 72: Marathon Mode
- Standard endless mode
- Level 15 maximum
- High score focus
- Classic gameplay
- **Runnable:** Marathon mode

### Unit 73: Sprint Mode
- Clear 40 lines fastest
- Timer display
- Time-based scoring
- Speed challenge
- **Runnable:** Sprint mode

### Unit 74: Ultra Mode
- 3-minute time limit
- Score attack
- Maximum points goal
- Intense gameplay
- **Runnable:** Ultra mode

### Unit 75: Mode Selection Menu
- Choose game mode
- Mode descriptions
- Easy navigation
- Mode confirmation
- **Runnable:** Mode selection

### Unit 76: Difficulty Settings
- Starting level selection
- Choose level 0-15
- Higher start = more points
- Skill selection
- **Runnable:** Starting level choice

### Unit 77: Two-Player Concept
- Competitive puzzle
- Split screen layout
- Garbage line sending
- Attack mechanics
- **Runnable:** Two-player design

### Unit 78: Two-Player Implementation
- Two playfields
- Independent controls
- Garbage on enemy clears
- Win condition
- **Runnable:** Two-player versus

### Unit 79: Garbage Line System
- Lines sent on clears
- Garbage rises from bottom
- Hole position random
- Attack strategy
- **Runnable:** Garbage mechanics

### Unit 80: Phase 5 Integration
- All advanced mechanics
- Multiple game modes
- Two-player option
- Feature-complete
- **Runnable:** Advanced puzzle game

---

## Phase 6: Content & Variety (Units 81-96)
*Themes, challenges, and depth*

### Unit 81: Visual Theme System
- Multiple graphical themes
- Block style variants
- Background variants
- Theme data structure
- **Runnable:** Theme system

### Unit 82: Classic Theme
- Traditional block style
- Solid colours
- Original aesthetic
- Clean appearance
- **Runnable:** Classic theme

### Unit 83: Modern Theme
- Gradient blocks
- Shaded 3D effect
- Contemporary style
- Visual upgrade
- **Runnable:** Modern theme

### Unit 84: Retro Theme
- Minimal graphics
- Outline blocks
- Nostalgic style
- Simple aesthetic
- **Runnable:** Retro theme

### Unit 85: Theme Selection
- Choose theme in menu
- Preview themes
- Save preference
- Easy access
- **Runnable:** Theme selection menu

### Unit 86: Challenge Mode Concept
- Preset challenges
- Specific goals
- Unlock progression
- Achievement system
- **Runnable:** Challenge concept

### Unit 87: Clear Challenges
- Clear X lines challenge
- Time limit variations
- Score target challenges
- Variety of goals
- **Runnable:** Clear challenges

### Unit 88: Survival Challenges
- Survive at high speed
- Pre-filled grid start
- Excavation challenges
- Difficult starts
- **Runnable:** Survival challenges

### Unit 89: Challenge Selection
- List of challenges
- Completion tracking
- Star ratings
- Challenge menu
- **Runnable:** Challenge menu

### Unit 90: Statistics Tracking
- Total lines cleared
- Total Tetrises
- Total T-spins
- Playtime tracking
- **Runnable:** Statistics screen

### Unit 91: High Score Table
- Top 10 scores per mode
- Name entry
- Score, level, lines
- Persistent storage concept
- **Runnable:** High score table

### Unit 92: Replay System Concept
- Record input sequence
- Replay playback
- Share replays concept
- Demo recording
- **Runnable:** Replay concept

### Unit 93: Demo Mode
- Automated gameplay
- AI or recorded demo
- Title screen attract
- Shows game features
- **Runnable:** Demo/attract mode

### Unit 94: Handicap System
- Skilled player handicap
- Start with garbage
- Level difference option
- Fair competition
- **Runnable:** Handicap options

### Unit 95: Practice Mode
- No game over
- Piece selection
- Situation practice
- Learning tool
- **Runnable:** Practice mode

### Unit 96: Phase 6 Integration
- All themes available
- Challenge mode complete
- Statistics tracking
- Full content
- **Runnable:** Content-complete game

---

## Phase 7: Optimisation & Effects (Units 97-112)
*Performance and special effects*

### Unit 97: Performance Analysis
- Measure frame timing
- Identify bottlenecks
- Collision check speed
- Rendering efficiency
- **Runnable:** Performance metrics

### Unit 98: Collision Optimisation
- Efficient piece checking
- Early exit conditions
- Lookup table usage
- Faster collision
- **Runnable:** Optimised collision

### Unit 99: Rendering Optimisation
- Update only changed tiles
- Dirty flag system
- Minimise VRAM writes
- Faster display
- **Runnable:** Optimised rendering

### Unit 100: Line Clear Optimisation
- Efficient row shifting
- Memory move optimisation
- Fast grid update
- Smooth clear animation
- **Runnable:** Fast line clear

### Unit 101: Screen Shake Effect
- Brief shake on Tetris
- Screen offset method
- Impact feedback
- Dramatic effect
- **Runnable:** Tetris screen shake

### Unit 102: Flash Effects
- Screen flash on events
- Palette manipulation
- Quick colour change
- Emphasis effect
- **Runnable:** Flash effects

### Unit 103: Particle Effects
- Sparkles on line clear
- Block debris
- Sprite-based particles
- Visual flair
- **Runnable:** Particle effects

### Unit 104: Level Transition Effect
- Special effect on level up
- Brief celebration
- Visual fanfare
- Achievement feel
- **Runnable:** Level-up effect

### Unit 105: Combo Display
- Show combo count
- Animated numbers
- Rising score popups
- Achievement feedback
- **Runnable:** Combo visuals

### Unit 106: Perfect Clear Detection
- Detect fully empty grid
- Massive bonus
- Special celebration
- Rare achievement
- **Runnable:** Perfect clear bonus

### Unit 107: Perfect Clear Animation
- Dramatic all-clear effect
- Full screen celebration
- Memorable moment
- Special feedback
- **Runnable:** Perfect clear animation

### Unit 108: Achievement Popups
- On-screen achievement notification
- Brief display
- Unobtrusive placement
- Positive feedback
- **Runnable:** Achievement popups

### Unit 109: Countdown Timer
- 3-2-1 game start
- Countdown display
- Ready player prompt
- Smooth game start
- **Runnable:** Start countdown

### Unit 110: Results Screen
- Post-game statistics
- Lines, level, score
- Performance summary
- Detailed breakdown
- **Runnable:** Results display

### Unit 111: Grade System
- Performance grading (S, A, B, C, D)
- Based on play quality
- Skill rating
- Achievement goal
- **Runnable:** Grade system

### Unit 112: Phase 7 Integration
- All optimisations complete
- Effects working
- Grade system
- High-performance build
- **Runnable:** Polished, fast game

---

## Phase 8: Final Polish & Release (Units 113-128)
*Final quality and release*

### Unit 113: Bug Sweep
- Systematic testing
- Edge case verification
- Fix issues found
- Stability confirmation
- **Runnable:** Bug-free game

### Unit 114: Balance Testing
- Level speed curve
- Score balance
- Challenge difficulty
- Fair progression
- **Runnable:** Balanced game

### Unit 115: Control Refinement
- DAS (Delayed Auto Shift) tuning
- Responsive movement
- Comfortable handling
- Professional feel
- **Runnable:** Refined controls

### Unit 116: Audio Balance
- Sound effect levels
- Music volume
- No clipping
- Pleasant mix
- **Runnable:** Balanced audio

### Unit 117: Loading Screen
- Logo display
- Loading message
- Professional presentation
- Quick load
- **Runnable:** Loading screen

### Unit 118: Credits Screen
- Developer credits
- Thank you notes
- Music credits
- Accessible credits
- **Runnable:** Credits screen

### Unit 119: Instructions
- How to play
- Control reference
- Scoring explanation
- Help screen
- **Runnable:** Instructions screen

### Unit 120: Options Menu
- Music on/off
- Sound effects on/off
- Ghost piece toggle
- Preference saving concept
- **Runnable:** Options menu

### Unit 121: NTSC/PAL Compatibility
- Test both systems
- Speed adjustments
- Visual verification
- Compatible build
- **Runnable:** Region compatible

### Unit 122: Mapper Verification
- Test on target mapper
- Verify ROM size
- CHR/PRG verification
- Hardware compatible
- **Runnable:** Mapper verified

### Unit 123: Memory Cleanup
- Remove debug code
- Optimise ROM usage
- Strip unused data
- Lean build
- **Runnable:** Clean build

### Unit 124: Final Performance
- Stable frame rate
- No slowdown
- Consistent timing
- Release quality
- **Runnable:** Stable performance

### Unit 125: Playtesting
- Extended sessions
- Various skill levels
- Feedback gathering
- Final notes
- **Runnable:** Playtested build

### Unit 126: Final Polish
- Address feedback
- Final tweaks
- Last improvements
- Complete polish
- **Runnable:** Fully polished

### Unit 127: Release Build
- Create final ROM
- Verify clean boot
- Final testing
- Release candidate
- **Runnable:** Release-ready ROM

### Unit 128: Project Retrospective
- Document techniques
- Rotation system mastery
- Puzzle game skills
- Foundation for future games
- **Runnable:** Complete Gridlock

---

## Technical Summary

### Key Algorithms
- Piece rotation with wall kicks
- Line clearing and gravity
- Random piece generation (7-bag)
- Ghost piece projection

### Code Patterns Introduced
```asm
; Piece rotation check
try_rotate:
    lda rotation
    clc
    adc #1
    and #$03              ; wrap 0-3
    sta temp_rotation
    jsr check_piece_fits
    bcs @blocked
    lda temp_rotation
    sta rotation
    rts
@blocked:
    jsr try_wall_kick     ; try offset
    rts

; Line clear detection
check_lines:
    ldx #19               ; bottom row
@row_loop:
    ldy #0
    lda #0
@cell_loop:
    ora grid,x           ; check cell
    ; ... check all 10 cells
    cmp #FULL_ROW
    bne @not_full
    jsr mark_line_clear
@not_full:
    dex
    bpl @row_loop
    rts
```

### Skills Progression
| Phase | Primary Skills |
|-------|---------------|
| 1 | Grid system, piece data |
| 2 | Movement, rotation, collision |
| 3 | Line clearing, scoring |
| 4 | Visual polish, audio |
| 5 | Advanced mechanics, modes |
| 6 | Themes, challenges |
| 7 | Optimisation, effects |
| 8 | Polish, release |

---

## Version History
- v1.0 - Initial 128-unit outline
