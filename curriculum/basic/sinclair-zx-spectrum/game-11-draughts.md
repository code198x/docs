# Game 11: Draughts

**Track:** Spectrum BASIC
**Genre:** Two-player board game
**Units:** 32 (2 phases × 16 units)
**Language:** Sinclair BASIC
**Max lines:** ~300

---

## Premise

Two players sit at the same keyboard and play draughts (checkers) on an 8×8 board. Dark pieces and light pieces, diagonal moves, captures by jumping, and the glorious moment when a piece reaches the far side and becomes a king.

The board is drawn with PRINT AT using INK and PAPER to create the alternating dark and light squares. Pieces sit on the dark squares — circles or filled blocks in contrasting colours. The game enforces every rule: pieces move diagonally, captures are mandatory when available, kings move backward as well as forward. No cheating allowed.

This is the first game where the learner builds a complete rule system. Previous games had simple collision or scoring rules. Draughts demands precision — every possible move must be checked, validated, and either allowed or rejected with a clear explanation. The code grows to 300 lines, and every line matters.

---

## Core Mechanics

### The Board

An 8×8 grid displayed using PRINT AT. Each square is one character cell. Dark squares use PAPER 1 (blue) or PAPER 0 (black); light squares use PAPER 6 (yellow) or PAPER 7 (white). Only dark squares are playable — pieces never appear on light squares.

Row labels 1-8 down the left side, column labels A-H across the top.

### The Pieces

Each player starts with 12 pieces on the dark squares of their nearest three rows.

| Player | Piece character | INK colour | Starting rows |
|--------|----------------|------------|---------------|
| Player 1 | `O` or UDG | Red (2) | Rows 1-3 |
| Player 2 | `O` or UDG | Green (4) | Rows 6-8 |
| King (P1) | `K` or UDG | Red (2), BRIGHT | — |
| King (P2) | `K` or UDG | Green (4), BRIGHT | — |

### Movement

- Ordinary pieces move one square diagonally forward (toward the opponent's side).
- Kings move one square diagonally in any direction.
- A piece captures an opponent by jumping over it diagonally to the empty square beyond. The captured piece is removed.
- Multi-jump captures: if a piece lands from a capture and can immediately capture again, it must continue jumping.
- Captures are mandatory. If a player can capture, they must. If multiple captures are available, the player chooses which one.

### Input

Players enter moves as coordinate pairs: origin and destination. For example, `C3 D4` moves the piece at column C, row 3 to column D, row 4. The game validates the input format, checks that the origin contains the current player's piece, and verifies the move is legal.

Invalid input produces a clear message: "No piece there", "That piece can't move there", "You must capture", or similar.

### King Promotion

When a piece reaches the opponent's back row (row 8 for Player 1, row 1 for Player 2), it becomes a king. The display changes to show the crowned piece. Kings can move and capture in all four diagonal directions.

### Win Condition

A player wins when the opponent has no pieces remaining, or when the opponent has no legal moves on their turn.

### Screen Layout

```
     A B C D E F G H
   ┌─────────────────┐
 1 │ . O . O . O . O │
 2 │ O . O . O . O . │
 3 │ . O . O . O . O │
 4 │   .   .   .   . │
 5 │ .   .   .   .   │
 6 │ O . O . O . O . │
 7 │ . O . O . O . O │
 8 │ O . O . O . O . │
   └─────────────────┘

 Player 1's turn
 Enter move (e.g. C3 D4):
```

The status area below the board shows whose turn it is, captured piece counts, and input prompts.

---

## Phase Breakdown

### Phase 1: The Board and Basic Play (Units 1-16)

Build the board display, place pieces, handle basic movement and single captures. By the end of this phase, two players can take turns moving pieces and capturing, with full validation of legal moves.

| Unit | Title | What the learner builds | New concepts |
|------|-------|------------------------|---------------|
| 1 | The Board Array | A 2D array `DIM b(8,8)` to represent the board. Values: 0=empty, 1=player 1 piece, 2=player 2 piece (kings added later). Fill the starting positions with a loop. | Board state as 2D array, initialisation pattern |
| 2 | Drawing the Board | PRINT AT loop draws the 8×8 grid. Alternating PAPER colours for dark and light squares. Empty board — no pieces yet, just the chequerboard pattern. | PRINT AT with INK/PAPER per cell, alternating colour pattern |
| 3 | Drawing Pieces | Read the board array and draw pieces on their squares. Player 1 pieces in red, Player 2 in green. The board looks like a real draughts game. | Mapping array data to screen display, colour per player |
| 4 | Row and Column Labels | Add labels: A-H across the top, 1-8 down the side. These give the player coordinates to reference when entering moves. | Formatted display layout, CHR$ for letters |
| 5 | Turn Tracking | A variable tracks whose turn it is (1 or 2). Display "Player 1's turn" or "Player 2's turn" below the board. Alternates after each valid move. | Turn-based flow, state variable |
| 6 | Reading Input | INPUT a move string like "C3 D4". Parse it into four values: source column, source row, destination column, destination row. Handle the letter-to-number conversion (A=1, B=2, etc.). | String parsing, CODE for letter conversion, input validation |
| 7 | Validating the Source | Check that the source square contains the current player's piece. "No piece there" if empty. "That's not your piece" if it belongs to the opponent. | Multi-condition validation, clear error messages |
| 8 | Diagonal Check | Verify the destination is exactly one square diagonally from the source. Reject horizontal, vertical, or long-distance moves. "Pieces move diagonally" if wrong. | Absolute difference check, diagonal geometry |
| 9 | Forward-Only Movement | Ordinary pieces can only move forward — toward the opponent's side. Player 1 moves toward row 8, Player 2 toward row 1. Reject backward moves for non-kings. | Direction constraint, player-specific rules |
| 10 | Making a Move | If the move is valid: update the board array (clear the source, set the destination), redraw the affected squares, switch turns. The game plays — two players can move pieces. | Array update, selective redraw, turn switch |
| 11 | Occupied Square Check | Reject moves to squares that already contain a piece. "That square is occupied." Check before allowing the move. | Pre-move validation, layered checks |
| 12 | Single Capture | Detect when the destination is two squares diagonally away and an opponent's piece sits in between. Remove the jumped piece from the array and screen. | Capture detection, intermediate square calculation |
| 13 | Capture Validation | A capture is only valid if the landing square is empty and the jumped square contains an opponent's piece. Reject captures over your own pieces or onto occupied squares. | Complex conditional logic, multiple validation steps |
| 14 | Capture Display | When a capture happens, update the display: remove the captured piece, move the capturing piece, show a brief BEEP. Display captured piece counts below the board. | Visual feedback, capture counting |
| 15 | Subroutine Structure | Organise the code into GO SUBs: draw board, read input, validate move, make move, check capture. The main loop calls each in sequence. | Code organisation at scale, GO SUB architecture |
| 16 | Two-Player Game | Two players can take turns, move pieces diagonally, and capture opponent pieces. Invalid moves are rejected with clear messages. The board updates correctly after every move. | Integration milestone, end-to-end play |

**Milestone:** A working two-player draughts game with board display, piece movement, single captures, and input validation. Two people can sit down and play — though kings, mandatory captures, and win detection are still to come.

### Phase 2: Full Rules and Polish (Units 17-32)

Add king promotion, mandatory captures, multi-jump chains, win detection, and polish. The game enforces every rule of draughts by the end.

| Unit | Title | What the learner builds | New concepts |
|------|-------|------------------------|---------------|
| 17 | King Promotion | When a piece reaches the opponent's back row, change its value in the array (3=player 1 king, 4=player 2 king). Draw kings with a different character or BRIGHT to distinguish them. | State change on condition, extended array values |
| 18 | King Movement | Kings can move diagonally in all four directions, not just forward. Modify the validation to allow backward moves for kings. | Conditional rule relaxation, piece-type branching |
| 19 | King Captures | Kings can capture in any diagonal direction — forward and backward. The capture logic now checks piece type before applying the forward-only restriction. | Unified capture logic with type-specific rules |
| 20 | Scanning for Captures | Before accepting a simple move, scan the board for any available captures for the current player. If a capture exists, the player must take one — simple moves are rejected. | Board scanning, mandatory capture rule |
| 21 | Finding All Captures | A subroutine that checks all of the current player's pieces and records which ones can capture. If the player tries to move a piece that cannot capture while another piece can, reject it. | Systematic search, move enumeration |
| 22 | Multi-Jump Chains | After a capture, check if the same piece can capture again from its new position. If so, the turn continues — the player must keep jumping until no more captures are available. | Recursive-style logic with GO TO, chain detection |
| 23 | Multi-Jump Input | During a multi-jump, prompt the player for each subsequent jump. Display which piece is continuing and highlight available landing squares. | Mid-turn interaction, constrained input |
| 24 | Win by Elimination | After each capture, check if the opponent has any pieces left. If not, the current player wins. Display "Player N wins!" with a celebratory BEEP and the final board. | Win condition check, game end state |
| 25 | Win by No Moves | At the start of each turn, check if the current player has any legal moves (including captures). If not, the other player wins. This handles the stalemate case in draughts. | Exhaustive move search, stalemate detection |
| 26 | Move Highlighting | When the player selects a source piece, briefly highlight the legal destination squares (FLASH or different INK). Helps the player see what moves are available. | Visual move preview, user experience |
| 27 | Error Message Area | Dedicate a fixed area below the board for messages. Clear it before each new message. Prevents old errors lingering on screen or scrolling the display. | Screen region management, message display |
| 28 | New Game Option | After a game ends, offer "Play again? (Y/N)". If yes, reset the board array, redraw, and start fresh. No need to re-run the program. | Game reset, replay loop |
| 29 | Piece Count Display | Show each player's remaining piece count and captured count in the status area. Update after every capture. | Running tallies, formatted status display |
| 30 | Sound Design | Distinct sounds: piece placed (short click), capture (satisfying thud), king promotion (ascending fanfare), win (celebratory sequence), invalid move (low buzz). | BEEP sequences for game events |
| 31 | Edge Case Testing | Test and fix: captures at board edges, king promotion during a multi-jump chain, capturing the last piece mid-chain, both players unable to move. | Systematic testing, edge case handling |
| 32 | The Finished Game | Clean up the listing. Test a complete game from start to finish. Both players follow the full rules of draughts. 300 lines of working, rule-enforcing board game code. | Code review, final integration, polish |

**Milestone:** A complete two-player draughts game with king promotion, mandatory captures, multi-jump chains, win detection (by elimination and by no legal moves), move highlighting, sound effects, and replay. The full rules of draughts, enforced precisely.

---

## Technical Notes

### Board Array

```
DIM b(8,8)
Values:
  0 = empty
  1 = Player 1 piece
  2 = Player 2 piece
  3 = Player 1 king
  4 = Player 2 king
```

Only squares where `(row + col)` is odd (or even, depending on convention) are playable. The other squares are always 0 and are drawn as light-coloured cells.

### Key Variables

```
t   - whose turn (1 or 2)
sr  - source row
sc  - source column
dr  - destination row
dc  - destination column
c1  - player 1 captured count
c2  - player 2 captured count
mj  - multi-jump flag (1 = currently in a chain)
```

### Input Parsing

The move string "C3 D4" is parsed as:
- `CODE a$(1) - CODE "A" + 1` → source column (3)
- `VAL a$(2)` → source row (3)
- `CODE a$(4) - CODE "A" + 1` → destination column (4)
- `VAL a$(5)` → destination row (4)

Validate string length and character ranges before parsing.

### Line Numbering

- 1-99: Initialisation, board setup, DIM
- 100-149: Draw board subroutine
- 150-199: Draw pieces subroutine
- 200-299: Main game loop (turn flow, input, dispatch)
- 300-349: Input parsing and format validation
- 350-399: Move validation (diagonal, forward, occupied)
- 400-449: Capture detection and validation
- 450-499: Multi-jump chain logic
- 500-549: King promotion
- 550-599: Win condition checks
- 600-649: Display messages and status
- 650-699: Capture scanning (mandatory capture check)
- 700-749: Sound effects
- 750-799: New game / reset

### Memory

The game uses minimal memory. The 8×8 board array, a handful of scalar variables, and ~300 lines of BASIC fit comfortably in the 48K Spectrum's available memory.

### No ELSE

The Spectrum 48K has no ELSE keyword. All branching uses `IF condition THEN GO TO line` to skip past the alternative. Multi-condition validation is built from layered IF/THEN checks, each jumping to an error message line or falling through to the next check.

---

## Changelog

- **v1.0 (2026-03-13):** Initial game outline for v5.0 curriculum.
