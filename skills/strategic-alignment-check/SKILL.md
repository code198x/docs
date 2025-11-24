---
name: strategic-alignment-check
description: Use when validating lesson against project strategic principles - scans for copyright violations, nostalgia tourism, abstract theory, modern engines, instructor dependency using grep patterns and systematic checklist
---

# Strategic Alignment Check

## Overview

Every lesson must align with strategic principles in `/docs/CONTENT-CREATION-WORKFLOW.md` (see "Strategic Principles" section). Lessons violating core principles (copyright, nostalgia, abstract theory, modern engines, instructor dependency) must be rejected.

## When to Use

Use when:
- Validating new lesson content
- Reviewing lesson changes
- Part of lesson validation workflow
- Investigating why lesson feels "wrong"
- Before committing any lesson

**Do NOT:**
- Assume strategic alignment without checking
- Skip because "seems fine"
- Check only obvious violations

## Strategic Document

**Location:** `/docs/CONTENT-CREATION-WORKFLOW.md` → "Strategic Principles" section

**Read this section** before using this skill.

## Quick Violation Scan

### 1. Copyright Violations

**Forbidden:** Exact reproductions, copying sprites/graphics, recreating specific games

```bash
grep -iE "exact|replica|reproduction|recreat(e|ing)|pixel.perfect|copy|authentic|original game" [file.mdx]
```

**Red flags:** "Donkey Kong replica", "exact copy", "authentic sprites"

### 2. Nostalgia Tourism

**Forbidden:** Focus on memories, childhood, "remember when", nostalgia as motivation

```bash
grep -iE "remember|nostalg|childhood|memory|memories|magical|back in (19|the day)" [file.mdx]
```

**Red flags:** "Remember loading games?", "nostalgic joy", "magical memories"

### 3. Abstract Theory

**Forbidden:** Teaching concepts in isolation, theory without implementation, "memorize these"

```bash
grep -iE "theor(y|etical)|in isolation|memorize|memorise|later lessons|abstract concept|before we build" [file.mdx]
```

**Red flags:** "Understanding variables (theory)", "memorize these concepts", "we'll apply this later"

### 4. Modern Engines

**Forbidden:** Unity, Unreal, Godot, modern game engines

```bash
grep -iE "Unity|Unreal|Godot|modern engine|contemporary|GameMaker" [file.mdx]
```

**Red flags:** Any mention of modern engines (zero tolerance)

### 5. Instructor Dependency

**Forbidden:** Submit for grading, instructor feedback, grades, assessments

```bash
grep -iE "submit|grading|instructor|feedback|assignment|grade|assess(ment|ed)" [file.mdx]
```

**Red flags:** "Submit to your instructor", "grading rubric", "feedback required"

### 6. Shallow Coverage

**Forbidden:** "Quick survey", "brief overview", surface-level tours

```bash
grep -iE "quick (survey|overview|tour)|brief|surface.level|skim" [file.mdx]
```

**Red flags:** "Quick survey of platforms", "brief introduction"

## Systematic Checklist

**Use TodoWrite to track:**

### 1. Core Principles Check
- [ ] **Game-First Pedagogy** - Concepts taught through game implementation (not isolated theory)?
- [ ] **Hardware Intimacy** - Direct hardware access (sprites, joysticks, sound)?
- [ ] **Original Creation** - Inspired by classics, NOT reproductions?
- [ ] **Mastery Through Repetition** - Part of series, not one-off?
- [ ] **Self-Directed Learning** - No instructor/grading dependency?

### 2. Non-Goals Check
- [ ] **Not Nostalgia Tourism** - Focuses on skills, not memories?
- [ ] **Not Modern Engines** - No Unity/Unreal/Godot mention?
- [ ] **Not Reproductions** - No exact copies of existing games?
- [ ] **Not Quick Fixes** - Realistic about difficulty/time?
- [ ] **Not Shallow Coverage** - Deep treatment, not survey?
- [ ] **Not Instructor-Dependent** - Self-assessment only?
- [ ] **Not Abstract Theory** - Games teach concepts?

### 3. Quick Grep Scan
- [ ] Run copyright violation pattern
- [ ] Run nostalgia tourism pattern
- [ ] Run abstract theory pattern
- [ ] Run modern engines pattern
- [ ] Run instructor dependency pattern
- [ ] Run shallow coverage pattern

### 4. Code Reality Check
- [ ] Code compiles and runs?
- [ ] Code produces playable output?
- [ ] Code demonstrates stated concepts?

## Severity Assessment

### CRITICAL (Reject Immediately)
- Copyright violations (exact reproductions)
- Modern engine mentions (Unity, Unreal, Godot)

**Action:** Reject lesson completely. Cannot be salvaged.

### HIGH (Major Revision Required)
- Nostalgia tourism as primary motivation
- Abstract theory without game context
- Instructor dependency for assessment
- Non-working code

**Action:** Major rewrite required. Archive if significant work.

### MEDIUM (Needs Fixes)
- Shallow coverage language
- Minor nostalgia references (fixable)
- Unrealistic promises about ease

**Action:** Edit to fix violations. Document changes.

## Strategic Alignment Report Format

```
STRATEGIC ALIGNMENT CHECK: Lesson {NNN}

Strategic Document: /docs/CONTENT-CREATION-WORKFLOW.md (Strategic Principles section)

=== QUICK SCAN RESULTS ===

Copyright Violations:
  Found: [YES/NO]
  Issues: {list with line numbers}

Nostalgia Tourism:
  Found: [YES/NO]
  Issues: {list with line numbers}

Abstract Theory:
  Found: [YES/NO]
  Issues: {list with line numbers}

Modern Engines:
  Found: [YES/NO]
  Issues: {list with line numbers}

Instructor Dependency:
  Found: [YES/NO]
  Issues: {list with line numbers}

Shallow Coverage:
  Found: [YES/NO]
  Issues: {list with line numbers}

=== CORE PRINCIPLES ALIGNMENT ===

Game-First Pedagogy: [PASS/FAIL]
  Evidence: {specific examples}

Hardware Intimacy: [PASS/FAIL]
  Evidence: {specific examples}

Original Creation: [PASS/FAIL]
  Evidence: {specific examples}

Mastery Through Repetition: [PASS/FAIL / N/A]
  Evidence: {context in series}

Self-Directed Learning: [PASS/FAIL]
  Evidence: {assessment method}

=== SEVERITY SUMMARY ===

CRITICAL violations: {count}
HIGH violations: {count}
MEDIUM violations: {count}

=== VERDICT ===

Strategic Alignment: [ALIGNED / NEEDS FIXES / REJECT]

Recommendation: {specific action}
Reason: {explanation}
```

## Common Violations and Fixes

### Violation 1: Copyright Reproduction

**Bad:**
```markdown
# Recreating Space Invaders

Build a pixel-perfect replica of the 1978 arcade classic.
```

**Good:**
```markdown
# Wave Defense Game

Build an original wave-based shooter inspired by the genre.
```

### Violation 2: Nostalgia Motivation

**Bad:**
```markdown
Remember the joy of loading games from cassette tape? Let's recreate that magical feeling.
```

**Good:**
```markdown
Loading from tape taught timing and hardware interaction. You'll learn these skills through direct hardware access.
```

### Violation 3: Abstract Theory

**Bad:**
```markdown
## Understanding Variables (Theory)

Before we code, memorize these theoretical concepts about variables.
We'll apply them in future lessons.
```

**Good:**
```markdown
## Tracking Player Position

Let's track the player's X and Y coordinates using variables. Add this code...
```

### Violation 4: Modern Engines

**Bad:**
```markdown
Here's how you'd do this in Unity for comparison.
```

**Good:**
```markdown
[Remove entirely - no modern engine references]
```

### Violation 5: Instructor Dependency

**Bad:**
```markdown
Submit your game to your instructor for grading.
```

**Good:**
```markdown
Run your game. Can you reach the goal? Your working game is the proof of success.
```

## Common Mistakes

**Mistake 1:** "Just a small nostalgia reference"
- **Fix:** Strategic document says "Not Nostalgia Tourism". Any nostalgia focus violates this.

**Mistake 2:** "Mentioning Unity for context"
- **Fix:** Zero tolerance. "Not Modern Engines: No Unity, Unreal, Godot."

**Mistake 3:** "Theory first, then games"
- **Fix:** "Game-First Pedagogy" means games teach concepts, not theory-then-application.

**Mistake 4:** "Visual scan caught issues"
- **Fix:** Use grep patterns. Human scanning misses keywords.

**Mistake 5:** "Minor violation, probably OK"
- **Fix:** Check severity assessment. CRITICAL = reject immediately.

## Common Rationalizations

| Excuse | Reality |
|--------|---------|
| "Just one nostalgic reference" | Strategic document explicitly says "Not Nostalgia Tourism". Violations matter. |
| "Unity mention for comparison" | Zero tolerance on modern engines. Strategic boundary is clear. |
| "Theory makes concepts clearer" | "Game-First Pedagogy: Concepts emerge from implementation, never isolated drills." |
| "Students need instructor feedback" | "Self-Directed Learning: No instructor required." This is architectural. |
| "Donkey Kong is just an example" | "No reproductions. Respect copyright." Legal and strategic violation. |
| "Quick scan was thorough enough" | Grep finds keywords humans miss. Use systematic patterns. |

## Red Flags - Stop and Check

If you find yourself:
- Thinking "small violation doesn't matter"
- Defending nostalgia as "engagement"
- Explaining "just one theory section"
- Rationalizing modern engine mentions
- Saying "students want instructor feedback"
- Skipping grep patterns

**STOP. Read strategic document. Use checklist systematically.**

## Quick Reference

```bash
# Copyright violations
grep -iE "exact|replica|reproduction|recreat(e|ing)" lesson.mdx

# Nostalgia tourism
grep -iE "remember|nostalg|childhood|memory" lesson.mdx

# Abstract theory
grep -iE "theor(y|etical)|memorize|later lessons" lesson.mdx

# Modern engines (ZERO TOLERANCE)
grep -iE "Unity|Unreal|Godot" lesson.mdx

# Instructor dependency
grep -iE "submit|grading|instructor|feedback" lesson.mdx

# Read strategic document
cat /Users/stevehill/Projects/Code198x/docs/CONTENT-CREATION-WORKFLOW.md
```

## Integration with Other Skills

**This skill checks strategic alignment only.**

For complete validation:
1. **strategic-alignment-check** - Aligns with project principles
2. **curriculum-alignment-check** - Matches phase/tier curriculum
3. **voice-tone-check** - Proper tone, no marketing speak
4. **british-english-check** - British spellings
5. **lesson-validation** - Code compiles, runs, validates

## The Bottom Line

**Strategic principles are non-negotiable. CRITICAL violations = reject lesson.**

Run grep patterns. Use checklist. No Unity/Unreal/Godot. Ever.
