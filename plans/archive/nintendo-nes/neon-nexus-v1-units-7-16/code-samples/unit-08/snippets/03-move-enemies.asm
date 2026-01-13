;──────────────────────────────────────────────────────────────
; MOVE ENEMIES
;──────────────────────────────────────────────────────────────
; Simple movement pattern: some move down, some move up.
; Wrap around when reaching screen edges.

.proc move_enemies
    ; Enemies 0 and 1 move down
    inc enemy_y
    inc enemy_y + 1

    ; Enemies 2 and 3 move up
    dec enemy_y + 2
    dec enemy_y + 3

    ; Check boundaries and wrap

    ; Enemies 0 and 1: wrap from bottom to top
    lda enemy_y
    cmp #224                ; Bottom boundary
    bcc @check_enemy_1      ; Branch if < 224
    lda #9                  ; Reset to top
    sta enemy_y

@check_enemy_1:
    lda enemy_y + 1
    cmp #224
    bcc @check_enemy_2
    lda #9
    sta enemy_y + 1

@check_enemy_2:
    ; Enemies 2 and 3: wrap from top to bottom
    lda enemy_y + 2
    cmp #8                  ; Top boundary
    bcs @check_enemy_3      ; Branch if >= 8
    lda #223                ; Reset to bottom
    sta enemy_y + 2

@check_enemy_3:
    lda enemy_y + 3
    cmp #8
    bcs @done
    lda #223
    sta enemy_y + 3

@done:
    rts
.endproc
