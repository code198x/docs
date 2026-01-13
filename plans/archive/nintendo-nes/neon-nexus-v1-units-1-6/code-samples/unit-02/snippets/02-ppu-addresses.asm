;──────────────────────────────────────────────────────────────
; PPU ADDRESS CONSTANTS
;──────────────────────────────────────────────────────────────
; Key locations in the PPU's 16KB address space.

PPU_PATTERN_0   = $0000     ; Pattern table 0 (background tiles)
PPU_PATTERN_1   = $1000     ; Pattern table 1 (sprite tiles)
PPU_NAMETABLE_0 = $2000     ; Nametable 0 (screen layout)
PPU_NAMETABLE_1 = $2400     ; Nametable 1
PPU_ATTRIBUTE_0 = $23C0     ; Attribute table 0 (palette zones)
PPU_PALETTES    = $3F00     ; Palette data
