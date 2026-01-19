# C64 Game 4: Brick Basher - Full 128-Unit Outline

**Platform:** Commodore 64
**Game:** Brick Basher
**Units:** 128 (8 phases × 16 units)
**Concept:** Breakout clone polished to commercial quality. Paddle, ball, bricks - with tight physics, satisfying destruction, and the SID chip making every bounce sing.

---

## Overview

Brick Basher builds on the physics foundations from Platform Panic and Maze Raider, applying them to ball dynamics. After mastering gravity and tile-based movement, learners now tackle velocity vectors, reflection angles, and the satisfaction of destruction.

**Key Learning Goals:**
- Ball physics (velocity, angles, reflection, spin)
- Paddle collision with positional influence
- Character graphics for brick fields
- Fixed-point maths for smooth movement
- Power-up systems
- SID audio design for impacts

---

## Phase 1: Ball and Paddle Foundation (Units 1-16)

### Unit 1: The Brick Wall
**Builds:** Colourful brick field using custom characters.
**Teaches:** Character set redefinition for game graphics.
**Code pattern:**
```asm
; Custom character set for bricks
; Each character: 8 bytes defining 8x8 pixel pattern
!to "bricks.prg",cbm
* = $0801
    !basic

* = $2000           ; Character set location
brick_chars:
    ; Character 0: Solid brick left half
    !byte %11111111
    !byte %11111110
    !byte %11111110
    !byte %11111110
    !byte %11111110
    !byte %11111110
    !byte %11111110
    !byte %00000000

    ; Character 1: Solid brick right half
    !byte %11111111
    !byte %01111111
    !byte %01111111
    !byte %01111111
    !byte %01111111
    !byte %01111111
    !byte %01111111
    !byte %00000000

* = $0900
init:
    ; Point VIC to custom charset at $2000
    lda $d018
    and #%11110000
    ora #%00001000      ; Chars at $2000
    sta $d018
    rts
```
**If it doesn't work:** Characters not showing? Check $D018 points to correct bank. Garbled graphics? Verify character data is 8 bytes per character.

---

### Unit 2: Drawing Bricks
**Builds:** Fill screen area with brick characters.
**Teaches:** Screen memory manipulation.
**Code pattern:**
```asm
SCREEN = $0400
COLOUR = $d800
BRICK_ROWS = 6
BRICK_COLS = 18

draw_bricks:
    ldx #0
    ldy #0
@row_loop:
    lda #<(SCREEN + 40 + 1)     ; Start row 1, col 1
    clc
    adc row_offset,y
    sta screen_ptr
    lda #>(SCREEN + 40 + 1)
    adc row_offset_hi,y
    sta screen_ptr+1

    ; Draw 18 bricks (2 chars each = 36 chars)
    ldx #0
@brick_loop:
    lda #0                      ; Left brick char
    sta (screen_ptr),x
    inx
    lda #1                      ; Right brick char
    sta (screen_ptr),x
    inx
    cpx #36
    bne @brick_loop

    iny
    cpy #BRICK_ROWS
    bne @row_loop
    rts
```
**If it doesn't work:** Bricks in wrong place? Check row offset calculation. Missing bricks? Verify loop counters.

---

### Unit 3: Brick Colours
**Builds:** Different colour for each row using colour RAM.
**Teaches:** Colour RAM usage.
**Code pattern:**
```asm
; Colour RAM mirrors screen layout
brick_colours:
    !byte 2, 10, 7, 5, 6, 4     ; Red, pink, yellow, green, blue, purple

colour_bricks:
    ldy #0
@row_loop:
    ; Calculate colour RAM address for row
    lda #<(COLOUR + 40 + 1)
    clc
    adc row_offset,y
    sta colour_ptr
    lda #>(COLOUR + 40 + 1)
    adc row_offset_hi,y
    sta colour_ptr+1

    lda brick_colours,y         ; Get row colour

    ldx #0
@col_loop:
    sta (colour_ptr),x
    inx
    cpx #36
    bne @col_loop

    iny
    cpy #BRICK_ROWS
    bne @row_loop
    rts
```
**If it doesn't work:** All same colour? Ensure colour_ptr is different from screen_ptr. Wrong colours? Check colour RAM address ($D800).

---

### Unit 4: Paddle Sprite
**Builds:** Paddle at bottom of screen using hardware sprite.
**Teaches:** Sprite setup for paddle.
**Code pattern:**
```asm
SPRITE_PTR = $07f8
SPRITE_DATA = $2800

paddle_x:   !byte 160
paddle_y = 230

init_paddle:
    ; Enable sprite 0
    lda #%00000001
    sta $d015

    ; Set sprite pointer
    lda #(SPRITE_DATA/64)
    sta SPRITE_PTR

    ; Position
    lda paddle_x
    sta $d000               ; Sprite 0 X
    lda #paddle_y
    sta $d001               ; Sprite 0 Y

    ; Colour
    lda #1                  ; White
    sta $d027
    rts
```
**If it doesn't work:** No paddle? Check sprite enable register $D015. Wrong position? Verify X/Y registers.

---

### Unit 5: Paddle Movement
**Builds:** Joystick moves paddle left/right.
**Teaches:** Horizontal-only joystick control.
**Code pattern:**
```asm
PADDLE_SPEED = 3
PADDLE_MIN = 24
PADDLE_MAX = 255

update_paddle:
    lda $dc00               ; Read joystick port 2
    lsr                     ; Bit 0 = up (ignore)
    lsr                     ; Bit 1 = down (ignore)
    lsr                     ; Bit 2 = left
    bcs @check_right

    ; Move left
    lda paddle_x
    sec
    sbc #PADDLE_SPEED
    cmp #PADDLE_MIN
    bcs @store
    lda #PADDLE_MIN
    jmp @store

@check_right:
    lsr                     ; Bit 3 = right
    bcs @done

    ; Move right
    lda paddle_x
    clc
    adc #PADDLE_SPEED
    cmp #PADDLE_MAX
    bcc @store
    lda #PADDLE_MAX

@store:
    sta paddle_x
    sta $d000               ; Update sprite X

@done:
    rts
```
**If it doesn't work:** Not responding? Check joystick port ($DC00 vs $DC01). Inverted? Remember 0 = pressed.

---

### Unit 6: Ball Sprite
**Builds:** Ball displayed as sprite.
**Teaches:** Second sprite setup.
**Code pattern:**
```asm
ball_x:     !byte 160
ball_y:     !byte 150

init_ball:
    ; Enable sprites 0 and 1
    lda #%00000011
    sta $d015

    ; Sprite 1 pointer
    lda #(BALL_SPRITE_DATA/64)
    sta SPRITE_PTR+1

    ; Position
    lda ball_x
    sta $d002               ; Sprite 1 X
    lda ball_y
    sta $d003               ; Sprite 1 Y

    ; Colour - yellow
    lda #7
    sta $d028
    rts
```

---

### Unit 7: Ball Movement
**Builds:** Ball moves in a direction.
**Teaches:** Velocity application.
**Code pattern:**
```asm
ball_vel_x:     !byte 1
ball_vel_y:     !byte $ff       ; Negative = upward

update_ball:
    ; Update X
    lda ball_x
    clc
    adc ball_vel_x
    sta ball_x
    sta $d002

    ; Update Y
    lda ball_y
    clc
    adc ball_vel_y
    sta ball_y
    sta $d003
    rts
```
**If it doesn't work:** Not moving? Check velocity isn't zero. Wrong direction? Verify signed arithmetic.

---

### Unit 8: Wall Bouncing
**Builds:** Ball bounces off screen edges.
**Teaches:** Boundary collision and velocity reversal.
**Code pattern:**
```asm
check_walls:
    ; Left wall
    lda ball_x
    cmp #24
    bcs @check_right
    lda #0
    sec
    sbc ball_vel_x
    sta ball_vel_x
    lda #24
    sta ball_x

@check_right:
    lda ball_x
    cmp #240
    bcc @check_top
    lda #0
    sec
    sbc ball_vel_x
    sta ball_vel_x
    lda #240
    sta ball_x

@check_top:
    lda ball_y
    cmp #50
    bcs @done
    lda #0
    sec
    sbc ball_vel_y
    sta ball_vel_y
    lda #50
    sta ball_y

@done:
    rts
```
**If it doesn't work:** Going through walls? Check comparison values. Not reversing? Verify subtraction from zero for negation.

---

### Unit 9: Ball Lost
**Builds:** Ball below paddle loses life.
**Teaches:** Miss detection, game state.

---

### Unit 10: Paddle Collision
**Builds:** Ball bounces off paddle.
**Teaches:** Sprite-to-sprite collision zone.
**Code pattern:**
```asm
PADDLE_WIDTH = 24

check_paddle:
    ; Is ball at paddle Y?
    lda ball_y
    cmp #paddle_y - 8
    bcc @no_hit
    cmp #paddle_y + 4
    bcs @no_hit

    ; Is ball within paddle X range?
    lda ball_x
    sec
    sbc paddle_x
    bcc @no_hit             ; Left of paddle
    cmp #PADDLE_WIDTH + 8
    bcs @no_hit             ; Right of paddle

    ; Hit! Reverse Y
    lda #0
    sec
    sbc ball_vel_y
    sta ball_vel_y
    jsr sound_paddle

@no_hit:
    rts
```
**If it doesn't work:** Not bouncing? Check Y comparison range. Going through? Widen collision zone.

---

### Unit 11: Position to Brick
**Builds:** Convert ball position to brick grid location.
**Teaches:** Screen-to-grid conversion.
**Code pattern:**
```asm
; Convert sprite position to brick row/column
; Bricks start at screen row 1, col 1
; Each brick is 16x8 pixels (2 chars wide, 1 char tall)

get_brick_position:
    ; Row = (ball_y - 50) / 8
    lda ball_y
    sec
    sbc #50                 ; Brick area start Y
    lsr
    lsr
    lsr                     ; /8
    sta brick_row

    ; Column = (ball_x - 24) / 16
    lda ball_x
    sec
    sbc #24                 ; Brick area start X
    lsr
    lsr
    lsr
    lsr                     ; /16
    sta brick_col
    rts
```
**If it doesn't work:** Wrong brick? Check offset values match screen layout. Off by one? Verify division.

---

### Unit 12: Brick Collision Detection
**Builds:** Check if brick exists at ball position.
**Teaches:** Grid-based collision.
**Code pattern:**
```asm
; Check screen memory for brick character
check_brick:
    jsr get_brick_position

    ; Is position in valid brick area?
    lda brick_row
    cmp #BRICK_ROWS
    bcs @no_brick
    lda brick_col
    cmp #BRICK_COLS
    bcs @no_brick

    ; Calculate screen address
    ; Address = SCREEN + 40 + 1 + (row * 40) + (col * 2)
    lda brick_row
    asl
    asl
    asl                     ; * 8
    sta temp
    asl
    asl                     ; * 32
    clc
    adc temp                ; * 40
    clc
    adc #41                 ; Offset from start
    adc brick_col
    adc brick_col           ; col * 2
    sta screen_ptr
    lda #>SCREEN
    adc #0
    sta screen_ptr+1

    ; Is there a brick here?
    ldy #0
    lda (screen_ptr),y
    cmp #32                 ; Space = no brick
    beq @no_brick

    ; Brick found!
    lda #1
    rts

@no_brick:
    lda #0
    rts
```
**If it doesn't work:** Wrong detection? Check screen address calculation. Missing bricks? Verify character code for empty space.

---

### Unit 13: Brick Destruction
**Builds:** Remove brick when hit.
**Teaches:** Screen memory modification.
**Code pattern:**
```asm
destroy_brick:
    ; Clear both characters of brick
    lda #32                 ; Space character
    ldy #0
    sta (screen_ptr),y
    iny
    sta (screen_ptr),y

    ; Update brick count
    dec bricks_remaining
    bne @not_win
    jmp level_complete

@not_win:
    ; Add score
    sed                     ; Decimal mode
    lda score
    clc
    adc #$10                ; 10 points
    sta score
    cld
    jsr update_score_display

    ; Reverse ball
    lda #0
    sec
    sbc ball_vel_y
    sta ball_vel_y

    jsr sound_brick
    rts
```
**If it doesn't work:** Brick not disappearing? Check screen_ptr still valid. Score wrong? Remember to exit decimal mode.

---

### Unit 14: Lives Display
**Builds:** Show remaining lives.
**Teaches:** HUD elements.

---

### Unit 15: Score Display
**Builds:** Show current score.
**Teaches:** Number-to-character conversion.

---

### Unit 16: Sound - Basic Impacts
**Builds:** SID sounds for paddle and brick hits.
**Teaches:** Basic SID programming.
**Code pattern:**
```asm
SID = $d400

sound_paddle:
    lda #$0f
    sta SID+24              ; Volume
    lda #$00
    sta SID+5               ; Attack/Decay
    lda #$f0
    sta SID+6               ; Sustain/Release
    lda #$30
    sta SID                 ; Freq low
    lda #$10
    sta SID+1               ; Freq high
    lda #$21                ; Pulse + gate
    sta SID+4
    rts

sound_brick:
    ; Higher pitch for brick
    lda #$80
    sta SID
    lda #$15
    sta SID+1
    lda #$11                ; Triangle + gate
    sta SID+4
    rts
```
**If it doesn't work:** No sound? Check volume register. Wrong pitch? Adjust frequency values.

---

## Phase 2: Physics Refinement (Units 17-32)

### Unit 17: Fixed-Point Position
**Builds:** Sub-pixel ball movement.
**Teaches:** 8.8 fixed-point maths.
**Code pattern:**
```asm
; 8.8 fixed point: high byte = pixels, low byte = fraction
ball_x_lo:  !byte 0         ; Fractional part
ball_x_hi:  !byte 160       ; Pixel part
ball_y_lo:  !byte 0
ball_y_hi:  !byte 150
vel_x_lo:   !byte $80       ; 1.5 pixels per frame
vel_x_hi:   !byte 1
vel_y_lo:   !byte $00
vel_y_hi:   !byte $ff       ; -1

update_ball_smooth:
    ; X += vel_x (16-bit add)
    clc
    lda ball_x_lo
    adc vel_x_lo
    sta ball_x_lo
    lda ball_x_hi
    adc vel_x_hi
    sta ball_x_hi
    sta $d002               ; Sprite X

    ; Y += vel_y (16-bit add)
    clc
    lda ball_y_lo
    adc vel_y_lo
    sta ball_y_lo
    lda ball_y_hi
    adc vel_y_hi
    sta ball_y_hi
    sta $d003               ; Sprite Y
    rts
```
**If it doesn't work:** Jerky movement? Ensure low byte isn't ignored. Drifting? Check signed addition for negative velocities.

---

### Unit 18: Ball Speed Progression
**Builds:** Ball speeds up as game progresses.
**Teaches:** Dynamic difficulty.

---

### Unit 19: Paddle Angle Control
**Builds:** Where ball hits paddle affects bounce angle.
**Teaches:** Positional collision response.
**Code pattern:**
```asm
; Offset from paddle centre determines X velocity
calculate_angle:
    ; Get hit position relative to paddle centre
    lda ball_x_hi
    sec
    sbc paddle_x
    sec
    sbc #PADDLE_WIDTH/2     ; Centre offset

    ; Now A is -12 to +12 (roughly)
    ; Use as velocity adjustment
    sta vel_x_hi

    ; Ensure ball moves upward
    lda #$ff
    sta vel_y_hi
    lda #$00
    sta vel_y_lo
    rts
```
**If it doesn't work:** Always same angle? Check offset calculation. Too extreme? Scale down the offset.

---

### Unit 20: Paddle Spin Effect
**Builds:** Moving paddle adds spin to ball.
**Teaches:** Velocity transfer.

---

### Unit 21: Brick Side Detection
**Builds:** Determine which side of brick was hit.
**Teaches:** Directional collision.

---

### Unit 22: Horizontal Brick Bounce
**Builds:** Side hits reverse X instead of Y.
**Teaches:** Multi-axis collision.

---

### Unit 23: Corner Collision
**Builds:** Corner hits handled correctly.
**Teaches:** Edge cases.

---

### Unit 24: Multi-Brick Hits
**Builds:** Ball can hit multiple bricks per frame.
**Teaches:** Multiple collision handling.

---

### Unit 25: Stuck Prevention
**Builds:** Ball can't embed in bricks.
**Teaches:** Position correction.

---

### Unit 26: Launch System
**Builds:** Ball starts on paddle, launch with fire.
**Teaches:** Serve mechanic.
**Code pattern:**
```asm
serving:    !byte 1         ; 1 = ball on paddle

update_serve:
    lda serving
    beq @playing

    ; Ball follows paddle
    lda paddle_x
    clc
    adc #PADDLE_WIDTH/2
    sta ball_x_hi
    sta $d002

    ; Check fire button
    lda $dc00
    and #%00010000          ; Fire bit
    bne @done               ; Not pressed

    ; Launch!
    lda #0
    sta serving
    ; Set initial velocity
    lda #$ff
    sta vel_y_hi
    lda #1
    sta vel_x_hi

@done:
@playing:
    rts
```

---

### Unit 27: Launch Direction
**Builds:** Paddle movement affects launch angle.
**Teaches:** Aimed serving.

---

### Unit 28: Ball Trail Effect
**Builds:** Brief afterimage following ball.
**Teaches:** Visual polish.

---

### Unit 29: Brick Flash
**Builds:** Brief colour flash when hit.
**Teaches:** Impact feedback.

---

### Unit 30: Sound - Varied Pitches
**Builds:** Different brick colours = different sounds.
**Teaches:** Audio variety.

---

### Unit 31: Sound - Wall Bounce
**Builds:** Distinct wall sound.
**Teaches:** Sound design.

---

### Unit 32: Phase 2 Polish
**Builds:** Tight, satisfying physics.

---

## Phase 3: Brick Variety (Units 33-48)

### Unit 33: Brick Point Values
**Builds:** Different colours worth different points.
**Teaches:** Scoring variety.

---

### Unit 34: Hard Bricks
**Builds:** Silver bricks take 2 hits.
**Teaches:** Hit points.

---

### Unit 35: Hard Brick Visual
**Builds:** Hard bricks look different when damaged.
**Teaches:** State-based graphics.

---

### Unit 36: Unbreakable Bricks
**Builds:** Gold bricks never break.
**Teaches:** Obstacles.

---

### Unit 37: Explosive Bricks
**Builds:** Red bricks destroy neighbours.
**Teaches:** Chain reactions.

---

### Unit 38: Explosive Animation
**Builds:** Visual effect for explosions.
**Teaches:** Particle effects.

---

### Unit 39: Moving Brick Row
**Builds:** Top row moves side to side.
**Teaches:** Dynamic playfield.

---

### Unit 40: Regenerating Bricks
**Builds:** Ghost bricks return after time.
**Teaches:** Timed respawns.

---

### Unit 41: Hidden Bricks
**Builds:** Invisible until ball approaches.
**Teaches:** Reveal mechanics.

---

### Unit 42: Brick Patterns
**Builds:** Creative arrangements.
**Teaches:** Level design.

---

### Unit 43: Row Clear Bonus
**Builds:** Bonus for clearing full row.
**Teaches:** Combo bonus.

---

### Unit 44: Multiplier System
**Builds:** Consecutive hits build multiplier.
**Teaches:** Score chains.

---

### Unit 45: Brick Animation
**Builds:** Bricks shimmer or pulse.
**Teaches:** Background animation.

---

### Unit 46: Brick Destruction Animation
**Builds:** Bricks crumble when destroyed.
**Teaches:** Destruction effects.

---

### Unit 47: Sound - Chain Reactions
**Builds:** Escalating sounds for chains.
**Teaches:** Audio feedback.

---

### Unit 48: Phase 3 Polish
**Builds:** Rich brick variety.

---

## Phase 4: Power-Ups (Units 49-64)

### Unit 49: Power-Up System
**Builds:** Items drop from certain bricks.
**Teaches:** Item spawning.
**Code pattern:**
```asm
; Power-up uses sprite 2
powerup_active: !byte 0
powerup_x:      !byte 0
powerup_y:      !byte 0
powerup_type:   !byte 0
POWERUP_FALL_SPEED = 2

spawn_powerup:
    ; 20% chance on brick destroy
    jsr random
    and #%00000111
    cmp #2
    bcs @no_spawn

    ; Get brick position as starting point
    lda ball_x_hi
    sta powerup_x
    lda ball_y_hi
    sta powerup_y

    ; Random type (0-7)
    jsr random
    and #%00000111
    sta powerup_type

    ; Activate sprite 2
    lda $d015
    ora #%00000100
    sta $d015

    lda #1
    sta powerup_active

@no_spawn:
    rts
```

---

### Unit 50: Power-Up Falling
**Builds:** Item falls toward paddle.
**Teaches:** Gravity for items.

---

### Unit 51: Power-Up Collection
**Builds:** Paddle catches item.
**Teaches:** Collection collision.

---

### Unit 52: Power-Up - Extend
**Builds:** Paddle becomes wider.
**Teaches:** Player enhancement.

---

### Unit 53: Power-Up - Shrink
**Builds:** Paddle becomes smaller.
**Teaches:** Negative items.

---

### Unit 54: Power-Up - Multi-Ball
**Builds:** Ball splits into three.
**Teaches:** Multiple ball management.

---

### Unit 55: Multi-Ball Tracking
**Builds:** Game continues until all balls lost.
**Teaches:** Entity arrays.

---

### Unit 56: Power-Up - Catch
**Builds:** Ball sticks to paddle.
**Teaches:** State modifier.

---

### Unit 57: Catch Release
**Builds:** Press fire to release caught ball.
**Teaches:** Input-triggered release.

---

### Unit 58: Power-Up - Laser
**Builds:** Paddle shoots lasers.
**Teaches:** Weapon power-up.

---

### Unit 59: Laser Firing
**Builds:** Fire button shoots while active.
**Teaches:** Projectile spawning.

---

### Unit 60: Power-Up - Slow
**Builds:** Ball moves slower.
**Teaches:** Speed modification.

---

### Unit 61: Power-Up - Fast
**Builds:** Ball speeds up.
**Teaches:** Risk/reward.

---

### Unit 62: Power-Up - Extra Life
**Builds:** Rare 1-up.
**Teaches:** High-value items.

---

### Unit 63: Power-Up Timer Display
**Builds:** Show remaining time for timed effects.
**Teaches:** Status display.

---

### Unit 64: Phase 4 Polish
**Builds:** Balanced power-up system.

---

## Phase 5: Level Design (Units 65-80)

### Unit 65: Level Data Format
**Builds:** Efficient level storage.
**Teaches:** Data-driven levels.
**Code pattern:**
```asm
; Level format: 6 rows × 18 columns = 108 bytes
; 0 = empty, 1 = normal, 2 = hard, 3 = unbreakable
level_01:
    !byte 1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1
    !byte 1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1
    !byte 2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2
    !byte 1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1
    !byte 1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1
    !byte 1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1

level_pointers_lo:
    !byte <level_01, <level_02, <level_03
    ; ... etc
level_pointers_hi:
    !byte >level_01, >level_02, >level_03
```

---

### Unit 66: Level Loading
**Builds:** Draw level from data.
**Teaches:** Data-to-screen.

---

### Unit 67-76: Levels 1-10
**Builds:** Varied level designs.
**Teaches:** Level design iteration.

---

### Unit 77-78: Levels 11-20
**Builds:** Expert challenges.
**Teaches:** Difficulty curve.

---

### Unit 79: Level Transitions
**Builds:** Effects between levels.
**Teaches:** Polish transitions.

---

### Unit 80: Phase 5 Polish
**Builds:** 20 complete levels.

---

## Phase 6: Audio and Features (Units 81-96)

### Unit 81: Sound System
**Builds:** Channel management.
**Teaches:** Audio architecture.

---

### Unit 82-85: Sound Effects
**Builds:** Full SFX set.
**Teaches:** Sound design.

---

### Unit 86: Music - Title Theme
**Builds:** Catchy title music.
**Teaches:** SID music.

---

### Unit 87: Music - In-Game
**Builds:** Background music.
**Teaches:** Game music.

---

### Unit 88: Music/SFX Balance
**Builds:** Sounds work with music.
**Teaches:** Audio mixing.

---

### Unit 89: Title Screen
**Builds:** Attractive presentation.
**Teaches:** Title design.

---

### Unit 90: High Score Table
**Builds:** Top scores.
**Teaches:** Score display.

---

### Unit 91: High Score Entry
**Builds:** Name entry.
**Teaches:** Text input.

---

### Unit 92: Pause Feature
**Builds:** Mid-game pause.
**Teaches:** Pause implementation.

---

### Unit 93: Two-Player Mode
**Builds:** Alternating play.
**Teaches:** Multiplayer.

---

### Unit 94: Difficulty Options
**Builds:** Easy/Normal/Hard.
**Teaches:** Settings.

---

### Unit 95: Continue System
**Builds:** Continue option.
**Teaches:** Continues.

---

### Unit 96: Phase 6 Polish
**Builds:** Complete features.

---

## Phase 7: Optimisation (Units 97-112)

### Unit 97: Frame Rate Check
**Builds:** Solid 50/60fps.
**Teaches:** Performance.

---

### Unit 98: Collision Optimisation
**Builds:** Faster brick checks.
**Teaches:** Efficiency.

---

### Unit 99: Memory Layout
**Builds:** Optimal organisation.
**Teaches:** Memory planning.

---

### Unit 100: Difficulty Balance
**Builds:** Fair challenge.
**Teaches:** Balance.

---

### Unit 101-104: Tuning
**Builds:** Speed, power-ups, controls.
**Teaches:** Polish iteration.

---

### Unit 105-108: Bug Fixes
**Builds:** Find and fix issues.
**Teaches:** Debugging.

---

### Unit 109-111: Polish
**Builds:** Visual and audio consistency.
**Teaches:** Final polish.

---

### Unit 112: Phase 7 Complete
**Builds:** Stable, balanced game.

---

## Phase 8: Release (Units 113-128)

### Unit 113-116: Presentation
**Builds:** Title art, instructions, credits.
**Teaches:** Professional presentation.

---

### Unit 117-120: Testing
**Builds:** Emulator and hardware testing.
**Teaches:** Quality assurance.

---

### Unit 121-124: Final Polish
**Builds:** Easter eggs, cheats, fixes.
**Teaches:** Release preparation.

---

### Unit 125-127: Documentation
**Builds:** Manual, packaging concept.
**Teaches:** Distribution preparation.

---

### Unit 128: Release
**Builds:** Final release.
**Teaches:** Shipping a game.

---

## Version History

- **1.0 (2026-01-18):** Initial 128-unit outline created.
