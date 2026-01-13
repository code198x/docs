;──────────────────────────────────────────────────────────────
; FILLING A ROW
;──────────────────────────────────────────────────────────────
; Each row is 32 tiles. Use a loop to fill efficiently.

    ; Set address to start of row 0 ($2000)
    bit PPUSTATUS
    lda #$20
    sta PPUADDR
    lda #$00
    sta PPUADDR

    ; Fill 32 tiles with tile index 2 (solid block)
    ldx #32
@fill_loop:
    lda #2                  ; Solid block tile
    sta PPUDATA
    dex
    bne @fill_loop

; Result: The entire top row is solid blocks.
; This creates a horizontal border across the screen.
