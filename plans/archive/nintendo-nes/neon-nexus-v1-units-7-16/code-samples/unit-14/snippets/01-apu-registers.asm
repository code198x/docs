;──────────────────────────────────────────────────────────────
; APU REGISTERS
;──────────────────────────────────────────────────────────────
; The NES Audio Processing Unit registers for pulse channel 1.

APU_PULSE1_CTRL = $4000     ; Duty cycle, envelope, volume
APU_PULSE1_SWEEP = $4001    ; Sweep unit (pitch bending)
APU_PULSE1_LO = $4002       ; Timer low byte (pitch)
APU_PULSE1_HI = $4003       ; Length counter, timer high
APU_STATUS = $4015          ; Channel enable flags

; APU_PULSE1_CTRL bits:
;   Bits 7-6: Duty cycle (00=12.5%, 01=25%, 10=50%, 11=75%)
;   Bit 5: Length counter halt / envelope loop
;   Bit 4: Constant volume (1) or envelope (0)
;   Bits 3-0: Volume / envelope period

; APU_STATUS enables channels:
;   Bit 0: Pulse 1
;   Bit 1: Pulse 2
;   Bit 2: Triangle
;   Bit 3: Noise
;   Bit 4: DMC
