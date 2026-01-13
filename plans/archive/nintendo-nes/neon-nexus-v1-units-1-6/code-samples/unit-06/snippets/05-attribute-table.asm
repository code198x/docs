;──────────────────────────────────────────────────────────────
; ATTRIBUTE TABLE
;──────────────────────────────────────────────────────────────
; The attribute table at $23C0 controls palette assignments
; for the background. Each byte covers a 4×4 tile area (32×32 pixels).
;
; Byte layout (bits):
;   Bits 0-1: Top-left 2×2 tiles
;   Bits 2-3: Top-right 2×2 tiles
;   Bits 4-5: Bottom-left 2×2 tiles
;   Bits 6-7: Bottom-right 2×2 tiles
;
; Each 2-bit value selects palette 0-3.

    bit PPUSTATUS

    ; Set address to attribute table ($23C0)
    lda #$23
    sta PPUADDR
    lda #$C0
    sta PPUADDR

    ; Fill all 64 bytes with $00 (palette 0 everywhere)
    lda #$00
    ldx #64
@attr_loop:
    sta PPUDATA
    dex
    bne @attr_loop

; For varied palettes, calculate which byte and bits to modify.
; Example: $55 = %01010101 assigns palette 1 to all quadrants.
