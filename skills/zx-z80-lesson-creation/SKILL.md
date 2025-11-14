---
name: zx-z80-lesson-creation
description: Use when creating or editing ZX Spectrum Z80 Assembly lessons - enforces platform-specific compilation, validation, screenshot capture, and Z80 requirements
---

# ZX Spectrum Z80 Assembly Lesson Creation

## Overview

This skill guides creation of ZX Spectrum Z80 assembly lessons. Z80 is NOT 6502 - completely different instruction set, registers (A/B/C/D/E/H/L not A/X/Y), 16-bit operations native. No hardware sprites (software only). ULA for graphics. sjasmplus assembler produces .tap files.

## When to Use

- Creating/editing ZX Spectrum Z80 assembly lessons
- **NOT** for ZX BASIC (use zx-lesson-creation)

## Prerequisites

1. **lesson-creation-workflow skill**
2. **Curriculum:** `/docs/sinclair-zx-spectrum/PHASE-N-CURRICULUM.md`
3. **Tools:** sjasmplus assembler, FUSE emulator, Python 3 validator

## Z80 Assembly Rules

### 1. Z80 Instruction Set (NOT 6502!)

**Registers:**
- 8-bit: A, B, C, D, E, H, L, I, R
- 16-bit pairs: BC, DE, HL, IX, IY, SP, PC
- Shadow registers: AF', BC', DE', HL'
- Flags: S, Z, H, P/V, N, C

**Key differences from 6502:**
- No X/Y registers
- 16-bit operations native (LD HL, $4000)
- Memory-to-memory operations possible
- Different mnemonics entirely

**Common instructions:**
```asm
LD A,0          ; Load A with 0
LD HL,$4000     ; Load HL with address
LD (HL),A       ; Store A to address in HL
INC HL          ; Increment HL
DJNZ loop       ; Decrement B, jump if not zero
CALL subroutine ; Call subroutine
RET             ; Return
```

### 2. Syntax (sjasmplus)

```asm
; Comments start with semicolon
    ORG $8000       ; Origin
label:              ; Labels
    LD A,0          ; Instructions
    OUT ($FE),A     ; I/O
    RET
```

### 3. No Hardware Sprites

**Unlike C64/NES, ZX has NO hardware sprites:**
- All sprites software-rendered
- Manual pixel plotting
- XOR for flicker-free movement
- Attribute handling separate

**Space-efficient sprite routines essential!**

## Required Files Checklist

- [ ] `/website/src/pages/sinclair-zx-spectrum/phase-X/tier-Y/lesson-NNN.mdx`
- [ ] `/code-samples/sinclair-zx-spectrum/phase-X/tier-Y/lesson-NNN/example-1.asm`
- [ ] `/code-samples/sinclair-zx-spectrum/phase-X/tier-Y/lesson-NNN/example-1.tap` (assembled)
- [ ] `/website/public/images/sinclair-zx-spectrum/phase-X/tier-Y/lesson-NNN/screenshot-1.png`

## Compilation Process

### Option 1: Raw Binary

```bash
cd /code-samples/sinclair-zx-spectrum/phase-X/tier-Y/lesson-NNN/

# Assemble to raw binary
sjasmplus example-1.asm --raw=example-1.bin
```

### Option 2: TAP File (Preferred)

```bash
# Assemble directly to .tap
sjasmplus example-1.asm --tap=example-1.tap
```

**Semantic validation:**
```bash
python3 /scripts/validate-zx-asm.py example-1.asm
```

**Checks:**
- Z80 instructions (not 6502)
- Screen memory access ($4000-$57FF)
- Attribute memory access ($5800-$5AFF)
- ULA port usage ($FE)
- Register usage patterns
- Stack management

## Screenshot Capture (FUSE - Manual)

**Same as ZX BASIC:**

```bash
fuse example-1.tap

# Media → Screenshot
# Save to /website/public/images/sinclair-zx-spectrum/.../screenshot-1.png
```

## Z80-Specific Validation

### Memory Map (Same as BASIC)

| Range | Purpose | Writable |
|-------|---------|----------|
| $4000-$57FF | Screen RAM (6144 bytes) | ✓ |
| $5800-$5AFF | Attribute RAM (768 bytes) | ✓ |
| $5B00-$FFFF | User RAM | ✓ |

### Screen Layout

**Pixels:** 256×192 (6144 bytes)
**Attributes:** 32×24 (768 bytes)

**Non-linear pixel layout:**
- Interleaved scanlines (not sequential)
- Complex address calculation required
- Space-efficient algorithms essential

### ULA Port ($FE)

```asm
LD A,7          ; White border, no sound
OUT ($FE),A     ; Write to ULA
```

### Keyboard Reading

**Port $FE with row select:**
```asm
LD BC,$FEFE     ; Read keys A-G,CAPS
IN A,(C)        ; Read port
```

## Anti-Patterns

### 1. Using 6502 Mnemonics

**Anti-pattern:**
```asm
LDA #0          ; This is 6502, not Z80!
STA $4000
```

**Fix:**
```asm
LD A,0          ; Z80 syntax
LD ($4000),A
```

### 2. Assuming Hardware Sprites

**Anti-pattern:**
```asm
; Looking for sprite registers like C64/NES
; ZX has NONE!
```

**Fix:**
```asm
; Implement software sprite routine
; Plot pixels manually
; Use XOR for movement
```

### 3. Linear Screen Address Assumption

**Anti-pattern:**
```asm
LD HL,$4000
INC HL          ; Next pixel... NOT next scanline!
```

**Fix:**
```asm
; Use proper scanline address calculation
; Account for interleaved layout
```

### 4. Wasting Memory/Cycles

**Principle: Space and speed efficiency**
- 48K RAM limit
- No hardware acceleration
- Tight loops essential
- Minimize redundant operations

### 5. Not Using 16-bit Operations

**Anti-pattern:**
```asm
LD A,H
ADD A,4
LD H,A          ; Clumsy 16-bit add
```

**Fix:**
```asm
LD BC,4
ADD HL,BC       ; Native 16-bit add
```

## Complete Workflow Checklist

1. **Preparation:** Read curriculum, create directories
2. **Code Creation:** Write .asm (Z80 syntax!), assemble with sjasmplus
3. **Screenshot:** Manual capture with FUSE
4. **Lesson MDX:** Explain Z80 differences from 6502
5. **Validation:** Run all validation skills
6. **File Verification:** ls all locations
7. **Navigation Update:** Update indexes

## Quick Reference

### Compilation
```bash
sjasmplus example-1.asm --tap=example-1.tap
```

### Screenshot
```bash
fuse example-1.tap
# Media → Screenshot (manual)
```

### Z80 vs 6502 Quick Comparison

| Feature | 6502 | Z80 |
|---------|------|-----|
| Registers | A, X, Y | A, B, C, D, E, H, L |
| 16-bit | No native | BC, DE, HL pairs |
| Load | LDA | LD A, |
| Store | STA | LD (addr),A |
| Increment | INX/INY | INC B/INC HL |
| Call | JSR | CALL |
| Return | RTS | RET |

### Common Z80 Patterns
```asm
; Load 16-bit
LD HL,$4000

; Store to address in HL
LD (HL),A

; 16-bit increment
INC HL

; Decrement loop
DJNZ loop

; Exchange registers
EX AF,AF'
EXX
```

## Common Mistakes

1. **6502 syntax** - Use Z80 mnemonics
2. **Looking for hardware sprites** - Software only
3. **Linear screen assumption** - Non-linear layout
4. **Not using 16-bit ops** - Z80's strength
5. **Wasting memory** - 48K limit, be efficient

## Platform-Specific Resources

**Essential docs:**
- `/docs/Z80-QUICK-REFERENCE.md` - Z80 instruction set
- `/docs/ZX-SPECTRUM-QUICK-REFERENCE.md` - ULA, memory map
- `/docs/START-HERE.md` - Navigation

## The Bottom Line

**ZX Spectrum Z80 lessons require:**
1. sjasmplus compilation to .tap
2. Z80 instruction set (NOT 6502)
3. Software sprite implementation (no hardware)
4. Non-linear screen layout handling
5. FUSE manual screenshot capture
6. Space and cycle-efficient code
7. British English (except "program")

**Zero tolerance for:**
- 6502 syntax (wrong processor!)
- Assuming hardware sprites (none exist)
- Linear screen access (non-linear layout)
- Wasting memory/cycles (limited resources)
- Unverified screenshots
- American spellings (except "program")

**Every Z80 lesson must assemble to .tap, run in FUSE, and display expected output. Z80 is fundamentally different from 6502 - treat as completely separate architecture.**
