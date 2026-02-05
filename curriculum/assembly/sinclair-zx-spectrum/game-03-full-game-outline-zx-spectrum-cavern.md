# ZX Spectrum Game 3: Cavern - Full 128-Unit Outline

**Platform:** Sinclair ZX Spectrum
**Game:** Cavern
**Units:** 128 (8 phases × 16 units)
**Concept:** Single-screen platformer in the Manic Miner tradition. Navigate platforms, avoid hazards, collect keys to open the exit. Air supply adds tension.

---

## Overview

Cavern builds on the physics foundation from Shatter (Game 2), applying those skills to gravity-based platforming instead of bouncing balls. This is the Spectrum's signature genre - games like Manic Miner and Jet Set Willy defined the platform.

**Key Learning Goals:**
- Gravity and jump physics (velocity, acceleration)
- Platform collision (landing, bonking head)
- Hazard patterns (crumbling floors, patrolling enemies)
- Air supply mechanic (time pressure)
- Level design for single-screen platformers
- Player animation (walk cycle, jump)

---

## Phase 1: Movement Foundation (Units 1-16)

### Unit 1: The Empty Cavern
**Builds:** Static screen with platforms displayed.
**Teaches:** Screen memory layout for level rendering.
**Code pattern:**
```z80
; Screen memory: $4000-$57FF (6144 bytes)
; Draw platforms as filled rectangles
draw_platforms:
    ld hl,SCREEN + (16*32)  ; Row 16
    ld b,32                  ; Full width
    ld a,$FF                 ; Solid pixels
.loop:
    ld (hl),a
    inc l
    djnz .loop
    ret
```
**If it doesn't work:** Platform not visible? Check screen address calculation. Partial platform? Verify loop counter covers full width.

---

### Unit 2: Player Character
**Builds:** Miner character displayed on screen.
**Teaches:** UDG (User Defined Graphics) setup.
**Code pattern:**
```z80
; Player sprite (8x8 pixels)
player_sprite:
    defb %00111100  ; Head
    defb %00111100
    defb %11111111  ; Body with arms
    defb %00111100
    defb %00111100  ; Body
    defb %00111100
    defb %01100110  ; Legs apart
    defb %01100110

; Copy to UDG area
setup_udg:
    ld hl,player_sprite
    ld de,$FF58     ; UDG 'A' location
    ld bc,8
    ldir
    ret
```
**If it doesn't work:** Garbage character? Check UDG address. Wrong shape? Verify bit patterns (1=ink, 0=paper).

---

### Unit 3: Keyboard Input
**Builds:** Player responds to Q/A/O/P keys.
**Teaches:** Keyboard reading via port $FE.
**Code pattern:**
```z80
; Read keyboard for QAOP
; Q=up, A=down, O=left, P=right
read_keys:
    ld a,$FB        ; Row Q-T
    in a,($FE)
    bit 0,a         ; Q key
    jr nz,.no_q
    set 0,b         ; Q pressed
.no_q:
    ld a,$FD        ; Row A-G
    in a,($FE)
    bit 0,a         ; A key
    jr nz,.no_a
    set 1,b         ; A pressed
.no_a:
    ; Continue for O and P...
    ret
```
**If it doesn't work:** No response? Check port address and row selection. Wrong keys? Verify bit positions for each key.

---

### Unit 4: Horizontal Movement
**Builds:** Player moves left/right with O/P.
**Teaches:** Position updates, boundary checks.
**Code pattern:**
```z80
player_x:    defb 128   ; Pixel X position
PLAYER_SPEED equ 2

move_left:
    ld a,(player_x)
    sub PLAYER_SPEED
    cp 8            ; Left boundary
    jr c,.stop
    ld (player_x),a
    ret
.stop:
    ld a,8
    ld (player_x),a
    ret
```
**If it doesn't work:** Moving too fast? Reduce PLAYER_SPEED. Wrapping around? Check boundary comparison is unsigned.

---

### Unit 5: Gravity Introduction
**Builds:** Player falls when not on platform.
**Teaches:** Velocity accumulation, terminal velocity.
**Code pattern:**
```z80
player_y:      defb 100  ; Pixel Y
player_vel_y:  defb 0    ; Vertical velocity
GRAVITY        equ 1
MAX_FALL       equ 8

apply_gravity:
    ld a,(player_vel_y)
    add a,GRAVITY
    cp MAX_FALL
    jr c,.no_cap
    ld a,MAX_FALL
.no_cap:
    ld (player_vel_y),a

    ; Apply to position
    ld b,a
    ld a,(player_y)
    add a,b
    ld (player_y),a
    ret
```
**If it doesn't work:** Falling through floor? Collision check needed (next unit). Accelerating forever? Check terminal velocity cap.

---

### Unit 6: Platform Detection
**Builds:** Check if player is on solid ground.
**Teaches:** Pixel-level collision detection.
**Code pattern:**
```z80
; Check pixel below player's feet
check_floor:
    ld a,(player_x)
    ld e,a
    ld a,(player_y)
    add a,8         ; Check below sprite
    ld d,a
    call get_pixel_address
    ld a,(hl)       ; Get screen byte
    and c           ; Mask for pixel
    ret             ; Z=no floor, NZ=floor
```
**If it doesn't work:** Always falling? Check Y offset puts us below sprite. Never landing? Verify pixel address calculation.

---

### Unit 7: Landing on Platforms
**Builds:** Player stops falling when hitting platform.
**Teaches:** Collision response, velocity reset.
**Code pattern:**
```z80
update_player_y:
    call apply_gravity
    call check_floor
    ret z           ; No floor, keep falling

    ; Land on platform
    xor a
    ld (player_vel_y),a

    ; Align to platform
    ld a,(player_y)
    and $F8         ; Align to 8-pixel grid
    ld (player_y),a
    ret
```
**If it doesn't work:** Bouncing on landing? Velocity not zeroed. Sinking into platform? Alignment calculation wrong.

---

### Unit 8: Jump Input
**Builds:** Player can jump with Q or Space.
**Teaches:** Jump initiation, state flags.
**Code pattern:**
```z80
on_ground: defb 1
JUMP_POWER equ -12    ; Negative = upward

try_jump:
    ld a,(on_ground)
    or a
    ret z           ; Can't jump in air

    ; Check jump key
    ld a,$7F        ; Space row
    in a,($FE)
    bit 0,a
    ret nz          ; Space not pressed

    ; Jump!
    ld a,JUMP_POWER
    ld (player_vel_y),a
    xor a
    ld (on_ground),a
    ret
```
**If it doesn't work:** Can't jump? Check on_ground flag set when landing. Double jumping? Ensure flag clears immediately on jump.

---

### Unit 9: Jump Arc
**Builds:** Smooth parabolic jump trajectory.
**Teaches:** Physics feel, velocity curves.

---

### Unit 10: Head Collision
**Builds:** Player bonks head on ceiling, stops rising.
**Teaches:** Upward collision, velocity cancellation.
**Code pattern:**
```z80
check_head:
    ld a,(player_vel_y)
    bit 7,a         ; Check if moving up
    ret z           ; Moving down, ignore

    ; Check pixel above head
    ld a,(player_y)
    dec a           ; One pixel above
    ; ... get pixel at position
    and c
    ret z           ; No ceiling

    ; Bonk!
    xor a
    ld (player_vel_y),a
    ret
```
**If it doesn't work:** Going through ceilings? Check is only for upward movement. Getting stuck? Ensure position doesn't embed in ceiling.

---

### Unit 11: Left/Right Collision
**Builds:** Player blocked by walls.
**Teaches:** Horizontal collision checks.

---

### Unit 12: Walk Animation
**Builds:** Player legs animate while moving.
**Teaches:** Frame animation, direction facing.
**Code pattern:**
```z80
anim_frame:  defb 0
facing:      defb 1      ; 0=left, 1=right

; Alternate between walk frames
update_animation:
    ld a,(moving)
    or a
    ret z           ; Not moving, no animation

    ld a,(anim_frame)
    inc a
    and 3           ; 4 frames
    ld (anim_frame),a

    ; Get sprite for frame and direction
    ld b,a
    ld a,(facing)
    or a
    jr z,.left
    ld hl,walk_right_frames
    jr .done
.left:
    ld hl,walk_left_frames
.done:
    ; b = frame offset
    ; ... copy frame to UDG
    ret
```
**If it doesn't work:** Animation too fast? Only increment every N frames. Wrong direction? Check facing flag updates on input.

---

### Unit 13: Standing vs. Falling Animation
**Builds:** Different pose when falling.
**Teaches:** State-based animation.

---

### Unit 14: Player Colour
**Builds:** Player rendered in distinct colour.
**Teaches:** Attribute memory coordination.
**Code pattern:**
```z80
PLAYER_INK   equ 7      ; White
PLAYER_PAPER equ 0      ; Black
PLAYER_ATTR  equ (PLAYER_PAPER*8)+PLAYER_INK+64  ; +BRIGHT

set_player_colour:
    call get_attr_address
    ld a,PLAYER_ATTR
    ld (hl),a
    ret
```
**If it doesn't work:** Wrong colour? Check attribute byte construction. Colour in wrong place? Verify attribute address matches screen position.

---

### Unit 15: Platform Colours
**Builds:** Platforms have distinct colour.
**Teaches:** Level attribute setup.

---

### Unit 16: Phase 1 Polish
**Builds:** Smooth movement, correct collision feel.
**If it doesn't work:** Movement jerky? Check frame rate is consistent. Collision glitchy? Review edge cases in all directions.

---

## Phase 2: Hazards and Enemies (Units 17-32)

### Unit 17: Static Hazard - Spikes
**Builds:** Touching spikes kills player.
**Teaches:** Hazard collision, death handling.
**Code pattern:**
```z80
SPIKE_COLOUR equ $46    ; Yellow on black

check_hazards:
    call get_player_attr
    cp SPIKE_COLOUR
    ret nz          ; Not on spike

    ; Hit spike!
    call play_death_sound
    call player_death
    ret
```
**If it doesn't work:** Not detecting spikes? Check colour comparison exact. Dying randomly? Verify attribute read is at player position.

---

### Unit 18: Death Animation
**Builds:** Player flashes/spins on death.
**Teaches:** Death sequence, animation priority.

---

### Unit 19: Life System
**Builds:** Start with 3 lives, display remaining.
**Teaches:** Life tracking, HUD display.

---

### Unit 20: Patrolling Enemy
**Builds:** Robot that walks back and forth.
**Teaches:** Enemy AI basics, patrol patterns.
**Code pattern:**
```z80
enemy1_x:    defb 100
enemy1_dir:  defb 1     ; 1=right, -1=left
ENEMY_SPEED  equ 1

update_enemy1:
    ; Move in current direction
    ld a,(enemy1_x)
    ld hl,enemy1_dir
    add a,(hl)
    ld (enemy1_x),a

    ; Check boundaries / walls
    call enemy1_check_wall
    ret nc          ; No wall hit

    ; Reverse direction
    ld a,(enemy1_dir)
    neg
    ld (enemy1_dir),a
    ret
```
**If it doesn't work:** Enemy not moving? Check direction add is signed. Walking through walls? Verify wall check uses enemy position.

---

### Unit 21: Enemy Collision
**Builds:** Touching enemy kills player.
**Teaches:** Entity-to-entity collision.

---

### Unit 22: Multiple Enemies
**Builds:** Three patrolling enemies per screen.
**Teaches:** Enemy array management.

---

### Unit 23: Enemy Animation
**Builds:** Enemies have walk animation.
**Teaches:** Multi-entity animation.

---

### Unit 24: Crumbling Platforms
**Builds:** Platforms that collapse after standing on them.
**Teaches:** Timed hazards, level modification.
**Code pattern:**
```z80
; Track crumbling state for each crumbly platform
crumble_timers: defs 8  ; Up to 8 crumbling platforms

update_crumble:
    ; For each active crumble...
    ld ix,crumble_timers
    ld b,8
.loop:
    ld a,(ix+0)
    or a
    jr z,.next      ; Not active
    dec a
    ld (ix+0),a
    jr nz,.next     ; Still counting

    ; Timer expired - remove platform
    call remove_crumbled_platform
.next:
    inc ix
    djnz .loop
    ret
```
**If it doesn't work:** Not crumbling? Check timer starts when player lands. Crumbling instantly? Verify timer has enough frames.

---

### Unit 25: Conveyor Belts
**Builds:** Platforms that push player left or right.
**Teaches:** Environmental movement modifiers.

---

### Unit 26: Air Supply Introduction
**Builds:** Air bar depletes over time.
**Teaches:** Time pressure, resource management.
**Code pattern:**
```z80
air_supply: defb 255    ; Full air
AIR_DRAIN   equ 1       ; Per frame

update_air:
    ld a,(air_supply)
    sub AIR_DRAIN
    jr c,.dead      ; Ran out of air
    ld (air_supply),a
    call draw_air_bar
    ret
.dead:
    call player_death
    ret
```
**If it doesn't work:** Air lasting too long? Increase drain rate. Dying too fast? Balance for level completion time.

---

### Unit 27: Air Bar Display
**Builds:** Visual bar showing remaining air.
**Teaches:** HUD elements, progress bars.

---

### Unit 28: Air Refill
**Builds:** Completing level refills air.
**Teaches:** Level transition rewards.

---

### Unit 29: Falling Hazard
**Builds:** Stalactites that fall when player passes under.
**Teaches:** Triggered hazards.

---

### Unit 30: Moving Platform (Horizontal)
**Builds:** Platform that carries player side to side.
**Teaches:** Riding moving objects.
**Code pattern:**
```z80
platform1_x: defb 64
platform1_dir: defb 1

update_moving_platform:
    ; Move platform
    ld a,(platform1_x)
    ld hl,platform1_dir
    add a,(hl)
    ld (platform1_x),a

    ; If player is on this platform, move player too
    call is_player_on_platform1
    ret z           ; Not on platform

    ld a,(player_x)
    ld hl,platform1_dir
    add a,(hl)
    ld (player_x),a
    ret
```
**If it doesn't work:** Player not moving with platform? Check "on platform" detection. Sliding off? Player velocity might need adjustment.

---

### Unit 31: Moving Platform (Vertical)
**Builds:** Lift platforms.
**Teaches:** Vertical conveyance.

---

### Unit 32: Phase 2 Polish
**Builds:** All hazards feeling fair and consistent.

---

## Phase 3: Collectibles and Goals (Units 33-48)

### Unit 33: Key Items
**Builds:** Collect keys scattered around level.
**Teaches:** Collectible items, inventory.
**Code pattern:**
```z80
keys_collected: defb 0
keys_required:  defb 5

collect_key:
    ; Check if player touches key
    call check_key_collision
    ret z           ; No key here

    ; Collect it
    ld a,(keys_collected)
    inc a
    ld (keys_collected),a

    ; Remove key from screen
    call remove_key_sprite
    call play_collect_sound
    ret
```
**If it doesn't work:** Key not collecting? Check collision detection area. Count wrong? Verify increment only happens once per key.

---

### Unit 34: Key Display
**Builds:** Show collected keys in HUD.
**Teaches:** Inventory display.

---

### Unit 35: Exit Door
**Builds:** Door that opens when all keys collected.
**Teaches:** Win conditions, state changes.
**Code pattern:**
```z80
check_exit:
    ; Is player at door?
    call player_at_exit
    ret z           ; Not at exit

    ; Do we have all keys?
    ld a,(keys_collected)
    ld b,a
    ld a,(keys_required)
    cp b
    ret nz          ; Not enough keys

    ; Level complete!
    call level_complete
    ret
```
**If it doesn't work:** Door not working? Check both position AND key count. Triggering too easily? Verify exit position check is precise.

---

### Unit 36: Door Animation
**Builds:** Door visually opens when keys collected.
**Teaches:** State-based level graphics.

---

### Unit 37: Score Collectibles
**Builds:** Optional gems/coins for points.
**Teaches:** Risk/reward placement.

---

### Unit 38: Score Display
**Builds:** Show score at top of screen.
**Teaches:** Score rendering, number display.

---

### Unit 39: High Score
**Builds:** Track and display best score.
**Teaches:** Persistent best score.

---

### Unit 40: Bonus Points
**Builds:** Remaining air converted to score at level end.
**Teaches:** Completion bonuses.

---

### Unit 41: Level Timer
**Builds:** Optional speed-run timer display.
**Teaches:** Time tracking.

---

### Unit 42: Secret Areas
**Builds:** Hidden collectibles in non-obvious places.
**Teaches:** Exploration rewards.

---

### Unit 43: One-Up Item
**Builds:** Rare extra life collectible.
**Teaches:** High-value rewards.

---

### Unit 44: Power-Up - Speed
**Builds:** Temporary speed boost.
**Teaches:** Timed power-ups.

---

### Unit 45: Power-Up - Invincibility
**Builds:** Brief invulnerability.
**Teaches:** State-based immunity.

---

### Unit 46: Power-Up Display
**Builds:** Visual indicator of active power-up.
**Teaches:** Status effects HUD.

---

### Unit 47: Collectible Variety
**Builds:** Different items worth different points.
**Teaches:** Item variety.

---

### Unit 48: Phase 3 Polish
**Builds:** Satisfying collection, clear goals.

---

## Phase 4: Level Design (Units 49-64)

### Unit 49: Level Data Format
**Builds:** Compressed level storage.
**Teaches:** Data structures for levels.
**Code pattern:**
```z80
; Level data format:
; Byte 0-1: Platform count
; Then: X, Y, Width, Type for each platform
level1_data:
    defw 8          ; 8 platforms
    ; Platform 1: floor
    defb 0, 184, 32, PLATFORM_SOLID
    ; Platform 2: mid-level
    defb 48, 128, 8, PLATFORM_SOLID
    ; Platform 3: crumbling
    defb 96, 96, 4, PLATFORM_CRUMBLE
    ; ...
```
**If it doesn't work:** Platforms in wrong place? Check coordinate order (X, Y, Width). Wrong type? Verify type constants match drawing code.

---

### Unit 50: Level Loading
**Builds:** Decode and render level data.
**Teaches:** Level initialisation.

---

### Unit 51: Level 1 - Tutorial
**Builds:** Simple level teaching basic movement.
**Teaches:** Tutorial design, gentle introduction.

---

### Unit 52: Level 2 - Jump Practice
**Builds:** Level requiring jump timing.
**Teaches:** Skill ramp.

---

### Unit 53: Level 3 - First Enemies
**Builds:** Introduce patrolling enemies.
**Teaches:** Hazard introduction.

---

### Unit 54: Level 4 - Crumbling Challenge
**Builds:** Crumbling platforms are essential path.
**Teaches:** Mechanic-focused design.

---

### Unit 55: Level 5 - Vertical Climb
**Builds:** Ascending structure.
**Teaches:** Vertical level design.

---

### Unit 56: Levels 6-10 Design
**Builds:** Five more varied levels.
**Teaches:** Level variety.

---

### Unit 57: Levels 11-15 Design
**Builds:** Intermediate difficulty levels.
**Teaches:** Difficulty progression.

---

### Unit 58: Levels 16-20 Design
**Builds:** Expert difficulty levels.
**Teaches:** Challenge design.

---

### Unit 59: Enemy Placement
**Builds:** Strategic enemy positioning.
**Teaches:** Fair challenge design.

---

### Unit 60: Collectible Placement
**Builds:** Meaningful item positions.
**Teaches:** Reward design.

---

### Unit 61: Level Themes
**Builds:** Visual variety between levels.
**Teaches:** Aesthetic variation.

---

### Unit 62: Level Transitions
**Builds:** Smooth between-level sequence.
**Teaches:** Level flow.

---

### Unit 63: Level Select (Debug)
**Builds:** Quick access to any level.
**Teaches:** Development tools.

---

### Unit 64: Phase 4 Polish
**Builds:** 20 complete, balanced levels.

---

## Phase 5: Audio (Units 65-80)

### Unit 65: Beeper Basics
**Builds:** Simple tone output.
**Teaches:** Spectrum beeper control.
**Code pattern:**
```z80
; Simple beep - toggle speaker bit
beep:
    ld a,$10        ; Speaker bit
    ld b,100        ; Duration
.loop:
    out ($FE),a
    xor $10         ; Toggle
    ld c,50         ; Pitch delay
.delay:
    dec c
    jr nz,.delay
    djnz .loop
    ret
```
**If it doesn't work:** No sound? Check port $FE and bit 4. Wrong pitch? Adjust delay loop counter.

---

### Unit 66: Jump Sound
**Builds:** Quick ascending tone on jump.
**Teaches:** Action feedback.

---

### Unit 67: Collect Sound
**Builds:** Pleasant chime for collecting items.
**Teaches:** Reward audio.

---

### Unit 68: Death Sound
**Builds:** Descending/buzzing death tone.
**Teaches:** Failure audio.

---

### Unit 69: Enemy Sounds
**Builds:** Enemies make sounds.
**Teaches:** Entity audio.

---

### Unit 70: Level Complete Sound
**Builds:** Victory fanfare.
**Teaches:** Achievement audio.

---

### Unit 71: Air Warning Sound
**Builds:** Beeping when air low.
**Teaches:** Urgency audio.

---

### Unit 72: Music - Title Theme
**Builds:** Simple melody for title screen.
**Teaches:** Beeper music basics.

---

### Unit 73: Music - In-Game
**Builds:** Background music during play.
**Teaches:** Game music composition.

---

### Unit 74: Music - Game Over
**Builds:** Sad tune for game over.
**Teaches:** Mood through music.

---

### Unit 75: Sound Priority
**Builds:** Important sounds override others.
**Teaches:** Sound management.

---

### Unit 76: Sound/Music Toggle
**Builds:** Option to mute sounds.
**Teaches:** Audio options.

---

### Unit 77: Pitch Variation
**Builds:** Sounds vary slightly for interest.
**Teaches:** Audio polish.

---

### Unit 78: Crumble Sound
**Builds:** Distinct sound for crumbling platforms.
**Teaches:** Environmental audio.

---

### Unit 79: Moving Platform Sound
**Builds:** Mechanical sounds for lifts.
**Teaches:** Ambient audio.

---

### Unit 80: Phase 5 Polish
**Builds:** Complete, balanced audio.

---

## Phase 6: Game Features (Units 81-96)

### Unit 81: Title Screen
**Builds:** Attractive title with options.
**Teaches:** Game presentation.

---

### Unit 82: Menu System
**Builds:** Start game, options, high scores.
**Teaches:** Menu navigation.

---

### Unit 83: Options Menu
**Builds:** Sound toggle, controls display.
**Teaches:** Settings screens.

---

### Unit 84: High Score Entry
**Builds:** Enter initials for high score.
**Teaches:** Text input.

---

### Unit 85: High Score Table
**Builds:** Display top scores.
**Teaches:** Score display.

---

### Unit 86: Lives Display
**Builds:** Show remaining lives nicely.
**Teaches:** HUD design.

---

### Unit 87: Pause Feature
**Builds:** Pause game mid-level.
**Teaches:** Pause implementation.

---

### Unit 88: Continue System
**Builds:** Continue from last level.
**Teaches:** Progress saving.

---

### Unit 89: Password System
**Builds:** Level passwords for progress.
**Teaches:** Simple save system.
**Code pattern:**
```z80
; Generate 4-letter password from level number
; Level 5 = "COAL", Level 10 = "PICK", etc.
passwords:
    defm "MINECOALGOLDPICKAXE..."

get_password:
    ld a,(current_level)
    dec a           ; Level 1 = no password
    ret z
    sla a
    sla a           ; ×4 for offset
    ld hl,passwords
    ld e,a
    ld d,0
    add hl,de
    ; HL points to password
    ret
```
**If it doesn't work:** Wrong password? Check level-to-offset calculation. Not accepting valid password? Verify case-insensitive comparison.

---

### Unit 90: Instructions Screen
**Builds:** How to play information.
**Teaches:** Onboarding.

---

### Unit 91: Credits Screen
**Builds:** Attribution display.
**Teaches:** Credits design.

---

### Unit 92: Game Over Sequence
**Builds:** Proper game over handling.
**Teaches:** End state.

---

### Unit 93: Victory Sequence
**Builds:** Completion celebration.
**Teaches:** Win state.

---

### Unit 94: Two-Player Mode
**Builds:** Alternating two-player.
**Teaches:** Multiplayer basics.

---

### Unit 95: Attract Mode
**Builds:** Demo play when idle.
**Teaches:** Demonstration system.

---

### Unit 96: Phase 6 Polish
**Builds:** Complete feature set.

---

## Phase 7: Optimisation and Balance (Units 97-112)

### Unit 97: Frame Rate Check
**Builds:** Ensure 50fps consistency.
**Teaches:** Performance measurement.

---

### Unit 98: Drawing Optimisation
**Builds:** Only redraw changed sprites.
**Teaches:** Efficient rendering.

---

### Unit 99: Collision Optimisation
**Builds:** Faster collision checks.
**Teaches:** Algorithm efficiency.

---

### Unit 100: Memory Usage
**Builds:** Verify fits in 48K.
**Teaches:** Memory management.

---

### Unit 101: Difficulty Balance
**Builds:** Tune level difficulty curve.
**Teaches:** Playtesting feedback.

---

### Unit 102: Control Feel
**Builds:** Fine-tune jump and movement.
**Teaches:** Game feel.

---

### Unit 103: Enemy Speed Balance
**Builds:** Fair enemy movement speeds.
**Teaches:** Challenge balance.

---

### Unit 104: Air Supply Tuning
**Builds:** Right amount of time pressure.
**Teaches:** Resource balance.

---

### Unit 105: Hit Detection Tuning
**Builds:** Fair collision boxes.
**Teaches:** Hitbox design.

---

### Unit 106: Bug Hunting
**Builds:** Find and fix remaining bugs.
**Teaches:** Debugging process.

---

### Unit 107: Edge Cases
**Builds:** Handle unusual situations.
**Teaches:** Robustness.

---

### Unit 108: Playtest Feedback
**Builds:** Implement tester suggestions.
**Teaches:** Iterative improvement.

---

### Unit 109: Platform Alignment
**Builds:** Ensure pixel-perfect platform collision.
**Teaches:** Collision polish.

---

### Unit 110: Animation Timing
**Builds:** Smooth animation frame rates.
**Teaches:** Animation polish.

---

### Unit 111: Audio Balance
**Builds:** Volume levels appropriate.
**Teaches:** Audio mix.

---

### Unit 112: Phase 7 Polish
**Builds:** Stable, balanced game.

---

## Phase 8: Release (Units 113-128)

### Unit 113: Title Screen Art
**Builds:** Eye-catching title graphics.
**Teaches:** Logo design.

---

### Unit 114: Loading Screen
**Builds:** Image displayed during load.
**Teaches:** Presentation.

---

### Unit 115: Inlay Card Design
**Builds:** Cassette cover artwork concept.
**Teaches:** Marketing materials.

---

### Unit 116: Manual Content
**Builds:** Write instruction manual.
**Teaches:** Documentation.

---

### Unit 117: TAP File Creation
**Builds:** Standard tape format.
**Teaches:** Distribution format.

---

### Unit 118: TZX File Creation
**Builds:** Enhanced tape format with loading screen.
**Teaches:** Advanced distribution.

---

### Unit 119: Emulator Testing
**Builds:** Verify in multiple emulators.
**Teaches:** Compatibility testing.

---

### Unit 120: Hardware Testing
**Builds:** Test on real Spectrum.
**Teaches:** Hardware verification.

---

### Unit 121: 128K Detection
**Builds:** Check for 128K features (optional).
**Teaches:** Hardware detection.

---

### Unit 122: Easter Eggs
**Builds:** Hidden features.
**Teaches:** Secrets.

---

### Unit 123: Cheat Codes
**Builds:** Debug cheats.
**Teaches:** Cheat systems.

---

### Unit 124: Release Candidate
**Builds:** Final test build.
**Teaches:** Release process.

---

### Unit 125: Final Bug Fixes
**Builds:** Last-minute fixes.
**Teaches:** Polish cycle.

---

### Unit 126: Version Numbering
**Builds:** Track releases.
**Teaches:** Version control.

---

### Unit 127: Community Release
**Builds:** Prepare for distribution.
**Teaches:** Release preparation.

---

### Unit 128: Release Complete
**Builds:** Final release.
**Teaches:** Shipping a game.

---

## Version History

- **1.0 (2026-01-18):** Initial 128-unit outline created.
