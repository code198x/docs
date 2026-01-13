;──────────────────────────────────────────────────────────────
; MOVEMENT DISPATCHER
;──────────────────────────────────────────────────────────────
; Check each enemy's pattern and call the right movement code.

.proc move_enemies
    ldx #0

@loop:
    ; Check movement type
    lda enemy_dir_x, x
    cmp #2
    beq @vertical_only      ; X direction = 2? Vertical only

    lda enemy_dir_y, x
    cmp #2
    beq @horizontal_only    ; Y direction = 2? Horizontal only

    ; Diagonal movement (both axes)
    jsr move_enemy_x
    jsr move_enemy_y
    jmp @next

@horizontal_only:
    jsr move_enemy_x
    jmp @next

@vertical_only:
    jsr move_enemy_y

@next:
    inx
    cpx #NUM_ENEMIES
    bne @loop

    rts
.endproc
