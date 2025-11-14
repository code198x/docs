---
name: british-english-check
description: Use when checking lesson content for American vs British English spellings - runs comprehensive grep pattern to find American spellings, with program exception for computer programs
---

# British English Check

## Overview

All lesson content uses British English (colour, learnt, organised) with ONE critical exception: "program" when referring to computer programs is always correct.

## When to Use

Use when:
- Validating new lesson content
- Checking edited lessons before commit
- Reviewing any MDX documentation
- Part of lesson validation workflow

**Do NOT:**
- Check code samples inside code blocks (those follow platform conventions)
- Change "program" to "programme" (computer programs always use "program")
- Rely on visual inspection alone

## Standard Check Command

```bash
grep -in "color\|behavior\|favor\|honor\|labor\|organize\|recognize\|realize\|analyze\|learned\|skeptic\|gray\|center\|meter\|liter\|defense\|offense\|license" [file.mdx]
```

**Flags:**
- `-i`: Case insensitive
- `-n`: Show line numbers

## Common American → British Mappings

| American | British | Exception |
|----------|---------|-----------|
| color | colour | — |
| behavior | behaviour | — |
| favor | favour | — |
| honor | honour | — |
| labor | labour | — |
| organize | organise | — |
| recognize | recognise | — |
| realize | realise | — |
| analyze | analyse | — |
| learned | learnt | — |
| skeptic | sceptic | — |
| gray | grey | — |
| center | centre | — |
| meter | metre | (unit of measure) |
| liter | litre | — |
| defense | defence | — |
| offense | offence | — |
| license (verb) | licence (verb) | — |
| program | programme | **"program" for computers** |

## The Program Exception

**ALWAYS CORRECT:**
- "computer program"
- "program the computer"
- "this program demonstrates"
- "run the program"
- "example program"

**Context matters:** If it's about computer programs, "program" is correct. Don't change it.

## Check Workflow

1. **Run grep command** on lesson file
2. **Review each match:**
   - Is it in prose text? → Should be British
   - Is it in code block? → Ignore (follows platform conventions)
   - Is it "program" referring to computer program? → Correct, ignore
3. **Report findings** with line numbers
4. **User decides** which to fix

## Report Format

```
BRITISH ENGLISH CHECK: lesson-NNN.mdx

Line 6: "colors" → should be "colours"
Line 12: "optimize" → should be "optimise"
Line 24: "learned" → should be "learnt"
Line 18: "program" → CORRECT (computer program exception)

Found 3 American spellings to fix.
```

## Common Mistakes

**Mistake 1:** Visual inspection only
- **Fix:** Always run grep command with comprehensive pattern

**Mistake 2:** Changing "program" to "programme"
- **Fix:** Check context - computer programs use "program"

**Mistake 3:** Checking code samples
- **Fix:** Only check prose text, not code inside code blocks

**Mistake 4:** Using incomplete pattern
- **Fix:** Use the standard command above with full pattern

**Mistake 5:** "I'll remember to check"
- **Fix:** Part of mandatory validation, run explicitly

## Common Rationalizations

| Excuse | Reality |
|--------|---------|
| "Visual scan is faster" | Grep takes 2 seconds and catches everything. Visual scanning takes longer and misses things. |
| "I'll just check for color/colour" | Pattern has 17+ spelling pairs. You'll miss half of them. |
| "Program should be programme" | NO. Computer programs always use "program". This is explicit project policy. |
| "Code is urgent, skip this check" | Time pressure demands reliability. Grep is faster than scanning anyway. |
| "I'm good at spotting British English" | You're not. Grep finds 100% of instances, humans miss things. |

## Red Flags - Stop and Use Skill

If you find yourself:
- Scanning visually instead of using grep
- Saying "just check for color/colour"
- Flagging "program" as incorrect
- Skipping because "urgent"
- Confident you can spot them manually

**STOP. Run the grep command. Follow the skill.**

## Quick Reference

```bash
# Check single file
grep -in "color\|behavior\|favor\|honor\|labor\|organize\|recognize\|realize\|analyze\|learned\|skeptic\|gray\|center\|meter\|liter\|defense\|offense\|license" lesson-007.mdx

# Check multiple lessons
grep -in "color\|...\|license" website/src/pages/commodore-64/phase-0/tier-1/lesson-*.mdx

# REMEMBER: "program" for computer programs is ALWAYS correct
```

## The Bottom Line

**Run grep with comprehensive pattern. Report findings. User decides fixes.**

"program" for computer programs is correct. Don't change it.
