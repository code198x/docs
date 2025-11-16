---
name: zx-lesson-creation  
description: Use when creating or editing ZX Spectrum BASIC lessons - enforces platform-specific compilation, validation, screenshot capture, and Sinclair BASIC requirements
---

# ZX Spectrum BASIC Lesson Creation

## Overview

This skill guides creation of ZX Spectrum Sinclair BASIC lessons. Key differences from C64 BASIC: mandatory LET keyword, PRINT AT y,x (not x,y), ULA graphics (attribute-based colour), BEEP sound (no sound chip), case-insensitive, .tap file format.

## When to Use

- Creating/editing ZX Spectrum BASIC lessons
- **NOT** for Z80 assembly (use zx-z80-lesson-creation)

## Prerequisites

1. **lesson-creation-workflow skill**
2. **Curriculum:** `/docs/curriculum/sinclair-zx-spectrum-curriculum.md`
3. **Tools:** zmakebas compiler, FUSE emulator, Python 3 validator

## ZX Spectrum BASIC Rules

### 1. Case-Insensitive Keywords

```basic
✓ CORRECT (any case works):
10 PRINT "HELLO"
10 print "hello"
10 Print "Hello"

✗ C64-style lowercase in .bas not required
```

### 2. Mandatory LET Keyword

```basic
✓ CORRECT:
10 LET SCORE=0
20 LET X=X+1

✗ WRONG:
10 SCORE=0     ← Syntax error without LET
```

### 3. PRINT AT (Note Order: Y,X)

```basic
✓ CORRECT:
10 PRINT AT 10,5;"HELLO"  ; Row 10, Column 5

✗ WRONG:
10 PRINT AT 5,10;"HELLO"  ; Backwards!
```

### 4. Colour System (INK/PAPER/BORDER)

```basic
10 BORDER 0        ; Black border
20 PAPER 7         ; White paper (background)
30 INK 2           ; Red ink (foreground)
40 PRINT "HELLO"   ; Red text on white
```

**Colours: 0-7 only** (not 0-15 like C64)

### 5. BEEP for Sound

```basic
10 BEEP duration,pitch
20 BEEP 0.5,10    ; 0.5 sec, pitch 10
```

**No SID chip - BEEP only!**

## Required Files Checklist

- [ ] `/website/src/pages/sinclair-zx-spectrum/phase-X/tier-Y/lesson-NNN.mdx`
- [ ] `/code-samples/sinclair-zx-spectrum/phase-X/tier-Y/lesson-NNN/example-1.bas`
- [ ] `/code-samples/sinclair-zx-spectrum/phase-X/tier-Y/lesson-NNN/example-1.tap` (compiled)
- [ ] `/website/public/images/sinclair-zx-spectrum/phase-X/tier-Y/lesson-NNN/screenshot-1.png`

## Compilation Process

```bash
cd /code-samples/sinclair-zx-spectrum/phase-X/tier-Y/lesson-NNN/

# Compile to .tap
zmakebas -o example-1.tap -n LESSON example-1.bas

# -n LESSON = Program name shown in ZX menu
```

**Semantic validation:**
```bash
python3 /scripts/validate-zx-basic.py example-1.bas
```

**Checks:**
- LET keyword present for assignments
- PRINT AT order (y,x not x,y)
- Colours 0-7 range
- Screen coordinates (32×24 characters)
- PEEK/POKE addresses valid for ZX

## Screenshot Capture (FUSE - Manual Only)

**FUSE emulator resists automation - manual capture required:**

```bash
# Load ROM
fuse example-1.tap

# Media → Screenshot
# Save to /website/public/images/sinclair-zx-spectrum/.../screenshot-1.png
```

**Verify with READ tool after capture.**

## ZX-Specific Validation

### Memory Map

| Range | Purpose | Writable |
|-------|---------|----------|
| $4000-$57FF | Screen RAM | ✓ |
| $5800-$5AFF | Attribute RAM (colour) | ✓ |
| $5B00-$FFFF | User RAM | ✓ |

**Screen:** 256×192 pixels, 32×24 characters
**Attributes:** 8×8 pixel blocks, INK/PAPER/BRIGHT/FLASH

### ULA Port ($FE)

```basic
OUT 254,value   ; Border colour + speaker
```

**Bits:**
- 0-2: Border colour
- 3: MIC (cassette)
- 4: Speaker (BEEP)

## Anti-Patterns

### 1. Missing LET

**Anti-pattern:**
```basic
10 X=5     ← Syntax error!
```

**Fix:**
```basic
10 LET X=5
```

### 2. PRINT AT Order Wrong

**Anti-pattern:**
```basic
10 PRINT AT 5,10;"X"  ; Column 5, Row 10 - backwards!
```

**Fix:**
```basic
10 PRINT AT 10,5;"X"  ; Row 10, Column 5
```

### 3. Using C64 Colour Codes

**Anti-pattern:**
```basic
10 INK 14  ; Only 0-7 valid!
```

**Fix:**
```basic
10 INK 6   ; Use 0-7 range
```

### 4. Wasting Memory

**Principle: Don't waste space**
- ZX Spectrum 48K has limited RAM
- Keep code tight, no unnecessary padding
- Use space-efficient algorithms

## Complete Workflow Checklist

1. **Preparation:** Read curriculum, create directories
2. **Code Creation:** Write .bas with LET, compile with zmakebas
3. **Screenshot:** Manual capture with FUSE
4. **Lesson MDX:** Create with uppercase keywords for display
5. **Validation:** Run all validation skills
6. **File Verification:** ls all locations
7. **Navigation Update:** Update tier/phase/platform indexes

## Quick Reference

### Compilation
```bash
zmakebas -o example-1.tap -n LESSON example-1.bas
```

### Screenshot
```bash
fuse example-1.tap
# Media → Screenshot (manual)
```

### Key Differences from C64
- LET mandatory
- PRINT AT y,x (not x,y)
- Colours 0-7 (not 0-15)
- BEEP (no SID chip)
- Case-insensitive

### Common Addresses
```basic
16384  REM Screen start ($4000)
22528  REM Attributes start ($5800)
254    REM ULA port (border/sound)
```

## Common Mistakes

1. **Missing LET** - Syntax error
2. **PRINT AT backwards** - Wrong coordinates
3. **Colour out of range** - Only 0-7
4. **Expecting SID chip** - Use BEEP only
5. **C64-style lowercase** - Not required, any case works

## Platform-Specific Resources

**Essential quick references** (in `/docs/platforms/sinclair-zx-spectrum/language/`):
- `ZX-SPECTRUM-BASIC-QUICK-REFERENCE.md` - BASIC commands, syntax
- `ZX-SPECTRUM-MEMORY-AND-GRAPHICS-REFERENCE.md` - ULA, memory map, graphics

**Common errors documentation:**
- `/docs/platforms/sinclair-zx-spectrum/ZX-COMMON-ERRORS.md` - BASIC pitfalls
- `/docs/platforms/sinclair-zx-spectrum/Z80-COMMON-ERRORS.md` - Assembly pitfalls

## The Bottom Line

**ZX Spectrum BASIC lessons require:**
1. zmakebas compilation to .tap
2. LET keyword for all assignments
3. PRINT AT y,x order (row first)
4. Colours 0-7 range
5. FUSE manual screenshot capture
6. Space-efficient code (48K RAM limit)
7. British English (except "program")

**Zero tolerance for:**
- Missing LET keyword
- Wrong PRINT AT order
- Colour values > 7
- Unverified screenshots
- American spellings (except "program")

**Every ZX BASIC lesson must compile to .tap, run in FUSE, and display expected output verified with manual screenshots.**
