;──────────────────────────────────────────────────────────────
; GAME OVER STATE
;──────────────────────────────────────────────────────────────
; When collision sets game_over to 1, the main loop changes behaviour.

main_loop:
    ; Wait for VBlank
    lda #$00
    sta nmi_ready
@wait:
    lda nmi_ready
    beq @wait

    ; Check game state
    lda game_over
    bne @game_over_state

    ; Normal gameplay
    jsr read_controller
    jsr update_player
    jsr move_enemies
    jsr update_enemy_sprites
    jsr check_collision
    jmp main_loop

@game_over_state:
    ; Game over - everything freezes
    ; Only check for Start button to restart
    jsr read_controller
    lda buttons
    and #BTN_START
    beq main_loop           ; Keep waiting
    jsr restart_game
    jmp main_loop

; When game_over is set:
; - Player doesn't move
; - Enemies don't move
; - Only controller is read (checking for Start)
