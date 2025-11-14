---
name: amiga-68k-lesson-creation
description: Use when creating or editing Amiga 68000 Assembly lessons - enforces platform-specific compilation, validation, screenshot capture, and 68K requirements
---

# Amiga 68000 Assembly Lesson Creation

## Overview

This skill guides creation of Amiga 68000 assembly lessons. The 68000 is completely different from 6502/Z80: 32-bit data/address registers (D0-D7/A0-A7), memory-to-memory operations, sophisticated addressing modes, privileged modes. Amiga has custom chips (copper, blitter, Paula) and Exec OS. vasm assembler, FS-UAE emulator.

## When to Use

- Creating/editing Amiga 68000 assembly lessons
- **NOT** for AMOS BASIC (use amiga-lesson-creation)

## Prerequisites

1. **lesson-creation-workflow skill**
2. **Curriculum:** `/docs/commodore-amiga/PHASE-N-CURRICULUM.md`
3. **Tools:** vasm assembler (68000, mot syntax), FS-UAE emulator, Python 3 validator

## 68000 Assembly Rules

### 1. 68000 Architecture (NOT 6502/Z80!)

**Registers:**
- **Data:** D0-D7 (32-bit, can use as 8/16/32-bit)
- **Address:** A0-A7 (32-bit, A7 is stack pointer)
- **Program Counter:** PC
- **Status Register:** SR (system byte + condition codes)

**Key differences from 6502/Z80:**
- 32-bit registers (not 8-bit)
- Memory-to-memory operations possible
- Sophisticated addressing modes
- Privilege levels (user/supervisor)
- No zero page (full 32-bit address space)

### 2. 68000 Instructions

**Common operations:**
```asm
MOVE.L #0,D0        ; Move long (32-bit) to D0
MOVE.W D0,(A0)      ; Move word to address in A0
LEA $DFF000,A0      ; Load effective address
ADD.W #1,D0         ; Add word
JSR subroutine      ; Jump to subroutine
RTS                 ; Return
```

**Size suffixes:**
- `.B` = Byte (8-bit)
- `.W` = Word (16-bit)
- `.L` = Long (32-bit)

### 3. Syntax (vasm mot syntax)

```asm
; Comments start with semicolon
    ORG $1000           ; Origin
label:                  ; Labels
    MOVE.L #0,D0        ; Instructions
    RTS
```

### 4. Custom Chip Registers ($DFFxxx)

**Critical Amiga hardware:**
- Copper: $DFF080-$DFF088
- Blitter: $DFF040-$DFF074
- Paula audio: $DFF0A0-$DFF0D8
- Display: $DFF000-$DFF1FF

**Space-efficient code: Direct hardware access is fast but plan register usage.**

## Required Files Checklist

- [ ] `/website/src/pages/commodore-amiga/phase-X/tier-Y/lesson-NNN.mdx`
- [ ] `/code-samples/commodore-amiga/phase-X/tier-Y/lesson-NNN/example-1.asm`
- [ ] `/code-samples/commodore-amiga/phase-X/tier-Y/lesson-NNN/example-1` (executable)
- [ ] `/website/public/images/commodore-amiga/phase-X/tier-Y/lesson-NNN/screenshot-1.png`

## Compilation Process

```bash
cd /code-samples/commodore-amiga/phase-X/tier-Y/lesson-NNN/

# Assemble with vasm (68000, mot syntax, hunk executable)
vasm68k_mot -Fhunkexe -o example-1 example-1.asm

# Check exit code
echo $?  # Should be 0 (success)
```

**Flags explained:**
- `vasm68k_mot` = 68000 with Motorola syntax
- `-Fhunkexe` = AmigaDOS hunk executable format
- `-o example-1` = Output file
- `example-1.asm` = Input source

**Semantic validation:**
```bash
python3 /scripts/validate-amiga-asm.py example-1.asm
```

**Checks:**
- 68000 instructions (not 6502/Z80)
- Custom chip register access
- Supervisor/user mode usage
- Exec library calls
- Register preservation
- Stack management
- AmigaDOS conventions

## Screenshot Capture (FS-UAE - Manual)

```bash
# Load executable
fs-uae --amiga-model=A1200 --hard-drive-0=/code-samples/commodore-amiga/.../

# Run program from Workbench/CLI
# Capture screenshot via menu
# Save to /website/public/images/commodore-amiga/.../screenshot-1.png
```

## 68000-Specific Validation

### Register Usage

**Data registers (D0-D7):** General purpose, calculations
**Address registers (A0-A6):** Pointers, addressing
**A7 (SP):** Stack pointer - don't corrupt!

**Convention: Preserve registers in subroutines**

```asm
subroutine:
    MOVEM.L D0-D7/A0-A6,-(SP)    ; Save all registers
    ; ... do work ...
    MOVEM.L (SP)+,D0-D7/A0-A6    ; Restore all registers
    RTS
```

### Addressing Modes

**68000 has rich addressing:**
```asm
MOVE.L #100,D0          ; Immediate
MOVE.L D0,D1            ; Register to register
MOVE.L (A0),D0          ; Indirect
MOVE.L (A0)+,D0         ; Post-increment
MOVE.L -(A0),D0         ; Pre-decrement
MOVE.L 4(A0),D0         ; Displacement
MOVE.L 4(A0,D0.W),D1    ; Indexed
```

**Don't waste: Use appropriate addressing mode for efficiency.**

### Custom Chip Access

**Example: Copper list**
```asm
    LEA $DFF080,A0          ; COPCON
    MOVE.W #$8000,(A0)      ; Enable copper
```

**Example: Blitter**
```asm
    LEA $DFF000,A5          ; Custom chip base
    MOVE.W #$09F0,$40(A5)   ; Blitter control
```

**Example: Paula audio**
```asm
    LEA $DFF0A0,A0          ; Audio channel 0
    MOVE.L sample_addr,(A0) ; Set sample pointer
```

### Exec Library Calls

**Calling OS functions:**
```asm
    MOVE.L 4.W,A6           ; Get ExecBase
    JSR -132(A6)            ; Call Forbid()
```

**Preserve A6 if using library calls!**

## Anti-Patterns

### 1. Using 6502/Z80 Mnemonics

**Anti-pattern:**
```asm
LDA #0              ; This is 6502!
STA $D020
```

**Fix:**
```asm
MOVE.L #0,D0        ; 68000 syntax
MOVE.W D0,$DFF180   ; Custom chip write
```

### 2. Not Using 32-bit Operations

**Anti-pattern:**
```asm
MOVE.W D0,D1        ; Only moving 16 bits
```

**Fix (if appropriate):**
```asm
MOVE.L D0,D1        ; Full 32-bit move
```

### 3. Corrupting Stack Pointer (A7)

**Anti-pattern:**
```asm
MOVE.L A7,A0
MOVE.L #$1000,A7    ; Corrupted stack - crash!
```

**Fix:**
```asm
; Never modify A7 directly unless you know exactly what you're doing
; Use LINK/UNLK for stack frames
```

### 4. Not Preserving Registers

**Anti-pattern:**
```asm
subroutine:
    MOVE.L #0,D0        ; Clobbers D0
    RTS                 ; Caller's D0 destroyed!
```

**Fix:**
```asm
subroutine:
    MOVEM.L D0-D1/A0-A1,-(SP)
    ; ... work ...
    MOVEM.L (SP)+,D0-D1/A0-A1
    RTS
```

### 5. Wasting Memory/Cycles

**Principle: Memory is more abundant than 8-bit systems, but still plan efficiently.**
- Use appropriate data sizes (.B/.W/.L)
- Leverage addressing modes
- Minimize custom chip register access (slow)

### 6. Ignoring Privilege Levels

**Anti-pattern:**
```asm
; User mode trying to write supervisor registers - crash!
MOVE.W #$8000,SR
```

**Fix:**
```asm
; Use Exec library calls for privileged operations
; Or ensure code runs in supervisor mode if appropriate
```

## Complete Workflow Checklist

1. **Preparation:** Read curriculum, create directories
2. **Code Creation:** Write .asm (68000 syntax!), assemble with vasm
3. **Screenshot:** Manual capture with FS-UAE
4. **Lesson MDX:** Explain 68000 differences from 6502/Z80, custom chips
5. **Validation:** Run all validation skills
6. **File Verification:** ls all locations
7. **Navigation Update:** Update indexes

## Quick Reference

### Compilation
```bash
vasm68k_mot -Fhunkexe -o example-1 example-1.asm
```

### Screenshot
```bash
fs-uae --amiga-model=A1200 --hard-drive-0=/path/
# Run executable, capture via menu
```

### 68000 vs 6502/Z80 Comparison

| Feature | 6502 | Z80 | 68000 |
|---------|------|-----|-------|
| Registers | A,X,Y (8-bit) | A,B,C,D,E,H,L (8-bit) | D0-D7,A0-A7 (32-bit) |
| Load | LDA | LD A, | MOVE.L |
| Add | ADC | ADD A, | ADD.L |
| Call | JSR | CALL | JSR |
| Return | RTS | RET | RTS |
| Mem-Mem | No | Limited | Yes |

### Common 68000 Patterns
```asm
; Load address
LEA data,A0

; Memory to memory
MOVE.L (A0)+,(A1)+

; Save/restore registers
MOVEM.L D0-D7/A0-A6,-(SP)
MOVEM.L (SP)+,D0-D7/A0-A6

; Custom chip access
LEA $DFF000,A5
MOVE.W #value,offset(A5)
```

### Custom Chip Base Addresses
```asm
$DFF000  ; Custom chip base
$DFF080  ; Copper
$DFF040  ; Blitter
$DFF0A0  ; Paula audio
$DFF180  ; Color palette
```

## Common Mistakes

1. **6502/Z80 syntax** - Use 68000 mnemonics
2. **Not using 32-bit** - Leverage full registers
3. **Corrupting A7 (SP)** - System crash
4. **Not preserving registers** - Unexpected behavior
5. **Ignoring privilege levels** - Crashes
6. **Inefficient addressing** - Use rich addressing modes

## Platform-Specific Resources

**Essential docs:**
- `/docs/68000-QUICK-REFERENCE.md` - 68000 instruction set
- `/docs/AMIGA-QUICK-REFERENCE.md` - Custom chips, memory map
- `/docs/START-HERE.md` - Navigation

## The Bottom Line

**Amiga 68000 lessons require:**
1. vasm compilation to hunk executable
2. 68000 instruction set (NOT 6502/Z80)
3. Custom chip register usage (copper/blitter/Paula)
4. Register preservation (MOVEM.L)
5. FS-UAE manual screenshot capture
6. Space and cycle-efficient code
7. British English (except "program")

**Zero tolerance for:**
- 6502/Z80 syntax (wrong processor!)
- Corrupting stack pointer (system crash)
- Not preserving registers (unpredictable)
- Wasting memory/cycles (be efficient)
- Unverified screenshots
- American spellings (except "program")

**Every 68000 lesson must assemble to hunk format, run in FS-UAE, and display expected output. 68000 is fundamentally different from 8-bit processors - treat as completely separate architecture with 32-bit capabilities.**
