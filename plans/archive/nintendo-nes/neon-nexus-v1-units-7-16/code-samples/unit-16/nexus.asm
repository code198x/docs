;──────────────────────────────────────────────────────────────
; NEON NEXUS
; A fixed-screen action game for the Nintendo Entertainment System
; Unit 15: Title Screen and Game States
;──────────────────────────────────────────────────────────────

;==============================================================
; iNES HEADER
;==============================================================

.segment "HEADER"
    .byte "NES", $1A
    .byte 2
    .byte 1
    .byte $01
    .byte $00
    .byte 0,0,0,0,0,0,0,0

;==============================================================
; VARIABLES
;==============================================================

.segment "ZEROPAGE"

nmi_ready:      .res 1
frame_counter:  .res 1
buttons:        .res 1
player_x:       .res 1
player_y:       .res 1
enemy_x:        .res 4
enemy_y:        .res 4
enemy_dir_x:    .res 4
enemy_dir_y:    .res 4
item_x:         .res 1
item_y:         .res 1
score:          .res 1
game_state:     .res 1      ; Current game state
score_dirty:    .res 1
lives:          .res 1
lives_dirty:    .res 1
invuln_timer:   .res 1
sfx_timer:      .res 1
sfx_type:       .res 1
screen_drawn:   .res 1      ; Has current screen been drawn?

;==============================================================
; CONSTANTS
;==============================================================

.segment "CODE"

PPUCTRL   = $2000
PPUMASK   = $2001
PPUSTATUS = $2002
OAMADDR   = $2003
PPUSCROLL = $2005
PPUADDR   = $2006
PPUDATA   = $2007
OAMDMA    = $4014
JOYPAD1   = $4016

APU_PULSE1_CTRL = $4000
APU_PULSE1_SWEEP = $4001
APU_PULSE1_LO = $4002
APU_PULSE1_HI = $4003
APU_STATUS = $4015

BTN_A      = %00000001
BTN_B      = %00000010
BTN_SELECT = %00000100
BTN_START  = %00001000
BTN_UP     = %00010000
BTN_DOWN   = %00100000
BTN_LEFT   = %01000000
BTN_RIGHT  = %10000000

NUM_ENEMIES = 4
HITBOX_SIZE = 7
ITEM_HITBOX = 8
TILE_DIGIT_0 = 5
STARTING_LIVES = 3
INVULN_FRAMES = 90

SFX_NONE = 0
SFX_COLLECT = 1
SFX_HIT = 2

; Game states
STATE_TITLE = 0
STATE_PLAYING = 1
STATE_GAMEOVER = 2

; Letter tiles (reuse existing S,C,O,R,E,L,I,V at 20-27)
TILE_S = 20
TILE_C = 21
TILE_O = 22
TILE_R = 23
TILE_E = 24
TILE_L = 25
TILE_I = 26
TILE_V = 27
; Additional letters for title/game over
TILE_N = 28
TILE_X = 29
TILE_P = 30
TILE_T = 31
TILE_A = 32
TILE_G = 33
TILE_M = 34
TILE_U = 35

;==============================================================
; RESET HANDLER
;==============================================================

.proc reset
    sei
    cld
    ldx #$40
    stx $4017
    ldx #$FF
    txs
    inx
    stx PPUCTRL
    stx PPUMASK
    stx $4010

@vblank_wait_1:
    bit PPUSTATUS
    bpl @vblank_wait_1

    lda #$00
@clear_ram:
    sta $0000, x
    sta $0100, x
    sta $0200, x
    sta $0300, x
    sta $0400, x
    sta $0500, x
    sta $0600, x
    sta $0700, x
    inx
    bne @clear_ram

    lda #$FF
    ldx #$00
@clear_oam:
    sta $0200, x
    inx
    bne @clear_oam

@vblank_wait_2:
    bit PPUSTATUS
    bpl @vblank_wait_2

    jsr init_apu
    jsr load_palettes
    jsr fill_attributes

    ; Start at title screen
    lda #STATE_TITLE
    sta game_state
    lda #0
    sta screen_drawn

    lda #%10000000
    sta PPUCTRL
    lda #%00011110
    sta PPUMASK

    lda #$00
    sta PPUSCROLL
    sta PPUSCROLL

main_loop:
    lda #$00
    sta nmi_ready
@wait_for_nmi:
    lda nmi_ready
    beq @wait_for_nmi

    ; State machine
    lda game_state
    cmp #STATE_TITLE
    beq title_state
    cmp #STATE_PLAYING
    beq playing_state
    jmp gameover_state

title_state:
    lda screen_drawn
    bne @check_start
    jsr draw_title_screen
    lda #1
    sta screen_drawn

@check_start:
    jsr read_controller
    lda buttons
    and #BTN_START
    beq @done_title

    ; Transition to playing
    jsr start_game
    lda #STATE_PLAYING
    sta game_state
    lda #0
    sta screen_drawn

@done_title:
    jmp main_loop

playing_state:
    lda screen_drawn
    bne @normal_play
    jsr draw_playfield
    lda #1
    sta screen_drawn

@normal_play:
    lda invuln_timer
    beq @no_invuln
    dec invuln_timer
@no_invuln:

    jsr read_controller
    jsr update_player
    jsr move_enemies
    jsr update_enemy_sprites
    jsr update_item_sprite
    jsr check_enemy_collision
    jsr check_item_collision
    jsr update_sound

    ; Check for game over
    lda game_state
    cmp #STATE_GAMEOVER
    beq @transition_gameover
    jmp main_loop

@transition_gameover:
    lda #0
    sta screen_drawn
    jmp main_loop

gameover_state:
    lda screen_drawn
    bne @check_restart
    jsr draw_gameover_screen
    lda #1
    sta screen_drawn

@check_restart:
    jsr read_controller
    lda buttons
    and #BTN_START
    beq @done_gameover

    ; Transition to playing
    jsr start_game
    lda #STATE_PLAYING
    sta game_state
    lda #0
    sta screen_drawn

@done_gameover:
    jmp main_loop
.endproc

;==============================================================
; DRAW TITLE SCREEN
;==============================================================

.proc draw_title_screen
    ; Hide all sprites
    ldx #0
    lda #$FF
@hide_sprites:
    sta $0200, x
    inx
    bne @hide_sprites

    ; Clear nametable first
    jsr clear_nametable

    ; Draw "NEON" at row 10, centered
    bit PPUSTATUS
    lda #$21
    sta PPUADDR
    lda #$4E                ; Row 10, column 14
    sta PPUADDR

    lda #TILE_N
    sta PPUDATA
    lda #TILE_E
    sta PPUDATA
    lda #TILE_O
    sta PPUDATA
    lda #TILE_N
    sta PPUDATA

    ; Draw "NEXUS" at row 12, centered
    bit PPUSTATUS
    lda #$21
    sta PPUADDR
    lda #$8D                ; Row 12, column 13
    sta PPUADDR

    lda #TILE_N
    sta PPUDATA
    lda #TILE_E
    sta PPUDATA
    lda #TILE_X
    sta PPUDATA
    lda #TILE_U
    sta PPUDATA
    lda #TILE_S
    sta PPUDATA

    ; Draw "PRESS START" at row 18
    bit PPUSTATUS
    lda #$22
    sta PPUADDR
    lda #$49                ; Row 18, column 9 (dummy + text)
    sta PPUADDR

    lda #0                  ; Dummy write for PPU timing
    sta PPUDATA
    lda #TILE_P
    sta PPUDATA
    lda #TILE_R
    sta PPUDATA
    lda #TILE_E
    sta PPUDATA
    lda #TILE_S
    sta PPUDATA
    lda #TILE_S
    sta PPUDATA
    lda #0                  ; Space
    sta PPUDATA
    lda #TILE_S
    sta PPUDATA
    lda #TILE_T
    sta PPUDATA
    lda #TILE_A
    sta PPUDATA
    lda #TILE_R
    sta PPUDATA
    lda #TILE_T
    sta PPUDATA

    lda #$00
    sta PPUSCROLL
    sta PPUSCROLL

    rts
.endproc

;==============================================================
; DRAW GAME OVER SCREEN
;==============================================================

.proc draw_gameover_screen
    ; Hide all sprites
    ldx #0
    lda #$FF
@hide_sprites:
    sta $0200, x
    inx
    bne @hide_sprites

    ; Clear nametable
    jsr clear_nametable

    ; Draw "GAME" at row 10
    bit PPUSTATUS
    lda #$21
    sta PPUADDR
    lda #$4E                ; Row 10, column 14
    sta PPUADDR

    lda #TILE_G
    sta PPUDATA
    lda #TILE_A
    sta PPUDATA
    lda #TILE_M
    sta PPUDATA
    lda #TILE_E
    sta PPUDATA

    ; Draw "OVER" at row 12
    lda #$21
    sta PPUADDR
    lda #$8E                ; Row 12, column 14
    sta PPUADDR

    lda #TILE_O
    sta PPUDATA
    lda #TILE_V
    sta PPUDATA
    lda #TILE_E
    sta PPUDATA
    lda #TILE_R
    sta PPUDATA

    ; Draw "SCORE" at row 16
    lda #$22
    sta PPUADDR
    lda #$0C                ; Row 16, column 12
    sta PPUADDR

    lda #TILE_S
    sta PPUDATA
    lda #TILE_C
    sta PPUDATA
    lda #TILE_O
    sta PPUDATA
    lda #TILE_R
    sta PPUDATA
    lda #TILE_E
    sta PPUDATA
    lda #0                  ; Space
    sta PPUDATA

    ; Draw score digits
    lda score

    ldx #0
@hundreds:
    cmp #100
    bcc @tens_setup
    sec
    sbc #100
    inx
    jmp @hundreds
@tens_setup:
    pha
    txa
    clc
    adc #TILE_DIGIT_0
    sta PPUDATA
    pla

    ldx #0
@tens:
    cmp #10
    bcc @ones_setup
    sec
    sbc #10
    inx
    jmp @tens
@ones_setup:
    pha
    txa
    clc
    adc #TILE_DIGIT_0
    sta PPUDATA
    pla

    clc
    adc #TILE_DIGIT_0
    sta PPUDATA

    lda #$00
    sta PPUSCROLL
    sta PPUSCROLL

    rts
.endproc

;==============================================================
; CLEAR NAMETABLE
;==============================================================

.proc clear_nametable
    bit PPUSTATUS
    lda #$20
    sta PPUADDR
    lda #$00
    sta PPUADDR

    lda #0
    ldx #0
    ldy #4                  ; 4 * 256 = 1024 bytes
@outer:
@inner:
    sta PPUDATA
    inx
    bne @inner
    dey
    bne @outer

    rts
.endproc

;==============================================================
; DRAW PLAYFIELD
;==============================================================

.proc draw_playfield
    jsr fill_nametable
    jsr draw_hud_labels
    rts
.endproc

;==============================================================
; START GAME
;==============================================================

.proc start_game
    lda #116
    sta player_y
    lda #124
    sta player_x

    jsr init_enemies

    lda #180
    sta item_x
    lda #100
    sta item_y

    lda #0
    sta score
    sta invuln_timer
    sta sfx_timer
    sta sfx_type
    lda #1
    sta score_dirty
    sta lives_dirty
    lda #STARTING_LIVES
    sta lives

    rts
.endproc

;==============================================================
; APU INITIALISATION
;==============================================================

.proc init_apu
    lda #%00000001
    sta APU_STATUS
    lda #%00110000
    sta APU_PULSE1_CTRL
    lda #$00
    sta APU_PULSE1_SWEEP
    sta APU_PULSE1_LO
    sta APU_PULSE1_HI
    rts
.endproc

;==============================================================
; PLAY COLLECT SOUND
;==============================================================

.proc play_collect_sound
    lda #SFX_COLLECT
    sta sfx_type
    lda #16
    sta sfx_timer
    lda #%10111111
    sta APU_PULSE1_CTRL
    lda #$C0
    sta APU_PULSE1_LO
    lda #%00001000
    sta APU_PULSE1_HI
    rts
.endproc

;==============================================================
; PLAY HIT SOUND
;==============================================================

.proc play_hit_sound
    lda #SFX_HIT
    sta sfx_type
    lda #20
    sta sfx_timer
    lda #%11111111
    sta APU_PULSE1_CTRL
    lda #$40
    sta APU_PULSE1_LO
    lda #%00001000
    sta APU_PULSE1_HI
    rts
.endproc

;==============================================================
; UPDATE SOUND
;==============================================================

.proc update_sound
    lda sfx_timer
    beq @done

    dec sfx_timer
    beq @silence

    lda sfx_type
    cmp #SFX_COLLECT
    beq @update_collect
    cmp #SFX_HIT
    beq @update_hit
    rts

@update_collect:
    lda sfx_timer
    and #%00000011
    bne @done
    lda APU_PULSE1_LO
    sec
    sbc #$20
    sta APU_PULSE1_LO
    rts

@update_hit:
    lda sfx_timer
    and #%00000011
    bne @done
    lda APU_PULSE1_LO
    clc
    adc #$30
    sta APU_PULSE1_LO
    rts

@silence:
    lda #%00110000
    sta APU_PULSE1_CTRL
    lda #SFX_NONE
    sta sfx_type

@done:
    rts
.endproc

;==============================================================
; DRAW HUD LABELS
;==============================================================

.proc draw_hud_labels
    bit PPUSTATUS
    lda #$20
    sta PPUADDR
    lda #$02
    sta PPUADDR
    lda #TILE_S
    sta PPUDATA
    lda #TILE_C
    sta PPUDATA
    lda #TILE_O
    sta PPUDATA
    lda #TILE_R
    sta PPUDATA
    lda #TILE_E
    sta PPUDATA

    lda #$20
    sta PPUADDR
    lda #$18
    sta PPUADDR
    lda #TILE_L
    sta PPUDATA
    lda #TILE_I
    sta PPUDATA
    lda #TILE_V
    sta PPUDATA
    lda #TILE_E
    sta PPUDATA
    lda #TILE_S
    sta PPUDATA

    rts
.endproc

;==============================================================
; UPDATE SCORE DISPLAY
;==============================================================

.proc update_score_display
    lda score_dirty
    beq @done

    bit PPUSTATUS
    lda #$20
    sta PPUADDR
    lda #$08
    sta PPUADDR

    lda score

    ldx #0
@hundreds:
    cmp #100
    bcc @tens_setup
    sec
    sbc #100
    inx
    jmp @hundreds
@tens_setup:
    pha
    txa
    clc
    adc #TILE_DIGIT_0
    sta PPUDATA
    pla

    ldx #0
@tens:
    cmp #10
    bcc @ones_setup
    sec
    sbc #10
    inx
    jmp @tens
@ones_setup:
    pha
    txa
    clc
    adc #TILE_DIGIT_0
    sta PPUDATA
    pla

    clc
    adc #TILE_DIGIT_0
    sta PPUDATA

    lda #0
    sta score_dirty

@done:
    rts
.endproc

;==============================================================
; UPDATE LIVES DISPLAY
;==============================================================

.proc update_lives_display
    lda lives_dirty
    beq @done

    bit PPUSTATUS
    lda #$20
    sta PPUADDR
    lda #$1E
    sta PPUADDR

    lda lives
    clc
    adc #TILE_DIGIT_0
    sta PPUDATA

    lda #0
    sta lives_dirty

@done:
    rts
.endproc

;==============================================================
; INITIALISE ENEMIES
;==============================================================

.proc init_enemies
    lda #32
    sta enemy_x
    lda #48
    sta enemy_y
    lda #1
    sta enemy_dir_x
    lda #1
    sta enemy_dir_y

    lda #200
    sta enemy_x + 1
    lda #64
    sta enemy_y + 1
    lda #0
    sta enemy_dir_x + 1
    lda #1
    sta enemy_dir_y + 1

    lda #48
    sta enemy_x + 2
    lda #140
    sta enemy_y + 2
    lda #1
    sta enemy_dir_x + 2
    lda #2
    sta enemy_dir_y + 2

    lda #180
    sta enemy_x + 3
    lda #180
    sta enemy_y + 3
    lda #2
    sta enemy_dir_x + 3
    lda #0
    sta enemy_dir_y + 3

    rts
.endproc

;==============================================================
; MOVE ENEMIES
;==============================================================

.proc move_enemies
    ldx #0

@loop:
    lda enemy_dir_x, x
    cmp #2
    beq @vertical_only

    lda enemy_dir_y, x
    cmp #2
    beq @horizontal_only

    jsr move_enemy_x
    jsr move_enemy_y
    jmp @next

@horizontal_only:
    jsr move_enemy_x
    jmp @next

@vertical_only:
    jsr move_enemy_y

@next:
    inx
    cpx #NUM_ENEMIES
    bne @loop

    rts
.endproc

.proc move_enemy_x
    lda enemy_dir_x, x
    beq @move_left

    inc enemy_x, x
    lda enemy_x, x
    cmp #232
    bcc @done
    lda #0
    sta enemy_dir_x, x
    jmp @done

@move_left:
    dec enemy_x, x
    lda enemy_x, x
    cmp #9
    bcs @done
    lda #1
    sta enemy_dir_x, x

@done:
    rts
.endproc

.proc move_enemy_y
    lda enemy_dir_y, x
    beq @move_up

    inc enemy_y, x
    lda enemy_y, x
    cmp #216
    bcc @done
    lda #0
    sta enemy_dir_y, x
    jmp @done

@move_up:
    dec enemy_y, x
    lda enemy_y, x
    cmp #25
    bcs @done
    lda #1
    sta enemy_dir_y, x

@done:
    rts
.endproc

;==============================================================
; CHECK ENEMY COLLISION
;==============================================================

.proc check_enemy_collision
    lda invuln_timer
    bne @no_collision

    ldx #0

@loop:
    lda player_x
    sec
    sbc enemy_x, x
    bcs @x_pos
    eor #$FF
    clc
    adc #1
@x_pos:
    cmp #HITBOX_SIZE
    bcs @next

    lda player_y
    sec
    sbc enemy_y, x
    bcs @y_pos
    eor #$FF
    clc
    adc #1
@y_pos:
    cmp #HITBOX_SIZE
    bcs @next

    jsr lose_life
    rts

@next:
    inx
    cpx #NUM_ENEMIES
    bne @loop

@no_collision:
    rts
.endproc

;==============================================================
; LOSE LIFE
;==============================================================

.proc lose_life
    dec lives
    lda #1
    sta lives_dirty

    jsr play_hit_sound

    lda lives
    beq @game_over

    lda #INVULN_FRAMES
    sta invuln_timer
    rts

@game_over:
    lda #STATE_GAMEOVER
    sta game_state
    rts
.endproc

;==============================================================
; CHECK ITEM COLLISION
;==============================================================

.proc check_item_collision
    lda player_x
    sec
    sbc item_x
    bcs @x_pos
    eor #$FF
    clc
    adc #1
@x_pos:
    cmp #ITEM_HITBOX
    bcs @no_collision

    lda player_y
    sec
    sbc item_y
    bcs @y_pos
    eor #$FF
    clc
    adc #1
@y_pos:
    cmp #ITEM_HITBOX
    bcs @no_collision

    jsr collect_item

@no_collision:
    rts
.endproc

;==============================================================
; COLLECT ITEM
;==============================================================

.proc collect_item
    lda score
    cmp #255
    beq @skip_inc
    inc score
@skip_inc:

    lda #1
    sta score_dirty

    jsr play_collect_sound

    lda frame_counter
    asl a
    asl a
    clc
    adc #32
    cmp #224
    bcc @x_ok
    lda #180
@x_ok:
    sta item_x

    lda frame_counter
    eor score
    and #%01111111
    clc
    adc #48
    sta item_y

    rts
.endproc

;==============================================================
; UPDATE ITEM SPRITE
;==============================================================

.proc update_item_sprite
    lda item_y
    sta $0200 + 20
    lda #4
    sta $0200 + 21
    lda #%00000010
    sta $0200 + 22
    lda item_x
    sta $0200 + 23
    rts
.endproc

;==============================================================
; UPDATE PLAYER SPRITE
;==============================================================

.proc update_player_sprite
    lda invuln_timer
    beq @visible

    and #%00000100
    beq @hidden

@visible:
    lda player_y
    sta $0200
    lda #1
    sta $0201
    lda #%00000000
    sta $0202
    lda player_x
    sta $0203
    rts

@hidden:
    lda #$FF
    sta $0200
    rts
.endproc

;==============================================================
; UPDATE ENEMY SPRITES
;==============================================================

.proc update_enemy_sprites
    ldx #0
    ldy #4

@loop:
    lda enemy_y, x
    sta $0200, y
    iny

    lda #2
    sta $0200, y
    iny

    lda #%00000001
    sta $0200, y
    iny

    lda enemy_x, x
    sta $0200, y
    iny

    inx
    cpx #NUM_ENEMIES
    bne @loop

    rts
.endproc

;==============================================================
; READ CONTROLLER
;==============================================================

.proc read_controller
    lda #$01
    sta JOYPAD1
    lda #$00
    sta JOYPAD1

    ldx #8
@loop:
    lda JOYPAD1
    lsr a
    rol buttons
    dex
    bne @loop

    rts
.endproc

;==============================================================
; UPDATE PLAYER
;==============================================================

.proc update_player
    lda buttons
    and #BTN_UP
    beq @check_down
    lda player_y
    cmp #24
    bcc @check_down
    dec player_y

@check_down:
    lda buttons
    and #BTN_DOWN
    beq @check_left
    lda player_y
    cmp #223
    bcs @check_left
    inc player_y

@check_left:
    lda buttons
    and #BTN_LEFT
    beq @check_right
    lda player_x
    cmp #9
    bcc @check_right
    dec player_x

@check_right:
    lda buttons
    and #BTN_RIGHT
    beq @done
    lda player_x
    cmp #239
    bcs @done
    inc player_x

@done:
    jsr update_player_sprite
    rts
.endproc

;==============================================================
; LOAD PALETTES
;==============================================================

.proc load_palettes
    bit PPUSTATUS
    lda #$3F
    sta PPUADDR
    lda #$00
    sta PPUADDR
    ldx #$00
@loop:
    lda palette_data, x
    sta PPUDATA
    inx
    cpx #32
    bne @loop
    rts
.endproc

;==============================================================
; FILL NAMETABLE
;==============================================================

.proc fill_nametable
    bit PPUSTATUS
    lda #$20
    sta PPUADDR
    lda #$00
    sta PPUADDR

    ldx #32
@top:
    lda #0
    sta PPUDATA
    dex
    bne @top

    ldx #32
@border_top:
    lda #3
    sta PPUDATA
    dex
    bne @border_top

    ldy #26
@middle:
    lda #3
    sta PPUDATA
    ldx #30
@empty:
    lda #0
    sta PPUDATA
    dex
    bne @empty
    lda #3
    sta PPUDATA
    dey
    bne @middle

    ldx #32
@bottom:
    lda #3
    sta PPUDATA
    dex
    bne @bottom

    rts
.endproc

;==============================================================
; FILL ATTRIBUTES
;==============================================================

.proc fill_attributes
    bit PPUSTATUS
    lda #$23
    sta PPUADDR
    lda #$C0
    sta PPUADDR
    lda #$00
    ldx #64
@loop:
    sta PPUDATA
    dex
    bne @loop
    rts
.endproc

;==============================================================
; NMI HANDLER
;==============================================================

.proc nmi
    pha
    txa
    pha
    tya
    pha

    inc frame_counter

    lda #$00
    sta OAMADDR
    lda #$02
    sta OAMDMA

    ; Only update HUD during gameplay
    lda game_state
    cmp #STATE_PLAYING
    bne @skip_hud
    jsr update_score_display
    jsr update_lives_display
@skip_hud:

    lda #$00
    sta PPUSCROLL
    sta PPUSCROLL

    lda #$01
    sta nmi_ready

    pla
    tay
    pla
    tax
    pla
    rti
.endproc

;==============================================================
; IRQ HANDLER
;==============================================================

.proc irq
    rti
.endproc

;==============================================================
; DATA
;==============================================================

palette_data:
    .byte $0F, $30, $10, $00
    .byte $0F, $19, $29, $39
    .byte $0F, $15, $25, $35
    .byte $0F, $00, $10, $30
    .byte $0F, $30, $21, $11
    .byte $0F, $16, $26, $36
    .byte $0F, $2A, $1A, $0A
    .byte $0F, $27, $17, $07

;==============================================================
; VECTORS
;==============================================================

.segment "VECTORS"
    .word nmi
    .word reset
    .word irq

;==============================================================
; CHR-ROM
;==============================================================

.segment "CHARS"

; Tile 0: Empty
    .byte $00, $00, $00, $00, $00, $00, $00, $00
    .byte $00, $00, $00, $00, $00, $00, $00, $00

; Tile 1: Player ship
    .byte %00011000, %00111100, %01111110, %11111111
    .byte %11111111, %00100100, %00100100, %01100110
    .byte $00, $00, $00, $00, $00, $00, $00, $00

; Tile 2: Enemy
    .byte %01100110, %11111111, %11011011, %11111111
    .byte %01111110, %00100100, %01000010, %10000001
    .byte $00, $00, $00, $00, $00, $00, $00, $00

; Tile 3: Solid block
    .byte $FF, $FF, $FF, $FF, $FF, $FF, $FF, $FF
    .byte $00, $00, $00, $00, $00, $00, $00, $00

; Tile 4: Item
    .byte %00011000, %00111100, %01111110, %11111111
    .byte %11111111, %01111110, %00111100, %00011000
    .byte $00, $00, $00, $00, $00, $00, $00, $00

; Tiles 5-14: Digits 0-9
    .byte %00111100, %01100110, %01101110, %01110110, %01100110, %01100110, %00111100, %00000000
    .byte $00, $00, $00, $00, $00, $00, $00, $00
    .byte %00011000, %00111000, %00011000, %00011000, %00011000, %00011000, %01111110, %00000000
    .byte $00, $00, $00, $00, $00, $00, $00, $00
    .byte %00111100, %01100110, %00000110, %00011100, %00110000, %01100000, %01111110, %00000000
    .byte $00, $00, $00, $00, $00, $00, $00, $00
    .byte %00111100, %01100110, %00000110, %00011100, %00000110, %01100110, %00111100, %00000000
    .byte $00, $00, $00, $00, $00, $00, $00, $00
    .byte %00001110, %00011110, %00110110, %01100110, %01111111, %00000110, %00000110, %00000000
    .byte $00, $00, $00, $00, $00, $00, $00, $00
    .byte %01111110, %01100000, %01111100, %00000110, %00000110, %01100110, %00111100, %00000000
    .byte $00, $00, $00, $00, $00, $00, $00, $00
    .byte %00011100, %00110000, %01100000, %01111100, %01100110, %01100110, %00111100, %00000000
    .byte $00, $00, $00, $00, $00, $00, $00, $00
    .byte %01111110, %00000110, %00001100, %00011000, %00110000, %00110000, %00110000, %00000000
    .byte $00, $00, $00, $00, $00, $00, $00, $00
    .byte %00111100, %01100110, %01100110, %00111100, %01100110, %01100110, %00111100, %00000000
    .byte $00, $00, $00, $00, $00, $00, $00, $00
    .byte %00111100, %01100110, %01100110, %00111110, %00000110, %00001100, %00111000, %00000000
    .byte $00, $00, $00, $00, $00, $00, $00, $00

; Tiles 15-19: Reserved
    .res 80

; Tiles 20-27: S, C, O, R, E, L, I, V
    .byte %00111100, %01100110, %01100000, %00111100, %00000110, %01100110, %00111100, %00000000
    .byte $00, $00, $00, $00, $00, $00, $00, $00
    .byte %00111100, %01100110, %01100000, %01100000, %01100000, %01100110, %00111100, %00000000
    .byte $00, $00, $00, $00, $00, $00, $00, $00
    .byte %00111100, %01100110, %01100110, %01100110, %01100110, %01100110, %00111100, %00000000
    .byte $00, $00, $00, $00, $00, $00, $00, $00
    .byte %01111100, %01100110, %01100110, %01111100, %01101100, %01100110, %01100110, %00000000
    .byte $00, $00, $00, $00, $00, $00, $00, $00
    .byte %01111110, %01100000, %01100000, %01111100, %01100000, %01100000, %01111110, %00000000
    .byte $00, $00, $00, $00, $00, $00, $00, $00
    .byte %01100000, %01100000, %01100000, %01100000, %01100000, %01100000, %01111110, %00000000
    .byte $00, $00, $00, $00, $00, $00, $00, $00
    .byte %01111110, %00011000, %00011000, %00011000, %00011000, %00011000, %01111110, %00000000
    .byte $00, $00, $00, $00, $00, $00, $00, $00
    .byte %01100110, %01100110, %01100110, %01100110, %01100110, %00111100, %00011000, %00000000
    .byte $00, $00, $00, $00, $00, $00, $00, $00

; Tiles 28-35: N, X, P, T, A, G, M, U (for title/game over)
    .byte %01100110, %01110110, %01111110, %01111110, %01101110, %01100110, %01100110, %00000000
    .byte $00, $00, $00, $00, $00, $00, $00, $00
    .byte %01100110, %01100110, %00111100, %00011000, %00111100, %01100110, %01100110, %00000000
    .byte $00, $00, $00, $00, $00, $00, $00, $00
; Tile 30: P
    .byte %01111100, %01100110, %01100110, %01111100, %01100000, %01100000, %01100000, %00000000
    .byte $00, $00, $00, $00, $00, $00, $00, $00
    .byte %01111110, %00011000, %00011000, %00011000, %00011000, %00011000, %00011000, %00000000
    .byte $00, $00, $00, $00, $00, $00, $00, $00
    .byte %00011000, %00111100, %01100110, %01100110, %01111110, %01100110, %01100110, %00000000
    .byte $00, $00, $00, $00, $00, $00, $00, $00
    .byte %00111100, %01100110, %01100000, %01101110, %01100110, %01100110, %00111100, %00000000
    .byte $00, $00, $00, $00, $00, $00, $00, $00
    .byte %01100011, %01110111, %01111111, %01101011, %01100011, %01100011, %01100011, %00000000
    .byte $00, $00, $00, $00, $00, $00, $00, $00
; Tile 35: U
    .byte %01100110, %01100110, %01100110, %01100110, %01100110, %01100110, %00111100, %00000000
    .byte $00, $00, $00, $00, $00, $00, $00, $00

; Fill rest
    .res 8192 - 576
