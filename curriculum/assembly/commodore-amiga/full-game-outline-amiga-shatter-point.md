# Amiga Game 3: Shatter Point - Full 128-Unit Outline

**Platform:** Commodore Amiga
**Game:** Shatter Point
**Units:** 128 (8 phases × 16 units)
**Concept:** Breakout clone with Amiga audiovisual flair. Paddle, ball, bricks - with Copper gradient backgrounds, sampled sound effects, and smooth 50fps gameplay.

---

## Overview

Shatter Point applies the Blitter skills from Games 1-2 to ball physics and background manipulation. While the shooter and timing games used sprites and BOBs for moving objects, breakout introduces precise physics calculations and the satisfying destruction of background elements.

**Key Learning Goals:**
- Ball physics with fixed-point maths (smooth sub-pixel movement)
- Blitter fills for brick rendering and destruction
- Copper gradient backgrounds (dynamic sky effects)
- Paula sample playback for impacts
- Power-up systems
- Paddle control feel and responsiveness

---

## Phase 1: Ball and Paddle Foundation (Units 1-16)

### Unit 1: The Brick Wall
**Builds:** Colourful brick field using Blitter fills.
**Teaches:** Blitter area fill for rectangles.
**Code pattern:**
```asm
; Draw a brick using Blitter fill
; Each brick: 32x8 pixels
BLTCON0 = $dff040
BLTCON1 = $dff042
BLTDPT  = $dff054
BLTDMOD = $dff066
BLTSIZE = $dff058

draw_brick:
    ; Wait for Blitter
    btst    #6,$dff002
    bne.s   draw_brick

    ; Set up destination
    move.l  brick_address,BLTDPT
    move.w  #SCREEN_WIDTH-4,BLTDMOD     ; Modulo (40-4 bytes)

    ; Solid colour fill
    move.w  #$0100,BLTCON0              ; D=0 (clear first)
    move.w  #$0000,BLTCON1
    move.w  #(8<<6)|2,BLTSIZE           ; 8 rows, 2 words wide
    rts
```
**If it doesn't work:** Bricks not appearing? Check Blitter DMA enabled ($DFF096). Wrong size? Verify BLTSIZE calculation (rows×64 + words).

---

### Unit 2: Brick Colour via Copper
**Builds:** Different colour bands for brick rows using Copper.
**Teaches:** Copper colour changes per scanline.
**Code pattern:**
```asm
; Copper list with colour changes for brick rows
copper_list:
    dc.w    $2c01,$fffe     ; Wait line 44
    dc.w    $0180,$0f00     ; COLOR00 = red bricks
    dc.w    $3401,$fffe     ; Wait line 52
    dc.w    $0180,$0f50     ; Orange
    dc.w    $3c01,$fffe     ; Wait line 60
    dc.w    $0180,$0ff0     ; Yellow
    dc.w    $4401,$fffe     ; Wait line 68
    dc.w    $0180,$00f0     ; Green
    dc.w    $4c01,$fffe     ; Wait line 76
    dc.w    $0180,$00ff     ; Cyan
    dc.w    $5401,$fffe     ; Wait line 84
    dc.w    $0180,$000f     ; Blue
    dc.w    $ffff,$fffe     ; End
```
**If it doesn't work:** All same colour? Check Copper enabled and list pointer set. Colours at wrong lines? Adjust WAIT commands.

---

### Unit 3: Paddle Setup
**Builds:** Paddle at bottom of screen as a BOB.
**Teaches:** BOB for player-controlled element.
**Code pattern:**
```asm
; Paddle: 48x8 pixels BOB
paddle_x:       dc.w    136     ; Center of screen
paddle_y:       dc.w    232     ; Near bottom
PADDLE_WIDTH    equ     48

draw_paddle:
    ; Calculate screen address
    move.w  paddle_y,d0
    mulu    #SCREEN_WIDTH,d0
    add.l   #screen,d0
    move.w  paddle_x,d1
    lsr.w   #3,d1               ; /8 for byte offset
    add.w   d1,d0

    ; Blitter copy paddle BOB
    ; ... setup Blitter for cookie-cut
    rts
```
**If it doesn't work:** Paddle not visible? Check screen address calculation. Corrupted? Verify Blitter masking for edges.

---

### Unit 4: Paddle Movement
**Builds:** Joystick moves paddle left/right.
**Teaches:** Smooth joystick control.
**Code pattern:**
```asm
PADDLE_SPEED    equ     4
PADDLE_MIN      equ     16
PADDLE_MAX      equ     272     ; 320-48

update_paddle:
    ; Clear old paddle
    bsr     clear_paddle

    ; Read joystick
    move.w  $dff00c,d0          ; JOY1DAT
    btst    #1,d0               ; Right
    beq.s   .check_left
    add.w   #PADDLE_SPEED,paddle_x
    cmp.w   #PADDLE_MAX,paddle_x
    ble.s   .draw
    move.w  #PADDLE_MAX,paddle_x
    bra.s   .draw

.check_left:
    btst    #9,d0               ; Left
    beq.s   .draw
    sub.w   #PADDLE_SPEED,paddle_x
    cmp.w   #PADDLE_MIN,paddle_x
    bge.s   .draw
    move.w  #PADDLE_MIN,paddle_x

.draw:
    bsr     draw_paddle
    rts
```
**If it doesn't work:** Not responding? Check JOY1DAT address. Wrong direction? Verify bit positions for left/right.

---

### Unit 5: Ball Sprite
**Builds:** Ball displayed using hardware sprite.
**Teaches:** Hardware sprite setup for small moving object.
**Code pattern:**
```asm
; Ball uses hardware sprite 0
; Sprite data in chip RAM
ball_sprite:
    dc.w    0,0                 ; Control words (filled at runtime)
    dc.w    %0000011000000000,%0000011000000000
    dc.w    %0001111110000000,%0000111100000000
    dc.w    %0011111111000000,%0001111110000000
    dc.w    %0011111111000000,%0001111110000000
    dc.w    %0001111110000000,%0000111100000000
    dc.w    %0000011000000000,%0000011000000000
    dc.w    0,0                 ; End of sprite

ball_x:     dc.w    160
ball_y:     dc.w    160

update_ball_sprite:
    ; Set sprite position in control words
    move.w  ball_y,d0
    move.w  ball_x,d1
    ; ... encode into sprite control
    rts
```
**If it doesn't work:** Sprite not visible? Check sprite DMA enabled and pointer registers set. Position wrong? Verify HSTART/VSTART encoding.

---

### Unit 6: Ball Movement
**Builds:** Ball moves in a direction.
**Teaches:** Velocity application.
**Code pattern:**
```asm
ball_vel_x:     dc.w    2       ; Pixels per frame
ball_vel_y:     dc.w    -2      ; Negative = upward

update_ball:
    move.w  ball_x,d0
    add.w   ball_vel_x,d0
    move.w  d0,ball_x

    move.w  ball_y,d0
    add.w   ball_vel_y,d0
    move.w  d0,ball_y

    bsr     update_ball_sprite
    rts
```
**If it doesn't work:** Ball not moving? Check velocity not zero. Sprite not updating? Ensure control words recalculated.

---

### Unit 7: Wall Bouncing
**Builds:** Ball bounces off screen edges.
**Teaches:** Boundary collision.
**Code pattern:**
```asm
check_walls:
    ; Left wall
    move.w  ball_x,d0
    cmp.w   #16,d0
    bge.s   .check_right
    neg.w   ball_vel_x
    move.w  #16,ball_x

.check_right:
    cmp.w   #304,d0
    ble.s   .check_top
    neg.w   ball_vel_x
    move.w  #304,ball_x

.check_top:
    move.w  ball_y,d0
    cmp.w   #32,d0
    bge.s   .done
    neg.w   ball_vel_y
    move.w  #32,ball_y

.done:
    rts
```
**If it doesn't work:** Going through wall? Check comparison values match screen bounds. Not reversing? Verify NEG instruction works on word.

---

### Unit 8: Ball Lost Detection
**Builds:** Ball below paddle loses life.
**Teaches:** Miss detection.

---

### Unit 9: Paddle Collision
**Builds:** Ball bounces off paddle.
**Teaches:** Rectangle collision.
**Code pattern:**
```asm
check_paddle:
    ; Is ball at paddle Y level?
    move.w  ball_y,d0
    cmp.w   #228,d0             ; Paddle Y - some margin
    blt.s   .no_hit
    cmp.w   #240,d0             ; Below paddle
    bgt.s   .no_hit

    ; Is ball within paddle X range?
    move.w  ball_x,d0
    move.w  paddle_x,d1
    sub.w   #4,d1               ; Ball radius
    cmp.w   d1,d0
    blt.s   .no_hit
    add.w   #PADDLE_WIDTH,d1
    add.w   #8,d1               ; Ball width
    cmp.w   d1,d0
    bgt.s   .no_hit

    ; Hit!
    neg.w   ball_vel_y
    bsr     sound_paddle

.no_hit:
    rts
```
**If it doesn't work:** Not bouncing? Check Y range covers ball descent speed. Going through? Increase collision zone.

---

### Unit 10: Brick Collision Detection
**Builds:** Detect when ball hits brick area.
**Teaches:** Position-to-grid conversion.
**Code pattern:**
```asm
; Brick grid: 10 columns × 6 rows
; Each brick: 32×8 pixels
; Grid starts at X=0, Y=32
BRICK_WIDTH     equ     32
BRICK_HEIGHT    equ     8
BRICKS_X        equ     0
BRICKS_Y        equ     32

check_brick_hit:
    ; Is ball in brick area?
    move.w  ball_y,d0
    cmp.w   #BRICKS_Y,d0
    blt.s   .no_hit
    cmp.w   #BRICKS_Y+(6*BRICK_HEIGHT),d0
    bge.s   .no_hit

    ; Calculate row
    sub.w   #BRICKS_Y,d0
    divu    #BRICK_HEIGHT,d0
    move.w  d0,brick_row

    ; Calculate column
    move.w  ball_x,d0
    divu    #BRICK_WIDTH,d0
    move.w  d0,brick_col

    ; Check if brick exists at this position
    bsr     get_brick_status
    tst.b   d0
    beq.s   .no_hit

    ; Hit brick!
    bsr     destroy_brick
    neg.w   ball_vel_y

.no_hit:
    rts
```
**If it doesn't work:** Wrong brick hit? Check division and grid offset. Missing bricks? Verify ball centre used for detection.

---

### Unit 11: Brick Destruction
**Builds:** Clear brick from screen.
**Teaches:** Blitter clear operations.
**Code pattern:**
```asm
; Mark brick as destroyed and clear from screen
destroy_brick:
    ; Mark in grid
    move.w  brick_row,d0
    mulu    #10,d0              ; 10 columns
    add.w   brick_col,d0
    lea     brick_grid,a0
    clr.b   (a0,d0.w)

    ; Calculate screen position
    move.w  brick_row,d0
    mulu    #BRICK_HEIGHT,d0
    add.w   #BRICKS_Y,d0
    mulu    #SCREEN_WIDTH,d0

    move.w  brick_col,d1
    mulu    #BRICK_WIDTH/8,d1   ; Bytes per brick
    add.w   d1,d0
    add.l   #screen,d0

    ; Blitter clear
    ; ... clear 32×8 pixels
    rts
```
**If it doesn't work:** Wrong brick cleared? Check address calculation. Partial clear? Verify Blitter size.

---

### Unit 12: Brick Counter
**Builds:** Track remaining bricks for win condition.
**Teaches:** Game state tracking.

---

### Unit 13: Lives System
**Builds:** Three lives, displayed at bottom.
**Teaches:** Life tracking.

---

### Unit 14: Score System
**Builds:** Points for bricks, displayed on screen.
**Teaches:** Score tracking.

---

### Unit 15: Sound - Paddle Hit
**Builds:** Sample plays on paddle contact.
**Teaches:** Paula sample playback.
**Code pattern:**
```asm
; Play sample on channel 0
AUD0LCH = $dff0a0
AUD0LEN = $dff0a4
AUD0PER = $dff0a6
AUD0VOL = $dff0a8

sound_paddle:
    lea     paddle_sample,a0
    move.l  a0,AUD0LCH
    move.w  #PADDLE_SAMPLE_LEN/2,AUD0LEN
    move.w  #256,AUD0PER        ; Period (pitch)
    move.w  #64,AUD0VOL         ; Full volume

    ; Trigger playback
    move.w  #$8001,$dff096      ; DMACON - enable audio 0
    rts
```
**If it doesn't work:** No sound? Check audio DMA enabled. Wrong pitch? Adjust period value.

---

### Unit 16: Phase 1 Polish
**Builds:** Basic game loop working.
**If it doesn't work:** Ball behaving strangely? Check all collision checks run in correct order.

---

## Phase 2: Physics Refinement (Units 17-32)

### Unit 17: Fixed-Point Ball Position
**Builds:** Sub-pixel ball movement for smoothness.
**Teaches:** 16.16 fixed-point maths.
**Code pattern:**
```asm
; 16.16 fixed point: high word = pixels, low word = fraction
ball_x_fp:      dc.l    160<<16     ; 160.0
ball_y_fp:      dc.l    160<<16     ; 160.0
ball_vel_x_fp:  dc.l    $00018000   ; 1.5 pixels per frame
ball_vel_y_fp:  dc.l    $FFFE8000   ; -1.5 pixels per frame

update_ball_fixed:
    ; X += vel_x
    move.l  ball_x_fp,d0
    add.l   ball_vel_x_fp,d0
    move.l  d0,ball_x_fp
    swap    d0
    move.w  d0,ball_x           ; Integer part for display

    ; Y += vel_y
    move.l  ball_y_fp,d0
    add.l   ball_vel_y_fp,d0
    move.l  d0,ball_y_fp
    swap    d0
    move.w  d0,ball_y
    rts
```
**If it doesn't work:** Jerky movement? Make sure velocity has fractional component. Drifting? Check signed arithmetic for negative velocities.

---

### Unit 18: Ball Speed Progression
**Builds:** Ball speeds up over time.
**Teaches:** Dynamic difficulty.

---

### Unit 19: Paddle Angle Control
**Builds:** Hit position affects bounce angle.
**Teaches:** Angle based on collision offset.
**Code pattern:**
```asm
; Angle based on where ball hits paddle
; Center = straight up, edges = sharp angle
calculate_angle:
    move.w  ball_x,d0
    sub.w   paddle_x,d0         ; Offset from paddle left
    sub.w   #PADDLE_WIDTH/2,d0  ; Center offset

    ; Scale offset to velocity
    ; d0 now -24 to +24
    asr.w   #3,d0               ; /8 for reasonable velocity
    add.w   d0,ball_vel_x_fp+2  ; Add to fractional X velocity

    ; Ensure minimum upward velocity
    move.l  ball_vel_y_fp,d0
    cmp.l   #$FFFF0000,d0       ; At least -1 pixel
    blt.s   .ok
    move.l  #$FFFF0000,ball_vel_y_fp
.ok:
    rts
```
**If it doesn't work:** Always same angle? Check offset calculation from paddle centre. Too extreme? Reduce scaling factor.

---

### Unit 20: Ball Spin from Paddle
**Builds:** Moving paddle adds spin.
**Teaches:** Velocity transfer.

---

### Unit 21: Brick Side Detection
**Builds:** Determine which side of brick was hit.
**Teaches:** Multi-direction collision response.

---

### Unit 22: Corner Collision
**Builds:** Corner hits bounce diagonally.
**Teaches:** Corner case handling.

---

### Unit 23: Multi-Brick Hits
**Builds:** Ball can hit multiple bricks per frame.
**Teaches:** Multiple collision handling.

---

### Unit 24: Stuck Prevention
**Builds:** Prevent ball embedding in bricks.
**Teaches:** Position correction.

---

### Unit 25: Launch System
**Builds:** Ball sticks to paddle until launched.
**Teaches:** Serve mechanic.
**Code pattern:**
```asm
serving:        dc.w    1       ; 1 = ball on paddle

update_serve:
    tst.w   serving
    beq.s   .playing

    ; Ball follows paddle
    move.w  paddle_x,d0
    add.w   #PADDLE_WIDTH/2,d0
    move.w  d0,ball_x

    move.w  #220,ball_y         ; Just above paddle

    ; Fire button launches
    btst    #7,$bfe001          ; Fire button
    bne.s   .done

    ; Launch!
    clr.w   serving
    ; Set initial velocity
    move.l  #$FFFE0000,ball_vel_y_fp    ; -2 upward
    move.l  #$00010000,ball_vel_x_fp    ; 1 right

.done:
.playing:
    rts
```
**If it doesn't work:** Ball not following? Check serve state flag. Not launching? Verify fire button read.

---

### Unit 26: Launch Direction Indicator
**Builds:** Arrow shows launch angle.
**Teaches:** Player feedback.

---

### Unit 27: Tight Paddle Control
**Builds:** Responsive, precise movement.
**Teaches:** Control feel.

---

### Unit 28: Ball Trail Effect
**Builds:** Afterimage as ball moves.
**Teaches:** Visual effects.

---

### Unit 29: Brick Hit Flash
**Builds:** Brief flash when brick destroyed.
**Teaches:** Impact feedback.

---

### Unit 30: Sound - Brick Hit
**Builds:** Different sample for bricks.
**Teaches:** Sound variety.

---

### Unit 31: Sound - Wall Bounce
**Builds:** Distinct wall sound.
**Teaches:** Audio feedback.

---

### Unit 32: Phase 2 Polish
**Builds:** Satisfying physics feel.

---

## Phase 3: Brick Variety (Units 33-48)

### Unit 33: Brick Colours
**Builds:** Multiple brick colours via Copper.
**Teaches:** Colour variety.

---

### Unit 34: Brick Point Values
**Builds:** Different colours = different points.
**Teaches:** Scoring variety.

---

### Unit 35: Hard Bricks
**Builds:** Bricks requiring two hits.
**Teaches:** Hit points.
**Code pattern:**
```asm
; Brick grid stores health: 0=empty, 1=normal, 2=hard
brick_grid:     dcb.b   60,1    ; 6×10 grid, all normal

damage_brick:
    ; Get brick index
    move.w  brick_row,d0
    mulu    #10,d0
    add.w   brick_col,d0

    lea     brick_grid,a0
    subq.b  #1,(a0,d0.w)        ; Reduce health
    bne.s   .not_destroyed

    ; Destroyed
    dec.w   bricks_remaining
    bsr     clear_brick
    bsr     add_score
    bra.s   .done

.not_destroyed:
    ; Change to cracked appearance
    bsr     draw_cracked_brick

.done:
    rts
```

---

### Unit 36: Cracked Brick Visual
**Builds:** Hard bricks show damage.
**Teaches:** State-based visuals.

---

### Unit 37: Unbreakable Bricks
**Builds:** Metal bricks never break.
**Teaches:** Obstacles.

---

### Unit 38: Explosive Bricks
**Builds:** Red bricks destroy neighbours.
**Teaches:** Chain reactions.

---

### Unit 39: Explosive Effect
**Builds:** Explosion animation.
**Teaches:** Particle effects with Blitter.

---

### Unit 40: Moving Brick Row
**Builds:** Top row moves side to side.
**Teaches:** Dynamic backgrounds.

---

### Unit 41: Regenerating Bricks
**Builds:** Ghostly bricks return after time.
**Teaches:** Timed respawns.

---

### Unit 42: Hidden Bricks
**Builds:** Invisible until ball nearby.
**Teaches:** Reveal mechanics.

---

### Unit 43: Brick Patterns
**Builds:** Creative arrangements.
**Teaches:** Level design.

---

### Unit 44: Row Clear Bonus
**Builds:** Clear full row for bonus.
**Teaches:** Combo bonuses.

---

### Unit 45: Score Multiplier
**Builds:** Consecutive hits build multiplier.
**Teaches:** Score chains.

---

### Unit 46: Brick Break Animation
**Builds:** Bricks crumble when destroyed.
**Teaches:** Destruction animation.

---

### Unit 47: Background Variety
**Builds:** Different Copper backgrounds per level.
**Teaches:** Level theming.

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
; Power-up falls from brick position
powerup_active: dc.w    0
powerup_x:      dc.w    0
powerup_y:      dc.w    0
powerup_type:   dc.w    0
POWERUP_SPEED   equ     2

spawn_powerup:
    ; 20% chance
    bsr     random
    and.w   #$7,d0
    cmp.w   #1,d0
    bgt.s   .no_spawn

    ; Spawn at brick position
    move.w  brick_row,d0
    mulu    #BRICK_HEIGHT,d0
    add.w   #BRICKS_Y,d0
    move.w  d0,powerup_y

    move.w  brick_col,d0
    mulu    #BRICK_WIDTH,d0
    add.w   #16,d0              ; Center of brick
    move.w  d0,powerup_x

    ; Random type (0-7)
    bsr     random
    and.w   #7,d0
    move.w  d0,powerup_type

    move.w  #1,powerup_active

.no_spawn:
    rts
```

---

### Unit 50: Power-Up Falling
**Builds:** Item falls toward paddle.
**Teaches:** Item gravity.

---

### Unit 51: Power-Up Collection
**Builds:** Paddle catches item.
**Teaches:** Item collision.

---

### Unit 52: Power-Up - Extend
**Builds:** Paddle grows wider.
**Teaches:** Player enhancement.

---

### Unit 53: Power-Up - Shrink
**Builds:** Paddle gets smaller.
**Teaches:** Negative items.

---

### Unit 54: Power-Up - Multi-Ball
**Builds:** Ball splits into three.
**Teaches:** Multiple ball management.
**Code pattern:**
```asm
MAX_BALLS       equ     3
num_balls:      dc.w    1
ball_active:    dc.w    1,0,0   ; Which balls are in play

spawn_multi_ball:
    cmp.w   #MAX_BALLS,num_balls
    bge.s   .done

    ; Clone current ball with different angles
    move.w  #1,ball_active+2    ; Activate ball 2
    move.w  #1,ball_active+4    ; Activate ball 3

    ; Ball 2: steeper angle
    move.l  ball_x_fp,ball2_x_fp
    move.l  ball_y_fp,ball2_y_fp
    move.l  #$00020000,ball2_vel_x_fp

    ; Ball 3: other direction
    move.l  ball_x_fp,ball3_x_fp
    move.l  ball_y_fp,ball3_y_fp
    move.l  #$FFFE0000,ball3_vel_x_fp

    move.w  #3,num_balls

.done:
    rts
```

---

### Unit 55: Multi-Ball Logic
**Builds:** All balls active until all lost.
**Teaches:** Entity arrays.

---

### Unit 56: Power-Up - Catch
**Builds:** Ball sticks, can re-aim.
**Teaches:** State modifier.

---

### Unit 57: Power-Up - Laser
**Builds:** Paddle fires lasers.
**Teaches:** Weapon power-up.

---

### Unit 58: Laser Firing
**Builds:** Fire button shoots lasers.
**Teaches:** Projectile spawning.

---

### Unit 59: Power-Up - Slow
**Builds:** Ball slows down.
**Teaches:** Speed modifier.

---

### Unit 60: Power-Up - Warp
**Builds:** Skip to next level.
**Teaches:** Level skip.

---

### Unit 61: Power-Up - Extra Life
**Builds:** Rare 1-up.
**Teaches:** High-value items.

---

### Unit 62: Power-Up Timer
**Builds:** Some power-ups are temporary.
**Teaches:** Timed effects.

---

### Unit 63: Power-Up Display
**Builds:** Show active power-up.
**Teaches:** Status HUD.

---

### Unit 64: Phase 4 Polish
**Builds:** Balanced power-up system.

---

## Phase 5: Level Design (Units 65-80)

### Unit 65: Level Data Format
**Builds:** Efficient level storage.
**Teaches:** Level data structures.

---

### Unit 66: Level Loading
**Builds:** Draw level from data.
**Teaches:** Data-driven content.

---

### Unit 67: Level 1 - Classic
**Builds:** Standard brick layout.
**Teaches:** Baseline design.

---

### Unit 68: Level 2 - Pyramid
**Builds:** Triangular formation.
**Teaches:** Shape variety.

---

### Unit 69: Level 3 - Fortress
**Builds:** Unbreakable walls.
**Teaches:** Obstacle design.

---

### Unit 70: Levels 4-10
**Builds:** Varied designs.
**Teaches:** Design iteration.

---

### Unit 71: Levels 11-15
**Builds:** Intermediate difficulty.
**Teaches:** Difficulty curve.

---

### Unit 72: Levels 16-20
**Builds:** Expert challenges.
**Teaches:** Expert design.

---

### Unit 73: Level Copper Themes
**Builds:** Different gradients per level.
**Teaches:** Visual theming.

---

### Unit 74: Level Transitions
**Builds:** Effects between levels.
**Teaches:** Polish.

---

### Unit 75: Boss Level
**Builds:** Special challenge.
**Teaches:** Boss design.

---

### Unit 76: Bonus Stages
**Builds:** Point collection levels.
**Teaches:** Variety.

---

### Unit 77: Level Select (Debug)
**Builds:** Jump to any level.
**Teaches:** Dev tools.

---

### Unit 78: Level Progression
**Builds:** Sequential unlock.
**Teaches:** Progression.

---

### Unit 79: Endless Mode
**Builds:** Procedural levels.
**Teaches:** Random generation.

---

### Unit 80: Phase 5 Polish
**Builds:** 20 complete levels.

---

## Phase 6: Audio and Features (Units 81-96)

### Unit 81: Sound System
**Builds:** Channel management.
**Teaches:** Audio architecture.

---

### Unit 82: Sound - Various Impacts
**Builds:** Different sounds for different bricks.
**Teaches:** Sound variety.

---

### Unit 83: Sound - Power-Up Collect
**Builds:** Positive collection sound.
**Teaches:** Reward audio.

---

### Unit 84: Sound - Ball Lost
**Builds:** Negative feedback.
**Teaches:** Failure audio.

---

### Unit 85: Sound - Level Complete
**Builds:** Victory fanfare.
**Teaches:** Achievement audio.

---

### Unit 86: Music - Title Theme
**Builds:** MOD music for title.
**Teaches:** MOD replay basics.

---

### Unit 87: Music - In-Game
**Builds:** Background music.
**Teaches:** Game music.

---

### Unit 88: Music/SFX Mixing
**Builds:** Sounds don't interrupt music.
**Teaches:** Channel allocation.

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

## Phase 7: Optimisation and Balance (Units 97-112)

### Unit 97: Frame Rate Check
**Builds:** Solid 50fps.
**Teaches:** Performance.

---

### Unit 98: Blitter Optimisation
**Builds:** Efficient brick clearing.
**Teaches:** Blitter efficiency.

---

### Unit 99: Collision Optimisation
**Builds:** Faster checks.
**Teaches:** Algorithm efficiency.

---

### Unit 100: Memory Layout
**Builds:** Optimal organisation.
**Teaches:** Memory planning.

---

### Unit 101: Difficulty Balance
**Builds:** Fair challenge.
**Teaches:** Balance.

---

### Unit 102: Ball Speed Tuning
**Builds:** Right progression.
**Teaches:** Speed balance.

---

### Unit 103: Power-Up Balance
**Builds:** Right rates.
**Teaches:** Item balance.

---

### Unit 104: Control Feel
**Builds:** Tight paddle.
**Teaches:** Input feel.

---

### Unit 105: Bug Hunting
**Builds:** Find issues.
**Teaches:** Debugging.

---

### Unit 106: Edge Cases
**Builds:** Handle unusual situations.
**Teaches:** Robustness.

---

### Unit 107: Playtest Feedback
**Builds:** Implement suggestions.
**Teaches:** Iteration.

---

### Unit 108: Multi-Ball Testing
**Builds:** Handle 3 balls smoothly.
**Teaches:** Entity testing.

---

### Unit 109: Audio Balance
**Builds:** Volume levels.
**Teaches:** Audio mix.

---

### Unit 110: Visual Consistency
**Builds:** Cohesive look.
**Teaches:** Visual polish.

---

### Unit 111: Code Cleanup
**Builds:** Well-organised.
**Teaches:** Code quality.

---

### Unit 112: Phase 7 Polish
**Builds:** Stable game.

---

## Phase 8: Release (Units 113-128)

### Unit 113: Title Art
**Builds:** Eye-catching logo.
**Teaches:** Title design.

---

### Unit 114: Instructions
**Builds:** How to play.
**Teaches:** Onboarding.

---

### Unit 115: Credits
**Builds:** Attribution.
**Teaches:** Credits.

---

### Unit 116: ADF Creation
**Builds:** Bootable disk.
**Teaches:** Distribution format.

---

### Unit 117: Build Process
**Builds:** Final assembly.
**Teaches:** Build automation.

---

### Unit 118: Emulator Testing
**Builds:** Multiple emulators.
**Teaches:** Compatibility.

---

### Unit 119: Hardware Testing
**Builds:** Real Amiga.
**Teaches:** Hardware verification.

---

### Unit 120: Easter Eggs
**Builds:** Hidden features.
**Teaches:** Secrets.

---

### Unit 121: Cheat Codes
**Builds:** Debug cheats.
**Teaches:** Cheat systems.

---

### Unit 122: OCS/ECS Compatibility
**Builds:** Works on all Amigas.
**Teaches:** Compatibility.

---

### Unit 123: Release Candidate
**Builds:** Final test.
**Teaches:** Release process.

---

### Unit 124: Final Fixes
**Builds:** Last adjustments.
**Teaches:** Polish.

---

### Unit 125: Documentation
**Builds:** Manual.
**Teaches:** Documentation.

---

### Unit 126: Box Art Concept
**Builds:** Cover design.
**Teaches:** Marketing.

---

### Unit 127: Community Feedback
**Builds:** Beta testing.
**Teaches:** Community.

---

### Unit 128: Release
**Builds:** Final release.
**Teaches:** Shipping.

---

## Version History

- **1.0 (2026-01-18):** Initial 128-unit outline created.
