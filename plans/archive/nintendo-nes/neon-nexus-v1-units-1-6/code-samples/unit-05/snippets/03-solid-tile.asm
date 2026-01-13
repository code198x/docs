;──────────────────────────────────────────────────────────────
; TILE 2: Solid Block
;──────────────────────────────────────────────────────────────
; All pixels filled with colour 3 (both planes set).
; This creates a completely solid 8×8 square.

    ; Low plane - all bits set
    .byte $FF, $FF, $FF, $FF, $FF, $FF, $FF, $FF

    ; High plane - all bits set
    .byte $FF, $FF, $FF, $FF, $FF, $FF, $FF, $FF

; Result: Every pixel has Low=1 and High=1, giving colour 3.
