# Lesson Pre-Flight Checklist

**PURPOSE:** Prevent working on lessons that don't match curriculum specification.
**WHEN TO USE:** Before editing ANY lesson file.
**MANDATORY:** This checklist MUST be completed before touching lesson content.

---

## ⚠️ CRITICAL RULE

**Before editing lesson-NNN.mdx:**
1. Read PHASE-0-CURRICULUM.md specification for that lesson number
2. Compare current lesson title/objectives to curriculum spec
3. If mismatch → STOP and consult this checklist

**DO NOT edit lessons that don't match curriculum without explicit approval.**

---

## Step 1: Curriculum Verification

Read the curriculum specification:

```bash
# Check what the curriculum says for this lesson
grep -A 10 "Lesson $LESSON_NUM:" /Users/stevehill/Projects/Code198x/docs/PHASE-0-CURRICULUM.md
```

**Required fields from curriculum:**
- [ ] Lesson title matches curriculum spec exactly
- [ ] Main concept matches curriculum spec
- [ ] WOW moment matches curriculum spec

---

## Step 2: Alignment Check

Compare current lesson to curriculum spec:

| Aspect | Curriculum Says | Current Lesson Has | Match? |
|--------|----------------|-------------------|--------|
| Title | [from curriculum] | [from lesson frontmatter] | ✅/❌ |
| Main Concept | [from curriculum] | [from lesson body] | ✅/❌ |
| WOW Moment | [from curriculum] | [from lesson] | ✅/❌ |

**If ANY field shows ❌:**
- **STOP immediately**
- Do NOT edit the lesson
- Proceed to Step 3 (Decision)

---

## Step 3: Decision Matrix

### Scenario A: Complete Mismatch (❌❌❌)

**Current lesson does NOT match curriculum at all.**

**Action:**
1. Rename current file to `lesson-NNN-OLD.mdx.bak`
2. Move to `/website/src/pages/commodore-64/phase-0/tier-1/_archive/`
3. Create new lesson from curriculum spec
4. Document in commit: "Replaced lesson-NNN with curriculum-aligned version"

**Example:**
```bash
# Current: "Sound Off" (SID programming)
# Curriculum: "The First Color" (VIC-II/POKE)
# Action: Archive old, write new
```

### Scenario B: Partial Match (✅❌✅ or similar)

**Some elements match, but key concepts differ.**

**Action:**
1. Create detailed comparison in issue/PR description
2. Extract reusable code examples from current lesson
3. Archive current lesson as in Scenario A
4. Write new lesson incorporating reusable elements
5. Document salvaged elements in commit message

**Example:**
```bash
# Current: "Counting" teaches FOR...NEXT
# Curriculum: "Counting" teaches Variables
# Action: Extract FOR content for later lesson, rewrite with variables
```

### Scenario C: Strong Match (✅✅✅ with minor differences)

**Core concept and WOW moment match, minor variations only.**

**Action:**
1. Document differences in commit message
2. Edit lesson to align with curriculum spec
3. Keep existing structure and examples if they support curriculum goals
4. Mark as "curriculum-aligned" in commit

**Example:**
```bash
# Current: "Hello, Computer" - PRINT, GOTO, infinite scroll
# Curriculum: "Hello, Computer" - PRINT, GOTO, infinite scroll
# Action: Minor edits to improve clarity, keep core content
```

---

## Step 4: Before-Edit Checklist

Only proceed with editing if you answer YES to ALL:

- [ ] I have read the curriculum spec for this lesson number
- [ ] The current lesson matches curriculum (Scenario C only)
- [ ] OR I have archived the mismatched lesson (Scenarios A/B)
- [ ] I know what WOW moment should be in this lesson
- [ ] I have checked docs/TIER-1-CURRICULUM-REVIEW.md for guidance
- [ ] I will NOT introduce concepts from old lesson that don't belong here

---

## Step 5: Post-Edit Verification

After editing, verify:

- [ ] Lesson title matches `PHASE-0-CURRICULUM.md`
- [ ] Main concept taught matches curriculum
- [ ] WOW moment matches curriculum specification
- [ ] No orphaned concepts from previous version
- [ ] Frontmatter objectives align with curriculum
- [ ] Code examples support curriculum goals (not old curriculum)

### Step 5A: Code Validation (MANDATORY)

**All `.bas` files MUST pass validation before committing:**

```bash
# Validate each example
./scripts/validate-bas.sh code-samples/.../lesson-NNN/example-1.bas
./scripts/validate-bas.sh code-samples/.../lesson-NNN/example-2.bas
```

**Validation checks:**
- ✅ petcat syntax validation (tokenization)
- ✅ C64 BASIC V2 semantic correctness
- ✅ Hardware register addresses
- ✅ POKE value ranges (0-255)
- ⚠️  Sprite boundary warnings (non-blocking)

**What validation catches:**
- `RESTORE 10` → Error (should be bare `RESTORE`)
- `POKE 53280,300` → Error (value >255)
- Unsupported BASIC features (DO, WHILE, PROC)
- Invalid hardware addresses

**See `/scripts/README.md` for detailed validation documentation.**

**Required before commit:**
- [ ] All `.bas` files validated successfully
- [ ] No validation errors (warnings are OK)
- [ ] PRG files regenerated after any fixes

---

## Emergency Procedures

### If You Already Edited Wrong Content

**You accidentally edited a mismatched lesson:**

1. **STOP** committing/pushing
2. Check git status: `git status`
3. If uncommitted: `git restore lesson-NNN.mdx`
4. If committed: `git revert HEAD` or `git reset --soft HEAD^`
5. Return to Step 1 of this checklist
6. Follow proper alignment decision (Scenarios A/B/C)

### If You Discover Drift Mid-Session

**You realize partway through that lesson doesn't match curriculum:**

1. **STOP immediately**
2. Document what was changed: `git diff lesson-NNN.mdx > /tmp/drift-changes.diff`
3. Revert changes: `git restore lesson-NNN.mdx`
4. Review `/tmp/drift-changes.diff` - salvage any universally useful edits (typos, clarity)
5. Follow proper alignment procedure from Step 3
6. Apply salvaged edits only if they support curriculum version

---

## Reference Quick Links

- **Curriculum Spec:** `/Users/stevehill/Projects/Code198x/docs/PHASE-0-CURRICULUM.md`
- **Alignment Review:** `/Users/stevehill/Projects/Code198x/docs/TIER-1-CURRICULUM-REVIEW.md`
- **Archive Location:** `/Users/stevehill/Projects/Code198x/website/src/pages/commodore-64/phase-0/tier-1/_archive/`

---

## Validation Commands

```bash
# Before editing lesson 7
LESSON_NUM=7
CURRICULUM_FILE="/Users/stevehill/Projects/Code198x/docs/PHASE-0-CURRICULUM.md"
LESSON_FILE="/Users/stevehill/Projects/Code198x/website/src/pages/commodore-64/phase-0/tier-1/lesson-007.mdx"

# What does curriculum say?
echo "=== CURRICULUM SAYS ==="
grep -A 5 "Lesson $LESSON_NUM:" $CURRICULUM_FILE

# What does current lesson say?
echo "=== CURRENT LESSON SAYS ==="
head -20 $LESSON_FILE | grep -E "title:|objectives:"

# Do they match?
echo "=== VERIFY MATCH BEFORE PROCEEDING ==="
```

---

## Commit Message Templates

### Scenario A (Complete Rewrite):
```
rewrite(tier-1): Replace lesson-NNN with curriculum-aligned version

Previous lesson taught [OLD TOPIC], curriculum specifies [NEW TOPIC].
Archived old content to _archive/lesson-NNN-OLD.mdx.bak.

Implements curriculum spec:
- Title: [CURRICULUM TITLE]
- Concept: [MAIN CONCEPT]
- WOW: [WOW MOMENT]

Refs: docs/PHASE-0-CURRICULUM.md line XX
```

### Scenario B (Partial Salvage):
```
rewrite(tier-1): Rewrite lesson-NNN to match curriculum, salvage examples

Previous lesson had [OVERLAP] but wrong focus on [WRONG THING].
Extracted reusable code: [LIST EXAMPLES KEPT].
Archived old content to _archive/.

Implements curriculum spec:
- Title: [CURRICULUM TITLE]
- Concept: [MAIN CONCEPT]
- WOW: [WOW MOMENT]
- Reused: [WHAT WAS KEPT]

Refs: docs/PHASE-0-CURRICULUM.md line XX
```

### Scenario C (Minor Alignment):
```
fix(tier-1): Align lesson-NNN with curriculum specification

Lesson already teaches correct concept, minor adjustments:
- [CHANGE 1]
- [CHANGE 2]

Now fully matches curriculum spec.

Refs: docs/PHASE-0-CURRICULUM.md line XX
```

---

**Remember:** When in doubt, archive and rewrite. Preserving incorrect content causes more work than starting fresh.
