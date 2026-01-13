;──────────────────────────────────────────────────────────────
; PPU REGISTER DEFINITIONS
;──────────────────────────────────────────────────────────────
; The PPU (Picture Processing Unit) is controlled through
; memory-mapped registers at $2000-$2007.

.segment "CODE"

PPUCTRL   = $2000           ; PPU control register
PPUMASK   = $2001           ; PPU mask register (rendering control)
PPUSTATUS = $2002           ; PPU status register
