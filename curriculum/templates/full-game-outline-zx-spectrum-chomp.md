# ZX Spectrum Game 6: Chomp - Full 128-Unit Outline

**Platform:** Sinclair ZX Spectrum
**Game:** Chomp
**Units:** 128 (8 phases × 16 units)
**Concept:** Pac-Man style maze game polished to commercial quality. Collect dots, avoid ghosts, eat power pills to turn the tables. Each ghost has distinct personality AI.

---

## Overview

Chomp introduces constrained corridor movement and enemy AI personalities. After the strategic Ink War (Game 5), learners return to real-time action but with smarter enemies. The four ghosts each behave differently - teaching that AI variety creates emergent gameplay.

**Key Learning Goals:**
- Tile-based maze structure
- Constrained corridor movement (can only turn at junctions)
- Ghost AI personalities (Blinky, Pinky, Inky, Clyde patterns)
- Chase/scatter mode state machines
- Frightened mode reversal
- Screen wrap-around tunnels
- Power-up state changes

---

## Phase 1: Maze Foundation (Units 1-16)

### Unit 1: Maze Display
**Builds:** Draw maze using character graphics.
**Teaches:** Tile-based maze layout.
**Code pattern:**
```z80
; Maze data: 28x31 tiles
; 0=empty, 1=wall, 2=dot, 3=power pill, 4=tunnel
maze_data:
    defb 1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1
    defb 1,2,2,2,2,2,2,2,2,2,2,2,2,1,1,2,2,2,2,2,2,2,2,2,2,2,2,1
    defb 1,2,1,1,1,1,2,1,1,1,1,1,2,1,1,2,1,1,1,1,1,2,1,1,1,1,2,1
    defb 1,3,1,1,1,1,2,1,1,1,1,1,2,1,1,2,1,1,1,1,1,2,1,1,1,1,3,1
    ; ... continue for 31 rows

; Character codes for maze elements
CHAR_WALL = 128         ; Solid block
CHAR_DOT = 46           ; Period
CHAR_POWER = 42         ; Asterisk
CHAR_EMPTY = 32         ; Space

draw_maze:
    ld hl,maze_data
    ld de,$4000         ; Screen start
    ld b,31             ; Rows
draw_row:
    push bc
    ld b,28             ; Columns
draw_tile:
    ld a,(hl)
    call get_char_for_tile
    ld (de),a
    inc hl
    inc de
    djnz draw_tile
    ; Move to next row
    pop bc
    djnz draw_row
    ret
```
**If it doesn't work:** Maze garbled? Check screen address calculation. Wrong characters? Verify character code mapping.

---

### Unit 2: Player Sprite
**Builds:** Pac-Man character.
**Teaches:** UDG for player.

---

### Unit 3: Player Movement
**Builds:** Move with keyboard/joystick.
**Teaches:** 4-way movement.
**Code pattern:**
```z80
player_x:       defb 14     ; Tile position
player_y:       defb 23     ; Starting position
player_dir:     defb 0      ; 0=right,1=down,2=left,3=up
next_dir:       defb 0      ; Buffered direction

MOVE_RIGHT equ 0
MOVE_DOWN  equ 1
MOVE_LEFT  equ 2
MOVE_UP    equ 3

; Direction vectors
dir_x:  defb 1, 0, -1, 0
dir_y:  defb 0, 1, 0, -1

update_player:
    ; Check if can turn to buffered direction
    ld a,(next_dir)
    call can_move_dir
    jr z,try_current
    ; Can turn - change direction
    ld a,(next_dir)
    ld (player_dir),a

try_current:
    ; Try to move in current direction
    ld a,(player_dir)
    call can_move_dir
    ret z               ; Blocked

    ; Move player
    ld a,(player_dir)
    ld c,a
    ld b,0
    ld hl,dir_x
    add hl,bc
    ld a,(player_x)
    add a,(hl)
    ld (player_x),a

    ld hl,dir_y
    add hl,bc
    ld a,(player_y)
    add a,(hl)
    ld (player_y),a
    ret
```

---

### Unit 4: Wall Collision
**Builds:** Can't move through walls.
**Teaches:** Tile collision.
**Code pattern:**
```z80
; Check if can move in direction A
; Returns Z if blocked, NZ if can move
can_move_dir:
    push af
    ; Calculate target tile
    ld c,a
    ld b,0

    ld hl,dir_x
    add hl,bc
    ld a,(player_x)
    add a,(hl)
    ld d,a              ; Target X

    ld hl,dir_y
    add hl,bc
    ld a,(player_y)
    add a,(hl)
    ld e,a              ; Target Y

    ; Get tile at target
    call get_maze_tile
    cp 1                ; Wall?
    pop af
    ret                 ; Z if wall, NZ if not
```

---

### Unit 5: Dot Collection
**Builds:** Eating dots.
**Teaches:** Pickup mechanics.

---

### Unit 6: Dot Counter
**Builds:** Track remaining dots.
**Teaches:** Win condition.

---

### Unit 7: Power Pills
**Builds:** Large dots at corners.
**Teaches:** Power-up placement.

---

### Unit 8: Score Display
**Builds:** Points on screen.
**Teaches:** HUD.

---

### Unit 9: Lives Display
**Builds:** Remaining lives.
**Teaches:** Life tracking.

---

### Unit 10: Single Ghost
**Builds:** One enemy ghost.
**Teaches:** Enemy basics.

---

### Unit 11: Ghost Movement
**Builds:** Ghost navigates maze.
**Teaches:** AI movement.

---

### Unit 12: Ghost-Player Collision
**Builds:** Ghost catches player.
**Teaches:** Damage collision.

---

### Unit 13: Death Animation
**Builds:** Player death sequence.
**Teaches:** Death handling.

---

### Unit 14: Respawn
**Builds:** Player returns after death.
**Teaches:** Respawn mechanics.

---

### Unit 15: Basic Sound
**Builds:** Beeper effects.
**Teaches:** Audio feedback.

---

### Unit 16: Phase 1 Polish
**Builds:** Basic game working.

---

## Phase 2: Ghost AI (Units 17-32)

### Unit 17: Blinky AI
**Builds:** Red ghost - direct chase.
**Teaches:** Chase behaviour.
**Code pattern:**
```z80
; Blinky: targets player's current tile
; "Shadow" - always chasing directly

blinky_target:
    ; Target = player position
    ld a,(player_x)
    ld (blinky_target_x),a
    ld a,(player_y)
    ld (blinky_target_y),a
    ret

; Ghost movement toward target
move_ghost_toward_target:
    ; At junction, choose direction that minimizes
    ; distance to target tile
    ; Never reverse unless mode change

    ; Calculate distance for each valid direction
    ; Choose smallest
    ; ... pathfinding logic
    ret
```
**If it doesn't work:** Ghost not chasing? Check target is updated each frame. Going through walls? Verify wall check in pathfinding.

---

### Unit 18: Pinky AI
**Builds:** Pink ghost - ambush.
**Teaches:** Predictive AI.
**Code pattern:**
```z80
; Pinky: targets 4 tiles ahead of player
; "Speedy" - tries to ambush

pinky_target:
    ; Target = 4 tiles ahead of player direction
    ld a,(player_dir)
    ld c,a
    ld b,0

    ld hl,dir_x
    add hl,bc
    ld a,(hl)
    add a,a             ; *2
    add a,a             ; *4
    ld b,a
    ld a,(player_x)
    add a,b
    ld (pinky_target_x),a

    ; Same for Y
    ld hl,dir_y
    add hl,bc
    ld a,(hl)
    add a,a
    add a,a
    ld b,a
    ld a,(player_y)
    add a,b
    ld (pinky_target_y),a
    ret
```

---

### Unit 19: Inky AI
**Builds:** Cyan ghost - flanker.
**Teaches:** Complex targeting.
**Code pattern:**
```z80
; Inky: uses Blinky's position in calculation
; Target = 2 tiles ahead of player, then
; vector from Blinky doubled

inky_target:
    ; Get 2 tiles ahead of player
    ; ... calculate intermediate point

    ; Get vector from Blinky to intermediate
    ld a,(intermediate_x)
    ld b,a
    ld a,(blinky_x)
    sub b
    neg                 ; Reverse direction
    add a,a             ; Double it
    add a,(intermediate_x)
    ld (inky_target_x),a
    ; Similar for Y
    ret
```

---

### Unit 20: Clyde AI
**Builds:** Orange ghost - random/shy.
**Teaches:** Conditional AI.
**Code pattern:**
```z80
; Clyde: chases when far, runs when close
; "Pokey" - unpredictable

clyde_target:
    ; Calculate distance to player
    ld a,(clyde_x)
    ld b,a
    ld a,(player_x)
    sub b
    jp p,pos_x
    neg
pos_x:
    ld c,a              ; |dx|

    ld a,(clyde_y)
    ld b,a
    ld a,(player_y)
    sub b
    jp p,pos_y
    neg
pos_y:
    add a,c             ; Manhattan distance

    cp 8                ; If distance >= 8, chase
    jr nc,clyde_chase

    ; Too close - target scatter corner
    ld a,0
    ld (clyde_target_x),a
    ld a,31
    ld (clyde_target_y),a
    ret

clyde_chase:
    ; Target player directly
    ld a,(player_x)
    ld (clyde_target_x),a
    ld a,(player_y)
    ld (clyde_target_y),a
    ret
```

---

### Unit 21: Scatter Mode
**Builds:** Ghosts retreat to corners.
**Teaches:** Mode switching.

---

### Unit 22: Chase/Scatter Timer
**Builds:** Automatic mode switching.
**Teaches:** Timed state changes.

---

### Unit 23: Frightened Mode
**Builds:** Power pill makes ghosts vulnerable.
**Teaches:** Power-up effects.

---

### Unit 24: Ghost Eating
**Builds:** Catch frightened ghosts.
**Teaches:** Role reversal.

---

### Unit 25: Ghost Eyes
**Builds:** Eaten ghosts return to base.
**Teaches:** Respawn AI.

---

### Unit 26: Ghost House
**Builds:** Ghosts start in pen.
**Teaches:** Spawn area.

---

### Unit 27: Ghost Release Timer
**Builds:** Ghosts leave pen over time.
**Teaches:** Staggered release.

---

### Unit 28: Tunnel Wrapping
**Builds:** Side tunnels wrap screen.
**Teaches:** Screen wrap.

---

### Unit 29: Ghost Speed
**Builds:** Different speeds per state.
**Teaches:** Speed variation.

---

### Unit 30: Frightened Flashing
**Builds:** Ghosts flash before normal.
**Teaches:** Warning feedback.

---

### Unit 31: AI Difficulty
**Builds:** Harder AI over levels.
**Teaches:** Progressive challenge.

---

### Unit 32: Phase 2 Polish
**Builds:** Complete ghost AI.

---

## Phase 3: Level System (Units 33-48)

### Unit 33: Level Counter
**Builds:** Track current level.
**Teaches:** Level tracking.

---

### Unit 34: Level Complete
**Builds:** Clear all dots to advance.
**Teaches:** Level completion.

---

### Unit 35: Level Transition
**Builds:** Flash screen between levels.
**Teaches:** Transition effects.

---

### Unit 36: Speed Progression
**Builds:** Faster each level.
**Teaches:** Difficulty scaling.

---

### Unit 37: Fruit Bonus
**Builds:** Bonus fruit appears.
**Teaches:** Bonus items.

---

### Unit 38: Fruit Variety
**Builds:** Different fruit per level.
**Teaches:** Level theming.

---

### Unit 39: Fruit Timer
**Builds:** Fruit disappears after time.
**Teaches:** Timed bonuses.

---

### Unit 40: Ghost Mode Timing
**Builds:** Shorter scatter at higher levels.
**Teaches:** Timer progression.

---

### Unit 41: Power Pill Duration
**Builds:** Shorter fright at higher levels.
**Teaches:** Balance progression.

---

### Unit 42: Maze Variants
**Builds:** Different maze layouts.
**Teaches:** Level variety.

---

### Unit 43: Ghost Cruise Elroy
**Builds:** Blinky speeds up when few dots remain.
**Teaches:** Dynamic difficulty.

---

### Unit 44: Intermissions
**Builds:** Cut-scenes between acts.
**Teaches:** Story breaks.

---

### Unit 45: Kill Screen
**Builds:** Handle level 256 overflow.
**Teaches:** Edge cases.

---

### Unit 46: Level Select (Debug)
**Builds:** Jump to any level.
**Teaches:** Dev tools.

---

### Unit 47: Level Statistics
**Builds:** Time, dots, ghosts eaten.
**Teaches:** Stats tracking.

---

### Unit 48: Phase 3 Polish
**Builds:** Complete level system.

---

## Phase 4: Audio (Units 49-64)

### Unit 49: Waka-Waka Sound
**Builds:** Dot eating sound.
**Teaches:** Rhythmic audio.

---

### Unit 50: Power Pill Sound
**Builds:** Power-up collection.
**Teaches:** Power audio.

---

### Unit 51: Ghost Eat Sound
**Builds:** Catching ghost.
**Teaches:** Success audio.

---

### Unit 52: Death Sound
**Builds:** Player death.
**Teaches:** Failure audio.

---

### Unit 53: Siren Sound
**Builds:** Background tension.
**Teaches:** Ambient audio.

---

### Unit 54: Frightened Sound
**Builds:** Different siren when powered.
**Teaches:** State audio.

---

### Unit 55: Level Start Jingle
**Builds:** Ready tune.
**Teaches:** Fanfare.

---

### Unit 56: Fruit Appear Sound
**Builds:** Bonus available.
**Teaches:** Alert audio.

---

### Unit 57: Extra Life Sound
**Builds:** 1-up at 10,000.
**Teaches:** Reward audio.

---

### Unit 58: Intermission Music
**Builds:** Cut-scene music.
**Teaches:** Scene music.

---

### Unit 59-63: Audio Polish
**Builds:** Balance and timing.
**Teaches:** Audio refinement.

---

### Unit 64: Phase 4 Polish
**Builds:** Complete audio.

---

## Phase 5: Presentation (Units 65-80)

### Unit 65: Title Screen
**Builds:** Attractive start.
**Teaches:** Title design.

---

### Unit 66: Demo Mode
**Builds:** AI plays itself.
**Teaches:** Attract mode.

---

### Unit 67: High Score Table
**Builds:** Best scores.
**Teaches:** Score table.

---

### Unit 68: Name Entry
**Builds:** Enter initials.
**Teaches:** Text input.

---

### Unit 69: Ghost Names
**Builds:** Show personalities.
**Teaches:** Character display.

---

### Unit 70: Instructions
**Builds:** How to play.
**Teaches:** Onboarding.

---

### Unit 71: Colour Scheme
**Builds:** Classic Pac-Man colours.
**Teaches:** Palette design.

---

### Unit 72: Smooth Animation
**Builds:** Character animation.
**Teaches:** Animation polish.

---

### Unit 73: Score Pop-ups
**Builds:** Points appear briefly.
**Teaches:** Score feedback.

---

### Unit 74: Pause Menu
**Builds:** Mid-game pause.
**Teaches:** Pause.

---

### Unit 75: Game Over
**Builds:** End screen.
**Teaches:** Game over.

---

### Unit 76-79: Visual Polish
**Builds:** Refinements.
**Teaches:** Quality.

---

### Unit 80: Phase 5 Polish
**Builds:** Complete presentation.

---

## Phase 6: Features (Units 81-96)

### Unit 81: Two-Player Mode
**Builds:** Alternating turns.
**Teaches:** Multiplayer.

---

### Unit 82: Cooperative Mode
**Builds:** Two Pac-Men (alternating control).
**Teaches:** Co-op design.

---

### Unit 83: Speed Options
**Builds:** Game speed selection.
**Teaches:** Options.

---

### Unit 84: Starting Level
**Builds:** Begin at higher level.
**Teaches:** Difficulty options.

---

### Unit 85: Practice Mode
**Builds:** Infinite lives.
**Teaches:** Practice.

---

### Unit 86: Ghost AI Display
**Builds:** Show AI targets (debug).
**Teaches:** AI visualisation.

---

### Unit 87: Statistics
**Builds:** Career statistics.
**Teaches:** Long-term tracking.

---

### Unit 88: Achievements
**Builds:** Special accomplishments.
**Teaches:** Achievements.

---

### Unit 89-95: Polish
**Builds:** Refinements.
**Teaches:** Quality.

---

### Unit 96: Phase 6 Polish
**Builds:** Complete features.

---

## Phase 7: Optimisation (Units 97-112)

### Unit 97: Frame Rate
**Builds:** Consistent speed.
**Teaches:** Performance.

---

### Unit 98: AI Efficiency
**Builds:** Fast pathfinding.
**Teaches:** AI optimisation.

---

### Unit 99: Collision Speed
**Builds:** Efficient collision.
**Teaches:** Collision optimisation.

---

### Unit 100-104: Balance
**Builds:** Fair difficulty.
**Teaches:** Game balance.

---

### Unit 105-108: Bug Fixes
**Builds:** Fix issues.
**Teaches:** Debugging.

---

### Unit 109-111: Polish
**Builds:** Final refinements.
**Teaches:** Quality.

---

### Unit 112: Phase 7 Complete
**Builds:** Stable game.

---

## Phase 8: Release (Units 113-128)

### Unit 113-116: Final Testing
**Builds:** Thorough testing.
**Teaches:** QA.

---

### Unit 117-120: Compatibility
**Builds:** Test on all Spectrum models.
**Teaches:** Compatibility.

---

### Unit 121-124: Final Polish
**Builds:** Last fixes.
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
