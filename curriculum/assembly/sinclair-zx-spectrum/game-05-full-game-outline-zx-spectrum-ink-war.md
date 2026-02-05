# ZX Spectrum Game 5: Ink War - Full 128-Unit Outline

**Platform:** Sinclair ZX Spectrum
**Game:** Ink War
**Units:** 128 (8 phases × 16 units)
**Concept:** Territory control strategy game where the attribute system IS the gameplay. Player vs AI, taking turns to claim 8×8 attribute cells. Control the majority to win. A unique genre that turns the Spectrum's colour limitations into a feature.

---

## Overview

Ink War is a deliberate change of pace. After four action games, learners explore strategic thinking and turn-based gameplay. The Spectrum's attribute system - often seen as a limitation - becomes the core mechanic. Every claimed cell changes colour, creating a visual battlefield.

**Key Learning Goals:**
- Deep attribute system mastery
- Turn-based game loop (different paradigm)
- Strategic AI decision-making
- Game state management
- Board game design principles
- Minimax or heuristic AI

---

## Phase 1: Board Foundation (Units 1-16)

### Unit 1: The Board
**Builds:** 8×8 grid of attribute cells displayed.
**Teaches:** Attribute-based display.
**Code pattern:**
```z80
; Display 8x8 board using attributes
; Each cell is 8x8 pixels = 1 attribute
; Board starts at attribute row 4, column 4
BOARD_ATTR_START equ $5900 + (4*32) + 4

draw_board:
    ld hl,BOARD_ATTR_START
    ld b,8              ; 8 rows
.row_loop:
    push bc
    push hl
    ld b,8              ; 8 columns
.col_loop:
    ld a,PAPER_WHITE | INK_BLACK
    ld (hl),a
    inc hl
    djnz .col_loop
    pop hl
    ld de,32            ; Next attribute row
    add hl,de
    pop bc
    djnz .row_loop
    ret

; Clear the pixel area too
clear_board_pixels:
    ld hl,$4000 + (32*8) + 4    ; Screen row 4, col 4
    ; ... clear 64x64 pixels
    ret
```
**If it doesn't work:** Board not showing? Check attribute address calculation. Wrong position? Verify starting offset.

---

### Unit 2: Cell Graphics
**Builds:** Each cell shows ownership pattern.
**Teaches:** Pixel patterns within attributes.
**Code pattern:**
```z80
; Draw pattern in cell to show ownership
; Unclaimed: empty, Player: cross-hatch, AI: diagonal
PATTERN_EMPTY   equ 0
PATTERN_PLAYER  equ 1
PATTERN_AI      equ 2

draw_cell_pattern:
    ; Input: B=row, C=col, A=pattern
    push af
    call get_cell_screen_addr   ; HL = screen address
    pop af

    cp PATTERN_EMPTY
    jr z,.draw_empty
    cp PATTERN_PLAYER
    jr z,.draw_player
    jr .draw_ai

.draw_empty:
    ld b,8
    xor a
.empty_loop:
    ld (hl),a
    inc h               ; Next pixel row
    djnz .empty_loop
    ret

.draw_player:
    ld de,player_pattern
    jr .draw_pattern

.draw_ai:
    ld de,ai_pattern

.draw_pattern:
    ld b,8
.pattern_loop:
    ld a,(de)
    ld (hl),a
    inc de
    inc h
    djnz .pattern_loop
    ret

player_pattern:
    defb %10101010
    defb %01010101
    defb %10101010
    defb %01010101
    defb %10101010
    defb %01010101
    defb %10101010
    defb %01010101

ai_pattern:
    defb %10000001
    defb %01000010
    defb %00100100
    defb %00011000
    defb %00011000
    defb %00100100
    defb %01000010
    defb %10000001
```

---

### Unit 3: Board State
**Builds:** Track who owns each cell.
**Teaches:** Game state array.
**Code pattern:**
```z80
; Board state: 8x8 = 64 bytes
; 0 = unclaimed, 1 = player, 2 = AI
board_state:
    defs 64, 0

; Get cell state
; Input: B=row (0-7), C=col (0-7)
; Output: A=state
get_cell_state:
    ld a,b
    rlca
    rlca
    rlca                ; row × 8
    or c                ; + col
    ld e,a
    ld d,0
    ld hl,board_state
    add hl,de
    ld a,(hl)
    ret

; Set cell state
; Input: B=row, C=col, A=new state
set_cell_state:
    push af
    ld a,b
    rlca
    rlca
    rlca
    or c
    ld e,a
    ld d,0
    ld hl,board_state
    add hl,de
    pop af
    ld (hl),a
    ret
```

---

### Unit 4: Cursor Display
**Builds:** Flashing cursor shows current selection.
**Teaches:** Cursor UI.
**Code pattern:**
```z80
cursor_row:     defb 0
cursor_col:     defb 0
cursor_flash:   defb 0

update_cursor:
    ; Flash cursor by toggling brightness
    ld a,(cursor_flash)
    inc a
    and $0f             ; Flash rate
    ld (cursor_flash),a
    jr nz,.no_toggle

    ; Toggle cursor cell brightness
    call get_cursor_attr_addr
    ld a,(hl)
    xor BRIGHT          ; Toggle bright bit
    ld (hl),a

.no_toggle:
    ret

get_cursor_attr_addr:
    ld a,(cursor_row)
    ld b,a
    ld a,(cursor_col)
    ld c,a
    ; Calculate attribute address
    ld a,b
    rlca
    rlca
    rlca
    rlca
    rlca                ; row × 32
    or c
    add a,4             ; board offset col
    ld l,a
    ld a,BOARD_ATTR_START / 256
    adc a,0
    add a,b             ; add row offset for attr rows
    ld h,a
    ; ... proper calculation needed
    ret
```

---

### Unit 5: Cursor Movement
**Builds:** Joystick moves cursor.
**Teaches:** Grid navigation.

---

### Unit 6: Cell Selection
**Builds:** Fire button claims cell.
**Teaches:** Selection mechanics.

---

### Unit 7: Claim Validation
**Builds:** Can only claim unclaimed cells.
**Teaches:** Move validation.
**Code pattern:**
```z80
; Check if move is valid
; Input: B=row, C=col
; Output: Carry set if invalid
validate_move:
    call get_cell_state
    or a                ; Check if 0 (unclaimed)
    jr nz,.invalid
    ; Also check adjacency rules if needed
    or a                ; Clear carry = valid
    ret
.invalid:
    scf                 ; Set carry = invalid
    ret
```

---

### Unit 8: Claim Cell
**Builds:** Update state and display.
**Teaches:** State change.
**Code pattern:**
```z80
; Claim cell for current player
; Input: B=row, C=col
claim_cell:
    ld a,(current_player)
    call set_cell_state

    ; Update attribute colour
    push bc
    call get_cell_attr_addr
    ld a,(current_player)
    cp PLAYER_HUMAN
    jr z,.player_colour
    ld a,PAPER_RED | INK_WHITE  ; AI colour
    jr .set_colour
.player_colour:
    ld a,PAPER_BLUE | INK_WHITE ; Player colour
.set_colour:
    ld (hl),a
    pop bc

    ; Draw ownership pattern
    ld a,(current_player)
    call draw_cell_pattern
    ret
```

---

### Unit 9: Turn System
**Builds:** Alternate between player and AI.
**Teaches:** Turn-based loop.
**Code pattern:**
```z80
current_player: defb PLAYER_HUMAN
PLAYER_HUMAN    equ 1
PLAYER_AI       equ 2

game_loop:
    call check_game_over
    jr c,.game_end

    ld a,(current_player)
    cp PLAYER_HUMAN
    jr z,.human_turn

.ai_turn:
    call ai_make_move
    jr .switch_turn

.human_turn:
    call wait_human_move

.switch_turn:
    ld a,(current_player)
    xor 3               ; Toggle between 1 and 2
    ld (current_player),a
    jr game_loop

.game_end:
    call show_winner
    ret
```

---

### Unit 10: Score Counting
**Builds:** Count cells owned by each player.
**Teaches:** Score calculation.
**Code pattern:**
```z80
count_scores:
    ld hl,board_state
    ld bc,64            ; 64 cells
    ld d,0              ; Player count
    ld e,0              ; AI count

.count_loop:
    ld a,(hl)
    cp PLAYER_HUMAN
    jr nz,.not_player
    inc d
.not_player:
    cp PLAYER_AI
    jr nz,.not_ai
    inc e
.not_ai:
    inc hl
    dec bc
    ld a,b
    or c
    jr nz,.count_loop

    ld a,d
    ld (player_score),a
    ld a,e
    ld (ai_score),a
    ret
```

---

### Unit 11: Score Display
**Builds:** Show scores on screen.
**Teaches:** HUD display.

---

### Unit 12: Win Condition
**Builds:** Game ends when board full.
**Teaches:** End condition.

---

### Unit 13: Winner Detection
**Builds:** Compare scores to determine winner.
**Teaches:** Victory logic.

---

### Unit 14: Sound - Claim
**Builds:** Sound when claiming cell.
**Teaches:** Action feedback.

---

### Unit 15: Sound - Invalid
**Builds:** Sound for invalid move.
**Teaches:** Error feedback.

---

### Unit 16: Phase 1 Polish
**Builds:** Basic game working.

---

## Phase 2: AI Foundation (Units 17-32)

### Unit 17: Random AI
**Builds:** AI picks random valid cell.
**Teaches:** Basic AI.
**Code pattern:**
```z80
ai_random_move:
.try_again:
    ; Generate random row and col
    call random
    and $07             ; 0-7
    ld b,a
    call random
    and $07
    ld c,a

    ; Check if valid
    call validate_move
    jr c,.try_again     ; Invalid, try again

    ; Make the move
    call claim_cell
    ret

random:
    ; Simple LFSR random number generator
    ld hl,(random_seed)
    ld a,h
    rra
    ld a,l
    rra
    xor h
    ld h,a
    ld a,l
    rra
    ld a,h
    rra
    xor l
    ld l,a
    xor h
    ld h,a
    ld (random_seed),hl
    ld a,l
    ret
```

---

### Unit 18: Greedy AI
**Builds:** AI picks cell with most neighbours.
**Teaches:** Heuristic evaluation.
**Code pattern:**
```z80
; Count how many adjacent cells AI owns
; This cell would connect to existing territory
count_adjacent:
    ; Input: B=row, C=col
    ; Output: A=count of adjacent AI cells
    ld d,0              ; Count

    ; Check up
    ld a,b
    or a
    jr z,.skip_up
    dec b
    call get_cell_state
    inc b
    cp PLAYER_AI
    jr nz,.skip_up
    inc d
.skip_up:

    ; Check down
    ld a,b
    cp 7
    jr z,.skip_down
    inc b
    call get_cell_state
    dec b
    cp PLAYER_AI
    jr nz,.skip_down
    inc d
.skip_down:

    ; Check left, right similarly...
    ; ...

    ld a,d
    ret

ai_greedy_move:
    ld e,0              ; Best score
    ld hl,0             ; Best position

    ; Check all cells
    ld b,0
.row_loop:
    ld c,0
.col_loop:
    ; Is cell available?
    call get_cell_state
    or a
    jr nz,.next_cell

    ; Score this cell
    call count_adjacent
    cp e
    jr c,.next_cell     ; Not better
    jr z,.next_cell

    ; New best
    ld e,a
    ld h,b
    ld l,c

.next_cell:
    inc c
    ld a,c
    cp 8
    jr nz,.col_loop
    inc b
    ld a,b
    cp 8
    jr nz,.row_loop

    ; Make best move
    ld b,h
    ld c,l
    call claim_cell
    ret
```

---

### Unit 19: Corner Strategy
**Builds:** AI prioritises corners.
**Teaches:** Strategic positions.

---

### Unit 20: Edge Strategy
**Builds:** AI values edges.
**Teaches:** Positional evaluation.

---

### Unit 21: Blocking
**Builds:** AI blocks player expansion.
**Teaches:** Defensive play.

---

### Unit 22: Look-Ahead (1 move)
**Builds:** AI considers player's response.
**Teaches:** Simple prediction.

---

### Unit 23: Position Scoring
**Builds:** Weighted cell values.
**Teaches:** Evaluation function.
**Code pattern:**
```z80
; Position weights - corners and edges more valuable
position_weights:
    defb 10, 2, 5, 5, 5, 5, 2, 10    ; Row 0
    defb  2, 1, 2, 2, 2, 2, 1,  2    ; Row 1
    defb  5, 2, 3, 3, 3, 3, 2,  5    ; Row 2
    defb  5, 2, 3, 3, 3, 3, 2,  5    ; Row 3
    defb  5, 2, 3, 3, 3, 3, 2,  5    ; Row 4
    defb  5, 2, 3, 3, 3, 3, 2,  5    ; Row 5
    defb  2, 1, 2, 2, 2, 2, 1,  2    ; Row 6
    defb 10, 2, 5, 5, 5, 5, 2, 10    ; Row 7

get_position_weight:
    ; Input: B=row, C=col
    ; Output: A=weight
    ld a,b
    rlca
    rlca
    rlca                ; row × 8
    or c
    ld e,a
    ld d,0
    ld hl,position_weights
    add hl,de
    ld a,(hl)
    ret
```

---

### Unit 24: AI Difficulty Levels
**Builds:** Easy/Medium/Hard AI.
**Teaches:** Difficulty scaling.

---

### Unit 25: Minimax Introduction
**Builds:** Basic minimax concept.
**Teaches:** Game tree search.

---

### Unit 26: Simple Minimax
**Builds:** 2-ply minimax search.
**Teaches:** Minimax implementation.
**Code pattern:**
```z80
; Minimax with depth 2
; Returns best move in best_row, best_col
minimax_search:
    ld a,255            ; Best score (minimising for opponent)
    ld (best_score),a

    ; Try each cell
    ld b,0
.row_loop:
    ld c,0
.col_loop:
    call get_cell_state
    or a
    jr nz,.next

    ; Simulate AI move
    push bc
    ld a,PLAYER_AI
    call set_cell_state

    ; Find opponent's best response
    call find_opponent_best

    ; Undo move
    pop bc
    push af             ; Save opponent score
    xor a
    call set_cell_state
    pop af

    ; Is this better for us? (opponent scores less)
    ld hl,best_score
    cp (hl)
    jr nc,.next

    ; New best
    ld (best_score),a
    ld a,b
    ld (best_row),a
    ld a,c
    ld (best_col),a

.next:
    inc c
    ld a,c
    cp 8
    jr nz,.col_loop
    inc b
    ld a,b
    cp 8
    jr nz,.row_loop
    ret
```

---

### Unit 27: Alpha-Beta Pruning
**Builds:** Optimised minimax.
**Teaches:** Search optimisation.

---

### Unit 28: Opening Book
**Builds:** Pre-computed opening moves.
**Teaches:** Opening theory.

---

### Unit 29: AI Personality
**Builds:** Different AI play styles.
**Teaches:** Behavioural variety.

---

### Unit 30: AI Thinking Display
**Builds:** Show AI is "thinking".
**Teaches:** User feedback.

---

### Unit 31: AI Move Delay
**Builds:** AI doesn't move instantly.
**Teaches:** Pacing.

---

### Unit 32: Phase 2 Polish
**Builds:** Smart, beatable AI.

---

## Phase 3: Game Modes (Units 33-48)

### Unit 33: Two-Player Mode
**Builds:** Human vs human.
**Teaches:** Multiplayer.

---

### Unit 34: Player Colours
**Builds:** Choose your colour.
**Teaches:** Customisation.

---

### Unit 35: First Move Choice
**Builds:** Who goes first option.
**Teaches:** Fairness options.

---

### Unit 36: Board Sizes
**Builds:** 6×6, 8×8, 10×10 options.
**Teaches:** Variant rules.

---

### Unit 37: Time Limits
**Builds:** Optional move timer.
**Teaches:** Pressure mechanics.

---

### Unit 38: Handicap Mode
**Builds:** AI starts with cells.
**Teaches:** Difficulty adjustment.

---

### Unit 39: Tournament Mode
**Builds:** Best of 3/5 matches.
**Teaches:** Match structure.

---

### Unit 40: Quick Play
**Builds:** Fast game variant.
**Teaches:** Game variants.

---

### Unit 41: Undo Move
**Builds:** Take back last move.
**Teaches:** Undo functionality.

---

### Unit 42: Move History
**Builds:** Review game moves.
**Teaches:** History tracking.

---

### Unit 43: Replay Mode
**Builds:** Watch completed game.
**Teaches:** Replay system.

---

### Unit 44: Save Game
**Builds:** Save/load game state.
**Teaches:** Persistence.

---

### Unit 45: Statistics
**Builds:** Win/loss tracking.
**Teaches:** Stats system.

---

### Unit 46: Achievements
**Builds:** Unlock achievements.
**Teaches:** Achievement system.

---

### Unit 47: Tutorial Mode
**Builds:** Learn to play.
**Teaches:** Onboarding.

---

### Unit 48: Phase 3 Polish
**Builds:** Complete mode variety.

---

## Phase 4: Visual Polish (Units 49-64)

### Unit 49: Board Theme
**Builds:** Different colour schemes.
**Teaches:** Visual themes.

---

### Unit 50: Cell Animation
**Builds:** Cells animate when claimed.
**Teaches:** Feedback animation.

---

### Unit 51: Cursor Animation
**Builds:** Animated cursor.
**Teaches:** UI animation.

---

### Unit 52: Score Animation
**Builds:** Scores update with effect.
**Teaches:** Number animation.

---

### Unit 53: Victory Animation
**Builds:** Winner celebration.
**Teaches:** Victory effects.

---

### Unit 54: Border Effects
**Builds:** Decorative border.
**Teaches:** Visual framing.

---

### Unit 55: Player Indicators
**Builds:** Clear turn indicator.
**Teaches:** State display.

---

### Unit 56: Move Preview
**Builds:** Show what cell would look like.
**Teaches:** Preview feedback.

---

### Unit 57: Territory Lines
**Builds:** Show connected regions.
**Teaches:** Visual grouping.

---

### Unit 58: Capture Animation
**Builds:** Effect when gaining territory.
**Teaches:** Reward feedback.

---

### Unit 59: Background Pattern
**Builds:** Non-board screen decoration.
**Teaches:** Background design.

---

### Unit 60: Logo Design
**Builds:** Ink War logo.
**Teaches:** Title graphics.

---

### Unit 61: Character Set
**Builds:** Custom font/graphics.
**Teaches:** Character design.

---

### Unit 62: Colour Harmony
**Builds:** Pleasing colour combinations.
**Teaches:** Colour theory.

---

### Unit 63: Visual Consistency
**Builds:** Unified look.
**Teaches:** Visual coherence.

---

### Unit 64: Phase 4 Polish
**Builds:** Polished visuals.

---

## Phase 5: Audio (Units 65-80)

### Unit 65: Sound System
**Builds:** Beeper sound manager.
**Teaches:** Audio architecture.

---

### Unit 66: Move Sound
**Builds:** Cell claim sound.
**Teaches:** Action audio.

---

### Unit 67: Invalid Sound
**Builds:** Error beep.
**Teaches:** Error audio.

---

### Unit 68: Cursor Sound
**Builds:** Movement clicks.
**Teaches:** Navigation audio.

---

### Unit 69: Turn Sound
**Builds:** Turn change indicator.
**Teaches:** State change audio.

---

### Unit 70: Victory Fanfare
**Builds:** Winner celebration.
**Teaches:** Success audio.

---

### Unit 71: Defeat Sound
**Builds:** Loss acknowledgment.
**Teaches:** Failure audio.

---

### Unit 72: Music - Title
**Builds:** Title screen music.
**Teaches:** Beeper music.

---

### Unit 73: Music - Game
**Builds:** Subtle background music.
**Teaches:** Game music.

---

### Unit 74: Music Toggle
**Builds:** Music on/off option.
**Teaches:** Audio options.

---

### Unit 75: Sound Effects Toggle
**Builds:** SFX on/off option.
**Teaches:** Audio preferences.

---

### Unit 76: AI Thinking Sound
**Builds:** Processing indicator.
**Teaches:** Feedback audio.

---

### Unit 77: Timer Warning
**Builds:** Low time alert.
**Teaches:** Warning audio.

---

### Unit 78: Combo Sound
**Builds:** Multi-capture celebration.
**Teaches:** Reward audio.

---

### Unit 79: Audio Balance
**Builds:** Volume levels.
**Teaches:** Audio mixing.

---

### Unit 80: Phase 5 Polish
**Builds:** Complete audio.

---

## Phase 6: Presentation (Units 81-96)

### Unit 81: Title Screen
**Builds:** Attractive start.
**Teaches:** Title design.

---

### Unit 82: Menu System
**Builds:** Mode selection.
**Teaches:** Menu navigation.

---

### Unit 83: Instructions
**Builds:** How to play.
**Teaches:** Rule explanation.

---

### Unit 84: Strategy Tips
**Builds:** Hints for players.
**Teaches:** Strategy guidance.

---

### Unit 85: High Scores
**Builds:** Best performances.
**Teaches:** Score tracking.

---

### Unit 86: Credits
**Builds:** Attribution.
**Teaches:** Credits design.

---

### Unit 87: Pause Screen
**Builds:** In-game pause.
**Teaches:** Pause handling.

---

### Unit 88: Game Over
**Builds:** End screen.
**Teaches:** Conclusion.

---

### Unit 89: Attract Mode
**Builds:** Demo play.
**Teaches:** Attract sequence.

---

### Unit 90: Loading Screen
**Builds:** Initial display.
**Teaches:** Load presentation.

---

### Unit 91: Options Menu
**Builds:** Settings screen.
**Teaches:** Options design.

---

### Unit 92: Confirm Dialogs
**Builds:** "Are you sure?" prompts.
**Teaches:** Confirmation UI.

---

### Unit 93: Error Messages
**Builds:** Clear error feedback.
**Teaches:** Error handling.

---

### Unit 94: Help System
**Builds:** In-game help.
**Teaches:** Help design.

---

### Unit 95: Polish Pass
**Builds:** Final UI tweaks.
**Teaches:** UI refinement.

---

### Unit 96: Phase 6 Polish
**Builds:** Complete presentation.

---

## Phase 7: Optimisation (Units 97-112)

### Unit 97: AI Speed
**Builds:** Fast AI calculation.
**Teaches:** Algorithm optimisation.

---

### Unit 98: Display Speed
**Builds:** Fast screen updates.
**Teaches:** Display efficiency.

---

### Unit 99: Memory Usage
**Builds:** Efficient data storage.
**Teaches:** Memory optimisation.

---

### Unit 100: Code Size
**Builds:** Compact code.
**Teaches:** Size optimisation.

---

### Unit 101-104: Balance
**Builds:** Fair AI difficulty.
**Teaches:** Game balance.

---

### Unit 105-108: Bug Fixes
**Builds:** Find and fix issues.
**Teaches:** Debugging.

---

### Unit 109-111: Polish
**Builds:** Final refinements.
**Teaches:** Quality polish.

---

### Unit 112: Phase 7 Complete
**Builds:** Stable game.

---

## Phase 8: Release (Units 113-128)

### Unit 113-116: TAP/TZX Creation
**Builds:** Distribution format.
**Teaches:** Tape image.

---

### Unit 117-120: Testing
**Builds:** Thorough testing.
**Teaches:** Quality assurance.

---

### Unit 121-124: Final Polish
**Builds:** Last adjustments.
**Teaches:** Release prep.

---

### Unit 125-127: Documentation
**Builds:** Instructions.
**Teaches:** Documentation.

---

### Unit 128: Release
**Builds:** Final release.
**Teaches:** Shipping.

---

## Version History

- **1.0 (2026-01-18):** Initial 128-unit outline created.
