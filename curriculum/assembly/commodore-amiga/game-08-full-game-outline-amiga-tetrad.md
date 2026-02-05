# Game 8: Tetrad - Complete 128-Unit Outline

## Game Overview
**Platform:** Commodore Amiga
**Genre:** Falling blocks puzzle (Tetris-style)
**Concept:** Classic falling block puzzle polished to Amiga quality. Uses the Blitter for efficient grid rendering and the Copper for visual effects. Piece rotation, line clearing, and competitive two-player modes.

**Technical Focus:**
- Piece rotation mathematics
- Grid collision detection
- Line clearing with Blitter scroll
- Efficient grid rendering
- Next piece and ghost piece display
- Two-player competitive mode
- Copper colour effects

---

## Phase 1: Foundation (Units 1-16)
*Establish playfield and rendering*

### Unit 1: Project Setup
- Create tetrad project structure
- Amiga memory layout
- Custom chip setup
- System takeover
- **Runnable:** Clean startup

### Unit 2: Display Configuration
- Bitplane setup for playfield
- Colour depth (8+ colours)
- Screen dimensions
- Copper list basic
- **Runnable:** Display ready

### Unit 3: Colour Palette
- Seven piece colours
- Background colour
- Grid line colour
- Border colours
- **Runnable:** Palette set

### Unit 4: Playfield Layout
- 10x20 grid standard
- Grid to screen mapping
- Cell size in pixels
- Centred playfield
- **Runnable:** Layout planned

### Unit 5: Draw Playfield Border
- Blitter rectangle
- Framed play area
- Clean borders
- Professional look
- **Runnable:** Border drawn

### Unit 6: Grid Structure
- 10x20 data array
- Cell states (empty/piece type)
- Efficient storage
- Access routines
- **Runnable:** Grid allocated

### Unit 7: Block Graphics
- Single block design
- Colour per piece type
- Highlight/shadow
- 3D effect
- **Runnable:** Block graphics

### Unit 8: Draw Single Block
- Blitter block copy
- Position on grid
- Colour application
- Building unit
- **Runnable:** Block renders

### Unit 9: Piece Definitions
- Seven tetriminos
- I, O, T, S, Z, J, L
- 4x4 bounding box
- Piece data format
- **Runnable:** Pieces defined

### Unit 10: Rotation Data
- Four orientations each
- All 28 states stored
- Efficient lookup
- Complete rotations
- **Runnable:** Rotations defined

### Unit 11: Draw Piece
- Render piece from data
- Multiple blocks
- Correct colour
- Complete piece
- **Runnable:** Piece displayed

### Unit 12: Spawn Position
- Top-centre spawn
- Entry coordinates
- Piece appears
- Starting point
- **Runnable:** Piece spawns

### Unit 13: Current Piece State
- Position X, Y
- Rotation state
- Piece type
- Active tracking
- **Runnable:** State managed

### Unit 14: Joystick Input
- Read joystick
- Direction mapping
- Fire for rotate
- Responsive input
- **Runnable:** Input working

### Unit 15: Move Left/Right
- Horizontal movement
- Grid-aligned steps
- Boundary aware
- Smooth control
- **Runnable:** Piece moves

### Unit 16: Phase 1 Integration
- Playfield displayed
- Piece spawns and moves
- Blitter rendering
- Foundation complete
- **Runnable:** Basic control

---

## Phase 2: Core Mechanics (Units 17-32)
*Rotation, falling, and locking*

### Unit 17: Rotation Input
- Fire button rotate
- Clockwise rotation
- Input detection
- Rotation trigger
- **Runnable:** Rotation input

### Unit 18: Rotation Logic
- Cycle rotation state
- Update piece display
- Clear and redraw
- State change
- **Runnable:** Piece rotates

### Unit 19: Collision Concept
- Check before move/rotate
- Grid overlap detection
- Boundary checking
- Prevent illegal moves
- **Runnable:** Concept defined

### Unit 20: Grid Collision
- Piece vs placed blocks
- Check all cells
- Collision flag
- Accurate detection
- **Runnable:** Grid collision

### Unit 21: Boundary Collision
- Wall detection
- Floor detection
- Combined checks
- Boundary enforcement
- **Runnable:** Boundaries work

### Unit 22: Move with Collision
- Check then move
- Reject invalid moves
- Safe movement
- Proper physics
- **Runnable:** Safe movement

### Unit 23: Rotate with Collision
- Check rotation validity
- Reject if blocked
- Safe rotation
- Proper handling
- **Runnable:** Safe rotation

### Unit 24: Fall Timer
- VBlank counter
- Fall interval
- Timer-based descent
- Consistent speed
- **Runnable:** Timer running

### Unit 25: Automatic Falling
- Drop one row on timer
- Continuous descent
- Game flow
- Piece falls
- **Runnable:** Auto-fall

### Unit 26: Soft Drop
- Down accelerates fall
- Faster descent
- Player control
- Score bonus
- **Runnable:** Soft drop

### Unit 27: Hard Drop
- Instant drop
- Find bottom
- Quick placement
- Advanced control
- **Runnable:** Hard drop

### Unit 28: Lock Detection
- Cannot move down
- Lock delay
- Landing detection
- Prepare to place
- **Runnable:** Landing detected

### Unit 29: Lock Piece
- Transfer to grid
- Mark cells filled
- Store piece type
- Permanent placement
- **Runnable:** Piece locks

### Unit 30: Line Detection
- Scan all rows
- Find complete lines
- Mark for clearing
- Line counting
- **Runnable:** Lines detected

### Unit 31: Line Clear with Blitter
- Remove complete lines
- Blitter scroll down
- Efficient clearing
- Visual clear
- **Runnable:** Lines clear

### Unit 32: Phase 2 Integration
- Full piece control
- Rotation and falling
- Collision and locking
- Line clearing
- **Runnable:** Core gameplay

---

## Phase 3: Game Systems (Units 33-48)
*Scoring, speed, and game flow*

### Unit 33: Score System
- Points per line
- Single/Double/Triple/Tetris
- Score variable
- Point calculation
- **Runnable:** Scoring

### Unit 34: Score Display
- Score on screen
- Large numbers
- Blitter text
- Live update
- **Runnable:** Score displayed

### Unit 35: Line Counter
- Total lines cleared
- Lines display
- Progress tracking
- Statistics
- **Runnable:** Lines counted

### Unit 36: Level System
- Level by lines (10 per level)
- Level display
- Progression
- Difficulty marker
- **Runnable:** Levels

### Unit 37: Speed Increase
- Faster per level
- Speed curve
- Maximum cap
- Challenge progression
- **Runnable:** Speed scaling

### Unit 38: Next Piece Preview
- Preview area
- Show upcoming
- Strategic planning
- Preview display
- **Runnable:** Next piece shown

### Unit 39: Piece Randomiser
- 7-bag system
- Fair distribution
- No long droughts
- Balanced random
- **Runnable:** Fair random

### Unit 40: Ghost Piece
- Show landing position
- Transparent rendering
- Placement preview
- Helpful guide
- **Runnable:** Ghost piece

### Unit 41: Game Over Detection
- Spawn blocked
- Stack too high
- Game end trigger
- Detect game over
- **Runnable:** Game over detected

### Unit 42: Game Over Screen
- Final score
- High score check
- Restart option
- Clear ending
- **Runnable:** Game over screen

### Unit 43: Title Screen
- Tetrad title
- Start prompt
- High score
- Attractive title
- **Runnable:** Title screen

### Unit 44: Copper Title Effects
- Colour cycling
- Gradient title
- Visual appeal
- Amiga showcase
- **Runnable:** Copper title

### Unit 45: Pause Function
- Pause key
- Freeze gameplay
- Hidden grid (prevent cheating)
- Resume function
- **Runnable:** Pause works

### Unit 46: Hold Piece
- Store current piece
- Swap with held
- Once per piece
- Strategic option
- **Runnable:** Hold piece

### Unit 47: Hold Display
- Hold area display
- Show held piece
- Clear indication
- UI element
- **Runnable:** Hold displayed

### Unit 48: Phase 3 Integration
- Complete scoring
- Speed progression
- Preview and hold
- Full game flow
- **Runnable:** Full puzzle game

---

## Phase 4: Polish & Feel (Units 49-64)
*Visual and audio refinement*

### Unit 49: Wall Kick System
- Rotation adjustment
- Offset attempts
- SRS-style kicks
- Better rotation
- **Runnable:** Wall kicks

### Unit 50: Wall Kick Data
- Offset tables
- Per-piece data
- Standard tests
- Robust rotation
- **Runnable:** Full kicks

### Unit 51: T-Spin Detection
- Detect T-spins
- Corner checks
- Special moves
- Advanced technique
- **Runnable:** T-spins detected

### Unit 52: T-Spin Scoring
- Bonus points
- T-spin variants
- Skill reward
- Special display
- **Runnable:** T-spin scoring

### Unit 53: Combo System
- Consecutive clears
- Combo counter
- Bonus multiplier
- Combo display
- **Runnable:** Combos

### Unit 54: Back-to-Back
- Consecutive special clears
- B2B bonus
- Skill chain
- B2B indicator
- **Runnable:** Back-to-back

### Unit 55: Clear Animation
- Line flash effect
- Blitter fill
- Removal animation
- Satisfying clear
- **Runnable:** Clear animation

### Unit 56: Lock Animation
- Placement flash
- Brief highlight
- Confirmation feedback
- Visual polish
- **Runnable:** Lock animation

### Unit 57: Paula Audio Setup
- Sample playback
- Sound effect system
- Audio channels
- Effect triggers
- **Runnable:** Audio ready

### Unit 58: Movement Sounds
- Move sound
- Rotate sound
- Distinct effects
- Tactile feedback
- **Runnable:** Move sounds

### Unit 59: Line Clear Sound
- Satisfying clear audio
- Tetris special sound
- Multi-line sounds
- Reward feedback
- **Runnable:** Clear sounds

### Unit 60: Drop Sounds
- Soft drop sound
- Hard drop sound
- Lock sound
- Complete audio
- **Runnable:** Drop sounds

### Unit 61: Module Music
- Background music track
- Puzzle tempo
- Looping music
- Atmosphere
- **Runnable:** Music playing

### Unit 62: HUD Polish
- Clean score area
- Level/lines display
- Professional layout
- Readable HUD
- **Runnable:** Polished HUD

### Unit 63: Copper Background
- Gradient background
- Colour cycling
- Visual depth
- Amiga beauty
- **Runnable:** Copper background

### Unit 64: Phase 4 Integration
- Wall kicks complete
- T-spins working
- Full audio
- Visual polish
- **Runnable:** Polished Tetrad

---

## Phase 5: Advanced Features (Units 65-80)
*Game modes and multiplayer*

### Unit 65: Marathon Mode
- Endless play
- Speed caps at 20
- High score focus
- Classic mode
- **Runnable:** Marathon

### Unit 66: Sprint Mode
- Clear 40 lines
- Best time wins
- Timer display
- Speed challenge
- **Runnable:** Sprint

### Unit 67: Ultra Mode
- 3-minute limit
- Maximum score
- Time pressure
- Score attack
- **Runnable:** Ultra

### Unit 68: Mode Menu
- Mode selection
- Clear descriptions
- Easy selection
- Mode variety
- **Runnable:** Mode menu

### Unit 69: Two-Player Concept
- Split screen
- Competitive play
- Garbage attack
- Head-to-head
- **Runnable:** Two-player design

### Unit 70: Split Screen Setup
- Two playfields
- Screen division
- Both players visible
- Efficient rendering
- **Runnable:** Split display

### Unit 71: Two-Player Controls
- Two joysticks
- Independent control
- No conflicts
- Simultaneous play
- **Runnable:** Dual controls

### Unit 72: Garbage System
- Lines sent to opponent
- Incomplete rows
- Attack mechanic
- Competitive element
- **Runnable:** Garbage lines

### Unit 73: Garbage Indicator
- Incoming warning
- Queue display
- Strategic info
- Clear communication
- **Runnable:** Garbage warning

### Unit 74: Victory Condition
- First to top out loses
- Winner celebration
- Match end
- Victory screen
- **Runnable:** Win detection

### Unit 75: Match System
- Best of rounds
- Match scoring
- Series play
- Extended competition
- **Runnable:** Match system

### Unit 76: AI Opponent
- Computer player
- Piece placement AI
- Decision logic
- Single-player versus
- **Runnable:** AI plays

### Unit 77: AI Difficulty
- Easy/Medium/Hard
- Decision quality
- Speed variation
- Fair challenge
- **Runnable:** AI levels

### Unit 78: Custom Game
- Starting level
- Starting lines
- Garbage toggle
- Options
- **Runnable:** Custom settings

### Unit 79: 20G Mode
- Instant drop
- Extreme challenge
- Expert only
- Brutal mode
- **Runnable:** 20G mode

### Unit 80: Phase 5 Integration
- All modes working
- Two-player complete
- AI opponent
- Feature-complete
- **Runnable:** Full modes

---

## Phase 6: Content & Variety (Units 81-96)
*Themes and extras*

### Unit 81: Speed Level 1-5
- Gentle start
- Learning curve
- Beginner friendly
- Comfortable
- **Runnable:** Easy speeds

### Unit 82: Speed Level 6-10
- Moderate pace
- Skill building
- Intermediate
- Good progression
- **Runnable:** Medium speeds

### Unit 83: Speed Level 11-15
- Fast gameplay
- Requiring skill
- Advanced play
- Challenging
- **Runnable:** Fast speeds

### Unit 84: Speed Level 16-20
- Maximum speed
- Expert only
- End-game
- Brutal
- **Runnable:** Max speeds

### Unit 85: Theme System
- Visual themes
- Colour schemes
- Block styles
- Customisation
- **Runnable:** Theme framework

### Unit 86: Classic Theme
- Traditional colours
- Clean blocks
- Standard look
- Default theme
- **Runnable:** Classic theme

### Unit 87: Neon Theme
- Bright colours
- Glow effect
- Futuristic
- Eye-catching
- **Runnable:** Neon theme

### Unit 88: Marble Theme
- Stone colours
- Textured blocks
- Elegant look
- Sophisticated
- **Runnable:** Marble theme

### Unit 89: Theme Selection
- Theme menu
- Preview
- Easy selection
- Save preference
- **Runnable:** Theme menu

### Unit 90: Achievement System
- Track accomplishments
- First Tetris
- Score milestones
- Skill achievements
- **Runnable:** Achievements

### Unit 91: Achievement Display
- Achievement list
- Unlock status
- Progress view
- Collection screen
- **Runnable:** Achievement screen

### Unit 92: Statistics
- Games played
- Lines cleared
- Tetrises
- Best scores
- **Runnable:** Statistics

### Unit 93: Tutorial Mode
- Guided intro
- Basic controls
- Rotation demo
- Welcoming
- **Runnable:** Tutorial

### Unit 94: Advanced Tutorial
- T-spin teaching
- Combo building
- Advanced skills
- Skill development
- **Runnable:** Advanced tutorial

### Unit 95: 128K Sound
- Enhanced music
- Multiple tracks
- Module variety
- Audio options
- **Runnable:** Enhanced audio

### Unit 96: Phase 6 Integration
- All content complete
- Themes working
- Achievements
- Full options
- **Runnable:** Content complete

---

## Phase 7: Optimisation & Effects (Units 97-112)
*Performance and effects*

### Unit 97: Performance Analysis
- Measure timing
- Identify bottlenecks
- Blitter efficiency
- Optimisation targets
- **Runnable:** Performance data

### Unit 98: Grid Rendering Optimised
- Minimal redraws
- Changed cells only
- Efficient updates
- Fast rendering
- **Runnable:** Fast grid

### Unit 99: Line Clear Optimised
- Blitter scroll
- Efficient memory copy
- Smooth clearing
- Quick operation
- **Runnable:** Fast clear

### Unit 100: Collision Optimised
- Fast checks
- Early exit
- Efficient detection
- Responsive feel
- **Runnable:** Fast collision

### Unit 101: Screen Effects
- Clear effects
- Flash effects
- Visual flair
- Celebration
- **Runnable:** Screen effects

### Unit 102: Tetris Clear Effect
- Special 4-line effect
- Dramatic animation
- Big reward
- Memorable
- **Runnable:** Tetris effect

### Unit 103: Level Up Effect
- Transition effect
- Copper flash
- Celebration
- Progress marker
- **Runnable:** Level up effect

### Unit 104: High Score Entry
- Name input
- Keyboard handling
- Character selection
- Score saving
- **Runnable:** Name entry

### Unit 105: High Score Table
- Top 10 display
- Per-mode scores
- Names and scores
- Competition
- **Runnable:** Score table

### Unit 106: Score Persistence
- Save to disk
- Load on start
- Reliable storage
- Permanent records
- **Runnable:** Saved scores

### Unit 107: Demo Mode
- AI on title
- Shows gameplay
- Attract mode
- Arcade feel
- **Runnable:** Demo mode

### Unit 108: Copper Tricks
- Advanced effects
- Raster bars
- Dynamic palette
- Amiga showcase
- **Runnable:** Copper tricks

### Unit 109: DAS Tuning
- Delayed auto-shift
- Auto-repeat rate
- Modern feel
- Comfortable controls
- **Runnable:** DAS tuned

### Unit 110: Lock Delay Options
- Adjustable delay
- Move reset option
- Player preference
- Fair mechanics
- **Runnable:** Lock options

### Unit 111: A500 Compatibility
- 512K chip RAM
- OCS compatible
- Wide compatibility
- Mass market
- **Runnable:** A500 tested

### Unit 112: Phase 7 Integration
- All optimisations
- Effects complete
- High scores
- Polished build
- **Runnable:** Optimised game

---

## Phase 8: Final Polish & Release (Units 113-128)
*Final quality and release*

### Unit 113: Bug Testing
- Systematic testing
- All modes
- Edge cases
- Bug fixes
- **Runnable:** Bug-free

### Unit 114: Balance Testing
- Speed curve
- Scoring balance
- Mode balance
- Fair gameplay
- **Runnable:** Balanced

### Unit 115: Control Tuning
- Input feel
- DAS/ARR settings
- Responsive controls
- Comfortable play
- **Runnable:** Tuned controls

### Unit 116: Audio Balance
- Music/SFX levels
- Channel balance
- Pleasant mix
- No distortion
- **Runnable:** Balanced audio

### Unit 117: Visual Consistency
- Colour harmony
- Theme consistency
- Professional look
- Polished visuals
- **Runnable:** Visual polish

### Unit 118: Loading Screen
- Attractive loader
- Progress display
- Game branding
- Professional start
- **Runnable:** Loading screen

### Unit 119: Credits
- Developer credits
- Music credits
- Acknowledgements
- Complete credits
- **Runnable:** Credits screen

### Unit 120: Instructions
- How to play
- Controls
- Mode descriptions
- Complete help
- **Runnable:** Instructions

### Unit 121: Disk Format
- Bootable ADF
- File structure
- Proper boot
- Disk ready
- **Runnable:** ADF created

### Unit 122: Multi-Disk Check
- Single disk fits
- Or handle multi-disk
- User experience
- Proper distribution
- **Runnable:** Disk verified

### Unit 123: Final Performance
- Stable 50fps
- No slowdown
- Consistent timing
- Release quality
- **Runnable:** Stable game

### Unit 124: Full Testing
- All modes played
- All features tested
- No issues
- Quality verified
- **Runnable:** Fully tested

### Unit 125: Playtesting
- External feedback
- Fresh perspectives
- Final adjustments
- User validation
- **Runnable:** Playtested

### Unit 126: Documentation
- Game manual
- Controls reference
- Mode descriptions
- Complete package
- **Runnable:** Documented

### Unit 127: Release Build
- Final disk image
- Version numbered
- Release notes
- Ready for release
- **Runnable:** Release ADF

### Unit 128: Project Retrospective
- Puzzle game mastery
- Blitter efficiency
- Rotation maths
- Two-player systems
- **Runnable:** Complete Tetrad

---

## Technical Summary

### Key Amiga Features Used
- Blitter for grid rendering
- Blitter scroll for line clear
- Copper for colour effects
- Paula for audio
- Efficient 68000 code

### Code Patterns Introduced
```asm
; Piece rotation with collision
try_rotate:
    move.b  rotation,d0
    addq.b  #1,d0
    and.b   #3,d0           ; Wrap 0-3
    move.b  d0,temp_rotation
    bsr     check_rotation_collision
    tst.b   d0
    bne.s   .try_kick
    ; Rotation valid
    move.b  temp_rotation,rotation
    rts
.try_kick:
    ; Try wall kick offsets
    bsr     try_wall_kicks
    rts

; Line clear with Blitter scroll
clear_line:
    ; Calculate source and dest
    ; Blitter scroll rows down
    move.w  #$09f0,BLTCON0
    move.w  #$0000,BLTCON1
    move.l  source,BLTAPT
    move.l  dest,BLTDPT
    move.w  #(lines*64)+BLIT_WIDTH,BLTSIZE
    rts
```

### Skills Progression
| Phase | Primary Skills |
|-------|---------------|
| 1 | Blitter rendering, grid system |
| 2 | Rotation, collision, locking |
| 3 | Scoring, speed progression |
| 4 | Wall kicks, T-spins, audio |
| 5 | Game modes, multiplayer |
| 6 | Themes, achievements |
| 7 | Optimisation, effects |
| 8 | Polish, release |

---

## Version History
- v1.0 - Initial 128-unit outline
