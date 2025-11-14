---
name: lesson-creation-workflow
description: Use when creating any new lesson - provides complete step-by-step workflow from planning through validation to navigation updates, ensuring all files created in correct locations and all quality checks passed
---

# Lesson Creation Workflow

## Overview

Creating a lesson requires following a specific workflow to ensure all files are created, validated, and navigation updated. Skipping steps causes missing files and broken links.

**MANDATORY:** Use TodoWrite to track progress through all steps.

## When to Use

Use when:
- Creating a new lesson from scratch
- Following platform-specific lesson creation skill
- Ensuring complete lesson workflow
- Student asks to create a lesson

## Complete Workflow

### Step 1: Lesson Planning

**Identify lesson details:**
- Platform (c64, zx-spectrum, nes, amiga)
- Phase number
- Tier number
- Lesson number
- Game/concept being taught

**Check curriculum:**
Read `/docs/{platform}/PHASE-{N}-CURRICULUM.md` for lesson specification.

**Create TodoWrite checklist:**
```
- [ ] Step 1: Lesson Planning
- [ ] Step 2: Code Development
- [ ] Step 3: Validation (MANDATORY)
- [ ] Step 4: Lesson Writing
- [ ] Step 5: File Organization
- [ ] Step 6: Update Navigation
- [ ] Step 7: Quality Verification
```

### Step 2: Code Development

**Write code** following platform conventions:
- C64 BASIC: lowercase keywords in .bas, flush left
- ZX Spectrum: platform-specific conventions
- NES: assembly with proper mapper
- Amiga: 68K assembly

**File naming:**
```
example-1.bas
example-2.bas
(etc.)
```

**Compile and test in emulator.**

### Step 3: Validation (MANDATORY)

**REQUIRED SUB-SKILLS:**
- Use **lesson-validation** skill for complete validation
- Use **screenshot-verification** skill for screenshots

**Do NOT skip validation.**

### Step 4: Lesson Writing

**Create MDX file** at:
```
/website/src/pages/{platform}/phase-{N}/tier-{N}/lesson-{NNN}.mdx
```

**Frontmatter required:**
```yaml
---
layout: ../../../../layouts/LessonLayout.astro
title: "Lesson Title"
---
```

**Follow lesson archetype:**
- Discovery (Tier 1): Guided exploration
- Challenge: Problem-solving
- Synthesis: Combining concepts
- Deep Dive: Technical depth

**Voice & tone:**
- British English (colour, learnt, whilst)
- Exception: "program" for computer programs
- Playful but rigorous
- No marketing speak

### Step 5: File Organization

**Verify all files in correct locations:**

**Code samples:**
```
/code-samples/{platform}/phase-{N}/tier-{N}/lesson-{NNN}/
  ├── example-1.bas
  ├── example-1.prg
  ├── example-2.bas
  └── example-2.prg
```

**Screenshots:**
```
/website/public/images/{platform}/phase-{N}/tier-{N}/lesson-{NNN}/
  ├── example-1.png
  └── example-2.png
```

**Lesson file:**
```
/website/src/pages/{platform}/phase-{N}/tier-{N}/lesson-{NNN}.mdx
```

**Check with ls:**
```bash
ls -la code-samples/{platform}/phase-{N}/tier-{N}/lesson-{NNN}/
ls -la website/public/images/{platform}/phase-{N}/tier-{N}/lesson-{NNN}/
ls website/src/pages/{platform}/phase-{N}/tier-{N}/lesson-{NNN}.mdx
```

### Step 6: Update Navigation/Overview Files

**CRITICAL:** Navigation updates are NOT optional.

**Files to update:**

**a) Tier Index:**
```
/website/src/pages/{platform}/phase-{N}/tier-{N}/index.astro
```

Add lesson to lessons array:
```javascript
{
  number: NNN,
  title: "Lesson Title",
  description: "Brief description",
  status: "available"
}
```

**b) Phase Index (if first lesson in new tier):**
```
/website/src/pages/{platform}/phase-{N}/index.astro
```

Add tier entry if new tier.

**c) Platform Overview (if first lesson in new phase):**
```
/website/src/pages/{platform}/index.astro
```

Add phase entry if new phase.

**d) Homepage (if significant milestone):**
```
/website/src/pages/index.mdx
```

Update if milestone (e.g., Phase 1 Tier 1 complete).

**Verify navigation:**
Check that lesson is linked from tier index.

### Step 7: Quality Verification

**Run preflight checklist** (if exists):
```
/docs/LESSON-PREFLIGHT-CHECKLIST.md
```

**Final checks:**
- [ ] Code compiles
- [ ] Semantic validation passed
- [ ] Screenshots verified
- [ ] British English checked
- [ ] All files in correct locations
- [ ] Navigation updated
- [ ] Links work

**Mark TodoWrite complete.**

## File Naming Conventions

**Lesson numbers:**
- 001-016: Tier 1
- 017-032: Tier 2
- etc.

**Always zero-padded:** `lesson-007.mdx` not `lesson-7.mdx`

**Screenshots match examples:** `example-1.png` for `example-1.bas`

## Platform-Specific Workflows

**C64 BASIC:**
- Follow `/docs/skills/c64-lesson-creation/SKILL.md`
- Use petcat for compilation
- VICE x64sc for screenshots

**ZX Spectrum:**
- Follow `/docs/skills/zx-lesson-creation/SKILL.md`
- Use zmakebas / sjasmplus
- Fuse for screenshots

**NES:**
- Follow `/docs/skills/nes-lesson-creation/SKILL.md`
- Use ca65/ld65
- FCEUX for screenshots

**Amiga:**
- Follow `/docs/skills/amiga-lesson-creation/SKILL.md`
- Use vasm
- FS-UAE for screenshots

## Common Mistakes

**Mistake 1:** Skipping navigation updates
- **Impact:** Lesson not discoverable on website
- **Fix:** Always update tier/phase/platform indexes

**Mistake 2:** Wrong file locations
- **Impact:** Broken links, build failures
- **Fix:** Follow file organization structure exactly

**Mistake 3:** Skipping validation
- **Impact:** Broken code, incorrect screenshots
- **Fix:** Use lesson-validation skill (mandatory)

**Mistake 4:** Not using TodoWrite
- **Impact:** Forgotten steps, incomplete lessons
- **Fix:** Create checklist at start, track progress

**Mistake 5:** Inconsistent file naming
- **Impact:** Navigation breaks, files not found
- **Fix:** Use zero-padded numbers (001, 007, 016)

## Red Flags - Skipped Steps

If you:
- Create lesson without updating navigation
- Skip validation because "code looks correct"
- Don't check all file locations
- Forget to track progress with TodoWrite
- Move to next lesson before this one complete

**STOP. Complete current lesson workflow first.**

## Quick Reference

```
1. Plan → Read curriculum spec
2. Code → Write, compile, test
3. Validate → Use lesson-validation skill
4. Write → Create MDX with frontmatter
5. Organize → Verify all file locations
6. Navigate → Update tier/phase/platform indexes
7. Verify → Run final checks

Use TodoWrite throughout.
```

## Workflow Diagram

```
Planning
  ↓
Code Development
  ↓
Validation (MANDATORY) ←──┐
  ↓ PASS                  │
Lesson Writing            │
  ↓                       │
File Organization         │
  ↓                       │
Navigation Updates        │
  ↓                       │
Quality Verification ─────┘
  ↓ PASS
COMPLETE
```

## The Bottom Line

**Follow all steps. Update navigation. Validate everything.**

Navigation updates aren't optional. Validation isn't optional.

Use TodoWrite. Complete one lesson before starting next.
