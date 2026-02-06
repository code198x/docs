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

## Unit 9: Enemies Spawn Continuously

**Builds on:** Unit 8 (score display)
**What the learner builds:** Instead of one enemy, a spawn timer creates a new enemy periodically. Still one enemy on screen at a time, but the spawn timing is controlled rather than immediate.

### New variables
```asm
spawn_timer   = $08     ; Frames until next enemy spawn
enemy_active  = $09     ; 0 = no enemy on screen, 1 = active
```

### Assembly code design
- **Init:** Set `enemy_active` to 1, `spawn_timer` to 0 (enemy starts on screen).
- **On hit/off-screen:** Set `enemy_active` to 0, disable sprite 2, set `spawn_timer` to 60 (about 1.2 seconds at PAL).
- **Spawn logic:** Each frame, if `enemy_active` is 0, decrement `spawn_timer`. When it reaches 0, spawn a new enemy (random X, Y at top), set `enemy_active` to 1, enable sprite 2.
- **Subroutines:** Introduce `JSR`/`RTS` — extract `spawn_enemy` as a subroutine called from both init and spawn timer expiry.

### Key 6510 concepts
- **`JSR`/`RTS`** — subroutine call and return, the stack stores the return address
- **Spawn timer** — another frame counter, this time for delayed appearance
- **Active flags** — tracking whether an object exists on screen

### Snippets
1. `01-spawn-timer.asm` — The spawn countdown and enemy activation
2. `02-subroutine.asm` — The `spawn_enemy` subroutine with `JSR`/`RTS`

### MDX sections
- Subroutines: JSR and RTS
- The Spawn Timer
- Active Flags
- The Complete Code
- If It Doesn't Work
- Try This: Faster/Slower Spawns

---

## Unit 10: Enemy Touches Ship = Death

**Builds on:** Unit 9 (spawn timer, subroutines)
**What the learner builds:** The enemy can now kill the player. Each frame, check enemy-ship distance. On collision, the ship flashes red and the game halts (for now — no lives yet, just a stop).

### New variables
```asm
player_dead   = $0a     ; 0 = alive, 1 = dead
```

### Assembly code design
- **New collision check:** After enemy movement, compare enemy position to ship position using the same distance-check pattern from Unit 6. Ship position comes from `$D000`/`$D001`.
- **On player hit:** Set `player_dead` to 1, flash border red (`$D020 = $02`), play a death sound on voice 3 (low descending tone).
- **Game loop guard:** At the top of the game loop, check `player_dead`. If set, skip all input/update logic — the game freezes.

### Key 6510 concepts
- **Reusing collision pattern** — same distance check, different sprites
- **Game state flag** — a single byte controls whether the game runs
- **SID voice 3** — third independent voice for the death sound

### Snippets
1. `01-ship-collision.asm` — The enemy-ship distance check
2. `02-death-state.asm` — Setting `player_dead`, border flash, game freeze

### MDX sections
- The Ship Can Die
- Reusing the Collision Pattern
- Voice 3: The Death Sound
- Freezing the Game
- The Complete Code
- If It Doesn't Work
- Try This: Different Death Effects

---

## Unit 11: Game Over Screen

**Builds on:** Unit 10 (death state)
**What the learner builds:** When the player dies, "GAME OVER" appears in the centre of the screen using screen RAM writes. The game stays frozen — no restart yet.

### New variables
None new — uses `player_dead` from Unit 10.

### Assembly code design
- **`show_game_over` subroutine:** Writes "GAME OVER" to screen RAM at row 12, column 15 (centred on 40-column screen). Each character written with a loop or unrolled `LDA #char / STA $0400+offset` sequence.
- **Colour:** Write matching colour values to colour RAM for the text.
- **Called once:** When `player_dead` transitions from 0 to 1, call `show_game_over` then keep looping without updates.

### Key 6510 concepts
- **Screen RAM text output** — writing specific characters to calculated positions
- **Screen codes vs PETSCII** — C64 screen codes differ from PETSCII; 'A'=1, 'B'=2, etc.
- **Calculated screen positions** — row × 40 + column + $0400

### Snippets
1. `01-screen-text.asm` — The `show_game_over` subroutine with character writes
2. `02-screen-position.asm` — Calculating row/column offsets in screen RAM

### MDX sections
- Screen Codes
- Positioning Text on Screen
- The Game Over Display
- The Complete Code
- If It Doesn't Work
- Try This: Custom Messages / Colour Effects

---

## Unit 12: Press Fire to Restart

**Builds on:** Unit 11 (game over screen)
**What the learner builds:** After game over, pressing fire restarts the game. All state resets — score, enemy position, player position, screen cleared.

### New variables
```asm
game_state    = $0b     ; 0 = playing, 1 = game over
```
Replaces `player_dead` — more general purpose.

### Assembly code design
- **State machine:** `game_state` replaces `player_dead`. The game loop branches on `game_state`: if 0, run the game; if 1, check for fire button.
- **`init_game` subroutine:** Extract all initialisation into a reusable subroutine. Called on first boot and on restart.
- **Restart:** When fire is pressed during game over, call `init_game`, clear the screen, set `game_state` to 0.

### Key 6510 concepts
- **State machine** — game behaviour determined by a state variable
- **Initialisation as subroutine** — reusable setup via `JSR init_game`
- **Complete reset** — clearing screen, variables, sprite positions

### Snippets
1. `01-state-machine.asm` — The game loop branching on `game_state`
2. `02-restart.asm` — The `init_game` subroutine and restart logic

### MDX sections
- Game States
- The State Machine Pattern
- Extracting Initialisation
- The Restart Flow
- The Complete Code
- If It Doesn't Work
- Try This: Countdown Before Restart

---

## Unit 13: Title Screen

**Builds on:** Unit 12 (restart, state machine)
**What the learner builds:** The game starts with a title screen showing the game name. Press fire to begin. The state machine gains a third state.

### New variables
```asm
; game_state: 0 = title, 1 = playing, 2 = game over
```

### Assembly code design
- **State 0 (title):** Display "STARFIELD" and "PRESS FIRE" on screen RAM. Wait for fire button. On press, transition to state 1.
- **`show_title` subroutine:** Writes title text and "PRESS FIRE" prompt to screen RAM with colour.
- **Screen clear:** Factor out screen clearing into a `clear_screen` subroutine, called before title and before gameplay.
- **State transitions:** Title → Playing (fire pressed), Playing → Game Over (death), Game Over → Title (fire pressed).

### Key 6510 concepts
- **Three-state machine** — title, playing, game over
- **Screen RAM fills** — clearing and writing larger blocks of text
- **Colour RAM** — per-character colour for styled title text

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

## Unit 14: Three Lives

**Builds on:** Unit 13 (title screen, three-state machine)
**What the learner builds:** The player has three lives. Each death decrements the counter. Lives displayed as ship icons (or numbers) at the top of the screen. Game over only when lives reach zero.

### New variables
```asm
lives         = $0c     ; Lives remaining (starts at 3)
```

### Assembly code design
- **Init:** Set `lives` to 3. Display "3" (or three ship characters) at top-right of screen RAM.
- **On death:** Decrement `lives`. If zero, transition to game over. If non-zero, flash the ship, reset positions, continue playing.
- **`update_lives_display`:** Write current lives count to screen RAM.
- **Respawn:** After losing a life, brief invulnerability (reuse frame counter pattern from Unit 7).

### Key 6510 concepts
- **Game state in zero page** — lives as a tracked variable
- **Conditional state transition** — game over only at zero lives
- **Display update** — keeping screen in sync with game state

### Snippets
1. `01-lives-counter.asm` — Decrementing lives and checking for game over
2. `02-lives-display.asm` — Writing lives count to screen RAM

### MDX sections
- Tracking Lives
- Death Without Game Over
- Updating the Display
- Brief Invulnerability
- The Complete Code
- If It Doesn't Work
- Try This: Extra Life at Score Threshold

---

## Unit 15: Life Lost Flash/Sound

**Builds on:** Unit 14 (three lives)
**What the learner builds:** When the player loses a life, the border flashes red for several frames and SID plays a descending tone. Visual and audio feedback for death, matching the explosion feedback from Unit 7.

### New variables
```asm
death_timer   = $0d     ; Death flash countdown (0 = no flash)
```

### Assembly code design
- **On death (non-game-over):** Set `death_timer` to 16. Set border colour to red (`$D020 = $02`). Trigger SID voice 3 with a descending sawtooth.
- **Each frame:** If `death_timer` > 0, decrement. Ship is invulnerable during flash. When timer expires, restore border to black, resume normal play.
- **SID voice 3:** Low-frequency sawtooth that decays — a falling, mournful tone contrasting with the sharp noise explosion.

### Key 6510 concepts
- **Border flash (`$D020`)** — simple whole-screen visual effect
- **SID voice 3 as sound** — using the third voice for game audio (not just random numbers)
- **Frame counter reuse** — same pattern as `flash_timer`, different purpose

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

## Unit 16: Integration + Edge Cases

**Builds on:** Unit 15 (death flash/sound)
**What the learner builds:** The final Phase 1 unit. Fixes edge cases: sprite X bit 8 for wide-screen movement, screen boundary clamping, reset of all timers on restart. The game is now a complete, polished loop.

### New variables
None new — this unit is about fixing and integrating existing code.

### Assembly code design
- **Sprite X bit 8 (`$D010`):** The C64 screen is wider than 255 pixels. `$D010` holds bit 8 of each sprite's X position. Handle this for the ship so it can reach the right edge.
- **Boundary clamping:** Prevent the ship from moving off-screen (top, bottom, left, right). Clamp Y to a visible range, handle X with the 9-bit logic.
- **Clean restart:** Ensure all timers (`flash_timer`, `spawn_timer`, `death_timer`) reset to 0 on restart. Ensure SID voices are silenced (gate off on all three).
- **Edge case: bullet vs dead enemy:** Don't check collision if enemy is inactive or flashing.
- **Edge case: fire during death flash:** Ignore fire input during `death_timer` countdown.

### Key 6510 concepts
- **9-bit X positions** — `$D010` as a bitmask for bit 8 of each sprite's X
- **Boundary checking** — clamping values with `CMP`/branch
- **Integration testing mindset** — finding and fixing interactions between systems

### Snippets
1. `01-x-bit-8.asm` — Reading and writing `$D010` for 9-bit X positions
2. `02-boundary-clamp.asm` — Clamping ship movement to screen bounds

### MDX sections
- The Ninth Bit: `$D010`
- Staying on Screen
- Clean Restarts
- Edge Cases Worth Fixing
- The Complete Code
- If It Doesn't Work
- Phase 1 Complete: What You've Built

---

## Implementation Sequencing Notes

- **Unit 8 depends on Unit 7** — adds to the `hit_enemy` block
- **Unit 9 restructures enemy logic** — `enemy_active` flag changes how the enemy section works; must be careful not to break the flash timer
- **Units 10–12 form a tight sequence** — death → game over → restart. Best implemented together without long gaps.
- **Unit 13 (title screen) refactors state** — changes `game_state` values, which ripples through the code. Plan the state values before writing.
- **Units 14–15 are paired** — lives counter and death feedback go together naturally
- **Unit 16 is cleanup** — should be implemented last as it fixes issues across all prior units

## Growing Complexity

By Unit 16, the assembly file will be significantly larger than Unit 7. Consider whether comments and section headers need updating as the file grows. The learner needs to navigate the code, so clear section markers matter.
