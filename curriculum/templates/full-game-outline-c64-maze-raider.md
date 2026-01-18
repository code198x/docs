# C64 Game 3: Maze Raider - Full 128-Unit Outline

**Platform:** Commodore 64
**Game:** Maze Raider
**Units:** 128 (8 phases × 16 units)
**Concept:** Pac-Man style maze chase. Navigate corridors, collect pellets, avoid ghosts. When you grab a power pill, the tables turn.

---

## Overview

Maze Raider teaches character-based graphics and AI pathfinding. After learning sprites in Games 1-2, learners now master custom character sets for building tile-based worlds. The ghost AI introduces pathfinding - a fundamental skill for all future games.

**Key Learning Goals:**
- Custom character sets (redefining the C64's characters)
- Tile-based map data and rendering
- Ghost AI with personality (chase, scatter, frightened)
- Pathfinding introduction (A* concepts)
- State machines for game entities
- Screen-based level design

---

## Phase 1: Maze Foundation (Units 1-16)

### Unit 1: The Empty Maze
**Builds:** Static maze displayed on screen using default characters.
**Teaches:** Screen memory basics, using existing characters for walls.
**Code pattern:**
```asm
; Screen memory starts at $0400
; Use @ for walls, space for paths
SCREEN = $0400

draw_maze:
    ldx #0
.loop:
    lda maze_data,x
    sta SCREEN,x
    inx
    cpx #250        ; First 250 bytes
    bne .loop
    rts

maze_data:
    !byte 64,64,64,64,64,64  ; @ = wall
    !byte 64,32,32,32,32,64  ; spaces = path
    ; ... continue for 25 rows
```
**If it doesn't work:** Maze not visible? Check screen memory address. Garbage characters? Verify maze_data bytes match character codes.

---

### Unit 2: Custom Wall Characters
**Builds:** Maze with custom wall graphics (proper corners, edges).
**Teaches:** Custom character sets, VIC-II character pointer.
**Code pattern:**
```asm
; Point VIC to custom charset at $3000
; Character memory = $3000-$37FF (2KB)
CHAR_BASE = $3000

setup_charset:
    lda #%00011100  ; Charset at $3000
    sta $d018
    rts

; Define wall corner (character 0)
corner_char:
    !byte %11111111
    !byte %10000000
    !byte %10000000
    !byte %10000000
    !byte %10000000
    !byte %10000000
    !byte %10000000
    !byte %10000000
```
**If it doesn't work:** Garbage on screen? Character pointer in $D018 is wrong. Chars look wrong? Check bit patterns - remember 8 bytes per character.

---

### Unit 3: Player Character
**Builds:** Player "mouth" character that moves with joystick.
**Teaches:** Player position tracking, character animation basics.
**Code pattern:**
```asm
player_x:   !byte 5     ; Character column
player_y:   !byte 5     ; Character row

; Custom player characters (open/closed mouth)
player_open:
    !byte %00111100
    !byte %01111110
    !byte %11111000
    !byte %11110000
    !byte %11110000
    !byte %11111000
    !byte %01111110
    !byte %00111100

update_player:
    ; Erase old position
    jsr get_screen_pos
    lda #32         ; Space
    sta (screen_ptr),y

    ; Read joystick and update position
    jsr read_joystick
    jsr try_move

    ; Draw new position
    jsr get_screen_pos
    lda #PLAYER_CHAR
    sta (screen_ptr),y
    rts
```
**If it doesn't work:** Player not moving? Check joystick reading at $DC00. Player drawing in wrong place? Verify screen position calculation (row × 40 + column).

---

### Unit 4: Wall Collision
**Builds:** Player cannot move through walls.
**Teaches:** Tile-based collision detection.
**Code pattern:**
```asm
; Check if target tile is passable
can_move:
    ; Calculate target position
    lda player_x
    clc
    adc move_dx
    sta target_x
    lda player_y
    clc
    adc move_dy
    sta target_y

    ; Get character at target
    jsr get_tile_at_target
    cmp #WALL_CHAR
    beq .blocked
    lda #1          ; Can move
    rts
.blocked:
    lda #0          ; Blocked
    rts
```
**If it doesn't work:** Walking through walls? Check tile lookup is reading the right position. Stuck everywhere? Verify wall character code comparison.

---

### Unit 5: Pellet Placement
**Builds:** Pellets fill the maze paths.
**Teaches:** Filling maze data, pellet counting.
**Code pattern:**
```asm
PELLET_CHAR = 46    ; Period character
pellet_count: !byte 0

place_pellets:
    lda #0
    sta pellet_count
    ldx #0
.loop:
    lda SCREEN,x
    cmp #32         ; If empty space
    bne .skip
    lda #PELLET_CHAR
    sta SCREEN,x
    inc pellet_count
.skip:
    inx
    bne .loop
    ; Continue for full screen...
    rts
```
**If it doesn't work:** No pellets? Make sure paths are spaces before filling. Wrong count? Check increment happens only for placed pellets.

---

### Unit 6: Pellet Collection
**Builds:** Player collects pellets, score increases.
**Teaches:** Collision response, score tracking.
**Code pattern:**
```asm
score_lo: !byte 0
score_hi: !byte 0

check_pellet:
    jsr get_screen_pos
    lda (screen_ptr),y
    cmp #PELLET_CHAR
    bne .no_pellet

    ; Collect it
    lda #32         ; Clear pellet
    sta (screen_ptr),y
    dec pellet_count

    ; Add 10 points
    lda score_lo
    clc
    adc #10
    sta score_lo
    bcc .done
    inc score_hi
.done:
.no_pellet:
    rts
```
**If it doesn't work:** Score not increasing? Check pellet character code match. Pellet not disappearing? Verify screen pointer is correct.

---

### Unit 7: Score Display
**Builds:** Score shown at top of screen with custom number font.
**Teaches:** Number-to-character conversion, display formatting.
**Code pattern:**
```asm
; Display score at screen position
SCORE_POS = $0400 + 33  ; Top row, column 33

display_score:
    ; Convert score_hi:score_lo to decimal
    ; Display 5 digits
    ldx #4          ; 5 digits, right to left
.digit_loop:
    lda score_digit,x
    clc
    adc #48         ; Convert to ASCII '0'-'9'
    sta SCORE_POS,x
    dex
    bpl .digit_loop
    rts
```
**If it doesn't work:** Wrong numbers? Check binary-to-decimal conversion. Numbers in wrong place? Verify SCORE_POS calculation.

---

### Unit 8: First Ghost
**Builds:** Single ghost that moves randomly.
**Teaches:** Entity structure, simple AI movement.
**Code pattern:**
```asm
ghost1_x: !byte 10
ghost1_y: !byte 10
ghost1_dir: !byte 0  ; 0=up, 1=right, 2=down, 3=left

update_ghost1:
    ; Erase old position
    jsr draw_ghost1_clear

    ; Try to move in current direction
    jsr ghost1_try_move
    bcs .moved

    ; Hit wall - pick new random direction
    jsr random
    and #3
    sta ghost1_dir

.moved:
    ; Draw at new position
    jsr draw_ghost1
    rts
```
**If it doesn't work:** Ghost not moving? Check direction-to-delta conversion. Ghost walking through walls? Ensure collision check uses ghost position, not player.

---

### Unit 9: Ghost-Player Collision
**Builds:** Ghost catches player, life lost.
**Teaches:** Entity-to-entity collision, game state.
**Code pattern:**
```asm
lives: !byte 3

check_ghost_collision:
    lda player_x
    cmp ghost1_x
    bne .no_hit
    lda player_y
    cmp ghost1_y
    bne .no_hit

    ; Collision!
    dec lives
    beq .game_over
    jsr reset_positions
    rts

.game_over:
    jmp show_game_over
.no_hit:
    rts
```
**If it doesn't work:** No collision detected? Check comparison is position-to-position, not screen memory. Instant death? Make sure reset gives player invincibility frames.

---

### Unit 10: Sound Effects
**Builds:** SID sounds for pellet eating, death.
**Teaches:** SID basics (expanding from Games 1-2).
**Code pattern:**
```asm
SID = $D400

sound_eat:
    lda #$00
    sta SID+5       ; Attack/Decay
    lda #$F0
    sta SID+6       ; Sustain/Release
    lda #$40
    sta SID+1       ; Frequency high
    lda #$21        ; Sawtooth, gate on
    sta SID+4
    rts

sound_death:
    ; Descending tone
    lda #$80
    sta SID+1
    lda #$81        ; Noise, gate on
    sta SID+4
    rts
```
**If it doesn't work:** No sound? Check SID volume at $D418 is not zero. Wrong sound? Verify waveform and frequency settings.

---

### Unit 11: Power Pellet
**Builds:** Four large power pellets in corners.
**Teaches:** Special item placement, game state changes.
**Code pattern:**
```asm
POWER_CHAR = 81     ; Filled circle
power_mode: !byte 0
power_timer: !byte 0

check_power_pellet:
    jsr get_screen_pos
    lda (screen_ptr),y
    cmp #POWER_CHAR
    bne .no_power

    ; Activate power mode
    lda #1
    sta power_mode
    lda #255        ; Timer
    sta power_timer

    ; Clear the pellet
    lda #32
    sta (screen_ptr),y
.no_power:
    rts
```
**If it doesn't work:** Power mode not activating? Check power pellet character code. Mode ending instantly? Verify timer decrement is per frame, not per loop.

---

### Unit 12: Frightened Ghosts
**Builds:** Ghosts turn blue and flee when power mode active.
**Teaches:** AI state machines, behaviour switching.
**Code pattern:**
```asm
GHOST_NORMAL = 1
GHOST_FRIGHTENED = 2

ghost1_state: !byte GHOST_NORMAL

update_ghost1_ai:
    lda power_mode
    beq .normal

    ; Frightened - move away from player
    lda #GHOST_FRIGHTENED
    sta ghost1_state
    jsr ghost1_flee
    rts

.normal:
    lda #GHOST_NORMAL
    sta ghost1_state
    jsr ghost1_chase
    rts
```
**If it doesn't work:** Ghost not changing colour? Check state affects drawing routine. Not fleeing? Verify flee direction is opposite of chase.

---

### Unit 13: Eating Ghosts
**Builds:** Player can eat frightened ghosts for points.
**Teaches:** State-dependent collision, point multipliers.
**Code pattern:**
```asm
ghost_points: !byte 0  ; 200, 400, 800, 1600

eat_ghost:
    lda ghost1_state
    cmp #GHOST_FRIGHTENED
    bne .no_eat

    ; Ghost eaten!
    jsr add_ghost_points
    jsr respawn_ghost1

    ; Double points for next ghost
    asl ghost_points

.no_eat:
    rts
```
**If it doesn't work:** Can't eat ghosts? Check state comparison before collision. Points wrong? Verify multiplier resets each power mode.

---

### Unit 14: Ghost Respawn
**Builds:** Eaten ghosts return from the ghost house.
**Teaches:** Spawn points, entity reset.
**Code pattern:**
```asm
GHOST_HOUSE_X = 13
GHOST_HOUSE_Y = 11

respawn_ghost1:
    lda #GHOST_HOUSE_X
    sta ghost1_x
    lda #GHOST_HOUSE_Y
    sta ghost1_y
    lda #GHOST_NORMAL
    sta ghost1_state
    lda #120        ; Delay before leaving
    sta ghost1_timer
    rts
```
**If it doesn't work:** Ghost appearing in wrong place? Check ghost house coordinates. Leaving immediately? Ensure timer prevents movement until expired.

---

### Unit 15: Level Complete
**Builds:** Clear all pellets to complete level.
**Teaches:** Win condition, level transitions.
**Code pattern:**
```asm
check_level_complete:
    lda pellet_count
    bne .not_done

    ; Level complete!
    jsr flash_screen
    inc level_number
    jsr init_level

.not_done:
    rts

flash_screen:
    ldx #8
.flash:
    lda $d020
    eor #$07
    sta $d020
    jsr delay
    dex
    bne .flash
    rts
```
**If it doesn't work:** Level not completing? Check pellet_count reaches exactly zero. Flash not visible? Increase delay duration.

---

### Unit 16: Phase 1 Polish
**Builds:** Title screen, lives display, attract mode.
**Teaches:** Game state management, presentation.
**If it doesn't work:** Attract mode glitchy? Ensure it resets cleanly when player starts. Lives display wrong? Check display updates after each death.

---

## Phase 2: Ghost AI Personalities (Units 17-32)

### Unit 17: Chase Mode Introduction
**Builds:** Ghost actively pursues player position.
**Teaches:** Target-seeking movement.
**Code pattern:**
```asm
ghost1_chase:
    ; Calculate direction to player
    lda player_x
    sec
    sbc ghost1_x
    bmi .go_left
    lda #1          ; Go right
    sta preferred_dx
    jmp .check_y
.go_left:
    lda #$FF        ; Go left
    sta preferred_dx
.check_y:
    ; Similar for Y...
    rts
```
**If it doesn't work:** Ghost not chasing? Check direction calculation signs. Stuck in corners? Need fallback when preferred direction blocked.

---

### Unit 18: Scatter Mode
**Builds:** Ghosts retreat to corners periodically.
**Teaches:** Mode timers, patrol behaviour.
**Code pattern:**
```asm
CHASE_TIME = 200
SCATTER_TIME = 70

mode_timer: !byte CHASE_TIME
current_mode: !byte MODE_CHASE

update_mode:
    dec mode_timer
    bne .no_change

    lda current_mode
    eor #1          ; Toggle mode
    sta current_mode

    ; Set appropriate timer
    lda current_mode
    beq .set_scatter
    lda #CHASE_TIME
    jmp .store
.set_scatter:
    lda #SCATTER_TIME
.store:
    sta mode_timer
.no_change:
    rts
```
**If it doesn't work:** Mode not switching? Check timer decrement and toggle logic. Ghosts ignoring mode? Verify AI checks current_mode.

---

### Unit 19: Ghost Personality - Blinky
**Builds:** Red ghost that directly chases player.
**Teaches:** Individual AI behaviour, entity identification.

---

### Unit 20: Ghost Personality - Pinky
**Builds:** Pink ghost that targets 4 tiles ahead of player.
**Teaches:** Predictive targeting, direction awareness.
**Code pattern:**
```asm
; Pinky targets 4 tiles ahead of player
pinky_chase:
    lda player_x
    clc
    adc player_dir_dx
    adc player_dir_dx
    adc player_dir_dx
    adc player_dir_dx
    sta pinky_target_x
    ; Similar for Y...
    jsr move_toward_target
    rts
```

---

### Unit 21: Ghost Personality - Inky
**Builds:** Cyan ghost with complex targeting (uses Blinky's position).
**Teaches:** Multi-entity AI coordination.

---

### Unit 22: Ghost Personality - Clyde
**Builds:** Orange ghost that flees when close, chases when far.
**Teaches:** Distance-based behaviour switching.
**Code pattern:**
```asm
CLYDE_FEAR_DISTANCE = 8

clyde_chase:
    ; Calculate distance to player
    jsr calc_distance_to_player
    cmp #CLYDE_FEAR_DISTANCE
    bcs .chase

    ; Too close - scatter to corner
    jsr clyde_scatter
    rts

.chase:
    ; Far enough - chase like Blinky
    jsr direct_chase
    rts
```

---

### Unit 23: All Four Ghosts
**Builds:** Complete ghost team with distinct behaviours.
**Teaches:** Multiple entity management.

---

### Unit 24: Pathfinding Introduction
**Builds:** Ghosts choose best path at intersections.
**Teaches:** Basic pathfinding concepts.
**Code pattern:**
```asm
; At intersection, evaluate each direction
choose_direction:
    lda #$FF
    sta best_distance

    ; Check each valid direction
    ldx #0
.check_dir:
    jsr can_move_direction
    bcc .next
    jsr calc_distance_if_move
    cmp best_distance
    bcs .next
    sta best_distance
    stx best_direction
.next:
    inx
    cpx #4
    bne .check_dir

    lda best_direction
    rts
```

---

### Unit 25: No Reverse Rule
**Builds:** Ghosts cannot reverse direction except on mode change.
**Teaches:** Movement constraints, rule exceptions.

---

### Unit 26: Tunnel Behaviour
**Builds:** Ghosts slow down in tunnel areas.
**Teaches:** Zone-based speed modification.

---

### Unit 27: Ghost House Exit
**Builds:** Ghosts leave house one at a time based on pellet count.
**Teaches:** Spawn timing, entity queuing.

---

### Unit 28: Elroy Mode
**Builds:** Blinky speeds up when few pellets remain.
**Teaches:** Dynamic difficulty, entity-specific rules.

---

### Unit 29: Corner Navigation
**Builds:** Ghosts pre-turn in corners (smoother movement).
**Teaches:** Movement polish, look-ahead.

---

### Unit 30: Scatter Targets
**Builds:** Each ghost has a unique corner target in scatter mode.
**Teaches:** Per-entity target positions.

---

### Unit 31: Mode Change Reversal
**Builds:** All ghosts reverse when mode changes (chase↔scatter).
**Teaches:** Global behaviour triggers.

---

### Unit 32: Phase 2 Polish
**Builds:** Ghost state indicators, AI debugging display (optional).
**If it doesn't work:** Debug display interfering with game? Make it toggle-able with a key.

---

## Phase 3: Level Design and Progression (Units 33-48)

### Unit 33: Level Data Structure
**Builds:** Maze stored as compressed data.
**Teaches:** Level data formats, memory efficiency.
**Code pattern:**
```asm
; RLE-encoded maze: byte pairs (count, tile)
level1_data:
    !byte 40, WALL      ; 40 wall tiles (top row)
    !byte 1, WALL       ; Left wall
    !byte 11, PATH      ; 11 path tiles
    !byte 2, WALL       ; Internal wall
    ; ... continue encoding
```

---

### Unit 34: Level Loading
**Builds:** Decode level data to screen.
**Teaches:** RLE decompression, streaming data.

---

### Unit 35: Level 1 Design
**Builds:** Classic arcade-style maze layout.
**Teaches:** Maze design principles (symmetry, flow).

---

### Unit 36: Level 2 Design
**Builds:** Alternate maze with different paths.
**Teaches:** Level variety, difficulty through layout.

---

### Unit 37: Level 3 Design
**Builds:** More complex maze with narrow corridors.
**Teaches:** Choke points, risk/reward paths.

---

### Unit 38: Level 4+ Layouts
**Builds:** Additional unique mazes.
**Teaches:** Level set completion.

---

### Unit 39: Speed Progression
**Builds:** Player and ghosts get faster each level.
**Teaches:** Difficulty curves, speed tables.
**Code pattern:**
```asm
; Speed increases per level (frames per move)
player_speeds:
    !byte 4, 4, 3, 3, 3, 2, 2, 2, 2, 2
ghost_speeds:
    !byte 5, 4, 4, 3, 3, 3, 2, 2, 2, 2

get_player_speed:
    ldx level_number
    cpx #10
    bcc .lookup
    ldx #9
.lookup:
    lda player_speeds,x
    rts
```

---

### Unit 40: Frightened Duration
**Builds:** Power mode gets shorter on later levels.
**Teaches:** Diminishing advantage, difficulty balance.

---

### Unit 41: Ghost Speed Variance
**Builds:** Different ghosts have different base speeds.
**Teaches:** Entity differentiation through stats.

---

### Unit 42: Bonus Fruit System
**Builds:** Fruit appears after eating certain pellet counts.
**Teaches:** Timed bonus spawns, variety.
**Code pattern:**
```asm
; Fruit appears at 70 and 170 pellets eaten
FRUIT_SPAWN_1 = 70
FRUIT_SPAWN_2 = 170

fruit_active: !byte 0
fruit_timer: !byte 0

check_fruit_spawn:
    lda pellets_eaten
    cmp #FRUIT_SPAWN_1
    beq .spawn
    cmp #FRUIT_SPAWN_2
    beq .spawn
    rts

.spawn:
    lda fruit_active
    bne .already
    lda #1
    sta fruit_active
    lda #200        ; Visible for 200 frames
    sta fruit_timer
.already:
    rts
```

---

### Unit 43: Fruit Types
**Builds:** Different fruits per level (cherry, strawberry, etc.).
**Teaches:** Level-indexed content.

---

### Unit 44: Intermission Screens
**Builds:** Cutscenes between certain levels.
**Teaches:** Non-gameplay sequences, storytelling.

---

### Unit 45: Kill Screen Prevention
**Builds:** Proper handling of high levels (no overflow bugs).
**Teaches:** Edge case handling, robustness.

---

### Unit 46: Level Select (Debug)
**Builds:** Hidden level select for testing.
**Teaches:** Debug features, developer tools.

---

### Unit 47: Attract Mode Demo
**Builds:** AI plays game during attract mode.
**Teaches:** Replay systems, demonstration.

---

### Unit 48: Phase 3 Polish
**Builds:** Smooth level transitions, complete level set.
**If it doesn't work:** Transition glitchy? Clear screen fully before loading new level.

---

## Phase 4: Advanced Graphics (Units 49-64)

### Unit 49: Animated Player
**Builds:** Player mouth opens and closes while moving.
**Teaches:** Frame animation, direction-based sprites.

---

### Unit 50: Ghost Animation
**Builds:** Ghosts have waving skirt animation.
**Teaches:** Multi-frame entity animation.

---

### Unit 51: Direction-Facing Sprites
**Builds:** Player and ghosts face movement direction.
**Teaches:** Direction-to-frame lookup.
**Code pattern:**
```asm
; Character frames per direction
; 0=up, 1=right, 2=down, 3=left
player_frames:
    !byte PLAYER_UP_1, PLAYER_UP_2
    !byte PLAYER_RIGHT_1, PLAYER_RIGHT_2
    !byte PLAYER_DOWN_1, PLAYER_DOWN_2
    !byte PLAYER_LEFT_1, PLAYER_LEFT_2

get_player_frame:
    lda player_direction
    asl             ; ×2 for frame pair
    clc
    adc anim_frame  ; 0 or 1
    tax
    lda player_frames,x
    rts
```

---

### Unit 52: Death Animation
**Builds:** Player "deflates" when caught.
**Teaches:** Death sequence, animation priority.

---

### Unit 53: Ghost Eyes
**Builds:** Eaten ghosts become just eyes returning to house.
**Teaches:** State-dependent rendering.

---

### Unit 54: Colour Per Ghost
**Builds:** Each ghost has distinct colour.
**Teaches:** Colour RAM usage with characters.
**Code pattern:**
```asm
; Ghost colours
BLINKY_COLOUR = 2   ; Red
PINKY_COLOUR = 4    ; Purple
INKY_COLOUR = 6     ; Cyan
CLYDE_COLOUR = 7    ; Orange

draw_ghost1:
    jsr get_screen_pos
    lda #GHOST_CHAR
    sta (screen_ptr),y

    ; Set colour
    jsr get_colour_pos
    lda #BLINKY_COLOUR
    sta (colour_ptr),y
    rts
```

---

### Unit 55: Frightened Flash
**Builds:** Blue ghosts flash white near power mode end.
**Teaches:** Timer-based visual warnings.

---

### Unit 56: Score Pop-ups
**Builds:** Points appear briefly when eating ghost/fruit.
**Teaches:** Temporary display elements.

---

### Unit 57: Maze Colour Variety
**Builds:** Different mazes use different wall colours.
**Teaches:** Level theming through colour.

---

### Unit 58: Smooth Movement
**Builds:** Pixel-based movement between tiles (not instant jump).
**Teaches:** Sub-tile positioning, interpolation.

---

### Unit 59: Border Effects
**Builds:** Border colour changes with game state.
**Teaches:** Using border for feedback.

---

### Unit 60: Custom Font
**Builds:** Complete custom font for score and text.
**Teaches:** Font design, character set completion.

---

### Unit 61: High Score Entry
**Builds:** Enter initials for high score.
**Teaches:** Text input, character selection.

---

### Unit 62: High Score Table
**Builds:** Persistent high score display.
**Teaches:** Score sorting, table management.

---

### Unit 63: Screen Transitions
**Builds:** Wipe effects between screens.
**Teaches:** Visual polish, transition effects.

---

### Unit 64: Phase 4 Polish
**Builds:** All graphics complete, consistent visual style.

---

## Phase 5: Audio and Music (Units 65-80)

### Unit 65: Sound Effect System
**Builds:** Priority-based sound effect manager.
**Teaches:** Audio priorities, effect queuing.

---

### Unit 66: Pellet Eating Sound
**Builds:** Alternating waka-waka sound.
**Teaches:** Sound variation, classic effects.
**Code pattern:**
```asm
waka_toggle: !byte 0

sound_waka:
    lda waka_toggle
    eor #1
    sta waka_toggle
    beq .low

    ; High waka
    lda #$30
    sta SID+1
    jmp .play

.low:
    ; Low waka
    lda #$28
    sta SID+1

.play:
    lda #$21        ; Sawtooth
    sta SID+4
    rts
```

---

### Unit 67: Power Pellet Sound
**Builds:** Distinct sound when grabbing power pellet.
**Teaches:** Event-specific audio.

---

### Unit 68: Frightened Mode Sound
**Builds:** Background siren during power mode.
**Teaches:** Continuous background audio.

---

### Unit 69: Ghost Eaten Sound
**Builds:** Gulp sound when eating ghost.
**Teaches:** Reward audio feedback.

---

### Unit 70: Death Sound
**Builds:** Descending tone for player death.
**Teaches:** Negative feedback audio.

---

### Unit 71: Level Complete Sound
**Builds:** Victory fanfare.
**Teaches:** Achievement audio.

---

### Unit 72: Background Siren
**Builds:** Pitch varies with remaining pellets.
**Teaches:** Dynamic audio feedback.

---

### Unit 73: Music Introduction
**Builds:** Simple tune for title screen.
**Teaches:** Basic SID music, note sequences.

---

### Unit 74: Intermission Music
**Builds:** Music for cutscene sequences.
**Teaches:** Longer musical pieces.

---

### Unit 75: Music Player
**Builds:** Pattern-based music playback.
**Teaches:** Music data structures.

---

### Unit 76: Sound/Music Mixing
**Builds:** Sound effects don't interrupt music.
**Teaches:** Voice allocation, mixing.

---

### Unit 77: Extra Life Sound
**Builds:** Distinctive sound at 10,000 points.
**Teaches:** Milestone audio.

---

### Unit 78: Audio Polish
**Builds:** All sounds balanced and consistent.
**Teaches:** Audio mix, volume balance.

---

### Unit 79: ADSR Tuning
**Builds:** Refine envelope settings for all sounds.
**Teaches:** Sound design polish.

---

### Unit 80: Phase 5 Polish
**Builds:** Complete audio implementation.

---

## Phase 6: Game Features (Units 81-96)

### Unit 81: Two-Player Alternating
**Builds:** Players take turns on death.
**Teaches:** Multi-player state management.

---

### Unit 82: Two-Player Score Tracking
**Builds:** Separate scores for each player.
**Teaches:** Per-player data.

---

### Unit 83: Lives System
**Builds:** Start with 3 lives, display remaining.
**Teaches:** Life tracking, display.

---

### Unit 84: Extra Life Award
**Builds:** Bonus life at 10,000 points.
**Teaches:** Score milestones.

---

### Unit 85: Pause Feature
**Builds:** Pause game with RUN/STOP key.
**Teaches:** Game pause implementation.

---

### Unit 86: Difficulty Settings
**Builds:** Easy/Normal/Hard options.
**Teaches:** Difficulty parameters.

---

### Unit 87: Speed Options
**Builds:** Slow/Normal/Fast game speed.
**Teaches:** Game speed control.

---

### Unit 88: Starting Level Option
**Builds:** Begin at higher levels (with score penalty).
**Teaches:** Level select systems.

---

### Unit 89: Credits Screen
**Builds:** Display developer credits.
**Teaches:** Presentation, attribution.

---

### Unit 90: Instructions Screen
**Builds:** How to play information.
**Teaches:** Onboarding, help systems.

---

### Unit 91: Statistics Tracking
**Builds:** Track pellets eaten, ghosts eaten, etc.
**Teaches:** Play statistics.

---

### Unit 92: End Game Summary
**Builds:** Show stats at game over.
**Teaches:** Session summary.

---

### Unit 93: Game State Machine
**Builds:** Clean transitions between all states.
**Teaches:** Overall game architecture.

---

### Unit 94: Input Buffering
**Builds:** Queue direction changes for responsiveness.
**Teaches:** Input feel, cornering.

---

### Unit 95: Pre-Turn Feature
**Builds:** Turn slightly before reaching corner.
**Teaches:** Movement feel polish.

---

### Unit 96: Phase 6 Polish
**Builds:** All features working together smoothly.

---

## Phase 7: Optimisation and Testing (Units 97-112)

### Unit 97: Frame Rate Analysis
**Builds:** Measure and display frame time.
**Teaches:** Performance measurement.

---

### Unit 98: Ghost AI Optimisation
**Builds:** Faster pathfinding calculations.
**Teaches:** Algorithm efficiency.

---

### Unit 99: Drawing Optimisation
**Builds:** Only redraw changed characters.
**Teaches:** Dirty rectangle concept.

---

### Unit 100: Memory Layout
**Builds:** Optimal data placement.
**Teaches:** Memory map planning.

---

### Unit 101: Code Organisation
**Builds:** Clean module structure.
**Teaches:** Code architecture.

---

### Unit 102: Bug Hunt - Collision
**Builds:** Fix corner-case collision bugs.
**Teaches:** Edge case testing.

---

### Unit 103: Bug Hunt - AI
**Builds:** Fix ghost behaviour edge cases.
**Teaches:** AI debugging.

---

### Unit 104: Bug Hunt - Timing
**Builds:** Fix frame rate inconsistencies.
**Teaches:** Timing issues.

---

### Unit 105: Playtesting - Difficulty
**Builds:** Adjust difficulty curve from feedback.
**Teaches:** Iterative balancing.

---

### Unit 106: Playtesting - Feel
**Builds:** Tune movement and response.
**Teaches:** Game feel refinement.

---

### Unit 107: Playtesting - Fairness
**Builds:** Ensure ghosts feel fair, not cheap.
**Teaches:** AI fairness.

---

### Unit 108: Stress Testing
**Builds:** Verify no crashes with extreme play.
**Teaches:** Robustness testing.

---

### Unit 109: Memory Check
**Builds:** Verify no memory corruption.
**Teaches:** Memory debugging.

---

### Unit 110: Save/Load State (Optional)
**Builds:** Save position for testing.
**Teaches:** State serialisation.

---

### Unit 111: Final Bug Fixes
**Builds:** Address remaining issues.
**Teaches:** Bug prioritisation.

---

### Unit 112: Phase 7 Polish
**Builds:** Stable, optimised codebase.

---

## Phase 8: Final Polish and Release (Units 113-128)

### Unit 113: Title Screen Art
**Builds:** Custom title screen graphics.
**Teaches:** Logo design, presentation.

---

### Unit 114: Loading Screen
**Builds:** Display while loading from tape/disk.
**Teaches:** Load screen design.

---

### Unit 115: Box Art Mockup
**Builds:** Design fictional box art.
**Teaches:** Marketing, presentation.

---

### Unit 116: Manual Writing
**Builds:** Write game manual.
**Teaches:** Documentation, instructions.

---

### Unit 117: Easter Eggs
**Builds:** Hidden features for dedicated players.
**Teaches:** Secrets, player rewards.

---

### Unit 118: Cheat Codes
**Builds:** Debug codes (infinite lives, level skip).
**Teaches:** Cheat implementation.

---

### Unit 119: Version Numbering
**Builds:** Track build versions.
**Teaches:** Release management.

---

### Unit 120: PRG Creation
**Builds:** Final assembled binary.
**Teaches:** Build process.

---

### Unit 121: D64 Disk Image
**Builds:** Distributable disk image.
**Teaches:** Disk mastering.

---

### Unit 122: T64 Tape Image
**Builds:** Tape distribution format.
**Teaches:** Tape mastering.

---

### Unit 123: Emulator Testing
**Builds:** Verify in VICE emulator.
**Teaches:** Cross-testing.

---

### Unit 124: Hardware Testing
**Builds:** Test on real C64.
**Teaches:** Hardware verification.

---

### Unit 125: Release Candidate
**Builds:** Final pre-release build.
**Teaches:** Release process.

---

### Unit 126: Community Feedback
**Builds:** Gather tester feedback.
**Teaches:** Beta testing.

---

### Unit 127: Final Fixes
**Builds:** Last adjustments from feedback.
**Teaches:** Polish cycle.

---

### Unit 128: Release
**Builds:** Final release build.
**Teaches:** Shipping a complete game.

---

## Version History

- **1.0 (2026-01-18):** Initial 128-unit outline created.
