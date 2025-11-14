---
name: curriculum-alignment-check
description: Use when validating lesson matches curriculum specification - reads phase/tier curriculum docs, compares lesson content systematically, reports mismatches with archive-vs-fix decision guidance
---

# Curriculum Alignment Check

## Overview

Every lesson must align with its curriculum specification. Misaligned lessons get archived, not edited. Read curriculum FIRST, before creating or validating lessons.

## When to Use

Use when:
- Creating new lesson (read curriculum spec FIRST)
- Validating existing lesson
- Reviewing lesson changes
- Part of lesson validation workflow
- Investigating why lesson seems "off"

**Critical:** If lesson doesn't match curriculum, ARCHIVE IT. Don't edit to force alignment.

## Finding Curriculum Specifications

### File Path Pattern

```
/docs/{platform}/PHASE-{N}-CURRICULUM.md
```

**Examples:**
- `/docs/commodore-64/PHASE-0-CURRICULUM.md`
- `/docs/sinclair-zx-spectrum/PHASE-0-CURRICULUM.md`
- `/docs/nintendo-entertainment-system/PHASE-1-CURRICULUM.md`

### Structured Curricula (Phase 0 ZX Spectrum, some others)

Some curricula use granular structure:
```
/docs/{platform}/phase-{N}/tier-{N}/README.md
/docs/{platform}/phase-{N}/tier-{N}/lesson-NNN.md
```

**Check top-level PHASE file first** - it indicates if detailed structure exists.

## Alignment Checklist

**Use TodoWrite to track each item:**

### 1. Locate Curriculum Spec
- [ ] Find PHASE-{N}-CURRICULUM.md for platform
- [ ] If structured, find tier-{N}/README.md
- [ ] Read lesson specification for lesson number

### 2. Core Alignment
- [ ] **Title** - Matches curriculum lesson title?
- [ ] **Arc Position** - Lesson in correct arc (e.g., Arc 1: Number Challenge)?
- [ ] **Game/Concept** - Teaching the specified game or concept?
- [ ] **Primary Commands** - Using commands curriculum specifies?

### 3. Concept Coverage
- [ ] **Concepts Listed** - Curriculum lists specific concepts (loops, variables, INPUT)?
- [ ] **Lesson Covers** - Does lesson actually teach those concepts?
- [ ] **Concept Order** - Introduces concepts in curriculum sequence?

### 4. Code Complexity
- [ ] **Line Count Range** - Curriculum specifies range (e.g., 5-60 lines)?
- [ ] **Code Matches** - Example code within expected range?
- [ ] **Complexity Level** - Appropriate for tier/lesson position?

### 5. Prerequisites
- [ ] **Prior Knowledge** - Curriculum lists prerequisites?
- [ ] **Lesson Assumes** - Does lesson assume only prior prerequisites?
- [ ] **No Forward References** - Doesn't use concepts from future lessons?

## Alignment Report Format

```
CURRICULUM ALIGNMENT CHECK: Lesson {NNN}

Platform: {platform}
Phase: {N}
Tier: {N}
Curriculum Spec: {file path}

=== ALIGNMENT ANALYSIS ===

Title:
  Curriculum: "{expected title}"
  Lesson:     "{actual title}"
  Status:     [MATCH / MISMATCH]

Arc Position:
  Curriculum: {arc name and number}
  Lesson:     {inferred from content}
  Status:     [MATCH / MISMATCH]

Game/Concept:
  Curriculum: {what should be taught}
  Lesson:     {what is actually taught}
  Status:     [MATCH / MISMATCH]

Primary Commands:
  Curriculum: {expected commands}
  Lesson:     {commands actually used}
  Status:     [MATCH / MISMATCH]

Concepts Covered:
  Expected:   {list from curriculum}
  Actual:     {list from lesson}
  Status:     [MATCH / PARTIAL / MISMATCH]

Code Complexity:
  Expected:   {line range from curriculum}
  Actual:     {actual line count}
  Status:     [MATCH / MISMATCH]

=== VERDICT ===

Alignment: [ALIGNED / PARTIALLY ALIGNED / MISALIGNED]

Issues:
  - {list each mismatch with severity}

Recommendation: [ACCEPT / ARCHIVE]
Reason: {explanation}
```

## Decision Tree

### If ALIGNED
- ✅ Lesson matches curriculum on all key aspects
- **Action:** Proceed with validation

### If PARTIALLY ALIGNED
- ⚠️ Minor mismatches (e.g., slightly different emphasis, code length off by 10%)
- **Consider:** Is curriculum spec flexible? Is this acceptable variation?
- **Action:** User decides (document decision)

### If MISALIGNED
- ❌ Major mismatches (wrong game, wrong concept, wrong arc)
- **Action:** ARCHIVE lesson, don't edit
  - Move to `_archive/lesson-NNN-OLD.mdx.bak`
  - Create new lesson following curriculum
- **Never:** Try to force-fit lesson to curriculum by heavy editing

## Why Archive Instead of Edit?

From project policy (CLAUDE.md):

> If lesson doesn't match curriculum → ARCHIVE IT, don't edit it.

**Reasons:**
1. Misaligned lesson teaches wrong concepts in wrong order
2. Heavy editing = essentially rewriting = might as well start fresh
3. Archived lesson preserves work if curriculum changes
4. Forces curriculum-first approach

## Common Mistakes

**Mistake 1:** Writing lesson without reading curriculum
- **Fix:** Read curriculum spec BEFORE writing any code or lesson content

**Mistake 2:** "Close enough" thinking
- **Fix:** Use checklist systematically. Document partial alignment.

**Mistake 3:** Editing misaligned lesson to force alignment
- **Fix:** Archive it. Start fresh following curriculum.

**Mistake 4:** Assuming curriculum from lesson number
- **Fix:** Read actual curriculum doc. Lesson numbers can be deceptive.

**Mistake 5:** Checking only title, ignoring concepts
- **Fix:** Use complete checklist. Verify all aspects.

## Quick Reference

```bash
# Find curriculum spec
ls docs/{platform}/PHASE-{N}-CURRICULUM.md

# If structured:
ls docs/{platform}/phase-{N}/tier-{N}/README.md
cat docs/{platform}/phase-{N}/tier-{N}/lesson-NNN.md

# Check lesson file
cat website/src/pages/{platform}/phase-{N}/tier-{N}/lesson-{NNN}.mdx

# Compare systematically using checklist above
```

## Red Flags - Stop and Check Curriculum

If you find yourself:
- Writing lesson without knowing what curriculum says
- Saying "I'll check curriculum later"
- Editing heavily to match curriculum
- Assuming lesson is aligned based on number/title
- Skipping checklist items

**STOP. Read curriculum first. Use checklist.**

## The Bottom Line

**Read curriculum FIRST. Check systematically. If misaligned, archive it.**

Curriculum is authoritative. Lesson must match. No exceptions.
