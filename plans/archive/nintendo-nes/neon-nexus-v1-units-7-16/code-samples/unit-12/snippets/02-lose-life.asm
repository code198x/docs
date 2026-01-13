;──────────────────────────────────────────────────────────────
; LOSE LIFE
;──────────────────────────────────────────────────────────────
; Called when enemy collision is detected.
; Decrements lives, triggers invulnerability, or game over.

.proc lose_life
    dec lives
    lda #1
    sta lives_dirty         ; Mark for HUD update

    ; Check for game over
    lda lives
    beq @game_over

    ; Still alive - become invulnerable
    lda #INVULN_FRAMES
    sta invuln_timer
    rts

@game_over:
    lda #1
    sta game_over
    rts
.endproc

; The game_over flag only sets when lives reaches 0.
; Otherwise, the player gets brief invulnerability to recover.
