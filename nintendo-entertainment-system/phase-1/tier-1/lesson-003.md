# Lesson 003: CPU and Memory Map

**Arc:** Hello, NES
**Position:** Lesson 3 of 4 in arc
**Type:** Standard
**Estimated Completion:** 25 lines of assembly

## Learning Objectives

- Understand 6502 CPU architecture
- Master NES memory map
- Use zero page for variables
- Store and retrieve game state

## Key Concepts Introduced

### 6502 CPU
8-bit processor, 1.79 MHz (NTSC). Three registers: A (accumulator), X, Y (index). 256-byte stack at $0100-$01FF.

### NES Memory Map
- $0000-$00FF: Zero page (fast access, 2-cycle instructions)
- $0100-$01FF: Stack
- $0200-$02FF: OAM buffer (sprite data)
- $0300-$07FF: General RAM
- $8000-$FFFF: PRG-ROM (program code)

### Zero Page Variables
Store game state in zero page for fast access. LDA $00 is faster than LDA $0300. Use for frequently accessed data.

### Variable Storage Pattern
Define memory locations with labels. Use .segment "ZEROPAGE" for variables. Store/load with STA/LDA.

## Code Pattern

```asm
; Define variables in zero page
.segment "ZEROPAGE"
counter: .res 1      ; 1 byte at $00
colour:  .res 1      ; 1 byte at $01

.segment "CODE"
Reset:
    SEI
    CLD

    ; Wait for PPU
    BIT $2002
:   BIT $2002
    BPL :-
:   BIT $2002
    BPL :-

    ; Initialize variables
    LDA #$00
    STA counter
    LDA #$12
    STA colour

    ; Use variable to set background colour
    LDA #$3F
    STA $2006
    LDA #$00
    STA $2006
    LDA colour       ; Load from variable
    STA $2007

    ; Enable rendering
    LDA #%00001000
    STA $2001

Forever:
    ; Increment counter
    INC counter
    JMP Forever
```

## Quick Reference

### Memory Access Speeds
- Zero page: 3 cycles (`LDA $00`)
- Absolute: 4 cycles (`LDA $0300`)
- Immediate: 2 cycles (`LDA #$12`)

### 6502 Registers
- **A**: Accumulator (arithmetic, logic)
- **X**: Index register (array access, counters)
- **Y**: Index register (array access, counters)
- **SP**: Stack pointer ($0100-$01FF)
- **PC**: Program counter (current instruction)

### Memory Allocation
- Reserve zero page for hottest variables
- Use $0200-$02FF for OAM buffer (sprite data)
- Use $0300+ for general game state

---

**Version:** 1.0
**Created:** 2025-10-24
