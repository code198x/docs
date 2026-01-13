;──────────────────────────────────────────────────────────────
; NMI HANDLER
;──────────────────────────────────────────────────────────────
; The NMI (Non-Maskable Interrupt) fires at the start of VBlank,
; 60 times per second on NTSC. For now, it does nothing.

.proc nmi
    rti                     ; Return from interrupt
.endproc

;──────────────────────────────────────────────────────────────
; IRQ HANDLER
;──────────────────────────────────────────────────────────────
; The IRQ handler for hardware interrupts. We don't use IRQs
; in this game, but we need a handler anyway.

.proc irq
    rti                     ; Return from interrupt
.endproc
