;──────────────────────────────────────────────────────────────
; ENEMY VARIABLES
;──────────────────────────────────────────────────────────────
; Each enemy needs X and Y coordinates.
; We store them in arrays — 4 enemies, 4 bytes each.

.segment "ZEROPAGE"

enemy_x:        .res 4      ; X positions for 4 enemies
enemy_y:        .res 4      ; Y positions for 4 enemies

; Constants
NUM_ENEMIES = 4

; Access individual enemies with indexed addressing:
;   lda enemy_x       ; Enemy 0 X
;   lda enemy_x + 1   ; Enemy 1 X
;   lda enemy_x, x    ; Enemy X where X register = index
