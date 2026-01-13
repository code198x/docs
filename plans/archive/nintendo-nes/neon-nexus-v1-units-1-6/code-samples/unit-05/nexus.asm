;──────────────────────────────────────────────────────────────
; NEON NEXUS
; A fixed-screen action game for the Nintendo Entertainment System
; Unit 5: Pattern Tables
;──────────────────────────────────────────────────────────────

;==============================================================
; iNES HEADER
;==============================================================

.segment "HEADER"
    .byte "NES", $1A        ; Magic number
    .byte 2                 ; PRG-ROM: 2 × 16KB = 32KB
    .byte 1                 ; CHR-ROM: 1 × 8KB
    .byte $01               ; Flags 6: Mapper 0, vertical mirroring
    .byte $00               ; Flags 7: Mapper 0 (continued)
    .byte 0,0,0,0,0,0,0,0   ; Padding

;==============================================================
; VARIABLES
;==============================================================

.segment "ZEROPAGE"

nmi_ready:      .res 1
frame_counter:  .res 1

;==============================================================
; PPU REGISTER DEFINITIONS
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

    inx                     ; X = $00
    stx PPUCTRL
    stx PPUMASK
    stx $4010

    ; First VBlank wait
@vblank_wait_1:
    bit PPUSTATUS
    bpl @vblank_wait_1

    ; Clear RAM
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

    ; Clear shadow OAM to $FF (sprites hidden off-screen)
    lda #$FF
    ldx #$00
@clear_oam:
    sta $0200, x
    inx
    bne @clear_oam

    ; Second VBlank wait
@vblank_wait_2:
    bit PPUSTATUS
    bpl @vblank_wait_2

    ; Load palettes
    jsr load_palettes

    ;----------------------------------------------------------
    ; Set up a sprite to display our tile
    ;----------------------------------------------------------
    ; Shadow OAM at $0200-$02FF holds sprite data.
    ; Each sprite uses 4 bytes:
    ;   Byte 0: Y position (0-239)
    ;   Byte 1: Tile index (0-255)
    ;   Byte 2: Attributes (palette, flip, priority)
    ;   Byte 3: X position (0-255)

    ; Sprite 0: Display tile 1 (player ship) at centre screen
    lda #116                ; Y position (centre vertically)
    sta $0200
    lda #1                  ; Tile index 1 (player ship)
    sta $0201
    lda #%00000000          ; Attributes: palette 0, no flip
    sta $0202
    lda #124                ; X position (centre horizontally)
    sta $0203

    ; Sprite 1: Display tile 2 (solid block) to the right
    lda #116
    sta $0204
    lda #2                  ; Tile index 2 (solid block)
    sta $0205
    lda #%00000001          ; Attributes: palette 1
    sta $0206
    lda #140
    sta $0207

    ; Sprite 2: Display tile 3 (checker pattern)
    lda #116
    sta $0208
    lda #3                  ; Tile index 3 (checker)
    sta $0209
    lda #%00000010          ; Attributes: palette 2
    sta $020A
    lda #156
    sta $020B

    ; Sprite 3: Display tile 4 (diagonal lines)
    lda #116
    sta $020C
    lda #4                  ; Tile index 4 (diagonal)
    sta $020D
    lda #%00000011          ; Attributes: palette 3
    sta $020E
    lda #172
    sta $020F

    ;----------------------------------------------------------
    ; Enable rendering
    ;----------------------------------------------------------
    lda #%10000000          ; NMI enable
    sta PPUCTRL

    lda #%00011110          ; Show background AND sprites
    sta PPUMASK

    lda #$00
    sta PPUSCROLL
    sta PPUSCROLL

;--------------------------------------------------------------
; MAIN LOOP
;--------------------------------------------------------------

main_loop:
    lda #$00
    sta nmi_ready

@wait_for_nmi:
    lda nmi_ready
    beq @wait_for_nmi

    jmp main_loop
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
; NMI HANDLER
;==============================================================

.proc nmi
    pha
    txa
    pha
    tya
    pha

    inc frame_counter

    ; Perform OAM DMA transfer
    ; This copies $0200-$02FF to the PPU's sprite memory
    lda #$00
    sta OAMADDR             ; Start at OAM address 0
    lda #$02                ; High byte of $0200
    sta OAMDMA              ; Trigger DMA (halts CPU for ~513 cycles)

    ; Reset scroll
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
    .byte $01               ; Universal background: dark blue
    .byte $21, $31, $30     ; Palette 0: blues to white
    .byte $01
    .byte $19, $29, $39     ; Palette 1: greens
    .byte $01
    .byte $15, $25, $35     ; Palette 2: magentas
    .byte $01
    .byte $00, $10, $30     ; Palette 3: greys

    ; Sprite palettes
    .byte $01
    .byte $30, $21, $11     ; Palette 0: white/blue (for player)
    .byte $01
    .byte $2A, $1A, $0A     ; Palette 1: greens
    .byte $01
    .byte $25, $15, $05     ; Palette 2: magentas
    .byte $01
    .byte $27, $17, $07     ; Palette 3: oranges

;==============================================================
; VECTORS
;==============================================================

.segment "VECTORS"
    .word nmi
    .word reset
    .word irq

;==============================================================
; CHARACTER DATA (CHR-ROM)
;==============================================================
; This is the pattern table - tile graphics data.
; Each tile is 8x8 pixels, using 16 bytes (8 low + 8 high plane).
;
; The two bit planes combine to create 2-bit colour values:
;   Low=0, High=0 → Colour 0 (transparent for sprites)
;   Low=1, High=0 → Colour 1
;   Low=0, High=1 → Colour 2
;   Low=1, High=1 → Colour 3

.segment "CHARS"

;--------------------------------------------------------------
; TILE 0: Empty (all transparent/background colour)
;--------------------------------------------------------------
; Used as the default "nothing" tile.

    .byte $00, $00, $00, $00, $00, $00, $00, $00  ; Low plane
    .byte $00, $00, $00, $00, $00, $00, $00, $00  ; High plane

;--------------------------------------------------------------
; TILE 1: Player Ship (pointing up)
;--------------------------------------------------------------
; A simple arrow/ship shape. Uses colour 1 only.
;
;   . . . X X . . .     ($18)
;   . . X X X X . .     ($3C)
;   . X X X X X X .     ($7E)
;   X X X X X X X X     ($FF)
;   X X X X X X X X     ($FF)
;   . . X . . X . .     ($24)
;   . . X . . X . .     ($24)
;   . X X . . X X .     ($66)

    ; Low plane (colour bit 0)
    .byte %00011000         ; row 0
    .byte %00111100         ; row 1
    .byte %01111110         ; row 2
    .byte %11111111         ; row 3
    .byte %11111111         ; row 4
    .byte %00100100         ; row 5
    .byte %00100100         ; row 6
    .byte %01100110         ; row 7

    ; High plane (colour bit 1) - all zeros = colour 1 only
    .byte $00, $00, $00, $00, $00, $00, $00, $00

;--------------------------------------------------------------
; TILE 2: Solid Block
;--------------------------------------------------------------
; All pixels filled with colour 3 (both planes set).

    ; Low plane
    .byte $FF, $FF, $FF, $FF, $FF, $FF, $FF, $FF
    ; High plane
    .byte $FF, $FF, $FF, $FF, $FF, $FF, $FF, $FF

;--------------------------------------------------------------
; TILE 3: Checkerboard Pattern
;--------------------------------------------------------------
; Alternating pixels - demonstrates 2-bit colour.
;
;   X . X . X . X .     ($AA)
;   . X . X . X . X     ($55)
;   (repeating...)

    ; Low plane
    .byte $AA, $55, $AA, $55, $AA, $55, $AA, $55
    ; High plane (inverted = creates colour 2 and 3 pattern)
    .byte $55, $AA, $55, $AA, $55, $AA, $55, $AA

;--------------------------------------------------------------
; TILE 4: Diagonal Lines
;--------------------------------------------------------------
; Diagonal stripe pattern.

    ; Low plane
    .byte %10000001         ; X . . . . . . X
    .byte %01000010         ; . X . . . . X .
    .byte %00100100         ; . . X . . X . .
    .byte %00011000         ; . . . X X . . .
    .byte %00011000         ; . . . X X . . .
    .byte %00100100         ; . . X . . X . .
    .byte %01000010         ; . X . . . . X .
    .byte %10000001         ; X . . . . . . X

    ; High plane
    .byte $00, $00, $00, $00, $00, $00, $00, $00

;--------------------------------------------------------------
; Fill the rest of CHR-ROM
;--------------------------------------------------------------
; We've defined 5 tiles (80 bytes). CHR-ROM is 8192 bytes.

    .res 8192 - 80          ; Fill remaining space with zeros
