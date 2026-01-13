;──────────────────────────────────────────────────────────────
; NEON NEXUS
; A fixed-screen action game for the Nintendo Entertainment System
; Unit 11: Score Display
;──────────────────────────────────────────────────────────────

;==============================================================
; iNES HEADER
;==============================================================

.segment "HEADER"
    .byte "NES", $1A
    .byte 2                 ; PRG-ROM: 32KB
    .byte 1                 ; CHR-ROM: 8KB
    .byte $01               ; Mapper 0, vertical mirroring
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
item_x:         .res 1
item_y:         .res 1
score:          .res 1      ; Player score (0-255)
game_over:      .res 1
score_dirty:    .res 1      ; Flag: score needs redraw

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

; Tile indices for digits 0-9
TILE_DIGIT_0 = 5

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
    jsr draw_score_label

    ; Initialise player
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

    ; Initialise item
    lda #180
    sta item_x
    lda #100
    sta item_y

    ; Initialise score
    lda #0
    sta score
    sta game_over
    lda #1
    sta score_dirty         ; Draw initial score

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
; DRAW SCORE LABEL
;==============================================================
; Write "SCORE" text to nametable at startup.

.proc draw_score_label
    bit PPUSTATUS
    lda #$20                ; Nametable $2000
    sta PPUADDR
    lda #$22                ; Row 1, column 2
    sta PPUADDR

    ; Write "SCORE:" using tiles 15-19
    lda #15                 ; S
    sta PPUDATA
    lda #16                 ; C
    sta PPUDATA
    lda #17                 ; O
    sta PPUDATA
    lda #18                 ; R
    sta PPUDATA
    lda #19                 ; E
    sta PPUDATA

    rts
.endproc

;==============================================================
; UPDATE SCORE DISPLAY
;==============================================================
; Called during NMI when score_dirty is set.
; Writes 3-digit score to nametable.

.proc update_score_display
    lda score_dirty
    beq @done

    bit PPUSTATUS
    lda #$20                ; Nametable $2000
    sta PPUADDR
    lda #$28                ; Row 1, column 8 (after "SCORE:")
    sta PPUADDR

    ; Convert score to 3 digits
    lda score

    ; Hundreds digit
    ldx #0
@hundreds:
    cmp #100
    bcc @tens_setup
    sec
    sbc #100
    inx
    jmp @hundreds
@tens_setup:
    pha                     ; Save remainder
    txa
    clc
    adc #TILE_DIGIT_0       ; Convert to tile
    sta PPUDATA

    pla                     ; Restore remainder

    ; Tens digit
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

    ; Ones digit
    clc
    adc #TILE_DIGIT_0
    sta PPUDATA

    lda #0
    sta score_dirty

@done:
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
    ; Increment score (cap at 255)
    lda score
    cmp #255
    beq @skip_inc
    inc score
@skip_inc:

    ; Mark score for redraw
    lda #1
    sta score_dirty

    ; Respawn item
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
    adc #48                 ; Keep below score area
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
; CHECK ENEMY COLLISION
;==============================================================

.proc check_enemy_collision
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

    lda #1
    sta game_over
    rts

@next:
    inx
    cpx #NUM_ENEMIES
    bne @loop

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

    lda player_y
    sta $0200
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
    lda #1
    sta score_dirty

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

    lda #216
    sta enemy_x + 1
    lda #64
    sta enemy_y + 1

    lda #48
    sta enemy_x + 2
    lda #200
    sta enemy_y + 2

    lda #200
    sta enemy_x + 3
    lda #184
    sta enemy_y + 3

    rts
.endproc

;==============================================================
; MOVE ENEMIES
;==============================================================

.proc move_enemies
    inc enemy_y
    inc enemy_y + 1
    dec enemy_y + 2
    dec enemy_y + 3

    lda enemy_y
    cmp #224
    bcc @check_1
    lda #24
    sta enemy_y

@check_1:
    lda enemy_y + 1
    cmp #224
    bcc @check_2
    lda #24
    sta enemy_y + 1

@check_2:
    lda enemy_y + 2
    cmp #24
    bcs @check_3
    lda #223
    sta enemy_y + 2

@check_3:
    lda enemy_y + 3
    cmp #24
    bcs @done
    lda #223
    sta enemy_y + 3

@done:
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
    cmp #24                 ; Keep below HUD
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
    lda player_y
    sta $0200
    lda player_x
    sta $0203
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

    ; Top row (HUD area)
    ldx #32
@top:
    lda #0                  ; Empty for HUD
    sta PPUDATA
    dex
    bne @top

    ; Second row (border)
    ldx #32
@border_top:
    lda #3
    sta PPUDATA
    dex
    bne @border_top

    ; Middle rows (play area)
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

    ; Bottom row
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

    ; Update score display during VBlank
    jsr update_score_display

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
    ; Background palettes
    .byte $0F, $30, $10, $00    ; Palette 0: white text on black
    .byte $0F, $19, $29, $39
    .byte $0F, $15, $25, $35
    .byte $0F, $00, $10, $30

    ; Sprite palettes
    .byte $0F, $30, $21, $11    ; Palette 0: white/blue (player)
    .byte $0F, $16, $26, $36    ; Palette 1: red (enemies)
    .byte $0F, $2A, $1A, $0A    ; Palette 2: green (items)
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
    .byte %00011000
    .byte %00111100
    .byte %01111110
    .byte %11111111
    .byte %11111111
    .byte %00100100
    .byte %00100100
    .byte %01100110
    .byte $00, $00, $00, $00, $00, $00, $00, $00

; Tile 2: Enemy
    .byte %01100110
    .byte %11111111
    .byte %11011011
    .byte %11111111
    .byte %01111110
    .byte %00100100
    .byte %01000010
    .byte %10000001
    .byte $00, $00, $00, $00, $00, $00, $00, $00

; Tile 3: Solid block (border)
    .byte $FF, $FF, $FF, $FF, $FF, $FF, $FF, $FF
    .byte $00, $00, $00, $00, $00, $00, $00, $00

; Tile 4: Item (diamond)
    .byte %00011000
    .byte %00111100
    .byte %01111110
    .byte %11111111
    .byte %11111111
    .byte %01111110
    .byte %00111100
    .byte %00011000
    .byte $00, $00, $00, $00, $00, $00, $00, $00

; Tiles 5-14: Digits 0-9
; Tile 5: Digit 0
    .byte %00111100
    .byte %01100110
    .byte %01101110
    .byte %01110110
    .byte %01100110
    .byte %01100110
    .byte %00111100
    .byte %00000000
    .byte $00, $00, $00, $00, $00, $00, $00, $00

; Tile 6: Digit 1
    .byte %00011000
    .byte %00111000
    .byte %00011000
    .byte %00011000
    .byte %00011000
    .byte %00011000
    .byte %01111110
    .byte %00000000
    .byte $00, $00, $00, $00, $00, $00, $00, $00

; Tile 7: Digit 2
    .byte %00111100
    .byte %01100110
    .byte %00000110
    .byte %00011100
    .byte %00110000
    .byte %01100000
    .byte %01111110
    .byte %00000000
    .byte $00, $00, $00, $00, $00, $00, $00, $00

; Tile 8: Digit 3
    .byte %00111100
    .byte %01100110
    .byte %00000110
    .byte %00011100
    .byte %00000110
    .byte %01100110
    .byte %00111100
    .byte %00000000
    .byte $00, $00, $00, $00, $00, $00, $00, $00

; Tile 9: Digit 4
    .byte %00001110
    .byte %00011110
    .byte %00110110
    .byte %01100110
    .byte %01111111
    .byte %00000110
    .byte %00000110
    .byte %00000000
    .byte $00, $00, $00, $00, $00, $00, $00, $00

; Tile 10: Digit 5
    .byte %01111110
    .byte %01100000
    .byte %01111100
    .byte %00000110
    .byte %00000110
    .byte %01100110
    .byte %00111100
    .byte %00000000
    .byte $00, $00, $00, $00, $00, $00, $00, $00

; Tile 11: Digit 6
    .byte %00011100
    .byte %00110000
    .byte %01100000
    .byte %01111100
    .byte %01100110
    .byte %01100110
    .byte %00111100
    .byte %00000000
    .byte $00, $00, $00, $00, $00, $00, $00, $00

; Tile 12: Digit 7
    .byte %01111110
    .byte %00000110
    .byte %00001100
    .byte %00011000
    .byte %00110000
    .byte %00110000
    .byte %00110000
    .byte %00000000
    .byte $00, $00, $00, $00, $00, $00, $00, $00

; Tile 13: Digit 8
    .byte %00111100
    .byte %01100110
    .byte %01100110
    .byte %00111100
    .byte %01100110
    .byte %01100110
    .byte %00111100
    .byte %00000000
    .byte $00, $00, $00, $00, $00, $00, $00, $00

; Tile 14: Digit 9
    .byte %00111100
    .byte %01100110
    .byte %01100110
    .byte %00111110
    .byte %00000110
    .byte %00001100
    .byte %00111000
    .byte %00000000
    .byte $00, $00, $00, $00, $00, $00, $00, $00

; Tiles 15-19: Letters S, C, O, R, E
; Tile 15: S
    .byte %00111100
    .byte %01100110
    .byte %01100000
    .byte %00111100
    .byte %00000110
    .byte %01100110
    .byte %00111100
    .byte %00000000
    .byte $00, $00, $00, $00, $00, $00, $00, $00

; Tile 16: C
    .byte %00111100
    .byte %01100110
    .byte %01100000
    .byte %01100000
    .byte %01100000
    .byte %01100110
    .byte %00111100
    .byte %00000000
    .byte $00, $00, $00, $00, $00, $00, $00, $00

; Tile 17: O
    .byte %00111100
    .byte %01100110
    .byte %01100110
    .byte %01100110
    .byte %01100110
    .byte %01100110
    .byte %00111100
    .byte %00000000
    .byte $00, $00, $00, $00, $00, $00, $00, $00

; Tile 18: R
    .byte %01111100
    .byte %01100110
    .byte %01100110
    .byte %01111100
    .byte %01101100
    .byte %01100110
    .byte %01100110
    .byte %00000000
    .byte $00, $00, $00, $00, $00, $00, $00, $00

; Tile 19: E
    .byte %01111110
    .byte %01100000
    .byte %01100000
    .byte %01111100
    .byte %01100000
    .byte %01100000
    .byte %01111110
    .byte %00000000
    .byte $00, $00, $00, $00, $00, $00, $00, $00

; Fill rest
    .res 8192 - 320
