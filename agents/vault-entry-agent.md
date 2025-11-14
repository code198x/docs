# Vault Entry Agent (RECURSIVE)

**Version:** 1.0
**Status:** Specification complete, not yet tested
**Priority:** P2 (Medium - Content Expansion)

---

## Purpose

Creates complete Vault entries with recursive cross-reference management. The agent not only creates the requested entry but automatically:
- Creates stub entries for any missing cross-references
- Updates existing entries to link back (bidirectional linking)
- Prevents infinite recursion with depth limits

**Think:** "Create Jeff Minter entry" → Agent creates Minter, notices missing Llamasoft entry, creates Llamasoft stub, links both entries bidirectionally.

---

## When to Use

Use this agent when:
- Creating new Vault entry (person/company/game/event/technique)
- Entry requires cross-references that may not exist yet
- Want automatic bidirectional linking
- Expanding Vault systematically

**Do NOT use when:**
- Just updating existing entry (use Edit tool directly)
- Creating simple entry with all cross-references already existing (Edit tool faster)
- Cross-references are uncertain (manual creation better)

---

## Inputs Required

### Minimum Required

**Entry specification:**
```
ENTRY TYPE: {Person|Company|Game|Event|Technique}
TITLE: {Name or title}
SUBTITLE: {One-line descriptor}
SUMMARY: {50-150 char summary}
SYSTEM_TAGS: [{Platform1}, {Platform2}]
PEOPLE_TAGS: [{Category1}, {Category2}]
YEARS: [start, end]
```

**Content specification:**
```
OVERVIEW: {2-4 sentences of context and significance}

FAST FACTS:
- Debut: {first work}
- Trademark: {distinctive characteristics}
- Notable: {key achievements}

INFLUENCE: {1-3 paragraphs on impact and legacy}

SEE ALSO: {3+ related entries}
```

### Optional

- **Recursion depth:** Max levels to recurse (default: 2, max: 3)
- **Stub detail:** How much content for stub entries (minimal/basic/detailed)
- **Dry run:** Preview entry graph without creating files

---

## Workflow Steps

### Phase 1: Entry Creation

**Step 1:** Read vault-entry-template skill
- Location: `/docs/skills/vault-entry-template/SKILL.md`
- Purpose: Understand structure requirements

**Step 2:** Validate input specification
- All required frontmatter fields present?
- Summary 50-150 chars?
- system_tags and people_tags are arrays?
- years field present?
- Minimum 3 "See also" entries?

**Step 3:** Create main entry file
- Path: `/website/src/pages/vault/{slug}.mdx`
- Slug: Lowercase, hyphenated (e.g., "jeff-minter")
- Content: Full entry with all sections

**Step 4:** Run vault-entry-template validation
- Use Skill tool to validate entry
- Fix any issues before proceeding

**STOP if validation fails** - report errors, do not proceed to recursion.

### Phase 2: Recursive Cross-Reference Management

**Step 5:** Extract "See also" references
- Parse ## See also section
- Extract all linked entries
- Example: `[Llamasoft](/vault/llamasoft)` → slug: "llamasoft"

**Step 6:** Check which references exist
```bash
for slug in {extracted_slugs}; do
  if [ -f "/website/src/pages/vault/${slug}.mdx" ]; then
    echo "EXISTS: $slug"
  else
    echo "MISSING: $slug"
  fi
done
```

**Step 7:** FOR EACH MISSING REFERENCE (Recursive Step)

**Recursion depth check:**
- If current depth >= max depth (default 2):
  - Log: "Max recursion depth reached, skipping {slug}"
  - Continue to next reference
- Else:
  - Proceed with stub creation

**Create stub entry:**
- Path: `/website/src/pages/vault/{slug}.mdx`
- Content: Minimal stub (see Stub Entry Template below)
- Frontmatter: Best-guess based on context
- Overview: Placeholder noting this is stub
- See also: Link back to parent entry

**Recursive call:**
- If stub has "See also" links:
  - Repeat Steps 5-7 with depth + 1
  - Prevent circular references (track visited slugs)

**Step 8:** Update existing entries for bidirectional linking

For each EXISTING reference:
- Read `/website/src/pages/vault/{slug}.mdx`
- Check if ## See also section exists
- Check if current entry already linked
- If not linked: Add link to current entry
- Preserve alphabetical order in See also section

**Step 9:** Generate entry graph report

```
VAULT ENTRY GRAPH: {main-entry}

CREATED:
✓ {main-entry-slug} (full entry)
✓ {stub-entry-1-slug} (stub - depth 1)
✓ {stub-entry-2-slug} (stub - depth 2)

UPDATED (bidirectional links):
↔ {existing-entry-1-slug} (added link to {main-entry})
↔ {existing-entry-2-slug} (added link to {main-entry})

SKIPPED (max depth):
⊗ {deep-entry-slug} (would be depth 3)

TOTAL FILES CREATED: {N}
TOTAL FILES UPDATED: {N}
```

---

## Stub Entry Template

Stubs created by recursive process use minimal content:

```markdown
---
layout: ../../layouts/VaultLayout.astro
title: "{Inferred Name}"
subtitle: "{Inferred descriptor}"
summary: "{Minimal summary based on context.}"
system_tags: [{inferred}]
people_tags: [{inferred}]
years: [unknown, unknown]
---

## Overview

{Inferred name} is referenced in multiple Vault entries but does not yet have complete documentation. This stub entry serves as a placeholder pending expansion.

## Fast facts

- **Referenced by:** [{Parent Entry}](/vault/{parent-slug})
- **Context:** {Brief context from parent entry}
- **Status:** Stub entry pending research

## Influence

(Pending research and documentation)

## See also

- [{Parent Entry}](/vault/{parent-slug})

---

**Status:** Stub (requires expansion)
**Created:** {YYYY-MM-DD}
**Source:** Automatically generated by vault-entry-agent
```

**Stub inference rules:**
- Person name → Infer birth/death years as `unknown`
- Company name → Infer `people_tags: ["Companies"]`
- Game title → Infer `people_tags: ["Games"]`
- Event → Infer `people_tags: ["Events"]`

---

## Recursion Control

### Maximum Depth

**Default:** 2 levels (main entry → stub → stub's stub)

**Rationale:** Prevents runaway creation while handling most real scenarios.

**Example depth 2 chain:**
1. Create "Jeff Minter" entry (depth 0)
2. Minter references "Gridrunner" → Create Gridrunner stub (depth 1)
3. Gridrunner references "Vic-20" → Create Vic-20 stub (depth 2)
4. Vic-20 references "Commodore" → STOP (would be depth 3)

### Circular Reference Prevention

**Track visited slugs:**
```
visited = {main-entry-slug}

For each missing reference:
  if reference-slug in visited:
    log "Circular reference detected: {reference-slug}"
    skip creation
  else:
    visited.add(reference-slug)
    create stub
```

**Example circular scenario:**
- Creating "Llamasoft" entry
- Llamasoft references "Jeff Minter"
- Jeff Minter references "Llamasoft"
- Agent detects circular reference, skips second creation

### Recursion Limit Override

User can specify higher limit (max 3):
```
RECURSION_DEPTH: 3
```

**Warning if depth > 2:** "Recursion depth {N} may create many stub entries. Recommend reviewing entry graph in dry run mode first."

---

## Skills Used

### vault-entry-template (Primary validation)
- Location: `/docs/skills/vault-entry-template/SKILL.md`
- When: After creating each entry (main and stubs)
- Purpose: Ensure structure compliance

### british-english-check (Language validation)
- Location: `/docs/skills/british-english-check/SKILL.md`
- When: After creating main entry
- Purpose: Verify British English spellings

**Note:** Stubs skip british-english-check (minimal content).

---

## Error Handling

### Error Scenarios

**Error 1: Invalid input specification**
```
AGENT FAILED at Step 2 (input validation)

FAILED:
✗ Missing required field: {field-name}
✗ Summary length: {N} chars (50-150 required)
✗ system_tags not array format

SUGGESTED FIX:
- Provide complete entry specification
- See vault-entry-template skill for required fields
```

**Error 2: Main entry validation fails**
```
AGENT FAILED at Step 4 (main entry validation)

COMPLETED:
✓ Created entry file: /website/src/pages/vault/{slug}.mdx

FAILED:
✗ Validation errors: {specific issues from vault-entry-template skill}

SUGGESTED FIX:
- Fix validation errors in main entry
- Re-run agent from Step 4 (validation)
- OR manually fix file and continue with recursion separately
```

**Error 3: File already exists**
```
AGENT FAILED at Step 3 (file creation)

FAILED:
✗ File already exists: /website/src/pages/vault/{slug}.mdx

SUGGESTED FIX:
- Choose different slug (title variation)
- OR delete existing file if replacing
- OR use Edit tool to update existing entry
```

**Error 4: Recursion creates too many stubs**
```
AGENT WARNING at Step 7 (recursive stub creation)

WARNING:
⚠ Created {N} stub entries (depth {N})
⚠ May indicate overly broad cross-references

COMPLETED:
✓ Main entry created
✓ {N} stubs created

RECOMMENDATION:
- Review entry graph
- Consider reducing cross-references in main entry
- Some stubs may warrant full entries (not stubs)
```

### Partial Completion Recovery

If agent fails during recursion:
- Main entry IS created (step 3)
- Some stubs MAY be created (step 7)
- Bidirectional links MAY be incomplete (step 8)

**Recovery:**
1. Check entry graph report (shows completed files)
2. Manually complete missing stubs OR
3. Remove incomplete stubs and rerun agent with lower recursion depth

---

## Invocation Pattern

### Basic Invocation

```javascript
{
  subagent_type: "general-purpose",
  description: "Create Vault entry with recursion",
  prompt: `VAULT ENTRY SPECIFICATION:

ENTRY TYPE: Person
TITLE: Jeff Minter
SUBTITLE: The llama-loving wizard of Llamasoft
SUMMARY: Founder of Llamasoft, creator of psychedelic shooters filled with neon particles and ungulates.
SYSTEM_TAGS: ["C64", "Atari ST", "Jaguar"]
PEOPLE_TAGS: ["Bedroom coders", "Indie pioneers"]
YEARS: [1962, 2024]

OVERVIEW:
Jeff Minter founded Llamasoft in 1982 and promptly filled British shelves with neon shooters starring ungulates and particle storms. His work combined tight arcade mechanics with humour that felt unmistakably personal.

FAST FACTS:
- Debut: Gridrunner (1982) established his psychedelic shooter style
- Trademark: Llamatron, Tempest 2000, and other games featuring ungulates
- Notable: Tempest 2000 hailed as Jaguar's killer app
- Longevity: Still creating with Llamasoft in 2024

INFLUENCE:
Minter proved bedroom coders could build distinctive brands around personal obsessions. His audiovisual intensity influenced generations of indie developers to embrace weirdness as identity.

SEE ALSO:
- Llamasoft
- Gridrunner
- Tempest 2000
- Attack of the Mutant Camels
- Atari Jaguar

Use the vault-entry-agent to create this entry with recursive cross-reference management. Maximum recursion depth: 2.`
}
```

### Dry Run Invocation

```javascript
{
  subagent_type: "general-purpose",
  description: "Preview Vault entry graph",
  prompt: `{same specification as above}

DRY RUN MODE: Do not create any files. Instead:
1. Validate main entry specification
2. Identify missing cross-references
3. Project what stubs would be created (up to depth 2)
4. Generate entry graph report showing projected files
5. Report estimated file count

This allows reviewing the entry graph before committing to creation.`
}
```

### High Recursion Depth

```javascript
{
  subagent_type: "general-purpose",
  description: "Create Vault entry depth 3",
  prompt: `{entry specification}

RECURSION_DEPTH: 3

WARNING ACKNOWLEDGED: This may create many stub entries. Review entry graph carefully.`
}
```

---

## Example Scenarios

### Scenario 1: Simple Entry (No Recursion Needed)

**Input:** Create "Elite" entry
**References:** David Braben, Ian Bell, Acornsoft (all exist)
**Agent behavior:**
1. Creates `/website/src/pages/vault/elite.mdx`
2. Checks references: all exist
3. Updates David Braben entry: adds Elite link
4. Updates Ian Bell entry: adds Elite link
5. Updates Acornsoft entry: adds Elite link
6. No stubs created

**Output:**
```
VAULT ENTRY GRAPH: elite

CREATED:
✓ elite (full entry)

UPDATED (bidirectional links):
↔ david-braben (added link to elite)
↔ ian-bell (added link to elite)
↔ acornsoft (added link to elite)

TOTAL FILES CREATED: 1
TOTAL FILES UPDATED: 3
```

### Scenario 2: Recursive Creation (Depth 1)

**Input:** Create "Firebird Software" entry
**References:** Elite (exists), The Sentinel (missing), Paradroid (exists)
**Agent behavior:**
1. Creates `/website/src/pages/vault/firebird-software.mdx`
2. Checks references:
   - Elite: exists
   - The Sentinel: missing → create stub
   - Paradroid: exists
3. Creates `/website/src/pages/vault/the-sentinel.mdx` (stub, depth 1)
4. The Sentinel stub references "Firebird Software" (no further recursion)
5. Updates Elite and Paradroid with bidirectional links

**Output:**
```
VAULT ENTRY GRAPH: firebird-software

CREATED:
✓ firebird-software (full entry)
✓ the-sentinel (stub - depth 1)

UPDATED (bidirectional links):
↔ elite (added link to firebird-software)
↔ paradroid (added link to firebird-software)

TOTAL FILES CREATED: 2
TOTAL FILES UPDATED: 2
```

### Scenario 3: Deep Recursion (Depth 2 Limit)

**Input:** Create "Gridrunner" entry
**References:** Jeff Minter (missing), Vic-20 (missing), Llamasoft (missing)
**Agent behavior:**
1. Creates `/website/src/pages/vault/gridrunner.mdx`
2. Jeff Minter missing → Create stub (depth 1)
   - Jeff Minter stub references Llamasoft (missing)
   - Create Llamasoft stub (depth 2)
   - Llamasoft stub references Commodore (missing)
   - Depth limit reached, skip Commodore
3. Vic-20 missing → Create stub (depth 1)
   - Vic-20 stub references Commodore (missing)
   - Create Commodore stub (depth 2)
4. Llamasoft missing → Already created in step 2

**Output:**
```
VAULT ENTRY GRAPH: gridrunner

CREATED:
✓ gridrunner (full entry)
✓ jeff-minter (stub - depth 1)
✓ llamasoft (stub - depth 2)
✓ vic-20 (stub - depth 1)
✓ commodore (stub - depth 2)

SKIPPED (max depth):
⊗ Additional references from depth 2 stubs

TOTAL FILES CREATED: 5
TOTAL FILES UPDATED: 0
```

### Scenario 4: Circular Reference Detected

**Input:** Create "Ultimate Play The Game" entry
**References:** Tim Stamper (missing), Chris Stamper (missing)
**Agent behavior:**
1. Creates `/website/src/pages/vault/ultimate-play-the-game.mdx`
2. Tim Stamper missing → Create stub (depth 1)
   - Tim Stamper stub references Ultimate Play The Game (circular!)
   - Circular reference detected, skip (already in visited set)
   - Tim Stamper stub also references Chris Stamper (missing)
   - Create Chris Stamper stub (depth 2)
   - Chris Stamper stub references Ultimate Play The Game (circular!)
   - Circular reference detected, skip
3. Chris Stamper missing → Already created in step 2

**Output:**
```
VAULT ENTRY GRAPH: ultimate-play-the-game

CREATED:
✓ ultimate-play-the-game (full entry)
✓ tim-stamper (stub - depth 1)
✓ chris-stamper (stub - depth 2)

CIRCULAR REFERENCES PREVENTED:
⊗ ultimate-play-the-game (already created)

TOTAL FILES CREATED: 3
TOTAL FILES UPDATED: 0
```

---

## Testing Checklist

Before production use, test with:

**Test 1: Simple entry (all references exist)**
- Input: Entry with 3-5 existing cross-references
- Expected: Main entry created, all references updated bidirectionally, 0 stubs

**Test 2: Single-level recursion**
- Input: Entry with 1-2 missing references
- Expected: Main entry + 1-2 stubs created, depth 1

**Test 3: Multi-level recursion**
- Input: Entry with missing references that have missing references
- Expected: Main entry + stubs at depth 1 and 2, depth 3 skipped

**Test 4: Circular reference**
- Input: Entry A references B (missing), B would reference A
- Expected: A and B created, circular reference detected and prevented

**Test 5: Duplicate slug**
- Input: Entry with slug matching existing file
- Expected: Error at step 3, no file overwritten

**Test 6: Invalid specification**
- Input: Missing required fields or malformed data
- Expected: Error at step 2, no files created

**Test 7: Dry run mode**
- Input: Any specification with DRY RUN MODE
- Expected: Entry graph report, 0 files created

---

## Agent Autonomy

**High autonomy - No user intervention during execution:**
- Creates all files automatically
- Infers stub content from context
- Makes slug naming decisions
- Determines which references need stubs
- Manages recursion depth

**User provides:**
- Complete entry specification
- Optionally: recursion depth override
- Optionally: dry run flag

**User reviews after completion:**
- Entry graph report
- Main entry quality
- Stub entries (for expansion priority)

---

## Production Notes

### When Stubs Are Created

**Stubs indicate missing Vault content.** After running vault-entry-agent:

1. Review entry graph report
2. Identify high-value stubs (referenced by multiple entries)
3. Expand stubs to full entries (manually or with agent)
4. Eventually all stubs become full entries

**Stub expansion priority:**
- Stubs referenced by 3+ entries: High priority
- Stubs for major people/companies: High priority
- Stubs for obscure topics: Low priority (may remain stubs)

### Bidirectional Linking Maintenance

Agent handles bidirectional linking automatically, but:
- If you manually create entry, manually add cross-references
- If you delete entry, manually remove cross-references
- Consider **curriculum-audit-agent** (P2) for link validation

---

## Integration with Other Agents

**vault-entry-agent** can be called by:

**pattern-extraction-agent:**
- Extracts pattern from lesson
- Discovers technique pioneer (person)
- Calls vault-entry-agent to create pioneer entry

**lesson-creation-agent:**
- Creates lesson about specific game
- Discovers game not in Vault
- Calls vault-entry-agent to create game entry

**curriculum-audit-agent:**
- Scans Vault for broken links
- Identifies missing entries
- Suggests vault-entry-agent invocations

---

## The Bottom Line

**vault-entry-agent automates Vault growth:**
- Creates requested entry
- Recursively creates stub entries for missing cross-references (up to depth 2)
- Updates existing entries for bidirectional linking
- Prevents circular references and runaway recursion

**Use when:**
- Creating entry with potentially missing cross-references
- Want automatic stub creation
- Expanding Vault systematically

**Produces:**
- Complete main entry
- Stub entries for missing references
- Bidirectional links in existing entries
- Entry graph report showing all changes

**Review stubs after creation and expand high-priority ones to full entries over time.**

---

**Status:** Specification complete, not yet tested in production
**Next steps:** Test with real Vault entry specs, refine recursion heuristics
