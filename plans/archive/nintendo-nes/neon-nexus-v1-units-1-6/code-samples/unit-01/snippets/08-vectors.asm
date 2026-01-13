;──────────────────────────────────────────────────────────────
; VECTOR TABLE
;──────────────────────────────────────────────────────────────
; The CPU looks at $FFFA-$FFFF to find interrupt handlers.
; These MUST be at the very end of the ROM.

.segment "VECTORS"
    .word nmi               ; $FFFA - NMI vector
    .word reset             ; $FFFC - Reset vector
    .word irq               ; $FFFE - IRQ vector

;──────────────────────────────────────────────────────────────
; CHARACTER DATA (CHR-ROM)
;──────────────────────────────────────────────────────────────
; The PPU's pattern tables. For now, just empty space.
; We'll add tile graphics in later units.

.segment "CHARS"
    .res 8192               ; 8KB of empty CHR data
