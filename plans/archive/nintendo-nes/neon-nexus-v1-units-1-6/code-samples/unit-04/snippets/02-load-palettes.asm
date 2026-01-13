;──────────────────────────────────────────────────────────────
; LOAD PALETTES
;──────────────────────────────────────────────────────────────
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
