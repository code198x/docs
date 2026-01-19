# Phase 1 Breakdown: C64 Starfield (Game 1)

**Game:** Starfield (Game 1 — revised)
**Phase:** 1 of 8 (128-unit structure)
**Units:** 1-16
**Theme:** Your First Shoot-'em-up

---

## Design Principles

1. **Playable in Unit 1** — ship moves and shoots from the first session
2. **Every unit improves the game** — no theory-only units
3. **Debugging inline** — "if it doesn't work, check X" right where you need it
4. **Sound from the start** — laser pew in Unit 1, not Unit 10
5. **Visuals always** — never a blank screen

---

## Phase 1 Overview

By the end of Phase 1, learners will have:
- A complete single-screen shooter (move, shoot, enemies, scoring)
- Basic SID sound effects (laser, explosion)
- Understanding of sprites, joystick, collision
- Confidence to debug common sprite problems

**Phase 1 Output:** Playable game — ship vs waves of enemies, with sound and score.

---

## Unit Progression

### Unit 1: Ship That Shoots
**Time:** 60 minutes
**You Build:** A spaceship that moves and fires

Type this complete program. It runs. You play it.

```asm
; Starfield - Unit 1: Ship That Shoots
; Assemble with: acme -f cbm -o starfield.prg starfield.asm

*= $0801
!byte $0c,$08,$0a,$00,$9e,$32,$30,$36,$31,$00,$00,$00

*= $080d
        sei
        cld

        ; Black background, dark blue border
        lda #$00
        sta $d020
        sta $d021

        ; Enable sprite 0
        lda #$01
        sta $d015

        ; Sprite 0 position (centre-ish)
        lda #$b0
        sta $d000           ; X
        lda #$e0
        sta $d001           ; Y

        ; Sprite 0 pointer (block 13 = $0340)
        lda #$0d
        sta $07f8

        ; Sprite 0 colour (white)
        lda #$01
        sta $d027

        ; Copy ship sprite data to $0340
        ldx #$3e
-       lda ship_sprite,x
        sta $0340,x
        dex
        bpl -

        ; Enable bullet sprite (sprite 1)
        lda #$03
        sta $d015           ; Sprites 0 and 1

        ; Bullet pointer (block 14 = $0380)
        lda #$0e
        sta $07f9

        ; Bullet colour (yellow)
        lda #$07
        sta $d028

        ; Bullet starts off-screen
        lda #$00
        sta $d002           ; Bullet X
        sta $d003           ; Bullet Y
        sta bullet_active

        cli

main_loop:
        ; Wait for raster line 255 (simple frame sync)
-       lda $d012
        cmp #$ff
        bne -

        jsr read_joystick
        jsr move_ship
        jsr check_fire
        jsr move_bullet

        jmp main_loop

; --- Joystick reading ---
read_joystick:
        lda $dc00           ; CIA1 port A (joystick 2)
        sta joy_state
        rts

; --- Ship movement ---
move_ship:
        lda joy_state
        lsr                 ; Bit 0 = up
        bcs +
        dec $d001           ; Move up
        dec $d001
+       lsr                 ; Bit 1 = down
        bcs +
        inc $d001           ; Move down
        inc $d001
+       lsr                 ; Bit 2 = left
        bcs +
        dec $d000           ; Move left
        dec $d000
+       lsr                 ; Bit 3 = right
        bcs +
        inc $d000           ; Move right
        inc $d000
+       rts

; --- Fire button ---
check_fire:
        lda bullet_active
        bne +               ; Already a bullet flying

        lda joy_state
        and #$10            ; Bit 4 = fire (active low)
        bne +               ; Not pressed

        ; Fire!
        lda $d000           ; Ship X
        clc
        adc #$0c            ; Centre of ship
        sta $d002           ; Bullet X
        lda $d001           ; Ship Y
        sta $d003           ; Bullet Y

        lda #$01
        sta bullet_active

        ; --- SOUND: Laser pew ---
        lda #$0f
        sta $d418           ; Volume on
        lda #$00
        sta $d405           ; Attack/Decay
        lda #$a8            ; Sustain/Release
        sta $d406
        lda #$20            ; Frequency low
        sta $d400
        lda #$18            ; Frequency high
        sta $d401
        lda #$81            ; Noise + gate
        sta $d404
+       rts

; --- Bullet movement ---
move_bullet:
        lda bullet_active
        beq +               ; No bullet

        ; Move bullet up
        lda $d003
        sec
        sbc #$04            ; Bullet speed
        sta $d003

        cmp #$10            ; Off top of screen?
        bcs +
        lda #$00
        sta bullet_active   ; Deactivate
        sta $d003           ; Hide bullet
+
        ; Turn off sound after a few frames
        lda $d003
        cmp #$d0
        bcc ++
        lda #$80            ; Gate off
        sta $d404
++      rts

; --- Data ---
joy_state:      !byte 0
bullet_active:  !byte 0

ship_sprite:
        !byte %00011000, %00000000, %00000000
        !byte %00011000, %00000000, %00000000
        !byte %00011000, %00000000, %00000000
        !byte %00111100, %00000000, %00000000
        !byte %00111100, %00000000, %00000000
        !byte %01111110, %00000000, %00000000
        !byte %01111110, %00000000, %00000000
        !byte %11111111, %00000000, %00000000
        !byte %11111111, %00000000, %00000000
        !byte %11100111, %00000000, %00000000
        !byte %11000011, %00000000, %00000000
        !byte %00000000, %00000000, %00000000
        !byte %00000000, %00000000, %00000000
        !byte %00000000, %00000000, %00000000
        !byte %00000000, %00000000, %00000000
        !byte %00000000, %00000000, %00000000
        !byte %00000000, %00000000, %00000000
        !byte %00000000, %00000000, %00000000
        !byte %00000000, %00000000, %00000000
        !byte %00000000, %00000000, %00000000
        !byte %00000000, %00000000, %00000000

bullet_sprite = ship_sprite + 63    ; Just use a dot (we'll improve later)
```

**What you get:** A spaceship you control with the joystick. Press fire — laser shoots up with a "pew" sound.

**If it doesn't work:**
- **Black screen, no sprite?** Check `$d015` — must be non-zero to enable sprites
- **Sprite in wrong place?** X is `$d000`, Y is `$d001` — easy to swap
- **No sound?** Check `$d418` — volume must be non-zero ($0f = max)
- **Fire doesn't work?** Joystick 2 is `$dc00`, joystick 1 is `$dc01`

**Experiment:** Change `$d027` to different values (0-15). Watch your ship change colour.

---

### Unit 2: Enemies Appear
**Time:** 60 minutes
**You Build:** Enemies that spawn and move down

Add enemies using sprites 2-7. They appear at the top and drift down.

**New code added:**

```asm
; In init section:
        ; Enable sprites 0-7
        lda #$ff
        sta $d015

        ; Set enemy sprite pointers (all use block 15)
        lda #$0f
        sta $07fa           ; Sprite 2
        sta $07fb           ; Sprite 3
        sta $07fc           ; Sprite 4
        sta $07fd           ; Sprite 5
        sta $07fe           ; Sprite 6
        sta $07ff           ; Sprite 7

        ; Enemy colours (green)
        lda #$05
        sta $d029
        sta $d02a
        sta $d02b
        sta $d02c
        sta $d02d
        sta $d02e

        jsr init_enemies

; New routines:
init_enemies:
        ldx #$05            ; 6 enemies (sprites 2-7)
-       lda #$00
        sta enemy_active,x  ; All start inactive
        dex
        bpl -
        rts

spawn_enemy:
        ; Find an inactive enemy slot
        ldx #$05
-       lda enemy_active,x
        beq +               ; Found one
        dex
        bpl -
        rts                 ; All slots full
+
        ; Spawn at random X, top of screen
        lda $d012           ; Pseudo-random from raster
        and #$7f
        clc
        adc #$40            ; Range ~64-191
        sta enemy_x,x
        lda #$32            ; Start Y (top)
        sta enemy_y,x
        lda #$01
        sta enemy_active,x
        rts

move_enemies:
        ldx #$05
-       lda enemy_active,x
        beq ++              ; Skip inactive

        ; Move down
        lda enemy_y,x
        clc
        adc #$01            ; Enemy speed
        sta enemy_y,x

        ; Off bottom?
        cmp #$f8
        bcc +
        lda #$00
        sta enemy_active,x  ; Deactivate
+
        ; Update sprite position
        txa
        asl                 ; ×2 for sprite register offset
        asl
        clc
        adc #$04            ; Sprite 2 starts at $d004
        tay
        lda enemy_x,x
        sta $d000,y
        lda enemy_y,x
        sta $d001,y
++      dex
        bpl -
        rts

; In main loop, add:
        jsr move_enemies
        jsr maybe_spawn

maybe_spawn:
        ; Spawn enemy every ~60 frames
        inc spawn_timer
        lda spawn_timer
        cmp #$3c
        bcc +
        lda #$00
        sta spawn_timer
        jsr spawn_enemy
+       rts

; Data
enemy_x:        !fill 6, 0
enemy_y:        !fill 6, 0
enemy_active:   !fill 6, 0
spawn_timer:    !byte 0
```

**What you get:** Enemies drift down from the top. Your ship flies around. Bullets still fire.

**If it doesn't work:**
- **Only some enemies show?** Check all sprite pointers ($07fa-$07ff)
- **Enemies stuck at top?** Check `move_enemies` is called in main loop
- **Enemies flicker?** You might have two using same slot — check `spawn_enemy` logic

**Experiment:** Change enemy speed (the `adc #$01` in move_enemies). Make them faster/slower.

---

### Unit 3: Collision — Bullet Hits Enemy
**Time:** 60 minutes
**You Build:** Bullets destroy enemies (with explosion sound)

**New code added:**

```asm
check_bullet_hits:
        lda bullet_active
        beq +               ; No bullet flying

        ldx #$05
-       lda enemy_active,x
        beq ++              ; Enemy not active

        ; Check X distance
        lda $d002           ; Bullet X
        sec
        sbc enemy_x,x
        bpl .pos_x
        eor #$ff            ; Absolute value
        clc
        adc #$01
.pos_x: cmp #$10            ; Within 16 pixels?
        bcs ++              ; No hit

        ; Check Y distance
        lda $d003           ; Bullet Y
        sec
        sbc enemy_y,x
        bpl .pos_y
        eor #$ff
        clc
        adc #$01
.pos_y: cmp #$10            ; Within 16 pixels?
        bcs ++              ; No hit

        ; HIT!
        lda #$00
        sta enemy_active,x  ; Kill enemy
        sta bullet_active   ; Remove bullet
        sta $d003           ; Hide bullet

        jsr explosion_sound
        jmp +               ; Done checking
++      dex
        bpl -
+       rts

explosion_sound:
        lda #$0f
        sta $d418
        lda #$00
        sta $d405
        lda #$f0            ; Long release
        sta $d406
        lda #$00
        sta $d400
        lda #$08            ; Low frequency
        sta $d401
        lda #$81            ; Noise + gate
        sta $d404
        rts
```

**What you get:** Shoot enemies, they vanish with a satisfying explosion noise.

**If it doesn't work:**
- **Bullets pass through?** Check collision distance — 16 pixels might be too tight, try 20
- **Wrong enemies dying?** Make sure you're comparing bullet position to enemy X/Y, not sprite registers directly
- **No explosion sound?** Is volume still on? Laser sound might have turned it off

**Experiment:** Change collision distance. Make it generous (easier) or tight (harder).

---

### Unit 4: Score Display
**Time:** 60 minutes
**You Build:** Score that increases when you hit enemies

**New code added:**

```asm
; In init:
        jsr init_score_display

init_score_display:
        ; Print "SCORE:" at top of screen
        ldx #$00
-       lda score_text,x
        beq +
        sta $0400,x         ; Screen memory
        lda #$01            ; White
        sta $d800,x         ; Colour memory
        inx
        bne -
+       rts

score_text:
        !scr "score: 00000"
        !byte 0

add_score:
        ; Add 10 points
        sed                 ; Decimal mode for BCD
        clc
        lda score
        adc #$10
        sta score
        lda score+1
        adc #$00
        sta score+1
        cld

        ; Update display
        jsr update_score_display
        rts

update_score_display:
        lda score+1
        lsr
        lsr
        lsr
        lsr
        ora #$30            ; Convert to PETSCII digit
        sta $0407           ; Ten thousands
        lda score+1
        and #$0f
        ora #$30
        sta $0408           ; Thousands
        lda score
        lsr
        lsr
        lsr
        lsr
        ora #$30
        sta $0409           ; Hundreds
        lda score
        and #$0f
        ora #$30
        sta $040a           ; Tens
        lda #$30            ; Always 0 (we add 10 at a time)
        sta $040b           ; Ones
        rts

score:  !word 0

; In check_bullet_hits, after "HIT!":
        jsr add_score
```

**What you get:** "SCORE: 00000" at top. +10 points per enemy destroyed.

**If it doesn't work:**
- **Garbage instead of numbers?** Check PETSCII conversion — digits are $30-$39
- **Score doesn't update?** Make sure `add_score` is called after the hit
- **Score shows wrong values?** BCD mode is tricky — make sure you `cld` after

**Experiment:** Change points per enemy. Make big enemies worth more (later).

---

### Unit 5: Ship-Enemy Collision (Game Over)
**Time:** 60 minutes
**You Build:** Crash into enemy = game over

**New code added:**

```asm
check_ship_hit:
        ldx #$05
-       lda enemy_active,x
        beq ++              ; Skip inactive

        ; Check X distance
        lda $d000           ; Ship X
        sec
        sbc enemy_x,x
        bpl .pos_x
        eor #$ff
        clc
        adc #$01
.pos_x: cmp #$14            ; Within 20 pixels?
        bcs ++

        ; Check Y distance
        lda $d001           ; Ship Y
        sec
        sbc enemy_y,x
        bpl .pos_y
        eor #$ff
        clc
        adc #$01
.pos_y: cmp #$14
        bcs ++

        ; CRASH!
        jsr game_over
        jmp game_over_loop  ; Stop main loop
++      dex
        bpl -
        rts

game_over:
        ; Flash border red
        lda #$02
        sta $d020

        ; Big explosion sound
        lda #$0f
        sta $d418
        lda #$0f            ; Slow attack
        sta $d405
        lda #$f9            ; Long decay
        sta $d406
        lda #$00
        sta $d400
        lda #$02            ; Very low
        sta $d401
        lda #$81
        sta $d404

        ; Print GAME OVER
        ldx #$00
-       lda gameover_text,x
        beq +
        sta $05e0,x         ; Centre of screen
        lda #$02            ; Red
        sta $d9e0,x
        inx
        bne -
+       rts

gameover_text:
        !scr "game over"
        !byte 0

game_over_loop:
        ; Wait for fire to restart
        lda $dc00
        and #$10
        bne game_over_loop
        jmp $080d           ; Restart game
```

**What you get:** Hit an enemy = screen flashes, "GAME OVER", press fire to restart.

**If it doesn't work:**
- **Dying when enemies aren't near?** Check collision box size — 20 pixels is generous
- **Game over text in wrong place?** $05e0 is row 15. Adjust address for different position
- **Can't restart?** Check fire button logic (active low — AND #$10, BNE means not pressed)

**Experiment:** Make collision box smaller (harder) or bigger (easier).

---

### Unit 6: Enemy Variety
**Time:** 60 minutes
**You Build:** Two enemy types with different speeds

**New code added:**

```asm
; In data section:
enemy_type:     !fill 6, 0      ; 0 = fast, 1 = slow

; In spawn_enemy:
        ; Random enemy type
        lda $d012
        and #$01
        sta enemy_type,x

        ; Different sprite for each type
        beq .fast_enemy
        lda #$10            ; Block 16 for slow enemy
        bne .set_pointer
.fast_enemy:
        lda #$0f            ; Block 15 for fast enemy
.set_pointer:
        ; Set sprite pointer (sprite 2+x)
        txa
        clc
        adc #$fa            ; $07fa = sprite 2 pointer
        tay
        sta $0700,y

; In move_enemies, replace fixed speed:
        lda enemy_type,x
        beq .fast_speed
        lda enemy_y,x       ; Slow enemy
        clc
        adc #$01
        jmp .set_y
.fast_speed:
        lda enemy_y,x       ; Fast enemy
        clc
        adc #$02
.set_y: sta enemy_y,x
```

**What you get:** Two enemy types — fast (green) and slow (different colour). Different sprites.

**If it doesn't work:**
- **All enemies same speed?** Check the type branch logic
- **Wrong sprites showing?** Sprite pointers are at $07f8+sprite_number

**Experiment:** Add a third enemy type. Maybe one that moves diagonally?

---

### Unit 7: Lives System
**Time:** 60 minutes
**You Build:** Three lives, displayed as ship icons

**New code added:**

```asm
lives:  !byte 3

init_lives_display:
        ; Draw 3 ship icons at top-right
        lda #$51            ; Ship character (custom or use *)
        sta $0417
        sta $0418
        sta $0419
        lda #$01            ; White
        sta $d817
        sta $d818
        sta $d819
        rts

update_lives_display:
        lda lives
        cmp #$03
        bcc +
        lda #$51
        bne ++
+       lda #$20            ; Space (blank)
++      sta $0419
        lda lives
        cmp #$02
        bcc +
        lda #$51
        bne ++
+       lda #$20
++      sta $0418
        ; First life icon always shown until 0
        rts

lose_life:
        dec lives
        beq game_over       ; No lives left

        jsr update_lives_display

        ; Brief invincibility flash
        lda #$10            ; Frames of invincibility
        sta invincible
        rts

invincible: !byte 0

; In check_ship_hit, at start:
        lda invincible
        beq .can_die
        dec invincible
        rts
.can_die:

; When hit, call lose_life instead of game_over directly
```

**What you get:** Three lives. Lose one when hit. Brief invincibility after respawn. Game over when all gone.

**If it doesn't work:**
- **Lives don't decrease?** Check `lose_life` is called on collision
- **Die instantly after respawn?** Invincibility counter not working — check it's decremented

**Experiment:** Change starting lives. Add extra life at 1000 points.

---

### Unit 8: Title Screen
**Time:** 60 minutes
**You Build:** Title screen before game starts

```asm
; New entry point
*= $080d
        jsr show_title
        jmp game_init

show_title:
        ; Clear screen
        lda #$20
        ldx #$00
-       sta $0400,x
        sta $0500,x
        sta $0600,x
        sta $0700,x
        inx
        bne -

        ; Draw title
        ldx #$00
-       lda title_text,x
        beq +
        sta $0400+172,x     ; Row 5, centered
        lda #$07            ; Yellow
        sta $d800+172,x
        inx
        bne -
+
        ; Draw "PRESS FIRE TO START"
        ldx #$00
-       lda start_text,x
        beq +
        sta $0400+452,x     ; Row 14
        lda #$01
        sta $d800+452,x
        inx
        bne -
+
        ; Wait for fire
-       lda $dc00
        and #$10
        bne -
        ; Wait for release
-       lda $dc00
        and #$10
        beq -
        rts

title_text:
        !scr "starfield"
        !byte 0
start_text:
        !scr "press fire to start"
        !byte 0
```

**What you get:** Title screen with game name. Press fire to start.

**If it doesn't work:**
- **Text garbled?** Check PETSCII — lowercase in assembler often needs `!scr`
- **Starts immediately without waiting?** Fire button check is active low

**Experiment:** Add high score display on title screen.

---

### Unit 9: Wave System
**Time:** 60 minutes
**You Build:** Waves that get harder

```asm
wave_number:    !byte 1
enemies_left:   !byte 10
spawn_delay:    !byte 60

start_wave:
        lda wave_number
        asl
        asl                 ; ×4
        clc
        adc #$06            ; Base 6 + wave×4 enemies
        sta enemies_left

        ; Faster spawning each wave
        lda #$3c            ; 60 frames base
        sec
        sbc wave_number
        sbc wave_number
        sbc wave_number     ; -3 per wave
        cmp #$10            ; Minimum 16 frames
        bcs +
        lda #$10
+       sta spawn_delay

        ; Display wave number
        jsr show_wave_banner
        rts

show_wave_banner:
        ; "WAVE X" briefly on screen
        ; ... (similar to title text drawing)
        rts

check_wave_complete:
        ; All enemies spawned and cleared?
        lda enemies_left
        ora enemy_active+0
        ora enemy_active+1
        ora enemy_active+2
        ora enemy_active+3
        ora enemy_active+4
        ora enemy_active+5
        bne +

        ; Wave complete!
        inc wave_number
        jsr start_wave
+       rts
```

**What you get:** Waves of enemies. Each wave has more enemies, faster spawning.

**If it doesn't work:**
- **Wave never ends?** Check all enemy slots are cleared
- **Spawn delay broken?** Don't let it go below minimum or it overflows

**Experiment:** Add bonus points for completing a wave.

---

### Unit 10: Enemy Shooting
**Time:** 75 minutes
**You Build:** Enemies that shoot back

```asm
enemy_bullet_x:     !byte 0
enemy_bullet_y:     !byte 0
enemy_bullet_active: !byte 0

; Enable sprite for enemy bullet (sprite 1 becomes player bullet, we need another)
; Actually, let's use the X MSB trick or reuse sprite carefully
; For simplicity, enemy bullets are character-based

update_enemy_bullets:
        lda enemy_bullet_active
        beq try_enemy_fire

        ; Move enemy bullet down
        inc enemy_bullet_y
        inc enemy_bullet_y

        ; Off screen?
        lda enemy_bullet_y
        cmp #$f8
        bcc +
        lda #$00
        sta enemy_bullet_active
        jmp ++
+
        ; Draw bullet (character at position)
        jsr draw_enemy_bullet

        ; Check if hits player
        jsr check_player_hit
++      rts

try_enemy_fire:
        ; Random chance to fire
        lda $d012
        and #$3f
        bne +               ; ~1/64 chance per frame

        ; Pick a random active enemy
        ; ... (simplified: use first active enemy)
        ldx #$05
-       lda enemy_active,x
        bne .found
        dex
        bpl -
        rts                 ; No active enemies
.found:
        lda enemy_x,x
        sta enemy_bullet_x
        lda enemy_y,x
        sta enemy_bullet_y
        lda #$01
        sta enemy_bullet_active
+       rts

draw_enemy_bullet:
        ; Convert pixel coords to screen position
        ; ... (divide by 8 for character position)
        rts

check_player_hit:
        ; Compare enemy bullet to ship position
        ; ... (similar to ship-enemy collision)
        ; If hit, call lose_life
        rts
```

**What you get:** Enemies occasionally fire back. Dodge or die!

**If it doesn't work:**
- **Enemy bullets invisible?** Character drawing needs screen address calculation
- **Too many bullets?** Limit to one at a time (we only track one)
- **Never fires?** Check random number logic — might never hit condition

**Experiment:** Make enemies fire more often in later waves.

---

### Unit 11: Polish — Better Sprites
**Time:** 60 minutes
**You Build:** Improved ship and enemy graphics

Replace placeholder sprites with better-looking versions.

```asm
ship_sprite:
        ; Improved ship design
        !byte %00011000, %00000000, %00000000
        !byte %00111100, %00000000, %00000000
        !byte %00111100, %00000000, %00000000
        !byte %01111110, %00000000, %00000000
        !byte %11111111, %00000000, %00000000
        !byte %11111111, %00000000, %00000000
        !byte %11111111, %00000000, %00000000
        !byte %01111110, %10000001, %00000000
        !byte %01100110, %11000011, %00000000
        !byte %01000010, %01000010, %00000000
        ; ... etc
```

**What you get:** Game looks more polished. Same mechanics.

**If it doesn't work:**
- **Sprite looks wrong?** Remember sprites are 24×21 pixels, 3 bytes per row
- **Colours off?** Multicolour sprites need different setup

**Experiment:** Design your own ship. Make enemies look menacing.

---

### Unit 12: Polish — Sound Improvements
**Time:** 60 minutes
**You Build:** Better sound effects, background "music"

```asm
; Background pulse/drone using voice 3
init_bg_sound:
        lda #$08
        sta $d40f           ; Low frequency
        lda #$01
        sta $d40e
        lda #$08
        sta $d412           ; Attack/Decay
        lda #$40            ; Low sustain
        sta $d413
        lda #$41            ; Pulse + gate
        sta $d411
        rts

; Improved laser with pitch bend
laser_sound:
        lda #$00
        sta $d405
        lda #$a8
        sta $d406
        lda #$30
        sta $d400
        lda #$20
        sta $d401
        lda #$21            ; Sawtooth + gate (sharper than noise)
        sta $d404
        ; Pitch will drop over next few frames
        rts

; Call from main loop
update_sound:
        ; Drop laser pitch for "pew" effect
        lda $d401
        beq +
        dec $d401
+       rts
```

**What you get:** Low background hum, better laser sound with pitch drop.

**If it doesn't work:**
- **Sounds clash?** Each voice is independent — check you're using different voices
- **Background too loud?** Adjust sustain level in voice 3

**Experiment:** Create different sounds for each enemy type destruction.

---

### Unit 13: Polish — Starfield Background
**Time:** 60 minutes
**You Build:** Scrolling stars in background (hence the name!)

```asm
NUM_STARS = 20
star_x:     !fill NUM_STARS, 0
star_y:     !fill NUM_STARS, 0
star_speed: !fill NUM_STARS, 0
star_char:  !fill NUM_STARS, 0

init_stars:
        ldx #NUM_STARS-1
-       lda $d012           ; Random X
        sta star_x,x
        lda $d011           ; Random Y
        sta star_y,x
        lda $d012
        and #$03
        clc
        adc #$01            ; Speed 1-4
        sta star_speed,x
        ; Random char (. or *)
        lda $d012
        and #$01
        beq +
        lda #$2e            ; .
        bne ++
+       lda #$2a            ; *
++      sta star_char,x
        dex
        bpl -
        rts

update_stars:
        ldx #NUM_STARS-1
-       ; Erase old position
        jsr erase_star

        ; Move down
        lda star_y,x
        clc
        adc star_speed,x
        cmp #$c8            ; 200 = bottom
        bcc +
        lda #$00            ; Wrap to top
+       sta star_y,x

        ; Draw new position
        jsr draw_star

        dex
        bpl -
        rts

erase_star:
        ; Calculate screen position, write space
        ; ... (y÷8 * 40 + x÷8)
        rts

draw_star:
        ; Calculate screen position, write star_char
        ; ...
        rts
```

**What you get:** Scrolling starfield in background. Different speeds = parallax effect.

**If it doesn't work:**
- **Stars flicker?** Erase before draw, and do during vblank
- **Stars and sprites clash?** Stars are characters, sprites are on top — should be fine

**Experiment:** More stars. Different speeds. Dim colours for distant stars.

---

### Unit 14: Polish — Screen Shake & Juice
**Time:** 60 minutes
**You Build:** Screen shake on explosions, visual polish

```asm
shake_timer: !byte 0

trigger_shake:
        lda #$08            ; 8 frames of shake
        sta shake_timer
        rts

update_shake:
        lda shake_timer
        beq +
        dec shake_timer
        and #$01
        beq .shake_right
        lda #$00            ; Normal position
        bne .set_scroll
.shake_right:
        lda #$01            ; Shifted 1 pixel
.set_scroll:
        sta $d016
+       rts

; Call trigger_shake when enemy destroyed
```

**What you get:** Screen shakes when enemies explode. Feels impactful.

**If it doesn't work:**
- **Shake too violent?** Only modify lower bits of $d016 (scroll fine position)
- **Screen doesn't reset?** Make sure shake_timer reaches 0 and resets scroll

**Experiment:** Bigger shake for bigger enemies.

---

### Unit 15: High Score
**Time:** 60 minutes
**You Build:** High score that persists (in memory at least)

```asm
high_score: !word 0

check_high_score:
        ; Compare score to high_score
        lda score+1
        cmp high_score+1
        bcc +               ; Current < high
        bne .new_high       ; Current > high
        lda score
        cmp high_score
        bcc +               ; Current < high
        beq +               ; Equal, no update
.new_high:
        lda score
        sta high_score
        lda score+1
        sta high_score+1
        ; Could trigger fanfare here
+       rts

; Display high score on title screen and during game
```

**What you get:** High score tracked and displayed. Bragging rights.

**If it doesn't work:**
- **High score resets?** It's in RAM — only persists while machine is on
- **Comparison wrong?** BCD comparison is tricky — compare high byte first

**Experiment:** Add initials entry for high score (advanced — needs text input).

---

### Unit 16: Complete Game
**Time:** 60 minutes
**You Build:** Final polish, all systems integrated

Combine everything:
- Title screen with high score
- Wave progression
- Multiple enemy types
- Lives system
- Sound effects and background
- Starfield
- Screen shake
- Game over with restart

**Final checklist:**
- [ ] Title screen shows, waits for fire
- [ ] Game starts, ship moves and shoots
- [ ] Enemies spawn and move down
- [ ] Bullets destroy enemies (sound + score)
- [ ] Player collision loses life
- [ ] Three lives, displayed
- [ ] Waves get harder
- [ ] Enemies shoot back
- [ ] Starfield scrolls
- [ ] Screen shakes on explosions
- [ ] Game over when lives exhausted
- [ ] High score tracked
- [ ] Press fire to restart

**If something doesn't work:**
- Go back to the unit where it was added
- Each unit's debugging tips still apply
- Most common: something not called in main loop

**You've built a complete game.** 🎮

---

## Phase 1 Summary

| Unit | You Build | Debugging Inline |
|------|-----------|------------------|
| 1 | Ship moves, shoots, sound | Sprite enable, volume, joystick port |
| 2 | Enemies appear | Sprite pointers, main loop calls |
| 3 | Bullet-enemy collision | Collision distance, position comparison |
| 4 | Score display | PETSCII digits, BCD mode |
| 5 | Ship-enemy collision | Collision box, game over flow |
| 6 | Enemy variety | Type branching, sprite pointers |
| 7 | Lives system | Invincibility, life display |
| 8 | Title screen | Text drawing, fire button wait |
| 9 | Wave system | Wave completion check, spawn timing |
| 10 | Enemy shooting | Bullet position, random firing |
| 11 | Better sprites | Sprite data format |
| 12 | Better sound | Multiple voices, pitch effects |
| 13 | Starfield | Character position, parallax |
| 14 | Screen shake | Scroll register, timer |
| 15 | High score | BCD comparison |
| 16 | Integration | Full checklist |

**No theory-only units. Every unit = game improvement + relevant debugging.**

---

## Phase 2 Preview

Phase 1 gives you a complete single-screen shooter. Phase 2 expands:
- Power-ups (speed, spread shot, shields)
- More enemy types with different behaviours
- Boss enemies
- Background variety
- Two-player mode

Same structure: every unit improves the game, debugging inline.

---

**Version:** 1.0
**Last Updated:** 2026-01-17
