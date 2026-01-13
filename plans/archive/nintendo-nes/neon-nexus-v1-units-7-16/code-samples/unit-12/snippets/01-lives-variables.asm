;──────────────────────────────────────────────────────────────
; LIVES VARIABLES
;──────────────────────────────────────────────────────────────

.segment "ZEROPAGE"

lives:          .res 1      ; Player lives (0-9)
lives_dirty:    .res 1      ; Flag: lives need redraw
invuln_timer:   .res 1      ; Invulnerability frames

; Constants
STARTING_LIVES = 3
INVULN_FRAMES = 90          ; 1.5 seconds at 60fps

; The player starts with 3 lives.
; After getting hit, they're invulnerable for 90 frames (1.5s).
; This prevents "combo hits" where touching an enemy kills you multiple times instantly.
