;──────────────────────────────────────────────────────────────
; NEON NEXUS
; A fixed-screen action game for the Nintendo Entertainment System
; Unit 7: Controller Input
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
buttons:        .res 1      ; Current button state
player_x:       .res 1      ; Player X position
player_y:       .res 1      ; Player Y position

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

; Button masks
BTN_A      = %00000001
BTN_B      = %00000010
BTN_SELECT = %00000100
BTN_START  = %00001000
BTN_UP     = %00010000
BTN_DOWN   = %00100000
BTN_LEFT   = %01000000
BTN_RIGHT  = %10000000

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

    ; Load palettes
    jsr load_palettes

    ; Fill the nametable with border
    jsr fill_nametable

    ; Fill attributes
    jsr fill_attributes

    ; Initialise player position (centre screen)
    lda #116
    sta player_y
    lda #124
    sta player_x

    ; Set up player sprite
    lda player_y
    sta $0200               ; Y position
    lda #1                  ; Player tile
    sta $0201
    lda #%00000000          ; Attributes
    sta $0202
    lda player_x
    sta $0203               ; X position

    ; Enable rendering
    lda #%10000000          ; NMI enable
    sta PPUCTRL
    lda #%00011110          ; Show background and sprites
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

    ; Read controller
    jsr read_controller

    ; Update player based on input
    jsr update_player

    jmp main_loop
.endproc

;==============================================================
; READ CONTROLLER
;==============================================================
; Reads the state of controller 1 into the 'buttons' variable.
; Buttons are stored as bits: A B Sel St Up Dn L R

.proc read_controller
    ; Strobe the controller
    lda #$01
    sta JOYPAD1             ; Write 1 to begin strobe
    lda #$00
    sta JOYPAD1             ; Write 0 to latch button state

    ; Read 8 buttons
    ldx #8
@loop:
    lda JOYPAD1             ; Read button (bit 0)
    lsr a                   ; Shift into carry
    rol buttons             ; Roll carry into buttons
    dex
    bne @loop

    rts
.endproc

;==============================================================
; UPDATE PLAYER
;==============================================================
; Move player sprite based on controller input.

.proc update_player
    ; Check UP
    lda buttons
    and #BTN_UP
    beq @check_down
    lda player_y
    cmp #9                  ; Border at 8
    bcc @check_down
    dec player_y

@check_down:
    lda buttons
    and #BTN_DOWN
    beq @check_left
    lda player_y
    cmp #223                ; Bottom border
    bcs @check_left
    inc player_y

@check_left:
    lda buttons
    and #BTN_LEFT
    beq @check_right
    lda player_x
    cmp #9                  ; Border at 8
    bcc @check_right
    dec player_x

@check_right:
    lda buttons
    and #BTN_RIGHT
    beq @done
    lda player_x
    cmp #239                ; Right border
    bcs @done
    inc player_x

@done:
    ; Update sprite position
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

    ; Set PPU address to nametable 0 ($2000)
    lda #$20
    sta PPUADDR
    lda #$00
    sta PPUADDR

    ; Row 0: Top border (32 solid tiles)
    ldx #32
@top_border:
    lda #2                  ; Solid block
    sta PPUDATA
    dex
    bne @top_border

    ; Rows 1-28: Left border, empty middle, right border
    ldy #28                 ; 28 middle rows
@middle_rows:
    ; Left border tile
    lda #2
    sta PPUDATA

    ; 30 empty tiles
    ldx #30
@empty_tiles:
    lda #0                  ; Empty tile
    sta PPUDATA
    dex
    bne @empty_tiles

    ; Right border tile
    lda #2
    sta PPUDATA

    dey
    bne @middle_rows

    ; Row 29: Bottom border (32 solid tiles)
    ldx #32
@bottom_border:
    lda #2
    sta PPUDATA
    dex
    bne @bottom_border

    rts
.endproc

;==============================================================
; FILL ATTRIBUTES
;==============================================================

.proc fill_attributes
    bit PPUSTATUS

    ; Attribute table is at $23C0
    lda #$23
    sta PPUADDR
    lda #$C0
    sta PPUADDR

    ; Fill 64 bytes with palette 0
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
    .byte $0F               ; Universal background: black
    .byte $11, $21, $31     ; Palette 0: blues
    .byte $0F
    .byte $19, $29, $39     ; Palette 1: greens
    .byte $0F
    .byte $15, $25, $35     ; Palette 2: magentas
    .byte $0F
    .byte $00, $10, $30     ; Palette 3: greys

    ; Sprite palettes
    .byte $0F
    .byte $30, $21, $11     ; Palette 0: white/blue
    .byte $0F
    .byte $2A, $1A, $0A     ; Palette 1: greens
    .byte $0F
    .byte $25, $15, $05     ; Palette 2: magentas
    .byte $0F
    .byte $27, $17, $07     ; Palette 3: oranges

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

; Tile 0: Empty (transparent)
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

; Tile 2: Solid block (border)
    .byte $FF, $FF, $FF, $FF, $FF, $FF, $FF, $FF
    .byte $00, $00, $00, $00, $00, $00, $00, $00

; Fill rest
    .res 8192 - 48
