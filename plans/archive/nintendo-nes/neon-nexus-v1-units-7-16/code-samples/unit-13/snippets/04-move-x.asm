;──────────────────────────────────────────────────────────────
; MOVE ENEMY X
;──────────────────────────────────────────────────────────────
; Move enemy horizontally and bounce off walls.
; X register = enemy index

.proc move_enemy_x
    lda enemy_dir_x, x
    beq @move_left

    ; Moving right
    inc enemy_x, x
    lda enemy_x, x
    cmp #232                ; Right boundary
    bcc @done
    lda #0
    sta enemy_dir_x, x      ; Reverse to left
    jmp @done

@move_left:
    dec enemy_x, x
    lda enemy_x, x
    cmp #9                  ; Left boundary
    bcs @done
    lda #1
    sta enemy_dir_x, x      ; Reverse to right

@done:
    rts
.endproc

; The pattern: check direction, move, check boundary, reverse.
; This is the foundation for all bouncing movement.
