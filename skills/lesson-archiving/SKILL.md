---
name: lesson-archiving
description: Use when archiving mismatched lessons - enforces systematic archiving process with navigation updates, git history preservation, and documentation
---

# Lesson Archiving

## Overview

This skill guides systematic archiving of lessons that no longer align with curriculum specifications. Archiving preserves the lesson (and git history) while removing it from active navigation. Used when curriculum-alignment-check detects mismatch or when lessons are replaced/deprecated.

## When to Use

Use when:
- curriculum-alignment-check detects curriculum mismatch
- Lesson needs replacement with curriculum-aligned version
- Lesson deprecated (curriculum changed)
- Lesson superseded by better version

**Do NOT use when:**
- Lesson just needs minor edits (use Edit tool)
- Lesson matches curriculum (no archiving needed)
- Lesson has temporary issues (fix, don't archive)

---

## Archiving Decision Tree

**START: curriculum-alignment-check detects mismatch**

```
Does lesson match curriculum spec?
├─ YES → No archiving needed, keep lesson
└─ NO → Continue to archiving decision

Can lesson be fixed to match curriculum?
├─ YES → Edit lesson, don't archive
└─ NO → Archive lesson

Why can't it be fixed?
├─ Teaches wrong concept → ARCHIVE (create new aligned lesson)
├─ Wrong tier/phase placement → ARCHIVE (relocate to correct tier)
├─ Curriculum changed → ARCHIVE (lesson now obsolete)
└─ Superseded by better lesson → ARCHIVE (replacement exists)
```

**Golden rule: If lesson teaches different concept than curriculum specifies, ARCHIVE IT.**

---

## Archiving Process

### Step 1: Verify Archiving Decision

**Before archiving, confirm:**

- [ ] curriculum-alignment-check ran and detected mismatch
- [ ] Lesson cannot be edited to match curriculum
- [ ] Archiving reason is clear and documented
- [ ] Replacement plan exists (if applicable)

**If unsure, consult curriculum document and strategic alignment.**

### Step 2: Document Archiving Reason

**Create archive log entry:**

```bash
# Location: /docs/LESSON-ARCHIVE-LOG.md

## Lesson {Platform} Phase {N} Tier {N} Lesson {NNN} - {YYYY-MM-DD}

**Reason:** {curriculum-mismatch|deprecated|replaced|relocated}

**Details:**
- Curriculum spec: {what curriculum says}
- Lesson teaches: {what lesson actually teaches}
- Mismatch: {specific mismatch description}

**Action:** Archived to `_archive/lesson-{NNN}-{date}.mdx.bak`

**Replacement:** {planned|exists at lesson-XXX|none}
```

**Example:**
```markdown
## Lesson C64 Phase 0 Tier 1 Lesson 012 - 2025-11-05

**Reason:** curriculum-mismatch

**Details:**
- Curriculum spec: "Joystick input basics"
- Lesson teaches: "Keyboard input"
- Mismatch: Wrong input method entirely

**Action:** Archived to `_archive/lesson-012-20251105.mdx.bak`

**Replacement:** New joystick lesson to be created
```

### Step 3: Create Archive Directory

**If not exists:**

```bash
mkdir -p /website/src/pages/{platform}/phase-{N}/tier-{N}/_archive/
```

**Archive directory naming:**
- Always `_archive` (leading underscore prevents routing)
- One per tier
- Preserves all archived lessons for that tier

### Step 4: Move Lesson File

**Rename with timestamp and .bak extension:**

```bash
# From:
/website/src/pages/{platform}/phase-{N}/tier-{N}/lesson-{NNN}.mdx

# To:
/website/src/pages/{platform}/phase-{N}/tier-{N}/_archive/lesson-{NNN}-{YYYYMMDD}.mdx.bak
```

**Naming convention:**
- Original lesson number preserved
- ISO date (YYYYMMDD) added
- `.bak` extension (prevents accidental rendering)

**Example:**
```bash
mv /website/src/pages/commodore-64/phase-0/tier-1/lesson-012.mdx \
   /website/src/pages/commodore-64/phase-0/tier-1/_archive/lesson-012-20251105.mdx.bak
```

**Git commit message:**
```bash
git add website/src/pages/commodore-64/phase-0/tier-1/_archive/lesson-012-20251105.mdx.bak
git commit -m "Archive lesson 012: curriculum mismatch (keyboard vs joystick)

Curriculum spec requires joystick input, lesson teaches keyboard.
Archived for replacement with curriculum-aligned joystick lesson.

See LESSON-ARCHIVE-LOG.md for details."
```

### Step 5: Remove from Navigation

**Update tier index:**

```bash
# Edit: /website/src/pages/{platform}/phase-{N}/tier-{N}.astro

# Remove lesson from lessons array
lessons: [
  { number: 11, title: "...", description: "...", status: "available" },
  // { number: 12, ... }  ← Remove or comment out
  { number: 13, title: "...", description: "...", status: "available" },
]
```

**Git commit:**
```bash
git add website/src/pages/commodore-64/phase-0/tier-1.astro
git commit -m "Remove archived lesson 012 from navigation

Lesson archived due to curriculum mismatch.
Navigation gap at lesson 012 will be filled by replacement."
```

### Step 6: Handle Code Samples (Optional)

**Decision: Archive or delete?**

**Archive code samples if:**
- Code might be useful reference
- Uncertain if replacement will reuse code
- Git history preservation desired

**Delete code samples if:**
- Code fundamentally wrong
- Replacement will be completely different
- No future reference value

**To archive:**
```bash
mv /code-samples/{platform}/phase-{N}/tier-{N}/lesson-{NNN}/ \
   /code-samples/{platform}/phase-{N}/tier-{N}/_archive/lesson-{NNN}-{YYYYMMDD}/
```

**To delete:**
```bash
rm -rf /code-samples/{platform}/phase-{N}/tier-{N}/lesson-{NNN}/

git add -A
git commit -m "Remove code samples for archived lesson 012

Code samples no longer align with curriculum.
Replacement lesson will have new code samples."
```

### Step 7: Handle Screenshots (Optional)

**Same decision as code samples: archive or delete.**

**To archive:**
```bash
mv /website/public/images/{platform}/phase-{N}/tier-{N}/lesson-{NNN}/ \
   /website/public/images/{platform}/phase-{N}/tier-{N}/_archive/lesson-{NNN}-{YYYYMMDD}/
```

**To delete:**
```bash
rm -rf /website/public/images/{platform}/phase-{N}/tier-{N}/lesson-{NNN}/
```

### Step 8: Update Archive Log

**Add entry to `/docs/LESSON-ARCHIVE-LOG.md`:**

```bash
# Append entry (created in Step 2)
git add docs/LESSON-ARCHIVE-LOG.md
git commit -m "Log archiving of lesson 012 to LESSON-ARCHIVE-LOG.md"
```

### Step 9: Verify Archiving Complete

**Checklist:**

- [ ] Lesson MDX moved to `_archive/` with `.bak` extension
- [ ] Navigation updated (lesson removed from tier index)
- [ ] Archive log entry created
- [ ] Git commits made (separate commits for each step)
- [ ] Code samples archived/deleted (documented in log)
- [ ] Screenshots archived/deleted (documented in log)
- [ ] Replacement plan documented (if applicable)

---

## Git Best Practices

### Separate Commits for Each Step

**Don't bundle everything into one commit:**

```bash
# WRONG: Single commit
git add -A
git commit -m "Archived lesson 012"
```

**CORRECT: Separate commits**

```bash
# Commit 1: Archive lesson
git add website/src/pages/.../tier-1/_archive/lesson-012-20251105.mdx.bak
git commit -m "Archive lesson 012: curriculum mismatch"

# Commit 2: Update navigation
git add website/src/pages/.../tier-1.astro
git commit -m "Remove archived lesson 012 from navigation"

# Commit 3: Log archiving
git add docs/LESSON-ARCHIVE-LOG.md
git commit -m "Log archiving of lesson 012"
```

**Why:** Separate commits preserve history and make reversion easier.

### Preserve Git History

**Always use `git mv` or `git add` after `mv`:**

```bash
# CORRECT:
mv lesson-012.mdx _archive/lesson-012-20251105.mdx.bak
git add _archive/lesson-012-20251105.mdx.bak
git commit -m "Archive lesson 012"

# Git tracks file move, preserves history
```

**Don't delete then create:**

```bash
# WRONG:
rm lesson-012.mdx
# create new file in _archive/
git add _archive/lesson-012-20251105.mdx.bak

# Git loses history connection!
```

---

## Archive Log Format

**Location:** `/docs/LESSON-ARCHIVE-LOG.md`

**Structure:**

```markdown
# Lesson Archive Log

This document logs all archived lessons with reasons and replacement plans.

**Archive criteria:**
- Curriculum mismatch (lesson teaches different concept than curriculum spec)
- Deprecated (curriculum changed, lesson obsolete)
- Replaced (better lesson created, old one superseded)
- Relocated (lesson moved to different tier/phase)

---

## [Platform] Phase [N] Tier [N] Lesson [NNN] - [YYYY-MM-DD]

**Reason:** {curriculum-mismatch|deprecated|replaced|relocated}

**Details:**
- Curriculum spec: {what curriculum says}
- Lesson teaches: {what lesson actually teaches}
- Mismatch: {specific description}

**Action:** Archived to `_archive/lesson-{NNN}-{YYYYMMDD}.mdx.bak`

**Code samples:** {archived|deleted|reason}

**Screenshots:** {archived|deleted|reason}

**Replacement:** {planned|exists at lesson-XXX|none|not needed}

**Git commits:**
- {commit hash}: Archive lesson
- {commit hash}: Update navigation
- {commit hash}: Log entry

---

{Next entry...}
```

---

## Common Scenarios

### Scenario 1: Curriculum Mismatch

**Situation:** Lesson teaches keyboard input, curriculum specifies joystick.

**Action:**
1. Archive lesson (curriculum mismatch)
2. Remove from navigation
3. Log with "Replacement: planned"
4. Create new joystick lesson following curriculum

### Scenario 2: Curriculum Changed

**Situation:** Phase curriculum revised, lesson no longer in scope.

**Action:**
1. Archive lesson (deprecated)
2. Remove from navigation
3. Log with "Replacement: none (out of scope)"
4. No new lesson needed

### Scenario 3: Better Lesson Created

**Situation:** New lesson covers same concept better.

**Action:**
1. Archive old lesson (replaced)
2. Remove from navigation
3. Log with "Replacement: exists at lesson-XXX"
4. New lesson already in place

### Scenario 4: Wrong Tier Placement

**Situation:** Lesson in Tier 1, should be Tier 2.

**Action:**
1. Archive lesson (relocated)
2. Remove from Tier 1 navigation
3. Create new lesson in Tier 2
4. Log with "Replacement: relocated to phase-X/tier-Y/lesson-ZZZ"

---

## Anti-Patterns

### 1. Deleting Without Archiving

**Anti-pattern:**
```bash
rm lesson-012.mdx
git add lesson-012.mdx
git commit -m "Removed lesson 012"
```

**Why wrong:** Loses file content and history.

**Fix:** Archive first, preserve history.

### 2. Editing Mismatched Lesson

**Anti-pattern:**
```bash
# Lesson teaches keyboard, curriculum says joystick
# Edit lesson to add joystick code alongside keyboard
```

**Why wrong:** Lesson becomes hybrid, doesn't match curriculum.

**Fix:** Archive old lesson, create new joystick-only lesson.

### 3. Not Updating Navigation

**Anti-pattern:**
```bash
# Archive lesson but leave in tier index
# Users see lesson 012 in navigation → 404 error
```

**Fix:** Always update navigation when archiving.

### 4. Not Logging Reason

**Anti-pattern:**
```bash
git commit -m "Archived lesson 012"
# No context, future confusion
```

**Fix:** Log detailed reason in LESSON-ARCHIVE-LOG.md.

### 5. Bundling Multiple Archives

**Anti-pattern:**
```bash
# Archive lessons 012, 015, 018 in one commit
```

**Fix:** Archive each lesson separately with individual commits and log entries.

---

## Integration with Other Skills

**This skill is called by:**

1. **curriculum-alignment-check** - Detects mismatch, recommends archiving
2. **curriculum-audit-agent** - Identifies mismatched lessons at scale

**After archiving:**

1. **lesson-creation-agent** - Create replacement lesson if needed
2. **navigation-update-agent** - Verify navigation consistency

---

## Quick Reference

### Archive Commands
```bash
# Create archive directory
mkdir -p .../_archive/

# Move lesson
mv lesson-{NNN}.mdx _archive/lesson-{NNN}-{YYYYMMDD}.mdx.bak

# Git commit
git add _archive/lesson-{NNN}-{YYYYMMDD}.mdx.bak
git commit -m "Archive lesson {NNN}: {reason}"

# Update navigation
# Edit tier-N.astro, remove lesson entry
git add tier-N.astro
git commit -m "Remove archived lesson {NNN} from navigation"

# Log archiving
# Append to LESSON-ARCHIVE-LOG.md
git add LESSON-ARCHIVE-LOG.md
git commit -m "Log archiving of lesson {NNN}"
```

### Archive Log Template
```markdown
## {Platform} Phase {N} Tier {N} Lesson {NNN} - {YYYY-MM-DD}

**Reason:** {curriculum-mismatch|deprecated|replaced|relocated}

**Details:**
- Curriculum spec: ...
- Lesson teaches: ...
- Mismatch: ...

**Action:** Archived to `_archive/lesson-{NNN}-{YYYYMMDD}.mdx.bak`

**Replacement:** {planned|exists|none}
```

---

## The Bottom Line

**Lesson archiving preserves history while removing mismatched lessons:**
1. Archive to `_archive/lesson-{NNN}-{YYYYMMDD}.mdx.bak`
2. Remove from navigation
3. Log reason in LESSON-ARCHIVE-LOG.md
4. Separate git commits for each step
5. Preserve git history (use `git add` after `mv`)

**Zero tolerance for:**
- Deleting without archiving (loses history)
- Editing mismatched lessons (doesn't fix mismatch)
- Not updating navigation (broken links)
- Not logging reason (future confusion)
- Bundling multiple archives (unclear history)

**When curriculum-alignment-check says "ARCHIVE IT" - follow this skill systematically. Archiving is not failure - it's curriculum maintenance.**
