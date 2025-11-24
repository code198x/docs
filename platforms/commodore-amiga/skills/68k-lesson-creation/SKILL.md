---
name: amiga-68k-lesson-creation
description: Use when creating or editing Amiga 68000 Assembly lessons - provides platform-specific compilation, validation, and screenshot capture for Phase 3 of the content creation workflow
---

# Amiga 68000 Assembly Lesson Creation

**Role:** Technical execution for Phase 3 (Validation) of the Content Creation Workflow.

**Prerequisite:** Read `/docs/CONTENT-CREATION-WORKFLOW.md` first. This skill provides 68000-specific technical details, not the full workflow.

---

## When to Use

Use this skill during **Phase 3 (Validation)** when:
- Assembling 68000 code with vasm
- Capturing screenshots with FS-UAE emulator
- Validating 68000 instruction usage and custom chip access
- Checking for Amiga-specific pitfalls

**Do NOT use for:**
- AMOS BASIC lessons (use `amos-lesson-creation` skill)
- Other platforms (use platform-specific skills)

---

## 68000 Assembly Rules (NOT 6502/Z80!)

### Registers

- **Data:** D0-D7 (32-bit, can use as 8/16/32-bit)
- **Address:** A0-A7 (32-bit, A7 is stack pointer)
- **Program Counter:** PC
- **Status Register:** SR

### Size Suffixes

- `.B` = Byte (8-bit)
- `.W` = Word (16-bit)
- `.L` = Long (32-bit)

### Key Instructions

```asm
MOVE.L #0,D0        ; Move long (32-bit) to D0
MOVE.W D0,(A0)      ; Move word to address in A0
LEA $DFF000,A0      ; Load effective address
ADD.W #1,D0         ; Add word
JSR subroutine      ; Jump to subroutine
RTS                 ; Return
```

### Custom Chip Registers ($DFFxxx)

- Copper: $DFF080-$DFF088
- Blitter: $DFF040-$DFF074
- Paula audio: $DFF0A0-$DFF0D8
- Display: $DFF000-$DFF1FF

---

## Phase 3: Validation (Technical Details)

### Step 3.1: Assemble with vasm

```bash
cd /code-samples/commodore-amiga/phase-X/tier-Y/lesson-NNN/

vasm68k_mot -Fhunkexe -o example-1 example-1.asm
echo $?  # Must be 0
```

**Flags:**
- `vasm68k_mot` = 68000 with Motorola syntax
- `-Fhunkexe` = AmigaDOS hunk executable
- `-o example-1` = Output file

### Step 3.2: Semantic Validation

```bash
python3 /scripts/validate-amiga-asm.py example-1.asm
```

**Checks:**
- ✅ 68000 instructions (not 6502/Z80)
- ✅ Custom chip register access
- ✅ Register preservation
- ✅ Stack management
- ✅ Exec library conventions

### Step 3.3: Screenshot Capture (FS-UAE - Manual)

```bash
fs-uae --amiga-model=A1200 --hard-drive-0=/path/to/code-samples/
```

1. Run executable from Workbench/CLI
2. Capture via FS-UAE menu
3. Save to `/website/public/images/commodore-amiga/phase-X/tier-Y/lesson-NNN/screenshot-1.png`

### Step 3.4: Screenshot Verification (MANDATORY)

**Use Read tool to VIEW every screenshot:**

```
✅ CORRECT: "Read screenshot-1.png - shows copper effect with colour bars,
   no Guru Meditation error."

❌ WRONG: "Screenshot verified ✅" (too vague)
```

---

## Register Preservation

```asm
subroutine:
    MOVEM.L D0-D7/A0-A6,-(SP)    ; Save all registers
    ; ... do work ...
    MOVEM.L (SP)+,D0-D7/A0-A6    ; Restore all registers
    RTS
```

---

## Common Pitfalls

### 1. Using 6502/Z80 Mnemonics
```asm
❌ WRONG: LDA #0          ; 6502 syntax!
✅ CORRECT: MOVE.L #0,D0  ; 68000 syntax
```

### 2. Corrupting Stack Pointer (A7)
```asm
❌ WRONG:
    MOVE.L #$1000,A7       ; Corrupted stack - crash!

✅ CORRECT:
    ; Never modify A7 directly
    ; Use LINK/UNLK for stack frames
```

### 3. Not Preserving Registers
```asm
❌ WRONG:
subroutine:
    MOVE.L #0,D0           ; Clobbers caller's D0!
    RTS

✅ CORRECT:
subroutine:
    MOVEM.L D0-D1,-(SP)
    ; ... work ...
    MOVEM.L (SP)+,D0-D1
    RTS
```

### 4. Not Using 32-bit Operations
```asm
❌ WRONG:
    MOVE.W D0,D1           ; Only 16 bits

✅ CORRECT (if appropriate):
    MOVE.L D0,D1           ; Full 32-bit
```

---

## 68000 vs 6502/Z80 Comparison

| Feature | 6502 | Z80 | 68000 |
|---------|------|-----|-------|
| Registers | A,X,Y (8-bit) | A-L (8-bit) | D0-D7,A0-A7 (32-bit) |
| Load | LDA | LD A, | MOVE.L |
| Call | JSR | CALL | JSR |
| Mem-Mem | No | Limited | Yes |

---

## Required Files

| File | Location |
|------|----------|
| Lesson MDX | `/website/src/pages/commodore-amiga/phase-X/tier-Y/lesson-NNN.mdx` |
| Source (.asm) | `/code-samples/commodore-amiga/phase-X/tier-Y/lesson-NNN/example-1.asm` |
| Executable | `/code-samples/commodore-amiga/phase-X/tier-Y/lesson-NNN/example-1` |
| Screenshot | `/website/public/images/commodore-amiga/phase-X/tier-Y/lesson-NNN/screenshot-1.png` |

---

## Quick Reference Commands

```bash
# Assemble
vasm68k_mot -Fhunkexe -o example-1 example-1.asm

# Semantic validation
python3 /scripts/validate-amiga-asm.py example-1.asm

# Test in emulator
fs-uae --amiga-model=A1200 --hard-drive-0=/path/
```

### Custom Chip Base Addresses
```asm
$DFF000  ; Custom chip base
$DFF080  ; Copper
$DFF040  ; Blitter
$DFF0A0  ; Paula audio
$DFF180  ; Color palette
```

---

## Platform-Specific Resources

**Quick references** (in `/docs/platforms/commodore-amiga/`):
- `hardware/68000-QUICK-REFERENCE.md` - Instruction set
- `hardware/AMIGA-HARDWARE-REFERENCE.md` - Custom chips

---

## The Bottom Line

**This skill provides:** Assembly, validation, and screenshot capture for 68000 lessons.

**The main workflow provides:** Planning, creation, integration, and publication steps.

**Zero tolerance for:**
- 6502/Z80 syntax (wrong processor!)
- Corrupting A7 (stack pointer)
- Not preserving registers
- Unverified screenshots
