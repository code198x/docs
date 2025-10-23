# Lesson Pre-Flight Checklist

**PURPOSE:** Prevent working on lessons that don't match curriculum specification.
**WHEN TO USE:** Before editing ANY lesson file.
**MANDATORY:** This checklist MUST be completed before touching lesson content.

---

## ⚠️ CRITICAL RULE

**Before editing any lesson file:**
1. Locate and read the lesson specification
2. Compare current lesson title/objectives to spec
3. If mismatch → STOP and consult this checklist

**DO NOT edit lessons that don't match curriculum without explicit approval.**

---

## Step 1: Locate Lesson Specification

Find the authoritative specification for the lesson you're editing:

**Specification Hierarchy (check in order):**

1. **Individual lesson spec** (most granular, preferred)
   - Location: `docs/{platform}/phase-{N}/tier-{N}/lesson-{NNN}.md`
   - Example: `docs/commodore-64/phase-0/tier-1/lesson-001.md`

2. **Tier overview spec** (if individual lesson spec doesn't exist yet)
   - Location: `docs/{platform}/phase-{N}/tier-{N}/README.md`
   - Contains specifications for all lessons in that tier
   - **Action needed:** Break out individual lesson spec before editing

3. **Phase curriculum spec** (if tier overview doesn't exist yet)
   - Location: `docs/{platform}/PHASE-{N}-CURRICULUM.md`
   - Contains specifications for all tiers/lessons in that phase
   - **Action needed:** Break out tier overview, then lesson spec before editing

4. **Platform overview** (if phase curriculum doesn't exist yet)
   - Location: `docs/{platform}/overview.md` or similar
   - **Action needed:** Create phase curriculum, tier overview, then lesson spec before editing

**If specification doesn't exist at ANY level:**
- **STOP** - Cannot edit lesson without specification
- Create specification hierarchy top-down before proceeding

---

## Step 2: Specification Verification

Read the lesson specification and verify required fields:

**Required fields from lesson spec:**
- [ ] Lesson title/name
- [ ] Learning objectives or key concepts
- [ ] Prerequisites (what students should know)
- [ ] Estimated completion or difficulty level

---

## Step 3: Alignment Check

Compare current lesson to specification:

| Aspect | Specification Says | Current Lesson Has | Match? |
|--------|-------------------|-------------------|--------|
| Title | [from spec] | [from lesson frontmatter] | ✅/❌ |
| Learning Objectives | [from spec] | [from lesson body] | ✅/❌ |
| Key Concepts | [from spec] | [from lesson] | ✅/❌ |

**If ANY field shows ❌:**
- **STOP immediately**
- Do NOT edit the lesson
- Proceed to Step 4 (Decision)

---

## Step 4: Decision Matrix

### Scenario A: Complete Mismatch (❌❌❌)

**Current lesson does NOT match curriculum at all.**

**Action:**
1. Rename current file to `lesson-NNN-OLD.{ext}.bak`
2. Move to appropriate archive directory (e.g., `_archive/` in same directory)
3. Create new lesson from specification
4. Document in commit: "Replaced lesson-NNN with spec-aligned version"

**Example:**
```bash
# Current: "Sound Off" (SID programming)
# Specification: "The First Color" (VIC-II/POKE)
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
# Specification: "Counting" teaches Variables
# Action: Extract FOR content for later lesson, rewrite with variables
```

### Scenario C: Strong Match (✅✅✅ with minor differences)

**Core concept and WOW moment match, minor variations only.**

**Action:**
1. Document differences in commit message
2. Edit lesson to align with specification
3. Keep existing structure and examples if they support spec goals
4. Mark as "spec-aligned" in commit

**Example:**
```bash
# Current: "Hello, Computer" - PRINT, GOTO, infinite scroll
# Specification: "Hello, Computer" - PRINT, GOTO, infinite scroll
# Action: Minor edits to improve clarity, keep core content
```

---

## Step 5: Before-Edit Checklist

Only proceed with editing if you answer YES to ALL:

- [ ] I have located and read the lesson specification
- [ ] If spec doesn't exist as individual file, I've broken it out from parent document
- [ ] The current lesson matches specification (Scenario C only)
- [ ] OR I have archived the mismatched lesson (Scenarios A/B)
- [ ] I know what key concepts should be in this lesson
- [ ] I will NOT introduce concepts from old lesson that don't belong here

---

## Step 6: Post-Edit Verification

After editing, verify:

- [ ] Lesson title matches specification
- [ ] Learning objectives match specification
- [ ] Key concepts match specification
- [ ] No orphaned concepts from previous version
- [ ] Frontmatter objectives align with specification
- [ ] Code examples support specification goals

### Step 6A: Code Validation (MANDATORY)

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

**Specification locations:**
- Individual lesson specs: `docs/{platform}/phase-{N}/tier-{N}/lesson-{NNN}.md`
- Tier overviews: `docs/{platform}/phase-{N}/tier-{N}/README.md`
- Phase curricula: `docs/{platform}/PHASE-{N}-CURRICULUM.md`

**Archive locations:**
- Typically: `_archive/` subdirectory in same location as lesson
- Or platform-specific archive structure

---

## Example Validation Workflow

```bash
# Example: Before editing C64 Phase 0 Tier 1 Lesson 7
PLATFORM="commodore-64"
PHASE="0"
TIER="1"
LESSON_NUM="007"

# Locate specification (try individual first, then tier, then phase)
SPEC_FILE="docs/${PLATFORM}/phase-${PHASE}/tier-${TIER}/lesson-${LESSON_NUM}.md"

if [ -f "$SPEC_FILE" ]; then
  echo "=== SPECIFICATION SAYS ==="
  cat "$SPEC_FILE"
else
  echo "Individual spec not found. Check tier README or phase curriculum."
  echo "Break out specification before editing lesson."
fi

# What does current lesson say?
LESSON_FILE="website/src/pages/${PLATFORM}/phase-${PHASE}/tier-${TIER}/lesson-${LESSON_NUM}.mdx"
echo "=== CURRENT LESSON SAYS ==="
head -30 "$LESSON_FILE"

# Verify match before proceeding
```

---

## Commit Message Templates

### Scenario A (Complete Rewrite):
```
rewrite({platform}/phase-{N}/tier-{N}): Replace lesson-NNN with spec-aligned version

Previous lesson taught [OLD TOPIC], specification requires [NEW TOPIC].
Archived old content to _archive/lesson-NNN-OLD.{ext}.bak.

Implements specification:
- Title: [SPEC TITLE]
- Objectives: [LEARNING OBJECTIVES]
- Key Concepts: [MAIN CONCEPTS]

Refs: docs/{platform}/phase-{N}/tier-{N}/lesson-{NNN}.md
```

### Scenario B (Partial Salvage):
```
rewrite({platform}/phase-{N}/tier-{N}): Rewrite lesson-NNN to match spec, salvage examples

Previous lesson had [OVERLAP] but wrong focus on [WRONG THING].
Extracted reusable code: [LIST EXAMPLES KEPT].
Archived old content to _archive/.

Implements specification:
- Title: [SPEC TITLE]
- Objectives: [LEARNING OBJECTIVES]
- Key Concepts: [MAIN CONCEPTS]
- Reused: [WHAT WAS KEPT]

Refs: docs/{platform}/phase-{N}/tier-{N}/lesson-{NNN}.md
```

### Scenario C (Minor Alignment):
```
fix({platform}/phase-{N}/tier-{N}): Align lesson-NNN with specification

Lesson already teaches correct concept, minor adjustments:
- [CHANGE 1]
- [CHANGE 2]

Now fully matches specification.

Refs: docs/{platform}/phase-{N}/tier-{N}/lesson-{NNN}.md
```

---

**Remember:** When in doubt, archive and rewrite. Preserving incorrect content causes more work than starting fresh.
