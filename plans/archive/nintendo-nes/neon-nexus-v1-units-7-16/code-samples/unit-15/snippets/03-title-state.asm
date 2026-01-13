;──────────────────────────────────────────────────────────────
; TITLE STATE
;──────────────────────────────────────────────────────────────
; Show title screen, wait for START press.

title_state:
    lda screen_drawn
    bne @check_start        ; Screen already drawn
    jsr draw_title_screen
    lda #1
    sta screen_drawn

@check_start:
    jsr read_controller
    lda buttons
    and #BTN_START
    beq @done_title         ; START not pressed

    ; Transition to playing
    jsr start_game          ; Reset all game variables
    lda #STATE_PLAYING
    sta game_state
    lda #0
    sta screen_drawn        ; Clear so playfield gets drawn

@done_title:
    jmp main_loop

; The screen_drawn flag prevents redrawing every frame.
; When transitioning states, we clear it so the new
; screen gets drawn once.
