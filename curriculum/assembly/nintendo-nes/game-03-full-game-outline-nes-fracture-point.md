# NES Game 3: Fracture Point - Full 128-Unit Outline

**Platform:** Nintendo Entertainment System
**Game:** Fracture Point
**Units:** 128 (8 phases × 16 units)
**Concept:** Breakout clone with NES flair. Paddle, ball, bricks. Clear the screen before the ball breaks through. Tension builds to the fracture point.

---

## Overview

Fracture Point teaches ball physics and background tile manipulation. After sprites in Games 1-2, learners now master dynamic backgrounds - the ball destroys bricks by modifying the nametable in real-time. This is a different relationship with PPU memory.

**Key Learning Goals:**
- Ball physics (velocity, angles, reflection)
- Background tile modification (bricks disappear)
- Paddle control with precise collision
- Fixed-point maths for smooth ball movement
- Power-up systems
- APU sound design for impacts

---

## Phase 1: Ball and Paddle Basics (Units 1-16)

### Unit 1: The Brick Wall
**Builds:** Static screen of bricks using background tiles.
**Teaches:** Nametable setup, pattern table for brick graphics.
**Code pattern:**
```asm
; Set up brick rows at top of screen
; Bricks are 2x1 tiles (16x8 pixels)
BRICK_TILE_L = $01
BRICK_TILE_R = $02
EMPTY_TILE   = $00

draw_bricks:
    lda #$20
    sta $2006       ; PPU address high
    lda #$42        ; Row 2, column 2
    sta $2006       ; PPU address low

    ldx #14         ; 14 bricks per row
@row:
    lda #BRICK_TILE_L
    sta $2007
    lda #BRICK_TILE_R
    sta $2007
    dex
    bne @row
    rts
```
**If it doesn't work:** Bricks not showing? Check PPU address is correct. Wrong tiles? Verify pattern table has brick graphics.

---

### Unit 2: Paddle Sprite
**Builds:** Paddle at bottom of screen that player controls.
**Teaches:** Sprite (OAM) setup for paddle.
**Code pattern:**
```asm
; Paddle uses sprites (can be multiple for width)
PADDLE_Y = 208      ; Near bottom
paddle_x: .byte 120 ; Center start

init_paddle:
    ; Sprite 0: Left part of paddle
    lda #PADDLE_Y
    sta $0200       ; Y
    lda #$10        ; Paddle tile
    sta $0201       ; Tile
    lda #$00        ; Attributes
    sta $0202
    lda paddle_x
    sta $0203       ; X

    ; Sprite 1: Right part
    lda #PADDLE_Y
    sta $0204
    lda #$11        ; Right paddle tile
    sta $0205
    lda #$00
    sta $0206
    lda paddle_x
    clc
    adc #8
    sta $0207       ; X + 8
    rts
```
**If it doesn't work:** Paddle not visible? Check OAM DMA runs each frame. Wrong position? Verify sprite Y coordinate (NES Y is top of sprite).

---

### Unit 3: Paddle Movement
**Builds:** Paddle moves left/right with controller.
**Teaches:** Controller reading, position updates.
**Code pattern:**
```asm
PADDLE_SPEED = 3
PADDLE_MIN = 8
PADDLE_MAX = 232

update_paddle:
    lda controller
    and #BUTTON_LEFT
    beq @check_right

    ; Move left
    lda paddle_x
    sec
    sbc #PADDLE_SPEED
    cmp #PADDLE_MIN
    bcs @store
    lda #PADDLE_MIN
    jmp @store

@check_right:
    lda controller
    and #BUTTON_RIGHT
    beq @done

    ; Move right
    lda paddle_x
    clc
    adc #PADDLE_SPEED
    cmp #PADDLE_MAX
    bcc @store
    lda #PADDLE_MAX

@store:
    sta paddle_x
    ; Update sprite X positions
    sta $0203
    clc
    adc #8
    sta $0207

@done:
    rts
```
**If it doesn't work:** Paddle not moving? Check controller reading latch ($4016). Going off screen? Verify boundary checks.

---

### Unit 4: Ball Sprite
**Builds:** Ball appears on screen.
**Teaches:** Additional sprite setup.
**Code pattern:**
```asm
ball_x: .byte 128   ; Starting position
ball_y: .byte 120

init_ball:
    ; Sprite 2: Ball
    lda ball_y
    sta $0208       ; Y
    lda #$20        ; Ball tile
    sta $0209
    lda #$00        ; Attributes
    sta $020A
    lda ball_x
    sta $020B       ; X
    rts
```

---

### Unit 5: Ball Movement
**Builds:** Ball moves in a direction.
**Teaches:** Velocity application.
**Code pattern:**
```asm
ball_vel_x: .byte 1     ; Pixels per frame
ball_vel_y: .byte $FF   ; Negative = upward

update_ball:
    ; Update X
    lda ball_x
    clc
    adc ball_vel_x
    sta ball_x
    sta $020B

    ; Update Y
    lda ball_y
    clc
    adc ball_vel_y
    sta ball_y
    sta $0208
    rts
```
**If it doesn't work:** Ball not moving? Check velocity isn't zero. Moving wrong way? Verify signed arithmetic.

---

### Unit 6: Wall Bouncing
**Builds:** Ball bounces off side walls.
**Teaches:** Boundary collision, velocity reversal.
**Code pattern:**
```asm
check_walls:
    ; Left wall
    lda ball_x
    cmp #8
    bcs @check_right
    lda #0
    sec
    sbc ball_vel_x
    sta ball_vel_x  ; Reverse X
    lda #8
    sta ball_x

@check_right:
    lda ball_x
    cmp #248
    bcc @check_top
    lda #0
    sec
    sbc ball_vel_x
    sta ball_vel_x
    lda #247
    sta ball_x

@check_top:
    lda ball_y
    cmp #16         ; Top boundary
    bcs @done
    lda #0
    sec
    sbc ball_vel_y
    sta ball_vel_y
    lda #16
    sta ball_y

@done:
    rts
```
**If it doesn't work:** Ball going through wall? Check comparison is correct side. Not reversing? Verify negation of velocity.

---

### Unit 7: Ball Misses Paddle
**Builds:** Ball going below paddle loses life.
**Teaches:** Miss detection, game state.

---

### Unit 8: Paddle Collision
**Builds:** Ball bounces off paddle.
**Teaches:** Sprite-to-sprite collision.
**Code pattern:**
```asm
; Check if ball hit paddle
check_paddle:
    ; Is ball at paddle Y level?
    lda ball_y
    cmp #PADDLE_Y - 4
    bcc @no_hit     ; Above paddle
    cmp #PADDLE_Y + 4
    bcs @no_hit     ; Below paddle

    ; Is ball within paddle X range?
    lda ball_x
    sec
    sbc paddle_x
    bcc @no_hit     ; Left of paddle
    cmp #24         ; Paddle width
    bcs @no_hit     ; Right of paddle

    ; Hit! Reverse Y velocity
    lda #0
    sec
    sbc ball_vel_y
    sta ball_vel_y
    jsr play_paddle_sound

@no_hit:
    rts
```
**If it doesn't work:** Not bouncing? Check Y comparison range covers ball size. Going through? Ensure collision checked before position update.

---

### Unit 9: Brick Collision Detection
**Builds:** Detect when ball hits a brick.
**Teaches:** Position to nametable conversion.
**Code pattern:**
```asm
; Convert ball position to nametable address
; Screen: 256x240, Nametable: 32x30 tiles
get_ball_tile:
    ; Column = X / 8
    lda ball_x
    lsr
    lsr
    lsr
    sta temp_col

    ; Row = Y / 8
    lda ball_y
    lsr
    lsr
    lsr
    sta temp_row

    ; Nametable address = $2000 + (row * 32) + col
    lda temp_row
    asl
    asl
    asl
    asl
    asl             ; * 32
    ora temp_col
    sta nametable_lo
    lda #$20
    adc #0          ; Carry from row
    sta nametable_hi
    rts
```
**If it doesn't work:** Wrong tile detected? Check division by 8 (three LSR). Address overflow? Verify high byte carry handling.

---

### Unit 10: Brick Destruction
**Builds:** Hit brick disappears.
**Teaches:** Writing to PPU mid-game.
**Code pattern:**
```asm
; During VBlank, clear the brick
destroy_brick:
    lda $2002       ; Reset PPU address latch
    lda nametable_hi
    sta $2006
    lda nametable_lo
    sta $2006
    lda #EMPTY_TILE
    sta $2007
    sta $2007       ; Two tiles for full brick
    rts
```
**If it doesn't work:** Brick not disappearing? Must write during VBlank. Wrong brick gone? Check nametable address calculation.

---

### Unit 11: Ball Bounce off Brick
**Builds:** Ball reverses direction when hitting brick.
**Teaches:** Directional bounce based on collision side.

---

### Unit 12: Brick Count
**Builds:** Track remaining bricks for win condition.
**Teaches:** Game state tracking.
**Code pattern:**
```asm
bricks_remaining: .byte 0

init_level:
    lda #84         ; 6 rows × 14 bricks
    sta bricks_remaining
    ; ... draw bricks
    rts

check_win:
    lda bricks_remaining
    bne @not_done
    jmp level_complete
@not_done:
    rts
```

---

### Unit 13: Lives System
**Builds:** Start with 3 lives, display remaining.
**Teaches:** Life tracking, HUD.

---

### Unit 14: Score System
**Builds:** Points for breaking bricks.
**Teaches:** Score tracking.

---

### Unit 15: Sound - Paddle Hit
**Builds:** Sound when ball hits paddle.
**Teaches:** APU basics.
**Code pattern:**
```asm
; Pulse 1 for paddle hit - high pitched click
sound_paddle:
    lda #%10011111  ; Duty 50%, volume 15
    sta $4000
    lda #$C0        ; Frequency low
    sta $4002
    lda #$08        ; Frequency high, length
    sta $4003
    rts
```
**If it doesn't work:** No sound? Check APU status register ($4015) enables channel. Wrong pitch? Adjust frequency values.

---

### Unit 16: Phase 1 Polish
**Builds:** Basic game loop complete.
**If it doesn't work:** Ball going through paddle sometimes? Check collision order in game loop.

---

## Phase 2: Physics and Feel (Units 17-32)

### Unit 17: Fixed-Point Ball Position
**Builds:** Sub-pixel ball movement for smoother motion.
**Teaches:** 8.8 fixed-point maths.
**Code pattern:**
```asm
; 8.8 fixed point: high byte = pixel, low byte = fraction
ball_x_lo: .byte 0      ; Fractional X
ball_x_hi: .byte 128    ; Pixel X
ball_y_lo: .byte 0
ball_y_hi: .byte 120
ball_vel_x_lo: .byte $80    ; Velocity 1.5 pixels
ball_vel_x_hi: .byte 1
ball_vel_y_lo: .byte $00
ball_vel_y_hi: .byte $FF    ; -1 pixel

update_ball_fixed:
    ; X = X + vel_x (16-bit add)
    clc
    lda ball_x_lo
    adc ball_vel_x_lo
    sta ball_x_lo
    lda ball_x_hi
    adc ball_vel_x_hi
    sta ball_x_hi
    sta $020B       ; Sprite X = high byte

    ; Similar for Y...
    rts
```
**If it doesn't work:** Jerky movement? Make sure fractional part isn't being ignored. Ball teleporting? Check 16-bit add includes carry.

---

### Unit 18: Ball Speed Progression
**Builds:** Ball speeds up as bricks cleared.
**Teaches:** Dynamic difficulty.

---

### Unit 19: Paddle Angle Control
**Builds:** Where ball hits paddle affects bounce angle.
**Teaches:** Positional collision response.
**Code pattern:**
```asm
; Ball angle based on paddle hit position
; Center = straight up, edges = sharp angle
calculate_bounce:
    ; Get relative hit position (0-24)
    lda ball_x
    sec
    sbc paddle_x
    ; 0-4: hard left, 5-9: left, 10-14: center
    ; 15-19: right, 20-24: hard right

    cmp #5
    bcc @hard_left
    cmp #10
    bcc @left
    cmp #15
    bcc @center
    cmp #20
    bcc @right
    jmp @hard_right

@hard_left:
    lda #<-3
    sta ball_vel_x_hi
    ; ...
```
**If it doesn't work:** Always same angle? Check position calculation is relative to paddle. Wrong direction? Verify velocity signs.

---

### Unit 20: Ball Spin
**Builds:** Moving paddle adds spin to ball.
**Teaches:** Velocity transfer.

---

### Unit 21: Improved Brick Collision
**Builds:** Determine which side of brick was hit.
**Teaches:** Side detection for proper bounce direction.

---

### Unit 22: Corner Collision
**Builds:** Ball hitting brick corner bounces correctly.
**Teaches:** Corner case handling.

---

### Unit 23: Multiple Brick Hits
**Builds:** Ball can hit multiple bricks in one frame.
**Teaches:** Multi-collision handling.

---

### Unit 24: Ball Stuck Prevention
**Builds:** Prevent ball from getting trapped in bricks.
**Teaches:** Edge case handling.

---

### Unit 25: Paddle Edge Collision
**Builds:** Hitting paddle edge gives extreme angle.
**Teaches:** Risk/reward mechanics.

---

### Unit 26: Ball Speed Limits
**Builds:** Cap maximum ball speed.
**Teaches:** Balance constraints.

---

### Unit 27: Launch Direction
**Builds:** Player can aim initial launch.
**Teaches:** Serve mechanics.
**Code pattern:**
```asm
; Ball follows paddle until launched
; Direction indicator shows launch angle
serve_state: .byte 0    ; 0=serving, 1=playing
launch_angle: .byte 4   ; 0-8, 4=straight up

update_serve:
    ; Ball tracks paddle
    lda paddle_x
    clc
    adc #8          ; Center of paddle
    sta ball_x_hi
    sta $020B

    ; Adjust angle with left/right
    lda controller_press
    and #BUTTON_LEFT
    beq @check_right
    dec launch_angle
    bpl @done
    lda #0
    sta launch_angle

@check_right:
    ; ... similar for right

@check_launch:
    lda controller_press
    and #BUTTON_A
    beq @done
    jsr launch_ball

@done:
    rts
```

---

### Unit 28: Launch Indicator
**Builds:** Visual showing where ball will go.
**Teaches:** Player feedback.

---

### Unit 29: Tight Controls
**Builds:** Fast, responsive paddle movement.
**Teaches:** Control feel refinement.

---

### Unit 30: Brick Hit Effect
**Builds:** Brief flash when brick destroyed.
**Teaches:** Visual feedback.

---

### Unit 31: Sound - Brick Hit
**Builds:** Distinct sound for brick destruction.
**Teaches:** Audio feedback.

---

### Unit 32: Phase 2 Polish
**Builds:** Satisfying ball physics.

---

## Phase 3: Brick Variety (Units 33-48)

### Unit 33: Multiple Brick Colours
**Builds:** Different coloured bricks via attributes.
**Teaches:** Attribute table usage.
**Code pattern:**
```asm
; Attribute table: one byte controls 4x4 tiles
; Set different palettes for brick rows
set_brick_attributes:
    lda #$23
    sta $2006
    lda #$C0        ; Attribute table start
    sta $2006

    ; Top rows: palette 0 (red)
    ldx #8
    lda #%00000000
@row1:
    sta $2007
    dex
    bne @row1

    ; Next rows: palette 1 (blue)
    ldx #8
    lda #%01010101
@row2:
    sta $2007
    dex
    bne @row2
    rts
```
**If it doesn't work:** Wrong colours? Check attribute byte bit positions. Affecting wrong area? Verify attribute table address.

---

### Unit 34: Brick Point Values
**Builds:** Different bricks worth different points.
**Teaches:** Colour-based mechanics.

---

### Unit 35: Hard Bricks
**Builds:** Bricks that take 2 hits to break.
**Teaches:** Hit points for entities.
**Code pattern:**
```asm
; Track brick health in RAM array
; 0 = empty, 1 = normal, 2 = hard
brick_health:
    .res 84         ; 6 rows × 14 bricks

damage_brick:
    ; Get brick index from position
    jsr get_brick_index

    ; Reduce health
    ldx brick_index
    dec brick_health,x
    bne @not_destroyed

    ; Brick destroyed
    dec bricks_remaining
    jsr clear_brick_tiles
    jmp @done

@not_destroyed:
    ; Change to cracked tile
    jsr draw_cracked_brick

@done:
    rts
```
**If it doesn't work:** Not tracking hits? Verify brick index calculation. Visual not updating? Check cracked tile drawing.

---

### Unit 36: Cracked Brick Visuals
**Builds:** Hard bricks show damage after first hit.
**Teaches:** State-based graphics.

---

### Unit 37: Unbreakable Bricks
**Builds:** Gold bricks never break.
**Teaches:** Indestructible obstacles.

---

### Unit 38: Unbreakable Detection
**Builds:** Ball bounces off gold, doesn't count toward clear.
**Teaches:** Type checking.

---

### Unit 39: Explosive Bricks
**Builds:** Silver bricks destroy adjacent bricks.
**Teaches:** Chain reactions.

---

### Unit 40: Explosive Visual
**Builds:** Explosion effect for chain reactions.
**Teaches:** Particle effects.

---

### Unit 41: Moving Bricks
**Builds:** Row of bricks moves side to side.
**Teaches:** Dynamic backgrounds.

---

### Unit 42: Regenerating Bricks
**Builds:** Some bricks reappear after time.
**Teaches:** Timed respawns.

---

### Unit 43: Hidden Bricks
**Builds:** Invisible until ball passes nearby.
**Teaches:** Reveal mechanics.

---

### Unit 44: Brick Patterns
**Builds:** Creative brick arrangements.
**Teaches:** Level design variety.

---

### Unit 45: Row-Clear Bonus
**Builds:** Extra points for clearing whole row.
**Teaches:** Bonus systems.

---

### Unit 46: Combo System
**Builds:** Multiple bricks in sequence = multiplier.
**Teaches:** Score multipliers.

---

### Unit 47: Brick Animation
**Builds:** Bricks pulse or shimmer.
**Teaches:** Background animation.

---

### Unit 48: Phase 3 Polish
**Builds:** Varied, interesting brick types.

---

## Phase 4: Power-Ups (Units 49-64)

### Unit 49: Power-Up Drop System
**Builds:** Some bricks release power-up when destroyed.
**Teaches:** Item spawning.
**Code pattern:**
```asm
; Power-up falls from destroyed brick
powerup_active: .byte 0
powerup_x: .byte 0
powerup_y: .byte 0
powerup_type: .byte 0

spawn_powerup:
    ; 25% chance of power-up
    jsr random
    and #3
    bne @no_spawn

    ; Create power-up at brick position
    lda brick_x
    sta powerup_x
    lda brick_y
    sta powerup_y

    ; Random type
    jsr random
    and #7          ; 8 types
    sta powerup_type

    lda #1
    sta powerup_active

@no_spawn:
    rts
```
**If it doesn't work:** Never spawning? Check random isn't always same value. Wrong position? Verify brick coordinates saved before destruction.

---

### Unit 50: Power-Up Falling
**Builds:** Power-up falls toward paddle.
**Teaches:** Gravity for items.

---

### Unit 51: Power-Up Collection
**Builds:** Paddle catches power-up.
**Teaches:** Item collision.

---

### Unit 52: Power-Up - Extend Paddle
**Builds:** Paddle becomes wider.
**Teaches:** Player enhancement.
**Code pattern:**
```asm
paddle_width: .byte 24  ; Default width

powerup_extend:
    lda paddle_width
    cmp #48         ; Max width
    bcs @done

    clc
    adc #16
    sta paddle_width

    ; Add more paddle sprites
    jsr update_paddle_sprites

    ; Set timer
    lda #255
    sta powerup_timer

@done:
    rts
```

---

### Unit 53: Power-Up - Shrink Paddle
**Builds:** Paddle becomes smaller (bad power-up).
**Teaches:** Negative items.

---

### Unit 54: Power-Up - Multi-Ball
**Builds:** Ball splits into three.
**Teaches:** Multiple ball management.

---

### Unit 55: Multi-Ball Logic
**Builds:** Track all balls, game continues until all lost.
**Teaches:** Entity arrays.

---

### Unit 56: Power-Up - Catch
**Builds:** Ball sticks to paddle, can re-aim.
**Teaches:** State modifiers.

---

### Unit 57: Catch Mechanics
**Builds:** Press button to release caught ball.
**Teaches:** Input-triggered release.

---

### Unit 58: Power-Up - Laser
**Builds:** Paddle shoots lasers to destroy bricks.
**Teaches:** Weapon power-ups.

---

### Unit 59: Laser Firing
**Builds:** Button fires lasers while active.
**Teaches:** Projectile spawning.

---

### Unit 60: Power-Up - Slow
**Builds:** Ball moves slower.
**Teaches:** Speed modification.

---

### Unit 61: Power-Up - Fast
**Builds:** Ball speeds up (bad or good?).
**Teaches:** Risk/reward items.

---

### Unit 62: Power-Up - Extra Life
**Builds:** Rare 1-up item.
**Teaches:** High-value items.

---

### Unit 63: Power-Up Timer Display
**Builds:** Show remaining time for timed power-ups.
**Teaches:** Status display.

---

### Unit 64: Phase 4 Polish
**Builds:** Balanced power-up system.

---

## Phase 5: Level Design (Units 65-80)

### Unit 65: Level Data Format
**Builds:** Efficient level storage.
**Teaches:** Data compression.
**Code pattern:**
```asm
; Level format: brick type per cell
; 0=empty, 1=normal, 2=hard, 3=unbreakable
; 6 rows × 14 columns = 84 bytes per level
level_01:
    .byte 1,1,1,1,1,1,1,1,1,1,1,1,1,1   ; Row 1
    .byte 1,1,1,1,1,1,1,1,1,1,1,1,1,1
    .byte 2,2,2,2,2,2,2,2,2,2,2,2,2,2   ; Hard bricks
    .byte 1,1,1,1,1,1,1,1,1,1,1,1,1,1
    .byte 1,1,1,1,1,1,1,1,1,1,1,1,1,1
    .byte 0,0,0,0,0,0,0,0,0,0,0,0,0,0   ; Empty row

level_pointers:
    .word level_01, level_02, level_03
    ; ...
```

---

### Unit 66: Level Loading
**Builds:** Draw level from data.
**Teaches:** Data-driven levels.

---

### Unit 67: Level 1 - Classic
**Builds:** Standard rectangular brick field.
**Teaches:** Baseline design.

---

### Unit 68: Level 2 - Pyramid
**Builds:** Triangular brick formation.
**Teaches:** Shape variety.

---

### Unit 69: Level 3 - Fortress
**Builds:** Unbreakable brick walls.
**Teaches:** Obstacle design.

---

### Unit 70: Level 4 - Checker
**Builds:** Alternating brick pattern.
**Teaches:** Pattern design.

---

### Unit 71: Levels 5-10
**Builds:** More varied layouts.
**Teaches:** Design iteration.

---

### Unit 72: Levels 11-15
**Builds:** Intermediate difficulty.
**Teaches:** Difficulty curve.

---

### Unit 73: Levels 16-20
**Builds:** Advanced challenges.
**Teaches:** Expert design.

---

### Unit 74: Level Colour Themes
**Builds:** Different palettes per level.
**Teaches:** Visual variety.

---

### Unit 75: Level Transitions
**Builds:** Effects between levels.
**Teaches:** Polish transitions.

---

### Unit 76: Boss Level
**Builds:** Special level with unique challenge.
**Teaches:** Boss design.

---

### Unit 77: Bonus Stages
**Builds:** All-collect levels for points.
**Teaches:** Variety stages.

---

### Unit 78: Level Select (Debug)
**Builds:** Jump to any level.
**Teaches:** Development tools.

---

### Unit 79: Level Progression
**Builds:** Unlock levels sequentially.
**Teaches:** Progression systems.

---

### Unit 80: Phase 5 Polish
**Builds:** 20 varied, balanced levels.

---

## Phase 6: Audio and Features (Units 81-96)

### Unit 81: Sound Effects System
**Builds:** Priority-based sound manager.
**Teaches:** Audio architecture.

---

### Unit 82: Sound - Wall Bounce
**Builds:** Different pitch for wall hits.
**Teaches:** Sound variety.

---

### Unit 83: Sound - Brick Destroy
**Builds:** Satisfying destruction sound.
**Teaches:** Impact audio.

---

### Unit 84: Sound - Power-Up Collect
**Builds:** Positive collection sound.
**Teaches:** Reward audio.

---

### Unit 85: Sound - Ball Lost
**Builds:** Negative sound for misses.
**Teaches:** Failure audio.

---

### Unit 86: Sound - Level Complete
**Builds:** Victory fanfare.
**Teaches:** Achievement audio.

---

### Unit 87: Music - Title Screen
**Builds:** Catchy title music.
**Teaches:** NES music composition.

---

### Unit 88: Music - Gameplay
**Builds:** Background music during play.
**Teaches:** Game music.

---

### Unit 89: Title Screen
**Builds:** Attractive start screen.
**Teaches:** Presentation.

---

### Unit 90: High Score Table
**Builds:** Top scores display.
**Teaches:** Score persistence.

---

### Unit 91: High Score Entry
**Builds:** Enter initials.
**Teaches:** Text input.

---

### Unit 92: Pause Feature
**Builds:** Pause mid-game.
**Teaches:** Pause implementation.

---

### Unit 93: Two-Player Mode
**Builds:** Alternating play.
**Teaches:** Multiplayer.

---

### Unit 94: Difficulty Settings
**Builds:** Easy/Normal/Hard options.
**Teaches:** Difficulty options.

---

### Unit 95: Continue System
**Builds:** Continue after game over.
**Teaches:** Continue mechanics.

---

### Unit 96: Phase 6 Polish
**Builds:** Complete feature set.

---

## Phase 7: Optimisation and Balance (Units 97-112)

### Unit 97: Frame Rate Analysis
**Builds:** Ensure 60fps consistency.
**Teaches:** Performance measurement.

---

### Unit 98: Collision Optimisation
**Builds:** Faster brick collision checks.
**Teaches:** Efficiency.

---

### Unit 99: PPU Update Optimisation
**Builds:** Efficient VBlank usage.
**Teaches:** PPU timing.

---

### Unit 100: Memory Layout
**Builds:** Optimal data organisation.
**Teaches:** Memory planning.

---

### Unit 101: Difficulty Balancing
**Builds:** Fair challenge curve.
**Teaches:** Balance iteration.

---

### Unit 102: Ball Speed Tuning
**Builds:** Right speed progression.
**Teaches:** Speed balance.

---

### Unit 103: Power-Up Balance
**Builds:** Right spawn rates and effects.
**Teaches:** Item balance.

---

### Unit 104: Control Response
**Builds:** Tight paddle control.
**Teaches:** Input feel.

---

### Unit 105: Bug Hunting
**Builds:** Find and fix issues.
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

### Unit 108: Sprite Limit Handling
**Builds:** Manage 8-sprite limit for multi-ball.
**Teaches:** NES constraints.

---

### Unit 109: Sound Balance
**Builds:** Volume levels right.
**Teaches:** Audio mix.

---

### Unit 110: Visual Polish
**Builds:** Consistent graphics.
**Teaches:** Visual consistency.

---

### Unit 111: Code Cleanup
**Builds:** Well-organised code.
**Teaches:** Code quality.

---

### Unit 112: Phase 7 Polish
**Builds:** Stable, balanced game.

---

## Phase 8: Release (Units 113-128)

### Unit 113: Title Screen Art
**Builds:** Eye-catching logo.
**Teaches:** Title design.

---

### Unit 114: Instructions Screen
**Builds:** How to play.
**Teaches:** Onboarding.

---

### Unit 115: Credits
**Builds:** Attribution.
**Teaches:** Credits design.

---

### Unit 116: NES ROM Header
**Builds:** Proper iNES header.
**Teaches:** ROM format.

---

### Unit 117: ROM Creation
**Builds:** Final assembled ROM.
**Teaches:** Build process.

---

### Unit 118: Emulator Testing
**Builds:** Test in multiple emulators.
**Teaches:** Compatibility.

---

### Unit 119: Hardware Testing
**Builds:** Test on real NES.
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

### Unit 122: Region Compatibility
**Builds:** NTSC/PAL considerations.
**Teaches:** Regional issues.

---

### Unit 123: Release Candidate
**Builds:** Final test build.
**Teaches:** Release process.

---

### Unit 124: Final Bug Fixes
**Builds:** Last fixes.
**Teaches:** Polish cycle.

---

### Unit 125: Documentation
**Builds:** Manual and readme.
**Teaches:** Documentation.

---

### Unit 126: Cartridge Label Design
**Builds:** Label artwork concept.
**Teaches:** Presentation.

---

### Unit 127: Community Feedback
**Builds:** Beta test results.
**Teaches:** Community testing.

---

### Unit 128: Release
**Builds:** Final release.
**Teaches:** Shipping a game.

---

## Version History

- **1.0 (2026-01-18):** Initial 128-unit outline created.
