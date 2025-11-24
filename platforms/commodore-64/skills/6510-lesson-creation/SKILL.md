---
name: c64-6510-lesson-creation
description: Use when creating or editing C64 6510 Assembly lessons - provides platform-specific compilation, validation, and screenshot capture for Phase 3 of the content creation workflow
---

# C64 6510 Assembly Lesson Creation

**Role:** Technical execution for Phase 3 (Validation) of the Content Creation Workflow.

**Prerequisite:** Read `/docs/CONTENT-CREATION-WORKFLOW.md` first. This skill provides 6510-specific technical details, not the full workflow.

---

## When to Use

Use this skill during **Phase 3 (Validation)** when:
- Assembling 6510 code with ca65/ld65
- Capturing screenshots with VICE x64sc
- Validating zero page usage and register preservation
- Checking for 6510-specific pitfalls

**Do NOT use for:**
- C64 BASIC lessons (use `basic-lesson-creation` skill)
- Other platforms (use platform-specific skills)

---

## 6510 Assembly Rules

### Instruction Set (6502 + I/O Port)

**Legal instructions:**
- Load/Store: LDA, LDX, LDY, STA, STX, STY
- Transfer: TAX, TAY, TXA, TYA, TSX, TXS
- Stack: PHA, PHP, PLA, PLP
- Arithmetic: ADC, SBC, INC, INX, INY, DEC, DEX, DEY
- Logic: AND, ORA, EOR
- Shift: ASL, LSR, ROL, ROR
- Compare: CMP, CPX, CPY
- Branch: BCC, BCS, BEQ, BMI, BNE, BPL, BVC, BVS
- Jump: JMP, JSR, RTS, RTI
- Flags: CLC, CLD, CLI, CLV, SEC, SED, SEI
- Other: BIT, NOP, BRK

### Addressing Modes

```asm
LDA #$00      ; Immediate
LDA $00       ; Zero page
LDA $00,X     ; Zero page indexed X
LDA $1000     ; Absolute
LDA $1000,X   ; Absolute indexed X
LDA $1000,Y   ; Absolute indexed Y
LDA ($00,X)   ; Indexed indirect
LDA ($00),Y   ; Indirect indexed
```

### BASIC Stub (Space-Efficient)

**C64 assembly requires BASIC stub for SYS call:**

```asm
.org $0801
; BASIC stub: 10 SYS 2061 (saves 3 bytes vs SYS 2064)
.byte $0b,$08,$0a,$00,$9e,$32,$30,$36,$31,$00,$00,$00

; Code starts at $080D (2061 decimal)
start:
    LDA #$00
    STA $D020
    RTS
```

---

## Phase 3: Validation (Technical Details)

### Step 3.1: Assemble with ca65

```bash
cd /code-samples/commodore-64/phase-X/tier-Y/lesson-NNN/

ca65 -t c64 example-1.asm -o example-1.o
echo $?  # Must be 0
```

**Common errors:**
- `Illegal instruction` → Invalid 6510 opcode
- `Undefined symbol` → Missing label
- `Range error` → Branch > 127 bytes

### Step 3.2: Link with ld65

```bash
ld65 -t c64 example-1.o -o example-1.prg
echo $?  # Must be 0
```

### Step 3.3: Semantic Validation

```bash
python3 /scripts/validate-c64-asm.py example-1.asm
```

**Checks:**
- ✅ Zero page usage (avoid $00-$8F)
- ✅ Register preservation (PHA/PLA balance)
- ✅ Stack balance (JSR/RTS pairs)
- ✅ SEI/CLI pairing
- ✅ Branch distances
- ✅ Hardware register validity

### Step 3.4: Screenshot Capture

**Manual:**
```bash
x64sc -autostart example-1.prg
# Press Alt+S to capture
```

**Automated:**
```bash
x64sc -autostart example-1.prg \
  -limitcycles 20000000 \
  -VICIIdsize \
  -exitscreenshot screenshot-1.png \
  +sound
```

### Step 3.5: Screenshot Verification (MANDATORY)

**Use Read tool to VIEW every screenshot:**

```
✅ CORRECT: "Read screenshot-1.png - shows black border, blue background,
   sprite at center. NO error messages visible."

❌ WRONG: "Screenshot verified ✅" (too vague)
```

**If ANY issue found:** Fix code → Reassemble → Recapture → Re-verify

---

## Zero Page Safety

| Range | Usage | Safe |
|-------|-------|------|
| $00-$01 | Processor port | ✗ Critical |
| $02-$8F | BASIC/KERNAL | ✗ Avoid |
| $90-$FA | BASIC storage | ⚠ Caution |
| $FB-$FE | Free for user | ✓ Safe |

**Always use $FB-$FE for your variables.**

---

## Register Preservation

**Preserve A/X/Y in subroutines:**

```asm
subroutine:
    PHA           ; Save A
    TXA : PHA     ; Save X
    TYA : PHA     ; Save Y

    ; ... work ...

    PLA : TAY     ; Restore Y
    PLA : TAX     ; Restore X
    PLA           ; Restore A
    RTS
```

**Validation:**
```bash
grep -c "PHA" example-1.asm  # Count pushes
grep -c "PLA" example-1.asm  # Should match
```

---

## Interrupt Handling

**Always pair SEI/CLI:**

```asm
setup_irq:
    SEI           ; Disable interrupts
    ; ... configure IRQ ...
    CLI           ; Re-enable interrupts
    RTS
```

---

## Common Pitfalls

### 1. Using SYS 2064 Instead of 2061
```asm
❌ WRONG: .byte ...$32,$30,$36,$34...  ; SYS 2064 (wastes 3 bytes)
✅ CORRECT: .byte ...$32,$30,$36,$31... ; SYS 2061
```

### 2. Using BASIC Zero Page
```asm
❌ WRONG: LDA $91    ; BASIC working storage
✅ CORRECT: LDA $FB  ; Safe user area
```

### 3. Unbalanced Stack
```asm
❌ WRONG:
    PHA
    ; forgot PLA
    RTS        ; Stack corrupted!

✅ CORRECT:
    PHA
    ; ... work ...
    PLA
    RTS
```

### 4. Branch Too Far
```asm
❌ WRONG:
loop:
    ; ... 200 bytes ...
    BNE loop   ; Range error!

✅ CORRECT:
loop:
    ; ... 200 bytes ...
    BEQ done
    JMP loop
done:
```

### 5. Missing SEI Before IRQ Setup
```asm
❌ WRONG:
    LDA #<irq_handler
    STA $0314    ; Crash during write!

✅ CORRECT:
    SEI
    LDA #<irq_handler
    STA $0314
    CLI
```

---

## Hardware Addresses

| Address | Decimal | Purpose |
|---------|---------|---------|
| $D020 | 53280 | Border colour |
| $D021 | 53281 | Background colour |
| $D000-$D010 | 53248-53264 | Sprite positions |
| $D015 | 53269 | Sprite enable |
| $D027-$D02E | 53287-53294 | Sprite colours |
| $DC00 | 56320 | CIA #1 Port A (joystick) |

---

## Required Files

| File | Location |
|------|----------|
| Lesson MDX | `/website/src/pages/commodore-64/phase-X/tier-Y/lesson-NNN.mdx` |
| Source (.asm) | `/code-samples/commodore-64/phase-X/tier-Y/lesson-NNN/example-1.asm` |
| Object (.o) | `/code-samples/commodore-64/phase-X/tier-Y/lesson-NNN/example-1.o` |
| Executable (.prg) | `/code-samples/commodore-64/phase-X/tier-Y/lesson-NNN/example-1.prg` |
| Screenshot | `/website/public/images/commodore-64/phase-X/tier-Y/lesson-NNN/screenshot-1.png` |

---

## Quick Reference Commands

```bash
# Assemble + link
ca65 -t c64 example-1.asm -o example-1.o
ld65 -t c64 example-1.o -o example-1.prg

# Semantic validation
python3 /scripts/validate-c64-asm.py example-1.asm

# Screenshot
x64sc -autostart example-1.prg
# Press Alt+S

# Check register balance
grep -c "PHA" example-1.asm
grep -c "PLA" example-1.asm
```

---

## Platform-Specific Resources

**Quick references** (in `/docs/platforms/commodore-64/`):
- `hardware/6510-QUICK-REFERENCE.md` - Instructions, addressing
- `hardware/VIC-II-QUICK-REFERENCE.md` - Graphics registers
- `hardware/CIA-QUICK-REFERENCE.md` - I/O registers

**Common errors:**
- `advanced/6510-COMMON-ERRORS.md` - Assembly pitfalls

---

## The Bottom Line

**This skill provides:** Assembly, linking, validation, and screenshot capture for 6510 lessons.

**The main workflow provides:** Planning, creation, integration, and publication steps.

**Zero tolerance for:**
- Missing BASIC stub
- Wasting space (use SYS 2061)
- Using BASIC/KERNAL zero page
- Unbalanced stack
- Unverified screenshots
