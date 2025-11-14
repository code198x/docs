---
name: voice-tone-check
description: Use when checking lesson content for voice/tone violations - scans for marketing speak, forbidden section headers, excessive hype, and tone consistency using systematic checklist and grep patterns
---

# Voice and Tone Check

## Overview

All lessons use a playful but rigorous tone. Avoid marketing speak, hype language, and forbidden section structures. British English throughout (use **british-english-check** skill for spellings).

## When to Use

Use when:
- Validating new lesson content
- Reviewing edited lessons
- Part of lesson validation workflow
- Investigating why lesson feels "off"
- Before committing any lesson

**Do NOT:**
- Rely on gut feeling about tone
- Skip because "it sounds fine"
- Check only titles, ignore body text

## Voice & Tone Guidelines

### The Tone

**Playful but rigorous:**
- Conversational without being condescending
- Technical without being dry
- Enthusiastic about concepts, not hyperbolic about results
- Focus on hardware/technical details, not vague promises

**Think:** Technical manual written by someone who genuinely enjoys the hardware

**Not:** Marketing copy for a product launch

### What's Forbidden

#### Explicitly Forbidden Section Headers

**NEVER use these section titles:**
- "WOW Moment" / "Wow Moment"
- "Insight Block" / "Insights"
- "Mind-Blowing Discovery"
- "Pro Tip" (unless part of established archetype)
- Any section header with emoji

**Why:** From CLAUDE.md: "NO 'Insight' blocks or 'WOW Moment' sections"

#### Marketing Speak (Unjustified Hype)

**Forbidden without specific justification:**
- amazing, stunning, incredible, breathtaking, revolutionary
- epic, awesome, mind-blowing, game-changing
- unlock, power, magic, secret, insider
- transform, revolutionize, discover the truth
- journey, dive deep, blow your mind

**Use technical descriptions instead:**
- "fast" not "blazingly fast"
- "efficient" not "incredibly optimized"
- "16 colors" not "stunning color palette"

#### Excessive Punctuation

- **Exclamation marks:** Rarely justified. Use periods.
- **Multiple exclamations:** Never. One is pushing it.
- **ALL CAPS:** Only for technical constants (like POKE, PRINT in code context)

## Quick Check Patterns

### 1. Forbidden Headers Check

```bash
grep -in "wow moment\|insight block\|pro tip\|mind.blow" [file.mdx]
```

If matches found → Violation. Rename sections.

### 2. Marketing Speak Check

```bash
grep -iE "amazing|stunning|incredible|breathtaking|revolutionary|epic|awesome|mind.blow|game.chang|unlock|transform|revolutioniz|discover the|journey|dive deep" [file.mdx]
```

Review each match - is it justified by technical reality?

### 3. Emoji in Headers Check

```bash
grep "^##.*[🎨💡🚀✨⚡]" [file.mdx]
```

If matches found → Remove emojis from headers.

### 4. Exclamation Mark Check

```bash
grep -o "!" [file.mdx] | wc -l
```

**Guidelines:**
- 0-2 in entire lesson: Good
- 3-5: Borderline (review each)
- 6+: Too many (reduce)

## Systematic Review Checklist

**Use TodoWrite to track:**

### 1. Forbidden Sections
- [ ] Run grep for forbidden section headers
- [ ] Check for emoji in any section headers
- [ ] Verify no "WOW Moment" or "Insight Block" sections

### 2. Marketing Language
- [ ] Run marketing speak grep pattern
- [ ] Review each match - justified or hype?
- [ ] Check opening paragraph - technical or promotional?
- [ ] Verify claims are specific (not vague promises)

### 3. Punctuation
- [ ] Count exclamation marks (should be 0-2)
- [ ] Check for ALL CAPS outside code context
- [ ] Verify periods used for factual statements

### 4. Tone Consistency
- [ ] Opening focuses on technical facts (not hype setup)
- [ ] Explanations reference hardware/addresses/specifics
- [ ] Enthusiasm about concepts, not about "power" or "magic"
- [ ] Compare to exemplar lessons (007-008 for Discovery tier)

### 5. British English
- [ ] Use **british-english-check** skill (separate check)

## Tone Report Format

```
VOICE & TONE CHECK: Lesson {NNN}

=== FORBIDDEN SECTIONS ===
Found: [YES/NO]
Issues:
  - Line X: "{section title}" → {recommended change}

=== MARKETING SPEAK ===
Found: [number] instances
Issues:
  - Line X: "{hype word/phrase}" → {technical alternative}

=== EXCLAMATION MARKS ===
Count: {number}
Status: [GOOD / BORDERLINE / EXCESSIVE]
Action: {reduce/acceptable}

=== TONE CONSISTENCY ===
Opening: [TECHNICAL / PROMOTIONAL]
Body: [RIGOROUS / VAGUE]
Overall: [PASS / NEEDS REVISION]

=== VERDICT ===
Voice & Tone: [ACCEPTABLE / NEEDS FIXES / MAJOR REVISION]

Recommendation: {specific changes or accept}
```

## Common Violations and Fixes

### Violation 1: Hype Opening

**Bad:**
```markdown
# Unlock the Power of Color!

Get ready for an incredible journey into color programming!
```

**Good:**
```markdown
# Character Color Memory

Lesson 7 changed border colors. Now control individual character colors by writing to color memory at address 55296.
```

### Violation 2: "WOW Moment" Section

**Bad:**
```markdown
## 🎨 WOW Moment: Direct Hardware Access!
```

**Good:**
```markdown
## Direct Memory Access

The VIC-II chip reads from address 55296 for color data.
```

### Violation 3: Unjustified Hype

**Bad:**
```markdown
This stunning technique will revolutionize your programs!
```

**Good:**
```markdown
Writing directly to color memory updates the screen immediately without affecting screen codes.
```

### Violation 4: Marketing Clichés

**Bad:**
```markdown
Let's dive deep into this amazing discovery!
```

**Good:**
```markdown
Color memory uses the same 40×25 grid layout as screen memory.
```

## Reference: Good Tone Examples

From Lesson 007 (exemplar):
- Opening: "Lesson 6 showed..."  (builds on prior, factual)
- Technical: "POKE 53280,6 sets border to blue" (specific address, specific effect)
- Enthusiastic: "Try different values" (encouraging, not hype)

From Lesson 008 (exemplar):
- Conversational: "whilst the programme runs" (British English, natural voice)
- Precise: "address 1024 marks top-left" (technical specifics)
- Rigorous: Explains hardware reasons, not just "it works"

## Common Mistakes

**Mistake 1:** "It's just a little enthusiasm"
- **Fix:** Enthusiasm about concepts (yes), hype about results (no)

**Mistake 2:** "Visual scan for tone"
- **Fix:** Use grep patterns. Marketing speak is easy to miss by eye.

**Mistake 3:** "One exclamation mark is fine"
- **Fix:** Probably is, but check context. Factual statements use periods.

**Mistake 4:** "Forbidden sections with different names are OK"
- **Fix:** "💡 Key Insight" is still a forbidden "Insight Block". No emoji headers.

**Mistake 5:** "British English check covers this"
- **Fix:** Separate concerns. British English = spellings. This = tone.

## Common Rationalizations

| Excuse | Reality |
|--------|---------|
| "Just a bit of excitement" | Marketing speak undermines credibility. Use technical facts. |
| "Students like enthusiastic tone" | Yes - about concepts. Not about vague "power" and "magic". |
| "WOW Moment in different words is fine" | No. Any "insight block" variation is forbidden. |
| "Quick scan caught the issues" | Grep finds patterns humans miss. Use systematic check. |
| "Lesson sounds engaging" | "Engaging" ≠ "promotional". Technical enthusiasm, not hype. |

## Red Flags - Stop and Check

If you find yourself:
- Thinking "it sounds exciting and engaging"
- Scanning visually without grep
- Defending "just one" forbidden section
- Saying "students will love this energy"
- Comparing to marketing materials (not technical docs)

**STOP. Run grep patterns. Use checklist systematically.**

## Quick Reference

```bash
# Check forbidden sections
grep -in "wow moment\|insight block\|pro tip" lesson.mdx

# Check marketing speak
grep -iE "amazing|stunning|incredible|epic|awesome" lesson.mdx

# Count exclamation marks
grep -o "!" lesson.mdx | wc -l

# Find emoji headers
grep "^##.*[🎨💡🚀✨⚡]" lesson.mdx

# British English (separate skill)
# Use british-english-check skill
```

## Integration with Other Skills

**This skill checks tone only.**

For complete validation:
1. **british-english-check** - American vs British spellings
2. **voice-tone-check** - Marketing speak, forbidden sections, tone
3. **curriculum-alignment-check** - Content matches curriculum
4. **lesson-validation** - Compilation, semantic validation, files

## The Bottom Line

**Playful but rigorous. Technical facts, not marketing hype.**

Run grep patterns. No "WOW Moment" or "Insight Block" sections. Ever.
