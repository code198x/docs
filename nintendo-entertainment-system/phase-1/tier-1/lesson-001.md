# Lesson 001: Minimal NES Program

**Arc:** Hello, NES
**Position:** Lesson 1 of 4 in arc
**Type:** Standard
**Estimated Completion:** 30 lines of assembly

## Learning Objectives

- Write first working NES ROM
- Understand iNES header format
- Create reset vector and boot sequence
- Display solid colour on screen

## Key Concepts Introduced

### iNES ROM Format
16-byte header + PRG-ROM + CHR-ROM. Header specifies mapper, ROM sizes, mirroring. All NES ROMs need this header to run in emulators and on real hardware.

### Reset Vector
CPU jumps to address at $FFFC on power-on. Reset vector points to program start. Part of 6-byte vector table at $FFFA-$FFFF.

### PPU (Picture Processing Unit)
Separate graphics chip. CPU writes to PPU registers ($2000-$2007) to control display. PPU runs independently, synchronized via VBlank.

### 6502 Basics
LDA (load), STA (store), JMP (jump). Memory-mapped I/O for hardware control. Simple instructions build complex programs.

## Code Pattern

```asm
; iNES header (16 bytes)
.segment "HEADER"
.byte "NES", $1A    ; Magic constant
.byte $02           ; 2 × 16KB PRG-ROM
.byte $01           ; 1 × 8KB CHR-ROM
.byte $00, $00      ; Mapper 0, horizontal mirroring

; Program code
.segment "CODE"
Reset:
    SEI             ; Disable interrupts
    CLD             ; Clear decimal mode (not used on NES)

    ; Wait for PPU warmup (2 VBlanks)
    BIT $2002
:   BIT $2002
    BPL :-

:   BIT $2002
    BPL :-

    ; Set background colour
    LDA #$3F
    STA $2006       ; PPUADDR high byte
    LDA #$00
    STA $2006       ; PPUADDR low byte
    LDA #$29        ; Colour $29 (green)
    STA $2007       ; PPUDATA

    ; Enable PPU
    LDA #%00001000  ; Enable background
    STA $2001

Forever:
    JMP Forever

; Interrupt handlers (empty for now)
NMI:
IRQ:
    RTI

; Vector table
.segment "VECTORS"
.word NMI           ; $FFFA: NMI handler
.word Reset         ; $FFFC: Reset handler
.word IRQ           ; $FFFE: IRQ handler

; Graphics data (empty for now)
.segment "CHARS"
.res 8192, $00
```

## Quick Reference

### iNES Header
- Bytes 0-3: "NES" + $1A
- Byte 4: PRG-ROM size (16KB units)
- Byte 5: CHR-ROM size (8KB units)
- Byte 6-7: Mapper and flags

### PPU Registers
- $2006: PPUADDR (address for VRAM access)
- $2007: PPUDATA (read/write VRAM)
- $2001: PPUMASK (enable rendering)
- $2002: PPUSTATUS (check VBlank)

### 6502 Instructions Used
- `SEI`: Set interrupt disable
- `CLD`: Clear decimal mode
- `LDA #value`: Load accumulator immediate
- `STA address`: Store accumulator
- `BIT address`: Test bits (sets flags)
- `BPL label`: Branch if plus (bit 7 clear)
- `JMP label`: Jump to label
- `RTI`: Return from interrupt

---

**Version:** 1.0
**Created:** 2025-10-24
