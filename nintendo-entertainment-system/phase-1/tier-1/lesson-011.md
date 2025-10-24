# Lesson 011: Sprite DMA

**Arc:** Sprite Fundamentals
**Position:** Lesson 3 of 4 in arc
**Type:** Standard
**Estimated Completion:** 40 lines of assembly

## Learning Objectives

- Implement OAM DMA ($4014)
- Update sprites during VBlank
- Understand DMA timing
- Master sprite synchronization

## Key Concepts Introduced

### OAM DMA (Direct Memory Access)
Hardware copies 256 bytes from CPU RAM to OAM in 513 cycles. Write high byte of source address to $4014. Must happen during VBlank.

### DMA Timing
513 CPU cycles = ~8.5 scanlines of VBlank. Efficient batch transfer. Much faster than manual copy (would take ~2560 cycles with loop).

### VBlank Window
~2273 cycles available during VBlank. DMA uses 513, leaving ~1760 for other updates (palettes, nametable, scroll).

### Update Pattern
Game logic updates OAM buffer ($0200) during main loop. NMI handler triggers DMA. Graphics update synchronized to 60fps.

## Code Pattern

```asm
.segment "ZEROPAGE"
paddle_y: .res 1

.segment "CODE"
Reset:
    ; [Init code from previous lessons]

    ; Set up initial sprite
    LDA #100
    STA paddle_y
    JSR UpdateOAM

    ; Enable NMI and rendering
    LDA #%10100000
    STA $2000
    LDA #%00011110
    STA $2001

MainLoop:
    ; Wait for NMI
:   LDA nmi_ready
    BEQ :-
    LDA #$00
    STA nmi_ready

    ; Game logic: Update paddle position
    JSR UpdateOAM

    JMP MainLoop

NMI:
    ; Save registers
    PHA
    TXA
    PHA
    TYA
    PHA

    ; Trigger OAM DMA
    LDA #$02         ; High byte of $0200
    STA $4014        ; Starts DMA transfer

    ; Set flag
    LDA #$01
    STA nmi_ready

    ; Restore and return
    PLA
    TAY
    PLA
    TAX
    PLA
    RTI

UpdateOAM:
    ; Write sprite data to OAM buffer
    LDA paddle_y
    STA $0200        ; Y position

    LDA #$00
    STA $0201        ; Tile

    LDA #%00000000
    STA $0202        ; Attributes

    LDA #16
    STA $0203        ; X position

    RTS
```

## DMA Timing Breakdown

```
Total VBlank: ~2273 cycles
OAM DMA:       513 cycles (22.5%)
Remaining:    1760 cycles (77.5%)

Available for:
- Palette updates (~100 cycles)
- Scroll updates (~10 cycles)
- Nametable writes (7 cycles per byte)
```

## Quick Reference

### $4014 Register
Write high byte of source address (usually $02 for $0200-$02FF). Hardware copies next 256 bytes to OAM.

### Why During VBlank?
PPU is idle during VBlank. CPU has exclusive access to PPU memory. Writes outside VBlank cause glitches.

### DMA Alignment
DMA waits for even CPU cycle. Actual cycles = 513 or 514 depending on CPU cycle parity when $4014 written.

---

**Version:** 1.0
**Created:** 2025-10-24
