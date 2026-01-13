;──────────────────────────────────────────────────────────────
; CALCULATING ABSOLUTE DISTANCE
;──────────────────────────────────────────────────────────────
; To get |A - B|, we subtract and check if the result is negative.
; If negative, we negate it to get the absolute value.

    ; Calculate |player_x - enemy_x|
    lda player_x
    sec
    sbc enemy_x, x          ; A = player_x - enemy_x
    bcs @positive           ; Branch if result >= 0

    ; Result is negative - negate it
    ; To negate: EOR with $FF and add 1 (two's complement)
    eor #$FF
    clc
    adc #1

@positive:
    ; A now contains the absolute distance
    cmp #HITBOX_SIZE
    bcs @no_collision       ; Branch if distance >= hitbox

; The subtraction sets the carry flag (C):
;   C=1 (set) means result >= 0 (no borrow)
;   C=0 (clear) means result < 0 (borrow occurred)
