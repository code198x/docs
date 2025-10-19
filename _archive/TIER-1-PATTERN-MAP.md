# Tier 1 Pattern Usage Map

**Purpose:** Quick reference for which patterns to use/create for each Tier 1 lesson
**Updated:** 2025-01-17 (before Tier 1 rewrite begins)

---

## Lessons 1-6: Programming Foundations

### Lesson 1: Hello, Computer
- **Pattern:** None needed (basic PRINT/RUN/GOTO)
- **Action:** None

### Lesson 2: Counting
- **Pattern:** None needed (basic variables)
- **Action:** None

### Lesson 3: Repeating Yourself
- **Pattern:** None needed (basic FOR...NEXT)
- **Action:** None (may extract from current L2 if useful)

### Lesson 4: Making Decisions
- **Pattern:** None needed (basic IF...THEN)
- **Action:** None

### Lesson 5: Collections
- **Pattern:** None needed (basic arrays)
- **Action:** None (may extract from current L9 if useful)

### Lesson 6: Data Everywhere
- **Pattern:** `data/read-data-pattern` ✅ EXISTS
- **Action:**
  1. Read existing pattern
  2. Use simplest variation for quiz program WOW
  3. Update `lessonsAppearIn` to add "Lesson 6"

---

## Lessons 7-11: Hardware Introduction

### Lesson 7: The First Color
- **Pattern:** `vic-ii/border-background-colors` ❌ MISSING - CREATE
- **Action:**
  1. Write lesson first
  2. Extract WOW moment (rainbow border animation)
  3. Create new pattern following existing structure
  4. Document POKE 53280/53281, color palette 0-15
  5. Include 5-6 variations (static colors, cycling, palette demo)

### Lesson 8: Painting the Screen
- **Pattern:** `screen/direct-writing` ❌ MISSING - CREATE
- **Action:**
  1. Write lesson first
  2. Extract WOW moment (pattern drawing)
  3. Create new pattern
  4. Document screen memory 1024-2023, color memory 55296+
  5. Include position calculation, character vs. screen codes

### Lesson 9: Character Graphics
- **Pattern:** `petscii/character-graphics` ❌ MISSING - CREATE
- **Action:**
  1. Write lesson first
  2. Extract WOW moment (border/box drawing)
  3. Create new pattern
  4. Document CHR$(), graphics characters, reverse video
  5. Include box-drawing character reference table

### Lesson 10: First Sound
- **Pattern:** `sound/sid-initialization` ✅ EXISTS
- **Action:**
  1. Read existing pattern thoroughly
  2. Use simplest variation (single triangle wave tone)
  3. Adapt ADSR explanation for first exposure
  4. Update `lessonsAppearIn` to replace "7" with "10"
  5. Verify "See Also" section cross-references

### Lesson 11: Sound Effects
- **Pattern:** `sound/sound-effects` ✅ EXISTS (verify)
- **Action:**
  1. Verify pattern exists (if not, create it)
  2. Use ADSR variations for different effect types
  3. Update `lessonsAppearIn` to add "Lesson 11"
  4. May need to expand pattern with explosion/beep/pickup examples

---

## Lessons 12-15: Interactive Foundation

### Lesson 12: Listening to the Player
- **Pattern:** `input/keyboard-polling` ✅ EXISTS
- **Action:**
  1. Read existing pattern thoroughly
  2. Use WASD variation for WOW moment (move @ around screen)
  3. Extract special key codes table (cursor keys, SPACE, RETURN)
  4. Update `lessonsAppearIn` to replace "25" with "12"
  5. Verify pattern's integration example is suitable

### Lesson 13: Random Events
- **Pattern:** `random/rnd-generation` ❌ MISSING - CREATE
- **Action:**
  1. Write lesson first
  2. Extract WOW moment (random stars appearing)
  3. Create new pattern
  4. Document RND(1), INT scaling, RND(-TI) seeding
  5. Include dice rolls, percentage chances, range generation

### Lesson 14: Game Logic Basics
- **Pattern:** None specific (concepts from multiple patterns)
- **Action:**
  1. May reference `input/keyboard-polling` for movement
  2. Simple collision doesn't need dedicated pattern yet
  3. Score tracking is basic variable use

### Lesson 15: Timing
- **Pattern:** `timing/ti-jiffy-clock` ❌ MISSING - CREATE
- **Action:**
  1. Write lesson first (may adapt from current L6 TI timing section)
  2. Extract WOW moment (countdown timer)
  3. Create new pattern
  4. Document TI jiffy clock, TI$ formatted time, frame-accurate delays
  5. Include delay patterns, clock display, reset technique

---

## Lesson 16: SYNTHESIS - Text Adventure

### Lesson 16: Text Adventure
- **Patterns:** Multiple patterns combine
- **Action:**
  1. Uses colors (from L7 pattern)
  2. Uses screen writing (from L8 pattern)
  3. Uses sound (from L10/L11 patterns)
  4. Uses input (from L12 pattern)
  5. Uses random (from L13 pattern)
  6. No new pattern created (synthesis lesson)

---

## Pattern Creation Priority

**Must create before writing these lessons:**

1. **NONE** - Write lessons first, extract patterns after

**Pattern creation workflow:**
1. Write the lesson following curriculum specs
2. Complete WOW moment code and test in VICE
3. Extract core technique from WOW moment
4. Create pattern file following existing structure
5. Add 5-6 variations showing different use cases
6. Document common mistakes encountered during lesson writing
7. Cross-reference back to lesson

---

## Pattern Update Workflow

**For each lesson that uses an existing pattern:**

1. **Before writing lesson:**
   - Read pattern thoroughly
   - Identify simplest variation suitable for first exposure
   - Note register addresses, memory locations, key techniques

2. **While writing lesson:**
   - Use pattern as technical foundation
   - Add pedagogical scaffolding (narrative, progression, context)
   - Expand WOW moment beyond pattern's basic example
   - Reference pattern in lesson's "See Also" section

3. **After lesson complete:**
   - Open pattern MDX file
   - Update `lessonsAppearIn` frontmatter
   - Add lesson to pattern's "See Also" section
   - Commit pattern update with lesson

---

## Missing Patterns Summary

**Total to create:** 5 beginner patterns

| Pattern | Lesson | Difficulty | Estimated Time |
|---------|--------|------------|----------------|
| `vic-ii/border-background-colors` | L7 | Beginner | 45-60 min |
| `screen/direct-writing` | L8 | Beginner | 60-90 min |
| `petscii/character-graphics` | L9 | Beginner | 45-60 min |
| `random/rnd-generation` | L13 | Beginner | 45-60 min |
| `timing/ti-jiffy-clock` | L15 | Beginner | 45-60 min |

**Total time investment:** ~4-6 hours (spread across lesson writing)

---

## Pattern File Locations

**Existing patterns:**
- `/website/src/pages/commodore-64/phase-0/patterns/sound/sid-initialization.mdx`
- `/website/src/pages/commodore-64/phase-0/patterns/input/keyboard-polling.mdx`
- `/website/src/pages/commodore-64/phase-0/patterns/data/read-data-pattern.mdx`
- `/website/src/pages/commodore-64/phase-0/patterns/sound/sound-effects.mdx` (verify exists)

**New patterns to create:**
- `/website/src/pages/commodore-64/phase-0/patterns/vic-ii/border-background-colors.mdx`
- `/website/src/pages/commodore-64/phase-0/patterns/screen/direct-writing.mdx`
- `/website/src/pages/commodore-64/phase-0/patterns/petscii/character-graphics.mdx`
- `/website/src/pages/commodore-64/phase-0/patterns/random/rnd-generation.mdx`
- `/website/src/pages/commodore-64/phase-0/patterns/timing/ti-jiffy-clock.mdx`

---

## Pattern Template Reference

Every pattern follows this structure (from existing patterns):

```markdown
---
layout: ../../../../../layouts/PatternLayout.astro
title: "Pattern Name"
category: "Category"
difficulty: "Beginner"
lessonsAppearIn: "Lessons X, Y, Z"
system: "C64"
---

## Overview
[One-sentence description of what pattern does]

## The Pattern
[Core code example - minimal, clear]

## Parameters
[Table: Variable | Type | Purpose | Range/Values]

## How It Works
### Step 1: [First action]
### Step 2: [Second action]
[etc.]

## Variations
### Variation 1: [Name]
[Code example]
**Use case:** [When to use this]

[5-6 variations total]

## Common Mistakes
- **Mistake 1**: [Description]
  - **Symptom**: [What happens]
  - **Fix**: [How to solve]

## Memory Usage
[Exact byte counts, register addresses]

## Integration Example
[Complete runnable program showing pattern in context]

## See Also
- [Related patterns]
- **Lessons**: X, Y, Z
- **Vault**: [Relevant vault entries]

## Quick Reference Card
[Copy-paste ready code block]
```

---

**Next Steps:**
1. Begin writing Lesson 1 (already aligned, minimal pattern work)
2. Progress through Lessons 2-6 (foundations, no patterns needed)
3. Hit Lesson 7 → Write lesson → Create VIC-II colors pattern
4. Continue through Tier 1, creating patterns as needed

---

**End of Map**
