# Cross-Reference Validator Agent

**Version:** 1.0
**Status:** Specification complete, not yet tested
**Priority:** P2 (High - Comprehensive link validation)

---

## Purpose

Validates ALL cross-references across the entire site beyond what curriculum-audit-agent provides. Checks lessons → patterns, patterns → lessons, vault → vault, curriculum → lessons, pattern `lessonsAppearIn` metadata accuracy, and bidirectional link consistency. Generates comprehensive link integrity report.

**Think:** "Are all cross-references working?" → Agent scans 500+ lessons/patterns/vault entries, validates every internal link, checks metadata accuracy, reports broken/missing/inconsistent links.

---

## When to Use

Use when:
- After major content changes (new lessons/patterns/vault entries)
- Periodic maintenance (monthly link health check)
- Before releases
- Suspected link rot
- After archiving lessons (verify references updated)

**Do NOT use when:**
- Just created single lesson (overkill - use lesson-validation)
- Only checking specific file (Read tool faster)

---

## Inputs Required

### Validation Scope

**Option A: Full validation (all content types)**
```
VALIDATE_ALL: true
```

**Option B: Specific content types**
```
CONTENT_TYPES: ["lessons", "patterns", "vault"]
```

**Option C: Specific platform**
```
PLATFORM: "C64"
PHASES: [0, 1]
```

### Validation Depth

**Quick validation (existence only):**
```
DEPTH: quick
- Check files exist
- Check links resolve
- ~5 minutes
```

**Standard validation (existence + metadata):**
```
DEPTH: standard  
- File existence
- Link resolution
- Metadata accuracy (lessonsAppearIn)
- Bidirectional link consistency
- ~15 minutes
```

**Deep validation (comprehensive):**
```
DEPTH: deep
- All standard checks
- Anchor link validation (#section-name)
- Orphaned content detection
- Dead link pattern analysis
- ~30 minutes
```

---

## Workflow Steps

### Phase 1: Content Discovery

**Step 1:** Discover all lesson files

```bash
find /website/src/pages/ -name "lesson-*.mdx" -type f
```

**Build lesson inventory:**
- Platform, phase, tier, lesson number
- File path
- Extract all internal links from content

**Step 2:** Discover all pattern files

```bash
find /website/src/pages/*/phase-*/patterns/library/ -name "*.mdx" -type f
```

**Build pattern inventory:**
- Pattern slug
- File path
- Extract `lessonsAppearIn` from frontmatter
- Extract all internal links from content

**Step 3:** Discover all vault entries

```bash
find /website/src/pages/vault/ -name "*.mdx" -type f
```

**Build vault inventory:**
- Entry slug
- File path
- Extract "See also" links

**Step 4:** Discover curriculum documents

```bash
find /docs/ -name "PHASE-*-CURRICULUM.md" -type f
```

**Build curriculum inventory:**
- Platform, phase
- Extract lesson references from curriculum

### Phase 2: Link Extraction

**Step 5:** Extract links from lessons

**Parse each lesson for:**
```markdown
[Pattern Name](/platform/phase/patterns/library/pattern-slug)
[Vault Entry](/vault/entry-slug)
[Other Lesson](/platform/phase/tier/lesson-NNN)
[External](#section-anchor)
```

**Build link graph:**
```
lesson-015 → pattern:score-display
lesson-015 → vault:jeff-minter
lesson-015 → lesson-014
```

**Step 6:** Extract links from patterns

**Parse each pattern for:**
```yaml
lessonsAppearIn: 15, 20, 25
```

**Parse content for:**
```markdown
[Lesson 15](/c64/phase-0/tier-2/lesson-015)
[Related Pattern](/c64/phase-0/patterns/library/sprite-basics)
```

**Build link graph:**
```
pattern:score-display → lesson-015
pattern:score-display → lesson-020  
pattern:score-display → lesson-025
pattern:score-display → pattern:variable-management
```

**Step 7:** Extract links from vault

**Parse "See also" sections:**
```markdown
## See also
- [Llamasoft](/vault/llamasoft)
- [Tempest 2000](/vault/tempest-2000)
```

**Build link graph:**
```
vault:jeff-minter → vault:llamasoft
vault:jeff-minter → vault:tempest-2000
```

**Step 8:** Extract lesson references from curriculum

**Parse curriculum for lesson numbers:**
```markdown
**Lesson 15: Score Display**
```

**Build curriculum expectations:**
```
c64-phase-0-curriculum expects: lesson-015
c64-phase-0-curriculum expects: lesson-016
...
```

### Phase 3: Link Validation

**Step 9:** Validate lesson links

**For each link in lessons:**

```bash
# Extract target from link
[Pattern](/c64/phase-0/patterns/library/score-display) 
→ target: /c64/phase-0/patterns/library/score-display.mdx

# Check file exists
if [ ! -f "/website/src/pages/c64/phase-0/patterns/library/score-display.mdx" ]; then
  log "BROKEN: lesson-015 → pattern:score-display (file not found)"
fi
```

**Check for:**
- ✓ File exists
- ✗ File missing (broken link)
- ✗ Wrong path (typo in link)

**Step 10:** Validate pattern `lessonsAppearIn` metadata

**For each pattern:**

```yaml
lessonsAppearIn: 15, 20, 25
```

**Verify:**
1. Do lessons 15, 20, 25 actually exist?
2. Do lessons 15, 20, 25 actually link back to this pattern?

**Report discrepancies:**
```
METADATA MISMATCH: pattern:score-display
- Claims lesson-015 uses it: ✓ TRUE (lesson-015 links to pattern)
- Claims lesson-020 uses it: ✓ TRUE (lesson-020 links to pattern)
- Claims lesson-025 uses it: ✗ FALSE (lesson-025 does NOT link to pattern)
- Lesson-030 links to pattern: ✗ MISSING from lessonsAppearIn
```

**Step 11:** Validate bidirectional links (vault)

**For each vault entry:**

```markdown
## vault/jeff-minter.mdx
See also:
- [Llamasoft](/vault/llamasoft)
```

**Check:**
1. Does `/vault/llamasoft.mdx` exist?
2. Does llamasoft link back to jeff-minter?

**Report:**
```
BIDIRECTIONAL LINK MISSING:
- jeff-minter → llamasoft: ✓ EXISTS
- llamasoft → jeff-minter: ✗ MISSING (should link back)
```

**Step 12:** Validate curriculum lesson references

**For each curriculum document:**

```markdown
**Lesson 15: Score Display**
```

**Check:**
1. Does lesson-015.mdx exist?
2. Does lesson title match curriculum spec?

**Report:**
```
CURRICULUM MISMATCH:
- Curriculum expects: lesson-015 "Score Display"
- File exists: ✓ YES
- Title matches: ✓ YES

- Curriculum expects: lesson-018 "Joystick Input"
- File exists: ✗ NO (missing or archived)
```

**Step 13:** Validate anchor links (if DEPTH=deep)

**For anchor links:**
```markdown
[See section](#the-pattern)
```

**Check:**
1. Does `## The Pattern` heading exist in same file?
2. Is anchor slug correct (`the-pattern` from `The Pattern`)?

**Common anchor issues:**
- Heading deleted but anchor link remains
- Wrong slug (spaces, special chars)

**Step 14:** Detect orphaned content

**Find content with zero incoming links:**

```
ORPHANED PATTERNS:
- pattern:obscure-technique (0 lessons link to it)

ORPHANED VAULT:
- vault:unknown-person (0 entries link to it)

ORPHANED LESSONS:
- lesson-099 (not in navigation, not in curriculum)
```

**Step 15:** Analyze dead link patterns

**Identify systematic issues:**

```
DEAD LINK PATTERNS:
- 15 links to archived lessons (pattern: /phase-0/tier-1/lesson-0{12,15,18})
- 8 links to renamed vault entries (pattern: /vault/old-slug-format)
- 3 links to moved patterns (pattern: /old-pattern-location/)
```

### Phase 4: Report Generation

**Step 16:** Generate comprehensive report

```markdown
# Cross-Reference Validation Report

**Date:** {YYYY-MM-DD}
**Scope:** {content types scanned}
**Depth:** {quick|standard|deep}
**Links Checked:** {N}
**Issues Found:** {N}

---

## Executive Summary

**Health Score:** {percentage}% ({N} broken, {N} inconsistent, {N} orphaned)

**Critical Issues:** {N} (broken links)
**High Issues:** {N} (metadata mismatches)
**Medium Issues:** {N} (bidirectional missing)
**Low Issues:** {N} (orphaned content)

---

## Broken Links (Critical)

### Lessons → Patterns

- **Lesson 015** → pattern:score-display (✗ file not found)
  - Link: `/c64/phase-0/patterns/library/score-display`
  - Expected file: `/website/src/pages/c64/phase-0/patterns/library/score-display.mdx`
  - **Fix:** Create pattern or update link

- **Lesson 020** → pattern:old-name (✗ renamed)
  - Link: `/c64/phase-0/patterns/library/old-name`
  - Actual file: `/website/src/pages/c64/phase-0/patterns/library/new-name.mdx`
  - **Fix:** Update link to new-name

### Lessons → Vault

- **Lesson 030** → vault:unknown-person (✗ file not found)
  - Link: `/vault/unknown-person`
  - Expected file: `/website/src/pages/vault/unknown-person.mdx`
  - **Fix:** Create vault entry or remove link

### Vault → Vault

- **vault/jeff-minter** → vault:nonexistent-game (✗ file not found)
  - Link: `/vault/nonexistent-game`
  - **Fix:** Create vault entry stub or remove link

---

## Metadata Mismatches (High)

### Pattern `lessonsAppearIn` Inaccuracy

#### pattern:score-display

**Claims:**
- lesson-015: ✓ CORRECT (lesson links to pattern)
- lesson-020: ✓ CORRECT (lesson links to pattern)
- lesson-025: ✗ INCORRECT (lesson does NOT link to pattern)

**Missing from metadata:**
- lesson-030: Links to pattern but not in lessonsAppearIn

**Fix:**
```yaml
# Current
lessonsAppearIn: 15, 20, 25

# Should be
lessonsAppearIn: 15, 20, 30
```

#### pattern:sprite-basics

**Claims:**
- lesson-010: ✗ INCORRECT (lesson does NOT link)

**Missing from metadata:**
- lesson-012: Links but not listed
- lesson-014: Links but not listed

**Fix:**
```yaml
# Current
lessonsAppearIn: 10

# Should be
lessonsAppearIn: 12, 14
```

---

## Bidirectional Link Issues (Medium)

### Vault Entries

- **jeff-minter → llamasoft:** ✓ Link exists
- **llamasoft → jeff-minter:** ✗ Missing (should link back)

- **llamasoft → attack-of-mutant-camels:** ✓ Link exists
- **attack-of-mutant-camels → llamasoft:** ✓ Link exists (bidirectional OK)

**Fix:** Add reciprocal links in vault entries

---

## Curriculum Mismatches (High)

### C64 Phase 0

- **Curriculum expects lesson-012:** ✗ Missing (archived 2025-11-05)
  - **Fix:** Create replacement or update curriculum

- **Curriculum expects lesson-015:** ✓ Exists
  - Title matches: ✓ "Score Display"

- **Curriculum expects lesson-018:** ✗ Missing
  - **Fix:** Create lesson or remove from curriculum

---

## Orphaned Content (Low)

### Patterns with Zero Incoming Links

- **pattern:advanced-technique** (0 lessons reference)
  - Created: 2025-10-15
  - **Recommendation:** Add to relevant lessons or archive

### Vault Entries with Zero Incoming Links

- **vault:obscure-developer** (0 entries reference)
  - **Recommendation:** Add to related entries or archive

### Lessons Not in Navigation

- **lesson-099** (not in tier index, not in curriculum)
  - **Recommendation:** Archive or add to navigation

---

## Dead Link Patterns (Analysis)

**Pattern 1: Archived lessons still referenced**
- 15 links to lesson-012, lesson-015, lesson-018 (all archived)
- **Fix:** Update links to replacement lessons or remove

**Pattern 2: Renamed vault entries**
- 8 links to old slug format (hyphenated vs underscored)
- **Fix:** Bulk update to new slug format

**Pattern 3: Moved patterns**
- 3 links to /old-location/patterns/
- **Fix:** Update to current /patterns/library/ location

---

## Anchor Link Issues (Deep Validation)

### Broken Anchors

- **lesson-015** → #the-pattern: ✗ Heading not found
  - Expected: `## The Pattern`
  - Actual: `## Pattern Example` (heading changed)
  - **Fix:** Update anchor or heading

### Invalid Anchor Slugs

- **pattern:sprite-basics** → #memory-usage: ✗ Invalid slug
  - Expected: `## Memory Usage` → slug: `#memory-usage`
  - Actual heading: `## Memory & Usage` → slug: `#memory--usage`
  - **Fix:** Update anchor link to `#memory--usage`

---

## Recommendations

### Immediate Actions (Critical)

1. Fix 25 broken links (lessons → patterns/vault)
2. Create 3 missing lessons (012, 015, 018) or update curriculum
3. Fix 5 renamed vault entry links

### Short-term Actions (High, within 1 week)

1. Update 15 pattern `lessonsAppearIn` metadata mismatches
2. Add 20 bidirectional vault links
3. Resolve 5 curriculum mismatches

### Medium-term Actions (Medium, within 1 month)

1. Add references to 10 orphaned patterns
2. Update 8 links to renamed vault entries
3. Archive 5 orphaned vault entries

### Long-term Actions (Low, opportunistic)

1. Review 15 orphaned lessons (archive or restore)
2. Standardize vault slug format project-wide
3. Establish link validation CI check

---

## Validation Methodology

**Scope:** {platforms, content types}
**Depth:** {quick|standard|deep}
**Duration:** {minutes}
**Files Scanned:** {N}
**Links Checked:** {N}

**Next Validation:** Recommend {date} or after major content changes

---

**Generated by:** cross-reference-validator-agent
**Health Score:** {percentage}%
```

**Step 17:** Generate fix script (optional)

**For bulk fixes:**

```bash
#!/bin/bash
# Generated by cross-reference-validator-agent
# Apply fixes for common broken links

# Fix 1: Update archived lesson links
find /website/src/pages/ -name "*.mdx" -exec sed -i 's|/lesson-012|/lesson-012-replacement|g' {} \;

# Fix 2: Update renamed vault entries
find /website/src/pages/ -name "*.mdx" -exec sed -i 's|/vault/old-slug|/vault/new-slug|g' {} \;

# Fix 3: Update moved patterns
find /website/src/pages/ -name "*.mdx" -exec sed -i 's|/old-location/patterns/|/patterns/library/|g' {} \;

echo "Bulk fixes applied. Review changes with git diff before committing."
```

---

## Skills Used

None (standalone comprehensive validation)

---

## Error Handling

### Error Scenarios

**Error 1: No content found**
```
AGENT FAILED at Step 1 (discovery)

FAILED:
✗ No lesson files found in /website/src/pages/

SUGGESTED FIX:
- Verify file paths correct
- Check content exists
```

**Error 2: Validation timeout**
```
AGENT TIMEOUT at Step 12 (curriculum validation)

COMPLETED:
✓ Lesson link validation (500 lessons)
✓ Pattern metadata validation (150 patterns)
✗ Curriculum validation (timed out after 300 lessons)

RESULT:
Partial validation completed

SUGGESTED ACTION:
- Use DEPTH: quick for large scans
- Split validation by platform
```

---

## Invocation Patterns

### Full Validation

```javascript
{
  subagent_type: "general-purpose",
  description: "Validate all cross-references",
  prompt: `CROSS-REFERENCE VALIDATION:

VALIDATE_ALL: true
DEPTH: standard

Use cross-reference-validator-agent to:
1. Discover all lessons, patterns, vault entries, curriculum docs
2. Extract all internal links
3. Validate file existence
4. Check metadata accuracy (lessonsAppearIn)
5. Verify bidirectional links
6. Generate comprehensive report

Expected duration: ~15 minutes for 500+ files`
}
```

### Platform-Specific

```javascript
{
  subagent_type: "general-purpose",
  description: "Validate C64 cross-references",
  prompt: `CROSS-REFERENCE VALIDATION:

PLATFORM: "C64"
PHASES: [0, 1]
DEPTH: deep

Validate all cross-references for C64 only, including anchor links and orphaned content detection.`
}
```

### Quick Check

```javascript
{
  subagent_type: "general-purpose",
  description: "Quick link health check",
  prompt: `CROSS-REFERENCE VALIDATION:

VALIDATE_ALL: true
DEPTH: quick

Quick validation (file existence only) for all content. Report broken links only.

Expected duration: ~5 minutes`
}
```

---

## Testing Checklist

Before production use, test with:

**Test 1: Known broken link**
- Input: Lesson with link to non-existent pattern
- Expected: Agent detects broken link, reports in "Broken Links" section

**Test 2: Metadata mismatch**
- Input: Pattern with `lessonsAppearIn: 15` but lesson-015 doesn't link to it
- Expected: Agent detects mismatch, reports in "Metadata Mismatches"

**Test 3: Missing bidirectional link**
- Input: Vault entry A → B but B doesn't link back to A
- Expected: Agent detects, reports in "Bidirectional Link Issues"

**Test 4: Orphaned content**
- Input: Pattern with zero incoming links
- Expected: Agent detects, reports in "Orphaned Content"

**Test 5: Curriculum mismatch**
- Input: Curriculum expects lesson-012 but file archived
- Expected: Agent detects, reports in "Curriculum Mismatches"

**Test 6: Large scale**
- Input: Full site (500+ files)
- Expected: Completes within timeout, generates report

---

## Agent Autonomy

**High autonomy - No user intervention during execution:**
- Discovers all content automatically
- Extracts all links
- Validates comprehensively
- Identifies patterns
- Generates detailed report

**User provides:**
- Validation scope
- Validation depth

**User reviews after completion:**
- Health score
- Comprehensive report
- Broken link list
- Fix recommendations

---

## Production Notes

### Validation Frequency

**Recommended schedule:**
- **Quick validation:** After every major content change
- **Standard validation:** Weekly (automated)
- **Deep validation:** Monthly (comprehensive audit)

### Health Score Interpretation

**95-100%:** Excellent - Minor orphaned content only
**85-94%:** Good - Some metadata mismatches, no critical broken links
**70-84%:** Fair - Multiple broken links, needs attention
**< 70%:** Poor - Extensive link rot, immediate action required

### Integration with CI/CD

**Consider automated validation:**
```yaml
# .github/workflows/validate-links.yml
on:
  pull_request:
  schedule:
    - cron: '0 0 * * 0'  # Weekly

jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - run: invoke cross-reference-validator-agent
      - fail-if: health-score < 85%
```

---

## Integration with Other Agents

**cross-reference-validator-agent** complements:

**curriculum-audit-agent:**
- curriculum-audit checks file existence
- cross-reference-validator checks link consistency

**After archiving lessons (lesson-archiving skill):**
- Run cross-reference-validator to find links to archived lessons
- Update links systematically

**Calls other agents:**
- (None - standalone validation)

---

## The Bottom Line

**cross-reference-validator-agent provides comprehensive link integrity:**
- Validates lessons → patterns, patterns → lessons, vault → vault, curriculum → lessons
- Checks metadata accuracy (`lessonsAppearIn`)
- Verifies bidirectional links
- Detects orphaned content
- Identifies dead link patterns
- Generates health score and detailed report

**Use when:**
- Regular maintenance (weekly/monthly)
- After major content changes
- Before releases
- Suspected link rot

**Produces:**
- Comprehensive validation report (markdown)
- Health score (0-100%)
- Prioritized fix recommendations
- Optional bulk fix script

**Health score > 85% = good, < 70% = needs immediate attention. Systematic link validation prevents user frustration from 404 errors.**

---

**Status:** Specification complete, not yet tested in production
**Next steps:** Test with real content (C64 Phase 0), refine link extraction patterns, validate fix script generation
