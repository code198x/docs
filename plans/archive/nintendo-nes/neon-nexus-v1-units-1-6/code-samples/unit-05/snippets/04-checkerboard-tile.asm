;──────────────────────────────────────────────────────────────
; TILE 3: Checkerboard Pattern
;──────────────────────────────────────────────────────────────
; Alternating pixels - demonstrates multi-colour tiles.
;
;   X . X . X . X .     ($AA)
;   . X . X . X . X     ($55)
;   (repeating...)
;
; The inverted high plane creates a 4-colour pattern:
;   Position (0,0): Low=1, High=0 → Colour 1
;   Position (1,0): Low=0, High=1 → Colour 2
;   Position (0,1): Low=0, High=1 → Colour 2
;   Position (1,1): Low=1, High=0 → Colour 1

    ; Low plane
    .byte $AA, $55, $AA, $55, $AA, $55, $AA, $55

    ; High plane (inverted pattern)
    .byte $55, $AA, $55, $AA, $55, $AA, $55, $AA
