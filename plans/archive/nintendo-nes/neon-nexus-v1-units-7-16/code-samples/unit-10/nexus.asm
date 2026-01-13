;──────────────────────────────────────────────────────────────
; NEON NEXUS
; A fixed-screen action game for the Nintendo Entertainment System
; Unit 10: Collectibles
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
item_x:         .res 1      ; Collectible X position
item_y:         .res 1      ; Collectible Y position
score:          .res 1      ; Player score (0-255)
game_over:      .res 1

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
ITEM_HITBOX = 8             ; Slightly larger for items

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
    lda #60
    sta item_y

    ; Initialise score
    lda #0
    sta score
    sta game_over

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
; CHECK ITEM COLLISION
;==============================================================
; Test if player overlaps the collectible item.

.proc check_item_collision
    ; Check X distance
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

    ; Check Y distance
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

    ; Collision! Collect the item
    jsr collect_item

@no_collision:
    rts
.endproc

;==============================================================
; COLLECT ITEM
;==============================================================
; Add to score and respawn the item.

.proc collect_item
    ; Increment score
    inc score

    ; Respawn item at new position
    ; Simple pseudo-random: use frame counter
    lda frame_counter
    asl a
    asl a
    clc
    adc #32                 ; Range 32-224
    cmp #224
    bcc @x_ok
    lda #180                ; Fallback
@x_ok:
    sta item_x

    lda frame_counter
    eor score               ; Mix in score for variation
    and #%01111111          ; 0-127
    clc
    adc #32                 ; Range 32-159
    sta item_y

    rts
.endproc

;==============================================================
; UPDATE ITEM SPRITE
;==============================================================

.proc update_item_sprite
    lda item_y
    sta $0200 + 20          ; Sprite 5 (after player and 4 enemies)
    lda #4                  ; Item tile
    sta $0200 + 21
    lda #%00000010          ; Palette 2
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
    lda #60
    sta item_y

    lda #0
    sta score
    sta game_over

    rts
.endproc

;==============================================================
; INITIALISE ENEMIES
;==============================================================

.proc init_enemies
    lda #32
    sta enemy_x
    lda #32
    sta enemy_y

    lda #216
    sta enemy_x + 1
    lda #48
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
    lda #9
    sta enemy_y

@check_1:
    lda enemy_y + 1
    cmp #224
    bcc @check_2
    lda #9
    sta enemy_y + 1

@check_2:
    lda enemy_y + 2
    cmp #8
    bcs @check_3
    lda #223
    sta enemy_y + 2

@check_3:
    lda enemy_y + 3
    cmp #8
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
    cmp #9
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

    ldx #32
@top:
    lda #3
    sta PPUDATA
    dex
    bne @top

    ldy #28
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
    .byte $0F, $11, $21, $31
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

; Tile 4: Item (diamond shape)
    .byte %00011000
    .byte %00111100
    .byte %01111110
    .byte %11111111
    .byte %11111111
    .byte %01111110
    .byte %00111100
    .byte %00011000
    .byte $00, $00, $00, $00, $00, $00, $00, $00

; Fill rest
    .res 8192 - 80
