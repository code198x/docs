;──────────────────────────────────────────────────────────────
; STATE MACHINE IN MAIN LOOP
;──────────────────────────────────────────────────────────────
; Branch to the correct state handler each frame.

main_loop:
    lda #$00
    sta nmi_ready
@wait_for_nmi:
    lda nmi_ready
    beq @wait_for_nmi

    ; State machine
    lda game_state
    cmp #STATE_TITLE
    beq title_state
    cmp #STATE_PLAYING
    beq playing_state
    jmp gameover_state

; Each state:
; 1. Draws its screen once (if screen_drawn = 0)
; 2. Handles its own logic
; 3. Checks for state transitions
; 4. Jumps back to main_loop
