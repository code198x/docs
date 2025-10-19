# How To Not Fuck It Up - Quick Reference

**Purpose:** Single-page reminder for maintaining quality without fucking things up
**For:** Claude Code creating C64 lessons

---

## The Three Rules

### 1. Curriculum is Authority
**File:** `/CRITICAL-CURRICULUM-AUTHORITY.md` → `/docs/PHASE-0-CURRICULUM.md`

```
BEFORE editing lesson-NNN.mdx:
✅ Read PHASE-0-CURRICULUM.md for lesson N spec
✅ Compare existing lesson to spec
✅ If mismatch → ARCHIVE, don't edit

❌ NEVER edit lessons without checking curriculum first
```

### 2. Evidence Before Claims
**Skill:** `/docs/skills/c64-lesson-creation/SKILL.md`

```
BEFORE saying "lesson complete" or "code works":
✅ Run petcat and SHOW output
✅ Run ls and SHOW file listings
✅ Run grep and SHOW results
✅ Quote curriculum spec

❌ NEVER claim success without showing evidence
❌ NEVER say "should work" or "probably complete"
```

### 3. Load Smart, Not Hard
**File:** `/docs/START-HERE.md`

```
WHEN needing technical reference:
✅ Load START-HERE.md for navigation
✅ Load quick references (12-13KB each)
✅ Avoid comprehensive refs unless needed (80-90KB)

Quick References:
- CIA-QUICK-REFERENCE.md (joystick/keyboard)
- VIC-II-QUICK-REFERENCE.md (sprites/colors)
- 6510-QUICK-REFERENCE.md (assembly)
- PETSCII-AND-SCREEN-CODES.md (characters)

❌ NEVER load 6510-MICROPROCESSOR-REFERENCE.md, 6526-CIA-REFERENCE.md, or VIC-II-REFERENCE.md first
```

---

## The Lesson Creation Checklist

**Follow this or the lesson will have problems:**

### Phase 1: Curriculum Verification
```
[ ] Read CRITICAL-CURRICULUM-AUTHORITY.md
[ ] Read PHASE-0-CURRICULUM.md lesson N specification
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
[ ] Create .bas files in /code-samples/.../lesson-NNN/
[ ] NO indentation (line numbers flush left)
[ ] Lowercase keywords in .bas files
[ ] British English in comments (colour, learnt)
[ ] Run petcat compilation: petcat -w2 -o example-1.prg -- example-1.bas
[ ] SHOW petcat output (verify exit code 0)
```

### Phase 4: Screenshots
```
[ ] Create screenshot directory if needed
[ ] Run x64sc with -exitscreenshot flag
[ ] Run ls to SHOW screenshot files exist
[ ] SHOW file sizes
```

### Phase 5: Lesson MDX
```
[ ] Read lesson-007.mdx or lesson-008.mdx for structure
[ ] Create lesson-NNN.mdx with proper sections
[ ] UPPERCASE keywords in MDX display
[ ] NO indentation in code blocks
[ ] British English throughout
[ ] Use "program" not "programme" for computer programs
[ ] NO "Insight" blocks or "WOW Moment" sections
```

### Phase 6: Final Verification
```
[ ] Re-read curriculum spec and quote it
[ ] Re-run petcat on all .bas files, show output
[ ] ls code samples directory, show files
[ ] ls screenshots directory, show files
[ ] grep for American spellings: grep -i "color\|behavior\|favorite"
[ ] Verify all formatting rules
[ ] ONLY THEN claim "lesson complete"
```

---

## Red Flags - STOP IMMEDIATELY

| If you're about to... | STOP and... |
|----------------------|-------------|
| Edit lesson without checking curriculum | Read CRITICAL-CURRICULUM-AUTHORITY.md |
| Say "code should work" | Run petcat and show output |
| Say "lesson complete" | Show evidence for all 6 phases |
| Load 80KB+ reference file | Load START-HERE.md instead |
| Claim "screenshots captured" | Run ls and show file sizes |
| Use American English | Use British (but "program" for software) |
| Indent BASIC code | Remove indentation (BASIC V2 requirement) |
| Say "verified formatting" | Run grep and show results |

---

## Common Fuckups and Fixes

### Fuckup: Curriculum Drift
**Symptom:** Lesson teaches wrong concept
**Cause:** Edited lesson without checking PHASE-0-CURRICULUM.md
**Fix:** Archive mismatched lesson, start from curriculum spec

### Fuckup: Broken Code
**Symptom:** BASIC program doesn't run
**Cause:** Didn't compile with petcat
**Fix:** Run petcat, fix syntax errors, show success

### Fuckup: Missing Files
**Symptom:** Screenshots or code samples don't exist
**Cause:** Didn't verify with ls
**Fix:** Run ls for all locations, show output

### Fuckup: Wrong English
**Symptom:** "Color" instead of "Colour"
**Cause:** Didn't grep for American spellings
**Fix:** Run grep, replace with British English
**Exception:** "program" is correct for computer programs

### Fuckup: Wrong Formatting
**Symptom:** Indented BASIC code
**Cause:** Didn't follow BASIC V2 rules
**Fix:** Remove ALL indentation, line numbers flush left

### Fuckup: Context Bloat
**Symptom:** Loading 80-90KB reference files
**Cause:** Didn't use START-HERE.md navigation
**Fix:** Load START-HERE.md, use quick references

---

## Quick Command Reference

**Verify curriculum alignment:**
```bash
grep -A 5 "Lesson N:" /Users/stevehill/Projects/Code198x/docs/PHASE-0-CURRICULUM.md
```

**Compile BASIC:**
```bash
cd /code-samples/commodore-64/phase-0/tier-1/lesson-NNN/
petcat -w2 -o example-1.prg -- example-1.bas
```

**Capture screenshot:**
```bash
x64sc -autostart example-1.prg \
      -limitcycles 20000000 \
      -VICIIdsize \
      -exitscreenshot /website/public/images/commodore-64/phase-0/tier-1/lesson-NNN/example-1.png \
      +sound
```

**Verify files exist:**
```bash
ls -lh /code-samples/commodore-64/phase-0/tier-1/lesson-NNN/
ls -lh /website/public/images/commodore-64/phase-0/tier-1/lesson-NNN/
```

**Check for American English:**
```bash
grep -i "color\|behavior\|favorite" lesson-NNN.mdx
```

---

## File Locations Quick Map

```
Workflow Skill:
  /docs/skills/c64-lesson-creation/SKILL.md    ← READ THIS FOR LESSON WORK

Authority Files:
  /CRITICAL-CURRICULUM-AUTHORITY.md             ← Read before ANY lesson edit
  /docs/PHASE-0-CURRICULUM.md                   ← The authoritative spec

Navigation:
  /docs/START-HERE.md                           ← Find the right reference

Quick References (load these):
  /docs/CIA-QUICK-REFERENCE.md                  ← 12KB (joystick/keyboard)
  /docs/VIC-II-QUICK-REFERENCE.md              ← 13KB (sprites/colors)
  /docs/6510-QUICK-REFERENCE.md                ← 13KB (assembly)
  /docs/PETSCII-AND-SCREEN-CODES.md            ← 12KB (characters)

Comprehensive References (avoid unless needed):
  /docs/6510-MICROPROCESSOR-REFERENCE.md       ← 85KB (hardware specs)
  /docs/6526-CIA-REFERENCE.md                  ← 107KB (hardware specs)
  /docs/VIC-II-REFERENCE.md                    ← 87KB (hardware specs)

Lesson Files:
  /website/src/pages/commodore-64/phase-0/tier-1/lesson-NNN.mdx
  /code-samples/commodore-64/phase-0/tier-1/lesson-NNN/example-N.bas
  /website/public/images/commodore-64/phase-0/tier-1/lesson-NNN/example-N.png
```

---

## The One-Sentence Summary

**Read the skill, follow every step, show evidence for each claim, or the lesson will have problems.**

---

**This document exists because lessons were previously created "by luck and judgment" and had:**
- ✗ Broken code that doesn't compile
- ✗ Missing screenshots
- ✗ Wrong concepts (curriculum drift)
- ✗ American English
- ✗ Indented BASIC code
- ✗ No evidence of verification

**Follow this guide and that won't happen.**

---

**Version:** 1.0.0
**Created:** 2025-10-18
**Purpose:** Single-page "don't fuck it up" reminder
