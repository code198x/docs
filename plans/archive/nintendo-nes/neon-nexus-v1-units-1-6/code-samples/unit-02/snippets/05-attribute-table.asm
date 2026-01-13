;──────────────────────────────────────────────────────────────
; ATTRIBUTE TABLE
;──────────────────────────────────────────────────────────────
; The attribute table assigns palettes to 2×2 tile groups.
; It's 64 bytes, located at $23C0 (after the nametable).
;
; Each byte controls a 4×4 tile area (32×32 pixels):
;
;   Byte layout:
;   +--------+--------+
;   | Bits   | Bits   |
;   | 1-0    | 3-2    |
;   +--------+--------+
;   | Bits   | Bits   |
;   | 5-4    | 7-6    |
;   +--------+--------+
;
; Each 2-bit value selects a palette (0-3).
;
; Example attribute byte: %11 10 01 00 = $E4
;   Top-left 2×2:     palette 0 (bits 1-0)
;   Top-right 2×2:    palette 1 (bits 3-2)
;   Bottom-left 2×2:  palette 2 (bits 5-4)
;   Bottom-right 2×2: palette 3 (bits 7-6)

attribute_example:
    ; Set palette 0 for entire screen (all zeros)
    bit PPUSTATUS
    lda #$23
    sta PPUADDR
    lda #$C0
    sta PPUADDR

    lda #$00                ; Palette 0 for all quadrants
    ldx #64
@loop:
    sta PPUDATA
    dex
    bne @loop
    rts
