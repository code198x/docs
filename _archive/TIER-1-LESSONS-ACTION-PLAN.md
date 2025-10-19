# Tier 1 Lessons: Action Plan

**Date:** 2025-01-17
**Status:** DRIFT DETECTED - Corrective action required
**Authority:** PHASE-0-CURRICULUM.md

---

## Audit Results

### ✅ Lessons to KEEP (Curriculum-Aligned)

**Lesson 1: Hello, Computer**
- Status: ✅ Matches curriculum
- Action: None - keep as-is
- Reason: Title and content match PHASE-0-CURRICULUM.md

**Lesson 2: Counting**
- Status: ✅ Matches curriculum
- Action: None - our recent edits align with curriculum
- Reason: Variables and arithmetic match spec

**Lesson 3: Repeating Yourself**
- Status: ✅ Matches curriculum
- Action: None - our recent edits align with curriculum
- Reason: FOR...NEXT loops match spec

### ⚠️ Lessons to EDIT (Minor Misalignment)

**Lesson 4: Decisions, Decisions**
- Status: ⚠️ Content matches, title differs
- Curriculum: "Making Decisions"
- Current: "Decisions, Decisions"
- Action: Change title to match curriculum exactly
- Content: Keep - IF...THEN content is correct

### ❌ Lessons to ARCHIVE & REWRITE (Completely Misaligned)

**Lesson 5: Collections**
- Current: "Random Encounters" (RND, dice, treasure)
- Curriculum: "Collections" (Arrays with DIM, high score table)
- Status: ❌ Completely wrong topic
- Action: Archive → `/website/src/pages/commodore-64/phase-0/tier-1/_archive/lesson-005-random-encounters.mdx.bak`
- Rewrite: New lesson teaching arrays
- Salvage: RND content moves to future Lesson 13 (Random Events)

**Lesson 6: Data Everywhere**
- Current: "Simple Animation" (TI timing, cursor control, bouncing star)
- Curriculum: "Data Everywhere" (DATA, READ, RESTORE, quiz program)
- Status: ❌ Completely wrong topic
- Action: Archive → `_archive/lesson-006-simple-animation.mdx.bak`
- Rewrite: New lesson teaching DATA statements
- Salvage: Animation/TI content moves to future Lesson 15 (Timing)

**Lesson 7: The First Color**
- Current: "Sound Off" (SID chip, POKE, waveforms, ADSR)
- Curriculum: "The First Color" (POKE 53280/53281, VIC-II, rainbow border)
- Status: ❌ Completely wrong topic
- Action: Archive → `_archive/lesson-007-sound-off.mdx.bak`
- Rewrite: New lesson teaching VIC-II color control
- Salvage: Sound content moves to future Lessons 10-11 (First Sound / Sound Effects)

---

## Salvage Map

### Content to Preserve for Future Lessons

**From Lesson 5 (Random Encounters) → Future Lesson 13 (Random Events):**
- `RND(1)` function
- Seeding with `RND(-TI)`
- Dice rolling example
- Treasure hunt game structure

**From Lesson 6 (Simple Animation) → Future Lesson 15 (Timing):**
- `TI` jiffy clock explanation
- Frame-accurate timing with `TI`
- FOR...NEXT delay loops
- Bouncing star animation example
- Videos: `example-1.mp4`, `example-2.mp4`

**From Lesson 7 (Sound Off) → Future Lessons 10-11 (First Sound / Sound Effects):**
- SID register addresses (54272-54296)
- Volume, frequency, waveform basics
- Attack/Decay/Sustain/Release (ADSR)
- Triangle wave example code
- Working SID code with proper gate control
- Video: `example-1.mp4`

---

## Action Steps (In Order)

### Step 1: Create Archive Directory ✅
```bash
mkdir -p /Users/stevehill/Projects/Code198x/website/src/pages/commodore-64/phase-0/tier-1/_archive
```

### Step 2: Fix Lesson 4 Title
```bash
# Edit lesson-004.mdx frontmatter
# Change: title: "Decisions, Decisions"
# To: title: "Making Decisions"
```

### Step 3: Archive Misaligned Lessons
```bash
cd /Users/stevehill/Projects/Code198x/website/src/pages/commodore-64/phase-0/tier-1

# Archive Lesson 5
mv lesson-005.mdx _archive/lesson-005-random-encounters.mdx.bak

# Archive Lesson 6
mv lesson-006.mdx _archive/lesson-006-simple-animation.mdx.bak

# Archive Lesson 7
mv lesson-007.mdx _archive/lesson-007-sound-off.mdx.bak
```

### Step 4: Archive Associated Media
```bash
cd /Users/stevehill/Projects/Code198x/website/public/images/commodore-64/phase-0/tier-1

# Mark archived lesson media
mv lesson-005 lesson-005-ARCHIVED-random-encounters
mv lesson-006 lesson-006-ARCHIVED-simple-animation
mv lesson-007 lesson-007-ARCHIVED-sound-off
```

### Step 5: Archive Code Samples
```bash
cd /Users/stevehill/Projects/Code198x/code-samples/commodore-64/phase-0/tier-1

# Mark archived code
mv lesson-005 lesson-005-ARCHIVED-random-encounters
mv lesson-006 lesson-006-ARCHIVED-simple-animation
mv lesson-007 lesson-007-ARCHIVED-sound-off
```

### Step 6: Create Salvage Document
Create `/docs/SALVAGED-CONTENT.md` with extracted code examples and explanations for future use.

### Step 7: Write New Lessons
Follow PHASE-0-CURRICULUM.md exactly:

**New Lesson 5: Collections**
- Teach: DIM, array indexing
- WOW: High score table
- Reference: PHASE-0-CURRICULUM.md lines 36-39

**New Lesson 6: Data Everywhere**
- Teach: DATA, READ, RESTORE
- WOW: Quiz program
- Reference: PHASE-0-CURRICULUM.md lines 41-44

**New Lesson 7: The First Color**
- Teach: POKE 53280/53281, VIC-II intro
- WOW: Rainbow border animation
- Reference: PHASE-0-CURRICULUM.md lines 48-52

### Step 8: Validate New Lessons
Use `docs/LESSON-PREFLIGHT-CHECKLIST.md` before and after writing.

---

## Git Commit Strategy

### Commit 1: Create archive directory
```
chore(tier-1): Create _archive directory for curriculum realignment

Preparing to archive lessons that don't match PHASE-0-CURRICULUM.md.
See docs/TIER-1-LESSONS-ACTION-PLAN.md for details.
```

### Commit 2: Fix Lesson 4 title
```
fix(tier-1): Align lesson-004 title with curriculum

Changed "Decisions, Decisions" to "Making Decisions" to match
PHASE-0-CURRICULUM.md specification.

Refs: docs/PHASE-0-CURRICULUM.md line 31
```

### Commit 3: Archive misaligned lessons
```
refactor(tier-1): Archive lessons 5-7 for curriculum realignment

Moved to _archive/:
- lesson-005: "Random Encounters" → curriculum says "Collections"
- lesson-006: "Simple Animation" → curriculum says "Data Everywhere"
- lesson-007: "Sound Off" → curriculum says "The First Color"

Content salvaged in docs/SALVAGED-CONTENT.md for use in
future lessons (L10-11 sound, L13 random, L15 timing).

Refs: docs/TIER-1-CURRICULUM-REVIEW.md
Refs: docs/TIER-1-LESSONS-ACTION-PLAN.md
```

### Commit 4-6: New lessons
```
feat(tier-1): Implement lesson-005 per curriculum spec

New lesson "Collections" teaching arrays with DIM.
WOW moment: High score table.

Implements PHASE-0-CURRICULUM.md lines 36-39.
Replaces archived "Random Encounters" lesson.
```

---

## Prevention: Mandatory Checklist

**Before touching ANY lesson file:**
1. Read `docs/LESSON-PREFLIGHT-CHECKLIST.md`
2. Verify lesson matches `docs/PHASE-0-CURRICULUM.md`
3. If mismatch → archive first, then rewrite

**This incident occurred because we edited existing lessons without checking curriculum first.**

---

## Timeline

- **Completed:** Lessons 1-3 (curriculum-aligned)
- **Next:** Fix Lesson 4 title (5 minutes)
- **Then:** Archive Lessons 5-7 (10 minutes)
- **Then:** Write new Lessons 5-7 (6-9 hours)
- **After:** Continue with Lessons 8-16 using preflight checklist

---

## Success Criteria

✅ No lesson exists that doesn't match PHASE-0-CURRICULUM.md
✅ All salvaged content documented for future use
✅ LESSON-PREFLIGHT-CHECKLIST.md used before every edit
✅ Git history shows clear archive → rewrite process

---

**End of Action Plan**
