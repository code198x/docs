# Lesson 004: VBlank Timing

**Arc:** Hello, NES
**Position:** Lesson 4 of 4 in arc
**Type:** Standard
**Estimated Completion:** 40 lines of assembly

## Learning Objectives

- Understand VBlank period
- Implement NMI handler
- Synchronize updates to 60fps
- Master game loop timing

## Key Concepts Introduced

### VBlank Period
Time when TV electron beam returns to top. ~2273 CPU cycles. Safe to update PPU during VBlank. Happens 60 times per second.

### NMI (Non-Maskable Interrupt)
Hardware interrupt triggered at start of VBlank. CPU jumps to NMI handler. Standard method for 60fps game loop.

### Register Preservation
NMI can interrupt main code. Must save A, X, Y at start, restore before RTI. Use PHA (push), PLA (pull).

### Game Loop Structure
Main loop does game logic. NMI does graphics updates. Flag variable synchronizes them. Clean separation of concerns.

## Code Pattern

```asm
.segment "ZEROPAGE"
nmi_ready: .res 1

.segment "CODE"
Reset:
    SEI
    CLD

    ; PPU warmup
    BIT $2002
:   BIT $2002
    BPL :-
:   BIT $2002
    BPL :-

    ; Enable NMI
    LDA #%10000000   ; Enable NMI (bit 7)
    STA $2000

    ; Enable rendering
    LDA #%00001000
    STA $2001

MainLoop:
    ; Wait for NMI
:   LDA nmi_ready
    BEQ :-

    ; Reset flag
    LDA #$00
    STA nmi_ready

    ; Game logic here
    ; (increment counters, check input, etc.)

    JMP MainLoop

NMI:
    ; Save registers
    PHA
    TXA
    PHA
    TYA
    PHA

    ; Graphics updates here
    ; (this runs 60 times per second)

    ; Set ready flag
    LDA #$01
    STA nmi_ready

    ; Restore registers
    PLA
    TAY
    PLA
    TAX
    PLA
    RTI
```

## Quick Reference

### VBlank Timing (NTSC)
- Active display: 241 scanlines (CPU running)
- VBlank period: 20 scanlines (~2273 cycles)
- Total frame: 261 scanlines (16.67ms)
- Frequency: 60 Hz

### NMI Control
- $2000 bit 7: Enable/disable NMI
- $2002 bit 7: VBlank flag (cleared on read)

### Stack Instructions
- `PHA`: Push A to stack
- `PLA`: Pull A from stack
- `PHP`: Push status flags
- `PLP`: Pull status flags

### Why This Pattern?
Separates game logic (MainLoop) from graphics (NMI). Game runs as fast as possible, graphics locked to 60fps. Standard NES architecture.

---

**Version:** 1.0
**Created:** 2025-10-24
