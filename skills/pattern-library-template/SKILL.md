---
name: pattern-library-template
description: Use when creating Pattern Library entries for reusable code techniques - provides mandatory structure, frontmatter fields, section requirements, and variation guidelines
---

# Pattern Library Template

## Overview

Pattern Library entries document reusable code techniques that appear across multiple lessons. Each pattern follows a comprehensive structure with working code examples, multiple variations, and complete integration examples.

**Patterns are NOT quick tips.** They are complete, authoritative references for specific techniques.

## When to Use

Use when:
- Creating new Pattern Library entry
- Reviewing existing pattern for completeness
- Expanding stub patterns
- Extracting patterns from completed lessons

**Do NOT:**
- Create shallow "tips and tricks" entries
- Skip required sections
- Provide only one variation
- Forget integration example
- Use American English spellings

## Entry Structure

### Required Frontmatter

```yaml
---
layout: ../../../../../layouts/PatternLayout.astro
title: {Pattern Name}
category: {Category}
difficulty: {Easy|Medium|Hard|Expert}
lessonsAppearIn: {lesson numbers, comma-separated}
system: {C64|NES|ZX Spectrum|Amiga|Universal}
---
```

**Field Requirements:**

**`layout`:** Always `../../../../../layouts/PatternLayout.astro`

**`title`:** (REQUIRED)
- Descriptive pattern name
- Proper capitalization
- Examples: "Score Display", "Sprite Multiplexing", "Raster Interrupt Setup"

**`category`:** (REQUIRED)
- One of: Game Mechanics, Graphics, Sound, Input, Memory Management, Performance, Architecture
- Proper capitalization

**`difficulty`:** (REQUIRED)
- Easy: Basic techniques, single concept
- Medium: Multiple concepts, moderate complexity
- Hard: Advanced hardware use, timing-critical
- Expert: Complex multi-system coordination

**`lessonsAppearIn`:** (REQUIRED)
- Comma-separated lesson numbers
- Examples: `15, 20, 25` or `8` (single lesson)
- Must list ALL lessons where pattern appears

**`system`:** (REQUIRED)
- Platform-specific: "C64", "NES", "ZX Spectrum", "Amiga"
- Cross-platform: "Universal" (BASIC patterns that work everywhere)

### Required Sections

All pattern entries must have these sections (in order):

#### 1. Overview (REQUIRED)

```markdown
## Overview
{2-4 sentences explaining what problem this pattern solves and why it matters}
```

**Guidelines:**
- Opens with problem statement
- Explains when you'd use this pattern
- Brief mention of key benefit
- British English

**Example (Good):**
```markdown
## Overview
Displaying a score requires converting a numeric value to screen characters and updating specific memory locations. This pattern shows how to maintain a score variable, format it for display, and update the screen efficiently without flickering.
```

**Example (Bad):**
```markdown
## Overview
This shows how to do scores.
```

#### 2. The Pattern (REQUIRED)

```markdown
## The Pattern
{Canonical code example showing the core technique - 10-20 lines}
```

**Guidelines:**
- Complete, working code
- Heavily commented
- Shows core technique only (no extra features)
- Platform-appropriate syntax
- British English in comments

**Example:**
```markdown
## The Pattern

\`\`\`basic
100 SCORE=0
110 PRINT CHR$(147)  : REM clear screen
120 PRINT "SCORE:";SCORE
130 :
140 REM game loop
150 SCORE=SCORE+10
160 POKE 214,0 : PRINT  : REM cursor to top
170 PRINT "SCORE:";SCORE
180 GOTO 150
\`\`\`
```

#### 3. Parameters (REQUIRED if applicable)

```markdown
## Parameters

| Parameter | Type | Range | Purpose |
|-----------|------|-------|---------|
| {name} | {type} | {range} | {what it does} |
```

**Guidelines:**
- Table format (markdown)
- All configurable values documented
- Realistic ranges
- Clear purpose descriptions

**Skip this section if:**
- Pattern has no configurable parameters (simple techniques)
- All values are constants

#### 4. How It Works (REQUIRED)

```markdown
## How It Works

{Step-by-step breakdown explaining the technique in detail}
```

**Guidelines:**
- Number steps (1, 2, 3...)
- Explain WHY, not just WHAT
- Reference specific line numbers
- Cover edge cases
- Technical accuracy (hardware specifics if relevant)
- British English

**Example:**
```markdown
## How It Works

1. **Initialise score variable** (line 100) - Starts at zero
2. **Display initial value** (line 120) - Shows "SCORE:0" on screen
3. **Increment score** (line 150) - Adds points when event occurs
4. **Reposition cursor** (line 160) - POKE 214,0 sets cursor to top row
5. **Update display** (line 170) - Prints new score over old value
```

#### 5. Variations (REQUIRED - minimum 3)

```markdown
## Variations

### {Variation Name 1}
{Description and code example}

### {Variation Name 2}
{Description and code example}

### {Variation Name 3}
{Description and code example}
```

**Guidelines:**
- Minimum 3 variations (6+ for complex patterns)
- Each variation addresses different use case
- Complete code for each
- Explain trade-offs
- Real-world scenarios

**Variation Types:**
- Different data types (byte vs word)
- Different speeds (fast vs memory-efficient)
- Different platforms (if Universal pattern)
- Different scales (single vs multiple instances)
- With/without specific hardware features

**Example:**
```markdown
## Variations

### Leading Zeros
Displays score with leading zeros (00150 instead of 150):
\`\`\`basic
...
\`\`\`

### Multi-digit with Formatting
Adds commas for readability (1,000 instead of 1000):
\`\`\`basic
...
\`\`\`

### Assembly Optimised
Faster version using 6510 assembly:
\`\`\`asm
...
\`\`\`
```

#### 6. Common Mistakes (REQUIRED)

```markdown
## Common Mistakes

### {Mistake Name}
**Symptom:** {what you see}
**Cause:** {why it happens}
**Fix:** {how to correct it}
```

**Guidelines:**
- List 3-5 common mistakes
- Always include Symptom, Cause, Fix
- Real mistakes from actual code
- Specific, not vague
- British English

**Example:**
```markdown
## Common Mistakes

### Flickering Score
**Symptom:** Score flashes on and off rapidly
**Cause:** Clearing entire screen instead of just score area
**Fix:** Use cursor positioning (POKE 214) to overwrite score location only

### Overflow Errors
**Symptom:** Score becomes negative or wraps to zero
**Cause:** Variable exceeds 16-bit limit (65535)
**Fix:** Add boundary check before incrementing
```

#### 7. Memory Usage (REQUIRED if applicable)

```markdown
## Memory Usage

- **Variables:** {X bytes}
- **Code:** {Y bytes}
- **Screen:** {Z bytes}
- **Total:** {X+Y+Z bytes}
```

**Guidelines:**
- List all memory requirements
- Separate by category
- Include screen memory if used
- Total at end

**Skip this section if:**
- Pattern uses negligible memory (< 10 bytes)
- Pattern is purely conceptual (architecture patterns)

#### 8. Integration Example (REQUIRED)

```markdown
## Integration Example

{Complete working program showing pattern in realistic context}
```

**Guidelines:**
- 30-60 lines
- Complete, runnable program
- Shows pattern integrated with other game elements
- Realistic scenario (not contrived)
- Heavily commented
- British English

**Example:**
```markdown
## Integration Example

Complete space shooter with score display:

\`\`\`basic
10 REM SPACE SHOOTER WITH SCORE
20 SCORE=0 : LIVES=3
30 PRINT CHR$(147) : REM clear screen
40 PRINT "SCORE:";SCORE;" LIVES:";LIVES
...
{30-60 lines showing complete game loop}
\`\`\`
```

#### 9. See Also (REQUIRED)

```markdown
## See Also

- [Related Pattern 1](/path/to/pattern-1)
- [Related Pattern 2](/path/to/pattern-2)
- [Related Lesson](/platform/phase/tier/lesson)
```

**Guidelines:**
- Minimum 3 cross-references
- Link to related patterns
- Link to lessons using this pattern
- Link to prerequisite patterns
- Use proper slug format

**Common cross-references:**
- Prerequisite patterns (must learn first)
- Complementary patterns (commonly used together)
- Advanced variations (next steps)
- Lessons demonstrating pattern

#### 10. Quick Reference Card (REQUIRED)

```markdown
## Quick Reference Card

**Key Memory Locations:**
- `$XXXX` - {purpose}

**Key Formulas:**
- `{formula}` - {what it calculates}

**Syntax:**
\`\`\`basic
{quick syntax reference}
\`\`\`
```

**Guidelines:**
- One-page reference format
- Essential information only
- Memory addresses if applicable
- Key formulas if applicable
- Syntax template
- No explanations (just facts)

#### 11. Best Practices (REQUIRED)

```markdown
## Best Practices

- {Practice 1}
- {Practice 2}
- {Practice 3}
```

**Guidelines:**
- Bulleted list
- 3-7 items
- Actionable advice
- Performance tips
- Maintainability tips
- British English

**Example:**
```markdown
## Best Practices

- Update score only when changed (avoid redundant screen writes)
- Use fixed-position display area for flicker-free updates
- Validate score limits before operations (prevent overflow)
- Pre-calculate string conversions for speed-critical sections
```

#### 12. Metadata Footer (REQUIRED)

```markdown
---

**Status:** {Draft|Complete|Updated}
**Last Updated:** {YYYY-MM-DD}
**Source Lesson:** [Lesson {N}](/platform/phase/tier/lesson-{N})
```

**Guidelines:**
- Horizontal rule separator
- Status: Draft (incomplete), Complete (all sections), Updated (recently revised)
- ISO date format (YYYY-MM-DD)
- Link to originating lesson if extracted
- British English

## Frontmatter Validation

### Check Required Fields

```bash
grep "^layout:\|^title:\|^category:\|^difficulty:\|^lessonsAppearIn:\|^system:" pattern.mdx
```

**Must all be present:**
- ✅ `layout: ../../../../../layouts/PatternLayout.astro`
- ✅ `title: "Pattern Name"`
- ✅ `category: "Category"`
- ✅ `difficulty: "Easy|Medium|Hard|Expert"`
- ✅ `lessonsAppearIn: N, N, N`
- ✅ `system: "Platform"`

### Check Category Value

**Valid categories:**
- Game Mechanics
- Graphics
- Sound
- Input
- Memory Management
- Performance
- Architecture

**Invalid:**
- ❌ "Gameplay" (use "Game Mechanics")
- ❌ "Visuals" (use "Graphics")
- ❌ "Audio" (use "Sound")

### Check Difficulty Value

**Must be exactly one of:**
- Easy
- Medium
- Hard
- Expert

**Invalid:**
- ❌ "Beginner" (use "Easy")
- ❌ "Advanced" (use "Hard")
- ❌ "Intermediate" (use "Medium")

## Section Validation

### Required Sections Checklist

- [ ] `## Overview` section present (2-4 sentences)
- [ ] `## The Pattern` section present (canonical code)
- [ ] `## Parameters` section present (if applicable)
- [ ] `## How It Works` section present (step-by-step)
- [ ] `## Variations` section present (minimum 3 subsections)
- [ ] `## Common Mistakes` section present (3-5 items with Symptom/Cause/Fix)
- [ ] `## Memory Usage` section present (if applicable)
- [ ] `## Integration Example` section present (30-60 line complete program)
- [ ] `## See Also` section present (minimum 3 links)
- [ ] `## Quick Reference Card` section present
- [ ] `## Best Practices` section present (3-7 bulleted items)
- [ ] Metadata footer present (status, date, source)

### Check Section Order

Sections must appear in this order:
1. Overview
2. The Pattern
3. Parameters (if applicable)
4. How It Works
5. Variations
6. Common Mistakes
7. Memory Usage (if applicable)
8. Integration Example
9. See Also
10. Quick Reference Card
11. Best Practices
12. Metadata footer

### Count Variations

```bash
grep "^### " pattern.mdx | grep -A 1 "^## Variations"
```

**Minimum 3 variations required.**

**For complex patterns (Hard/Expert difficulty), expect 6+ variations.**

### Verify Integration Example Length

```bash
# Count lines in Integration Example section
awk '/^## Integration Example/,/^## See Also/' pattern.mdx | wc -l
```

**Should be 30-60 lines minimum** (including code and explanation).

**Red flag if < 20 lines** - too shallow.

## British English Check

Use **british-english-check** skill for comprehensive checking.

**Pattern-specific terms:**
- optimise (not optimize)
- initialise (not initialize)
- programme (for TV/radio, but "program" for computer software)

## Common Mistakes

**Mistake 1:** Shallow variations
- **Fix:** Each variation must be substantially different (not just variable name changes)

**Mistake 2:** Missing integration example
- **Fix:** Always provide complete, runnable program showing realistic usage

**Mistake 3:** No "Common Mistakes" section
- **Fix:** Document 3-5 actual mistakes with Symptom/Cause/Fix format

**Mistake 4:** Vague "How It Works"
- **Fix:** Number steps, explain WHY, reference specific line numbers

**Mistake 5:** Missing cross-references
- **Fix:** Minimum 3 "See also" links to related patterns/lessons

**Mistake 6:** No Quick Reference Card
- **Fix:** Extract key facts (addresses, formulas, syntax) into scannable format

**Mistake 7:** Stub entry passed off as complete
- **Fix:** Pattern entries are 300-400+ lines minimum for proper depth

## Content Depth Guidelines

**By difficulty level:**

**Easy Patterns:**
- 250-350 lines total
- 3-4 variations
- Simple integration example (30-40 lines)
- Basic memory usage

**Medium Patterns:**
- 350-450 lines total
- 4-5 variations
- Realistic integration example (40-50 lines)
- Detailed memory breakdown

**Hard Patterns:**
- 450-600 lines total
- 5-6 variations
- Complex integration example (50-60 lines)
- Performance analysis

**Expert Patterns:**
- 600+ lines total
- 6+ variations
- Production-grade integration example (60+ lines)
- Comprehensive optimization discussion

**Red flag:** Pattern < 200 lines is almost certainly incomplete.

## Validation Report Format

```
PATTERN ENTRY VALIDATION: {title}

=== FRONTMATTER ===
layout: [CORRECT / WRONG]
title: [PRESENT / MISSING]
category: [VALID / INVALID / MISSING]
difficulty: [VALID / INVALID / MISSING]
lessonsAppearIn: [PRESENT / MISSING]
system: [VALID / MISSING]

=== REQUIRED SECTIONS ===
Overview: [PRESENT / MISSING] ({N} sentences)
The Pattern: [PRESENT / MISSING] ({N} lines)
Parameters: [PRESENT / MISSING / N/A]
How It Works: [PRESENT / MISSING] ({N} steps)
Variations: [PRESENT / MISSING] ({N} variations - min 3 required)
Common Mistakes: [PRESENT / MISSING] ({N} mistakes with Symptom/Cause/Fix)
Memory Usage: [PRESENT / MISSING / N/A]
Integration Example: [PRESENT / MISSING] ({N} lines - 30-60 required)
See Also: [PRESENT / MISSING] ({N} links - min 3 required)
Quick Reference Card: [PRESENT / MISSING]
Best Practices: [PRESENT / MISSING] ({N} items)
Metadata Footer: [PRESENT / MISSING]

=== SECTION ORDER ===
Order correct: [YES / NO]

=== CONTENT DEPTH ===
Total lines: {N} (expect 250-600+ depending on difficulty)
Depth assessment: [EXCELLENT / ADEQUATE / SHALLOW / STUB]

=== BRITISH ENGLISH ===
[Use british-english-check skill]

=== VERDICT ===
Entry status: [COMPLETE / NEEDS EXPANSION / STUB]
Recommendation: {specific fixes needed}
```

## Quick Reference

```bash
# Validate frontmatter fields
grep "^layout:\|^title:\|^category:\|^difficulty:\|^lessonsAppearIn:\|^system:" pattern.mdx

# Check required sections
grep "^## " pattern.mdx

# Count variations (minimum 3)
grep "^### " pattern.mdx | grep -c -A 1 "^## Variations"

# Check integration example length (30-60 lines minimum)
awk '/^## Integration Example/,/^## See Also/' pattern.mdx | wc -l

# Count cross-references (minimum 3)
grep -c "^- \[" pattern.mdx

# British English check
# Use british-english-check skill

# Total line count (250-600+ expected)
wc -l pattern.mdx
```

## Template (Copy This)

```markdown
---
layout: ../../../../../layouts/PatternLayout.astro
title: "{Pattern Name}"
category: "{Category}"
difficulty: "{Easy|Medium|Hard|Expert}"
lessonsAppearIn: {N, N, N}
system: "{Platform}"
---

## Overview
{2-4 sentences: what problem, when to use, key benefit}

## The Pattern

\`\`\`{language}
{10-20 lines canonical example}
\`\`\`

## Parameters

| Parameter | Type | Range | Purpose |
|-----------|------|-------|---------|
| {name} | {type} | {range} | {purpose} |

## How It Works

1. **{Step 1}** - {explanation}
2. **{Step 2}** - {explanation}
3. **{Step 3}** - {explanation}

## Variations

### {Variation 1}
{Description and code}

### {Variation 2}
{Description and code}

### {Variation 3}
{Description and code}

## Common Mistakes

### {Mistake 1}
**Symptom:** {what you see}
**Cause:** {why it happens}
**Fix:** {how to correct it}

### {Mistake 2}
**Symptom:** {what you see}
**Cause:** {why it happens}
**Fix:** {how to correct it}

### {Mistake 3}
**Symptom:** {what you see}
**Cause:** {why it happens}
**Fix:** {how to correct it}

## Memory Usage

- **Variables:** {X bytes}
- **Code:** {Y bytes}
- **Total:** {X+Y bytes}

## Integration Example

{Complete 30-60 line program showing realistic usage}

\`\`\`{language}
{complete working code}
\`\`\`

## See Also

- [Related Pattern 1](/path)
- [Related Pattern 2](/path)
- [Related Lesson](/path)

## Quick Reference Card

**Key Memory Locations:**
- `$XXXX` - {purpose}

**Key Formulas:**
- `{formula}` - {what it calculates}

**Syntax:**
\`\`\`{language}
{syntax template}
\`\`\`

## Best Practices

- {Practice 1}
- {Practice 2}
- {Practice 3}

---

**Status:** {Draft|Complete|Updated}
**Last Updated:** {YYYY-MM-DD}
**Source Lesson:** [Lesson {N}](/path)
```

## The Bottom Line

**Every pattern entry needs:**
1. Complete frontmatter (all 6 required fields)
2. 12 sections (Overview through Metadata) in correct order
3. Minimum 3 variations (6+ for Hard/Expert)
4. Complete integration example (30-60+ lines)
5. Common Mistakes with Symptom/Cause/Fix
6. Minimum 3 cross-references
7. Quick Reference Card
8. British English throughout
9. 250-600+ lines total (depending on difficulty)

**Zero tolerance for:**
- Stub entries (< 200 lines)
- Missing integration example
- Fewer than 3 variations
- Missing "Common Mistakes" section
- No cross-references
- Vague "How It Works" without specifics

**Patterns are comprehensive references, not quick tips. Treat them as authoritative documentation that saves developers hours of experimentation.**
