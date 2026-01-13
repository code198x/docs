;──────────────────────────────────────────────────────────────
; GAME OVER TRANSITION
;──────────────────────────────────────────────────────────────
; When lives reach zero, transition to game over state.

.proc lose_life
    dec lives
    lda #1
    sta lives_dirty

    jsr play_hit_sound

    lda lives
    beq @game_over          ; Lives = 0?

    ; Still alive - start invulnerability
    lda #INVULN_FRAMES
    sta invuln_timer
    rts

@game_over:
    ; Transition to game over state
    lda #STATE_GAMEOVER
    sta game_state
    rts
.endproc

; Note: we don't need to clear screen_drawn here.
; The playing_state code detects the state change
; and clears it before jumping to main_loop.
