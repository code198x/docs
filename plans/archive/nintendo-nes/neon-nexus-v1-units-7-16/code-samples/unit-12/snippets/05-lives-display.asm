;──────────────────────────────────────────────────────────────
; LIVES DISPLAY
;──────────────────────────────────────────────────────────────
; Update the lives counter in the HUD when it changes.

.proc update_lives_display
    lda lives_dirty
    beq @done               ; Nothing to update

    bit PPUSTATUS
    lda #$20
    sta PPUADDR
    lda #$1E                ; Row 0, column 30
    sta PPUADDR

    lda lives
    clc
    adc #TILE_DIGIT_0       ; Convert to digit tile
    sta PPUDATA

    lda #0
    sta lives_dirty         ; Clear the flag

@done:
    rts
.endproc

; Lives is a single digit (0-9), so no need for the complex
; hundreds/tens/ones conversion we use for score.
