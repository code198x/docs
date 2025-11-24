---
name: zx-z80-lesson-creation
description: Use when creating or editing ZX Spectrum Z80 Assembly lessons - provides platform-specific compilation, validation, and screenshot capture for Phase 3 of the content creation workflow
---

# ZX Spectrum Z80 Assembly Lesson Creation

**Role:** Technical execution for Phase 3 (Validation) of the Content Creation Workflow.

**Prerequisite:** Read `/docs/CONTENT-CREATION-WORKFLOW.md` first. This skill provides Z80-specific technical details, not the full workflow.

---

## When to Use

Use this skill during **Phase 3 (Validation)** when:
- Assembling Z80 code with sjasmplus
- Capturing screenshots with FUSE emulator
- Validating Z80 instruction usage
- Checking for ZX-specific pitfalls

**Do NOT use for:**
- ZX Spectrum BASIC lessons (use `basic-lesson-creation` skill)
- Other platforms (use platform-specific skills)

---

## Z80 Assembly Rules (NOT 6502!)

### Registers

- **8-bit:** A, B, C, D, E, H, L, I, R
- **16-bit pairs:** BC, DE, HL, IX, IY, SP, PC
- **Shadow registers:** AF', BC', DE', HL'
- **Flags:** S, Z, H, P/V, N, C

### Key Instructions

```asm
LD A,0          ; Load A with 0
LD HL,$4000     ; Load HL with address
LD (HL),A       ; Store A to address in HL
INC HL          ; Increment HL
DJNZ loop       ; Decrement B, jump if not zero
CALL subroutine ; Call subroutine
RET             ; Return
OUT ($FE),A     ; Output to port
```

### No Hardware Sprites

**Unlike C64/NES, ZX has NO hardware sprites:**
- All sprites software-rendered
- Manual pixel plotting
- XOR for flicker-free movement
- Attribute handling separate

---

## Phase 3: Validation (Technical Details)

### Step 3.1: Assemble with sjasmplus

```bash
cd /code-samples/sinclair-zx-spectrum/phase-X/tier-Y/lesson-NNN/

# Assemble to .tap
sjasmplus example-1.asm --tap=example-1.tap
echo $?  # Must be 0
```

### Step 3.2: Semantic Validation

```bash
python3 /scripts/validate-zx-asm.py example-1.asm
```

**Checks:**
- ✅ Z80 instructions (not 6502)
- ✅ Screen memory ($4000-$57FF)
- ✅ Attribute memory ($5800-$5AFF)
- ✅ ULA port usage ($FE)
- ✅ Stack management

### Step 3.3: Screenshot Capture (FUSE - Manual)

```bash
fuse example-1.tap
```

1. Wait for program to run
2. Menu → Media → Screenshot
3. Save to `/website/public/images/sinclair-zx-spectrum/phase-X/tier-Y/lesson-NNN/screenshot-1.png`

### Step 3.4: Screenshot Verification (MANDATORY)

**Use Read tool to VIEW every screenshot:**

```
✅ CORRECT: "Read screenshot-1.png - shows black border, pixel pattern
   in centre, no error messages visible."

❌ WRONG: "Screenshot verified ✅" (too vague)
```

---

## Memory Map

| Range | Purpose |
|-------|---------|
| $4000-$57FF | Screen RAM (6144 bytes) |
| $5800-$5AFF | Attribute RAM (768 bytes) |
| $5B00-$FFFF | User RAM |

**Screen:** 256×192 pixels (non-linear layout!)
**Attributes:** 32×24 (8×8 pixel blocks)

---

## Common Pitfalls

### 1. Using 6502 Mnemonics
```asm
❌ WRONG: LDA #0          ; 6502 syntax!
✅ CORRECT: LD A,0        ; Z80 syntax
```

### 2. Assuming Hardware Sprites
```asm
❌ WRONG: ; Looking for sprite registers - none exist!
✅ CORRECT: ; Implement software sprite routine
```

### 3. Linear Screen Address Assumption
```asm
❌ WRONG: INC HL         ; Next byte ≠ next scanline!
✅ CORRECT: ; Use proper scanline calculation
```

### 4. Not Using 16-bit Operations
```asm
❌ WRONG:
    LD A,H : ADD A,4 : LD H,A  ; Clumsy

✅ CORRECT:
    LD BC,4 : ADD HL,BC        ; Native 16-bit
```

---

## Z80 vs 6502 Quick Comparison

| Feature | 6502 | Z80 |
|---------|------|-----|
| Registers | A, X, Y | A, B, C, D, E, H, L |
| 16-bit | No native | BC, DE, HL pairs |
| Load | LDA | LD A, |
| Store | STA | LD (addr),A |
| Call | JSR | CALL |
| Return | RTS | RET |

---

## Required Files

| File | Location |
|------|----------|
| Lesson MDX | `/website/src/pages/sinclair-zx-spectrum/phase-X/tier-Y/lesson-NNN.mdx` |
| Source (.asm) | `/code-samples/sinclair-zx-spectrum/phase-X/tier-Y/lesson-NNN/example-1.asm` |
| Tape (.tap) | `/code-samples/sinclair-zx-spectrum/phase-X/tier-Y/lesson-NNN/example-1.tap` |
| Screenshot | `/website/public/images/sinclair-zx-spectrum/phase-X/tier-Y/lesson-NNN/screenshot-1.png` |

---

## Quick Reference Commands

```bash
# Assemble
sjasmplus example-1.asm --tap=example-1.tap

# Semantic validation
python3 /scripts/validate-zx-asm.py example-1.asm

# Screenshot (manual)
fuse example-1.tap
# Media → Screenshot
```

---

## Platform-Specific Resources

**Quick references** (in `/docs/platforms/sinclair-zx-spectrum/`):
- `language/Z80-QUICK-REFERENCE.md` - Instruction set
- `language/ZX-SPECTRUM-MEMORY-AND-GRAPHICS-REFERENCE.md` - ULA, memory

**Common errors:**
- `Z80-COMMON-ERRORS.md` - Assembly pitfalls

---

## The Bottom Line

**This skill provides:** Assembly, validation, and screenshot capture for Z80 lessons.

**The main workflow provides:** Planning, creation, integration, and publication steps.

**Zero tolerance for:**
- 6502 syntax (wrong processor!)
- Assuming hardware sprites (none exist)
- Unverified screenshots
