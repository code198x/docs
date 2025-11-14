# Pattern Extraction Agent

**Version:** 1.0
**Status:** Specification complete, not yet tested
**Priority:** P2 (Medium - Content Expansion)

---

## Purpose

Scans completed lessons to identify reusable code patterns, then generates complete Pattern Library entries following pattern-library-template structure. The agent analyzes code across multiple lessons to find repeated techniques and automatically documents them with variations and integration examples.

**Think:** "Scan Phase 0 Tier 1" → Agent finds score display technique used in lessons 15, 20, 25 → Generates complete pattern entry with variations from all three lessons.

---

## When to Use

Use this agent when:
- Completed lessons use similar techniques repeatedly
- Pattern Library needs expansion
- Systematically documenting techniques from existing curriculum
- Identifying candidates for pattern documentation

**Do NOT use when:**
- Pattern is already documented (use Edit tool to update)
- Lesson code is too simple/unique (no pattern exists)
- Only one lesson uses technique (not a pattern yet)

---

## Inputs Required

### Scan Scope

**Option A: Lesson range**
```
PLATFORM: C64
PHASE: 0
TIER: 1
LESSON_RANGE: 1-32
```

**Option B: Specific lessons**
```
PLATFORM: C64
PHASE: 0
LESSONS: [7, 8, 15, 20, 25]
```

**Option C: Entire phase**
```
PLATFORM: C64
PHASE: 0
SCAN_ALL: true
```

### Pattern Identification Criteria

**Threshold for pattern candidacy:**
```
MIN_OCCURRENCES: 3  (default - technique appears in 3+ lessons)
MIN_CODE_LINES: 5   (default - technique is 5+ lines)
SIMILARITY_THRESHOLD: 70%  (default - 70% code similarity)
```

**Optional overrides:**
- Lower MIN_OCCURRENCES to 2 (for rare but valuable patterns)
- Raise SIMILARITY_THRESHOLD to 90% (for exact pattern matches only)

### Output Preferences

**Pattern detail level:**
```
VARIATION_DETAIL: {minimal|standard|comprehensive}
- minimal: 3 variations
- standard: 4-5 variations
- comprehensive: 6+ variations with edge cases
```

**Dry run mode:**
```
DRY_RUN: true  (identifies patterns without creating files)
```

---

## Workflow Steps

### Phase 1: Pattern Identification

**Step 1:** Read pattern-library-template skill
- Location: `/docs/skills/pattern-library-template/SKILL.md`
- Purpose: Understand pattern structure requirements

**Step 2:** Scan lesson files in scope

For each lesson in range:
```bash
# Find code samples
find /code-samples/{platform}/{phase}/tier-{N}/lesson-{NNN}/ -name "*.bas" -o -name "*.asm"

# Find lesson MDX
find /website/src/pages/{platform}/{phase}/tier-{N}/lesson-{NNN}.mdx
```

**Step 3:** Extract code blocks from lessons

For each lesson:
1. Read all code sample files
2. Parse lesson MDX for inline code blocks
3. Catalog techniques by examining:
   - Screen manipulation (POKE to screen memory)
   - Input handling (joystick/keyboard)
   - Sprite operations (VIC-II POKEs)
   - Sound generation (SID POKEs)
   - Loops and timing
   - Data structures
   - Memory management

**Step 4:** Identify repeated techniques

Compare code across lessons:
- **Exact matches:** Same POKE addresses, same sequences
- **Structural matches:** Same pattern, different values
- **Conceptual matches:** Same goal, different implementation

**Pattern candidate criteria:**
- Appears in MIN_OCCURRENCES or more lessons
- Code block is MIN_CODE_LINES or longer
- Similarity >= SIMILARITY_THRESHOLD

**Step 5:** Rank pattern candidates

**Priority scoring:**
```
Score = (occurrences × 2) + (complexity × 1) + (generality × 3)

occurrences: How many lessons use it (1-10+ scale)
complexity: Lines of code / 5 (1-10 scale)
generality: Cross-platform applicability (1-5 scale)
```

**High-value patterns** (score >= 20):
- Used in 5+ lessons
- Moderate complexity (10-20 lines)
- Platform-specific but conceptually universal

**Step 6:** Generate pattern candidate report

```
PATTERN EXTRACTION SCAN: {platform} {phase} Tier {N}

HIGH-VALUE CANDIDATES (score >= 20):
1. Score Display [score: 24]
   - Lessons: 15, 20, 25, 28
   - Lines: 8-12
   - Category: Game Mechanics

2. Sprite Positioning [score: 22]
   - Lessons: 10, 14, 18, 22
   - Lines: 6-10
   - Category: Graphics

MEDIUM-VALUE CANDIDATES (score 10-19):
3. Sound Effect Trigger [score: 15]
   - Lessons: 12, 19
   - Lines: 5-7
   - Category: Sound

LOW-VALUE CANDIDATES (score < 10):
4. Simple Variable Increment [score: 6]
   - Lessons: 7, 13
   - Lines: 1-2
   - Category: (Too simple for pattern)

RECOMMENDATION:
- Extract patterns 1-2 (high value)
- Consider pattern 3 if sound patterns sparse
- Skip pattern 4 (too simple)
```

**If DRY_RUN mode:** Stop here, return report only.

### Phase 2: Pattern Documentation Generation

**For each approved pattern candidate:**

**Step 7:** Generate pattern entry structure

**Infer pattern metadata:**
- **Title:** Derive from technique (e.g., "Score Display", "Sprite Positioning")
- **Category:** Infer from code type (POKE $D000 = Graphics, POKE $D400 = Sound, etc.)
- **Difficulty:** Infer from complexity
  - Easy: < 10 lines, single concept
  - Medium: 10-20 lines, 2-3 concepts
  - Hard: 20-40 lines, timing-critical
  - Expert: 40+ lines, multi-system coordination
- **lessonsAppearIn:** List of lesson numbers from scan
- **system:** Platform being scanned (or "Universal" if cross-platform)

**Step 8:** Extract canonical example

From all occurrences, select:
- **Simplest version** as canonical example (for ## The Pattern section)
- **Most commented version** as basis for explanation
- **All versions** as variations

**Step 9:** Generate "How It Works" section

Analyze canonical example:
1. Identify steps (screen clear, variable init, loop, update, etc.)
2. Extract line-by-line operations
3. Generate numbered step-by-step breakdown
4. Include WHY (not just WHAT)

**Example analysis:**
```basic
100 SCORE=0        → Initialize variable
110 PRINT "SCORE:";SCORE  → Display initial value
...
```

Generates:
```markdown
## How It Works

1. **Initialise score variable** (line 100) - Starts at zero
2. **Display initial value** (line 110) - Shows "SCORE:0" on screen
...
```

**Step 10:** Generate Variations section

From all lesson occurrences:
- **Variation 1:** Simplest version (canonical)
- **Variation 2:** Most optimised version (if different)
- **Variation 3:** Most feature-rich version (formatting, boundaries, etc.)
- **Variation 4+:** Assembly version (if found), multi-digit, leading zeros, etc.

Each variation includes:
- Descriptive name
- Complete code
- Explanation of trade-offs

**Step 11:** Generate Common Mistakes section

Analyze lesson progression:
- Early lessons: Identify simpler/broken attempts
- Later lessons: Identify refined techniques

**Infer mistakes from progression:**
- Lesson 15 clears entire screen (flicker) → Mistake: Flickering Score
- Lesson 20 uses cursor positioning (no flicker) → Fix: Cursor positioning

Generate Symptom/Cause/Fix format:
```markdown
### Flickering Score
**Symptom:** Score flashes on and off rapidly
**Cause:** Clearing entire screen instead of just score area
**Fix:** Use cursor positioning (POKE 214) to overwrite score location only
```

**Step 12:** Generate Integration Example

Select one lesson occurrence that shows realistic usage:
- Prefer complete game loop example
- 30-60 lines
- Includes other game elements (lives, enemies, input)
- Well-commented

Extract and format as Integration Example.

**Step 13:** Generate cross-references

**Automatic "See also" links:**
- Related patterns (same category)
- Lessons where pattern appears (from lessonsAppearIn)
- Prerequisite patterns (techniques used before this one)

**Example:**
```markdown
## See also

- [Variable Management](/platform/phase/patterns/library/variable-management)
- [Screen Positioning](/platform/phase/patterns/library/screen-positioning)
- [Lesson 15](/c64/phase-0/tier-2/lesson-015)
- [Lesson 20](/c64/phase-0/tier-3/lesson-020)
```

**Step 14:** Generate remaining sections

**Parameters section:** Extract configurable values (memory addresses, ranges, limits)

**Memory Usage section:** Calculate:
- Variables used (bytes)
- Code size (bytes)
- Screen memory (if applicable)

**Quick Reference Card:** Extract:
- Key memory locations
- Key formulas
- Syntax template

**Best Practices:** Infer from lesson comments and progression

**Metadata Footer:**
```markdown
---

**Status:** Draft
**Last Updated:** {YYYY-MM-DD}
**Source Lesson:** [Lesson {N}](/platform/phase/tier/lesson-{N})
**Extracted:** Automatically by pattern-extraction-agent
```

**Step 15:** Create pattern file

Path: `/website/src/pages/{platform}/{phase}/patterns/library/{slug}.mdx`
Slug: Lowercase, hyphenated pattern title

**Step 16:** Validate with pattern-library-template skill

Use Skill tool:
```javascript
Skill("pattern-library-template")
```

Validate created pattern against skill requirements.

**If validation fails:**
- Log specific failures
- Mark pattern as "Draft - Needs Manual Refinement"
- Continue with next pattern (don't stop entire agent)

**Step 17:** Generate extraction report

```
PATTERN EXTRACTION COMPLETE: {platform} {phase} Tier {N}

PATTERNS CREATED:
✓ score-display.mdx (Easy, 4 lessons, validated)
✓ sprite-positioning.mdx (Medium, 4 lessons, validated)
✓ sound-effect-trigger.mdx (Easy, 2 lessons, needs refinement)

VALIDATION ISSUES:
⚠ sound-effect-trigger: Only 2 variations (3 required)
  → Manual refinement needed

FILES CREATED: 3
FILES NEEDING REFINEMENT: 1

NEXT STEPS:
- Review Draft patterns for accuracy
- Expand sound-effect-trigger variations
- Consider extracting lower-priority patterns manually
```

---

## Skills Used

### pattern-library-template (Structure enforcement)
- Location: `/docs/skills/pattern-library-template/SKILL.md`
- When: After creating each pattern entry
- Purpose: Validate completeness and structure

### british-english-check (Language validation)
- Location: `/docs/skills/british-english-check/SKILL.md`
- When: After creating each pattern entry
- Purpose: Verify British English spellings in generated content

---

## Error Handling

### Error Scenarios

**Error 1: No lessons found in scope**
```
AGENT FAILED at Step 2 (scan lessons)

FAILED:
✗ No lesson files found in:
  /code-samples/{platform}/{phase}/tier-{N}/lesson-{range}/

SUGGESTED FIX:
- Verify lesson range is correct
- Check platform/phase/tier values
- Ensure lessons exist in specified location
```

**Error 2: No patterns detected**
```
AGENT COMPLETED WITH NO PATTERNS

COMPLETED:
✓ Scanned {N} lessons
✓ Analyzed {N} code blocks

RESULT:
⊗ No repeated techniques found meeting criteria:
  - MIN_OCCURRENCES: {N}
  - MIN_CODE_LINES: {N}
  - SIMILARITY_THRESHOLD: {N}%

SUGGESTED ACTION:
- Lower MIN_OCCURRENCES threshold
- Scan broader lesson range
- Manually identify patterns (agent may miss subtle similarities)
```

**Error 3: Pattern validation fails**
```
AGENT PARTIAL SUCCESS at Step 16 (validation)

COMPLETED:
✓ Created pattern: {slug}.mdx

FAILED:
✗ Validation issues:
  - Only {N} variations ({min} required)
  - Missing Common Mistakes section
  - Integration example too short

RESULT:
⊗ Pattern marked as "Draft - Needs Manual Refinement"

SUGGESTED ACTION:
- Review pattern file manually
- Add missing sections
- Expand content to meet pattern-library-template requirements
```

**Error 4: File already exists**
```
AGENT FAILED at Step 15 (file creation)

FAILED:
✗ Pattern file already exists: {slug}.mdx

SUGGESTED FIX:
- Choose different pattern title/slug
- OR delete existing pattern if replacing
- OR use Edit tool to update existing pattern
```

---

## Pattern Recognition Heuristics

### Code Similarity Detection

**Exact match (100% similarity):**
```basic
# Lesson 15
100 SCORE=0
110 PRINT "SCORE:";SCORE

# Lesson 20
100 SCORE=0
110 PRINT "SCORE:";SCORE
```
→ Identical code, clear pattern

**Structural match (70-90% similarity):**
```basic
# Lesson 15
100 SCORE=0
110 PRINT "SCORE:";SCORE

# Lesson 20
200 POINTS=0
210 PRINT "POINTS:";POINTS
```
→ Same structure, different variable names

**Conceptual match (50-70% similarity):**
```basic
# Lesson 15 (BASIC)
100 SCORE=0
110 PRINT "SCORE:";SCORE

# Lesson 18 (Assembly)
LDA #0
STA SCORE
JSR DISPLAY_SCORE
```
→ Same goal, different implementation

**Agent identifies structural and conceptual matches** using:
- Line count similarity
- Variable pattern matching
- POKE address pattern matching
- Control flow similarity (loops, conditionals)

### Category Inference

**Memory address patterns:**
- `$D000-$D02E` → Graphics (VIC-II sprites)
- `$D400-$D41C` → Sound (SID chip)
- `$DC00-$DC0F` → Input (CIA joystick/keyboard)
- `$0400-$07E7` → Graphics (screen memory)
- `$D800-$DBE7` → Graphics (colour memory)

**Code pattern types:**
- Loops with user input → Input
- PEEKs from $DC00-$DC0F → Input
- POKEs to $D000-$D02E → Graphics
- POKEs to $D400-$D41C → Sound
- Variable arithmetic → Game Mechanics
- Array manipulation → Memory Management
- Timing loops (FOR...NEXT delays) → Performance

### Difficulty Inference

**Easy (< 10 lines, single concept):**
```basic
100 SCORE=0
110 PRINT "SCORE:";SCORE
120 SCORE=SCORE+10
```

**Medium (10-20 lines, 2-3 concepts):**
```basic
100 SCORE=0 : HISCORE=0
110 IF SCORE>HISCORE THEN HISCORE=SCORE
120 PRINT "SCORE:";SCORE;" HI:";HISCORE
130 REM boundary checking
140 IF SCORE>65000 THEN SCORE=0
```

**Hard (20-40 lines, timing-critical):**
```basic
100 POKE 53280,0
110 FOR I=1 TO 8
120   POKE 53287+I,I
130   FOR J=0 TO 20 : NEXT J : REM delay
140 NEXT I
```

**Expert (40+ lines, multi-system coordination):**
```asm
; Raster interrupt setup with sprite multiplexing
...
40+ lines of assembly
```

---

## Invocation Patterns

### Scan Entire Tier

```javascript
{
  subagent_type: "general-purpose",
  description: "Extract patterns from C64 Phase 0 Tier 1",
  prompt: `PATTERN EXTRACTION SCAN:

PLATFORM: C64
PHASE: 0
TIER: 1
LESSON_RANGE: 1-32

PATTERN CRITERIA:
MIN_OCCURRENCES: 3
MIN_CODE_LINES: 5
SIMILARITY_THRESHOLD: 70%

VARIATION_DETAIL: standard

Use pattern-extraction-agent to:
1. Scan all lessons in range
2. Identify repeated code techniques
3. Generate complete pattern entries
4. Validate with pattern-library-template skill
5. Report patterns created and any validation issues`
}
```

### Scan Specific Lessons

```javascript
{
  subagent_type: "general-purpose",
  description: "Extract patterns from specific lessons",
  prompt: `PATTERN EXTRACTION SCAN:

PLATFORM: C64
PHASE: 0
LESSONS: [15, 20, 25, 28]
FOCUS: Score display techniques

PATTERN CRITERIA:
MIN_OCCURRENCES: 2  (only 4 lessons)
MIN_CODE_LINES: 5
SIMILARITY_THRESHOLD: 70%

VARIATION_DETAIL: comprehensive

Use pattern-extraction-agent to generate comprehensive pattern entry for score display with all variations from these lessons.`
}
```

### Dry Run (Pattern Identification Only)

```javascript
{
  subagent_type: "general-purpose",
  description: "Identify pattern candidates",
  prompt: `PATTERN EXTRACTION SCAN:

PLATFORM: C64
PHASE: 0
TIER: 2
LESSON_RANGE: 33-64

DRY_RUN: true

Identify pattern candidates without creating files. Report:
- High-value candidates (score >= 20)
- Medium-value candidates (score 10-19)
- Recommended patterns to extract
- Estimated file count if extraction proceeds`
}
```

---

## Testing Checklist

Before production use, test with:

**Test 1: Known pattern (exact matches)**
- Input: Lessons known to use identical technique (e.g., score display in 15, 20, 25)
- Expected: Pattern extracted with 3+ variations, validated successfully

**Test 2: Structural similarity**
- Input: Lessons using same technique with different variable names
- Expected: Pattern recognized despite naming differences

**Test 3: No patterns found**
- Input: Lessons with unique, non-repeated code
- Expected: Agent reports "no patterns detected", no files created

**Test 4: Low occurrence threshold**
- Input: MIN_OCCURRENCES: 2
- Expected: More pattern candidates identified (may include marginal patterns)

**Test 5: Dry run mode**
- Input: DRY_RUN: true
- Expected: Candidate report generated, 0 files created

**Test 6: Validation failure**
- Input: Pattern with only 1-2 variations (below minimum)
- Expected: Pattern created but marked "Draft - Needs Manual Refinement"

**Test 7: Existing pattern file**
- Input: Pattern slug matches existing file
- Expected: Error at step 15, no file overwritten

---

## Agent Autonomy

**High autonomy - No user intervention during execution:**
- Identifies patterns automatically
- Generates complete documentation
- Infers metadata (category, difficulty, etc.)
- Creates variations from lesson examples
- Validates with pattern-library-template skill

**User provides:**
- Scan scope (lessons to analyze)
- Pattern criteria thresholds
- Variation detail level

**User reviews after completion:**
- Extraction report
- Created pattern entries
- Validation issues (for manual refinement)

---

## Production Notes

### Pattern Quality

**Agent-generated patterns are drafts.** After extraction:

1. **Review "How It Works" section** - May need clearer explanation
2. **Review "Common Mistakes" section** - May need more context
3. **Review "Integration Example"** - May need better commenting
4. **Add "Best Practices"** - Agent infers these, may miss nuances
5. **Expand variations** - Agent includes what it finds, may miss edge cases

**High-priority manual refinement:**
- Patterns marked "Draft - Needs Manual Refinement"
- Patterns with < 3 variations
- Patterns where lessons had limited examples

### Pattern vs. Anti-Pattern

**Agent may identify anti-patterns** (bad techniques used repeatedly):

Example: Early lessons use `PRINT CHR$(147)` (clear screen) in loops → flicker

**If detected:**
1. Agent creates pattern entry
2. Mark pattern as "Anti-Pattern" in metadata
3. "Common Mistakes" section becomes primary focus
4. "How It Works" explains why it's problematic
5. Variations show correct alternatives

### Integration with Curriculum

After extraction:
- Update curriculum docs to reference patterns
- Add pattern links to lesson MDX "From the Vault" sections
- Use patterns as teaching aids in future lessons

---

## Integration with Other Agents

**pattern-extraction-agent** can be called by:

**curriculum-audit-agent:**
- Scans all lessons
- Identifies lessons without pattern documentation
- Calls pattern-extraction-agent for gaps

**lesson-creation-agent:**
- Creates new lesson
- Identifies technique similar to existing pattern
- Suggests using documented pattern

**Calls other agents:**

**vault-entry-agent:**
- Extracts pattern pioneered by specific person
- Discovers person not in Vault
- Calls vault-entry-agent to create entry

---

## The Bottom Line

**pattern-extraction-agent automates Pattern Library growth:**
- Scans lessons for repeated techniques
- Identifies pattern candidates by occurrence and complexity
- Generates complete pattern documentation with variations
- Validates against pattern-library-template skill

**Use when:**
- Completed lessons use similar techniques repeatedly
- Pattern Library needs systematic expansion
- Want to document techniques already in curriculum

**Produces:**
- Complete pattern entries (Draft status)
- Extraction report with validation issues
- Cross-referenced lesson links

**Review and refine generated patterns - agent provides solid drafts requiring expert polish.**

---

**Status:** Specification complete, not yet tested in production
**Next steps:** Test with known pattern candidates (C64 Phase 0 Tier 1 score display), refine similarity heuristics
