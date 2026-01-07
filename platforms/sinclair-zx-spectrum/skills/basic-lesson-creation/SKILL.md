---
name: zx-basic-unit-creation
description: Use when creating or editing ZX Spectrum BASIC units - provides platform-specific compilation, validation, and screenshot capture for Phase 3 of the content creation workflow
---

# ZX Spectrum BASIC Unit Creation

**Role:** Technical execution for Phase 3 (Validation) of the Content Creation Workflow.

**Prerequisite:** Read `/docs/CONTENT-CREATION-WORKFLOW.md` first. This skill provides ZX-specific technical details, not the full workflow.

---

## When to Use

Use this skill during **Phase 3 (Validation)** when:
- Compiling ZX Spectrum BASIC with zmakebas
- Capturing screenshots with FUSE emulator
- Validating Sinclair BASIC syntax
- Checking for ZX-specific pitfalls

**Do NOT use for:**
- Z80 Assembly units (use `z80-lesson-creation` skill)
- Other platforms (use platform-specific skills)

---

## Sinclair BASIC Rules

### 1. Mandatory LET Keyword

```basic
✓ CORRECT:
10 LET SCORE=0
20 LET X=X+1

✗ WRONG:
10 SCORE=0     ← Syntax error without LET
```

### 2. PRINT AT Order (Y,X - Row First!)

```basic
✓ CORRECT:
10 PRINT AT 10,5;"HELLO"  ; Row 10, Column 5

✗ WRONG:
10 PRINT AT 5,10;"HELLO"  ; Backwards!
```

### 3. Colours 0-7 Only (Not 0-15)

```basic
10 BORDER 0        ; Black border
20 PAPER 7         ; White paper
30 INK 2           ; Red ink

Colours: 0=black, 1=blue, 2=red, 3=magenta, 4=green, 5=cyan, 6=yellow, 7=white
```

### 4. BEEP for Sound (No Sound Chip)

```basic
10 BEEP duration,pitch
20 BEEP 0.5,10    ; 0.5 sec, pitch 10
```

### 5. Case-Insensitive

Any case works (unlike C64):
```basic
10 PRINT "HELLO"
10 print "hello"
10 Print "Hello"  ; All valid
```

---

## Phase 3: Validation (Technical Details)

### Step 3.1: Semantic Validation

```bash
cd /code-samples/sinclair-zx-spectrum/game-NN-{slug}/unit-NN/

python3 /scripts/validate-zx-basic.py example-1.bas
```

**Checks:**
- ✅ LET keyword present for assignments
- ✅ PRINT AT order (y,x not x,y)
- ✅ Colours 0-7 range
- ✅ Screen coordinates (32×24)
- ✅ PEEK/POKE addresses valid

### Step 3.2: Compilation (zmakebas)

```bash
zmakebas -o example-1.tap -n LESSON example-1.bas
echo $?  # Must be 0
```

**Flags:**
- `-o example-1.tap` = Output .tap file
- `-n LESSON` = Program name in ZX menu
- `example-1.bas` = Input source

### Step 3.3: Screenshot Capture (FUSE - Manual)

**FUSE resists automation - manual capture required:**

```bash
fuse example-1.tap
```

1. Wait for program to run
2. Menu → Media → Screenshot
3. Save to `/website/public/images/sinclair-zx-spectrum/game-NN-{slug}/unit-NN/screenshot-1.png`

### Step 3.4: Screenshot Verification (MANDATORY)

**Use Read tool to VIEW every screenshot:**

```
✅ CORRECT: "Read screenshot-1.png - shows blue border, white background,
   text 'SCORE: 100' at row 10. NO error messages visible."

❌ WRONG: "Screenshot verified ✅" (too vague)
```

**If ANY error found:** Fix code → Recompile → Recapture → Re-verify

---

## Memory Map

| Range | Decimal | Purpose |
|-------|---------|---------|
| $4000-$57FF | 16384-22527 | Screen RAM (bitmap) |
| $5800-$5AFF | 22528-23295 | Attribute RAM (colour) |
| $5B00-$FFFF | 23296-65535 | User RAM |

**Screen:** 256×192 pixels, 32×24 characters

**Attributes:** 8×8 pixel blocks with INK/PAPER/BRIGHT/FLASH

---

## ULA Port

```basic
OUT 254,value   ; Border colour + speaker
```

**Bits 0-2:** Border colour (0-7)
**Bit 4:** Speaker (BEEP)

---

## Common Pitfalls

### 1. Missing LET
```basic
❌ WRONG: 10 X=5       ; Syntax error!
✅ CORRECT: 10 LET X=5
```

### 2. PRINT AT Order Wrong
```basic
❌ WRONG: 10 PRINT AT 5,10;"X"   ; Column 5, Row 10 - backwards!
✅ CORRECT: 10 PRINT AT 10,5;"X" ; Row 10, Column 5
```

### 3. Colour Out of Range
```basic
❌ WRONG: 10 INK 14    ; Only 0-7 valid!
✅ CORRECT: 10 INK 6
```

### 4. Expecting SID Chip
```basic
❌ WRONG: OUT 54296,15  ; C64 SID volume - doesn't exist!
✅ CORRECT: BEEP 1,10   ; ZX uses BEEP only
```

---

## Required Files

| File | Location |
|------|----------|
| Unit MDX | `/website/src/pages/sinclair-zx-spectrum/game-MM-{slug}/unit-NN-{slug}.mdx` |
| Source (.bas) | `/code-samples/sinclair-zx-spectrum/game-MM-{slug}/unit-NN/example-1.bas` |
| Tape (.tap) | `/code-samples/sinclair-zx-spectrum/game-MM-{slug}/unit-NN/example-1.tap` |
| Screenshot | `/website/public/images/sinclair-zx-spectrum/game-MM-{slug}/unit-NN/screenshot-1.png` |

---

## Quick Reference Commands

```bash
# Semantic validation
python3 /scripts/validate-zx-basic.py example-1.bas

# Compile
zmakebas -o example-1.tap -n LESSON example-1.bas

# Screenshot (manual)
fuse example-1.tap
# Media → Screenshot
```

---

## Key Differences from C64

| Feature | C64 | ZX Spectrum |
|---------|-----|-------------|
| LET keyword | Optional | **Mandatory** |
| PRINT position | POKE cursor | PRINT AT y,x |
| Colours | 0-15 | 0-7 |
| Sound | SID chip | BEEP only |
| Case | Lowercase in .bas | Any case |
| Output format | .prg | .tap |

---

## Platform-Specific Resources

**Quick references** (in `/docs/platforms/sinclair-zx-spectrum/`):
- `language/ZX-SPECTRUM-BASIC-QUICK-REFERENCE.md` - Commands, syntax
- `language/ZX-SPECTRUM-MEMORY-AND-GRAPHICS-REFERENCE.md` - ULA, memory

**Common errors:**
- `ZX-COMMON-ERRORS.md` - BASIC pitfalls
- `Z80-COMMON-ERRORS.md` - Assembly pitfalls

---

## The Bottom Line

**This skill provides:** Compilation, validation, and screenshot capture for ZX BASIC units.

**The main workflow provides:** Planning, creation, integration, and publication steps.

**Zero tolerance for:**
- Missing LET keyword
- Wrong PRINT AT order (must be y,x)
- Colour values > 7
- Unverified screenshots
