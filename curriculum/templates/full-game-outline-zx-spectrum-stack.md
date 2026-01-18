# Game 8: Stack - Complete 128-Unit Outline

## Game Overview
**Platform:** Sinclair ZX Spectrum
**Genre:** Falling blocks puzzle (Tetris-style)
**Concept:** Classic falling block puzzle with piece rotation, line clearing, and increasing speed. Tetriminos fall from above, player rotates and positions them to complete lines.

**Technical Focus:**
- Piece rotation mathematics (4 orientations)
- Grid collision detection
- Line detection and clearing
- Timer-based falling
- Wall kick mechanics
- Next piece preview and ghost piece
- Two-player competitive mode

---

## Phase 1: Foundation (Units 1-16)
*Establish playfield and piece display*

### Unit 1: Project Setup
- Create stack project structure
- Memory layout for puzzle game
- Basic initialisation
- System setup
- **Runnable:** Clean startup

### Unit 2: Display Configuration
- Screen setup for playfield
- Colour attribute planning
- Border colour
- Clean display
- **Runnable:** Display ready

### Unit 3: Colour Scheme
- Playfield background
- Piece colours (7 pieces = 7 colours)
- Border colours
- Visual clarity
- **Runnable:** Colour palette set

### Unit 4: Playfield Design
- 10 wide x 20 tall standard
- Grid to screen mapping
- Pixel dimensions
- Playfield borders
- **Runnable:** Playfield designed

### Unit 5: Draw Playfield Border
- Surrounding frame
- Clear interior
- Attribute colouring
- Clean playing area
- **Runnable:** Playfield visible

### Unit 6: Grid Data Structure
- 10x20 array
- Cell states (empty/filled/piece type)
- Memory efficient storage
- Grid access routines
- **Runnable:** Grid allocated

### Unit 7: Piece Definition
- Seven standard tetriminos
- I, O, T, S, Z, J, L shapes
- 4x4 bounding box
- Piece data format
- **Runnable:** Pieces defined

### Unit 8: Rotation Data
- 4 orientations per piece
- Rotation state data
- All 28 orientations stored
- Efficient lookup
- **Runnable:** Rotations defined

### Unit 9: Draw Single Block
- One cell rendering
- Attribute colour
- Solid or patterned
- Building block
- **Runnable:** Block draws

### Unit 10: Draw Piece at Position
- Render piece from data
- Position on grid
- Correct orientation
- Visible piece
- **Runnable:** Piece displayed

### Unit 11: Piece Spawn Position
- Top-centre spawn
- Starting orientation
- Initial position
- Entry point
- **Runnable:** Piece spawns

### Unit 12: Current Piece State
- Position X, Y
- Rotation state
- Piece type
- Active piece tracking
- **Runnable:** Piece state managed

### Unit 13: Input Detection
- Keyboard reading
- Left/Right/Down/Rotate
- Key mappings
- Responsive input
- **Runnable:** Input detected

### Unit 14: Move Left/Right
- Horizontal movement
- One cell per press
- Boundary checking
- Smooth control
- **Runnable:** Piece moves sideways

### Unit 15: Visual Update
- Clear old position
- Draw at new position
- Efficient redraw
- Flicker-free
- **Runnable:** Smooth movement

### Unit 16: Phase 1 Integration
- Playfield displayed
- Piece spawns and moves
- Foundation complete
- **Runnable:** Basic piece control

---

## Phase 2: Core Mechanics (Units 17-32)
*Rotation, falling, and locking*

### Unit 17: Rotation Input
- Rotate key detection
- Clockwise rotation
- Counter-clockwise option
- Rotation input
- **Runnable:** Rotation triggered

### Unit 18: Rotation Logic
- Increment rotation state
- Wrap 0-3
- Update piece display
- State change
- **Runnable:** Piece rotates

### Unit 19: Collision Detection Concept
- Check before move/rotate
- Grid overlap detection
- Boundary detection
- Prevent illegal moves
- **Runnable:** Concept defined

### Unit 20: Grid Collision Check
- Piece vs placed blocks
- Check all cells
- Return collision flag
- Accurate detection
- **Runnable:** Collision works

### Unit 21: Boundary Collision
- Left/right wall check
- Floor check
- Prevent out-of-bounds
- Combined with grid check
- **Runnable:** Boundaries enforced

### Unit 22: Move with Collision
- Check before moving
- Reject invalid moves
- Only allow legal moves
- Proper physics
- **Runnable:** Collision-safe movement

### Unit 23: Rotate with Collision
- Check rotation validity
- Reject if blocked
- Wall kick placeholder
- Safe rotation
- **Runnable:** Collision-safe rotation

### Unit 24: Fall Timer
- Frame counter
- Fall interval
- Timer-based descent
- Consistent speed
- **Runnable:** Timer running

### Unit 25: Automatic Falling
- Piece drops one row
- Timer-triggered
- Continuous descent
- Game flow
- **Runnable:** Piece falls

### Unit 26: Soft Drop
- Down key speeds fall
- Faster descent
- Player control
- Score bonus
- **Runnable:** Soft drop works

### Unit 27: Hard Drop
- Instant drop to bottom
- Find landing position
- Quick placement
- Advanced control
- **Runnable:** Hard drop works

### Unit 28: Lock Detection
- Piece cannot move down
- Lock delay timer
- Prepare to place
- Landing detection
- **Runnable:** Landing detected

### Unit 29: Lock Piece
- Transfer to grid
- Mark cells as filled
- Piece type stored
- Permanent placement
- **Runnable:** Piece locks

### Unit 30: Line Detection
- Check all rows
- Find complete lines
- Mark for clearing
- Line counting
- **Runnable:** Lines detected

### Unit 31: Line Clearing
- Remove complete lines
- Drop rows above
- Grid compression
- Visual clearing
- **Runnable:** Lines clear

### Unit 32: Phase 2 Integration
- Full piece control
- Rotation and falling
- Collision and locking
- Line clearing
- **Runnable:** Core Tetris gameplay

---

## Phase 3: Game Systems (Units 33-48)
*Scoring, speed, and game flow*

### Unit 33: Score System
- Points per line
- Single/Double/Triple/Tetris
- Score variable
- Point values
- **Runnable:** Score increments

### Unit 34: Score Display
- Score area on screen
- Number rendering
- Formatted display
- Live update
- **Runnable:** Score visible

### Unit 35: Line Counter
- Total lines cleared
- Lines display
- Progress tracking
- Achievement count
- **Runnable:** Lines counted

### Unit 36: Level System
- Level increases with lines
- 10 lines per level
- Level display
- Progression
- **Runnable:** Level tracking

### Unit 37: Speed Increase
- Faster falling per level
- Speed curve
- Maximum speed cap
- Difficulty progression
- **Runnable:** Speed increases

### Unit 38: Next Piece Preview
- Preview area
- Show upcoming piece
- Strategic planning
- Preview display
- **Runnable:** Next piece shown

### Unit 39: Piece Randomiser
- Random piece selection
- Bag randomiser (7-bag)
- Fair distribution
- No long droughts
- **Runnable:** Fair random

### Unit 40: Ghost Piece
- Show landing position
- Transparent/outlined
- Placement preview
- Helpful guide
- **Runnable:** Ghost piece visible

### Unit 41: Game Over Detection
- Piece spawns blocked
- Stack too high
- Game end condition
- Detect game over
- **Runnable:** Game over detected

### Unit 42: Game Over Screen
- Final score display
- High score check
- Restart option
- Clear ending
- **Runnable:** Game over screen

### Unit 43: Title Screen
- Game title
- Start prompt
- Controls display
- High score
- **Runnable:** Title screen

### Unit 44: Title Animation
- Falling blocks demo
- Animated title
- Attract mode
- Visual appeal
- **Runnable:** Animated title

### Unit 45: Pause Function
- Pause key
- Freeze gameplay
- Hidden playfield
- Resume function
- **Runnable:** Pause works

### Unit 46: Hold Piece
- Store current piece
- Swap with held
- One swap per piece
- Strategic option
- **Runnable:** Hold piece works

### Unit 47: Hold Display
- Hold area
- Show held piece
- Clear indication
- UI element
- **Runnable:** Hold displayed

### Unit 48: Phase 3 Integration
- Full scoring system
- Speed progression
- Preview and hold
- Complete game flow
- **Runnable:** Full puzzle game

---

## Phase 4: Polish & Feel (Units 49-64)
*Visual and audio refinement*

### Unit 49: Wall Kick System
- Rotation adjustment
- Try offset positions
- SRS-style kicks
- Better rotation
- **Runnable:** Wall kicks work

### Unit 50: Wall Kick Data
- Kick offset tables
- Per-piece kick data
- Standard kick tests
- Robust rotation
- **Runnable:** Full kick system

### Unit 51: T-Spin Detection
- Detect T-spin placement
- Corner checks
- Special scoring
- Advanced technique
- **Runnable:** T-spins detected

### Unit 52: T-Spin Scoring
- Bonus points for T-spins
- T-spin single/double/triple
- Skill reward
- Score display
- **Runnable:** T-spin scoring

### Unit 53: Combo System
- Consecutive line clears
- Combo counter
- Bonus points
- Combo display
- **Runnable:** Combos work

### Unit 54: Back-to-Back
- Consecutive Tetris/T-spins
- Bonus multiplier
- Skill chain
- B2B display
- **Runnable:** Back-to-back

### Unit 55: Clear Animation
- Line flash effect
- Removal animation
- Visual feedback
- Satisfying clear
- **Runnable:** Clear animation

### Unit 56: Lock Animation
- Flash on lock
- Placement confirmation
- Brief highlight
- Visual feedback
- **Runnable:** Lock animation

### Unit 57: Beeper Sound Setup
- Sound effect system
- Beeper routines
- Effect triggers
- Audio feedback
- **Runnable:** Sound ready

### Unit 58: Movement Sounds
- Move sound
- Rotate sound
- Distinct effects
- Tactile feedback
- **Runnable:** Movement audio

### Unit 59: Line Clear Sound
- Satisfying clear sound
- Tetris special sound
- Impact audio
- Reward feedback
- **Runnable:** Clear sounds

### Unit 60: Drop and Lock Sounds
- Soft drop sound
- Hard drop sound
- Lock sound
- Complete audio set
- **Runnable:** Drop sounds

### Unit 61: Music System
- Background music
- Korobeiniki-style
- Tempo with speed
- Puzzle atmosphere
- **Runnable:** Background music

### Unit 62: HUD Polish
- Clean score area
- Level display
- Lines display
- Professional layout
- **Runnable:** Polished HUD

### Unit 63: Visual Themes
- Colour variations
- Theme selection
- Personal preference
- Visual options
- **Runnable:** Theme options

### Unit 64: Phase 4 Integration
- Wall kicks complete
- T-spins working
- Audio polish
- Visual polish
- **Runnable:** Polished Stack

---

## Phase 5: Advanced Features (Units 65-80)
*Game modes and multiplayer*

### Unit 65: Marathon Mode
- Endless play
- Speed caps at 20
- High score focus
- Classic mode
- **Runnable:** Marathon mode

### Unit 66: Sprint Mode
- Clear 40 lines
- Fastest time wins
- Timer display
- Speed challenge
- **Runnable:** Sprint mode

### Unit 67: Ultra Mode
- 2-minute time limit
- Maximum score
- Time pressure
- Score attack
- **Runnable:** Ultra mode

### Unit 68: Mode Selection
- Mode menu
- Clear descriptions
- Mode variety
- Easy selection
- **Runnable:** Mode menu

### Unit 69: Two-Player Concept
- Split screen
- Head-to-head
- Garbage lines
- Competitive play
- **Runnable:** Two-player design

### Unit 70: Split Screen Display
- Two playfields
- Shared screen
- Player indicators
- Visual separation
- **Runnable:** Split display

### Unit 71: Two-Player Controls
- Separate key bindings
- No conflicts
- Both players play
- Control mapping
- **Runnable:** Dual controls

### Unit 72: Garbage Lines
- Lines sent to opponent
- Incomplete lines
- Attack mechanic
- Competitive element
- **Runnable:** Garbage system

### Unit 73: Garbage Display
- Incoming warning
- Line indicator
- Strategic information
- Clear communication
- **Runnable:** Garbage warning

### Unit 74: Two-Player Win
- First to top out loses
- Winner celebration
- Match end
- Victory screen
- **Runnable:** Win condition

### Unit 75: Match System
- Best of 3/5
- Match scoring
- Series play
- Extended competition
- **Runnable:** Match system

### Unit 76: AI Opponent
- Computer player
- Basic AI decisions
- Placement logic
- Single-player versus
- **Runnable:** AI opponent

### Unit 77: AI Difficulty
- Easy/Medium/Hard
- Decision quality
- Reaction speed
- Fair challenge
- **Runnable:** AI levels

### Unit 78: Custom Game
- Starting level
- Starting lines
- Garbage mode
- Customisation
- **Runnable:** Custom settings

### Unit 79: Master Mode
- 20G (instant drop)
- Extreme challenge
- For experts
- Brutal mode
- **Runnable:** Master mode

### Unit 80: Phase 5 Integration
- All modes working
- Two-player complete
- AI opponent
- Mode variety
- **Runnable:** Feature-complete

---

## Phase 6: Content & Variety (Units 81-96)
*Content depth and replay value*

### Unit 81: Level 1-5 Speeds
- Gentle introduction
- Learning curve
- Comfortable start
- Beginner friendly
- **Runnable:** Early levels

### Unit 82: Level 6-10 Speeds
- Moderate challenge
- Skill development
- Intermediate play
- Good progression
- **Runnable:** Mid levels

### Unit 83: Level 11-15 Speeds
- Fast gameplay
- Requiring skill
- Advanced territory
- Challenging
- **Runnable:** Fast levels

### Unit 84: Level 16-20 Speeds
- Maximum speed
- Expert only
- Extreme challenge
- End-game
- **Runnable:** Expert levels

### Unit 85: Achievement System
- Track accomplishments
- First Tetris
- Score milestones
- Skill achievements
- **Runnable:** Achievements

### Unit 86: Achievement Display
- Achievement list
- Unlock status
- Progress view
- Collection screen
- **Runnable:** Achievement screen

### Unit 87: Statistics
- Games played
- Lines cleared total
- Tetrises
- Best scores
- **Runnable:** Statistics screen

### Unit 88: Line Clear Stats
- Singles count
- Doubles count
- Triples count
- Tetris count
- **Runnable:** Detailed stats

### Unit 89: Piece Statistics
- Pieces placed per type
- Distribution analysis
- Play patterns
- Data tracking
- **Runnable:** Piece stats

### Unit 90: Tutorial Mode
- Guided introduction
- Basic controls
- Rotation demonstration
- Welcoming start
- **Runnable:** Tutorial

### Unit 91: Advanced Tutorial
- T-spin teaching
- Wall kick demonstration
- Combo building
- Skill development
- **Runnable:** Advanced tutorial

### Unit 92: Replay System
- Record game
- Playback
- Watch performance
- Learning tool
- **Runnable:** Replay system

### Unit 93: Ghost Toggle
- Enable/disable ghost
- Player preference
- Difficulty adjustment
- Option setting
- **Runnable:** Ghost toggle

### Unit 94: Alternate Controls
- Multiple control schemes
- QAOP/Arrow alternatives
- Player preference
- Customisation
- **Runnable:** Control options

### Unit 95: 128K Music
- AY music tracks
- Multiple songs
- Music variety
- Enhanced audio
- **Runnable:** 128K music

### Unit 96: Phase 6 Integration
- All content complete
- Achievements and stats
- Tutorials
- Full options
- **Runnable:** Content complete

---

## Phase 7: Optimisation & Effects (Units 97-112)
*Performance and visual effects*

### Unit 97: Performance Analysis
- Measure frame timing
- Identify bottlenecks
- Optimisation targets
- Profile code
- **Runnable:** Performance data

### Unit 98: Grid Operations Optimised
- Faster line detection
- Efficient clearing
- Optimised grid access
- Speed improvement
- **Runnable:** Fast grid ops

### Unit 99: Piece Drawing Optimised
- Faster piece render
- Reduced calculations
- Efficient updates
- Quick drawing
- **Runnable:** Fast drawing

### Unit 100: Collision Optimised
- Faster collision checks
- Early exit conditions
- Efficient detection
- Responsive controls
- **Runnable:** Fast collision

### Unit 101: Screen Effects
- Line clear effects
- Flash patterns
- Visual flair
- Celebration
- **Runnable:** Screen effects

### Unit 102: Tetris Clear Effect
- Special 4-line effect
- Dramatic clear
- Reward visual
- Memorable moment
- **Runnable:** Tetris effect

### Unit 103: Level Up Effect
- Level transition
- Brief celebration
- Speed warning
- Progression marker
- **Runnable:** Level up effect

### Unit 104: High Score Entry
- Name input
- Letter selection
- Character limit
- Score saving
- **Runnable:** Name entry

### Unit 105: High Score Table
- Top 10 display
- Names and scores
- By game mode
- Persistent records
- **Runnable:** Score table

### Unit 106: Score Persistence
- Save to tape/disk
- Load on start
- Reliable storage
- Competition records
- **Runnable:** Saved scores

### Unit 107: Demo Mode
- AI plays on title
- Shows gameplay
- Attract mode
- No-input demo
- **Runnable:** Demo mode

### Unit 108: Border Effects
- Border colour changes
- Line clear flash
- Level indication
- Visual feedback
- **Runnable:** Border effects

### Unit 109: Smooth Dropping
- Per-pixel falling
- Smooth animation
- Visual polish
- Modern feel
- **Runnable:** Smooth drop

### Unit 110: Lock Delay Polish
- Adjustable delay
- Move reset option
- Modern mechanics
- Fair timing
- **Runnable:** Lock delay tuned

### Unit 111: 48K/128K Detection
- Detect machine type
- Enable features
- Graceful scaling
- Compatibility
- **Runnable:** Machine detection

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
- All modes tested
- Bug fixes
- **Runnable:** Bug-free game

### Unit 114: Balance Testing
- Speed curve check
- Scoring balance
- Mode balance
- Fair gameplay
- **Runnable:** Balanced game

### Unit 115: Control Tuning
- Input responsiveness
- DAS (delayed auto-shift)
- ARR (auto-repeat rate)
- Comfortable controls
- **Runnable:** Tuned controls

### Unit 116: Audio Balance
- Music/SFX levels
- No interference
- Pleasant mix
- Balanced audio
- **Runnable:** Balanced audio

### Unit 117: Visual Consistency
- Colour harmony
- Consistent style
- No visual bugs
- Professional look
- **Runnable:** Visual polish

### Unit 118: Loading Screen
- Attractive loader
- Game branding
- Progress display
- Professional start
- **Runnable:** Loading screen

### Unit 119: Credits Screen
- Developer credits
- Acknowledgements
- Music credits
- Complete credits
- **Runnable:** Credits

### Unit 120: Instructions Screen
- How to play
- All controls
- Mode explanations
- Complete help
- **Runnable:** Instructions

### Unit 121: Tape Version
- TAP format
- Loading code
- Tape-compatible
- Standard release
- **Runnable:** Tape version

### Unit 122: +3 Disk Version
- +3DOS format
- Disk-based
- Quick loading
- Disk release
- **Runnable:** Disk version

### Unit 123: Final Performance
- Stable frame rate
- No slowdowns
- Consistent timing
- Release quality
- **Runnable:** Stable game

### Unit 124: Full Playthrough
- Test all modes
- Complete experience
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
- Control reference
- Mode descriptions
- Complete package
- **Runnable:** Documented

### Unit 127: Release Build
- Final compilation
- All files packaged
- Version numbered
- Release ready
- **Runnable:** Release build

### Unit 128: Project Retrospective
- Techniques learned
- Rotation maths mastery
- Grid collision expertise
- Puzzle game skills
- **Runnable:** Complete Stack

---

## Technical Summary

### Key ZX Spectrum Features Used
- Attribute-based colour
- Efficient grid operations
- Timer-based gameplay
- Beeper sound effects
- 128K AY music (optional)

### Code Patterns Introduced
```z80
; Piece rotation lookup
get_piece_data:
    ; a = piece type (0-6)
    ; b = rotation (0-3)
    ld h,0
    ld l,a
    add hl,hl
    add hl,hl           ; piece * 4
    ld a,b
    add a,l
    ld l,a              ; + rotation
    ld de,piece_table
    add hl,de
    ; hl = pointer to piece data
    ret

; Line clear check
check_lines:
    ld b,20             ; 20 rows
    ld hl,grid
check_row:
    ld c,10             ; 10 columns
    push hl
check_cell:
    ld a,(hl)
    or a
    jr z,not_complete   ; empty cell found
    inc hl
    dec c
    jr nz,check_cell
    ; row is complete - mark for clearing
    pop hl
    call mark_line
    jr next_row
not_complete:
    pop hl
next_row:
    ld de,10
    add hl,de
    djnz check_row
    ret
```

### Skills Progression
| Phase | Primary Skills |
|-------|---------------|
| 1 | Playfield, piece display |
| 2 | Rotation, collision, locking |
| 3 | Scoring, speed, game flow |
| 4 | Wall kicks, T-spins, audio |
| 5 | Game modes, multiplayer |
| 6 | Content, achievements |
| 7 | Optimisation, effects |
| 8 | Polish, release |

---

## Version History
- v1.0 - Initial 128-unit outline
