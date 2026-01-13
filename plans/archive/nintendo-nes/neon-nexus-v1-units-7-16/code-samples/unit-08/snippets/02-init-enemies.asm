;──────────────────────────────────────────────────────────────
; INITIALISE ENEMIES
;──────────────────────────────────────────────────────────────
; Place enemies at starting positions around the arena.

.proc init_enemies
    ; Enemy 0: top left area
    lda #32
    sta enemy_x
    lda #32
    sta enemy_y

    ; Enemy 1: top right area
    lda #216
    sta enemy_x + 1
    lda #48
    sta enemy_y + 1

    ; Enemy 2: bottom left area
    lda #48
    sta enemy_x + 2
    lda #200
    sta enemy_y + 2

    ; Enemy 3: bottom right area
    lda #200
    sta enemy_x + 3
    lda #184
    sta enemy_y + 3

    rts
.endproc

; Spacing enemies apart makes the game fair at startup.
; Different Y positions create visual variation.
