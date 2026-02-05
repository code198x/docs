# Amiga Game 4: Ascent - Full 128-Unit Outline

**Platform:** Commodore Amiga
**Game:** Ascent
**Units:** 128 (8 phases × 16 units)
**Concept:** Single-screen platformer polished to commercial quality. Climb upward through hazards, collect items, reach the exit. Smooth 50fps gameplay with Copper-enhanced visuals and sampled audio.

---

## Overview

Ascent introduces gravity and platform physics on the Amiga. After horizontal gameplay in Games 1-3 (shooter, Frogger, breakout), learners now tackle vertical movement, jump arcs, and platform collision - the foundation for countless classic games.

**Key Learning Goals:**
- Gravity and jump physics (velocity, acceleration)
- Platform collision with Blitter backgrounds
- BOB animation for player character
- Blitter cookie-cut masking
- Moving platforms and hazards
- Level data structures
- Copper colour splits for visual variety

---

## Phase 1: Platform Foundation (Units 1-16)

### Unit 1: Platform Level
**Builds:** Draw platforms using Blitter.
**Teaches:** Blitter fills for level geometry.
**Code pattern:**
```asm
; Level data: platform positions and sizes
; Each platform: x, y, width, height
platform_data:
    dc.w    32, 200, 64, 8      ; Ground platform
    dc.w    96, 168, 48, 8      ; Step up
    dc.w    160, 136, 48, 8     ; Higher
    dc.w    64, 104, 32, 8      ; Even higher
    dc.w    128, 72, 48, 8      ; Near top
    dc.w    -1                   ; End marker

draw_platforms:
    lea     platform_data,a0

.loop:
    move.w  (a0)+,d0            ; X
    bmi     .done               ; End marker
    move.w  (a0)+,d1            ; Y
    move.w  (a0)+,d2            ; Width
    move.w  (a0)+,d3            ; Height
    bsr     draw_platform_rect
    bra     .loop

.done:
    rts

draw_platform_rect:
    ; Calculate screen address
    ; Use Blitter to fill rectangle
    ; ... Blitter setup for solid fill
    rts
```
**If it doesn't work:** Platforms not showing? Check Blitter DMA enabled. Wrong positions? Verify coordinate system.

---

### Unit 2: Platform Collision Mask
**Builds:** Separate bitplane for collision.
**Teaches:** Collision bitmaps.
**Code pattern:**
```asm
; Use extra bitplane for collision detection
; Platform = solid pixels in collision plane
; Read collision plane to check if position is blocked

check_platform_collision:
    ; Convert pixel position to bit in collision plane
    move.w  d0,d2               ; X position
    move.w  d1,d3               ; Y position

    ; Calculate byte offset
    mulu    #SCREEN_WIDTH/8,d3
    move.w  d2,d4
    lsr.w   #3,d4               ; X / 8
    add.w   d4,d3

    ; Calculate bit position
    move.w  d2,d4
    and.w   #7,d4
    eor.w   #7,d4               ; Bit position (7-x%8)

    ; Check collision plane
    lea     collision_plane,a0
    add.w   d3,a0
    btst    d4,(a0)
    rts                         ; Z=0 if collision
```
**If it doesn't work:** Falling through platforms? Check collision plane has platform data. Wrong bit? Verify bit position calculation.

---

### Unit 3: Player BOB
**Builds:** Player character as Blitter Object.
**Teaches:** BOB setup and drawing.
**Code pattern:**
```asm
; Player: 16×16 pixel BOB
player_x:       dc.w    160
player_y:       dc.w    184
player_gfx:     dc.l    player_bob_data
player_mask:    dc.l    player_mask_data

draw_player:
    ; Wait for Blitter
    btst    #6,$dff002
    bne.s   draw_player

    ; Calculate screen destination
    move.w  player_y,d0
    mulu    #SCREEN_WIDTH,d0
    move.w  player_x,d1
    lsr.w   #3,d1
    add.w   d1,d0
    add.l   #screen,d0
    move.l  d0,$dff054          ; BLTDPT

    ; Set up cookie-cut blit
    ; A = mask, B = source, C = background, D = destination
    move.l  player_mask,$dff050 ; BLTAPT
    move.l  player_gfx,$dff04c  ; BLTBPT
    move.l  d0,$dff048          ; BLTCPT

    move.w  #$0fca,$dff040      ; BLTCON0: A&B | ~A&C
    move.w  #0,$dff042          ; BLTCON1

    ; Modulos and size
    move.w  #SCREEN_WIDTH-2,$dff064     ; BLTCMOD
    move.w  #SCREEN_WIDTH-2,$dff066     ; BLTDMOD
    move.w  #0,$dff062          ; BLTAMOD
    move.w  #0,$dff060          ; BLTBMOD

    move.w  #(16<<6)|1,$dff058  ; BLTSIZE: 16 rows, 1 word
    rts
```
**If it doesn't work:** Player not appearing? Check Blitter channel setup. Garbled? Verify cookie-cut formula.

---

### Unit 4: Player Movement
**Builds:** Left/right joystick control.
**Teaches:** Horizontal movement.
**Code pattern:**
```asm
PLAYER_SPEED    equ     2

update_player_movement:
    ; Read joystick
    move.w  $dff00c,d0          ; JOY1DAT

    ; Check left
    btst    #9,d0
    beq.s   .not_left
    sub.w   #PLAYER_SPEED,player_x

.not_left:
    ; Check right
    btst    #1,d0
    beq.s   .not_right
    add.w   #PLAYER_SPEED,player_x

.not_right:
    ; Clamp to screen bounds
    move.w  player_x,d0
    cmp.w   #16,d0
    bge.s   .not_min_x
    move.w  #16,player_x
.not_min_x:
    cmp.w   #288,d0
    ble.s   .not_max_x
    move.w  #288,player_x
.not_max_x:
    rts
```
**If it doesn't work:** Not responding? Check JOY1DAT address. Wrong direction? Verify bit positions.

---

### Unit 5: Gravity
**Builds:** Player falls when not on platform.
**Teaches:** Gravity physics.
**Code pattern:**
```asm
GRAVITY         equ     1
MAX_FALL_SPEED  equ     8

player_vel_y:   dc.w    0

apply_gravity:
    ; Add gravity to velocity
    move.w  player_vel_y,d0
    add.w   #GRAVITY,d0

    ; Cap fall speed
    cmp.w   #MAX_FALL_SPEED,d0
    ble.s   .not_max
    move.w  #MAX_FALL_SPEED,d0
.not_max:
    move.w  d0,player_vel_y

    ; Apply velocity to position
    add.w   d0,player_y
    rts
```
**If it doesn't work:** Not falling? Check gravity is being applied each frame. Falling forever? Need platform collision.

---

### Unit 6: Landing Detection
**Builds:** Stop falling when hitting platform.
**Teaches:** Ground collision.
**Code pattern:**
```asm
check_ground:
    ; Check position below player's feet
    move.w  player_x,d0
    add.w   #8,d0               ; Centre of player
    move.w  player_y,d1
    add.w   #16,d1              ; Bottom of player

    bsr     check_platform_collision
    beq.s   .no_ground          ; No collision

    ; On ground - stop falling
    clr.w   player_vel_y

    ; Snap to platform surface
    move.w  player_y,d0
    add.w   #16,d0
    and.w   #$fff8,d0           ; Round to 8 pixels
    sub.w   #16,d0
    move.w  d0,player_y

    move.w  #1,on_ground
    rts

.no_ground:
    clr.w   on_ground
    rts
```
**If it doesn't work:** Bouncing on platforms? Check snap calculation. Falling through? Ensure collision checked before position update.

---

### Unit 7: Jumping
**Builds:** Fire button makes player jump.
**Teaches:** Jump physics.
**Code pattern:**
```asm
JUMP_VELOCITY   equ     -10     ; Negative = upward

check_jump:
    ; Can only jump when on ground
    tst.w   on_ground
    beq.s   .no_jump

    ; Check fire button
    btst    #7,$bfe001
    bne.s   .no_jump            ; Not pressed

    ; Start jump
    move.w  #JUMP_VELOCITY,player_vel_y
    clr.w   on_ground
    bsr     sound_jump

.no_jump:
    rts
```
**If it doesn't work:** Can't jump? Check on_ground flag is set correctly. No height? Verify negative velocity.

---

### Unit 8: Variable Jump Height
**Builds:** Hold button for higher jump.
**Teaches:** Variable jump mechanics.
**Code pattern:**
```asm
; Release button early = lower jump
check_jump_release:
    ; Only while rising
    move.w  player_vel_y,d0
    bpl.s   .done               ; Falling, ignore

    ; If button released, reduce upward velocity
    btst    #7,$bfe001
    beq.s   .done               ; Still held

    ; Cut jump short
    move.w  player_vel_y,d0
    asr.w   #1,d0               ; Halve velocity
    move.w  d0,player_vel_y

.done:
    rts
```
**If it doesn't work:** Always full height? Check button release detection. Too short? Adjust velocity reduction.

---

### Unit 9: Head Collision
**Builds:** Hitting ceiling stops upward movement.
**Teaches:** Upward collision.

---

### Unit 10: Wall Collision
**Builds:** Can't walk through walls.
**Teaches:** Horizontal collision.

---

### Unit 11: Player Animation
**Builds:** Walk cycle and jump frames.
**Teaches:** BOB animation.
**Code pattern:**
```asm
player_frame:   dc.w    0
anim_counter:   dc.w    0
ANIM_SPEED      equ     4

; Animation frames: idle, walk1, walk2, walk3, jump
player_frames:
    dc.l    player_idle
    dc.l    player_walk1
    dc.l    player_walk2
    dc.l    player_walk3
    dc.l    player_jump

update_animation:
    ; Jumping?
    tst.w   on_ground
    bne.s   .on_ground
    move.w  #4,player_frame     ; Jump frame
    rts

.on_ground:
    ; Moving?
    move.w  $dff00c,d0
    and.w   #%0000001000000010,d0   ; Left or right
    beq.s   .idle

    ; Walk animation
    addq.w  #1,anim_counter
    move.w  anim_counter,d0
    and.w   #(ANIM_SPEED*4)-1,d0
    lsr.w   #2,d0               ; 0-3
    addq.w  #1,d0               ; 1-4 (walk frames)
    move.w  d0,player_frame
    rts

.idle:
    clr.w   player_frame
    rts
```

---

### Unit 12: Facing Direction
**Builds:** Player faces movement direction.
**Teaches:** Sprite flipping.

---

### Unit 13: Collectibles
**Builds:** Items to collect in level.
**Teaches:** Item placement and collection.

---

### Unit 14: Exit Door
**Builds:** Reach exit to complete level.
**Teaches:** Goal detection.

---

### Unit 15: Sound - Jump
**Builds:** Jump sound effect.
**Teaches:** Paula sample playback.

---

### Unit 16: Phase 1 Polish
**Builds:** Basic platforming working.

---

## Phase 2: Hazards and Enemies (Units 17-32)

### Unit 17: Spike Hazards
**Builds:** Instant death spikes.
**Teaches:** Hazard collision.

---

### Unit 18: Death and Respawn
**Builds:** Player dies and restarts.
**Teaches:** Death handling.

---

### Unit 19: Lives System
**Builds:** Multiple lives.
**Teaches:** Life tracking.

---

### Unit 20: Patrolling Enemies
**Builds:** Enemies walk back and forth.
**Teaches:** Simple enemy AI.
**Code pattern:**
```asm
; Enemy structure
ENEMY_X     equ 0
ENEMY_Y     equ 2
ENEMY_DIR   equ 4
ENEMY_TYPE  equ 6
ENEMY_SIZE  equ 8

MAX_ENEMIES equ 8

enemy_data:
    ds.b    MAX_ENEMIES * ENEMY_SIZE

update_enemies:
    lea     enemy_data,a0
    move.w  #MAX_ENEMIES-1,d7

.loop:
    ; Get enemy type
    move.w  ENEMY_TYPE(a0),d0
    beq.s   .next               ; Inactive

    ; Move based on direction
    move.w  ENEMY_DIR(a0),d0
    tst.w   d0
    bmi.s   .move_left

.move_right:
    add.w   #1,ENEMY_X(a0)
    cmp.w   #280,ENEMY_X(a0)
    blt.s   .next
    neg.w   ENEMY_DIR(a0)
    bra.s   .next

.move_left:
    sub.w   #1,ENEMY_X(a0)
    cmp.w   #16,ENEMY_X(a0)
    bgt.s   .next
    neg.w   ENEMY_DIR(a0)

.next:
    add.w   #ENEMY_SIZE,a0
    dbf     d7,.loop
    rts
```

---

### Unit 21: Enemy-Player Collision
**Builds:** Touching enemy hurts player.
**Teaches:** Damage collision.

---

### Unit 22: Stomping Enemies
**Builds:** Jump on enemies to defeat them.
**Teaches:** Directional collision.

---

### Unit 23: Enemy Animation
**Builds:** Enemies have walk cycles.
**Teaches:** Multi-entity animation.

---

### Unit 24: Flying Enemies
**Builds:** Enemies that fly in patterns.
**Teaches:** Non-ground AI.

---

### Unit 25: Crumbling Platforms
**Builds:** Platforms that break after standing.
**Teaches:** Timed hazards.

---

### Unit 26: Moving Platforms
**Builds:** Platforms that move horizontally.
**Teaches:** Platform movement.
**Code pattern:**
```asm
; Moving platform structure
MPLAT_X     equ 0
MPLAT_Y     equ 2
MPLAT_MINX  equ 4
MPLAT_MAXX  equ 6
MPLAT_DIR   equ 8
MPLAT_SIZE  equ 10

update_moving_platforms:
    ; Move platform
    ; Update collision mask
    ; If player on platform, move player too
    ; ...
    rts

; Check if player is on moving platform
check_moving_platform_carry:
    ; If player on this platform, add platform velocity to player
    move.w  mplat_vel_x,d0
    add.w   d0,player_x
    rts
```

---

### Unit 27: Vertical Moving Platforms
**Builds:** Platforms that move up/down.
**Teaches:** Vertical movers.

---

### Unit 28: Conveyor Belts
**Builds:** Surfaces that push player.
**Teaches:** Environmental forces.

---

### Unit 29: Fire Hazards
**Builds:** Periodic fire jets.
**Teaches:** Timed hazards.

---

### Unit 30: Water/Pits
**Builds:** Falling into water kills.
**Teaches:** Pit hazards.

---

### Unit 31: Sound - Enemy Defeat
**Builds:** Sound for stomping enemies.
**Teaches:** Action feedback.

---

### Unit 32: Phase 2 Polish
**Builds:** Complete hazard system.

---

## Phase 3: Level Design (Units 33-48)

### Unit 33: Level Data Format
**Builds:** Efficient level storage.
**Teaches:** Level data structures.
**Code pattern:**
```asm
; Level format:
; - Platform list (x, y, width, type)
; - Enemy list (x, y, type)
; - Item list (x, y, type)
; - Player start position
; - Exit position

level_01:
    dc.w    8                   ; Number of platforms
    dc.w    32, 200, 256, 0     ; Ground (type 0 = solid)
    dc.w    64, 168, 64, 0
    dc.w    160, 136, 64, 0
    dc.w    48, 104, 48, 1      ; Type 1 = crumbling
    dc.w    128, 72, 80, 0
    dc.w    200, 136, 48, 2     ; Type 2 = moving
    dc.w    96, 40, 64, 0       ; Near top
    dc.w    160, 16, 32, 0      ; Exit platform

    dc.w    2                   ; Number of enemies
    dc.w    100, 184, 0         ; Enemy type 0
    dc.w    180, 120, 1         ; Enemy type 1

    dc.w    3                   ; Number of items
    dc.w    80, 152, 0          ; Coin
    dc.w    176, 120, 0
    dc.w    112, 24, 1          ; Key

    dc.w    48, 184             ; Player start
    dc.w    168, 0              ; Exit position
```

---

### Unit 34: Level Loading
**Builds:** Parse and create level.
**Teaches:** Data-driven levels.

---

### Unit 35-44: Levels 1-10
**Builds:** Ten progressively harder levels.
**Teaches:** Level design iteration.

---

### Unit 45: Levels 11-20
**Builds:** Advanced levels.
**Teaches:** Expert design.

---

### Unit 46: Level Transitions
**Builds:** Effects between levels.
**Teaches:** Polish transitions.

---

### Unit 47: Level Themes
**Builds:** Different Copper palettes per level.
**Teaches:** Visual variety.

---

### Unit 48: Phase 3 Polish
**Builds:** 20 complete levels.

---

## Phase 4: Power-Ups and Features (Units 49-64)

### Unit 49: Coin Collection
**Builds:** Coins for score.
**Teaches:** Collectible scoring.

---

### Unit 50: Key and Lock
**Builds:** Keys open locked doors.
**Teaches:** Key mechanics.

---

### Unit 51: Power-Up - Speed
**Builds:** Temporary speed boost.
**Teaches:** Timed power-ups.

---

### Unit 52: Power-Up - High Jump
**Builds:** Temporary jump boost.
**Teaches:** Ability modification.

---

### Unit 53: Power-Up - Invincibility
**Builds:** Temporary immunity.
**Teaches:** State power-ups.

---

### Unit 54: Extra Life Pickup
**Builds:** 1-up items.
**Teaches:** Life pickups.

---

### Unit 55: Checkpoint System
**Builds:** Mid-level checkpoints.
**Teaches:** Progress saving.

---

### Unit 56: Score System
**Builds:** Points display.
**Teaches:** Scoring.

---

### Unit 57: Time Bonus
**Builds:** Bonus for fast completion.
**Teaches:** Time-based scoring.

---

### Unit 58: Combo System
**Builds:** Chains for bonus points.
**Teaches:** Combo mechanics.

---

### Unit 59: Hidden Items
**Builds:** Secret collectibles.
**Teaches:** Secrets.

---

### Unit 60: Boss Level
**Builds:** Boss at end of world.
**Teaches:** Boss design.

---

### Unit 61: Boss Pattern
**Builds:** Boss attack patterns.
**Teaches:** Boss AI.

---

### Unit 62: Boss Defeat
**Builds:** Defeating boss.
**Teaches:** Boss mechanics.

---

### Unit 63: World System
**Builds:** Multiple worlds with themes.
**Teaches:** World organisation.

---

### Unit 64: Phase 4 Polish
**Builds:** Complete feature set.

---

## Phase 5: Audio (Units 65-80)

### Unit 65: Sound System
**Builds:** Sample management.
**Teaches:** Audio architecture.

---

### Unit 66: Sound - Jump
**Builds:** Jump sound.
**Teaches:** Movement audio.

---

### Unit 67: Sound - Land
**Builds:** Landing thud.
**Teaches:** Impact audio.

---

### Unit 68: Sound - Collect
**Builds:** Coin collection sound.
**Teaches:** Reward audio.

---

### Unit 69: Sound - Death
**Builds:** Player death sound.
**Teaches:** Failure audio.

---

### Unit 70: Sound - Enemy
**Builds:** Enemy defeat sound.
**Teaches:** Action audio.

---

### Unit 71: Music - Title
**Builds:** Title screen MOD.
**Teaches:** MOD replay.

---

### Unit 72: Music - Gameplay
**Builds:** In-game music.
**Teaches:** Game music.

---

### Unit 73: Music - Boss
**Builds:** Tense boss music.
**Teaches:** Boss atmosphere.

---

### Unit 74: Music - Victory
**Builds:** Level complete tune.
**Teaches:** Success audio.

---

### Unit 75: Music/SFX Balance
**Builds:** Sounds work with music.
**Teaches:** Audio mixing.

---

### Unit 76: World Themes
**Builds:** Different music per world.
**Teaches:** Musical variety.

---

### Unit 77: Sound - Power-Up
**Builds:** Power-up collection sound.
**Teaches:** Power-up feedback.

---

### Unit 78: Sound - Warning
**Builds:** Low time/health warning.
**Teaches:** Status audio.

---

### Unit 79: Audio Polish
**Builds:** Volume balance.
**Teaches:** Final mix.

---

### Unit 80: Phase 5 Polish
**Builds:** Complete audio.

---

## Phase 6: Presentation (Units 81-96)

### Unit 81: Title Screen
**Builds:** Attractive start.
**Teaches:** Title design.

---

### Unit 82: Demo Mode
**Builds:** Attract sequence.
**Teaches:** Attract mode.

---

### Unit 83: High Scores
**Builds:** Top scores display.
**Teaches:** Score table.

---

### Unit 84: Name Entry
**Builds:** Enter initials.
**Teaches:** Text input.

---

### Unit 85: Instructions
**Builds:** How to play.
**Teaches:** Onboarding.

---

### Unit 86: World Map
**Builds:** Visual level selection.
**Teaches:** Map screen.

---

### Unit 87: Pause Menu
**Builds:** In-game pause.
**Teaches:** Pause implementation.

---

### Unit 88: Game Over
**Builds:** End screen.
**Teaches:** Game over handling.

---

### Unit 89: Victory Screen
**Builds:** Completion celebration.
**Teaches:** Victory presentation.

---

### Unit 90: Credits
**Builds:** Attribution.
**Teaches:** Credits design.

---

### Unit 91: Copper Effects
**Builds:** Visual polish with Copper.
**Teaches:** Copper tricks.

---

### Unit 92: Parallax Background
**Builds:** Simple parallax scrolling.
**Teaches:** Background depth.

---

### Unit 93: Particle Effects
**Builds:** Sparkles, dust clouds.
**Teaches:** Particle systems.

---

### Unit 94: Screen Transitions
**Builds:** Fade effects.
**Teaches:** Transition polish.

---

### Unit 95: Easter Eggs
**Builds:** Hidden features.
**Teaches:** Secrets.

---

### Unit 96: Phase 6 Polish
**Builds:** Complete presentation.

---

## Phase 7: Optimisation (Units 97-112)

### Unit 97: Frame Rate
**Builds:** Solid 50fps.
**Teaches:** Performance.

---

### Unit 98: Blitter Efficiency
**Builds:** Faster BOB drawing.
**Teaches:** Blitter optimisation.

---

### Unit 99: Collision Optimisation
**Builds:** Faster collision checks.
**Teaches:** Algorithm efficiency.

---

### Unit 100: Memory Layout
**Builds:** Optimal organisation.
**Teaches:** Memory planning.

---

### Unit 101-104: Balance
**Builds:** Fair difficulty.
**Teaches:** Game balance.

---

### Unit 105-108: Bug Fixes
**Builds:** Find and fix issues.
**Teaches:** Debugging.

---

### Unit 109-111: Polish
**Builds:** Visual consistency.
**Teaches:** Final polish.

---

### Unit 112: Phase 7 Complete
**Builds:** Stable game.

---

## Phase 8: Release (Units 113-128)

### Unit 113-116: ADF Creation
**Builds:** Bootable disk.
**Teaches:** Distribution.

---

### Unit 117-120: Testing
**Builds:** Emulator and hardware.
**Teaches:** Quality assurance.

---

### Unit 121-124: Final Polish
**Builds:** Last fixes.
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
