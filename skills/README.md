# Project-Specific Skills

This directory contains **skills** (process documentation) specific to the Code Like It's 198x project.

## What Are Skills?

Skills are structured process documents that enforce workflows. They prevent "working by luck and judgment" by encoding verified procedures.

**Key characteristics:**
- Mandatory steps with verification requirements
- Evidence-based completion (show output, don't just claim)
- Integration with TodoWrite for progress tracking
- Clear red flags and failure prevention

## Available Skills

### c64-lesson-creation

**Purpose:** Complete workflow for creating curriculum-aligned C64 BASIC lessons

**When to use:** Creating or editing ANY C64 lesson file

**What it enforces:**
- Curriculum verification (PHASE-0-CURRICULUM.md alignment)
- Code compilation (petcat with output shown)
- Screenshot capture (VICE with file verification)
- British English checking (grep for American spellings)
- Complete file verification (all locations checked)

**Why it exists:** Previous lessons created without this process had:
- Broken code that doesn't compile
- Missing screenshots
- Wrong concepts (curriculum drift)
- American English instead of British
- Indented BASIC code (violates BASIC V2)

**How to use:**
```bash
# Before creating/editing lesson N:
1. Read /docs/skills/c64-lesson-creation/SKILL.md
2. Follow EVERY step in order
3. Show evidence for each verification
4. Use TodoWrite to track progress
5. DO NOT claim completion without showing evidence
```

**Referenced in:** CLAUDE.md (project guidance file)

## How Skills Work

Skills use the **RED-GREEN-REFACTOR** pattern from Test-Driven Development:

1. **RED:** Document failures that happen without the skill
2. **GREEN:** Create skill that prevents those failures
3. **REFACTOR:** Close loopholes discovered through use

**Skills are living documents.** If you discover a failure mode not covered, update the skill.

## Skill Structure

Each skill has:
- **Frontmatter:** name, description, when_to_use, version
- **Overview:** Core principle
- **Workflow:** Step-by-step mandatory process
- **Verification:** Evidence requirements
- **Common Failures:** Red flags and prevention
- **Examples:** Correct vs incorrect approaches

## Integration with Superpowers Skills

This directory contains **project-specific** skills. These complement the **global** Superpowers skills:

**Global skills** (from Superpowers):
- verification-before-completion (evidence before claims)
- systematic-debugging (trace root causes)
- test-driven-development (write tests first)
- brainstorming (design before coding)

**Project skills** (this directory):
- c64-lesson-creation (C64 lesson workflow)

**Use both together:** Apply global patterns to project-specific work.

## Adding New Skills

When you notice a repeated failure pattern:

1. **Document the failure** - What goes wrong when skill doesn't exist?
2. **Create the skill** - Mandatory steps that prevent that failure
3. **Test it** - Try creating content with and without the skill
4. **Refine it** - Close loopholes discovered during use
5. **Reference it** - Update CLAUDE.md or other guidance docs

**Skills must include:**
- Clear "when to use" trigger
- Verification requirements (evidence, not claims)
- Common failure patterns
- Example of correct vs incorrect approach

## Why This Matters

**Without skills:** "I think the code works, lesson is probably complete"
**With skills:** "petcat compiled successfully [output shown], screenshots exist [ls output shown], curriculum verified [spec quoted], lesson complete with evidence"

**Skills turn subjective judgment into objective verification.**

---

**See also:**
- /CRITICAL-CURRICULUM-AUTHORITY.md (curriculum process)
- /docs/LESSON-PREFLIGHT-CHECKLIST.md (quality checklist)
- /docs/START-HERE.md (reference navigation)
