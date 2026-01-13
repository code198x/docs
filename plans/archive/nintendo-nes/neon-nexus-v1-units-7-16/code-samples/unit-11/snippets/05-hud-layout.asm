;──────────────────────────────────────────────────────────────
; HUD LAYOUT
;──────────────────────────────────────────────────────────────
; The HUD uses the top row of the nametable.
; Nametable address $2000 is row 0, column 0.

.proc draw_score_label
    bit PPUSTATUS
    lda #$20                ; High byte of $2022
    sta PPUADDR
    lda #$22                ; Low byte (row 1, col 2)
    sta PPUADDR

    ; Write "SCORE" using letter tiles 15-19
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

; Nametable address calculation:
; $2000 + (row * 32) + column
; Row 1, column 2 = $2000 + 32 + 2 = $2022
;
; The actual digits go at $2028 (after "SCORE:" with a gap)
; leaving space for labels and the 3-digit score.
