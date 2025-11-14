# Navigation Update Agent

**Type:** Autonomous multi-step execution agent
**Invoked via:** Task tool with `subagent_type: general-purpose`
**Priority:** P1 (High - needed frequently)
**Complexity:** Medium

---

## Purpose

Autonomously updates navigation files across all required levels when a new lesson is added:
- Tier index (always)
- Phase index (if first lesson in new tier)
- Platform index (if first lesson in new phase)
- Homepage (if significant milestone)

---

## What It Does

The agent updates navigation systematically:

1. **Reads lesson details** (number, title, description, platform, phase, tier)
2. **Updates tier index** - Adds lesson to lessons array
3. **Checks tier status** - If first lesson, updates phase index with new tier
4. **Checks phase status** - If first in phase, updates platform index
5. **Checks milestone status** - If significant (e.g., Phase 1 Tier 1 complete), updates homepage
6. **Verifies formatting** - Ensures consistent structure across all updated files
7. **Reports changes** - Lists all files modified with specific changes

---

## Input Required

**Lesson Details:**
- Platform (e.g., "sinclair-zx-spectrum")
- Phase number (e.g., 0, 1)
- Tier number (e.g., 1, 2)
- Lesson number (e.g., 1, 16)
- Lesson title (e.g., "Hello, Spectrum")
- Lesson description (1-2 sentences, max 150 characters)
- Lesson status ("available", "coming-soon", "draft")

**Example:**
```
Platform: sinclair-zx-spectrum
Phase: 0
Tier: 1
Lesson: 1
Title: "Hello, Spectrum"
Description: "Write your first program with an infinite counter using variables and PRINT AT positioning."
Status: available
```

---

## Decisions Agent Makes Autonomously

The agent makes these implementation decisions without asking:

1. **Update scope** - Determines which indexes need updating (tier always, phase/platform/home conditionally)
2. **Description formatting** - Ensures description is concise and consistent
3. **Status badge** - Uses appropriate status ("available", "coming-soon", "draft")
4. **Tier metadata** - Updates lessonCount, status (complete/in-progress/planned)
5. **Array insertion** - Places lesson in correct position (sorted by lesson number)
6. **Format preservation** - Maintains existing indentation, spacing, structure

---

## Agent Behavior

### Update Tier Index (Always)

**File:** `/website/src/pages/{platform}/phase-{N}/tier-{N}/index.astro`

**Action:** Add lesson object to lessons array:
```javascript
{
  number: {N},
  title: "{Lesson Title}",
  description: "{Lesson description}",
  status: "{available|coming-soon|draft}"
}
```

**Sorting:** Lessons array sorted by number (ascending)

**Format:** Maintains existing indentation and structure

### Update Phase Index (Conditional)

**Condition:** First lesson in a NEW tier

**File:** `/website/src/pages/{platform}/phase-{N}/index.astro`

**Action:** Add tier object to tiers array:
```javascript
{
  number: {N},
  title: "{Tier Name}",
  description: "{Tier description from curriculum}",
  lessonCount: {expected count},
  duration: "{estimated duration}",
  status: "in-progress",
  url: "/{platform}/phase-{N}/tier-{N}"
}
```

**Note:** Agent reads tier description from curriculum document

### Update Platform Index (Conditional)

**Condition:** First lesson in a NEW phase

**File:** `/website/src/pages/{platform}/index.astro`

**Action:** Add phase object to phases array (if not already present)

**Format:** Follows existing phase entry pattern

### Update Homepage (Conditional)

**Condition:** Significant milestone reached

**File:** `/website/src/pages/index.mdx`

**Milestones:**
- First lesson on new platform
- Phase 0 Tier 1 complete (all 16 lessons)
- Phase 1 Tier 1 complete
- Major game completed

**Action:** Update milestone section or latest updates

---

## Files Agent Updates

**Always:**
```
/website/src/pages/{platform}/phase-{N}/tier-{N}/index.astro
```

**Conditionally:**
```
/website/src/pages/{platform}/phase-{N}/index.astro (if first in tier)
/website/src/pages/{platform}/index.astro (if first in phase)
/website/src/pages/index.mdx (if milestone)
```

---

## Error Handling

### File Not Found

If tier index doesn't exist:
1. Agent reports error: "Tier index not found: {path}"
2. Agent does NOT create new index (requires manual setup)
3. User must create tier/phase structure first

### Duplicate Entry

If lesson number already exists in tier index:
1. Agent reports: "Lesson {N} already exists in tier index"
2. Agent asks: "Replace existing entry? (yes/no)"
3. If yes: Updates existing entry
4. If no: Aborts without changes

### Invalid Format

If index file has unexpected structure:
1. Agent reports: "Cannot parse {file}: unexpected format"
2. Agent does NOT modify file
3. User must fix file structure manually

---

## Invocation Pattern

```javascript
Task tool invocation:
{
  subagent_type: "general-purpose",
  description: "Update navigation for new lesson",
  prompt: `You are updating navigation files for the Code Like It's 198x project.

NEW LESSON DETAILS:
- Platform: {platform}
- Phase: {N}
- Tier: {N}
- Lesson: {NNN}
- Title: "{Lesson Title}"
- Description: "{Lesson description (max 150 chars)}"
- Status: {available|coming-soon|draft}

YOUR TASK:
Update all required navigation files following this logic:

1. ALWAYS UPDATE:
   /website/src/pages/{platform}/phase-{N}/tier-{N}/index.astro
   - Add lesson to lessons array
   - Sort by number
   - Maintain format

2. CONDITIONAL UPDATES:
   - If first lesson in tier: Update phase index with new tier entry
   - If first lesson in phase: Update platform index with new phase entry
   - If milestone: Update homepage

DECISIONS YOU MAKE:
- Which files need updating (based on lesson position)
- Description formatting (concise, technical)
- Tier metadata (lessonCount, status)
- Array insertion position (maintain sort order)

DO NOT ASK USER:
- Whether to update (always update required files)
- How to format (follow existing patterns)
- Description length (trim to 150 chars if needed)

ERROR HANDLING:
- If file not found: Report error, do NOT create
- If duplicate lesson number: Report, ask to replace
- If invalid format: Report error, do NOT modify

REPORT:
"Navigation updated successfully.

FILES MODIFIED:
- {file1}: Added lesson {N}
- {file2}: Added tier {N} entry (if applicable)
- {file3}: Added phase {N} entry (if applicable)

CHANGES:
{Describe specific changes made to each file}"

Execute navigation update now.`
}
```

---

## Verification

After update, agent verifies:

1. **Syntax valid** - Updated files are valid Astro/MDX
2. **Lesson present** - New lesson appears in tier index
3. **Sorted correctly** - Lessons array sorted by number
4. **Format preserved** - Indentation and structure match original
5. **Links work** - URLs point to correct paths

If any verification fails, agent reports issue.

---

## Common Mistakes and Fixes

**Mistake 1: Breaking array syntax**
- **Cause:** Comma placement wrong
- **Fix:** Validate JSON-like structure before writing
- **Prevention:** Parse existing array, add entry, stringify with proper format

**Mistake 2: Wrong sort order**
- **Cause:** Appending to end instead of inserting sorted
- **Fix:** Sort array by number after insertion
- **Prevention:** Always sort before writing

**Mistake 3: Updating wrong files**
- **Cause:** Not checking if tier/phase is new
- **Fix:** Check existing entries before updating parent indexes
- **Prevention:** Read phase index to see if tier exists

**Mistake 4: Long descriptions**
- **Cause:** Using full curriculum description
- **Fix:** Trim to 150 characters, end with period
- **Prevention:** Validate description length before insertion

**Mistake 5: Breaking indentation**
- **Cause:** Not matching existing spacing
- **Fix:** Parse indentation level from existing entries
- **Prevention:** Use consistent 2-space indent

---

## Example Update

**Input:**
```
Platform: sinclair-zx-spectrum
Phase: 0
Tier: 1
Lesson: 17
Title: "User-Defined Graphics"
Description: "Create custom characters with UDG for sprites and game graphics."
Status: available
```

**Actions:**
1. ✓ Update tier-1/index.astro (add lesson 17)
2. ✗ Skip phase index (tier 1 already exists)
3. ✗ Skip platform index (phase 0 already exists)
4. ✗ Skip homepage (not a milestone)

**Report:**
```
Navigation updated successfully.

FILES MODIFIED:
- /website/src/pages/sinclair-zx-spectrum/phase-0/tier-1/index.astro

CHANGES:
- Added lesson 17 to lessons array (position 17)
- Array sorted by lesson number
- Format preserved (2-space indent)
```

---

## Dependencies

**Required:**
- Tier index exists (must be created manually if new tier)
- Phase index exists (must be created manually if new phase)
- Platform index exists (must be created manually if new platform)

**Curriculum documents:**
- Tier description available in curriculum (for new tier entries)
- Lesson count known (for tier metadata)

---

## Success Metrics

**Agent succeeds if:**
- All required files updated
- No syntax errors introduced
- Lesson appears in correct position
- Format matches existing entries
- Links are valid

**Agent fails if:**
- Syntax broken
- Lesson appears twice
- Wrong sort order
- Files corrupted
- Missing required updates

---

## The Bottom Line

**This agent handles navigation updates systematically:**
1. Always updates tier index
2. Conditionally updates phase/platform/home
3. Maintains format consistency
4. Sorts entries correctly
5. Reports all changes clearly

**Zero tolerance for:**
- Breaking syntax
- Wrong sort order
- Missing tier update
- Format inconsistency
- Duplicate entries
