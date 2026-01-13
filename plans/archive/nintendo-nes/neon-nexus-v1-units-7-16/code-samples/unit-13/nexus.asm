;──────────────────────────────────────────────────────────────
; NEON NEXUS
; A fixed-screen action game for the Nintendo Entertainment System
; Unit 13: Enemy Patterns
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
enemy_dir_x:    .res 4      ; X direction: 0=left, 1=right
enemy_dir_y:    .res 4      ; Y direction: 0=up, 1=down
item_x:         .res 1
item_y:         .res 1
score:          .res 1
game_over:      .res 1
score_dirty:    .res 1
lives:          .res 1
lives_dirty:    .res 1
invuln_timer:   .res 1

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

    jsr load_palettes
    jsr fill_nametable
    jsr fill_attributes
    jsr draw_hud_labels

    lda #116
    sta player_y
    lda #124
    sta player_x

    lda player_y
    sta $0200
    lda #1
    sta $0201
    lda #%00000000
    sta $0202
    lda player_x
    sta $0203

    jsr init_enemies

    lda #180
    sta item_x
    lda #100
    sta item_y

    lda #0
    sta score
    sta game_over
    sta invuln_timer
    lda #1
    sta score_dirty
    sta lives_dirty
    lda #STARTING_LIVES
    sta lives

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

    lda game_over
    bne @game_over_state

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
    jmp main_loop

@game_over_state:
    jsr read_controller
    lda buttons
    and #BTN_START
    beq main_loop
    jsr restart_game
    jmp main_loop
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
    lda #20
    sta PPUDATA
    lda #21
    sta PPUDATA
    lda #22
    sta PPUDATA
    lda #23
    sta PPUDATA
    lda #24
    sta PPUDATA

    lda #$20
    sta PPUADDR
    lda #$18
    sta PPUADDR
    lda #25
    sta PPUDATA
    lda #26
    sta PPUDATA
    lda #27
    sta PPUDATA
    lda #24
    sta PPUDATA
    lda #20
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
; Each enemy has a unique movement pattern.

.proc init_enemies
    ; Enemy 0: Bounces diagonally (starts top-left, going down-right)
    lda #32
    sta enemy_x
    lda #48
    sta enemy_y
    lda #1                  ; Moving right
    sta enemy_dir_x
    lda #1                  ; Moving down
    sta enemy_dir_y

    ; Enemy 1: Bounces diagonally (starts top-right, going down-left)
    lda #200
    sta enemy_x + 1
    lda #64
    sta enemy_y + 1
    lda #0                  ; Moving left
    sta enemy_dir_x + 1
    lda #1                  ; Moving down
    sta enemy_dir_y + 1

    ; Enemy 2: Horizontal only (left-right)
    lda #48
    sta enemy_x + 2
    lda #140
    sta enemy_y + 2
    lda #1                  ; Moving right
    sta enemy_dir_x + 2
    lda #2                  ; Special: horizontal only
    sta enemy_dir_y + 2

    ; Enemy 3: Vertical only (up-down)
    lda #180
    sta enemy_x + 3
    lda #180
    sta enemy_y + 3
    lda #2                  ; Special: vertical only
    sta enemy_dir_x + 3
    lda #0                  ; Moving up
    sta enemy_dir_y + 3

    rts
.endproc

;==============================================================
; MOVE ENEMIES
;==============================================================
; Four movement patterns:
; - Enemies 0-1: Diagonal bounce
; - Enemy 2: Horizontal bounce
; - Enemy 3: Vertical bounce

.proc move_enemies
    ldx #0

@loop:
    ; Check movement type
    lda enemy_dir_x, x
    cmp #2
    beq @vertical_only

    lda enemy_dir_y, x
    cmp #2
    beq @horizontal_only

    ; Diagonal movement
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

;==============================================================
; MOVE ENEMY X
;==============================================================

.proc move_enemy_x
    lda enemy_dir_x, x
    beq @move_left

    ; Moving right
    inc enemy_x, x
    lda enemy_x, x
    cmp #232
    bcc @done
    lda #0
    sta enemy_dir_x, x      ; Reverse direction
    jmp @done

@move_left:
    dec enemy_x, x
    lda enemy_x, x
    cmp #9
    bcs @done
    lda #1
    sta enemy_dir_x, x      ; Reverse direction

@done:
    rts
.endproc

;==============================================================
; MOVE ENEMY Y
;==============================================================

.proc move_enemy_y
    lda enemy_dir_y, x
    beq @move_up

    ; Moving down
    inc enemy_y, x
    lda enemy_y, x
    cmp #216
    bcc @done
    lda #0
    sta enemy_dir_y, x      ; Reverse direction
    jmp @done

@move_up:
    dec enemy_y, x
    lda enemy_y, x
    cmp #25
    bcs @done
    lda #1
    sta enemy_dir_y, x      ; Reverse direction

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

    lda lives
    beq @game_over

    lda #INVULN_FRAMES
    sta invuln_timer
    rts

@game_over:
    lda #1
    sta game_over
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
; RESTART GAME
;==============================================================

.proc restart_game
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
    sta game_over
    sta invuln_timer
    lda #1
    sta score_dirty
    sta lives_dirty
    lda #STARTING_LIVES
    sta lives

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

    jsr update_score_display
    jsr update_lives_display

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

; Fill rest
    .res 8192 - 448
