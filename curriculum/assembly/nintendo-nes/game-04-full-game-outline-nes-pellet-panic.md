# NES Game 4: Pellet Panic - Full 128-Unit Outline

**Platform:** Nintendo Entertainment System
**Game:** Pellet Panic
**Units:** 128 (8 phases × 16 units)
**Concept:** Pac-Man style maze game polished to commercial quality. Collect all pellets, avoid ghosts, grab power pills to turn the tables. Frantic, panic-inducing energy.

---

## Overview

Pellet Panic teaches tile-based maze navigation and enemy AI personalities. After physics-focused Games 1-3, learners now build AI that feels alive - ghosts with distinct behaviours that make each playthrough different.

**Key Learning Goals:**
- Tile-based maze structure (background tiles)
- Constrained corridor movement
- Ghost AI with personalities (chase, scatter, frightened)
- Power-up state changes
- Screen wrap-around
- Speed and difficulty progression
- APU audio for atmosphere

---

## Phase 1: Maze Foundation (Units 1-16)

### Unit 1: Maze Background
**Builds:** Draw maze using background tiles.
**Teaches:** Nametable for static playfield.
**Code pattern:**
```asm
; Maze tiles in pattern table
; 0 = empty (pellet floor)
; 1 = wall
; 2 = pellet
; 3 = power pellet
TILE_EMPTY  = $00
TILE_WALL   = $01
TILE_PELLET = $02
TILE_POWER  = $03

; Maze data: 28×31 tiles (standard Pac-Man size)
; Stored as RLE or raw bytes
maze_data:
    .byte 1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1
    .byte 1,2,2,2,2,2,2,2,2,2,2,2,2,1,1,2,2,2,2,2,2,2,2,2,2,2,2,1
    ; ... continue for all rows

draw_maze:
    ; Set PPU address to nametable
    lda #$20
    sta $2006
    lda #$00
    sta $2006

    ldx #0
@loop:
    lda maze_data,x
    sta $2007
    inx
    cpx #224            ; 28×8 rows at a time
    bne @loop
    ; ... continue for full maze
    rts
```
**If it doesn't work:** Maze garbled? Check PPU address increments correctly. Missing sections? Verify all rows are drawn.

---

### Unit 2: Wall Tiles
**Builds:** Create wall pattern graphics.
**Teaches:** Pattern table design.

---

### Unit 3: Maze Attributes
**Builds:** Colour the maze with attribute table.
**Teaches:** Attribute table for maze colours.
**Code pattern:**
```asm
; Attribute table: colour different areas
; Classic Pac-Man: blue walls, black floor
set_maze_attributes:
    lda #$23
    sta $2006
    lda #$C0
    sta $2006

    ldx #64             ; 64 bytes for full attribute area
    lda #%01010101      ; Palette 1 for all
@loop:
    sta $2007
    dex
    bne @loop
    rts
```

---

### Unit 4: Player Sprite
**Builds:** Pac-Man character as sprite.
**Teaches:** Animated player sprite.
**Code pattern:**
```asm
player_x:   .byte 112       ; Starting position (centre bottom)
player_y:   .byte 184
player_dir: .byte DIR_LEFT  ; Current direction
player_frame: .byte 0       ; Animation frame

; Player uses sprites 0-3 (2x2 sprite for 16x16 character)
update_player_sprite:
    lda player_y
    sta $0200           ; Sprite 0 Y
    sta $0204           ; Sprite 1 Y
    lda player_y
    clc
    adc #8
    sta $0208           ; Sprite 2 Y
    sta $020C           ; Sprite 3 Y

    ; Tile selection based on direction and frame
    lda player_dir
    asl
    asl                 ; * 4 tiles per direction
    clc
    adc player_frame
    tax
    lda player_tiles,x
    sta $0201           ; Sprite 0 tile
    ; ... set other sprite tiles

    ; X positions
    lda player_x
    sta $0203
    sta $020B
    clc
    adc #8
    sta $0207
    sta $020F
    rts
```
**If it doesn't work:** Sprite misaligned? Check 2x2 sprite positioning. Wrong animation? Verify tile table indexing.

---

### Unit 5: Player Movement
**Builds:** Move player with controller.
**Teaches:** Direction-based movement.
**Code pattern:**
```asm
PLAYER_SPEED = 1

update_player:
    ; Read desired direction from controller
    lda controller
    and #BUTTON_UP
    beq @check_down
    lda #DIR_UP
    sta desired_dir

@check_down:
    ; ... check all directions

    ; Try to move in desired direction
    lda desired_dir
    sta temp_dir
    jsr can_move
    beq @try_current    ; Can't move desired way

    ; Move in desired direction
    lda desired_dir
    sta player_dir
    jmp @do_move

@try_current:
    ; Continue in current direction if possible
    lda player_dir
    sta temp_dir
    jsr can_move
    beq @stopped

@do_move:
    jsr move_player

@stopped:
    rts
```
**If it doesn't work:** Not turning? Check desired direction is being set. Stuck? Verify can_move checks correctly.

---

### Unit 6: Tile Collision
**Builds:** Player can only move through corridors.
**Teaches:** Tile-based collision for maze.
**Code pattern:**
```asm
; Check if player can move in direction stored in temp_dir
; Returns Z=1 if blocked, Z=0 if can move
can_move:
    ; Get tile position player would move to
    lda player_x
    sta temp_x
    lda player_y
    sta temp_y

    ; Add movement based on direction
    lda temp_dir
    cmp #DIR_UP
    bne @not_up
    lda temp_y
    sec
    sbc #PLAYER_SPEED
    sta temp_y
    jmp @check

@not_up:
    ; ... handle other directions

@check:
    ; Convert pixel to tile
    lda temp_x
    lsr
    lsr
    lsr                 ; /8
    sta tile_x

    lda temp_y
    lsr
    lsr
    lsr
    sta tile_y

    ; Read tile from maze data
    ; offset = tile_y * 28 + tile_x
    lda tile_y
    ; ... multiply and add
    tax
    lda maze_data,x
    cmp #TILE_WALL      ; Is it a wall?
    rts                 ; Z=1 if wall
```
**If it doesn't work:** Walking through walls? Check pixel-to-tile conversion. Stuck in corridors? May need to check multiple tiles for sprite size.

---

### Unit 7: Smooth Cornering
**Builds:** Automatic alignment when turning.
**Teaches:** Corner assistance.
**Code pattern:**
```asm
; When turning, snap to grid for smooth corners
CORNER_THRESHOLD = 4

align_for_turn:
    ; If turning perpendicular, align to grid
    lda player_dir
    cmp #DIR_UP
    beq @vertical
    cmp #DIR_DOWN
    beq @vertical

    ; Horizontal movement - align Y
    lda player_y
    and #7              ; Position within tile
    cmp #CORNER_THRESHOLD
    bcc @snap_y_down
    cmp #8-CORNER_THRESHOLD
    bcs @snap_y_up
    rts

@snap_y_down:
    lda player_y
    and #$F8            ; Round down to tile
    sta player_y
    rts

@snap_y_up:
    lda player_y
    clc
    adc #8
    and #$F8            ; Round up to tile
    sta player_y
    rts

@vertical:
    ; Similar for X alignment
    ; ...
    rts
```
**If it doesn't work:** Missing turns? Increase threshold. Jumping weirdly? Check snap direction.

---

### Unit 8: Pellet Collection
**Builds:** Collecting pellets from maze.
**Teaches:** Modifying background during play.
**Code pattern:**
```asm
pellets_remaining: .byte 0

check_pellet:
    ; Get tile at player position
    jsr get_player_tile
    cmp #TILE_PELLET
    beq @collect_pellet
    cmp #TILE_POWER
    beq @collect_power
    rts

@collect_pellet:
    ; Remove pellet from maze data
    ldx current_tile_index
    lda #TILE_EMPTY
    sta maze_data,x

    ; Queue PPU update for VBlank
    jsr queue_tile_clear

    ; Add score
    lda #10
    jsr add_score

    ; Decrement counter
    dec pellets_remaining
    bne @done
    jmp level_complete

@collect_power:
    ; ... handle power pellet
    jsr start_frightened_mode

@done:
    rts
```
**If it doesn't work:** Pellet not disappearing? Ensure PPU update happens during VBlank. Count wrong? Verify initial pellet count.

---

### Unit 9: Power Pellets
**Builds:** Large pellets that frighten ghosts.
**Teaches:** Power-up state change.

---

### Unit 10: Screen Wrap
**Builds:** Player exits one side, appears on other.
**Teaches:** Wrap-around tunnel.
**Code pattern:**
```asm
; Check for tunnel wrap
TUNNEL_Y = 112          ; Y position of tunnel row
TUNNEL_LEFT = 0
TUNNEL_RIGHT = 224

check_wrap:
    ; Only wrap at tunnel row
    lda player_y
    cmp #TUNNEL_Y
    bne @no_wrap

    lda player_x
    cmp #TUNNEL_LEFT
    bcc @wrap_right
    cmp #TUNNEL_RIGHT
    bcs @wrap_left
    rts

@wrap_left:
    lda #TUNNEL_LEFT+8
    sta player_x
    rts

@wrap_right:
    lda #TUNNEL_RIGHT-8
    sta player_x
    rts

@no_wrap:
    rts
```

---

### Unit 11: Pellet Animation
**Builds:** Power pellets flash.
**Teaches:** Background animation via palette.

---

### Unit 12: Player Animation
**Builds:** Chomping mouth animation.
**Teaches:** Frame-based animation.

---

### Unit 13: Score Display
**Builds:** Show current score.
**Teaches:** HUD numerals.

---

### Unit 14: Lives Display
**Builds:** Show remaining lives.
**Teaches:** Life icons.

---

### Unit 15: Sound - Chomp
**Builds:** Waka-waka eating sound.
**Teaches:** Rhythmic sound effect.

---

### Unit 16: Phase 1 Polish
**Builds:** Playable maze with pellets.

---

## Phase 2: Ghost AI (Units 17-32)

### Unit 17: Ghost Sprites
**Builds:** Four ghost characters.
**Teaches:** Multiple sprite entities.
**Code pattern:**
```asm
; Ghost data structure
GHOST_X     = 0
GHOST_Y     = 1
GHOST_DIR   = 2
GHOST_MODE  = 3
GHOST_FRAME = 4
GHOST_SIZE  = 5

NUM_GHOSTS  = 4

ghost_data:
    .res NUM_GHOSTS * GHOST_SIZE

; Ghost starting positions
ghost_start_x: .byte 104, 112, 120, 128
ghost_start_y: .byte 88, 88, 88, 88
```

---

### Unit 18: Ghost Movement
**Builds:** Ghosts move through maze.
**Teaches:** AI pathfinding basics.

---

### Unit 19: Ghost Wall Collision
**Builds:** Ghosts navigate corridors.
**Teaches:** AI tile collision.

---

### Unit 20: Blinky AI - Chase
**Builds:** Red ghost targets player directly.
**Teaches:** Direct pursuit.
**Code pattern:**
```asm
; Blinky always targets player position
blinky_target:
    lda player_x
    sta target_x
    lda player_y
    sta target_y
    rts

; Choose direction toward target at intersection
choose_direction:
    ; At intersection, pick direction closest to target
    ; Calculate distance for each valid direction
    ; Never reverse (except in frightened mode)

    ; Check each direction
    ldx #DIR_UP
    jsr check_direction_valid
    beq @skip_up
    jsr calc_distance_up
    ; ... compare and store best
@skip_up:
    ; ... check other directions

    ; Set ghost to best direction
    lda best_dir
    sta ghost_data+GHOST_DIR,y
    rts
```
**If it doesn't work:** Not chasing? Check target is player position. Stuck at corners? Verify intersection detection.

---

### Unit 21: Pinky AI - Ambush
**Builds:** Pink ghost targets ahead of player.
**Teaches:** Predictive targeting.
**Code pattern:**
```asm
; Pinky targets 4 tiles ahead of player
PINKY_AHEAD = 32        ; 4 tiles × 8 pixels

pinky_target:
    lda player_x
    sta target_x
    lda player_y
    sta target_y

    ; Add offset based on player direction
    lda player_dir
    cmp #DIR_UP
    bne @not_up
    lda target_y
    sec
    sbc #PINKY_AHEAD
    sta target_y
    rts

@not_up:
    ; ... handle other directions
    rts
```

---

### Unit 22: Inky AI - Flank
**Builds:** Cyan ghost uses Blinky position.
**Teaches:** Coordinated AI.

---

### Unit 23: Clyde AI - Random
**Builds:** Orange ghost alternates chase/scatter.
**Teaches:** Distance-based behaviour.
**Code pattern:**
```asm
; Clyde: chase when far, scatter when close
CLYDE_THRESHOLD = 64    ; 8 tiles

clyde_target:
    ; Calculate distance to player
    jsr calc_player_distance
    cmp #CLYDE_THRESHOLD
    bcc @scatter

    ; Far away - chase like Blinky
    lda player_x
    sta target_x
    lda player_y
    sta target_y
    rts

@scatter:
    ; Close - go to corner
    lda #16
    sta target_x
    lda #224
    sta target_y
    rts
```

---

### Unit 24: Scatter Mode
**Builds:** Ghosts retreat to corners periodically.
**Teaches:** Mode switching.

---

### Unit 25: Chase/Scatter Timer
**Builds:** Alternate between modes on timer.
**Teaches:** Timed state changes.

---

### Unit 26: Frightened Mode
**Builds:** Ghosts run away when powered.
**Teaches:** State machine.
**Code pattern:**
```asm
frightened_timer: .byte 0

start_frightened_mode:
    ; Set all ghosts to frightened
    ldx #NUM_GHOSTS-1
@loop:
    lda #MODE_FRIGHTENED
    sta ghost_data+GHOST_MODE,x
    ; Reverse direction
    lda ghost_data+GHOST_DIR,x
    eor #2              ; Reverse (0↔2, 1↔3)
    sta ghost_data+GHOST_DIR,x
    dex
    bpl @loop

    ; Set timer
    lda #255
    sta frightened_timer
    rts
```

---

### Unit 27: Frightened Movement
**Builds:** Ghosts choose random directions.
**Teaches:** Random AI.

---

### Unit 28: Eating Ghosts
**Builds:** Player eats frightened ghosts.
**Teaches:** State-dependent collision.

---

### Unit 29: Ghost Eyes
**Builds:** Eaten ghosts return to base.
**Teaches:** Retreat AI.

---

### Unit 30: Ghost Respawn
**Builds:** Ghosts regenerate in ghost house.
**Teaches:** Respawn mechanics.

---

### Unit 31: Ghost House
**Builds:** Central pen where ghosts start.
**Teaches:** Spawn area.

---

### Unit 32: Phase 2 Polish
**Builds:** Four distinct ghost personalities.

---

## Phase 3: Game Systems (Units 33-48)

### Unit 33: Ghost Release Timer
**Builds:** Ghosts leave pen one by one.
**Teaches:** Staggered spawning.

---

### Unit 34: Pellet Counter Release
**Builds:** Ghost release based on pellets eaten.
**Teaches:** Progress-based spawning.

---

### Unit 35: Speed Progression
**Builds:** Everything speeds up as game progresses.
**Teaches:** Difficulty curves.

---

### Unit 36: Level Progression
**Builds:** Complete level, start new maze.
**Teaches:** Level resets.

---

### Unit 37: Intermissions
**Builds:** Cutscenes between levels.
**Teaches:** Story moments.

---

### Unit 38: Bonus Fruit
**Builds:** Fruit appears for bonus points.
**Teaches:** Bonus items.

---

### Unit 39: Fruit Variety
**Builds:** Different fruit per level.
**Teaches:** Level-specific items.

---

### Unit 40: Ghost Point Values
**Builds:** 200, 400, 800, 1600 for ghosts.
**Teaches:** Escalating rewards.

---

### Unit 41: Extra Life
**Builds:** 1-up at score threshold.
**Teaches:** Score-based rewards.

---

### Unit 42: High Score
**Builds:** Track best score.
**Teaches:** Persistent records.

---

### Unit 43: Kill Screen
**Builds:** Handle level 256 gracefully.
**Teaches:** Overflow handling.

---

### Unit 44: Ghost Speed Variation
**Builds:** Ghosts have different speeds.
**Teaches:** Entity variation.

---

### Unit 45: Tunnel Speed
**Builds:** Ghosts slow in tunnel.
**Teaches:** Zone-based speed.

---

### Unit 46: Energizer Duration
**Builds:** Power-up lasts shorter in later levels.
**Teaches:** Dynamic duration.

---

### Unit 47: Sound - Siren
**Builds:** Background siren during play.
**Teaches:** Ambient audio.

---

### Unit 48: Phase 3 Polish
**Builds:** Complete game systems.

---

## Phase 4: Audio (Units 49-64)

### Unit 49: Sound System
**Builds:** APU channel management.
**Teaches:** Audio architecture.

---

### Unit 50: Waka Sound
**Builds:** Classic eating sound.
**Teaches:** Rhythmic SFX.

---

### Unit 51: Siren Pitch
**Builds:** Siren changes with pellets remaining.
**Teaches:** Dynamic audio.

---

### Unit 52: Frightened Sound
**Builds:** Different sound during power mode.
**Teaches:** Mode-based audio.

---

### Unit 53: Ghost Eaten
**Builds:** Sound for eating ghost.
**Teaches:** Action feedback.

---

### Unit 54: Death Sound
**Builds:** Player death melody.
**Teaches:** Failure audio.

---

### Unit 55: Level Start
**Builds:** Beginning jingle.
**Teaches:** Introduction audio.

---

### Unit 56: Intermission Music
**Builds:** Music for cutscenes.
**Teaches:** Cinematic audio.

---

### Unit 57: Fruit Sound
**Builds:** Sound for collecting fruit.
**Teaches:** Bonus feedback.

---

### Unit 58: Extra Life Sound
**Builds:** 1-up jingle.
**Teaches:** Reward audio.

---

### Unit 59: Power Pellet Sound
**Builds:** Sound when collecting power.
**Teaches:** Power-up audio.

---

### Unit 60: Ghost Return
**Builds:** Sound for eyes returning.
**Teaches:** State audio.

---

### Unit 61: Title Music
**Builds:** Music for title screen.
**Teaches:** Menu music.

---

### Unit 62: High Score Music
**Builds:** Celebratory music.
**Teaches:** Achievement audio.

---

### Unit 63: Audio Balance
**Builds:** Volume levels correct.
**Teaches:** Audio mixing.

---

### Unit 64: Phase 4 Polish
**Builds:** Complete audio.

---

## Phase 5: Presentation (Units 65-80)

### Unit 65: Title Screen
**Builds:** Attractive start screen.
**Teaches:** Title design.

---

### Unit 66: Ghost Parade
**Builds:** Ghosts introduced with names.
**Teaches:** Character introduction.

---

### Unit 67: High Score Table
**Builds:** Top scores display.
**Teaches:** Score table.

---

### Unit 68: Name Entry
**Builds:** Enter initials.
**Teaches:** Text input.

---

### Unit 69: Instructions
**Builds:** How to play.
**Teaches:** Onboarding.

---

### Unit 70: Demo Mode
**Builds:** AI plays during attract.
**Teaches:** Attract mode.

---

### Unit 71: Ready Screen
**Builds:** "Ready!" before starting.
**Teaches:** Pre-game pause.

---

### Unit 72: Game Over
**Builds:** End screen.
**Teaches:** Game over handling.

---

### Unit 73: Player Animation
**Builds:** Death animation.
**Teaches:** Death sequence.

---

### Unit 74: Ghost Animation
**Builds:** Frightened flashing.
**Teaches:** Warning animation.

---

### Unit 75: Score Popups
**Builds:** Points appear on screen.
**Teaches:** Visual feedback.

---

### Unit 76: Level Indicator
**Builds:** Show current level.
**Teaches:** Progress display.

---

### Unit 77: Fruit Display
**Builds:** Collected fruits shown.
**Teaches:** Achievement display.

---

### Unit 78: Credits
**Builds:** Attribution screen.
**Teaches:** Credits.

---

### Unit 79: Two-Player Mode
**Builds:** Alternating play.
**Teaches:** Multiplayer.

---

### Unit 80: Phase 5 Polish
**Builds:** Complete presentation.

---

## Phase 6: Level Design (Units 81-96)

### Unit 81: Classic Maze
**Builds:** Traditional layout.
**Teaches:** Baseline design.

---

### Unit 82-85: Alternative Mazes
**Builds:** 4 different layouts.
**Teaches:** Design variety.

---

### Unit 86: Maze Selection
**Builds:** Different maze per set of levels.
**Teaches:** Level variety.

---

### Unit 87: Maze Balance
**Builds:** Fair ghost house placement.
**Teaches:** Balance design.

---

### Unit 88: Tunnel Placement
**Builds:** Strategic tunnel location.
**Teaches:** Escape route design.

---

### Unit 89: Power Pellet Placement
**Builds:** Strategic power positions.
**Teaches:** Power-up placement.

---

### Unit 90: Safe Spots
**Builds:** Areas where ghosts can't reach.
**Teaches:** Safe zone design.

---

### Unit 91: Difficulty Curve
**Builds:** Gradual challenge increase.
**Teaches:** Progression balance.

---

### Unit 92-94: Playtesting
**Builds:** Refine based on feedback.
**Teaches:** Iteration.

---

### Unit 95: Bonus Stages
**Builds:** Special challenge levels.
**Teaches:** Variety stages.

---

### Unit 96: Phase 6 Polish
**Builds:** Balanced levels.

---

## Phase 7: Optimisation (Units 97-112)

### Unit 97: Frame Rate
**Builds:** Consistent 60fps.
**Teaches:** Performance.

---

### Unit 98: AI Optimisation
**Builds:** Faster pathfinding.
**Teaches:** AI efficiency.

---

### Unit 99: PPU Updates
**Builds:** Efficient VBlank usage.
**Teaches:** PPU timing.

---

### Unit 100: Sprite Management
**Builds:** Handle 8-sprite limit.
**Teaches:** Sprite limits.

---

### Unit 101-104: Bug Fixes
**Builds:** Find and fix issues.
**Teaches:** Debugging.

---

### Unit 105-108: Balance
**Builds:** Fair, fun difficulty.
**Teaches:** Game balance.

---

### Unit 109-111: Polish
**Builds:** Visual consistency.
**Teaches:** Final polish.

---

### Unit 112: Phase 7 Complete
**Builds:** Stable, balanced game.

---

## Phase 8: Release (Units 113-128)

### Unit 113-116: Final Presentation
**Builds:** Title art, attract mode.
**Teaches:** Professional presentation.

---

### Unit 117-120: Testing
**Builds:** Emulator and hardware.
**Teaches:** Quality assurance.

---

### Unit 121-124: Final Polish
**Builds:** Easter eggs, cheats.
**Teaches:** Release preparation.

---

### Unit 125-127: Documentation
**Builds:** Manual concept.
**Teaches:** Documentation.

---

### Unit 128: Release
**Builds:** Final release.
**Teaches:** Shipping a game.

---

## Version History

- **1.0 (2026-01-18):** Initial 128-unit outline created.
