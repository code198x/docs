# Skills and Agents Roadmap

**Version:** 1.0
**Date:** 2025-11-04
**Status:** Planning phase

---

## Purpose

This document defines all skills (process guidance + light automation) and agents (autonomous execution) needed for efficient lesson creation and maintenance. It prioritizes development order and notes dependencies.

---

## Skills vs Agents Boundary

**SKILLS** = Process documentation + lightweight automation
- Step-by-step guidance
- Run simple checks/commands
- Report results to user
- User makes decisions
- Examples: checklists, validation runs, file searches

**AGENTS** = Autonomous multi-step execution
- Execute complete workflows without asking
- Make implementation decisions within constraints
- Create/modify multiple files
- Handle errors and adapt
- Examples: create entire lesson, build tier of content

**Analogy**: Skill = recipe book, Agent = chef

---

## Skills Inventory

### Validation Skills

**1. lesson-validation**
- **Priority**: P0 (Critical - use immediately)
- **Purpose**: Runs all mandatory validation checks on a lesson
- **What it does**:
  - Compiles code (platform-specific)
  - Runs semantic validator
  - Checks screenshot exists
  - Verifies British English
  - Checks all files in correct locations
- **Returns**: Pass/fail report with specific issues
- **User decides**: Whether to fix or accept issues
- **Dependencies**: None
- **Location**: `docs/skills/lesson-validation/SKILL.md`

**2. screenshot-verification**
- **Priority**: P0 (Critical)
- **Purpose**: Verifies screenshot matches lesson expectations
- **What it does**:
  - Uses READ tool to view screenshot
  - Checks for expected visual elements
  - Compares to lesson description
- **Returns**: Verification report (matches/discrepancies)
- **User decides**: Whether screenshot is acceptable
- **Dependencies**: None
- **Location**: `docs/skills/screenshot-verification/SKILL.md`

**3. british-english-check**
- **Priority**: P1 (High - needed for quality)
- **Purpose**: Scans content for American spellings
- **What it does**:
  - Grep for common American spellings
  - Suggests British alternatives
  - Exception: "program" (computer programs)
- **Returns**: List of American spellings found
- **User decides**: Which to fix
- **Dependencies**: British English dictionary/list
- **Location**: `docs/skills/british-english-check/SKILL.md`
- **Note**: Need to expand dictionary beyond color/colour basics

**4. curriculum-alignment-check**
- **Priority**: P1 (High)
- **Purpose**: Verifies lesson matches phase curriculum spec
- **What it does**:
  - Reads phase curriculum doc
  - Compares lesson content to spec
  - Reports mismatches
- **Returns**: Alignment report
- **User decides**: Whether to fix lesson or update spec
- **Dependencies**: Phase curriculum docs exist
- **Location**: `docs/skills/curriculum-alignment-check/SKILL.md`

### Creation Guidance Skills

**5. lesson-creation-workflow**
- **Priority**: P0 (Critical - use immediately)
- **Purpose**: Step-by-step walkthrough of production workflow
- **What it does**:
  - Guides through each workflow step
  - Reminds about file locations
  - Prompts for validation at each stage
  - Tracks progress with TodoWrite
- **Returns**: Guided process completion
- **User decides**: When to proceed to next step
- **Dependencies**: None (references MASTER-CURRICULUM-PLAN.md workflow)
- **Location**: `docs/skills/lesson-creation-workflow/SKILL.md`

**6. vault-entry-template**
- **Priority**: P2 (Medium)
- **Purpose**: Guides creation of properly structured Vault entry
- **What it does**:
  - Shows Vault entry format
  - Prompts for required fields
  - Suggests related entries to cross-link
- **Returns**: Template with guidance
- **User decides**: Content and cross-links
- **Dependencies**: None
- **Location**: `docs/skills/vault-entry-template/SKILL.md`

**7. pattern-library-template**
- **Priority**: P2 (Medium)
- **Purpose**: Guides creation of pattern documentation
- **What it does**:
  - Shows pattern format
  - Prompts for sections
  - Guides through variations and examples
- **Returns**: Template with guidance
- **User decides**: Pattern content
- **Dependencies**: None
- **Location**: `docs/skills/pattern-library-template/SKILL.md`

### Strategic Skills

**8. strategic-alignment-check**
- **Priority**: P1 (High)
- **Purpose**: Validates work against strategic documents
- **What it does**:
  - Checks against mission statement
  - Verifies no violations of non-goals
  - Confirms voice/tone guidelines
- **Returns**: Strategic alignment report
- **User decides**: Whether to adjust content
- **Dependencies**: Strategic document exists
- **Location**: `docs/skills/strategic-alignment-check/SKILL.md`

**9. voice-tone-check**
- **Priority**: P1 (High)
- **Purpose**: Scans lesson content for tone violations
- **What it does**:
  - Checks for marketing speak ("wow moments", "insight blocks")
  - Verifies British English
  - Checks for era-appropriate language
  - Confirms playful but rigorous tone
- **Returns**: Tone report
- **User decides**: Which adjustments to make
- **Dependencies**: Voice guidelines document
- **Location**: `docs/skills/voice-tone-check/SKILL.md`

---

## Agents Inventory

### Content Creation Agents

**1. lesson-creation-agent**
- **Priority**: P1 (High - major time saver)
- **Purpose**: Autonomously creates complete lesson with all files
- **What it does**:
  - Takes lesson spec as input
  - Creates code files in correct location
  - Compiles code
  - Captures screenshot (platform-specific method)
  - Creates lesson MDX
  - Runs validation
  - Updates tier/phase/platform navigation
  - Reports completion or errors
- **Decisions it makes**:
  - File naming conventions
  - Screenshot timing/frames
  - Navigation text formatting
- **User involvement**: Reviews final output
- **Dependencies**:
  - Compilation commands per platform
  - Screenshot scripts per platform
  - lesson-validation skill
- **Location**: Subagent, invoked via Task tool
- **Complexity**: High

**2. vault-entry-agent (RECURSIVE)**
- **Priority**: P2 (Medium)
- **Purpose**: Creates complete Vault entry with recursive cross-linking
- **What it does**:
  - Takes entry spec (person/company/game/event)
  - Creates properly formatted MDX
  - Identifies "See also" references
  - **RECURSIVE**: Checks if referenced entries exist
  - **RECURSIVE**: Creates stub entries for missing references
  - **RECURSIVE**: Updates related entries to cross-link back
  - Validates frontmatter
- **Decisions it makes**:
  - Which related entries to create
  - Stub entry content
  - Bidirectional linking
- **User involvement**: Reviews entry graph
- **Dependencies**: vault-entry-template skill
- **Location**: Subagent, invoked via Task tool
- **Complexity**: High (recursion, graph management)
- **Note**: Must prevent infinite recursion

**3. pattern-extraction-agent**
- **Priority**: P2 (Medium - improves Pattern Library)
- **Purpose**: Scans completed lessons, extracts reusable patterns
- **What it does**:
  - Analyzes lesson code for patterns
  - Identifies repeated techniques
  - Generates pattern documentation
  - Suggests where pattern appears (lessonsAppearIn)
- **Decisions it makes**:
  - What constitutes a pattern
  - Pattern categorization
  - Variation identification
- **User involvement**: Reviews and refines patterns
- **Dependencies**: pattern-library-template skill
- **Location**: Subagent, invoked via Task tool
- **Complexity**: High (code analysis)

### Planning Agents

**4. curriculum-planning-agent**
- **Priority**: P1 (High - needed for NES/Amiga expansion)
- **Purpose**: Expands phase curricula following established patterns
- **What it does**:
  - Takes platform and phase as input
  - Analyzes existing platform curricula (C64, ZX)
  - Identifies universal concepts
  - Adapts game selections for platform strengths
  - Generates phase curriculum document
- **Decisions it makes**:
  - Game selections per platform
  - Lesson count distribution
  - Concept introduction timing
- **User involvement**: Reviews and adjusts curriculum
- **Dependencies**: MASTER-CURRICULUM-PLAN.md, existing curricula
- **Location**: Subagent, invoked via Task tool
- **Complexity**: High (pattern recognition, adaptation)

**5. concept-mapping-agent**
- **Priority**: P2 (Medium - improves cross-platform navigation)
- **Purpose**: Builds CONCEPT-CROSS-REFERENCE.md automatically
- **What it does**:
  - Parses all platform curriculum docs
  - Extracts concepts mentioned
  - Maps concepts to specific lessons
  - Identifies platform-specific vs universal
  - Generates cross-reference document
- **Decisions it makes**:
  - Concept identification and naming
  - Concept categorization
  - Lesson associations
- **User involvement**: Reviews and refines mappings
- **Dependencies**: All platform curriculum docs
- **Location**: Subagent, invoked via Task tool
- **Complexity**: Medium (parsing, mapping)

### Maintenance Agents

**6. navigation-update-agent**
- **Priority**: P1 (High - needed frequently)
- **Purpose**: Updates all tier/phase/platform/home indexes
- **What it does**:
  - Takes new lesson as input
  - Updates tier index (adds to lessons array)
  - Updates phase index if needed (new tier)
  - Updates platform index if needed (new phase)
  - Updates homepage if needed (milestone)
  - Ensures consistent formatting
- **Decisions it makes**:
  - When to update each level
  - Lesson description text
  - Status badges
- **User involvement**: Reviews navigation changes
- **Dependencies**: Index file structures
- **Location**: Subagent, invoked via Task tool
- **Complexity**: Medium

**7. curriculum-audit-agent**
- **Priority**: P2 (Medium - periodic maintenance)
- **Purpose**: Scans entire curriculum for issues
- **What it does**:
  - Checks all lessons for missing files
  - Verifies all navigation links work
  - Checks curriculum alignment across all lessons
  - Reports gaps in coverage
  - Identifies orphaned files
- **Decisions it makes**:
  - Issue severity classification
  - Repair suggestions
- **User involvement**: Reviews report, decides fixes
- **Dependencies**: All curriculum docs and lessons
- **Location**: Subagent, invoked via Task tool
- **Complexity**: Medium (comprehensive scanning)

---

## Implementation Priority

### Phase 1: Immediate Use (P0) ✅ COMPLETE
Build these first - needed for current lesson creation:

1. ✅ **lesson-validation** skill - `/docs/skills/lesson-validation/SKILL.md`
2. ✅ **screenshot-verification** skill - `/docs/skills/screenshot-verification/SKILL.md`
3. ✅ **lesson-creation-workflow** skill - `/docs/skills/lesson-creation-workflow/SKILL.md`

**Status**: All complete. Created using RED-GREEN-REFACTOR TDD methodology with subagent testing.

**Rationale**: These support manual lesson creation right now.

### Phase 2: Quality & Efficiency (P1) ✅ SPECIFICATIONS COMPLETE
Build next - major quality and time improvements:

4. ✅ **british-english-check** skill - `/docs/skills/british-english-check/SKILL.md`
5. ✅ **curriculum-alignment-check** skill - `/docs/skills/curriculum-alignment-check/SKILL.md`
6. ✅ **strategic-alignment-check** skill - `/docs/skills/strategic-alignment-check/SKILL.md`
7. ✅ **voice-tone-check** skill - `/docs/skills/voice-tone-check/SKILL.md`
8. ✅ **lesson-creation-agent** 🤖 - `/docs/agents/lesson-creation-agent.md` (two-phase with manual screenshots)
9. ✅ **navigation-update-agent** 🤖 - `/docs/agents/navigation-update-agent.md`
10. ✅ **curriculum-planning-agent** 🤖 - `/docs/agents/curriculum-planning-agent.md`

**Status**: All specifications complete. Skills tested with subagents. Agents not yet tested in production.

**Next**: Test agents with real lesson/curriculum specs.

**Rationale**: Quality gates (skills) + major automation (agents) for lesson workflow and planning.

### Phase 3: Content Expansion (P2) ✅ COMPLETE
Build when Phase 2 is solid:

11. ✅ **vault-entry-template** skill - `/docs/skills/vault-entry-template/SKILL.md`
12. ✅ **pattern-library-template** skill - `/docs/skills/pattern-library-template/SKILL.md`
13. ✅ **vault-entry-agent (RECURSIVE)** 🤖 - `/docs/agents/vault-entry-agent.md`
14. ✅ **pattern-extraction-agent** 🤖 - `/docs/agents/pattern-extraction-agent.md`
15. ✅ **concept-mapping-agent** 🤖 - `/docs/agents/concept-mapping-agent.md`
16. ✅ **curriculum-audit-agent** 🤖 - `/docs/agents/curriculum-audit-agent.md`
17. ✅ **lesson-archiving** skill - `/docs/skills/lesson-archiving/SKILL.md`
18. ✅ **cross-reference-validator-agent** 🤖 - `/docs/agents/cross-reference-validator-agent.md`
19. ✅ **code-comment-check** skill - `/docs/skills/code-comment-check/SKILL.md`
20. ✅ **screenshot-setup-helper** skill - `/docs/skills/screenshot-setup-helper/SKILL.md`

**Status**: All specifications complete. Skills tested with subagents (vault-entry-template, pattern-library-template, lesson-archiving, code-comment-check, screenshot-setup-helper). Agents not yet tested in production (vault-entry-agent, pattern-extraction-agent, concept-mapping-agent, curriculum-audit-agent, cross-reference-validator-agent).

**Next**: Test agents with real specs (vault entries, pattern extraction, concept mapping, curriculum audit, cross-reference validation).

**Rationale**: Vault and Pattern Library growth, cross-platform infrastructure, systematic maintenance, curriculum alignment enforcement, quality standards.

### Phase 4: Platform-Specific Skills (P1) ✅ COMPLETE

Build platform-specific lesson creation skills extending lesson-creation-workflow:

17. ✅ **c64-lesson-creation** skill - `/docs/skills/c64-lesson-creation/SKILL.md`
18. ✅ **c64-6510-lesson-creation** skill - `/docs/skills/c64-6510-lesson-creation/SKILL.md`
19. ✅ **nes-lesson-creation** skill - `/docs/skills/nes-lesson-creation/SKILL.md`
20. ✅ **zx-lesson-creation** skill - `/docs/skills/zx-lesson-creation/SKILL.md` (uses `sinclair-zx-spectrum` paths)
21. ✅ **zx-z80-lesson-creation** skill - `/docs/skills/zx-z80-lesson-creation/SKILL.md` (uses `sinclair-zx-spectrum` paths)
22. ✅ **amiga-lesson-creation** skill - `/docs/skills/amiga-lesson-creation/SKILL.md` (uses `commodore-amiga` paths)
23. ✅ **amiga-68k-lesson-creation** skill - `/docs/skills/amiga-68k-lesson-creation/SKILL.md` (uses `commodore-amiga` paths)

**Status**: All 7 platform-specific skills complete. Ready for production use.

**Key features:**
- Platform-specific compilation commands (petcat, ca65/ld65, zmakebas, sjasmplus, vasm)
- Emulator-specific screenshot capture (VICE, FCEUX, FUSE, FS-UAE)
- Platform-specific validation (memory maps, hardware registers, anti-patterns)
- "Don't waste space" principle applied across all platforms

**Rationale**: lesson-creation-agent needs platform-specific compilation, validation, screenshot methods. All platforms now covered.

### Phase 5: Future Enhancements (P3) ✅ SPECIFICATIONS COMPLETE

Build when Phases 1-4 are production-tested:

24. ✅ **lesson-adaptation-agent** 🤖 - `/docs/agents/lesson-adaptation-agent.md`
25. ✅ **lesson-dependency-mapper-agent** 🤖 - `/docs/agents/lesson-dependency-mapper-agent.md`
26. ✅ **semantic-validator-generator-agent** 🤖 - `/docs/agents/semantic-validator-generator-agent.md`
27. ✅ **memory-map-check** skill - `/docs/skills/memory-map-check/SKILL.md`

**Status**: All specifications complete. Not yet tested in production.

**Key features:**
- **lesson-adaptation-agent**: Cross-platform lesson translation with hardware mapping
- **lesson-dependency-mapper-agent**: Visualizes curriculum structure with cycle detection
- **semantic-validator-generator-agent**: Generates platform-specific validators from specifications
- **memory-map-check**: Memory safety validation guidance for all platforms

**Rationale**: Advanced automation for curriculum expansion, maintenance, and quality assurance. Cross-platform lesson translation, dependency visualization, validator generation, and comprehensive memory safety checking.

---

## Dependencies Graph

```
lesson-validation skill
  ↓ (used by)
lesson-creation-agent
  ↓ (uses)
navigation-update-agent

british-english-check skill
  ↓ (used by)
voice-tone-check skill
  ↓ (used by)
strategic-alignment-check skill

curriculum-alignment-check skill
  ↓ (used by)
curriculum-audit-agent

vault-entry-template skill
  ↓ (used by)
vault-entry-agent

pattern-library-template skill
  ↓ (used by)
pattern-extraction-agent

All platform curricula
  ↓ (parsed by)
concept-mapping-agent
  ↓ (generates)
CONCEPT-CROSS-REFERENCE.md
```

---

## Supporting Infrastructure Needed

### British English Dictionary
- **Location**: `docs/BRITISH-ENGLISH-DICTIONARY.md`
- **Contents**:
  - Common American → British mappings
  - Exception list ("program" for computer programs)
  - Context-sensitive rules
- **Status**: Needs creation/expansion

### Compilation Commands Registry
- **Location**: `docs/COMPILATION-COMMANDS.md`
- **Contents**: Per-platform build commands
  - C64 BASIC: `petcat -w2 -o output.prg -- input.bas`
  - C64 ASM: `ca65 + ld65` commands
  - ZX BASIC: `zmakebas` commands
  - ZX ASM: `sjasmplus` commands
  - NES ASM: `ca65 + ld65` with NES config
  - Amiga ASM: `vasm` commands
- **Status**: Needs compilation from existing scripts

### Screenshot Methods Registry
- **Location**: `docs/SCREENSHOT-METHODS.md`
- **Contents**: Per-platform screenshot approaches
  - Automated (script-based)
  - Semi-automated (GUI tools)
  - Manual (emulator keypress + file move)
- **Status**: Needs documentation from existing scripts

---

## Vault Entry Agent - Recursive Behavior

**Example Scenario:**

Creating entry for "Jeff Minter":
1. Agent creates `/vault/jeff-minter.mdx`
2. Identifies "See also": Llamasoft, Attack of the Mutant Camels, Tempest 2000
3. **Checks**: Do these entries exist?
   - Llamasoft: ✅ Exists
   - Attack of the Mutant Camels: ✅ Exists
   - Tempest 2000: ✅ Exists
4. **No recursion needed** - all references exist

**Recursive Scenario:**

Creating entry for "Firebird Software":
1. Agent creates `/vault/firebird-software.mdx`
2. Identifies "See also": Elite, The Sentinel, Paradroid, Hewson Consultants
3. **Checks**: Do these entries exist?
   - Elite: ❌ Missing
   - The Sentinel: ❌ Missing
   - Paradroid: ✅ Exists
   - Hewson Consultants: ✅ Exists
4. **RECURSIVELY creates stubs**:
   - Creates `/vault/elite.mdx` (minimal stub)
   - Creates `/vault/the-sentinel.mdx` (minimal stub)
5. **Updates related entries**:
   - Adds "Firebird Software" to Elite's "See also"
   - Adds "Firebird Software" to The Sentinel's "See also"

**Recursion Limits:**
- Max depth: 2 levels (prevent infinite chains)
- Stub entries get flagged for expansion
- User reviews entry graph before committing

---

## Next Steps

**All specifications complete!** (Phases 0-5, 27 items total)

**Production testing priorities:**

1. **Phase 0 skills** (P0): Already tested with subagents ✅
2. **Phase 1 agents** (P1): Test with real lesson/curriculum specs
3. **Phase 2 agents** (P2): Test vault entries, pattern extraction, concept mapping, curriculum audit
4. **Phase 4 platform skills** (P1): Test lesson creation on all 7 platforms
5. **Phase 5 agents** (P3): Test lesson adaptation, dependency mapping, validator generation

**Infrastructure needed:**
- British English dictionary expansion
- Compilation commands registry (from platform skills)
- Screenshot methods registry (from platform skills)
- Platform specification files (for semantic-validator-generator-agent)

---

## Revision History

- **1.0 (2025-11-04)**: Initial roadmap with priorities and recursive Vault agent
- **2.0 (2025-11-05)**: All 27 specifications complete (P0-P3), added Phase 5 (Future Enhancements)

---

**Note**: Skills are created as markdown documents in `docs/skills/{skill-name}/SKILL.md`. Agents are dispatched via Task tool with `subagent_type` parameter as needed.
