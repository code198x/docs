;──────────────────────────────────────────────────────────────
; NEON NEXUS
; A fixed-screen action game for the Nintendo Entertainment System
; Unit 4: Palettes and Colours
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

nmi_ready:      .res 1      ; Set by NMI, cleared by main loop
frame_counter:  .res 1      ; Increments every frame

;==============================================================
; PPU REGISTER DEFINITIONS
;==============================================================

.segment "CODE"

PPUCTRL   = $2000           ; PPU control register
PPUMASK   = $2001           ; PPU mask (rendering control)
PPUSTATUS = $2002           ; PPU status register
OAMADDR   = $2003           ; OAM address
PPUSCROLL = $2005           ; Scroll position
PPUADDR   = $2006           ; VRAM address (write twice)
PPUDATA   = $2007           ; VRAM data port
OAMDMA    = $4014           ; OAM DMA transfer

;==============================================================
; RESET HANDLER
;==============================================================

.proc reset
    sei
    cld

    ldx #$40
    stx $4017               ; Disable APU frame IRQ

    ldx #$FF
    txs

    inx                     ; X = $00
    stx PPUCTRL             ; Disable NMI
    stx PPUMASK             ; Disable rendering
    stx $4010               ; Disable DMC IRQs

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

    ; Second VBlank wait
@vblank_wait_2:
    bit PPUSTATUS
    bpl @vblank_wait_2

    ;----------------------------------------------------------
    ; Load palettes
    ;----------------------------------------------------------
    ; This is the key new code for this unit!
    ; We write palette data to PPU address $3F00.

    jsr load_palettes

    ;----------------------------------------------------------
    ; Enable NMI and rendering
    ;----------------------------------------------------------
    ; Now we enable both NMI and background rendering.
    ; The PPU will display the background colour from $3F00.

    lda #%10000000          ; Bit 7 = NMI enable
    sta PPUCTRL

    lda #%00001010          ; Bit 3 = show background
                            ; Bit 1 = show background in leftmost 8 pixels
    sta PPUMASK

    ; Reset scroll position
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

    ; Game logic would go here
    ; For now, we just loop - but look at the screen!
    ; It's no longer grey - it's showing our background colour!

    jmp main_loop
.endproc

;==============================================================
; LOAD PALETTES
;==============================================================
; Write 32 bytes of palette data to the PPU.
; Must be called during VBlank (or before rendering is enabled).

.proc load_palettes
    ; Reset the PPU address latch
    bit PPUSTATUS

    ; Set PPU address to $3F00 (palette RAM)
    lda #$3F                ; High byte
    sta PPUADDR
    lda #$00                ; Low byte
    sta PPUADDR

    ; Write all 32 palette bytes
    ldx #$00
@loop:
    lda palette_data, x     ; Load palette byte
    sta PPUDATA             ; Write to PPU (auto-increments address)
    inx
    cpx #32                 ; All 32 bytes written?
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

    ; Reset scroll (important after any PPUADDR/PPUDATA writes)
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

;--------------------------------------------------------------
; PALETTE DATA
;--------------------------------------------------------------
; 32 bytes total: 16 for background, 16 for sprites.
;
; NES colour values (selected examples):
;   $0F = Black
;   $00 = Dark grey
;   $10 = Light grey
;   $30 = White
;   $11 = Dark blue
;   $21 = Medium blue
;   $31 = Light blue
;   $15 = Dark magenta
;   $25 = Medium magenta
;   $16 = Dark red
;   $27 = Orange
;   $19 = Dark green
;   $29 = Medium green
;   $1A = Bright green

palette_data:
    ; Background palettes (16 bytes)
    ; The first byte ($3F00) is the universal background colour.
    ; It's visible wherever no tile is drawn.

    .byte $01               ; Universal background: dark blue
    .byte $21, $31, $30     ; Palette 0: blues to white
    .byte $01               ; (mirrors $3F00)
    .byte $19, $29, $39     ; Palette 1: greens
    .byte $01               ; (mirrors $3F00)
    .byte $15, $25, $35     ; Palette 2: magentas
    .byte $01               ; (mirrors $3F00)
    .byte $00, $10, $30     ; Palette 3: greys

    ; Sprite palettes (16 bytes)
    ; Sprite colour 0 is always transparent.

    .byte $01               ; (mirrors $3F00)
    .byte $30, $21, $11     ; Palette 0: white to dark blue
    .byte $01               ; (mirrors $3F00)
    .byte $27, $17, $07     ; Palette 1: oranges
    .byte $01               ; (mirrors $3F00)
    .byte $29, $19, $09     ; Palette 2: greens
    .byte $01               ; (mirrors $3F00)
    .byte $24, $14, $04     ; Palette 3: purples

;==============================================================
; VECTORS
;==============================================================

.segment "VECTORS"
    .word nmi               ; $FFFA - NMI vector
    .word reset             ; $FFFC - Reset vector
    .word irq               ; $FFFE - IRQ vector

;==============================================================
; CHARACTER DATA (CHR-ROM)
;==============================================================
; Still empty - we'll add tile graphics in Unit 5.

.segment "CHARS"
    .res 8192               ; 8KB of empty CHR data
