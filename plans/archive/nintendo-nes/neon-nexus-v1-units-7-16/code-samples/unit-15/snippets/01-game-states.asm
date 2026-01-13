;──────────────────────────────────────────────────────────────
; GAME STATE CONSTANTS
;──────────────────────────────────────────────────────────────
; Define the different states our game can be in.

STATE_TITLE = 0
STATE_PLAYING = 1
STATE_GAMEOVER = 2

.segment "ZEROPAGE"
game_state:     .res 1      ; Current game state
screen_drawn:   .res 1      ; Has current screen been drawn?

; The game starts in STATE_TITLE.
; Press START to go to STATE_PLAYING.
; When lives reach 0, go to STATE_GAMEOVER.
; Press START again to restart (back to STATE_PLAYING).
