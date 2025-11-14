---
name: c64-6510-lesson-creation
description: Use when creating or editing C64 6510 Assembly lessons - enforces platform-specific compilation, validation, screenshot capture, and assembly requirements
---

# C64 6510 Assembly Lesson Creation

## Overview

This skill guides creation of C64 6510 assembly language lessons with platform-specific validation, compilation, and screenshot capture. It extends the generic lesson-creation-workflow with 6510-specific requirements.

## When to Use

Use when:
- Creating new C64 6510 assembly lesson
- Editing existing C64 assembly lesson
- Validating C64 assembly lesson before commit

**Do NOT use for:**
- C64 BASIC lessons (use c64-lesson-creation instead)
- Other platforms (use platform-specific skills)

---

## Prerequisites

**Before starting, ensure:**

1. **lesson-creation-workflow skill** - Read generic workflow first
2. **Curriculum alignment** - Read `/docs/commodore-64/PHASE-N-CURRICULUM.md`
3. **Tools installed:**
   - `ca65` (cc65 assembler) - 6502/6510 assembler
   - `ld65` (cc65 linker) - Produces .prg files
   - `x64sc` (VICE emulator) - For screenshot capture
   - Python 3 - For semantic validator

---

## 6510 Assembly Rules

**Critical requirements for 6510 assembly:**

### 1. Instruction Set

**6510 = 6502 + illegal opcodes (optional)**

**Legal 6502 instructions:**
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

**Illegal opcodes (optional, use with caution):**
- DCP, ISC, LAX, RLA, RRA, SAX, SLO, SRE
- Document usage clearly if used

### 2. Addressing Modes

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

### 3. Syntax (ca65)

**Case-insensitive instructions, case-sensitive labels:**

```asm
; Comments start with semicolon
.org $0801        ; Origin directive
label:            ; Labels end with colon
    LDA #$00      ; Instructions indented
    STA $D020     ; Hex with $
    RTS           ; Return from subroutine
```

### 4. BASIC Stub Requirement (Space-Efficient)

**C64 assembly programs need BASIC stub for SYS call:**

```asm
.org $0801        ; BASIC start

; BASIC stub: 10 SYS 2061 (saves 3 bytes vs SYS 2064)
.byte $0b,$08,$0a,$00,$9e,$32,$30,$36,$31,$00,$00,$00

; Assembly code starts at $080D (2061 decimal)
start:
    LDA #$00
    STA $D020
    RTS
```

**Why SYS 2061 instead of 2064:** Code starts immediately after 12-byte stub, no wasted space.

---

## Required Files Checklist

For C64 6510 assembly lesson NNN in Phase X, Tier Y:

- [ ] `/website/src/pages/commodore-64/phase-X/tier-Y/lesson-NNN.mdx`
- [ ] `/code-samples/commodore-64/phase-X/tier-Y/lesson-NNN/example-1.asm`
- [ ] `/code-samples/commodore-64/phase-X/tier-Y/lesson-NNN/example-1.prg` (assembled+linked)
- [ ] `/code-samples/commodore-64/phase-X/tier-Y/lesson-NNN/example-2.asm` (if applicable)
- [ ] `/code-samples/commodore-64/phase-X/tier-Y/lesson-NNN/example-2.prg` (if applicable)
- [ ] `/website/public/images/commodore-64/phase-X/tier-Y/lesson-NNN/screenshot-1.png`
- [ ] `/website/public/images/commodore-64/phase-X/tier-Y/lesson-NNN/screenshot-2.png` (if applicable)

---

## Compilation Process

### Step 1: Assemble with ca65

```bash
cd /code-samples/commodore-64/phase-X/tier-Y/lesson-NNN/

# Assemble to object file
ca65 -t c64 example-1.asm -o example-1.o

# Check exit code
echo $?  # Should be 0 (success)
```

**Flags explained:**
- `-t c64` = Target C64 platform
- `-o example-1.o` = Output object file
- `example-1.asm` = Input assembly source

**Common ca65 errors:**
- `Error: Illegal instruction` → Invalid 6510 opcode
- `Error: Undefined symbol` → Missing label definition
- `Error: Range error` → Branch too far (> 127 bytes)

### Step 2: Link with ld65

```bash
# Link object to PRG
ld65 -t c64 example-1.o -o example-1.prg

# Check exit code
echo $?  # Should be 0 (success)
```

**Flags explained:**
- `-t c64` = Target C64 platform (generates correct PRG format)
- `example-1.o` = Input object file
- `-o example-1.prg` = Output executable

**Common ld65 errors:**
- `Error: Unresolved external` → Missing symbol in object
- `Error: Segment overflow` → Code too large for memory region

### Step 3: Run Semantic Validator

```bash
# 6510 assembly semantic validator
python3 /scripts/validate-c64-asm.py example-1.asm
```

**Semantic checks:**
- Register preservation (A/X/Y saved if needed)
- Zero page usage (avoid BASIC/KERNAL areas)
- Stack usage (JSR/RTS balanced)
- Hardware register writes (valid addresses)
- Interrupt handling (SEI/CLI pairs)
- Branch distance (not > ±127 bytes)
- Illegal opcode documentation

---

## Screenshot Capture

**Same as C64 BASIC:** x64sc emulator with .prg autostart.

### Manual Capture

```bash
x64sc -autostart example-1.prg

# Press Alt+S to capture screenshot
```

### Automated Capture

```bash
x64sc -autostart example-1.prg \
  -limitcycles 20000000 \
  -VICIIdsize \
  -exitscreenshot /website/public/images/.../screenshot-1.png \
  +sound
```

---

## 6510-Specific Validation

### 1. Zero Page Usage

**Safe zero page addresses:**

| Range | Usage | Safe for User Code |
|-------|-------|-------------------|
| $00-$01 | Processor port, memory config | ✗ Critical |
| $02-$8F | BASIC/KERNAL working storage | ✗ Avoid |
| $90-$FF | BASIC working storage | ⚠ Caution |
| $FB-$FE | Free for user code | ✓ Safe |

**Validation:**
```bash
# Find zero page usage
grep -iE "\\$[0-9a-f]{2}[^0-9a-f]" example-1.asm

# Check if using $02-$8F (BASIC/KERNAL area)
```

### 2. Register Preservation

**Good practice: Preserve A/X/Y in subroutines**

```asm
subroutine:
    PHA           ; Save A
    TXA
    PHA           ; Save X
    TYA
    PHA           ; Save Y
    
    ; ... do work ...
    
    PLA           ; Restore Y
    TAY
    PLA           ; Restore X
    TAX
    PLA           ; Restore A
    RTS
```

**Validation:**
```bash
# Check for PHA/PLA balance
grep -c "PHA" example-1.asm
grep -c "PLA" example-1.asm
# Counts should match
```

### 3. Interrupt Handling

**If setting up interrupt:**

```asm
setup_irq:
    SEI           ; Disable interrupts
    ; ... configure IRQ ...
    CLI           ; Re-enable interrupts
    RTS
```

**Validation:**
```bash
# Check SEI has matching CLI
grep -n "SEI\|CLI" example-1.asm
```

### 4. Branch Distance

**Branches limited to ±127 bytes:**

```asm
loop:
    ; ... lots of code ...
    DEX
    BNE loop      ; If > 127 bytes away, use JMP instead
```

**Validation:**
- ca65 reports "Range error" if branch too far
- Fix: Use JMP for long jumps

### 5. Hardware Access Validation

**Same as BASIC:**
- VIC-II: $D000-$D02E
- SID: $D400-$D41C
- CIA #1: $DC00-$DC0F
- CIA #2: $DD00-$DD0F
- Screen RAM: $0400-$07E7
- Colour RAM: $D800-$DBE7

```bash
# Find hardware access
grep -iE "\\$D[0-9A-F]{3}" example-1.asm
```

---

## Anti-Patterns (6510 Assembly Specific)

### 1. Not Preserving Registers

**Anti-pattern:**
```asm
main:
    JSR subroutine
    LDA counter    ; Expects A unchanged
    ; ... A was clobbered by subroutine!
```

**Fix:**
```asm
subroutine:
    PHA            ; Save registers
    ; ... work ...
    PLA            ; Restore registers
    RTS
```

### 2. Using Zero Page Without Checking

**Anti-pattern:**
```asm
LDA $91          ; BASIC working storage - corrupted!
```

**Fix:**
```asm
LDA $FB          ; Safe user area
```

### 3. Wasting Space with SYS 2064

**Anti-pattern:**
```asm
.org $0801
.byte $0b,$08,$0a,$00,$9e,$32,$30,$36,$34,$00,$00,$00  ; SYS 2064
; 3 wasted bytes at $080D-$080F
.org $0810       ; Code starts at 2064
start:
```

**Fix:**
```asm
.org $0801
.byte $0b,$08,$0a,$00,$9e,$32,$30,$36,$31,$00,$00,$00  ; SYS 2061
; Code starts immediately at $080D (saves 3 bytes)
start:
```

### 4. Long Branches

**Anti-pattern:**
```asm
loop:
    ; ... 200 bytes of code ...
    DEX
    BNE loop     ; Range error!
```

**Fix:**
```asm
loop:
    ; ... 200 bytes of code ...
    DEX
    BEQ done
    JMP loop     ; Use JMP for long distance
done:
```

### 5. Unbalanced Stack

**Anti-pattern:**
```asm
subroutine:
    PHA
    ; ... forgot PLA ...
    RTS          ; Stack corrupted!
```

**Fix:**
```asm
subroutine:
    PHA
    ; ... work ...
    PLA
    RTS
```

### 6. Reading Write-Only Registers

**Anti-pattern:**
```asm
LDA $D020      ; Border colour - write-only in some cases
```

**Better:**
```asm
; Keep shadow copy in RAM
LDA border_colour
```

---

## Integration with Other Skills

**After code creation, run these skills:**

1. **lesson-validation** - Generic validation
2. **curriculum-alignment-check** - Verify matches curriculum
3. **screenshot-verification** - Verify screenshots correct
4. **british-english-check** - Language validation
5. **voice-tone-check** - Voice consistency

---

## Complete Workflow Checklist

### Phase 1: Preparation

- [ ] Read curriculum spec for lesson
- [ ] Check if mismatched lesson exists (archive if needed)
- [ ] Create code sample directory
- [ ] Create screenshot directory

### Phase 2: Code Creation

- [ ] Write example-1.asm with BASIC stub (SYS 2061)
- [ ] Validate 6510 instruction set
- [ ] Check zero page usage ($FB-$FE safe)
- [ ] Check register preservation
- [ ] Assemble with ca65 → example-1.o
- [ ] Link with ld65 → example-1.prg
- [ ] Run semantic validator
- [ ] Create example-2.asm if needed

### Phase 3: Screenshot Capture

- [ ] Load example-1.prg in x64sc
- [ ] Capture screenshot (manual or automated)
- [ ] Save to correct location
- [ ] Verify screenshot with READ tool
- [ ] Capture additional screenshots if needed

### Phase 4: Lesson MDX Creation

- [ ] Create lesson-NNN.mdx
- [ ] Include assembly code with explanations
- [ ] Explain register usage
- [ ] Explain memory layout
- [ ] Add screenshots
- [ ] British English (except "program")

### Phase 5: Validation

- [ ] Run lesson-validation skill
- [ ] Run curriculum-alignment-check
- [ ] Run screenshot-verification
- [ ] Run british-english-check
- [ ] Run voice-tone-check
- [ ] Fix any issues

### Phase 6: File Verification

- [ ] ls code-samples/.../lesson-NNN/ (all files present)
- [ ] ls website/public/images/.../lesson-NNN/ (all screenshots present)
- [ ] ls website/src/pages/.../lesson-NNN.mdx (lesson file present)

### Phase 7: Navigation Update

- [ ] Update tier-N.astro with new lesson
- [ ] Update phase-N.astro if new tier
- [ ] Update commodore-64.astro if new phase

---

## Quick Reference

### Compilation
```bash
ca65 -t c64 example-1.asm -o example-1.o
ld65 -t c64 example-1.o -o example-1.prg
```

### Screenshot
```bash
x64sc -autostart example-1.prg
# Alt+S to capture
```

### BASIC Stub Template (Space-Efficient)
```asm
.org $0801
.byte $0b,$08,$0a,$00,$9e,$32,$30,$36,$31,$00,$00,$00  ; SYS 2061
; Code starts at $080D
```

### Safe Zero Page
```asm
$FB, $FC, $FD, $FE  ; Safe for user code
```

### Common Hardware Addresses
```asm
$D020  ; Border colour
$D021  ; Background colour
$D000  ; Sprite 0 X
$D001  ; Sprite 0 Y
$D015  ; Sprite enable
$D027  ; Sprite 0 colour
```

---

## Common Mistakes

**Mistake 1: Missing BASIC stub**
- **Symptom:** Program won't load from BASIC
- **Fix:** Add BASIC stub at $0801

**Mistake 2: Using SYS 2064 instead of SYS 2061**
- **Symptom:** 3 wasted bytes
- **Fix:** Use SYS 2061 ($080D) for space efficiency

**Mistake 3: Using BASIC zero page**
- **Symptom:** Crashes, corruption
- **Fix:** Use $FB-$FE only

**Mistake 4: Unbalanced stack**
- **Symptom:** RTS jumps to wrong address
- **Fix:** Balance PHA/PLA, JSR/RTS

**Mistake 5: Branch too far**
- **Symptom:** "Range error" during assembly
- **Fix:** Use JMP instead of branch

**Mistake 6: Not preserving registers**
- **Symptom:** Unexpected behavior after JSR
- **Fix:** PHA/PLA around subroutines

**Mistake 7: Forgetting SEI/CLI**
- **Symptom:** System crashes during IRQ setup
- **Fix:** Always pair SEI with CLI

---

## Platform-Specific Resources

**Essential docs:**
- `/docs/6510-QUICK-REFERENCE.md` - Instruction set, addressing modes
- `/docs/VIC-II-QUICK-REFERENCE.md` - Hardware registers
- `/docs/SID-QUICK-REFERENCE.md` - Sound registers
- `/docs/CIA-QUICK-REFERENCE.md` - I/O registers
- `/docs/START-HERE.md` - Navigation

---

## The Bottom Line

**C64 6510 assembly lessons require:**
1. ca65/ld65 compilation to .prg
2. BASIC stub at $0801 using SYS 2061 (space-efficient)
3. Safe zero page usage ($FB-$FE)
4. Register preservation in subroutines
5. SEI/CLI pairing for interrupts
6. Branch distance validation
7. British English (except "program")

**Zero tolerance for:**
- Missing BASIC stub (won't load)
- Wasting space (use SYS 2061, not 2064)
- Using BASIC/KERNAL zero page ($00-$8F)
- Unbalanced stack operations
- Unverified screenshots
- American spellings (except "program")

**Every 6510 assembly lesson must assemble, link, run, and display expected output verified with screenshots.**
