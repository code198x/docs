;──────────────────────────────────────────────────────────────
; PPU REGISTER DEFINITIONS
;──────────────────────────────────────────────────────────────
; The PPU has 8 memory-mapped registers at $2000-$2007.
; We define symbolic names to make the code readable.

; Control and status
PPUCTRL   = $2000           ; PPU control register
PPUMASK   = $2001           ; PPU mask (rendering control)
PPUSTATUS = $2002           ; PPU status register

; OAM (sprite) access
OAMADDR   = $2003           ; OAM address
OAMDATA   = $2004           ; OAM data port

; Scrolling
PPUSCROLL = $2005           ; Scroll position

; VRAM access
PPUADDR   = $2006           ; VRAM address (write twice)
PPUDATA   = $2007           ; VRAM data port

; DMA register (not in PPU, but used for sprites)
OAMDMA    = $4014           ; OAM DMA transfer
