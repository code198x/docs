;──────────────────────────────────────────────────────────────
; DIRECTION TRACKING VARIABLES
;──────────────────────────────────────────────────────────────
; Track each enemy's direction independently.

.segment "ZEROPAGE"

enemy_x:        .res 4      ; X position for each enemy
enemy_y:        .res 4      ; Y position for each enemy
enemy_dir_x:    .res 4      ; X direction: 0=left, 1=right, 2=none
enemy_dir_y:    .res 4      ; Y direction: 0=up, 1=down, 2=none

; Each enemy has 4 bytes of state:
; - Position (x, y)
; - Direction (x, y)
;
; The direction value 2 means "no movement on this axis" -
; this lets us create horizontal-only or vertical-only enemies.
