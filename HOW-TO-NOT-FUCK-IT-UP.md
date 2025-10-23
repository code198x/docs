# How To Not Fuck It Up - Quick Reference

**Purpose:** Single-page reminder for maintaining quality without fucking things up
**For:** Claude Code creating C64 lessons

---

## The Three Rules

### 1. Specification is Authority
**Location:** `docs/{platform}/phase-{N}/tier-{N}/lesson-{NNN}.md` (or parent if not broken out yet)

```
BEFORE editing any lesson file:
✅ Locate lesson specification (individual → tier → phase → platform)
✅ Break out spec from parent document if needed
✅ Compare existing lesson to spec
✅ If mismatch → ARCHIVE, don't edit

❌ NEVER edit lessons without checking specification first
```

### 2. Evidence Before Claims
**Principle:** Show, don't tell

```
BEFORE saying "lesson complete" or "code works":
✅ Run compilation/validation and SHOW output
✅ Run ls and SHOW file listings
✅ Run grep and SHOW results
✅ Quote specification

❌ NEVER claim success without showing evidence
❌ NEVER say "should work" or "probably complete"
```

### 3. Load Smart, Not Hard
**Navigation:** `docs/START-HERE.md`

```
WHEN needing technical reference:
✅ Load START-HERE.md for navigation
✅ Load quick references first (smaller, focused)
✅ Avoid comprehensive refs unless needed (large, hardware-level detail)

Example - C64 Quick References:
- commodore-64/hardware/CIA-QUICK-REFERENCE.md (joystick/keyboard)
- commodore-64/hardware/VIC-II-QUICK-REFERENCE.md (sprites/colors)
- commodore-64/hardware/6510-QUICK-REFERENCE.md (assembly)
- commodore-64/hardware/PETSCII-AND-SCREEN-CODES.md (characters)

❌ NEVER load comprehensive references first (load quick refs instead)
```

---

## The Lesson Creation Checklist

**Follow this or the lesson will have problems:**

### Phase 1: Specification Verification
```
[ ] Locate lesson specification (individual → tier → phase → platform)
[ ] Break out from parent document if needed
[ ] Read lesson specification
[ ] Archive mismatched lesson OR proceed to edit
[ ] Create TodoWrite todos for all phases
```

### Phase 2: Reference Loading
```
[ ] Read START-HERE.md
[ ] Load only relevant quick references
[ ] Avoid comprehensive references
```

### Phase 3: Code Creation
```
[ ] Create code files in code-samples/{platform}/phase-{N}/tier-{N}/lesson-{NNN}/
[ ] Follow platform conventions (e.g., C64: no indentation, lowercase keywords)
[ ] Use appropriate language/style (e.g., British English for C64)
[ ] Run compilation/validation for platform
[ ] SHOW compilation output (verify success)
```

### Phase 4: Assets (Screenshots/Media)
```
[ ] Create asset directory if needed
[ ] Capture screenshots/media using platform tools
[ ] Run ls to SHOW asset files exist
[ ] SHOW file sizes
```

### Phase 5: Lesson Content
```
[ ] Read example lessons for platform structure
[ ] Create lesson file with proper sections
[ ] Follow platform display conventions (e.g., C64: UPPERCASE keywords, no indentation)
[ ] Follow language conventions (e.g., C64: British English, "program" for software)
[ ] Avoid deprecated patterns (e.g., "Insight" blocks)
```

### Phase 6: Final Verification
```
[ ] Re-read specification and quote it
[ ] Re-run compilation/validation on all code files, show output
[ ] ls code samples directory, show files
[ ] ls assets directory, show files
[ ] Run platform-specific checks (e.g., C64: grep for American spellings)
[ ] Verify all formatting rules
[ ] ONLY THEN claim "lesson complete"
```

---

## Red Flags - STOP IMMEDIATELY

| If you're about to... | STOP and... |
|----------------------|-------------|
| Edit lesson without checking spec | Locate and read lesson specification |
| Say "code should work" | Run compilation/validation and show output |
| Say "lesson complete" | Show evidence for all 6 phases |
| Load large reference file | Load START-HERE.md navigation first |
| Claim "assets captured" | Run ls and show file sizes |
| Break platform conventions | Check platform style guide/examples |
| Say "verified formatting" | Run checks and show results |

---

## Common Fuckups and Fixes

### Fuckup: Specification Drift
**Symptom:** Lesson teaches wrong concept
**Cause:** Edited lesson without checking specification
**Fix:** Archive mismatched lesson, start from specification

### Fuckup: Broken Code
**Symptom:** Program doesn't run
**Cause:** Didn't compile/validate with platform tools
**Fix:** Run compilation/validation, fix errors, show success

### Fuckup: Missing Files
**Symptom:** Assets or code samples don't exist
**Cause:** Didn't verify with ls
**Fix:** Run ls for all locations, show output

### Fuckup: Wrong Conventions
**Symptom:** Platform-specific conventions violated (e.g., C64: "Color" instead of "Colour")
**Cause:** Didn't follow platform style guide
**Fix:** Check platform conventions, run validation, fix issues

### Fuckup: Wrong Formatting
**Symptom:** Platform formatting rules violated (e.g., C64: indented BASIC code)
**Cause:** Didn't follow platform conventions
**Fix:** Check platform style guide, fix formatting

### Fuckup: Context Bloat
**Symptom:** Loading 80-90KB reference files
**Cause:** Didn't use START-HERE.md navigation
**Fix:** Load START-HERE.md, use quick references

---

## Platform-Specific Examples

### Commodore 64 Example Commands

**Locate specification:**
```bash
cat docs/commodore-64/phase-0/tier-1/lesson-007.md
```

**Compile BASIC:**
```bash
cd code-samples/commodore-64/phase-0/tier-1/lesson-NNN/
petcat -w2 -o example-1.prg -- example-1.bas
```

**Capture screenshot:**
```bash
x64sc -autostart example-1.prg \
      -limitcycles 20000000 \
      -VICIIdsize \
      -exitscreenshot website/public/images/commodore-64/phase-0/tier-1/lesson-NNN/example-1.png \
      +sound
```

**Verify files:**
```bash
ls -lh code-samples/commodore-64/phase-0/tier-1/lesson-NNN/
ls -lh website/public/images/commodore-64/phase-0/tier-1/lesson-NNN/
```

**Check British English:**
```bash
grep -i "color\|behavior\|favorite" lesson-NNN.mdx
```

---

## File Locations Structure

```
Navigation:
  docs/START-HERE.md                                    ← Find the right reference

Specifications (check in order):
  docs/{platform}/phase-{N}/tier-{N}/lesson-{NNN}.md  ← Individual lesson spec
  docs/{platform}/phase-{N}/tier-{N}/README.md         ← Tier overview
  docs/{platform}/PHASE-{N}-CURRICULUM.md              ← Phase curriculum

Technical References (platform-specific):
  docs/{platform}/hardware/*-QUICK-REFERENCE.md        ← Load these first
  docs/{platform}/hardware/*-REFERENCE.md              ← Comprehensive (avoid unless needed)

Content Files:
  website/src/pages/{platform}/phase-{N}/tier-{N}/lesson-{NNN}.{ext}
  code-samples/{platform}/phase-{N}/tier-{N}/lesson-{NNN}/
  website/public/images/{platform}/phase-{N}/tier-{N}/lesson-{NNN}/

Example (C64 Phase 0 Tier 1 Lesson 7):
  docs/commodore-64/phase-0/tier-1/lesson-007.md
  website/src/pages/commodore-64/phase-0/tier-1/lesson-007.mdx
  code-samples/commodore-64/phase-0/tier-1/lesson-007/
  website/public/images/commodore-64/phase-0/tier-1/lesson-007/
```

---

## The One-Sentence Summary

**Read the skill, follow every step, show evidence for each claim, or the lesson will have problems.**

---

**This document exists because lessons were previously created "by luck and judgment" and had:**
- ✗ Broken code that doesn't compile
- ✗ Missing assets
- ✗ Wrong concepts (specification drift)
- ✗ Platform conventions violated
- ✗ No evidence of verification

**Follow this guide and that won't happen.**

---

**Version:** 1.0.0
**Created:** 2025-10-18
**Purpose:** Single-page "don't fuck it up" reminder
