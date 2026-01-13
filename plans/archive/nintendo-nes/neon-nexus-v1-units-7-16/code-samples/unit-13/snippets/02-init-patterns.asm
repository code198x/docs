;──────────────────────────────────────────────────────────────
; INITIALISE ENEMY PATTERNS
;──────────────────────────────────────────────────────────────
; Each enemy gets a unique movement pattern.

.proc init_enemies
    ; Enemy 0: Bounces diagonally (starts top-left, going down-right)
    lda #32
    sta enemy_x
    lda #48
    sta enemy_y
    lda #1                  ; Moving right
    sta enemy_dir_x
    lda #1                  ; Moving down
    sta enemy_dir_y

    ; Enemy 1: Bounces diagonally (starts top-right, going down-left)
    lda #200
    sta enemy_x + 1
    lda #64
    sta enemy_y + 1
    lda #0                  ; Moving left
    sta enemy_dir_x + 1
    lda #1                  ; Moving down
    sta enemy_dir_y + 1

    ; Enemy 2: Horizontal only (left-right)
    lda #48
    sta enemy_x + 2
    lda #140
    sta enemy_y + 2
    lda #1                  ; Moving right
    sta enemy_dir_x + 2
    lda #2                  ; Special: horizontal only
    sta enemy_dir_y + 2

    ; Enemy 3: Vertical only (up-down)
    lda #180
    sta enemy_x + 3
    lda #180
    sta enemy_y + 3
    lda #2                  ; Special: vertical only
    sta enemy_dir_x + 3
    lda #0                  ; Moving up
    sta enemy_dir_y + 3

    rts
.endproc
