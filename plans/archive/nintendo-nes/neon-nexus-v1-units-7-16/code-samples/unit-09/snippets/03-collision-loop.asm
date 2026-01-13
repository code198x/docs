;──────────────────────────────────────────────────────────────
; COLLISION DETECTION LOOP
;──────────────────────────────────────────────────────────────
; Check the player against all 4 enemies.

.proc check_collision
    ldx #0                  ; Enemy index

@loop:
    ; Check X distance
    lda player_x
    sec
    sbc enemy_x, x
    bcs @x_positive
    eor #$FF
    clc
    adc #1
@x_positive:
    cmp #HITBOX_SIZE
    bcs @next_enemy         ; X too far, try next enemy

    ; Check Y distance
    lda player_y
    sec
    sbc enemy_y, x
    bcs @y_positive
    eor #$FF
    clc
    adc #1
@y_positive:
    cmp #HITBOX_SIZE
    bcs @next_enemy         ; Y too far, try next enemy

    ; Both X and Y are close enough - collision!
    lda #1
    sta game_over
    rts                     ; Exit immediately

@next_enemy:
    inx
    cpx #NUM_ENEMIES
    bne @loop               ; Check next enemy

    rts                     ; No collision found
.endproc

; We exit early when a collision is found.
; No need to check remaining enemies - one hit is enough.
