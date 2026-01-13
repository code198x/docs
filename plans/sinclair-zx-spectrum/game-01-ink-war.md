# Ink War: 64-Unit Outline

**Game:** ZX Spectrum Game 1: Ink War
**Units:** 64
**Concept:** Territory control game - two players take turns claiming 8×8 attribute cells. Control the majority to win.

**Commercial Quality Target:** A game that could have sold for £7.99 on cassette in 1984. Simple, addictive, polished.

**Design Principle:** "Show First, Explain Later" - Scaffold provides working code immediately; theory follows experience.

---

## The Finished Game

Before detailing the units, here's what the learner builds:

### Core Gameplay
- 8×8 board of attribute cells (64 total)
- Two players (Red vs Blue) take turns
- Cursor moves with keyboard (Q/A/O/P or cursor keys)
- Space/Enter claims the current cell
- Can't claim already-claimed cells
- Game ends when board is full
- Player with most cells wins

### Content
- Single-player vs AI (Easy/Normal/Hard)
- Two-player hot-seat mode
- Board size options (6×6, 8×8)
- Practice mode (undo available)

### Audio
- Beeper sound effects (claim, invalid, turn change)
- Victory/defeat jingles
- Simple title music

### Visuals
- Custom character set for board and UI
- Animated cursor
- Score display
- Turn indicator
- Win celebration effect

### Polish
- Title screen
- Options menu
- High score display
- Pause functionality

---

## Engagement Milestones

| Milestone | Unit |
|-----------|------|
| First visible output (game board) | 1 |
| First interactivity (cursor moves) | 1 |
| First "game feel" (claiming cells) | 2 |
| Complete two-player game | 8 |
| Complete playable game with AI | 16 |

---

## Phase 1: Foundation (Units 1-16)

*Goal: A working two-player game with AI opponent. Playable from start to finish.*

*By the end of this phase, the learner has built a complete game. Humans can play against each other or against the computer. It's simple but fully functional - claim cells, track score, detect winner.*

---

### Unit 1: Hello Spectrum

**Learning Objectives:**
- Run a working ZX Spectrum program
- See the game board immediately
- Move a cursor with keyboard
- Experience the attribute system from minute one

**Concepts Introduced:**
- Scaffold approach (working code provided)
- Attribute memory overview
- Keyboard input basics
- Game loop structure

**Scaffold Provides:**
- BASIC loader (RANDOMIZE USR 32768)
- Game board drawn (8×8 grid with border)
- Cursor displayed on the board
- Keyboard reading for Q/A/O/P
- Cursor movement within board boundaries

**What the Learner Does:**
- Runs the scaffold - sees game board immediately
- Presses Q - cursor moves up
- Presses A - cursor moves down
- Presses O - cursor moves left
- Presses P - cursor moves right
- Changes border colour in code, sees immediate result
- Changes cursor colour, sees it change

**What the Learner Sees:**
A centred 8×8 game board with black border. A flashing cursor on the board. Pressing Q/A/O/P moves the cursor around. Interactive from the first moment.

**Technical Details:**
- Attribute memory: $5800-$5AFF
- Border colour: OUT ($FE), A
- Keyboard port: $FE with row selection
- Cursor: flashing using FLASH attribute bit

---

### Unit 2: Claiming Cells

**Learning Objectives:**
- Press Space to claim cells
- See cells change to player colour
- Track whose turn it is
- Experience core gameplay

**Concepts Introduced:**
- Cell state tracking
- Action key detection
- State change (empty → claimed)
- Turn alternation

**Code Written:**
```
- board_state: 64-byte array (0=empty, 1=red, 2=blue)
- current_player: starts at 1
- Space key detection
- Claim cell: set state, change attribute colour
- Alternate turns after valid claim
- Sound feedback on claim
```

**What the Learner Sees:**
Press Space on an empty cell - it turns red (Player 1's colour). Turn indicator changes. Press Space again - next cell turns blue (Player 2). Core gameplay works already.

**Technical Details:**
- Player 1: bright red paper (%01010000)
- Player 2: bright blue paper (%01001000)
- Empty: white paper (%00111000)
- State array: 64 bytes, indexed by row×8+col

---

### Unit 3: Making It Yours

**Learning Objectives:**
- Customise board colours (learn attribute byte structure)
- Move the board position (learn address calculation)
- Change cursor appearance (learn FLASH/BRIGHT bits)
- Understand by modifying, not just reading

**Concepts Introduced:**
- Attribute byte format (FBPPPIII) - through changing colours
- Address calculation: $5800 + row×32 + col - through moving the board
- FLASH and BRIGHT bits - through cursor customisation

**Code Written:**
```
- Change board border colour (modify attribute values)
- Change empty cell colour (white → cyan or other)
- Move board to different screen position
- Change cursor from FLASH to BRIGHT cycling
- Add border colour change on turn switch
```

**What the Learner Sees:**
A customised version of the game - different colours, different position, different cursor style. They've made it their own by understanding and changing the internals.

**Technical Details:**
- Attribute byte: bit 7=FLASH, bit 6=BRIGHT, bits 5-3=PAPER, bits 2-0=INK
- Colours: 0=black, 1=blue, 2=red, 3=magenta, 4=green, 5=cyan, 6=yellow, 7=white
- Board position: adjust base address calculation
- Border: OUT ($FE), A with colour in bits 0-2

---

### Unit 4: Score and Turn Display

**Learning Objectives:**
- Count cells owned by each player
- Display scores on screen
- Show whose turn it is
- Update display after each move

**Concepts Introduced:**
- Cell counting (iterate board)
- Number to character conversion
- UI areas on screen
- Efficient updates

**Code Written:**
```
- count_cells: iterate board, count 1s and 2s
- display_score: show "RED: nn  BLUE: nn"
- Turn indicator (coloured bar or text)
- Update after each claim
```

**What the Learner Sees:**
Score display at top shows "RED: 3 BLUE: 2". Turn indicator shows whose move it is. Numbers update when cells are claimed. Players can see who's winning.

**Technical Details:**
- Score at row 0-1 of screen
- Number display: add $30 (ASCII offset)
- Turn indicator: coloured attribute cells
- Maximum score: 64 (fits in two digits)

---

### Unit 5: Move Validation

**Learning Objectives:**
- Check if cell is already claimed
- Provide feedback for invalid moves
- Only switch turns on valid moves
- Beeper sound effects

**Concepts Introduced:**
- Input validation
- Error feedback (visual + audio)
- Beeper sound generation
- Defensive programming

**Code Written:**
```
- validate_move: check board_state[index] == 0
- Invalid: play error buzz, flash border red
- Valid: play success tone, proceed
- Don't change turn on invalid move
```

**What the Learner Sees:**
Pressing Space on an occupied cell plays a harsh buzz and border flashes red. Turn doesn't change. Only valid moves progress the game. Clear feedback for mistakes.

**Technical Details:**
- Beeper port: bit 4 of $FE
- Error sound: short noise at low frequency
- Success sound: pleasant rising tone
- Border flash: 2-3 frames of red

---

### Unit 6: Game End Detection

**Learning Objectives:**
- Detect when board is full
- Determine winner (or draw)
- Display results
- Allow restart

**Concepts Introduced:**
- End condition detection
- Score comparison
- Result states (win/lose/draw)
- Game restart

**Code Written:**
```
- Check if moves == 64 (or count empty == 0)
- Compare scores to determine winner
- Display "RED WINS!" or "BLUE WINS!" or "DRAW!"
- Flash screen in winner's colour
- Press key to restart
```

**What the Learner Sees:**
After 64 moves, "RED WINS!" (or similar) appears. Border flashes winner's colour. Press any key to play again. Complete game loop.

**Technical Details:**
- moves_made counter incremented each valid claim
- Game over when moves_made == 64
- Winner: score1 > score2 → P1, score2 > score1 → P2, else draw
- Victory celebration: colour cycling effect

---

### Unit 7: Title Screen

**Learning Objectives:**
- Create title screen state
- Display game title
- Start game on key press
- Simple state machine

**Concepts Introduced:**
- Game states (TITLE, PLAYING, RESULTS)
- State machine pattern
- State dispatch
- Title screen design

**Code Written:**
```
- game_state: TITLE=0, PLAYING=1, RESULTS=2
- Title screen: "INK WAR" in large text
- "PRESS ANY KEY TO START"
- Key press → transition to PLAYING
- Results → key press → TITLE
```

**What the Learner Sees:**
Game starts at title screen with "INK WAR". Press any key to start playing. After game ends, results show, then key returns to title. Complete game flow.

**Technical Details:**
- State values: TITLE=0, PLAYING=1, RESULTS=2
- Clear screen between states
- Reset board when entering PLAYING

---

### Unit 8: Complete Two-Player Game

**Learning Objectives:**
- Polish the experience
- Fix remaining issues
- Test complete flow
- Playable with a friend

**Concepts Introduced:**
- Integration testing
- Polish pass
- Edge cases
- Completeness checklist

**Code Written:**
```
- Final bug fixes
- Visual alignment fixes
- Input timing adjustments
- Complete playthrough verification
```

**What the Learner Sees:**
Complete, polished two-player game. Title → Play → Results → Title works perfectly. Hand the keyboard to a friend and play Ink War.

**Phase 1 Midpoint:**
At Unit 8, two humans can play Ink War competitively. The core game is complete.

---

### Unit 9: AI Framework

**Learning Objectives:**
- Add game mode selection (vs Human / vs AI)
- Implement random cell selection (baseline AI)
- Replace Player 2 with AI when selected
- Handle AI turn automatically

**Concepts Introduced:**
- Game mode variable
- AI turn handling
- Random number generation
- Finding valid moves

**Code Written:**
```
- game_mode: TWO_PLAYER or VS_AI
- Mode selection on title screen
- find_empty_cell: locate any empty cell
- AI makes random valid move
- Brief delay before AI moves
```

**What the Learner Sees:**
Title screen offers "1 - Two Player" / "2 - vs Computer". Selecting vs Computer, the AI takes Player 2's turns automatically. It plays randomly but legally.

**Technical Details:**
- Random using R register
- Find empty: scan board_state for 0
- AI delay: 25 frames (0.5 second)
- AI takes blue (player 2) side

---

### Unit 10: Smarter AI - Adjacent Priority

**Learning Objectives:**
- AI prefers cells adjacent to own territory
- Build connected territory clusters
- Evaluate cell adjacency
- More strategic behaviour

**Concepts Introduced:**
- Cell adjacency checking
- Priority scoring
- Building territory
- AI personality

**Code Written:**
```
- check_adjacent: count friendly neighbours
- Score cells by adjacency
- Pick highest-scoring empty cell
- Fall back to random if no adjacent options
```

**What the Learner Sees:**
AI builds connected regions instead of scattered claims. Territory grows outward. More intelligent behaviour.

---

### Unit 11: Defensive AI

**Learning Objectives:**
- AI blocks opponent expansion
- Evaluate defensive value of cells
- Balance offense and defense
- React to opponent's position

**Concepts Introduced:**
- Opponent adjacency
- Threat assessment
- Multi-factor evaluation
- Balanced strategy

**Code Written:**
```
- Count enemy adjacent cells
- High enemy adjacency = blocking opportunity
- Combine with friendly adjacency score
- Weighted evaluation
```

**What the Learner Sees:**
AI blocks player expansion too. More competitive. Harder to beat.

---

### Unit 12: Corner and Edge Strategy

**Learning Objectives:**
- AI values corners highly
- Edge cells have strategic value
- Position-based scoring
- Opening strategy

**Concepts Introduced:**
- Static cell values
- Corner importance
- Edge control
- Strategic positioning

**Code Written:**
```
- Cell value table (corners=high, edges=medium)
- Add position value to cell score
- Corners grabbed early
- Strategic opening moves
```

**What the Learner Sees:**
AI grabs corners early. Edge cells prioritised. Feels like playing a real opponent.

---

### Unit 13: AI Difficulty Levels

**Learning Objectives:**
- Implement Easy/Normal/Hard difficulty
- Easy: mostly random with some strategy
- Hard: full strategic evaluation
- Difficulty selection menu

**Concepts Introduced:**
- Difficulty parameter
- Probability-based decisions
- Strategy weight adjustment
- Player choice

**Code Written:**
```
- ai_difficulty: EASY, NORMAL, HARD
- Easy: 70% random, 30% strategic
- Normal: 30% random, 70% strategic
- Hard: 100% strategic
- Difficulty selection on mode screen
```

**What the Learner Sees:**
Choose AI difficulty. Easy is beatable by beginners. Hard requires good strategy to win.

---

### Unit 14: Sound Effects

**Learning Objectives:**
- Create distinct sounds for events
- Claim sounds, error sounds
- Victory/defeat jingles
- Audio feedback completeness

**Concepts Introduced:**
- Beeper sound design
- Positive vs negative sounds
- Musical jingles
- Audio feedback

**Code Written:**
```
- sound_claim: pleasant rising tone
- sound_invalid: harsh buzz
- jingle_victory: triumphant phrase
- jingle_defeat: sad descending phrase
- sound_turn: subtle click
```

**What the Learner Sees:**
Every action has sound. Claiming feels good. Invalid moves sound wrong. Winning plays celebration tune.

---

### Unit 15: Results Screen

**Learning Objectives:**
- Create proper results display
- Show final scores
- Winner announcement
- Play again option

**Concepts Introduced:**
- Results screen layout
- Statistics display
- Screen composition
- Polish for end state

**Code Written:**
```
- Clear screen for results
- Large winner announcement
- Final scores displayed
- Win margin shown
- "PRESS ANY KEY" to continue
```

**What the Learner Sees:**
Proper results screen. Clear winner. Final scores. Professional presentation.

---

### Unit 16: Phase 1 Complete

**Learning Objectives:**
- Polish complete experience
- Test all modes
- Fix remaining issues
- Celebrate completion

**Concepts Introduced:**
- Integration testing
- Mode switching verification
- Polish pass
- Milestone celebration

**Code Written:**
```
- Test two-player mode
- Test all AI difficulty levels
- Fix any issues found
- Final visual polish
```

**What the Learner Sees:**
Complete game with two-player and AI modes. Three AI difficulty levels. Sound effects. Title screen, gameplay, results. A real game.

**Phase 1 Checkpoint:**
The learner has built a complete game. They understand Spectrum display, Z80 input handling, and game logic. Two-player and AI modes work. Everything from here builds on this foundation.

---

## Phase 2: Expansion (Units 17-32)

*Goal: Enhanced visuals, more options, and gameplay variety.*

*By the end of this phase, the game has custom graphics, animations, options menu, and board variations.*

---

### Unit 17: Custom Character Set

**Learning Objectives:**
- Design custom characters
- Load charset in memory
- Switch to custom charset
- Better visual quality

**Concepts Introduced:**
- Character memory
- 8×8 character design
- Charset loading
- Visual identity

**Code Written:**
```
- Design border characters
- Design UI characters
- Load at startup
- Use throughout game
```

**What the Learner Sees:**
Game uses custom characters. Nicer borders, better symbols. More polished appearance.

---

### Unit 18: Cursor Animation

**Learning Objectives:**
- Animate cursor visibility
- Pulsing or cycling effect
- Better visual focus
- Frame timing for animation

**Concepts Introduced:**
- Frame-based animation
- Colour cycling
- Animation states
- Visual feedback

**Code Written:**
```
- Cursor cycles between colours
- Or: cursor pulses using BRIGHT
- Smooth animation timing
- Clear visual focus
```

**What the Learner Sees:**
Cursor pulses or colour-cycles. Easier to see. More alive.

---

### Unit 19: Claim Animation

**Learning Objectives:**
- Animate cell claim
- Brief flash effect
- More satisfying claims
- Visual polish

**Concepts Introduced:**
- Event-triggered animation
- Brief effects
- Feedback layering
- Polish through motion

**Code Written:**
```
- Claim: flash white briefly
- Then settle to player colour
- 4-6 frame animation
- Apply to all claims
```

**What the Learner Sees:**
Cells don't just snap to colour. Brief flash animation. More satisfying.

---

### Unit 20: Title Screen Animation

**Learning Objectives:**
- Animate title screen
- Colour cycling effects
- Visual interest
- Professional presentation

**Concepts Introduced:**
- Title animation
- Colour cycling
- Animation loops
- First impression

**Code Written:**
```
- Title text colour cycles
- Background colour shifts
- Pulsing menu cursor
- Animation loop
```

**What the Learner Sees:**
Title screen moves and breathes. Looks professional. Good first impression.

---

### Unit 21: Title Music

**Learning Objectives:**
- Create simple music loop
- Play on title screen
- Stop on game start
- Set the mood

**Concepts Introduced:**
- Music on beeper
- Note sequences
- Loop structure
- Music data format

**Code Written:**
```
- Simple melody (8-16 notes)
- Loop continuously
- Stop on key press
- Musical identity
```

**What the Learner Sees:**
Title screen has music. Creates atmosphere. Feels like a proper game.

---

### Unit 22: Options Menu

**Learning Objectives:**
- Create options screen
- Toggle settings
- Board size option
- Sound on/off

**Concepts Introduced:**
- Menu navigation
- Toggle UI
- Settings storage
- User preferences

**Code Written:**
```
- Options menu layout
- Sound: On/Off
- Board size: 6×6 or 8×8
- Return to title
```

**What the Learner Sees:**
Options menu with settings. Can change board size. Can mute sounds.

---

### Unit 23: Board Size Variation

**Learning Objectives:**
- Implement 6×6 board option
- Adjust drawing for size
- Adjust logic for size
- Quicker games

**Concepts Introduced:**
- Variable board size
- Parameterised drawing
- Adjusted calculations
- Game variants

**Code Written:**
```
- board_size variable (6 or 8)
- Adjust board drawing
- Adjust boundary checks
- Adjust win detection (36 vs 64)
```

**What the Learner Sees:**
6×6 option for quicker games. Works correctly. Different strategic feel.

---

### Unit 24: Move Timer (Optional)

**Learning Objectives:**
- Add optional time limit
- Timer display
- Auto-move on timeout
- Faster-paced games

**Concepts Introduced:**
- Frame counting for timer
- Timer display
- Timeout handling
- Optional features

**Code Written:**
```
- move_timer: counts down
- Display remaining seconds
- Timeout: random valid move
- Enable/disable in options
```

**What the Learner Sees:**
Optional timed mode. Timer counts down. Forces quick decisions.

---

### Unit 25: Statistics Tracking

**Learning Objectives:**
- Track session statistics
- Wins/losses/draws
- Best win margin
- Stats display

**Concepts Introduced:**
- Session data
- Statistics calculation
- Stats screen
- Progress tracking

**Code Written:**
```
- wins, losses, draws counters
- best_margin tracking
- Stats screen from menu
- Reset option
```

**What the Learner Sees:**
Statistics screen shows record. Tracks performance across games.

---

### Unit 26: Victory Effects

**Learning Objectives:**
- Elaborate win celebration
- Multi-stage effect
- Audio-visual combination
- Memorable moment

**Concepts Introduced:**
- Effect sequencing
- Combined feedback
- Celebration design
- Emotional payoff

**Code Written:**
```
- Flash sequence
- Winner colour flood
- Jingle synchronised
- Build-up effect
```

**What the Learner Sees:**
Winning is celebrated dramatically. Screen effects. Music plays. Satisfying victory.

---

### Unit 27: Screen Transitions

**Learning Objectives:**
- Smooth state transitions
- Wipe effects
- Visual continuity
- Professional feel

**Concepts Introduced:**
- Transition effects
- Screen wiping
- Effect timing
- Polish through transitions

**Code Written:**
```
- Wipe effect between screens
- Attribute cascade
- Consistent style
- Clean transitions
```

**What the Learner Sees:**
Screens don't just cut. Smooth transitions. Professional presentation.

---

### Unit 28: Practice Mode

**Learning Objectives:**
- Undo last move
- Learning aid
- Two-player only
- Practice without commitment

**Concepts Introduced:**
- State history
- Undo mechanism
- Mode-specific features
- Learning support

**Code Written:**
```
- Store previous state
- Undo key (U)
- Only in two-player practice
- Decrement move counter
```

**What the Learner Sees:**
Practice mode with undo. Learn from mistakes. Experiment freely.

---

### Unit 29: Control Options

**Learning Objectives:**
- Configurable controls
- Multiple key schemes
- Cursor keys option
- Accessibility

**Concepts Introduced:**
- Key binding
- Control schemes
- Input configuration
- User preference

**Code Written:**
```
- Control scheme selection
- QAOP or cursor keys
- Display current scheme
- Save preference
```

**What the Learner Sees:**
Choose control scheme. QAOP or cursor keys. Preference remembered.

---

### Unit 30: Help Screen

**Learning Objectives:**
- Display game rules
- Show controls
- How to play
- User guidance

**Concepts Introduced:**
- Text display
- Help content
- Instruction writing
- Onboarding

**Code Written:**
```
- Help screen layout
- Game rules text
- Control diagram
- Return to menu
```

**What the Learner Sees:**
Help screen explains rules and controls. New players can learn the game.

---

### Unit 31: Attract Mode

**Learning Objectives:**
- Auto-play demo
- AI vs AI game
- Return on input
- Shop window feature

**Concepts Introduced:**
- Demo playback
- AI vs AI mode
- Attract timing
- Feature showcase

**Code Written:**
```
- AI vs AI demonstration
- Trigger after idle timeout
- Any key returns to title
- Show gameplay
```

**What the Learner Sees:**
Leave game idle - it plays itself. Shows off gameplay. Any key returns.

---

### Unit 32: Phase 2 Complete

**Learning Objectives:**
- Integration testing
- All features verified
- Polish pass
- Phase completion

**Concepts Introduced:**
- Feature integration
- Testing methodology
- Quality verification
- Milestone

**Code Written:**
```
- Test all features together
- Fix integration issues
- Final polish
- Document known issues
```

**What the Learner Sees:**
Complete game with all Phase 2 features. Custom graphics, animations, options, variations. Ready for Phase 3.

**Phase 2 Checkpoint:**
The game now has custom graphics, animations, music, options, and game variations. It looks and sounds like a commercial product.

---

## Phase 3: Polish (Units 33-48)

*Goal: Professional presentation and advanced features.*

---

### Unit 33: Enhanced Title Screen

**Learning Objectives:**
- Large logo design
- Visual impact
- Menu refinement
- Brand identity

**Concepts Introduced:**
- Logo design with attributes
- Visual hierarchy
- Screen composition
- First impression

**Code Written:**
```
- "INK WAR" large logo
- Colour scheme
- Menu layout refined
- Credit text
```

**What the Learner Sees:**
Professional title screen with large colourful logo. Commercial quality.

---

### Unit 34: High Score Table

**Learning Objectives:**
- Track high scores
- Name entry
- Display leaderboard
- Persistence goal

**Concepts Introduced:**
- Score storage
- Name entry UI
- Sorting
- Achievement display

**Code Written:**
```
- high_scores array (10 entries)
- Name entry (3 letters)
- Insert in sorted position
- Display formatted table
```

**What the Learner Sees:**
High score table. Name entry for new records. Competition motivation.

---

### Unit 35: Pause Functionality

**Learning Objectives:**
- Mid-game pause
- Pause overlay
- Resume cleanly
- Professional feature

**Concepts Introduced:**
- Pause state
- State preservation
- Overlay display
- Resume handling

**Code Written:**
```
- P key pauses
- "PAUSED" overlay
- Game state frozen
- P again resumes
```

**What the Learner Sees:**
Press P to pause. Game freezes with overlay. P to resume.

---

### Unit 36: AI Speed Options

**Learning Objectives:**
- Adjustable AI think time
- Instant vs deliberate
- Player preference
- Pacing control

**Concepts Introduced:**
- Think time parameter
- Pacing options
- User preference
- Gameplay feel

**Code Written:**
```
- AI speed: Fast/Normal/Slow
- Adjust delay before AI moves
- Option in settings
- Apply per game
```

**What the Learner Sees:**
Choose AI thinking speed. Fast for quick games. Slow for tension.

---

### Unit 37: Cell Patterns

**Learning Objectives:**
- Pre-blocked cells
- Obstacle patterns
- Level variety
- Content expansion

**Concepts Introduced:**
- Obstacle cells
- Pattern data
- Level selection
- Game variants

**Code Written:**
```
- Blocked cells (neither can claim)
- Preset patterns
- Pattern selection
- Visual distinction
```

**What the Learner Sees:**
Board layouts with obstacles. More variety. Strategic depth.

---

### Unit 38: Tournament Mode

**Learning Objectives:**
- Best of N matches
- Match tracking
- Tournament winner
- Extended play

**Concepts Introduced:**
- Match series
- Progress tracking
- Victory conditions
- Extended sessions

**Code Written:**
```
- Best of 3/5/7
- Track match scores
- Tournament winner screen
- Match counter display
```

**What the Learner Sees:**
Tournament mode for extended competition. Track match progress.

---

### Unit 39: Campaign Mode

**Learning Objectives:**
- Progressive AI opponents
- Unlock system
- Increasing difficulty
- Sense of progression

**Concepts Introduced:**
- Progression design
- Unlock mechanics
- Challenge curve
- Player journey

**Code Written:**
```
- Series of AI levels
- Each harder than last
- Unlock next on victory
- Campaign complete screen
```

**What the Learner Sees:**
Campaign: beat progressively harder AI. Unlock opponents. Achievement.

---

### Unit 40: Board Themes

**Learning Objectives:**
- Visual themes for boards
- Colour schemes
- Themed characters
- Visual variety

**Concepts Introduced:**
- Theme system
- Colour palettes
- Asset swapping
- Visual freshness

**Code Written:**
```
- Theme selection
- Different colour schemes
- Theme-specific characters
- Apply to gameplay
```

**What the Learner Sees:**
Choose board themes. Different colour schemes. Visual variety.

---

### Unit 41: AI Personalities

**Learning Objectives:**
- Different AI styles
- Aggressive vs defensive
- Named opponents
- Character variety

**Concepts Introduced:**
- AI personality
- Strategy weights
- Character design
- Opponent variety

**Code Written:**
```
- Aggressive AI (offensive focus)
- Defensive AI (blocking focus)
- Balanced AI (current)
- Random or selectable
```

**What the Learner Sees:**
Different AI opponents play differently. Named characters. More variety.

---

### Unit 42: Tutorial Mode

**Learning Objectives:**
- Teach new players
- Step-by-step guidance
- Interactive learning
- Onboarding

**Concepts Introduced:**
- Tutorial design
- Step progression
- Guidance text
- Learning flow

**Code Written:**
```
- Tutorial sequence
- Highlighted instructions
- Forced moves for learning
- Completion detection
```

**What the Learner Sees:**
Tutorial teaches the game step by step. New players learn easily.

---

### Unit 43: Replay Viewer

**Learning Objectives:**
- Record game moves
- Playback recording
- Review games
- Learning tool

**Concepts Introduced:**
- Move recording
- Playback system
- State reconstruction
- Analysis tool

**Code Written:**
```
- Record all moves
- Playback mode
- Step forward/back
- Speed control
```

**What the Learner Sees:**
Review completed games. Step through moves. Learn from games.

---

### Unit 44: Sound Test

**Learning Objectives:**
- Preview all sounds
- Audio catalogue
- Testing feature
- Development aid

**Concepts Introduced:**
- Sound preview
- Audio catalogue
- Test mode
- Quality verification

**Code Written:**
```
- Sound test screen
- List all sounds
- Play on selection
- Return to options
```

**What the Learner Sees:**
Sound test plays all effects and jingles. Preview audio.

---

### Unit 45: Credits Screen

**Learning Objectives:**
- Acknowledge creation
- Professional credits
- Learner's name
- Completion reward

**Concepts Introduced:**
- Credits display
- Attribution
- Closure
- Recognition

**Code Written:**
```
- Credits screen
- Game by: [learner]
- Tools used
- Return to title
```

**What the Learner Sees:**
Credits screen with their name. They made this game.

---

### Unit 46: Loading Screen

**Learning Objectives:**
- First impression
- Loading display
- Set expectations
- Professional start

**Concepts Introduced:**
- Loading experience
- First impression
- Branding
- Presentation

**Code Written:**
```
- Loading screen image
- Title/logo display
- Brief delay or progress
- Transition to title
```

**What the Learner Sees:**
Game loads with proper loading screen. Professional presentation.

---

### Unit 47: Final Polish Pass

**Learning Objectives:**
- Review everything
- Fix inconsistencies
- Tighten timing
- Quality bar

**Concepts Introduced:**
- Polish methodology
- Detail attention
- Final review
- Quality standard

**Code Written:**
```
- Visual alignment fixes
- Timing adjustments
- Colour consistency
- Bug fixes
```

**What the Learner Sees:**
Everything slightly better. More consistent. More polished.

---

### Unit 48: Phase 3 Complete

**Learning Objectives:**
- Full verification
- All features working
- Quality sign-off
- Ready for Phase 4

**Concepts Introduced:**
- Release candidacy
- Verification
- Quality gate
- Milestone

**Code Written:**
```
- Complete playthrough
- All modes tested
- All features verified
- Document status
```

**What the Learner Sees:**
Complete, polished game. All features working. Professional quality.

**Phase 3 Checkpoint:**
The game has tournament mode, campaign mode, themes, AI personalities, tutorial, and full polish. Commercial presentation.

---

## Phase 4: Mastery (Units 49-64)

*Goal: Commercial quality and distribution.*

---

### Unit 49: Code Review

**Learning Objectives:**
- Review codebase
- Document structure
- Identify improvements
- Prepare for optimisation

**Concepts Introduced:**
- Code review
- Documentation
- Technical debt
- Architecture analysis

**Code Written:**
```
- Full code review
- Add comments
- Document memory map
- Note improvements
```

**What the Learner Sees:**
No visible change. Cleaner, documented code.

---

### Unit 50: Memory Optimisation

**Learning Objectives:**
- Reduce memory usage
- Remove waste
- Efficient data
- RAM budget

**Concepts Introduced:**
- Memory profiling
- Data compression
- Dead code removal
- Efficiency

**Code Written:**
```
- Remove unused code
- Compress data tables
- Optimise variables
- Document savings
```

**What the Learner Sees:**
Same game, smaller. More efficient.

---

### Unit 51: Performance Optimisation

**Learning Objectives:**
- Speed up code
- Optimise hot paths
- Smooth performance
- Professional quality

**Concepts Introduced:**
- Profiling
- Cycle counting
- Optimisation techniques
- Performance budget

**Code Written:**
```
- Identify slow routines
- Optimise critical paths
- Verify frame rate
- Document performance
```

**What the Learner Sees:**
Smoother performance. More responsive.

---

### Unit 52: Advanced AI - Look-Ahead

**Learning Objectives:**
- Simple minimax
- One-move look-ahead
- Stronger opponent
- AI mastery

**Concepts Introduced:**
- Minimax concept
- Evaluation function
- Game tree
- Advanced AI

**Code Written:**
```
- Simple minimax (depth 1)
- Evaluate positions
- Pick best outcome
- For Hard mode
```

**What the Learner Sees:**
Hard AI is noticeably stronger. Thinks ahead.

---

### Unit 53: AI Balancing

**Learning Objectives:**
- Tune all AI levels
- Test balance
- Fair challenge
- Quality AI

**Concepts Introduced:**
- Balance testing
- Weight tuning
- Difficulty curve
- Player experience

**Code Written:**
```
- Test all difficulties
- Adjust weights
- Verify win rates
- Document balance
```

**What the Learner Sees:**
All AI levels feel right. Fair but challenging.

---

### Unit 54: Two-Player Polish

**Learning Objectives:**
- Enhance two-player
- Turn indicators
- Player identification
- Social play

**Concepts Introduced:**
- Multiplayer UX
- Player distinction
- Turn clarity
- Social gaming

**Code Written:**
```
- Enhanced turn display
- Player labels
- Better visual separation
- Clearer feedback
```

**What the Learner Sees:**
Two-player mode feels better. Clearer turns. Better experience.

---

### Unit 55: Network Placeholder

**Learning Objectives:**
- Placeholder for future
- System design
- Extensibility
- Planning ahead

**Concepts Introduced:**
- Future-proofing
- System design
- Placeholder code
- Extensibility

**Code Written:**
```
- Input abstraction
- Turn state management
- Placeholder comments
- Clean interfaces
```

**What the Learner Sees:**
No visible change. Code ready for future network play.

---

### Unit 56: Accessibility Review

**Learning Objectives:**
- Check accessibility
- Colour considerations
- Control alternatives
- Inclusive design

**Concepts Introduced:**
- Accessibility
- Colour blind modes
- Alternative inputs
- Inclusive gaming

**Code Written:**
```
- Review colour choices
- Symbol alternatives
- Control options
- Document accessibility
```

**What the Learner Sees:**
Game works for more players. Accessible design.

---

### Unit 57: Bug Hunt

**Learning Objectives:**
- Systematic testing
- Edge cases
- Fix issues
- Quality assurance

**Concepts Introduced:**
- Bug hunting
- Edge case testing
- Defensive coding
- QA process

**Code Written:**
```
- Test all paths
- Fix edge cases
- Add defensive checks
- Document fixes
```

**What the Learner Sees:**
No new bugs. Stable game.

---

### Unit 58: External Testing

**Learning Objectives:**
- Fresh perspectives
- External feedback
- Final adjustments
- User testing

**Concepts Introduced:**
- User testing
- Feedback collection
- Iteration
- External validation

**Code Written:**
```
- Collect feedback
- Make adjustments
- Final tweaks
- Verify improvements
```

**What the Learner Sees:**
Improvements from feedback. Better experience.

---

### Unit 59: Documentation

**Learning Objectives:**
- Write instructions
- Create documentation
- Help text
- User guidance

**Concepts Introduced:**
- Documentation writing
- Instruction design
- User guidance
- Release materials

**Code Written:**
```
- Write instructions
- Quick reference
- Complete documentation
- In-game help updates
```

**What the Learner Sees:**
Complete documentation. Clear instructions.

---

### Unit 60: Feature Freeze

**Learning Objectives:**
- Lock features
- Final testing
- Release preparation
- Stability focus

**Concepts Introduced:**
- Feature freeze
- Release candidate
- Stability testing
- Final verification

**Code Written:**
```
- Lock all features
- Final test pass
- Fix only bugs
- Declare RC
```

**What the Learner Sees:**
Final version. Ready for release.

---

### Unit 61: TAP File Creation

**Learning Objectives:**
- Create TAP file
- Tape distribution
- Standard format
- Real hardware

**Concepts Introduced:**
- TAP format
- Tape distribution
- Loading headers
- Standard format

**Code Written:**
```
- Create TAP file
- Verify loading
- Test on emulator
- Document format
```

**What the Learner Sees:**
Loadable TAP file. Real distribution format.

---

### Unit 62: TZX with Loading Screen

**Learning Objectives:**
- Create TZX file
- Add loading screen
- Professional loading
- Enhanced format

**Concepts Introduced:**
- TZX format
- Loading screens
- Enhanced distribution
- Professional packaging

**Code Written:**
```
- Design loading screen
- Create TZX file
- Include loading screen
- Verify loading
```

**What the Learner Sees:**
Loading screen during load. Professional presentation.

---

### Unit 63: Final Playtest

**Learning Objectives:**
- Complete playthrough
- Final verification
- Release readiness
- Sign-off

**Concepts Introduced:**
- Release testing
- Final verification
- Quality gate
- Release readiness

**Code Written:**
```
- Complete playthrough
- All modes tested
- All features verified
- Release approved
```

**What the Learner Sees:**
Final, verified game. Ready for release.

---

### Unit 64: Distribution

**Learning Objectives:**
- Package for release
- Create distribution
- Archive source
- Release!

**Concepts Introduced:**
- Distribution packaging
- Release process
- Archival
- Project completion

**Code Written:**
```
- Final TAP/TZX files
- Documentation package
- Source archive
- Release!
```

**What the Learner Sees:**
Complete distribution package. Ready to share. A finished game.

**Phase 4 Checkpoint:**
The game is complete. Optimised, polished, tested, and packaged for distribution. Commercial quality. The learner has built a real ZX Spectrum game.

---

## Skills Mastery Summary

By completing all 64 units, learners have demonstrated mastery of:

### ZX Spectrum Display
- Screen memory organisation
- Attribute system (INK, PAPER, BRIGHT, FLASH)
- Custom character sets
- Screen composition

### Z80 Assembly
- Registers and addressing modes
- Arithmetic and logic operations
- Control flow (jumps, calls, loops)
- Memory management
- Keyboard input

### Game Development
- Game loop structure
- State machine patterns
- Input handling and validation
- Score and statistics
- AI opponent design

### Professional Skills
- Code organisation
- Testing and debugging
- Polish and game feel
- Distribution packaging

---

## Comparison: 8 Units vs 64 Units

| Aspect | 8-Unit Version | 64-Unit Version |
|--------|----------------|-----------------|
| Gameplay | Two-player only | AI + Two-player |
| AI | None | Three difficulty levels + personalities |
| Sound | None | Full SFX + music |
| Visuals | Basic | Custom graphics, animated |
| Options | None | Board sizes, themes, controls |
| Modes | Single | Tournament, Campaign, Practice |
| Save | None | High scores, statistics |
| Distribution | PRG file | TAP/TZX with loading screen |
| Commercial viable? | No | Yes |
| Time investment | 8-16 hours | 64-128 hours |

---

## Version History

- **3.0 (2026-01-12):** Complete restructure following "scaffold first, explain later" approach. Interactive from Unit 1 (board + moving cursor). Core gameplay by Unit 2. Theory (Unit 3) follows experience. AI by Unit 16.
- **2.0 (2026-01-09):** Previous restructure (playable two-player by Unit 16, AI in Phase 2).
- **1.0 (2025-xx-xx):** Original outline (display theory first, interactivity at Unit 5).
