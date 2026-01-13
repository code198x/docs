;──────────────────────────────────────────────────────────────
; VARIABLES
;──────────────────────────────────────────────────────────────
; Zero page is fast memory - use it for frequently accessed data.

.segment "ZEROPAGE"

nmi_ready:      .res 1      ; Set by NMI, cleared by main loop
frame_counter:  .res 1      ; Increments every frame (wraps at 256)
