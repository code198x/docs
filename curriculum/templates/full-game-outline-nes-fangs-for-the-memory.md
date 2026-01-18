# NES Game 6: Fangs for the Memory - Full 128-Unit Outline

**Platform:** Nintendo Entertainment System
**Game:** Fangs for the Memory
**Units:** 128 (8 phases × 16 units)
**Concept:** Snake game with a vampire bat theme. Eat food, grow longer, don't hit yourself or the walls. The ring buffer data structure taught through gameplay.

---

## Overview

Fangs for the Memory teaches the ring buffer - a fundamental data structure - through snake gameplay. After the complexity of Crypt Crawler, this simpler game lets concepts consolidate while introducing an important programming pattern used in audio, graphics, and game programming.

**Key Learning Goals:**
- Ring buffer data structure
- Grid-based movement
- Self-collision detection
- Growing entity management
- Food spawning
- Multiple game modes

---

## Phase 1: Snake Foundation (Units 1-16)

### Unit 1: Game Grid
**Builds:** Background grid display.
**Teaches:** Nametable setup for grid game.
**Code pattern:**
```asm
; Grid: 30x26 playable tiles (leaving border)
; Draw border around edge
GRID_WIDTH  = 30
GRID_HEIGHT = 26

draw_border:
    ; Top row
    lda #$20
    sta $2006
    lda #$00
    sta $2006

    lda #TILE_CORNER_TL
    sta $2007
    ldx #30
@top:
    lda #TILE_BORDER_H
    sta $2007
    dex
    bne @top
    lda #TILE_CORNER_TR
    sta $2007

    ; ... continue for sides and bottom
    rts
```
**If it doesn't work:** Border wrong? Check nametable addresses. Missing corners? Verify corner tile indices.

---

### Unit 2: Snake Head
**Builds:** Single tile snake.
**Teaches:** Sprite or tile for head.

---

### Unit 3: Snake Movement
**Builds:** Head moves each step.
**Teaches:** Grid movement.
**Code pattern:**
```asm
snake_x:        .byte 15    ; Head X (grid coords)
snake_y:        .byte 13    ; Head Y
snake_dir:      .byte 0     ; 0=right,1=down,2=left,3=up

; Direction deltas
dir_dx: .byte 1, 0, -1, 0
dir_dy: .byte 0, 1, 0, -1

move_snake:
    ldx snake_dir

    ; Move head
    lda snake_x
    clc
    adc dir_dx,x
    sta snake_x

    lda snake_y
    clc
    adc dir_dy,x
    sta snake_y
    rts
```

---

### Unit 4: Direction Control
**Builds:** Change direction with d-pad.
**Teaches:** Input handling.
**Code pattern:**
```asm
; Can't reverse direction (would hit self)
update_direction:
    lda controller
    and #BUTTON_RIGHT
    beq @check_down
    lda snake_dir
    cmp #2              ; Currently left?
    beq @done           ; Can't reverse
    lda #0
    sta snake_dir
    rts

@check_down:
    lda controller
    and #BUTTON_DOWN
    beq @check_left
    lda snake_dir
    cmp #3              ; Currently up?
    beq @done
    lda #1
    sta snake_dir
    rts

    ; ... check left and up
@done:
    rts
```
**If it doesn't work:** Can reverse? Add direction validation. Unresponsive? Check controller reading.

---

### Unit 5: Wall Collision
**Builds:** Die when hitting wall.
**Teaches:** Boundary collision.

---

### Unit 6: Ring Buffer Concept
**Builds:** Snake body storage.
**Teaches:** Ring buffer data structure.
**Code pattern:**
```asm
; Ring buffer for snake body positions
; Head index moves forward, tail follows
; When growing, tail doesn't move for one step
MAX_LENGTH = 100

snake_body_x:   .res MAX_LENGTH
snake_body_y:   .res MAX_LENGTH
snake_head_idx: .byte 0     ; Index of head in buffer
snake_tail_idx: .byte 0     ; Index of tail in buffer
snake_length:   .byte 3     ; Current length

; Add new head position
add_segment:
    ; Move head index forward (wrap at MAX_LENGTH)
    lda snake_head_idx
    clc
    adc #1
    cmp #MAX_LENGTH
    bcc @no_wrap
    lda #0
@no_wrap:
    sta snake_head_idx

    ; Store new position
    tax
    lda snake_x
    sta snake_body_x,x
    lda snake_y
    sta snake_body_y,x
    rts

; Remove tail (unless growing)
remove_tail:
    lda growing
    bne @skip           ; Don't remove if growing

    ; Clear old tail tile
    ldx snake_tail_idx
    lda snake_body_x,x
    sta temp_x
    lda snake_body_y,x
    sta temp_y
    jsr clear_grid_tile

    ; Move tail index forward
    lda snake_tail_idx
    clc
    adc #1
    cmp #MAX_LENGTH
    bcc @no_wrap
    lda #0
@no_wrap:
    sta snake_tail_idx

@skip:
    lda #0
    sta growing
    rts
```
**If it doesn't work:** Body not following? Check ring buffer indices. Gaps in snake? Verify add/remove order.

---

### Unit 7: Body Segments
**Builds:** Multi-segment snake.
**Teaches:** Ring buffer usage.

---

### Unit 8: Food Item
**Builds:** Food appears on grid.
**Teaches:** Random placement.

---

### Unit 9: Food Collision
**Builds:** Eating food.
**Teaches:** Pickup detection.

---

### Unit 10: Snake Growth
**Builds:** Get longer when eating.
**Teaches:** Growth mechanic.

---

### Unit 11: Self Collision
**Builds:** Die when hitting body.
**Teaches:** Self-intersection check.
**Code pattern:**
```asm
; Check if head position hits any body segment
check_self_collision:
    lda snake_tail_idx
    sta temp_idx

@loop:
    ; Skip head itself
    lda temp_idx
    cmp snake_head_idx
    beq @next

    ; Check if head matches this segment
    tax
    lda snake_body_x,x
    cmp snake_x
    bne @next
    lda snake_body_y,x
    cmp snake_y
    bne @next

    ; Collision!
    lda #1
    rts

@next:
    ; Move to next segment
    lda temp_idx
    clc
    adc #1
    cmp #MAX_LENGTH
    bcc @no_wrap
    lda #0
@no_wrap:
    sta temp_idx

    ; Have we checked all segments?
    cmp snake_head_idx
    bne @loop

    ; No collision
    lda #0
    rts
```

---

### Unit 12: Score Display
**Builds:** Points on screen.
**Teaches:** Score tracking.

---

### Unit 13: Lives System
**Builds:** Multiple lives.
**Teaches:** Life tracking.

---

### Unit 14: Game Over
**Builds:** Death handling.
**Teaches:** Game over state.

---

### Unit 15: Sound Effects
**Builds:** Eat and death sounds.
**Teaches:** APU basics.

---

### Unit 16: Phase 1 Polish
**Builds:** Basic snake working.

---

## Phase 2: Game Feel (Units 17-32)

### Unit 17: Movement Timing
**Builds:** Snake moves at intervals.
**Teaches:** Step timing.
**Code pattern:**
```asm
; Snake moves every N frames
move_timer:     .byte 0
MOVE_DELAY = 8          ; Frames between moves

update_snake:
    inc move_timer
    lda move_timer
    cmp #MOVE_DELAY
    bcc @done           ; Not time yet

    lda #0
    sta move_timer

    ; Do snake movement
    jsr move_snake
    jsr check_collisions
    jsr remove_tail
    jsr draw_snake

@done:
    rts
```

---

### Unit 18: Speed Progression
**Builds:** Faster as snake grows.
**Teaches:** Dynamic speed.

---

### Unit 19: Input Buffering
**Builds:** Queue direction changes.
**Teaches:** Input buffer.

---

### Unit 20: Smooth Animation
**Builds:** Interpolate between steps.
**Teaches:** Visual smoothing.

---

### Unit 21: Snake Sprites
**Builds:** Sprites for head/body.
**Teaches:** Sprite-based snake.

---

### Unit 22: Body Graphics
**Builds:** Different tiles for turns.
**Teaches:** Segment graphics.

---

### Unit 23: Head Animation
**Builds:** Animated head.
**Teaches:** Direction-based graphics.

---

### Unit 24: Tail Animation
**Builds:** Animated tail end.
**Teaches:** Tail graphics.

---

### Unit 25: Food Animation
**Builds:** Food pulses/moves.
**Teaches:** Item animation.

---

### Unit 26: Death Animation
**Builds:** Snake shrinks on death.
**Teaches:** Death effect.

---

### Unit 27: Growth Animation
**Builds:** Flash when eating.
**Teaches:** Feedback.

---

### Unit 28: Screen Shake
**Builds:** Shake on death.
**Teaches:** Impact effect.

---

### Unit 29: Score Pop-up
**Builds:** Points appear at food.
**Teaches:** Score feedback.

---

### Unit 30: Combo Display
**Builds:** Show rapid eat bonus.
**Teaches:** Combo feedback.

---

### Unit 31: Length Display
**Builds:** Show current length.
**Teaches:** Status display.

---

### Unit 32: Phase 2 Polish
**Builds:** Great game feel.

---

## Phase 3: Game Modes (Units 33-48)

### Unit 33: Classic Mode
**Builds:** Standard snake.
**Teaches:** Core mode.

---

### Unit 34: Level Mode
**Builds:** Discrete levels with targets.
**Teaches:** Level structure.

---

### Unit 35: Level Obstacles
**Builds:** Walls within levels.
**Teaches:** Obstacle placement.

---

### Unit 36: Level Data
**Builds:** Level definitions.
**Teaches:** Level storage.

---

### Unit 37: Maze Levels
**Builds:** Complex mazes.
**Teaches:** Maze design.

---

### Unit 38: Speed Mode
**Builds:** Fast-paced variant.
**Teaches:** Speed challenge.

---

### Unit 39: Survival Mode
**Builds:** Endless with hazards.
**Teaches:** Survival mechanics.

---

### Unit 40: Time Attack
**Builds:** Reach length in time limit.
**Teaches:** Timed challenge.

---

### Unit 41: Shrinking Arena
**Builds:** Walls close in.
**Teaches:** Dynamic arena.

---

### Unit 42: Multiple Food
**Builds:** Several food items.
**Teaches:** Multi-item.

---

### Unit 43: Special Food
**Builds:** Bonus items.
**Teaches:** Item variety.

---

### Unit 44: Power-Ups
**Builds:** Speed boost, invincibility.
**Teaches:** Power-up system.

---

### Unit 45: Mode Select
**Builds:** Choose game mode.
**Teaches:** Mode selection.

---

### Unit 46: Difficulty Settings
**Builds:** Easy/Medium/Hard.
**Teaches:** Difficulty options.

---

### Unit 47: Mode Statistics
**Builds:** Per-mode high scores.
**Teaches:** Mode tracking.

---

### Unit 48: Phase 3 Polish
**Builds:** Complete mode variety.

---

## Phase 4: Audio (Units 49-64)

### Unit 49: Movement Sound
**Builds:** Step sounds.
**Teaches:** Movement audio.

---

### Unit 50: Eat Sound
**Builds:** Food collection.
**Teaches:** Pickup audio.

---

### Unit 51: Death Sound
**Builds:** Collision sound.
**Teaches:** Failure audio.

---

### Unit 52: Level Complete
**Builds:** Success fanfare.
**Teaches:** Victory audio.

---

### Unit 53: Power-Up Sound
**Builds:** Collection sound.
**Teaches:** Power-up audio.

---

### Unit 54: Warning Sound
**Builds:** Near wall alert.
**Teaches:** Warning audio.

---

### Unit 55: Music - Title
**Builds:** Title theme.
**Teaches:** APU music.

---

### Unit 56: Music - Gameplay
**Builds:** In-game music.
**Teaches:** Game music.

---

### Unit 57: Music - Intensity
**Builds:** Faster music as longer.
**Teaches:** Dynamic music.

---

### Unit 58-63: Audio Polish
**Builds:** Balance and variety.
**Teaches:** Audio refinement.

---

### Unit 64: Phase 4 Polish
**Builds:** Complete audio.

---

## Phase 5: Presentation (Units 65-80)

### Unit 65: Title Screen
**Builds:** Vampire bat theme.
**Teaches:** Title design.

---

### Unit 66: Mode Select Screen
**Builds:** Choose mode.
**Teaches:** Menu design.

---

### Unit 67: High Score Table
**Builds:** Best scores per mode.
**Teaches:** Score table.

---

### Unit 68: Name Entry
**Builds:** Enter initials.
**Teaches:** Text input.

---

### Unit 69: Instructions
**Builds:** How to play.
**Teaches:** Tutorial.

---

### Unit 70: Visual Theme
**Builds:** Bat/gothic aesthetic.
**Teaches:** Theme design.

---

### Unit 71: Background Art
**Builds:** Level backgrounds.
**Teaches:** Background design.

---

### Unit 72: Pause Menu
**Builds:** Mid-game pause.
**Teaches:** Pause screen.

---

### Unit 73: Game Over Screen
**Builds:** Death statistics.
**Teaches:** End screen.

---

### Unit 74: Credits
**Builds:** Attribution.
**Teaches:** Credits.

---

### Unit 75-79: Visual Polish
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

### Unit 82: Versus Mode
**Builds:** Two snakes, one arena.
**Teaches:** Competitive.

---

### Unit 83: Versus AI
**Builds:** Play against CPU snake.
**Teaches:** AI opponent.

---

### Unit 84: Password System
**Builds:** Save progress.
**Teaches:** Passwords.

---

### Unit 85: Achievements
**Builds:** Special accomplishments.
**Teaches:** Achievements.

---

### Unit 86: Statistics
**Builds:** Career stats.
**Teaches:** Long-term tracking.

---

### Unit 87: Custom Levels
**Builds:** Level editor.
**Teaches:** Editor mode.

---

### Unit 88-95: Polish
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

### Unit 98: Ring Buffer Efficiency
**Builds:** Fast buffer operations.
**Teaches:** Data structure optimisation.

---

### Unit 99: Collision Speed
**Builds:** Fast self-check.
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

### Unit 113-116: Testing
**Builds:** Thorough testing.
**Teaches:** QA.

---

### Unit 117-120: ROM Creation
**Builds:** Final ROM.
**Teaches:** Build process.

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
