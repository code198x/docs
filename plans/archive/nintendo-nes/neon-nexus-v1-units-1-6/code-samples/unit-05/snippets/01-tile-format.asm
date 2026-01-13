;──────────────────────────────────────────────────────────────
; TILE FORMAT
;──────────────────────────────────────────────────────────────
; Each tile is 8×8 pixels, stored as two bit planes.
; 16 bytes per tile: 8 bytes low plane + 8 bytes high plane.
;
; The two planes combine to create 2-bit colour values:
;   Low=0, High=0 → Colour 0 (transparent for sprites)
;   Low=1, High=0 → Colour 1
;   Low=0, High=1 → Colour 2
;   Low=1, High=1 → Colour 3
;
; Memory layout for one tile:
;   Bytes 0-7:  Low plane (bit 0 of each pixel)
;   Bytes 8-15: High plane (bit 1 of each pixel)
