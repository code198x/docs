;──────────────────────────────────────────────────────────────
; ITEM VARIABLES
;──────────────────────────────────────────────────────────────
; Add variables for the collectible item and score.

.segment "ZEROPAGE"

item_x:         .res 1      ; Collectible X position
item_y:         .res 1      ; Collectible Y position
score:          .res 1      ; Player score (0-255)

; Constants for item collision
ITEM_HITBOX = 8             ; Slightly larger than enemy hitbox

; Items use a larger hitbox than enemies.
; This makes them easier to collect - a forgiving design choice.
; Enemy hitbox is 7 (precise), item hitbox is 8 (generous).
