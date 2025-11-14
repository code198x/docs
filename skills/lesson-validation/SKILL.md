---
name: lesson-validation
description: Use when validating a lesson before publication - runs mandatory compilation, semantic validators, British English checks, and screenshot verification to ensure lesson meets quality standards
---

# Lesson Validation

## Overview

Every lesson must pass automated validation before publication. Manual inspection is insufficient - you must run the actual validation tools and report their output.

## When to Use

Use this skill when:
- Validating a newly created lesson
- Checking lesson changes before commit
- Verifying lesson meets publication standards
- Debugging lesson issues

**Do NOT skip validation** because lesson "looks correct" or you're "confident it works."

## Validation Checklist

**Use TodoWrite to track these steps:**

### 1. Code Compilation
**Must pass for EVERY code file.**

**C64 BASIC:**
```bash
petcat -w2 -o output.prg -- input.bas
```

**ZX Spectrum BASIC:**
```bash
zmakebas -o output.tap input.bas
```

**NES Assembly:**
```bash
ca65 input.s -o input.o
ld65 input.o -C nes.cfg -o output.nes
```

**Failure = lesson not ready.** Fix compilation errors first.

### 1b. Roundtrip Validation (C64 BASIC only)
**Must verify committed .prg matches fresh compilation.**

**Why needed:** Ensures .prg files in git are valid and match source .bas files.

```bash
# Compile fresh .prg from .bas
petcat -w2 -o fresh.prg -- input.bas

# Compare with committed .prg
diff committed.prg fresh.prg

# Should output nothing (files identical)
```

**If diff shows differences:** Committed .prg is stale or corrupted. Replace with freshly compiled version.

**Example:**
```bash
cd code-samples/commodore-64/phase-0/tier-1/lesson-007/
petcat -w2 -o fresh-example-1.prg -- example-1.bas
diff example-1.prg fresh-example-1.prg
# Output: (nothing) = files match ✓
```

### 2. Semantic Validation
**Must run platform-specific validator.**

**C64 BASIC:**
```bash
python3 scripts/validate-c64-basic.py code-samples/path/to/file.bas
```

Checks:
- RESTORE syntax (no line numbers in C64 BASIC V2)
- POKE values >255
- Invalid register addresses
- Sprite boundary violations

**ZX Spectrum Assembly:**
```bash
python3 scripts/validate-z80-asm.py code-samples/path/to/file.asm
```

**NES Assembly:**
```bash
python3 scripts/validate-nes-asm.py code-samples/path/to/file.s
```

**Report validator output.** If errors, fix before proceeding.

### 3. British English Check
**Must run grep for American spellings.**

```bash
grep -i "color\|program" /path/to/lesson.mdx
```

**Check results:**
- "color" → Should be "colour" (unless in code context)
- "program" is CORRECT for computer programs
- Look for: "learned" (should be "learnt"), "optimize" (should be "optimise")

**Exception:** "program" when referring to computer programs is always correct.

### 4. Screenshot Verification
**Must verify screenshot exists AND content matches.**

```bash
ls -la website/public/images/{platform}/phase-{N}/tier-{N}/lesson-{NNN}/*.png
```

**Then use READ tool:**
- View the screenshot
- Verify it shows what lesson claims
- Check for error messages or blank screens
- Confirm output matches code example

**Screenshot must show working program output, not errors.**

### 5. File Location Verification
**Must verify all files in correct locations.**

**Required files:**
- Code: `/code-samples/{platform}/phase-{N}/tier-{N}/lesson-{NNN}/`
- Lesson: `/website/src/pages/{platform}/phase-{N}/tier-{N}/lesson-{NNN}.mdx`
- Screenshot: `/website/public/images/{platform}/phase-{N}/tier-{N}/lesson-{NNN}/`

```bash
ls -la code-samples/{platform}/phase-{N}/tier-{N}/lesson-{NNN}/
ls -la website/src/pages/{platform}/phase-{N}/tier-{N}/lesson-{NNN}.mdx
ls -la website/public/images/{platform}/phase-{N}/tier-{N}/lesson-{NNN}/
```

**All locations must exist.** Missing files = validation fails.

## Validation Report Template

After running all checks, report:

```
VALIDATION REPORT: Lesson {NNN}

1. Code Compilation: [PASS/FAIL]
   - Command: [exact command run]
   - Output: [compilation output]

2. Roundtrip Validation (C64 BASIC only): [PASS/FAIL/N/A]
   - Command: [exact diff command run]
   - Output: [diff output or "files match"]

3. Semantic Validation: [PASS/FAIL]
   - Command: [exact command run]
   - Output: [validator output]

4. British English: [PASS/FAIL]
   - Issues found: [list any American spellings]

5. Screenshot Verification: [PASS/FAIL]
   - Files exist: [YES/NO]
   - Content verified: [description of what screenshot shows]

6. File Locations: [PASS/FAIL]
   - All files present: [YES/NO]

OVERALL: [READY FOR PUBLICATION / NEEDS FIXES]
```

## Common Mistakes

**Mistake 1:** "I inspected the code and it looks correct"
- **Fix:** Run the actual compilation command. Show output.

**Mistake 2:** "The code should compile fine"
- **Fix:** "Should" means nothing. Compile it. Show results.

**Mistake 3:** "I visually checked for American spellings"
- **Fix:** Run grep. Manual inspection misses things.

**Mistake 4:** "Screenshot exists"
- **Fix:** Use READ tool. Verify content matches lesson claims.

**Mistake 5:** Skipping validation because "simple lesson"
- **Fix:** Simple lessons have errors too. Run all checks.

## Red Flags - Manual Inspection Instead of Automation

If you find yourself:
- Saying "looks correct" without running commands
- Claiming validation passed without showing output
- Skipping steps because "confident"
- Visual inspection instead of running scripts

**STOP. Run the actual validation tools.**

## Platform-Specific Commands

| Platform | Compilation | Semantic Validator | Screenshot Method |
|----------|-------------|-------------------|-------------------|
| **C64 BASIC** | `petcat -w2 -o out.prg -- in.bas` | `validate-c64-basic.py` | VICE x64sc with -exitscreenshot |
| **ZX Spectrum BASIC** | `zmakebas -o out.tap in.bas` | `validate-zx-basic.py` | Fuse with F12 screenshot |
| **NES Assembly** | `ca65 + ld65` with nes.cfg | `validate-nes-asm.py` | FCEUX with lua script |
| **Amiga 68K Assembly** | `vasm` | `validate-68k-asm.py` | FS-UAE screenshot |

## Quick Reference

```bash
# Validate C64 BASIC lesson
petcat -w2 -o test.prg -- code.bas
petcat -w2 -o fresh.prg -- code.bas && diff committed.prg fresh.prg  # Roundtrip
python3 scripts/validate-c64-basic.py code.bas
grep -i "color\|learned\|optimize" lesson.mdx
ls -la website/public/images/.../lesson-NNN/*.png
# Use READ tool on screenshots

# Report all outputs, not just "passed"
```

## The Bottom Line

**Manual inspection ≠ validation.**

Run the tools. Show the output. Report results.

No shortcuts. No "looks good to me." Evidence only.
