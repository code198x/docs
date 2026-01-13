;──────────────────────────────────────────────────────────────
; BOUNDING BOX COLLISION
;──────────────────────────────────────────────────────────────
; Two sprites collide if their bounding boxes overlap.
; A bounding box is an invisible rectangle around the sprite.
;
; For simple collision, check if:
;   |player_x - enemy_x| < hitbox_size  AND
;   |player_y - enemy_y| < hitbox_size
;
; The "hitbox size" is how close sprites must be to collide.
; 8 pixels = touching edges of 8×8 sprites.

HITBOX_SIZE = 7             ; Slightly less than sprite size
