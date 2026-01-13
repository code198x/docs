;──────────────────────────────────────────────────────────────
; RESTART GAME
;──────────────────────────────────────────────────────────────
; Reset everything to starting conditions.

.proc restart_game
    ; Reset player to centre
    lda #116
    sta player_y
    lda #124
    sta player_x

    ; Update sprite immediately
    lda player_y
    sta $0200
    lda player_x
    sta $0203

    ; Reset enemies to starting positions
    jsr init_enemies

    ; Clear the game over flag
    lda #0
    sta game_over

    rts
.endproc

; After restart, the main loop resumes normal gameplay
; since game_over is now 0.
