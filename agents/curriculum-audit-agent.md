# Curriculum Audit Agent

**Version:** 1.0
**Status:** Specification complete, not yet tested
**Priority:** P2 (Medium - Maintenance)

---

## Purpose

Comprehensive curriculum audit scanning all lessons, files, navigation, and cross-references for issues. The agent detects missing files, broken links, curriculum misalignment, orphaned files, coverage gaps, and validation failures across the entire project.

**Think:** "Health check on entire curriculum" → Agent scans 500+ lessons, validates all files exist, checks all links work, identifies gaps, reports issues with priorities.

---

## When to Use

Use this agent when:
- After major curriculum changes (new phase, platform expansion)
- Periodic maintenance (monthly/quarterly health check)
- Before major releases
- Suspected structural issues (broken links, missing files)
- Auditing coverage across platforms

**Do NOT use when:**
- Just created single lesson (use lesson-validation skill instead)
- Only checking specific file (Read tool faster)
- Real-time validation during development (too slow)

---

## Inputs Required

### Audit Scope

**Option A: Full audit (all platforms, all phases)**
```
SCAN_ALL: true
```

**Option B: Single platform**
```
PLATFORM: "C64"
PHASES: [0, 1]
```

**Option C: Single phase across platforms**
```
PHASE: 0
ALL_PLATFORMS: true
```

### Audit Depth

**Quick audit (structural only):**
```
AUDIT_DEPTH: quick
- File existence checks
- Navigation link validation
- No content validation
- ~5 minutes for 500 lessons
```

**Standard audit (structural + basic validation):**
```
AUDIT_DEPTH: standard
- File existence
- Navigation links
- Code compilation (spot check 10%)
- British English (spot check 10%)
- ~15 minutes for 500 lessons
```

**Deep audit (comprehensive validation):**
```
AUDIT_DEPTH: deep
- All structural checks
- Code compilation (all lessons)
- Screenshot verification (all lessons)
- British English (all lessons)
- Curriculum alignment (all lessons)
- ~60 minutes for 500 lessons
```

### Issue Priorities

**Priority levels:**
```
CRITICAL: Lesson completely broken (missing files, won't compile)
HIGH: Navigation broken, incorrect curriculum alignment
MEDIUM: British English errors, missing screenshots
LOW: Optimization suggestions, coverage gaps
```

**Filter by priority:**
```
REPORT_PRIORITY: "CRITICAL,HIGH"  (only show critical/high issues)
```

---

## Workflow Steps

### Phase 1: Discovery and Inventory

**Step 1:** Discover all curriculum documents

```bash
find /docs -name "PHASE-*-CURRICULUM.md"
```

**Build inventory:**
- Platform name
- Phase number
- Expected lesson count (from curriculum spec)

**Step 2:** Discover all lesson files

For each platform/phase:
```bash
find /website/src/pages/{platform}/phase-{N}/ -name "lesson-*.mdx"
```

**Build lesson inventory:**
- Platform
- Phase
- Tier
- Lesson number
- File path

**Step 3:** Discover all code sample directories

```bash
find /code-samples/{platform}/phase-{N}/ -type d -name "lesson-*"
```

**Build code sample inventory:**
- Platform
- Phase
- Tier
- Lesson number
- Directory path
- Code files found

**Step 4:** Discover all screenshot directories

```bash
find /website/public/images/{platform}/phase-{N}/ -type d -name "lesson-*"
```

**Build screenshot inventory:**
- Platform
- Phase
- Tier
- Lesson number
- Directory path
- Screenshot files found

**Step 5:** Discover all navigation files

```bash
# Tier indexes
find /website/src/pages/{platform}/phase-{N}/ -name "tier-*.astro"

# Phase indexes
find /website/src/pages/{platform}/ -name "phase-*.astro"

# Platform indexes
find /website/src/pages/ -name "{platform}.astro"
```

**Build navigation inventory:**
- Navigation level (tier/phase/platform)
- File path
- Lessons listed

### Phase 2: Structural Validation

**Step 6:** Check for missing lesson files

For each lesson in curriculum:
```bash
# Expected: /website/src/pages/{platform}/phase-{N}/tier-{N}/lesson-{NNN}.mdx
if [ ! -f "${expected_path}" ]; then
  log "CRITICAL: Missing lesson file: ${expected_path}"
fi
```

**Step 7:** Check for missing code samples

For each lesson MDX:
```bash
# Expected: /code-samples/{platform}/phase-{N}/tier-{N}/lesson-{NNN}/
if [ ! -d "${expected_path}" ]; then
  log "HIGH: Missing code sample directory: ${expected_path}"
fi

# Check for code files inside directory
if [ -d "${expected_path}" ]; then
  file_count=$(find "${expected_path}" -name "*.bas" -o -name "*.asm" | wc -l)
  if [ "$file_count" -eq 0 ]; then
    log "HIGH: Code sample directory empty: ${expected_path}"
  fi
fi
```

**Step 8:** Check for missing screenshots

For each lesson MDX:
```bash
# Expected: /website/public/images/{platform}/phase-{N}/tier-{N}/lesson-{NNN}/
if [ ! -d "${expected_path}" ]; then
  log "MEDIUM: Missing screenshot directory: ${expected_path}"
fi

# Check for screenshot files
if [ -d "${expected_path}" ]; then
  file_count=$(find "${expected_path}" -name "*.png" | wc -l)
  if [ "$file_count" -eq 0 ]; then
    log "MEDIUM: Screenshot directory empty: ${expected_path}"
  fi
fi
```

**Step 9:** Check navigation link integrity

For each navigation file (tier/phase/platform):

1. Parse lessons array from Astro file
2. For each lesson listed:
   ```bash
   # Check lesson file exists
   lesson_path="/website/src/pages/{platform}/{phase}/{tier}/lesson-{N}.mdx"
   if [ ! -f "${lesson_path}" ]; then
     log "HIGH: Broken navigation link: ${lesson_path} (referenced in ${nav_file})"
   fi
   ```

3. Check for duplicate lesson numbers
4. Check for lesson number gaps (e.g., 1, 2, 4, 5 - missing 3)

**Step 10:** Check for orphaned files

**Orphaned lesson files:**
```bash
# Lesson MDX exists but not in any navigation file
for lesson_file in $(find /website/src/pages/{platform}/ -name "lesson-*.mdx"); do
  if ! grep -r "${lesson_number}" /website/src/pages/{platform}/*/tier-*.astro; then
    log "MEDIUM: Orphaned lesson file: ${lesson_file} (not in navigation)"
  fi
done
```

**Orphaned code samples:**
```bash
# Code sample directory exists but no corresponding lesson MDX
for code_dir in $(find /code-samples/{platform}/ -type d -name "lesson-*"); do
  lesson_number=$(extract_number)
  if [ ! -f "/website/src/pages/{platform}/.../lesson-${lesson_number}.mdx" ]; then
    log "LOW: Orphaned code samples: ${code_dir}"
  fi
done
```

**Orphaned screenshots:**
```bash
# Screenshot directory exists but no corresponding lesson MDX
for screenshot_dir in $(find /website/public/images/{platform}/ -type d -name "lesson-*"); do
  lesson_number=$(extract_number)
  if [ ! -f "/website/src/pages/{platform}/.../lesson-${lesson_number}.mdx" ]; then
    log "LOW: Orphaned screenshots: ${screenshot_dir}"
  fi
done
```

### Phase 3: Content Validation

**Step 11:** Curriculum alignment check (if AUDIT_DEPTH >= standard)

For sample of lessons (10% quick, 100% deep):

1. Read curriculum spec for lesson
2. Read lesson MDX
3. Use **curriculum-alignment-check** skill
4. Report misalignment issues:
   ```
   HIGH: Lesson {N} curriculum mismatch
   - Curriculum says: "Sprite collision detection"
   - Lesson teaches: "Sprite animation"
   - RECOMMENDATION: Archive lesson, create new aligned lesson
   ```

**Step 12:** Code compilation check (if AUDIT_DEPTH >= standard)

For sample of code samples (10% quick, 100% deep):

1. Find compilation command for platform
2. Attempt compilation
3. Report failures:
   ```
   CRITICAL: Lesson {N} code won't compile
   - File: example-1.bas
   - Error: Syntax error line 25
   - RECOMMENDATION: Fix syntax error and recompile
   ```

**Step 13:** Screenshot verification (if AUDIT_DEPTH == deep)

For all lessons with screenshots:

1. Use **screenshot-verification** skill
2. Read screenshot with READ tool
3. Verify expected elements present
4. Report issues:
   ```
   MEDIUM: Lesson {N} screenshot verification failed
   - Expected: Sprite visible on screen
   - Actual: Blank screen
   - RECOMMENDATION: Recapture screenshot
   ```

**Step 14:** British English check (if AUDIT_DEPTH >= standard)

For sample of lessons (10% quick, 100% deep):

1. Use **british-english-check** skill
2. Report American spellings:
   ```
   MEDIUM: Lesson {N} American spelling detected
   - Line 45: "color" should be "colour"
   - Line 78: "behavior" should be "behaviour"
   - RECOMMENDATION: Apply british-english-check skill fixes
   ```

**Step 15:** Voice/tone check (if AUDIT_DEPTH == deep)

For all lessons:

1. Use **voice-tone-check** skill
2. Report violations:
   ```
   LOW: Lesson {N} voice/tone violation
   - Line 12: "WOW Moment" section (forbidden)
   - Line 34: "amazing" (marketing speak)
   - RECOMMENDATION: Apply voice-tone-check skill fixes
   ```

### Phase 4: Coverage Analysis

**Step 16:** Platform coverage comparison

Compare lesson counts across platforms:
```
PLATFORM COVERAGE:

C64:
- Phase 0: 64 lessons (100% of 64 planned)
- Phase 1: 32 lessons (50% of 64 planned)
- Total: 96 lessons

ZX Spectrum:
- Phase 0: 32 lessons (100% of 32 planned)
- Total: 32 lessons

NES:
- Phase 1: 16 lessons (25% of 64 planned)
- Total: 16 lessons

COVERAGE GAPS:
- HIGH: ZX Spectrum Phase 1 not started (0%)
- HIGH: NES Phase 1 incomplete (25%)
- MEDIUM: C64 Phase 1 incomplete (50%)
```

**Step 17:** Concept coverage analysis

Parse all lessons for concepts:
- Which concepts covered by multiple platforms?
- Which concepts missing from specific platforms?
- Which concepts over-represented?

```
CONCEPT COVERAGE:

Universal concepts (all platforms):
✓ loop, variable, score, joystick

Platform gaps:
⚠ "sprite collision" - C64 ✓, NES ✓, ZX Spectrum ✗
⚠ "sound effects" - C64 ✓, ZX Spectrum ✓, NES ✗
```

**Step 18:** Difficulty progression analysis

Check if difficulty increases properly within tiers:
```
DIFFICULTY PROGRESSION:

C64 Phase 0 Tier 1:
✓ Lessons 1-10: Steady progression (5-10-15-20 line complexity)
⚠ Lesson 11: Sudden jump (5 lines → 40 lines)
  RECOMMENDATION: Insert intermediate lesson

C64 Phase 0 Tier 2:
✓ Smooth progression
```

### Phase 5: Report Generation

**Step 19:** Generate audit report

```markdown
# Curriculum Audit Report

**Date:** {YYYY-MM-DD}
**Scope:** {platforms, phases}
**Audit Depth:** {quick|standard|deep}
**Lessons Scanned:** {N}
**Issues Found:** {N}

---

## Executive Summary

**Health Score:** {percentage}% ({N} critical, {N} high, {N} medium, {N} low issues)

**Critical Issues:** {N} (require immediate attention)
**High Issues:** {N} (fix before next release)
**Medium Issues:** {N} (fix during next maintenance cycle)
**Low Issues:** {N} (address opportunistically)

---

## Critical Issues (Blocking)

### Missing Lesson Files

- **Lesson:** C64 Phase 0 Tier 2 Lesson 015
- **Expected:** `/website/src/pages/commodore-64/phase-0/tier-2/lesson-015.mdx`
- **Status:** Missing
- **Impact:** Broken navigation link, curriculum gap
- **Fix:** Create lesson or update navigation to skip

### Code Won't Compile

- **Lesson:** C64 Phase 0 Tier 1 Lesson 008
- **File:** `example-2.bas`
- **Error:** Syntax error line 25
- **Impact:** Lesson code unusable
- **Fix:** Correct syntax error and recompile

---

## High Issues (Important)

### Broken Navigation Links

- **Navigation:** `/website/src/pages/commodore-64/phase-0/tier-2.astro`
- **Broken Link:** Lesson 018 (file doesn't exist)
- **Impact:** 404 error for users
- **Fix:** Remove lesson 018 from navigation or create file

### Missing Code Samples

- **Lesson:** ZX Spectrum Phase 0 Tier 1 Lesson 005
- **Expected:** `/code-samples/zx-spectrum/phase-0/tier-1/lesson-005/`
- **Status:** Directory missing
- **Impact:** Lesson has no downloadable code
- **Fix:** Create code samples directory with examples

### Curriculum Misalignment

- **Lesson:** C64 Phase 0 Tier 1 Lesson 012
- **Curriculum Says:** "Joystick input basics"
- **Lesson Teaches:** "Keyboard input"
- **Impact:** Curriculum progression broken
- **Fix:** Archive lesson, create new joystick lesson

---

## Medium Issues (Quality)

### Missing Screenshots

- **Lesson:** NES Phase 1 Tier 1 Lesson 003
- **Expected:** `/website/public/images/nintendo-entertainment-system/phase-1/tier-1/lesson-003/`
- **Status:** Directory empty
- **Impact:** Lesson has no visual examples
- **Fix:** Capture screenshots and populate directory

### British English Errors

- **Lesson:** C64 Phase 0 Tier 2 Lesson 020
- **Errors:** 3 American spellings detected
  - Line 45: "color" → "colour"
  - Line 67: "behavior" → "behaviour"
  - Line 89: "optimize" → "optimise"
- **Impact:** Inconsistent voice
- **Fix:** Apply british-english-check skill

---

## Low Issues (Enhancements)

### Orphaned Files

- **File:** `/code-samples/commodore-64/phase-0/tier-1/lesson-099/`
- **Status:** No corresponding lesson MDX
- **Impact:** Unused files taking space
- **Fix:** Delete orphaned directory or create lesson

### Coverage Gaps

- **Platform:** ZX Spectrum
- **Gap:** Phase 1 not started (0 of 64 lessons)
- **Impact:** Platform incomplete
- **Fix:** Create ZX Spectrum Phase 1 curriculum

### Voice/Tone Violations

- **Lesson:** C64 Phase 0 Tier 1 Lesson 007
- **Violations:** 2 instances of marketing speak
  - Line 12: "amazing" → remove or replace
  - Line 34: "wow moment" section → remove section
- **Impact:** Minor voice inconsistency
- **Fix:** Apply voice-tone-check skill

---

## Coverage Statistics

### By Platform

| Platform | Phases | Lessons | Complete | Critical Issues | High Issues |
|----------|--------|---------|----------|-----------------|-------------|
| C64 | 2 | 96 | 75% | 2 | 5 |
| ZX Spectrum | 1 | 32 | 100% | 0 | 1 |
| NES | 1 | 16 | 25% | 1 | 3 |
| Amiga | 0 | 0 | 0% | 0 | 0 |

### By Issue Type

| Type | Critical | High | Medium | Low | Total |
|------|----------|------|--------|-----|-------|
| Missing Files | 5 | 8 | 12 | 3 | 28 |
| Broken Links | 2 | 6 | 0 | 0 | 8 |
| Compilation | 3 | 0 | 0 | 0 | 3 |
| British English | 0 | 0 | 15 | 0 | 15 |
| Curriculum | 0 | 4 | 2 | 0 | 6 |
| Orphaned | 0 | 0 | 0 | 8 | 8 |
| Coverage | 0 | 0 | 0 | 5 | 5 |

---

## Recommendations

### Immediate Actions (Critical)

1. Fix compilation errors in 3 lessons
2. Create 5 missing lesson files or update navigation
3. Verify all navigation links resolve

### Short-term Actions (High, within 1 week)

1. Fix 6 broken navigation links
2. Create 8 missing code sample directories
3. Resolve 4 curriculum misalignment issues

### Medium-term Actions (Medium, within 1 month)

1. Capture 12 missing screenshot sets
2. Fix 15 British English errors
3. Resolve 2 curriculum alignment issues

### Long-term Actions (Low, opportunistic)

1. Clean up 8 orphaned file sets
2. Address 5 coverage gaps
3. Fix minor voice/tone violations

---

## Audit Methodology

**Scope:** {platforms scanned}
**Depth:** {quick|standard|deep}
**Duration:** {minutes}
**Lessons Scanned:** {N}
**Files Checked:** {N}

**Validation Tools:**
- lesson-validation skill
- curriculum-alignment-check skill
- screenshot-verification skill
- british-english-check skill
- voice-tone-check skill

**Next Audit:** Recommend {date} (or after major curriculum changes)

---

**Generated by:** curriculum-audit-agent
**Health Score:** {percentage}%
```

**Step 20:** Generate issue CSV for tracking

```csv
Priority,Type,Platform,Phase,Tier,Lesson,File,Issue,Fix
CRITICAL,Missing File,C64,0,2,15,lesson-015.mdx,File doesn't exist,Create lesson or update nav
CRITICAL,Compilation,C64,0,1,8,example-2.bas,Syntax error line 25,Fix syntax
HIGH,Broken Link,C64,0,2,18,tier-2.astro,Link to non-existent lesson,Remove from nav or create
HIGH,Missing Code,ZX,0,1,5,lesson-005,No code samples directory,Create directory with code
...
```

---

## Skills Used

### lesson-validation (Comprehensive lesson checks)
- Location: `/docs/skills/lesson-validation/SKILL.md`
- When: During content validation (if AUDIT_DEPTH >= standard)
- Purpose: Validate individual lessons

### curriculum-alignment-check (Alignment verification)
- Location: `/docs/skills/curriculum-alignment-check/SKILL.md`
- When: During content validation (if AUDIT_DEPTH >= standard)
- Purpose: Check lessons match curriculum specs

### screenshot-verification (Screenshot validation)
- Location: `/docs/skills/screenshot-verification/SKILL.md`
- When: During deep audit (AUDIT_DEPTH == deep)
- Purpose: Verify screenshots show expected content

### british-english-check (Language validation)
- Location: `/docs/skills/british-english-check/SKILL.md`
- When: During content validation (if AUDIT_DEPTH >= standard)
- Purpose: Detect American spellings

### voice-tone-check (Voice validation)
- Location: `/docs/skills/voice-tone-check/SKILL.md`
- When: During deep audit (AUDIT_DEPTH == deep)
- Purpose: Detect marketing speak and tone violations

---

## Error Handling

### Error Scenarios

**Error 1: No curriculum documents found**
```
AGENT FAILED at Step 1 (discovery)

FAILED:
✗ No PHASE-*-CURRICULUM.md files found

SUGGESTED FIX:
- Verify curriculum documents exist in /docs/{platform}/
- Check file naming convention
```

**Error 2: Audit timeout (too many lessons)**
```
AGENT TIMEOUT at Step 12 (code compilation)

COMPLETED:
✓ Structural validation (all lessons)
✗ Content validation (timed out after 300 lessons)

RESULT:
Partial audit completed (structural only)

SUGGESTED ACTION:
- Use AUDIT_DEPTH: quick for large scans
- OR split audit by platform
- OR increase timeout limit
```

**Error 3: Skill not found**
```
AGENT WARNING at Step 11 (curriculum alignment)

WARNING:
⚠ curriculum-alignment-check skill not found
⚠ Skipping curriculum alignment checks

COMPLETED:
✓ Structural validation
⊗ Content validation (partial - skipped alignment)

RESULT:
Audit incomplete (curriculum alignment not checked)
```

---

## Invocation Patterns

### Quick Audit (Structural Only)

```javascript
{
  subagent_type: "general-purpose",
  description: "Quick curriculum health check",
  prompt: `CURRICULUM AUDIT:

SCAN_ALL: true
AUDIT_DEPTH: quick

Use curriculum-audit-agent to:
1. Check all lesson files exist
2. Validate navigation links
3. Find orphaned files
4. Report critical/high issues only
5. Generate health score

Expected duration: ~5 minutes`
}
```

### Standard Audit (Structural + Sampling)

```javascript
{
  subagent_type: "general-purpose",
  description: "Standard curriculum audit",
  prompt: `CURRICULUM AUDIT:

SCAN_ALL: true
AUDIT_DEPTH: standard

Use curriculum-audit-agent to:
1. Full structural validation
2. Sample 10% code compilation
3. Sample 10% British English check
4. Sample 10% curriculum alignment
5. Generate comprehensive report

Expected duration: ~15 minutes`
}
```

### Deep Audit (Comprehensive)

```javascript
{
  subagent_type: "general-purpose",
  description: "Deep curriculum audit (all validations)",
  prompt: `CURRICULUM AUDIT:

PLATFORM: "C64"
PHASES: [0, 1]
AUDIT_DEPTH: deep

Use curriculum-audit-agent to:
1. Full structural validation
2. Compile ALL code samples
3. Verify ALL screenshots
4. Check ALL lessons for British English
5. Validate ALL lessons against curriculum
6. Check voice/tone for ALL lessons
7. Generate detailed report with CSV

Expected duration: ~60 minutes for 96 C64 lessons`
}
```

### Platform-Specific Audit

```javascript
{
  subagent_type: "general-purpose",
  description: "Audit ZX Spectrum only",
  prompt: `CURRICULUM AUDIT:

PLATFORM: "ZX Spectrum"
PHASES: [0]
AUDIT_DEPTH: standard
REPORT_PRIORITY: "CRITICAL,HIGH"

Audit ZX Spectrum Phase 0 only, report critical/high issues.`
}
```

---

## Testing Checklist

Before production use, test with:

**Test 1: Small scope (single tier)**
- Input: Platform C64, Phase 0, Tier 1 only
- Expected: Audit completes quickly, finds known issues

**Test 2: Missing files**
- Input: Temporarily rename lesson file
- Expected: Agent detects missing file, reports as CRITICAL

**Test 3: Broken navigation link**
- Input: Temporarily break navigation link
- Expected: Agent detects broken link, reports as HIGH

**Test 4: Compilation error**
- Input: Temporarily introduce syntax error in code
- Expected: Agent detects compilation failure, reports as CRITICAL

**Test 5: Quick vs deep audit**
- Input: Same scope, AUDIT_DEPTH: quick vs deep
- Expected: Quick completes faster, deep finds more issues

**Test 6: Orphaned files**
- Input: Create code sample directory with no lesson MDX
- Expected: Agent detects orphaned directory, reports as LOW

**Test 7: Report generation**
- Input: Any audit
- Expected: Generates markdown report + CSV issue list

---

## Agent Autonomy

**High autonomy - No user intervention during execution:**
- Discovers all files automatically
- Validates structure and content
- Prioritizes issues automatically
- Generates comprehensive report

**User provides:**
- Audit scope
- Audit depth (quick/standard/deep)
- Optional priority filter

**User reviews after completion:**
- Health score
- Issue report (prioritized)
- Recommendations
- CSV issue tracker

---

## Production Notes

### Audit Frequency

**Recommended schedule:**
- **Quick audit:** Weekly (automated)
- **Standard audit:** Monthly (before releases)
- **Deep audit:** Quarterly (comprehensive health check)

### Health Score Interpretation

**95-100%:** Excellent - Minor issues only
**85-94%:** Good - Some medium issues, no blockers
**70-84%:** Fair - Multiple high issues, needs attention
**< 70%:** Poor - Critical issues, immediate action required

### Issue Triage

**Triage workflow after audit:**
1. **Critical issues:** Fix immediately (blocking)
2. **High issues:** Schedule for next sprint
3. **Medium issues:** Add to backlog
4. **Low issues:** Address opportunistically

### CSV Issue Tracking

Import CSV into issue tracker (GitHub, Jira, etc.):
- Create tickets automatically from CSV
- Track fix progress
- Re-audit to verify fixes

---

## Integration with Other Agents

**curriculum-audit-agent** calls other agents for fixes:

**Calls lesson-creation-agent:**
- Detects missing lesson (curriculum gap)
- Suggests: "Run lesson-creation-agent to create lesson {N}"

**Calls navigation-update-agent:**
- Detects broken navigation links
- Suggests: "Run navigation-update-agent to rebuild indexes"

**Calls concept-mapping-agent:**
- Detects concept coverage gaps
- Suggests: "Run concept-mapping-agent to update cross-reference"

**Calls pattern-extraction-agent:**
- Detects lessons with undocumented patterns
- Suggests: "Run pattern-extraction-agent to extract patterns"

---

## The Bottom Line

**curriculum-audit-agent provides comprehensive health checks:**
- Scans all lessons for missing files, broken links, validation failures
- Identifies coverage gaps and orphaned files
- Validates content quality (compilation, British English, alignment)
- Generates prioritized issue report with health score

**Use when:**
- Regular maintenance (weekly/monthly/quarterly)
- After major curriculum changes
- Before releases
- Suspected structural issues

**Produces:**
- Comprehensive audit report (markdown)
- Issue CSV for tracking
- Health score (0-100%)
- Prioritized recommendations

**Health score > 85% = good, < 70% = needs immediate attention. Use issue CSV to track fixes systematically.**

---

**Status:** Specification complete, not yet tested in production
**Next steps:** Test quick audit on C64 Phase 0, validate issue prioritization, test CSV generation
