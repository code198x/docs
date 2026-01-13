;──────────────────────────────────────────────────────────────
; MOVE ENEMY Y
;──────────────────────────────────────────────────────────────
; Move enemy vertically and bounce off walls.
; X register = enemy index

.proc move_enemy_y
    lda enemy_dir_y, x
    beq @move_up

    ; Moving down
    inc enemy_y, x
    lda enemy_y, x
    cmp #216                ; Bottom boundary
    bcc @done
    lda #0
    sta enemy_dir_y, x      ; Reverse to up
    jmp @done

@move_up:
    dec enemy_y, x
    lda enemy_y, x
    cmp #25                 ; Top boundary (below HUD)
    bcs @done
    lda #1
    sta enemy_dir_y, x      ; Reverse to down

@done:
    rts
.endproc

; The Y movement uses the same pattern as X.
; Separating X and Y into subroutines lets us
; call just one for horizontal/vertical enemies.
