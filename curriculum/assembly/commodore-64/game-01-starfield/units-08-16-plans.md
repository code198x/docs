# Starfield Units 8–16: Implementation Plans

Units 1–7 give the learner a ship, bullets, an enemy, collision, and explosion feedback. Units 8–16 complete the game loop — scoring, death, restart, and polish.

Each plan below covers: what changes from the previous unit, new zero-page variables, assembly code design, snippets, and MDX section outline.

---

## Unit 8: Score Display

**Builds on:** Unit 7 (explosion feedback)
**What the learner builds:** A two-digit score displayed on screen using screen RAM. Each hit increments the score. The digits appear in the top-left corner.

### New variables
```asm
score         = $07     ; Score (0–99, BCD)
```

### Assembly code design
- **Init:** Clear score to `$00`. Write "00" to screen RAM ($0400/$0401) with colour RAM ($D800/$D801) set to white.
- **On hit:** After the explosion trigger in `hit_enemy`, use `SED` (decimal mode) to add 1 to score, then `CLD`. Convert the BCD byte to two ASCII digits: high nybble → tens digit, low nybble → ones digit. Write both to screen RAM.
- **Helper: `update_score`** — extracts nybbles with `LSR`×4 and `AND #$0F`, adds `$30` to get screen code for '0'–'9'.

### Key 6510 concepts
- **BCD mode** — `SED`/`CLD` for decimal arithmetic (no hex carry at 10)
- **Screen RAM** — writing characters directly to `$0400+`
- **Colour RAM** — `$D800+` controls per-character colour
- **Nybble extraction** — `LSR` four times for high, `AND #$0F` for low

### Snippets
1. `01-score-display.asm` — The `update_score` routine (nybble extraction, screen RAM writes)
2. `02-bcd-increment.asm` — The BCD add in `hit_enemy` (`SED` / `ADC` / `CLD`)

### MDX sections
- Screen RAM: Where Characters Live
- Colour RAM: One Byte Per Character
- Decimal Mode (BCD)
- Updating the Score Display
- The Complete Code
- If It Doesn't Work
- Try This: Starting Score / Score Cap at 99

---

## Unit 9: Enemy Waves

**Builds on:** Unit 8 (score display)
**What the learner builds:** Three enemies on screen at once, respawning in waves. Enemy positions stored in tables, processed with indexed addressing.

### New variables
```asm
enemy_x_tbl   = $08     ; 3 bytes: X positions for enemies 0–2
enemy_y_tbl   = $0b     ; 3 bytes: Y positions for enemies 0–2
enemy_active  = $0e     ; 3 bytes: active flag per enemy (0/1)
flash_tbl     = $11     ; 3 bytes: flash timer per enemy
```

### Assembly code design
- **Data tables:** Enemy state stored as parallel arrays — X, Y, active flag, flash timer. Indexed by X register (0, 1, 2).
- **Indexed addressing:** `LDA enemy_x_tbl,X` / `STA enemy_x_tbl,X` to process each enemy in a loop.
- **Subroutines:** Introduce `JSR`/`RTS`. Extract `spawn_enemy` (sets random X, Y at top, marks active) and `update_enemy` (movement, off-screen check) as subroutines.
- **Sprite mapping:** Sprites 2, 3, 4 for the three enemies. Sprite registers accessed via calculated offsets.
- **Collision check:** Loop through all active enemies for bullet collision. First hit wins — break out of the loop.

### Key 6510 concepts
- **Indexed addressing** — `LDA table,X` to access arrays of data
- **`JSR`/`RTS`** — subroutine call and return, the stack stores the return address
- **Data tables** — parallel arrays for multi-object state
- **Loop with index** — `LDX #$02` / `DEX` / `BPL` to iterate three enemies

### Snippets
1. `01-indexed-addressing.asm` — The enemy update loop with `LDA table,X`
2. `02-subroutines.asm` — `spawn_enemy` and `update_enemy` with `JSR`/`RTS`

### MDX sections
- Three Enemies at Once
- Data Tables
- Indexed Addressing: LDA table,X
- Subroutines: JSR and RTS
- The Complete Code
- If It Doesn't Work
- Try This: More Enemies / Faster Waves

---

## Unit 10: Player Death

**Builds on:** Unit 9 (enemy waves, indexed addressing, subroutines)
**What the learner builds:** The enemy can now kill the player. Each frame, check ship-enemy distance for all active enemies. On collision, set a `game_over` flag to stop the game loop.

### New variables
```asm
game_over     = $14     ; 0 = playing, 1 = game over
```

### Assembly code design
- **Ship-enemy collision:** After enemy movement, loop through all active enemies and compare each to the ship position. Same bounding-box distance check as bullet collision (Unit 6), but between ship and each enemy.
- **On player hit:** Set `game_over` to 1. The game loop checks this flag at the top — if set, skip all input/update logic. The game freezes.
- **Reuse pattern:** The distance-check code is the same shape as bullet collision, reinforcing the pattern.

### Key 6510 concepts
- **Reusing collision pattern** — same distance check, different sprites
- **Game state flag** — a single byte controls whether the game runs
- **Looped collision** — checking the ship against each enemy in the table

### Snippets
1. `01-ship-collision.asm` — The ship-enemy distance check loop
2. `02-game-over-flag.asm` — Setting and checking `game_over`

### MDX sections
- The Ship Can Die
- Reusing the Collision Pattern
- Checking All Enemies
- Freezing the Game
- The Complete Code
- If It Doesn't Work
- Try This: Different Death Effects

---

## Unit 11: Game Over

**Builds on:** Unit 10 (player death)
**What the learner builds:** "GAME OVER" text appears on screen. Pressing fire restarts the game — all state resets.

### New variables
```asm
game_state    = $14     ; 0 = playing, 1 = game over (replaces game_over)
```
Replaces `game_over` — same address, better name for what comes next.

### Assembly code design
- **`show_game_over` subroutine:** Writes "GAME OVER" to screen RAM at row 12, column 15 (centred on 40-column screen). Each character written as `LDA #char / STA $0400+offset`.
- **Screen codes:** C64 screen codes differ from PETSCII — 'A'=1, 'B'=2, etc. Calculated positions: row × 40 + column + $0400.
- **Colour:** Write matching colour values to colour RAM for the text.
- **`init_game` subroutine:** Extract all initialisation into a reusable subroutine. Called on first boot and on restart.
- **Restart:** Game loop checks `game_state`. If 1, poll fire button. On press, call `init_game`, clear screen, set `game_state` to 0.

### Key 6510 concepts
- **Screen RAM text output** — writing specific characters to calculated positions
- **Screen codes vs PETSCII** — C64 screen codes differ from PETSCII; 'A'=1, 'B'=2, etc.
- **Calculated screen positions** — row × 40 + column + $0400
- **Initialisation as subroutine** — reusable setup via `JSR init_game`

### Snippets
1. `01-game-over-text.asm` — The `show_game_over` subroutine with character writes
2. `02-restart.asm` — The `init_game` subroutine and restart logic

### MDX sections
- Screen Codes
- Positioning Text on Screen
- The Game Over Display
- Press Fire to Restart
- Extracting Initialisation
- The Complete Code
- If It Doesn't Work
- Try This: Custom Messages / Colour Effects

---

## Unit 12: Three Lives

**Builds on:** Unit 11 (game over + restart)
**What the learner builds:** The player has three lives. Each death decrements the counter. Lives displayed as a digit at the top-right of the screen. Game over only when lives reach zero.

### New variables
```asm
lives         = $15     ; Lives remaining (starts at 3)
```

### Assembly code design
- **Init:** Set `lives` to 3. Display "3" at top-right of screen RAM ($0400 + 39 = $0427).
- **On death:** Decrement `lives` with `DEC`. If zero, transition to game over. If non-zero, reset ship position, continue playing.
- **`update_lives_display`:** Convert lives count to screen code (add $30) and write to screen RAM.
- **Conditional transition:** `DEC lives / BEQ game_over_state` — game over only at zero.

### Key 6510 concepts
- **`DEC` for counters** — decrement a zero-page variable
- **Conditional state transition** — game over only at zero lives
- **Display update** — keeping screen in sync with game state

### Snippets
1. `01-lives-counter.asm` — Decrementing lives and checking for game over
2. `02-lives-display.asm` — Writing lives count to screen RAM

### MDX sections
- Tracking Lives
- Death Without Game Over
- Updating the Display
- The Complete Code
- If It Doesn't Work
- Try This: Extra Life at Score Threshold

---

## Unit 13: Life Lost Flash

**Builds on:** Unit 12 (three lives)
**What the learner builds:** When the player loses a life, the border flashes red for several frames and SID plays a descending tone on voice 3. An invulnerability timer prevents instant re-death.

### New variables
```asm
death_timer   = $16     ; Death flash countdown (0 = no flash)
```

### Assembly code design
- **On death (non-game-over):** Set `death_timer` to 16. Set border colour to red (`$D020 = $02`). Trigger SID voice 3 with a descending sawtooth.
- **Each frame:** If `death_timer` > 0, decrement. Ship is invulnerable during flash (skip ship-enemy collision). When timer expires, restore border to black, resume normal play.
- **SID voice 3:** Low-frequency sawtooth that decays — a falling, mournful tone contrasting with the sharp noise explosion.

### Key 6510 concepts
- **Border flash (`$D020`)** — simple whole-screen visual effect
- **SID voice 3** — third independent voice for the death sound
- **Invulnerability timer** — frame counter reuse, same pattern as `flash_timer`

### Snippets
1. `01-death-flash.asm` — Border flash with timer and colour restore
2. `02-death-sound.asm` — SID voice 3 descending sawtooth setup

### MDX sections
- The Border as Feedback
- Voice 3: A Different Sound
- Invulnerability During Flash
- The Complete Code
- If It Doesn't Work
- Try This: Different Death Sounds / Flash Colours

---

## Unit 14: Starfield

**Builds on:** Unit 13 (life lost flash)
**What the learner builds:** A star-filled scrolling background — the game's namesake. Characters written to screen RAM, coloured via colour RAM to suggest depth.

### New variables
```asm
star_tbl      = $17     ; Star Y offsets (8–16 stars in a table)
```

### Assembly code design
- **Star table:** A fixed table of screen RAM offsets for star positions. Each frame, move stars down by adding 40 (one row) to their offset. When past row 24, wrap to the top.
- **Character and colour:** Dim grey dots (colour $0B, dark grey) for distant stars, bright white dots (colour $01) for close ones. Character $2E (period) or $51 (filled circle) for different sizes.
- **Parallax illusion:** Close stars move every frame, distant stars move every other frame. A frame counter (AND #$01) controls the slow layer.
- **Init:** Scatter stars across the screen with initial offsets.

### Key 6510 concepts
- **Colour RAM (`$D800`+)** — per-character colour for visual depth
- **Character-based backgrounds** — using screen codes as graphics
- **Parallax scrolling** — two speed layers for depth illusion
- **Modular tables** — reusing the table pattern from Unit 9

### Snippets
1. `01-star-init.asm` — Setting up initial star positions in screen/colour RAM
2. `02-star-scroll.asm` — Moving stars down with wrap-around and parallax

### MDX sections
- The Namesake
- Characters as Graphics
- Colour for Depth
- Parallax: Two Speed Layers
- The Complete Code
- If It Doesn't Work
- Try This: More Stars / Different Patterns

---

## Unit 15: Title Screen

**Builds on:** Unit 14 (starfield)
**What the learner builds:** The game starts with a title screen showing "STARFIELD" and "PRESS FIRE". The state machine gains a third state: title, playing, game over.

### New variables
```asm
; game_state: 0 = title, 1 = playing, 2 = game over
```

### Assembly code design
- **State 0 (title):** Display "STARFIELD" and "PRESS FIRE" on screen RAM. Stars still animate in the background. Wait for fire button. On press, transition to state 1.
- **`show_title` subroutine:** Writes title text and "PRESS FIRE" prompt to screen RAM with colour.
- **`clear_screen` subroutine:** Factor out screen clearing, called before title and before gameplay.
- **State transitions:** Title → Playing (fire pressed), Playing → Game Over (death), Game Over → Title (fire pressed).

### Key 6510 concepts
- **Three-state machine** — title, playing, game over
- **Screen RAM fills** — clearing and writing larger blocks of text
- **State transitions** — branching on a state variable to different code paths

### Snippets
1. `01-title-screen.asm` — The `show_title` subroutine
2. `02-three-states.asm` — The expanded state machine with three branches

### MDX sections
- A Third State
- The Title Screen
- Screen Clearing Subroutine
- State Transitions
- The Complete Code
- If It Doesn't Work
- Try This: Colour Effects on Title

---

## Unit 16: Screen Edges

**Builds on:** Unit 15 (title screen)
**What the learner builds:** Full-width ship movement across the 320-pixel screen using the MSB register at `$D010`. Boundary clamping prevents the ship from wrapping.

### New variables
None new — this unit fixes how existing position logic works.

### Assembly code design
- **Sprite X bit 8 (`$D010`):** The C64 screen is wider than 255 pixels. `$D010` holds bit 8 of each sprite's X position. Use bit 0 for the ship so it can reach the right edge.
- **EOR for bit toggling:** When the ship crosses the 255/256 boundary, toggle bit 0 of `$D010` with `EOR #$01`.
- **Boundary clamping:** Prevent the ship from moving off-screen (top, bottom, left, right). Clamp Y to a visible range, handle X with 9-bit comparison logic.
- **Clean restart:** Ensure `$D010` resets to 0 on restart. Silence all SID voices (gate off on all three).

### Key 6510 concepts
- **`$D010` X-position MSB register** — bit 8 for each sprite's X coordinate
- **`EOR` for bit toggling** — flipping a single bit without affecting others
- **Boundary clamping** — `CMP`/branch to keep values in a valid range
- **9-bit arithmetic** — working with values that span two storage locations

### Snippets
1. `01-x-bit-8.asm` — Reading and writing `$D010` for 9-bit X positions
2. `02-boundary-clamp.asm` — Clamping ship movement to screen bounds

### MDX sections
- The Ninth Bit: `$D010`
- Toggling Bits with EOR
- Staying on Screen
- Clean Restarts
- The Complete Code
- If It Doesn't Work
- Phase 1 Complete: What You've Built

---

## Implementation Sequencing Notes

- **Unit 8 depends on Unit 7** — adds to the `hit_enemy` block
- **Unit 9 is a major refactor** — multiple enemies restructure the entire enemy section. Tables, indexed addressing, and subroutines all land at once. This is the biggest single-unit change in Phase 1.
- **Units 10–11 form a tight sequence** — death → game over + restart. Best implemented together.
- **Units 12–13 are paired** — lives counter and death feedback go together naturally
- **Unit 14 (starfield) is self-contained** — adds background visuals without changing game logic
- **Unit 15 (title screen) refactors state** — changes `game_state` from 2 values to 3, which ripples through the code
- **Unit 16 is polish** — fixes movement range and edge cases across all prior units

## Growing Complexity

By Unit 16, the assembly file will be significantly larger than Unit 7. Consider whether comments and section headers need updating as the file grows. The learner needs to navigate the code, so clear section markers matter.
