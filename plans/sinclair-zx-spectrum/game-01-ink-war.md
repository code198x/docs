# Ink War: 64-Unit Outline

**Game:** ZX Spectrum Game 1: Ink War
**Units:** 64
**Concept:** Territory control game - two players take turns claiming 8×8 attribute cells. Control the majority to win.

**Commercial Quality Target:** A game that could have sold for £7.99 on cassette in 1984. Simple, addictive, polished.

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

## Phase 1: Foundation (Units 1-16)

*Goal: A working two-player game. Playable from start to finish with a friend.*

*By the end of this phase, the learner has built a complete game. Two humans can play Ink War, taking turns at the keyboard. It's simple but fully functional - claim cells, track score, detect winner.*

---

### Unit 1: The Spectrum's Display

**Learning Objectives:**
- Understand the BASIC stub that launches machine code
- Know where screen memory lives ($4000-$57FF)
- Know where attribute memory lives ($5800-$5AFF)
- Write a working assembly program that runs on the Spectrum
- See colour on screen immediately

**Concepts Introduced:**
- Memory-mapped display
- Screen memory (bitmap) vs attribute memory (colour)
- The ORG directive
- BASIC loader (RANDOMIZE USR 32768)

**Code Written:**
```
- BASIC loader stub
- Set border colour via OUT
- Fill a few attribute cells with colour
- Infinite loop to keep program running
```

**What the Learner Sees:**
Border changes colour. A few coloured blocks appear on screen. First contact with the Spectrum display system. The program runs from their own code.

**Technical Details:**
- Border colour: OUT ($FE), A
- Attribute memory: $5800-$5AFF (768 bytes)
- Screen memory: $4000-$57FF (6144 bytes)
- Each attribute byte: one 8×8 cell

---

### Unit 2: The Attribute Grid

**Learning Objectives:**
- Understand the 32×24 attribute cell grid
- Calculate attribute address from row and column
- Decode attribute byte structure (INK, PAPER, BRIGHT, FLASH)
- Fill regions of the screen with colour

**Concepts Introduced:**
- Attribute byte format: FBPPPIII
- Address calculation: $5800 + (row × 32) + column
- BRIGHT and FLASH bits
- The 8 Spectrum colours

**Code Written:**
```
- Clear attribute memory to single colour
- Fill specific rows with different colours
- Create a checkerboard pattern
- Demonstrate BRIGHT effect
```

**What the Learner Sees:**
Colourful patterns fill the screen. Checkerboard shows alternating colours. BRIGHT colours visibly differ from normal. The attribute system makes sense.

**Technical Details:**
- Attribute byte: bit 7=FLASH, bit 6=BRIGHT, bits 5-3=PAPER, bits 2-0=INK
- Colours: 0=black, 1=blue, 2=red, 3=magenta, 4=green, 5=cyan, 6=yellow, 7=white
- 32 columns × 24 rows = 768 cells

---

### Unit 3: Drawing the Board

**Learning Objectives:**
- Plan game board layout on screen
- Calculate board position (centred)
- Draw border around the board
- Fill board with "empty" colour
- Use constants for maintainability

**Concepts Introduced:**
- EQU for constants
- Nested loops (row/column)
- Board positioning arithmetic
- Clear screen routine (LDIR)

**Code Written:**
```
- Define board constants (BOARD_TOP, BOARD_LEFT, BOARD_SIZE)
- Clear screen routine
- Draw 10×10 border (black cells around 8×8 board)
- Fill 8×8 board area with white (empty)
- Set black border colour
```

**What the Learner Sees:**
A centred 8×8 white game board with black border, on a black background. The game board is clearly visible. This is the play area.

**Technical Details:**
- Board: 8×8 cells
- Position: row 8, column 12 (centred on 32×24 screen)
- Border: row 7-16, column 11-20
- Empty cell colour: white paper (%00111000)
- Border colour: black (%00000000)

---

### Unit 4: Player Colours

**Learning Objectives:**
- Define player colour constants
- Write a routine to claim a cell
- Understand cell state (empty, player 1, player 2)
- Demonstrate the visual goal of the game

**Concepts Introduced:**
- Game state in memory (who owns each cell)
- Colour as game state indicator
- Subroutine for cell colouring
- Board array concept

**Code Written:**
```
- Define PLAYER1_ATTR (bright red) and PLAYER2_ATTR (bright blue)
- Subroutine: set_cell(row, col, colour)
- Manually place some red and blue cells
- Create snapshot of "game in progress"
```

**What the Learner Sees:**
The board shows some red cells (Player 1 territory) and some blue cells (Player 2 territory) with white empty cells remaining. A visual preview of what gameplay will look like.

**Technical Details:**
- Player 1: bright red paper = %01010000
- Player 2: bright blue paper = %01001000
- Empty: white paper = %00111000
- Cell state array: 64 bytes, values 0/1/2

---

### Unit 5: Keyboard Input

**Learning Objectives:**
- Understand the Spectrum keyboard matrix
- Read specific keys (Q, A, O, P, Space)
- Detect key press vs key held
- Provide visual feedback for input

**Concepts Introduced:**
- Keyboard port ($FE)
- Half-row addressing
- Key debouncing (previous state comparison)
- Edge detection (newly pressed)

**Code Written:**
```
- Keyboard reading routine
- Check Q (up), A (down), O (left), P (right), Space (action)
- Store previous key state
- Detect new key presses only
- Flash border on key press (visual feedback)
```

**What the Learner Sees:**
Pressing Q/A/O/P/Space causes the border to flash different colours. The program responds to specific keys. Input is debounced - holding a key doesn't repeat rapidly.

**Technical Details:**
- Port $FE with high byte selecting half-row
- Q: row $FB bit 0, A: row $FD bit 0
- O: row $DF bit 1, P: row $DF bit 0
- Space: row $7F, bit 0
- Debounce: compare current state with previous frame

---

### Unit 6: The Cursor

**Learning Objectives:**
- Track cursor position in memory
- Display cursor on the board
- Move cursor with keyboard input
- Constrain cursor to board boundaries

**Concepts Introduced:**
- Cursor state (row, column variables)
- Cursor display (different attribute or flashing)
- Boundary checking
- Game loop with input processing

**Code Written:**
```
- cursor_row, cursor_col variables
- draw_cursor: highlight current cell
- erase_cursor: restore cell's actual colour
- move_cursor: update position based on input
- Boundary checks (0-7 range)
- Main loop: erase, read input, move, draw
```

**What the Learner Sees:**
A highlighted cell (the cursor) on the board. Pressing Q/A/O/P moves it around. The cursor can't move outside the board. Smooth, responsive movement.

**Technical Details:**
- Cursor display: use FLASH bit or inverted colours
- Cursor position: 0-7 for row, 0-7 for column
- Movement: check boundaries before updating position
- Main loop runs at frame rate (HALT synchronisation)

---

### Unit 7: Claiming Cells

**Learning Objectives:**
- Detect action key press (Space)
- Check if current cell is empty
- Claim cell for current player
- Update visual display

**Concepts Introduced:**
- Cell state array (tracking ownership)
- Claim validation (empty check)
- State change (memory + display)
- Current player variable

**Code Written:**
```
- board_state: 64-byte array (0=empty, 1=P1, 2=P2)
- current_player: 1 or 2
- claim_cell: check empty, set state, update display
- Play feedback sound on claim
- Error feedback if cell occupied
```

**What the Learner Sees:**
Pressing Space on an empty cell turns it to the current player's colour (red or blue). Pressing Space on an occupied cell does nothing (or plays error sound). Cells stay claimed.

**Technical Details:**
- Board state array: 64 bytes at fixed address
- Index calculation: row × 8 + column
- State values: 0=empty, 1=player 1, 2=player 2
- Visual update: write player's attribute byte

---

### Unit 8: Turn System

**Learning Objectives:**
- Alternate between players after valid claim
- Display whose turn it is
- Change cursor colour to match current player
- Handle turn transitions cleanly

**Concepts Introduced:**
- Turn state management
- Player indicator display
- XOR for toggling (1↔2)
- UI updates on state change

**Code Written:**
```
- Switch player after successful claim (XOR or subtract)
- Draw turn indicator (coloured bar or text area)
- Cursor colour matches current player
- Update indicator on turn change
```

**What the Learner Sees:**
After claiming a cell, the turn indicator changes and cursor becomes the other player's colour. Red claims, then blue's turn, then red's turn. The game alternates properly.

**Technical Details:**
- Toggle: current_player = 3 - current_player (swaps 1↔2)
- Turn indicator: coloured cells at top of screen
- Cursor colour: use current player's attribute
- Both players use same keyboard (hot-seat)

---

### Unit 9: Move Validation

**Learning Objectives:**
- Validate moves before allowing them
- Provide clear feedback for invalid moves
- Only switch turns on valid moves
- Handle edge cases robustly

**Concepts Introduced:**
- Input validation pattern
- Error feedback (visual and audio)
- Defensive programming
- User experience for invalid actions

**Code Written:**
```
- validate_move: check cell is empty
- Invalid move: play error beep, flash border red
- Valid move: play success beep, proceed with claim
- Don't switch turns on invalid move
```

**What the Learner Sees:**
Trying to claim an occupied cell plays a harsh buzz and briefly flashes the border. The turn doesn't change. Only valid moves progress the game. Clear feedback for mistakes.

**Technical Details:**
- Validation: check board_state[index] == 0
- Error sound: short noise burst via beeper
- Success sound: pleasant tone
- Border flash: brief colour change (2-3 frames)

---

### Unit 10: Score Display

**Learning Objectives:**
- Count cells owned by each player
- Display scores on screen
- Update scores after each move
- Format numbers for display

**Concepts Introduced:**
- Counting algorithm (iterate board)
- Number to character conversion
- Efficient score update (increment vs recount)
- Score display area layout

**Code Written:**
```
- count_cells: iterate board, count 1s and 2s
- display_score: show "RED: nn  BLUE: nn"
- Update after each claim
- Position scores at top of screen
```

**What the Learner Sees:**
Score display at top shows "RED: 5 BLUE: 3" (or similar). Numbers update immediately when cells are claimed. Players can see who's winning.

**Technical Details:**
- Score positions: top row of screen
- Number display: convert to ASCII (add $30)
- Two-digit display: divide by 10 for tens digit
- Maximum score: 64 (fits in two digits)

---

### Unit 11: Detecting Game End

**Learning Objectives:**
- Detect when the board is full
- Transition to end-of-game state
- Stop accepting further moves
- Count total claimed cells

**Concepts Introduced:**
- Game state (playing vs ended)
- End condition detection
- State machine basics
- Total cell counting

**Code Written:**
```
- Check if moves_made == 64 (or count empty cells == 0)
- game_over flag
- When game_over: stop processing moves
- Transition to results display
```

**What the Learner Sees:**
After the 64th cell is claimed, the game stops accepting input. No more moves possible. The board is completely filled with red and blue.

**Technical Details:**
- Track moves_made counter (increment on each claim)
- Or count empty cells after each move
- Game over when moves_made == 64
- Set game_state to GAME_OVER

---

### Unit 12: Determining the Winner

**Learning Objectives:**
- Compare final scores
- Determine winner (or draw)
- Display winner announcement
- Celebrate victory visually

**Concepts Introduced:**
- Score comparison logic
- Three outcomes (P1 wins, P2 wins, draw)
- Victory display
- Visual celebration effect

**Code Written:**
```
- Compare player 1 score vs player 2 score
- Display "RED WINS!", "BLUE WINS!", or "DRAW!"
- Flash screen in winner's colour
- Hold on results
```

**What the Learner Sees:**
"RED WINS!" (or "BLUE WINS!" or "DRAW!") appears on screen. The border flashes the winner's colour. Clear indication of outcome.

**Technical Details:**
- Compare: if score1 > score2, P1 wins; if score2 > score1, P2 wins; else draw
- Message display: use screen memory or attributes
- Celebration: border colour cycling or flashing
- Hold: wait for key press before continuing

---

### Unit 13: Game States

**Learning Objectives:**
- Implement state machine (title, playing, results)
- Handle transitions between states
- Create simple title screen
- Structure code for multiple states

**Concepts Introduced:**
- Game state variable
- State machine pattern
- Dispatch based on state
- Initialisation per state

**Code Written:**
```
- game_state: TITLE, PLAYING, RESULTS
- Main loop dispatches to current state handler
- title_state: draw title, wait for key, → PLAYING
- playing_state: existing game logic
- results_state: show winner, wait for key, → TITLE
```

**What the Learner Sees:**
Game starts with title screen ("INK WAR - Press any key"). Key press starts game. After game ends, results show, then key press returns to title.

**Technical Details:**
- State values: 0=TITLE, 1=PLAYING, 2=RESULTS
- Dispatch: compare and jump to handler
- State init: reset variables when entering state
- Clean transitions between states

---

### Unit 14: Results Screen

**Learning Objectives:**
- Create proper results display
- Show final scores clearly
- Display winner prominently
- Calculate and show statistics

**Concepts Introduced:**
- Results screen layout
- Statistics (win margin, percentage)
- Screen composition
- Polish for end state

**Code Written:**
```
- Clear screen for results
- Large "RED WINS!" or "BLUE WINS!" display
- Final scores: "RED: 35  BLUE: 29"
- Win margin: "Won by 6 cells"
- Territory percentage (optional)
```

**What the Learner Sees:**
A proper results screen, not just overlaid text. Clear winner announcement, final scores, how much they won by. Looks like a finished game.

**Technical Details:**
- Clear screen before drawing results
- Centre text on screen
- Win margin: abs(score1 - score2)
- Percentage: (score × 100) / 64

---

### Unit 15: Play Again

**Learning Objectives:**
- Reset game state completely
- Return to title or restart game
- Clear board properly
- Handle game loop restart

**Concepts Introduced:**
- State reset
- Variable initialisation
- Clean restart
- Option: play again vs title

**Code Written:**
```
- reset_game: clear board_state array, reset scores
- Reset current_player to 1
- Reset cursor position
- From results: key press → TITLE (or PLAYING for quick rematch)
```

**What the Learner Sees:**
After results, press a key and the game restarts fresh. Board is empty, scores are zero, ready for another game. Can play indefinitely.

**Technical Details:**
- Zero the board_state array (64 bytes)
- Reset all game variables
- Redraw empty board
- Return to title or directly to playing

---

### Unit 16: Complete Two-Player Game

**Learning Objectives:**
- Polish the complete experience
- Fix any remaining issues
- Test full game flow
- Celebrate completion

**Concepts Introduced:**
- Integration testing
- Edge case handling
- Polish pass
- Completeness checklist

**Code Written:**
```
- Final bug fixes
- Timing adjustments
- Visual polish (consistent colours, aligned text)
- Verify all paths work
```

**What the Learner Sees:**
A complete, polished two-player game. Title → Play → Results → Title loop works perfectly. Hand the keyboard to a friend and play Ink War.

**Phase 1 Checkpoint:**
The learner has built a working game. Two humans can sit at the same keyboard and play Ink War competitively. It's simple but complete - exactly what Game 1 should deliver by Unit 16.

---

## Phase 2: Expansion (Units 17-32)

*Goal: Add AI opponent, sound effects, and enhanced gameplay options.*

*By the end of this phase, the game has a computer opponent with difficulty levels, sound effects, and gameplay options. It's a proper single-player experience.*

---

### Unit 17: AI Framework

**Learning Objectives:**
- Design AI decision structure
- Add game mode selection (vs Human / vs AI)
- Implement random cell selection (baseline AI)
- Replace Player 2 with AI when selected

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
```

**What the Learner Sees:**
Title screen offers "1 - Two Player" / "2 - vs Computer". Selecting vs Computer, the AI takes Player 2's turns automatically. It plays randomly but legally.

---

### Unit 18: Smarter AI - Adjacent Priority

**Learning Objectives:**
- AI prefers cells adjacent to own territory
- Build connected territory clusters
- Evaluate cell adjacency
- More strategic behaviour

**Concepts Introduced:**
- Cell adjacency checking
- Priority scoring
- Building territory
- AI personality through strategy

**Code Written:**
```
- check_adjacent: count friendly neighbours
- Score cells by adjacency
- Prefer cells with more friendly neighbours
- Fall back to random if no adjacent options
```

**What the Learner Sees:**
AI builds connected regions instead of scattered claims. Territory grows outward from existing cells. More intelligent behaviour.

---

### Unit 19: Defensive AI

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
AI doesn't just expand blindly - it blocks the player's expansion too. More competitive and challenging to beat.

---

### Unit 20: Corner and Edge Strategy

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
- Cell value table (corners=high, edges=medium, centre=low)
- Add position value to cell score
- Corners grabbed early
- Strategic opening moves
```

**What the Learner Sees:**
AI grabs corners early - good Othello/Reversi strategy. Edge cells prioritised. Feels like playing a real opponent.

---

### Unit 21: AI Difficulty Levels

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
- Hard: 100% strategic + look-ahead
- Difficulty selection on mode screen
```

**What the Learner Sees:**
Choose AI difficulty. Easy is beatable by beginners. Normal provides challenge. Hard requires good strategy to win.

---

### Unit 22: Beeper Basics

**Learning Objectives:**
- Understand the Spectrum beeper
- Generate tones of different pitches
- Create short sound effects
- Time sound generation

**Concepts Introduced:**
- Beeper port ($FE)
- Pitch as loop timing
- Duration as iterations
- Single-bit audio

**Code Written:**
```
- beep_tone: play note of given pitch/duration
- Click sound (very short beep)
- Rising tone, falling tone
- Test various pitches
```

**What the Learner Sees:**
Various beeps and tones play when testing. The Spectrum makes sound from code.

---

### Unit 23: Game Sound Effects

**Learning Objectives:**
- Create distinct sounds for game events
- Claim sound (positive feedback)
- Invalid move sound (negative feedback)
- Turn change sound

**Concepts Introduced:**
- Sound design for feedback
- Positive vs negative sounds
- Audio consistency
- Game feel through sound

**Code Written:**
```
- sound_claim: pleasant rising tone
- sound_invalid: harsh buzz
- sound_turn: subtle click
- Integrate into game events
```

**What the Learner Sees:**
Claims have satisfying bloop. Invalid moves have error buzz. Turn changes have subtle click. Game feels more alive.

---

### Unit 24: Victory Jingles

**Learning Objectives:**
- Create short musical phrases
- Victory jingle (celebratory)
- Defeat jingle (commiserating)
- Draw jingle (neutral)

**Concepts Introduced:**
- Musical phrases on beeper
- Emotional tone through music
- Multi-note sequences
- Note timing

**Code Written:**
```
- jingle_victory: ascending triumphant phrase
- jingle_defeat: descending sad phrase
- jingle_draw: neutral resolution
- Play appropriate jingle on results
```

**What the Learner Sees:**
Winning plays happy tune. Losing plays sad tune. Draw plays neutral tune. Audio matches emotional outcome.

---

### Unit 25: Title Music

**Learning Objectives:**
- Create simple looping music
- Music on title screen
- Interruptible by key press
- Set the mood

**Concepts Introduced:**
- Music loops
- Background music vs foreground action
- Music data format
- Simple sequencer

**Code Written:**
```
- Simple 8-16 bar melody
- Loop continuously on title
- Stop immediately on key press
- Musical identity for the game
```

**What the Learner Sees:**
Title screen has music playing. Creates atmosphere. Press key to start, music stops, game begins.

---

### Unit 26: Move Timer (Optional Mode)

**Learning Objectives:**
- Add optional time limit per turn
- Timer display countdown
- Auto-skip on timeout
- Faster-paced games

**Concepts Introduced:**
- Frame counting for timing
- Timer display
- Timeout handling
- Optional game modes

**Code Written:**
```
- move_timer: counts down from N seconds
- Display remaining time
- Timeout: random valid move or skip
- Option to enable/disable timer
```

**What the Learner Sees:**
Optional timed mode - timer counts down each turn. Adds urgency. Times out if too slow.

---

### Unit 27: Undo Move (Practice Mode)

**Learning Objectives:**
- Store previous board state
- Undo last move
- Practice mode only (not vs AI)
- Learning aid feature

**Concepts Introduced:**
- State history
- Undo mechanism
- Mode-specific features
- Learning assistance

**Code Written:**
```
- Store previous_board_state before each move
- Undo key restores previous state
- Only available in two-player practice
- Decrement move counter on undo
```

**What the Learner Sees:**
In practice mode, press U to undo last move. Learn from mistakes. Not available vs AI.

---

### Unit 28: Board Variations

**Learning Objectives:**
- Different board sizes (6×6, 8×8)
- Pre-blocked cells (obstacles)
- Starting positions variation
- Configuration options

**Concepts Introduced:**
- Configurable game parameters
- Board size as variable
- Obstacle cells
- Game variants

**Code Written:**
```
- board_size variable (6 or 8)
- Adjust drawing and logic for size
- Optional blocked cells (neither player can claim)
- Preset obstacle patterns
```

**What the Learner Sees:**
Options for 6×6 (quicker) or 8×8 (standard) boards. Optional obstacles create variety.

---

### Unit 29: Statistics Tracking

**Learning Objectives:**
- Track wins/losses/draws per session
- Display statistics screen
- Track best win margin
- Session statistics

**Concepts Introduced:**
- Persistent (session) data
- Statistics calculation
- Stats display screen
- Performance tracking

**Code Written:**
```
- wins, losses, draws counters
- best_margin tracking
- Stats screen from menu
- Reset stats option
```

**What the Learner Sees:**
Statistics screen shows session record: "Won: 5, Lost: 3, Draw: 1, Best win: 12 cells".

---

### Unit 30: Animation - Cell Claims

**Learning Objectives:**
- Animate cell colour change
- Smooth transition effect
- Visual feedback enhancement
- Polish through animation

**Concepts Introduced:**
- Frame-based animation
- Colour transitions
- Animation timing
- Visual polish

**Code Written:**
```
- Animate claim: flash white, then settle to colour
- Or: expand from centre effect using attributes
- Brief but noticeable
- Apply to all claims
```

**What the Learner Sees:**
Cells don't just snap to colour - brief flash or expansion animation. More satisfying claims.

---

### Unit 31: Animation - Cursor

**Learning Objectives:**
- Animate cursor visibility
- Smooth cursor movement (optional)
- Pulsing or flashing cursor
- Better visual focus

**Concepts Introduced:**
- Cursor animation states
- Visibility cycling
- Frame timing for animation
- Focus indication

**Code Written:**
```
- Cursor pulses (alternates highlight)
- Or: smooth colour transition
- Consistent animation timing
- Clear visual focus
```

**What the Learner Sees:**
Cursor pulses or flashes to draw attention. Easier to see where you are on the board.

---

### Unit 32: Phase 2 Complete

**Learning Objectives:**
- Integration testing
- Balance AI difficulty
- Polish all features
- Complete feature verification

**Concepts Introduced:**
- Feature integration
- Balance testing
- Quality assurance
- Phase completion

**Code Written:**
```
- Test all combinations
- Adjust AI balance if needed
- Fix integration issues
- Document known issues
```

**What the Learner Sees:**
Complete game with AI, sound, options, and polish. A proper single-player experience. Ready for Phase 3.

**Phase 2 Checkpoint:**
The game now has a competent AI opponent at multiple difficulty levels, sound effects and music, gameplay options, and visual polish. It's a complete single-player game.

---

## Phase 3: Polish (Units 33-48)

*Goal: Professional presentation and user experience.*

---

### Unit 33: Title Screen Design

**Learning Objectives:**
- Design visually appealing title
- Use attributes for logo/graphics
- Plan menu layout
- Establish visual identity

**Concepts Introduced:**
- Screen composition
- Logo design with attributes
- Colour scheme selection
- Visual hierarchy

**Code Written:**
```
- "INK WAR" logo using attributes
- Colour scheme (reds and blues)
- Menu option layout
- Version/credit text
```

**What the Learner Sees:**
Professional-looking title screen with large colourful logo. Clear menu options. Looks like a commercial game.

---

### Unit 34: Title Animation

**Learning Objectives:**
- Animate title elements
- Create visual interest
- Colour cycling effects
- Attract attention

**Concepts Introduced:**
- Frame-based animation
- Colour cycling
- Animation loops
- Visual polish

**Code Written:**
```
- Logo colour cycling
- Pulsing menu cursor
- Background animation
- Transition effects
```

**What the Learner Sees:**
Title screen moves and breathes. Logo shimmers, menu pulses. The game feels alive.

---

### Unit 35: Menu Navigation

**Learning Objectives:**
- Implement menu system
- Handle up/down selection
- Visual feedback for selection
- State transitions from menu

**Concepts Introduced:**
- Menu state management
- Cursor navigation
- Selection confirmation
- Menu hierarchies

**Code Written:**
```
- Menu cursor position
- Navigate with keys
- Confirm with Space/Enter
- Sub-menus for options
```

**What the Learner Sees:**
Navigate menus smoothly. Selection clearly visible. Sub-menus accessible. Professional feel.

---

### Unit 36: Attract Mode

**Learning Objectives:**
- Auto-play demonstration
- Showcase gameplay
- Return on input
- Cycle through features

**Concepts Introduced:**
- Demo playback
- AI vs AI mode
- Attract loop
- Marketing through gameplay

**Code Written:**
```
- AI vs AI game demo
- Cycle after timeout on title
- Any key returns to title
- Show different board states
```

**What the Learner Sees:**
Leave game idle and it plays itself. Shows off gameplay. Any key returns to menu. Shop window feature.

---

### Unit 37: Options Menu

**Learning Objectives:**
- Create options screen
- Toggle settings
- Display current values
- Return to main menu

**Concepts Introduced:**
- Settings storage
- Toggle UI pattern
- Options categories
- User preferences

**Code Written:**
```
- Options screen layout
- Toggle: Sound On/Off
- Toggle: Board Size
- Toggle: AI Difficulty
- Save settings in memory
```

**What the Learner Sees:**
Options menu with toggleable settings. Changes apply immediately. Preferences remembered during session.

---

### Unit 38: Control Configuration

**Learning Objectives:**
- Allow key remapping
- Display current controls
- Redefine keys option
- Support multiple schemes

**Concepts Introduced:**
- Key binding
- Input configuration
- Control schemes
- Accessibility

**Code Written:**
```
- Display current key bindings
- Redefine keys routine
- Default schemes (QAOP, cursor)
- Store custom bindings
```

**What the Learner Sees:**
View and change control keys. Multiple preset schemes. Custom key definition.

---

### Unit 39: Audio Options

**Learning Objectives:**
- Sound on/off toggle
- Music on/off toggle
- Sound test feature
- Audio preferences

**Concepts Introduced:**
- Audio flags
- Conditional sound playing
- Sound test mode
- User audio preferences

**Code Written:**
```
- sound_enabled flag
- music_enabled flag
- Check flags before playing
- Sound test: hear all effects
```

**What the Learner Sees:**
Turn sound/music on or off. Sound test plays all effects and jingles. Preferences respected.

---

### Unit 40: Help Screen

**Learning Objectives:**
- Display game rules
- Show controls
- How to play guide
- Return to menu

**Concepts Introduced:**
- Text display
- Scrolling text (if needed)
- Help content
- User guidance

**Code Written:**
```
- Help screen layout
- Game rules text
- Control diagram
- Objective explanation
```

**What the Learner Sees:**
Help screen explains rules and controls. New players can learn the game. Clear instructions.

---

### Unit 41: Custom Character Set

**Learning Objectives:**
- Design game-specific characters
- Load custom charset
- Better visual quality
- Consistent aesthetic

**Concepts Introduced:**
- Character memory
- Character design (8×8)
- Font replacement
- Visual identity

**Code Written:**
```
- Design custom characters for UI
- Arrows, borders, special symbols
- Load charset at startup
- Use throughout game
```

**What the Learner Sees:**
Game uses custom characters - nicer borders, better symbols. More polished appearance.

---

### Unit 42: Enhanced Board Graphics

**Learning Objectives:**
- Improve board appearance
- Cell detail using characters
- Border decorations
- Visual refinement

**Concepts Introduced:**
- Character graphics
- Screen composition
- Detail enhancement
- Polish through graphics

**Code Written:**
```
- Custom border characters
- Cell interior patterns (optional)
- Corner pieces
- Row/column markers
```

**What the Learner Sees:**
Board looks more finished. Decorative borders. Optional grid markings. Professional appearance.

---

### Unit 43: Victory Effects

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
- Particle-like effects
```

**What the Learner Sees:**
Winning is celebrated with elaborate effects. Screen flashes, colours flood, music plays. Satisfying victory.

---

### Unit 44: Screen Transitions

**Learning Objectives:**
- Smooth state transitions
- Wipe/fade effects
- Visual continuity
- Polish through transitions

**Concepts Introduced:**
- Transition effects
- Screen wiping
- Effect timing
- Professional feel

**Code Written:**
```
- Wipe: horizontal bar clears screen
- Or: attribute cascade effect
- Apply between states
- Consistent transition style
```

**What the Learner Sees:**
Screens don't just cut - they transition smoothly. Wipe effect between states. Professional presentation.

---

### Unit 45: High Score Table

**Learning Objectives:**
- Track high scores
- Name entry system
- Display leaderboard
- Persist during session

**Concepts Introduced:**
- Score storage
- Sorting/insertion
- Name entry UI
- Achievement display

**Code Written:**
```
- high_scores: array of scores + names
- Check if new high score
- Name entry (3 letters)
- Display table
```

**What the Learner Sees:**
High score table shows top scores with names. New high score prompts name entry. Leaderboard competition.

---

### Unit 46: Pause Functionality

**Learning Objectives:**
- Pause game mid-play
- Display pause state
- Resume cleanly
- Handle pause input

**Concepts Introduced:**
- Game pause state
- State preservation
- Pause overlay
- Resume handling

**Code Written:**
```
- Pause on P key
- Display "PAUSED"
- Freeze game state
- Resume on P again
```

**What the Learner Sees:**
Press P to pause - game freezes with overlay. Press P again to resume. Important feature for real play.

---

### Unit 47: Polish Pass

**Learning Objectives:**
- Review entire game
- Fix visual inconsistencies
- Tighten timing
- Final adjustments

**Concepts Introduced:**
- Polish methodology
- Detail attention
- Quality threshold
- Pre-release review

**Code Written:**
```
- Fix alignment issues
- Adjust colours for consistency
- Tighten input response
- Verify all text correct
```

**What the Learner Sees:**
Subtle improvements throughout. Everything more consistent and tight. The 90% to 100% jump.

---

### Unit 48: Phase 3 Complete

**Learning Objectives:**
- Full integration test
- Feature verification
- Quality sign-off
- Phase completion

**Concepts Introduced:**
- Release candidacy
- Feature completeness
- Quality bar
- Phase gates

**Code Written:**
```
- Complete playthrough
- All features verified
- Bug fixes
- Documentation updates
```

**What the Learner Sees:**
Complete, polished game. Professional presentation. Ready for final phase.

**Phase 3 Checkpoint:**
The game looks and sounds professional. Menus are polished, effects are satisfying, presentation is complete. It feels like a commercial product.

---

## Phase 4: Mastery (Units 49-64)

*Goal: Commercial quality and distribution.*

---

### Unit 49: Code Review

**Learning Objectives:**
- Review entire codebase
- Identify improvements
- Document architecture
- Prepare for optimisation

**Concepts Introduced:**
- Code review practices
- Technical debt
- Documentation
- Refactoring planning

**Code Written:**
```
- Add comments throughout
- Document memory map
- Note inefficiencies
- Plan optimisation targets
```

**What the Learner Sees:**
No visible change - cleaner code. Better organisation. Ready for optimisation.

---

### Unit 50: Memory Optimisation

**Learning Objectives:**
- Reduce memory usage
- Eliminate waste
- Compress data
- Free space for features

**Concepts Introduced:**
- Memory profiling
- Data compression
- Dead code removal
- Memory budgeting

**Code Written:**
```
- Remove unused code
- Compress look-up tables
- Optimise data structures
- Document savings
```

**What the Learner Sees:**
Same game, smaller size. More efficient. Professional optimisation.

---

### Unit 51: Performance Optimisation

**Learning Objectives:**
- Profile performance
- Speed up critical paths
- Optimise hot loops
- Maintain responsiveness

**Concepts Introduced:**
- Profiling techniques
- Cycle counting
- Loop optimisation
- Performance budgeting

**Code Written:**
```
- Identify slow routines
- Optimise board scanning
- Speed up display updates
- Verify frame rate
```

**What the Learner Sees:**
Game feels slightly smoother. More responsive. Professional performance.

---

### Unit 52: Timing Stability

**Learning Objectives:**
- Verify stable timing
- Handle worst cases
- Eliminate slowdown
- Rock-solid performance

**Concepts Introduced:**
- Worst-case analysis
- Timing verification
- Performance testing
- Stability assurance

**Code Written:**
```
- Test under load
- Verify all paths
- Fix any slowdown
- Document timing budget
```

**What the Learner Sees:**
Perfectly stable regardless of game state. No slowdown ever. Professional quality.

---

### Unit 53: Advanced AI - Look-Ahead

**Learning Objectives:**
- Implement simple minimax
- One-move look-ahead
- Better evaluation
- Stronger opponent

**Concepts Introduced:**
- Minimax algorithm
- Game tree concept
- Evaluation function
- Recursive thinking

**Code Written:**
```
- Simple minimax (depth 1)
- Evaluate resulting positions
- Pick best outcome
- Optional for Hard mode
```

**What the Learner Sees:**
Hard AI is noticeably stronger. Thinks ahead. Difficult to beat.

---

### Unit 54: AI Evaluation Tuning

**Learning Objectives:**
- Refine evaluation function
- Balance weights
- Test and adjust
- Optimal AI

**Concepts Introduced:**
- Weight tuning
- Testing methodology
- Balance iteration
- AI quality

**Code Written:**
```
- Adjust position values
- Tune adjacency weights
- Test against humans
- Fine-tune difficulty
```

**What the Learner Sees:**
AI plays better - feels more intelligent. Well-balanced challenge.

---

### Unit 55: AI Personalities

**Learning Objectives:**
- Multiple AI styles
- Aggressive vs defensive
- Random personality
- Variety in opponents

**Concepts Introduced:**
- AI personality
- Strategy variation
- Player preference
- Replayability

**Code Written:**
```
- Aggressive: maximise own territory
- Defensive: block opponent priority
- Balanced: current behaviour
- Random selection or player choice
```

**What the Learner Sees:**
Different AI opponents play differently. Choose style or random. More variety.

---

### Unit 56: AI Polish

**Learning Objectives:**
- Final AI testing
- Edge case handling
- Performance verification
- AI completion

**Concepts Introduced:**
- AI quality assurance
- Edge cases
- Final testing
- Completion criteria

**Code Written:**
```
- Test all difficulty levels
- Fix any issues
- Verify performance
- Document AI behaviour
```

**What the Learner Sees:**
AI is complete and polished. Reliable opponent at all levels.

---

### Unit 57: Tournament Mode

**Learning Objectives:**
- Best of N matches
- Match tracking
- Tournament winner
- Extended play

**Concepts Introduced:**
- Match series
- Progress tracking
- Victory conditions
- Extended game modes

**Code Written:**
```
- Tournament: best of 3/5/7
- Track match scores
- Declare tournament winner
- Tournament results screen
```

**What the Learner Sees:**
Tournament mode for extended play. Track match progress. Ultimate winner declared.

---

### Unit 58: Campaign Mode

**Learning Objectives:**
- Progressive challenges
- Unlock system
- Increasing difficulty
- Sense of progression

**Concepts Introduced:**
- Progression systems
- Unlock gates
- Challenge design
- Player journey

**Code Written:**
```
- Series of AI opponents
- Each harder than last
- Unlock next on victory
- Campaign completion reward
```

**What the Learner Sees:**
Campaign mode: beat progressively harder AI. Unlock opponents. Campaign completion achievement.

---

### Unit 59: Board Layouts

**Learning Objectives:**
- Additional board patterns
- Obstacles and variants
- Challenge boards
- Content variety

**Concepts Introduced:**
- Level design
- Board patterns
- Challenge modes
- Content creation

**Code Written:**
```
- Multiple obstacle patterns
- Challenge boards
- Selection in options
- Variety in play
```

**What the Learner Sees:**
Multiple board layouts. Obstacle patterns. More variety and replay value.

---

### Unit 60: Feature Complete

**Learning Objectives:**
- Final feature review
- Integration testing
- Bug fixes
- Feature lock

**Concepts Introduced:**
- Feature completeness
- Integration testing
- Release preparation
- Feature freeze

**Code Written:**
```
- Test all features together
- Fix integration issues
- Final adjustments
- Declare feature complete
```

**What the Learner Sees:**
All features working together. Complete game. Ready for release preparation.

---

### Unit 61: Loading Screen

**Learning Objectives:**
- Create loading display
- First impression
- Set expectations
- Professional presentation

**Concepts Introduced:**
- Loading experience
- First impressions
- Branding
- Professional start

**Code Written:**
```
- Loading screen graphic
- Copyright/credit text
- Brief display before title
- Clean transition
```

**What the Learner Sees:**
Game loads with proper loading screen. Professional first impression.

---

### Unit 62: Instructions

**Learning Objectives:**
- Complete documentation
- In-game help
- Printed instructions
- Player guidance

**Concepts Introduced:**
- Documentation
- User guidance
- Instruction writing
- Release materials

**Code Written:**
```
- Expand help screen
- Write text instructions
- Create quick reference
- Complete documentation
```

**What the Learner Sees:**
Complete instructions accessible in-game. Clear guidance for new players.

---

### Unit 63: Final Testing

**Learning Objectives:**
- Complete testing pass
- Edge cases
- Player testing
- Release candidate

**Concepts Introduced:**
- Release testing
- User testing
- Bug prioritisation
- Release readiness

**Code Written:**
```
- Full test pass
- Fix critical bugs
- Verify all paths
- Release candidate declared
```

**What the Learner Sees:**
Thoroughly tested game. All issues resolved. Ready for release.

---

### Unit 64: Distribution

**Learning Objectives:**
- Create distributable file
- TAP/TZX format
- Package game
- Release complete

**Concepts Introduced:**
- Distribution formats
- File packaging
- Release process
- Project completion

**Code Written:**
```
- Create TAP file
- Test on real hardware/emulator
- Package with documentation
- Release!
```

**What the Learner Sees:**
Finished TAP file ready to distribute. Complete game. Achievement unlocked.

**Phase 4 Checkpoint:**
The game is complete. Optimised, polished, feature-rich, and professionally packaged. It could have sold for £7.99 in 1984. The learner has built a commercial-quality game.

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

## Comparison: 16 Units vs 64 Units

| Aspect | 16-Unit Version | 64-Unit Version |
|--------|-----------------|-----------------|
| Gameplay | Two-player only | AI + Two-player |
| Sound | None | Full SFX + music |
| Visuals | Basic | Animated, polished |
| Options | None | Multiple settings |
| AI | None | Three difficulty levels |
| Save | None | Statistics tracking |
| Polish | Minimal | Professional |
| Commercial viable? | No | Yes |
| Time investment | 16-32 hours | 64-128 hours |

---

## Version History

- **2.0 (2026-01-09):** Complete restructure. Playable two-player game by Unit 16. Detailed unit breakdowns matching SID Symphony format. AI moved to Phase 2.
- **1.0 (2025-xx-xx):** Original outline (display-theory focused, no game until Phase 2).
