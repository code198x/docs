# Lesson Template - Code Like It's 198x

**Version:** 1.0
**Date:** 2025-10-21
**Purpose:** Standard structure for all C64 lessons

---

## File Location

Lessons are stored in:
```
/website/src/pages/commodore-64/phase-X/tier-Y/lesson-NNN.mdx
```

**Naming convention:**
- Phase: `phase-0` through `phase-16`
- Tier: `tier-1` through `tier-8` (varies by phase)
- Lesson: `lesson-001.mdx` through `lesson-8256.mdx` (zero-padded, 3 digits)

---

## Frontmatter Template

```yaml
---
layout: ../../../../layouts/LessonLayout.astro
title: "[Compelling Title - What Student Will Do]"
game: "Commodore 64 BASIC"  # or "6502 Assembly" for Phase 1+
system: "C64"
phase: 0  # 0-16
tier: 1   # 1-8 (depending on phase)
lessonNumber: 1  # 1-8256
totalLessons: 64  # 64 for Phase 0, 8256 total
prevLesson: "/commodore-64/phase-0/tier-1/lesson-000"  # or null for first lesson
nextLesson: "/commodore-64/phase-0/tier-1/lesson-002"  # or null for last lesson
objectives:
  - '[Objective 1 - specific, measurable, action-oriented]'
  - '[Objective 2 - builds on previous lessons]'
  - '[Objective 3 - introduces new concept]'
---
```

---

## Content Structure

### 1. Opening Hook (Required)
**Format:** `## [Catchy Heading]`

Start with context and motivation. Answer "Why does this matter?" Connect to student's journey.

**Example:**
```markdown
## Beyond PRINT

You've changed border and background colours—now you're going to paint the screen directly. The C64's text display isn't just for typing; it's a grid of 1000 character positions...
```

**Guidelines:**
- 2-4 sentences
- Reference previous lessons
- Create excitement/curiosity
- Avoid condescension (no "Amazing!", "Cool!", etc.)

---

### 2. The One-Minute Tour (Required)
**Format:** `### The One-Minute Tour`

Bullet-point summary of key concepts. Quick reference for students returning later.

**Example:**
```markdown
### The One-Minute Tour

- Screen memory starts at address 1024 (top-left corner)
- Each screen position has an address: 1024 to 2023
- POKE a character code (0-255) to display that character
- Colour memory starts at 55296 (same grid layout)
- Calculate position: `1024 + (row * 40) + column`
```

**Guidelines:**
- 4-8 bullet points
- Factual, concise
- Use backticks for code/values
- No explanations (that's for later sections)

---

### 3. Example Program (Required)
**Format:** `### Example Program`

Working BASIC or assembly code that demonstrates the concept.

**Example:**
```markdown
### Example Program

```basic
10 PRINT CHR$(147)
20 POKE 1024,42
30 POKE 1024+40,42
40 POKE 1024+80,42
50 END
```

Sample output:

```
*
*
*
READY.
```

![Screenshot description](/images/commodore-64/phase-0/tier-1/lesson-NNN/example-1.png)

**Line 10** clears screen. **Lines 20-40** POKE character 42 (asterisk) to three vertical positions. Each position is 40 bytes apart (one row down).

> **Tip:** Character code 42 is an asterisk (*) in C64 screen codes. Screen codes differ from PETSCII/ASCII.
```

**Guidelines:**
- Code must be complete and runnable
- Include sample output (text or screenshot)
- Explain key lines with **bold line numbers**
- Add one practical tip in blockquote
- Keep code short (10-20 lines ideal for BASIC)
- Image path: `/images/commodore-64/phase-X/tier-Y/lesson-NNN/example-N.png`

---

### 4. Experiment Section (Required)
**Format:** `### Experiment Section`

Hands-on variations and a more complex example.

**Example:**
```markdown
### Experiment Section

Try these variations:

- **Horizontal line**: Change line spacing to +1 instead of +40
- **Diagonal line**: Add both row and column: `1024+(I*41)` in a loop
- **Fill screen**: Use a FOR loop from 1024 to 2023
- **Different characters**: Try code 160 (solid block) or 102 (checkerboard)

Build a simple pattern drawer:

```basic
10 PRINT CHR$(147)
20 FOR R=0 TO 24
30 FOR C=0 TO 39
40 SC=1024+(R*40)+C
50 POKE SC,160
60 NEXT C
70 NEXT R
80 END
```

The programme fills the screen with solid blocks in a grid pattern.

![Pattern demonstration](/images/commodore-64/phase-0/tier-1/lesson-NNN/example-2.png)
```

**Guidelines:**
- 4-6 quick variations (bulleted)
- One longer example program
- Screenshot for longer example
- British spelling ("programme", "colour") for authenticity
- Encourage modification, not just copying

---

### 5. Concept Expansion (Optional)
**Format:** `### Concept Expansion`

Deeper explanation of WHY things work this way. Hardware details, historical context, technical depth.

**Example:**
```markdown
### Concept Expansion

**Screen memory is a character grid.** Unlike modern graphics where you draw pixels, the C64 text mode displays 8×8 character blocks. Memory location 1024 is the top-left corner, 1063 is top-right (1024+39), 1064 is second row start, and 2023 is bottom-right.

**Why 1024?** The C64's default screen memory starts at $0400 in hexadecimal (1024 decimal). You can actually move screen memory to different addresses (like $C000 for double-buffering), but that's for later lessons.
```

**Guidelines:**
- Use **bold subheadings** for topics
- Explain the "why" and "how"
- Reference designers/engineers when relevant
- Foreshadow future lessons
- Keep it conversational but accurate

---

### 6. Game Integration (Required)
**Format:** `### Game Integration`

Practical applications in real games. How this technique appears in actual C64 games or game development.

**Example:**
```markdown
### Game Integration

- **Draw borders**: Create boxes around play areas with character graphics
- **Status displays**: Draw health bars using repeated block characters
- **Tile maps**: Place maze walls, floors, treasure icons by POKEing codes
- **Sprite-free graphics**: Simple games can use character graphics before sprites
- **Instant updates**: No waiting for PRINT—POKE is immediate
```

**Guidelines:**
- 4-6 bulleted examples
- Reference classic games when appropriate (educational reference only!)
- Show how concept builds toward complete games
- Be specific (not "make graphics" but "draw health bars")

---

### 7. From the Vault (Optional)
**Format:** `### From the Vault`

Links to reference documentation in `/docs/` or external resources.

**Example:**
```markdown
### From the Vault

- [Screen Memory Map](/vault/screen-memory-map) — complete layout of all 1000 positions
- [PETSCII Chart](/vault/petscii-chart) — all 256 character codes
- [Colour Memory](/vault/colour-memory) — how colour RAM works
- [6510 CPU](/vault/6510-cpu) — the processor evaluating your conditions
```

**Guidelines:**
- Link to curriculum reference docs
- Link to external resources (CSDb, chip specs, etc.)
- Use em dash (—) for descriptions
- 2-5 links maximum
- Only include if genuinely helpful

---

### 8. Quick Reference (Required)
**Format:** `### Quick Reference`

Tables, formulas, or lists for quick lookup.

**Example:**
```markdown
### Quick Reference

| Memory Area | Address Range | Purpose |
|-------------|---------------|---------|
| Screen RAM | 1024-2023 | Character codes (what to display) |
| Colour RAM | 55296-56295 | Colour values (what colour) |

**Position Calculation:**
```
Screen address = 1024 + (row * 40) + column
Colour address = 55296 + (row * 40) + column
```

**Common Character Codes (Screen Codes, Uppercase Mode):**
```
32 = Space       42 = *          160 = Solid block
65 = A           81 = ●          102 = Checkerboard
```

> **Note for .bas files:** The downloadable code samples use lowercase keywords (e.g., `poke` instead of `POKE`) for technical compatibility with the petcat converter tool.
```

**Guidelines:**
- Tables for structured data
- Code blocks for formulas/calculations
- Keep it scannable
- Include technical notes in blockquotes
- Hex values in $XXXX format, decimal in plain numbers

---

### 9. What You've Learnt (Required)
**Format:** `### What You've Learnt`

Summary of lesson accomplishments and preview of next lesson.

**Example:**
```markdown
### What You've Learnt

- Screen memory (1024-2023) stores which character appears at each position
- Colour memory (55296+) stores the colour for each character
- Calculate position with `1024 + (row * 40) + column`
- POKE writes characters instantly anywhere on screen
- Character graphics let you draw patterns, boxes, and game graphics

**Next lesson:** We'll explore PETSCII character graphics and special characters (borders, blocks, card suits) to create detailed visual designs.
```

**Guidelines:**
- 4-6 bullet points summarizing achievements
- Bold "Next lesson:" preview
- Past tense for accomplishments ("learnt", not "learned")
- British spelling throughout
- Preview creates anticipation

---

## Writing Guidelines

### Tone and Voice

**DO:**
- Be conversational but precise
- Use British spelling (programme, colour, learnt)
- Reference hardware designers and engineers by name
- Acknowledge C64's limitations honestly
- Create excitement through discovery, not hype
- Use second person ("you've learnt", "you'll create")

**DON'T:**
- Use exclamation marks excessively
- Say "amazing", "awesome", "cool" without justification
- Condescend or over-explain obvious points
- Ignore hardware constraints
- Make false promises about BASIC speed

### Code Style

**BASIC:**
- Use uppercase for commands in prose (`POKE`, `PRINT`, `FOR`)
- Use lowercase in actual .bas files (petcat compatibility)
- Line numbers every 10 (10, 20, 30...)
- Keep programs short and focused
- Comment with REM sparingly (code should be clear)

**Assembly (Phase 1+):**
- Uppercase mnemonics (LDA, STA, JSR)
- Lowercase labels (init_screen, player_x)
- Comment WHY, not WHAT
- Include cycle counts for timing-critical sections

### Screenshots

**Required for:**
- Every Example Program
- Complex Experiment Section programs
- Concept demonstrations

**File naming:**
```
/images/commodore-64/phase-X/tier-Y/lesson-NNN/example-N.png
```

**Guidelines:**
- Actual VICE emulator screenshots (authentic)
- Crop to relevant area
- Clear, readable text
- Show before/after when appropriate

### Assets

**If lesson uses sprites/music/characters:**

Reference assets from repository:
```markdown
## Assets Needed

- Paddle sprite: [Download lesson-001-pong-paddle.spd](/assets/sprites/phase-1/lesson-001-pong-paddle.spd)
- Ball sprite: [Download lesson-001-pong-ball.spd](/assets/sprites/phase-1/lesson-001-pong-ball.spd)

**Or create your own** - See Lesson 5: Sprite Creation Tutorial
```

See [ASSET-GUIDELINES.md](/docs/ASSET-GUIDELINES.md) for details.

---

## Section Order Summary

1. **Frontmatter** (YAML, required)
2. **Opening Hook** (## heading, required)
3. **The One-Minute Tour** (### heading, required)
4. **Example Program** (### heading, required)
5. **Experiment Section** (### heading, required)
6. **Concept Expansion** (### heading, optional)
7. **Game Integration** (### heading, required)
8. **From the Vault** (### heading, optional)
9. **Quick Reference** (### heading, required)
10. **What You've Learnt** (### heading, required)

---

## Lesson Filename Example

```
/website/src/pages/commodore-64/phase-0/tier-3/lesson-033.mdx
```

For Phase 0, Tier 3, Lesson 33 (Advanced Animation)

---

## Complete Example Skeleton

```mdx
---
layout: ../../../../layouts/LessonLayout.astro
title: "Advanced Animation"
game: "Commodore 64 BASIC"
system: "C64"
phase: 0
tier: 3
lessonNumber: 33
totalLessons: 64
prevLesson: "/commodore-64/phase-0/tier-2/lesson-032"
nextLesson: "/commodore-64/phase-0/tier-3/lesson-034"
objectives:
  - 'Create multi-frame sprite animation sequences.'
  - 'Implement animation state machines for complex movement.'
  - 'Time frame transitions for smooth character motion.'
---

## [Opening Hook Title]

[2-4 sentences creating context and excitement]

---

### The One-Minute Tour

- [Key concept 1]
- [Key concept 2]
- [Key concept 3]
- [Key concept 4]

---

### Example Program

```basic
10 REM [Program description]
20 [Code]
```

Sample output:
```
[Expected output]
```

![Screenshot](/images/commodore-64/phase-0/tier-3/lesson-033/example-1.png)

**Line 10** [explanation]

> **Tip:** [Practical advice]

---

### Experiment Section

Try these variations:

- **[Variation 1]**: [Description]
- **[Variation 2]**: [Description]

Build a [more complex example]:

```basic
[Code]
```

[Explanation]

![Screenshot](/images/commodore-64/phase-0/tier-3/lesson-033/example-2.png)

---

### Concept Expansion

**[Subheading]** [Deep explanation]

---

### Game Integration

- **[Use case 1]**: [Description]
- **[Use case 2]**: [Description]

---

### From the Vault

- [Reference 1](/vault/link) — description
- [Reference 2](/vault/link) — description

---

### Quick Reference

[Tables, formulas, code samples]

> **Note:** [Technical notes]

---

### What You've Learnt

- [Achievement 1]
- [Achievement 2]
- [Achievement 3]

**Next lesson:** [Preview of next lesson]

---
```

---

## Phase-Specific Notes

### Phase 0 (BASIC)
- Focus on POKE, PEEK, loops, conditionals
- Honest about speed limitations
- Tier 3 explicitly shows BASIC ceiling (flicker, stuttering)
- Lesson 64 transitions to assembly

### Phase 1+ (Assembly)
- Include cycle counts for timing-critical code
- Reference hardware specs (VIC-II, SID, CIA)
- Show memory-efficient techniques
- Build toward complete games

---

## Quality Checklist

Before publishing a lesson:

- [ ] Frontmatter complete and accurate
- [ ] Lesson number matches filename and phase/tier
- [ ] Code examples tested in VICE
- [ ] Screenshots captured and correctly linked
- [ ] British spelling throughout (programme, colour, learnt)
- [ ] Objectives are specific and measurable
- [ ] "Next lesson" preview included
- [ ] Quick Reference table/code included
- [ ] Tone is conversational but precise
- [ ] No excessive exclamation marks or hype
- [ ] Assets referenced if needed (with download links)

---

**Version:** 1.0
**Date:** 2025-10-21
**Maintained by:** Code Like It's 198x curriculum team
**See also:** [LESSON-WORKFLOW.md](LESSON-WORKFLOW.md), [LESSON-PREFLIGHT-CHECKLIST.md](LESSON-PREFLIGHT-CHECKLIST.md)
