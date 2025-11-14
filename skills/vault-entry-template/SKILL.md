---
name: vault-entry-template
description: Use when creating Vault entries for people, companies, games, events, or techniques - provides mandatory structure, frontmatter fields, section requirements, and cross-reference guidelines
---

# Vault Entry Template

## Overview

Vault entries are encyclopedic references about retro computing history: people, companies, games, events, and techniques. Each entry follows a consistent structure with required sections and proper cross-references.

## When to Use

Use when:
- Creating new Vault entry
- Reviewing existing Vault entry for completeness
- Expanding stub entries
- Ensuring cross-references exist

**Do NOT:**
- Create marketing-style biographies
- Skip required sections
- Forget cross-references
- Use American English spellings

## Entry Structure

### Required Frontmatter

```yaml
---
layout: ../../layouts/VaultLayout.astro
title: "{Name or Title}"
subtitle: "{One-line descriptor}"
summary: "{50-150 char summary of significance}"
system_tags: ["{Platform1}", "{Platform2}"]
people_tags: ["{Category1}", "{Category2}"]
years: [start_year, end_year]
---
```

**Field Requirements:**

**`layout`:** Always `../../layouts/VaultLayout.astro`

**`title`:** (REQUIRED)
- Person name, company name, game title, event name, or technique
- Proper capitalization
- No quotes unless part of official name

**`subtitle`:** (REQUIRED)
- One-line descriptor (10-60 chars)
- Examples: "Co-founder of Activision", "The llama-loving wizard of Llamasoft", "Pioneering bedroom coder"
- No period at end

**`summary`:** (REQUIRED)
- 50-150 characters
- Single sentence capturing significance/impact
- Must end with period
- British English

**`system_tags`:** (REQUIRED if applicable)
- Array format: `["Platform Name", "Another Platform"]`
- Use official platform names: "C64" not "Commodore 64", "ZX Spectrum" not "Spectrum"
- Only systems directly relevant (don't list every platform if multi-platform developer)

**`people_tags`:** (REQUIRED if person/company entry)
- Array format: `["Category", "Another Category"]`
- Proper capitalization: "Game designers" not "game designers"
- Common categories: "Bedroom coders", "Game designers", "Indie pioneers", "Hardware engineers"

**`years`:** (REQUIRED)
- Array format: `[start, end]`
- For people: Birth year, death year (or current year if living)
- For companies: Founded year, closed year (or current year if active)
- For games: Release year (single value: `[1983, 1983]` or just `[1983]`)
- For events: Event year

### Required Sections

All vault entries must have these sections (in order):

#### 1. Overview (REQUIRED)

```markdown
## Overview
{2-4 sentences providing context, background, and significance}
```

**Guidelines:**
- Opens with context-setting statement
- Explains who/what and why significant
- Engaging tone (not dry factual listing)
- British English

**Example (Good):**
```markdown
## Overview
Jeff Minter founded Llamasoft in 1982 and promptly filled British shelves with neon shooters starring ungulates and particle storms. His work combined tight arcade mechanics with humour that felt unmistakably personal.
```

**Example (Bad):**
```markdown
## Overview
Jeff Minter was born in 1962. He started Llamasoft. He made games.
```

#### 2. Fast facts (REQUIRED)

```markdown
## Fast facts
- **Debut:** {first significant work with year}
- **Trademark:** {distinctive characteristics or techniques}
- **Notable:** {key achievements, innovations, or works}
- **Longevity:** {continued relevance, later career} (if applicable)
```

**Guidelines:**
- Bulleted list with bold labels
- 3-5 items
- Specific details (games, years, innovations)
- British English

#### 3. Influence (REQUIRED)

```markdown
## Influence
{1-3 paragraphs explaining impact, legacy, techniques pioneered, or cultural significance}
```

**Guidelines:**
- Explains lasting impact
- Connects to broader trends/movements
- Specific examples of influence
- Not just "was very successful" - explain HOW and WHY influential

#### 4. See also (REQUIRED)

```markdown
## See also
- [Related Entry 1](/vault/entry-1-slug)
- [Related Entry 2](/vault/entry-2-slug)
- [Related Entry 3](/vault/entry-3-slug)
```

**Guidelines:**
- Minimum 3 cross-references
- Link to related people, companies, games, platforms
- Use proper slug format: `/vault/slug-name` (lowercase, hyphenated)
- Entries should exist or be created (bidirectional linking)

**Common cross-references:**
- Person → Company they founded/worked for
- Person → Games they created
- Company → Key people
- Game → Creator/company
- Technique → People who pioneered it

## Frontmatter Validation

### Check Tag Format

```bash
grep "system_tags:" entry.mdx
grep "people_tags:" entry.mdx
```

**Must be arrays:**
- ✅ `system_tags: ["C64", "ZX Spectrum"]`
- ✅ `system_tags: []` (empty if not applicable)
- ❌ `system_tags: C64, ZX Spectrum` (not an array)
- ❌ `system_tags: "C64"` (string, not array)

### Check Years Field

```bash
grep "years:" entry.mdx
```

**Must be present:**
- ✅ `years: [1962, 2024]`
- ✅ `years: [1979]` (single year for games/events)
- ❌ Missing entirely

### Check Summary Length

**Count characters:**
- Should be 50-150 characters
- Single sentence
- Ends with period

## Section Validation

### Required Sections Checklist

- [ ] `## Overview` section present
- [ ] `## Fast facts` section present (with bulleted items)
- [ ] `## Influence` section present
- [ ] `## See also` section present (minimum 3 links)

### Check Section Order

Sections must appear in this order:
1. Overview
2. Fast facts
3. Influence
4. See also

## Cross-Reference Validation

For each link in "See also":
1. Extract slug from link (e.g., `/vault/llamasoft` → `llamasoft`)
2. Check if file exists: `/website/src/pages/vault/{slug}.mdx`
3. If missing, note for creation (or remove link)

**Bidirectional linking:**
- If entry A links to entry B
- Then entry B should link back to entry A
- (Not automatic - requires manual updating)

## British English Check

Use **british-english-check** skill for spellings.

**Common vault-specific words:**
- organisation (not organization)
- programme (for TV/radio, but "program" for computer software)
- whilst (not while)
- recognised (not recognized)

## Common Mistakes

**Mistake 1:** String tags instead of arrays
- **Fix:** `system_tags: ["C64"]` not `system_tags: C64`

**Mistake 2:** Missing years field
- **Fix:** Always include years, even if approximate

**Mistake 3:** Dry overview
- **Fix:** Lead with engaging context, not birth year

**Mistake 4:** Generic "Fast facts"
- **Fix:** Specific games, years, innovations - not vague achievements

**Mistake 5:** Missing cross-references
- **Fix:** Minimum 3 "See also" links, more for significant entries

**Mistake 6:** No "Influence" section
- **Fix:** Explain lasting impact, don't skip this section

## Entry Types

### Person Entry

**Focus:**
- Career arc (where they worked, what they created)
- Signature style or techniques
- Notable games/achievements
- Influence on industry

**Required tags:**
- `people_tags`: ["Category1", "Category2"]
- `system_tags`: Platforms they worked on
- `years`: [birth, death/current]

### Company Entry

**Focus:**
- Founding story
- Key releases
- Business model/innovation
- Closure or continued operation

**Required tags:**
- `people_tags`: ["Companies", "Publishers"] or similar
- `system_tags`: Primary platforms
- `years`: [founded, closed/current]

### Game Entry

**Focus:**
- Release context
- Gameplay innovation
- Technical achievements
- Cultural impact

**Required tags:**
- `system_tags`: Platform(s) released on
- `people_tags`: Genre or significance category
- `years`: [release_year]

### Technique Entry

**Focus:**
- What problem it solves
- Who pioneered it
- How it works (brief)
- Where it appears

**Required tags:**
- `system_tags`: Platform(s) using technique
- `people_tags`: Relevance category
- `years`: [first_use, last_significant_use]

## Validation Report Format

```
VAULT ENTRY VALIDATION: {title}

=== FRONTMATTER ===
Title: [PRESENT / MISSING]
Subtitle: [PRESENT / MISSING]
Summary: [50-150 chars / TOO SHORT / TOO LONG]
system_tags: [ARRAY FORMAT / WRONG FORMAT]
people_tags: [ARRAY FORMAT / WRONG FORMAT]
years: [PRESENT / MISSING]

=== REQUIRED SECTIONS ===
Overview: [PRESENT / MISSING]
Fast facts: [PRESENT / MISSING]
Influence: [PRESENT / MISSING]
See also: [PRESENT / MISSING] ({count} links)

=== SECTION ORDER ===
Order correct: [YES / NO]

=== CROSS-REFERENCES ===
Links found: {count}
Missing entries: [list any broken links]

=== BRITISH ENGLISH ===
[Use british-english-check skill]

=== VERDICT ===
Entry status: [COMPLETE / NEEDS FIXES / STUB]
Recommendation: {specific fixes needed}
```

## Quick Reference

```bash
# Validate frontmatter arrays
grep "system_tags:\|people_tags:" entry.mdx

# Check required sections
grep "^## " entry.mdx

# Count cross-references
grep -c "^\- \[" entry.mdx

# British English
# Use british-english-check skill

# Verify entry exists
ls /website/src/pages/vault/slug-name.mdx
```

## Template (Copy This)

```markdown
---
layout: ../../layouts/VaultLayout.astro
title: "{Name/Title}"
subtitle: "{One-line descriptor}"
summary: "{50-150 char summary ending with period.}"
system_tags: ["{Platform1}", "{Platform2}"]
people_tags: ["{Category1}", "{Category2}"]
years: [start, end]
---

## Overview
{2-4 sentences providing engaging context and significance}

## Fast facts
- **Debut:** {first work with year}
- **Trademark:** {distinctive characteristics}
- **Notable:** {key achievements}

## Influence
{1-3 paragraphs explaining lasting impact and cultural significance}

## See also
- [Related Entry 1](/vault/entry-1)
- [Related Entry 2](/vault/entry-2)
- [Related Entry 3](/vault/entry-3)
```

## The Bottom Line

**Every vault entry needs:**
1. Complete frontmatter (all required fields, proper array format)
2. Four sections (Overview, Fast facts, Influence, See also) in order
3. Minimum 3 cross-references
4. British English throughout
5. Engaging tone (not dry facts)

**Zero tolerance for:**
- Missing required sections
- String tags (must be arrays)
- No cross-references
- Stub entries without expansion plan
