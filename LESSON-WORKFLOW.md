# Lesson Authoring Workflow

**Last Updated:** 2025-01-17
**Philosophy:** Self-directed learning. No calendar assumptions. Respect the hardware and the learner.

This document describes the complete workflow for creating Code Like It's 198x lessons, from writing content to capturing screenshots to publishing.

---

## Overview

Each lesson consists of these components:

1. **Lesson content** (MDX) - `/website/src/pages/commodore-64/phase-N/tier-N/lesson-NNN.mdx`
2. **Runnable code** (BASIC/ASM) - `/code-samples/commodore-64/phase-N/tier-N/lesson-NNN/main.bas`
3. **Screenshots** (PNG) - `/website/public/images/lessons/commodore-64/phase-N/tier-N/lesson-NNN-*.png`
4. **Videos/GIFs** (optional) - `/website/public/media/lessons/commodore-64/phase-N/tier-N/lesson-NNN-*.mp4|.gif`

---

## Content Structure

### **Phase 0: BASIC Foundation** (64 lessons - Game-First Approach)
- **Tier 1:** Lessons 1-16 (Discovery - 6 foundation games)
- **Tier 2:** Lessons 17-32 (Building - 4 technical games, sprites/sound/physics)
- **Tier 3:** Lessons 33-48 (Mastery - 3 professional games: platformer, RPG, puzzle)
- **Tier 4:** Lessons 49-64 (Limits - 3 ceiling demonstrations, explicit BASIC limits)

### **Phases 1-8: Assembly Mastery** (1024 lessons, future)
- Each phase: 128 lessons across 8 tiers
- Progressive difficulty from basics to hardware mastery

**Important:** Tiers are organizational groupings, NOT calendar-based "weeks". Learners progress at their own pace.

---

## Lesson Archetypes

Choose the right archetype for your concept. See [LESSON-ARCHETYPES.md](LESSON-ARCHETYPES.md) for detailed guidance.

### **1. Discovery** (Most Common)
Standard teaching lesson: demonstrate concept, explain how it works, invite experimentation.

**Use for:** New commands, hardware features, programming techniques

### **2. Challenge** (Optional Detours)
Marked with ⚡. Problem to solve using previous concepts. Hints provided, solution at bottom.

**Use for:** Consolidating skills, encouraging problem-solving

### **3. Synthesis** (Every ~8-12 Lessons)
Marked with 🔗. Combines multiple concepts from previous lessons into complete program.

**Use for:** Natural checkpoints, creating something substantial

### **4. Deep Dive** (Optional Advanced)
Marked with 🔬. Hardware-level explanation of WHY things work.

**Use for:** Chip internals, historical context, advanced understanding

### **5. Reference** (Quick Lookup)
Marked with 📚. Tables, syntax guides, memory maps.

**Use for:** Quick reference material that supports other lessons

---

## The Magic Test

Before publishing any lesson, ask these questions:

### **1. Immediacy**
Does something visible or audible happen within 10 seconds of typing RUN?
- Screen changes color
- Sprite appears
- Sound plays
- Text animates
- Something HAPPENS

### **2. Hardware Connection**
Does the learner understand they're controlling real hardware?
- Use chip names (VIC-II, SID, CIA)
- Show memory addresses ($D000, decimal 53248)
- Explain what the hardware is doing
- Make the metal visible

### **3. Experimentation**
Can they change something and immediately see the result?
- Clear parameters to modify
- Obvious cause-and-effect
- Safe to break and fix
- Encourages tinkering

### **4. Clarity**
Is it obvious what this teaches and why it matters?
- Concept is focused (one thing)
- Purpose is clear
- Builds on previous knowledge
- Leads somewhere useful

### **5. Authenticity**
Are you being honest about what this is?
- BASIC is slow (assembly is faster)
- This proves the concept (pros used assembly)
- Hardware constraints are real (not apologized for)
- Historical connections when genuinely relevant (not forced)

**Quality Bar:** If yes to 4+ → Publish. If no to most → Rethink the lesson.

**Important warnings:**
- **Any technique becomes toxic when overused.** Vary your approach.
- **Historical connections:** Valuable when genuine, hollow when forced. Use sparingly.
- **Modern relevance:** Mention occasionally, trust learners to see it themselves.
- **"You're controlling hardware":** True, but don't repeat it every lesson.
- **The concepts speak for themselves.** Trust them.

---

## Step-by-Step Workflow

### **Step 1: Plan the Lesson**

**Choose archetype** - Which teaching pattern fits this concept?

**Check pattern library** - Does a pattern exist for this technique? ([Browse patterns](../website/src/pages/commodore-64/phase-0/patterns/))

**Check prerequisites** - What must learner know already?

**Define the moment** - What's the impressive result they'll create?

**Historical connection** - Which game/demo/programmer used this?

### **Step 2: Write the Lesson MDX**

Create `/website/src/pages/commodore-64/phase-0/tier-1/lesson-001.mdx`:

```markdown
---
layout: ../../../../layouts/LessonLayout.astro
title: "Moving Sprites with Joystick"
game: "Commodore 64 BASIC"
system: "C64"
phase: 0
tier: 2
lessonNumber: 23
totalLessons: 64
prevLesson: "/commodore-64/phase-0/tier-2/lesson-022"
nextLesson: "/commodore-64/phase-0/tier-2/lesson-024"
objectives:
  - Read joystick port at $DC00
  - Update sprite X/Y positions based on input
  - Create real-time interactive control
---

## Controlling Hardware in Real-Time

The joystick port at $DC00 updates 60 times per second. Read it in a loop,
and you're building the same control system that powered *Impossible Mission*.

[Rest of lesson content...]
```

**Frontmatter fields:**
- `layout`: Path to LessonLayout.astro
- `title`: Lesson name (concise, descriptive)
- `game`: Platform name
- `system`: Short code for styling (C64, Spectrum, NES, Amiga)
- `phase`: 0 for BASIC, 1-8 for Assembly
- `tier`: 1-4 for Phase 0 (1-8 for Assembly phases)
- `lessonNumber`: Sequential number (1-64 for Phase 0)
- `totalLessons`: 64 for Phase 0
- `prevLesson`: `/commodore-64/phase-N/tier-N/lesson-NNN` or null
- `nextLesson`: `/commodore-64/phase-N/tier-N/lesson-NNN` or null
- `objectives`: (optional) Array of learning goals

### **Step 3: Structure Your Content**

#### **Discovery Lessons** (Most Common)
```markdown
## Reading Hardware in Real-Time

The joystick port at $DC00 updates constantly. Read it in a loop and you've
got real-time input - the same principle whether you're programming a C64 or
a modern game engine.

## Try This First

[5-10 line simple demonstration]

Type this in and RUN it. Move the joystick.

## The Full Program

[20-40 line impressive result]

![Screenshot](/images/lessons/commodore-64/phase-0/tier-2/lesson-023-main.png)

BASIC reads the port directly - slower than assembly, but it proves the concept.
(Assembly lessons will show full-speed techniques.)

## How It Works

**CIA chip at $DC00:** Each direction clears a bit (0 = pressed)
- Bit 0: Up
- Bit 1: Down
- Bit 2: Left
- Bit 3: Right
- Bit 4: Fire

`PEEK(56320) AND 15` reads the lower 4 bits plus fire.

## Experiment

Try reversing the direction tests. What if you change line 90 to check
different bits?

### From the Vault

- [CIA](/vault/cia) - Complex Interface Adapter hardware details
- [Impossible Mission](/vault/impossible-mission) - Game that pioneered smooth joystick control

### Quick Reference

- **Joystick port 2:** $DC00 (56320)
- **Joystick port 1:** $DC01 (56321)
- **Reading:** `J = PEEK(56320) AND 15`
- **Testing:** `IF (J AND 1)=0 THEN` (up pressed)
```

**"From the Vault" Section:**
- Links to `/vault/*` pages on the website (NOT `/docs` files)
- References hardware, games, programmers, or companies mentioned in the lesson
- Provides deeper historical and technical context
- Only include entries that genuinely relate to the lesson content
- Maximum 2-3 links per lesson (avoid overwhelming learners)

**Tone Guidelines:**

**Do:**
- Name chips precisely (VIC-II, SID, CIA)
- Show memory addresses ($D000, decimal 53248)
- Acknowledge BASIC's speed limitations honestly
- Explain what the hardware is doing
- Let concepts speak for themselves
- Vary your approach between lessons

**Avoid:**
- Using hype language ("amazing!", "mind-blowing!")
- Apologizing for hardware ("only has", "limited")
- Forcing historical connections every lesson
- Claiming BASIC and assembly are equivalent
- Repeating the same phrases lesson after lesson
- Infantilizing ("let's play with...")

### **Step 4: Extract the Code**

Create `/code-samples/commodore-64/phase-0/tier-2/lesson-023/main.bas`:

```basic
10 REM JOYSTICK SPRITE DEMO
20 V=53248:REM VIC-II BASE
30 POKE V+21,1:REM ENABLE SPRITE 0
40 POKE 2040,13:REM SPRITE SHAPE
50 FOR I=0 TO 62:READ D:POKE 832+I,D:NEXT
60 X=160:Y=100
70 POKE V,X:POKE V+1,Y
80 J=PEEK(56320)AND15
90 IF J=14 THEN Y=Y-1
100 IF J=13 THEN Y=Y+1
110 IF J=11 THEN X=X-1
120 IF J=7 THEN X=X+1
130 GOTO 70
140 DATA 0,126,0,1,255,128,3,255,192
150 DATA 7,231,224,15,195,240,31,129,248
160 DATA 63,0,252,126,0,126,252,0,63
```

**Code Requirements:**
- Must run standalone (all DATA, all setup)
- NO indentation (BASIC V2 line numbers flush left)
- Include REM comments for clarity
- Use chip names in comments (VIC-II, SID, not "video chip", "sound chip")

### **Step 5: MANDATORY Pre-Completion Verification**

**⚠️ CRITICAL: Complete ALL these steps BEFORE claiming the lesson is done.**

Do NOT skip ahead to Step 7 (screenshots) or tell the user it's complete until every verification passes.

#### **5a. Validate Syntax with petcat**

For EACH code sample file:

```bash
# Validate syntax (must show no errors)
petcat -text -o /dev/null -- example-1.bas
petcat -text -o /dev/null -- example-2.bas
# etc.
```

**Required:** Must see no error output. Fix any syntax errors before proceeding.

**Common issues:**
- Unmatched quotes
- Invalid keywords (check BASIC V2 compatibility)
- Line numbers out of range
- Malformed DATA statements

#### **5b. Generate PRG Files**

```bash
# Generate loadable PRG files
petcat -w2 -o example-1.prg -- example-1.bas
petcat -w2 -o example-2.prg -- example-2.bas
```

**Required:** PRG files must be created successfully. Check file sizes are reasonable (>0 bytes).

#### **5c. Runtime Test with VICE**

For the MOST COMPLEX example (usually example-2 or the main demo):

```bash
# Test for runtime errors (100M cycles = ~2 minutes execution)
x64sc -autostart example-2.prg -limitcycles 100000000 +sound +confirmonexit
```

**Required:**
- Exit code must be 0 (no errors)
- No ILLEGAL QUANTITY ERROR
- No SYNTAX ERROR
- No OUT OF MEMORY ERROR
- Program runs for full cycle count without crashing

**Check exit code:**
```bash
echo $?  # Must be 0
```

If exit code is non-zero, DO NOT PROCEED. Debug and fix the code.

#### **5d. Verification Checklist**

Only proceed when you can answer YES to ALL:

- [ ] petcat validation passed for all .bas files
- [ ] All .prg files generated successfully
- [ ] Runtime test completed with exit code 0
- [ ] No runtime errors observed in output
- [ ] Code uses lowercase keywords in .bas files
- [ ] Code has NO indentation (line numbers flush left)
- [ ] MDX uses UPPERCASE for REM comments

**If ANY answer is NO:** Fix the issues before proceeding to Step 6.

### **Step 6: Capture Screenshots**

When the impressive moment is visible:

**macOS:**
- `Cmd+Shift+4`, then `Space` captures window
- `Cmd+Shift+4` and drag selects region

**Linux:**
- Use screenshot tool (GNOME Screenshot, Spectacle, etc.)
- Alternative: `scrot -s filename.png`

**Save to:**
```
/website/public/images/lessons/commodore-64/phase-0/tier-2/lesson-023-main.png
```

**Naming conventions:**
- `lesson-NNN-main.png` - The primary impressive moment
- `lesson-NNN-step1.png` - First intermediate step (if multi-step)
- `lesson-NNN-step2.png` - Second intermediate step
- `lesson-NNN-final.png` - Final result (if different from main)
- `lesson-NNN-experiment.png` - Result of suggested experiment

**Image guidelines:**
- PNG format (lossless, supports transparency)
- Capture VICE window directly (not whole desktop)
- Ensure text is readable at web size
- Crop to essential content
- Target file size < 500KB

### **Step 8: Reference Screenshots in MDX**

```markdown
## The Full Program

[Code block here]

![Sprite following joystick movements](/images/lessons/commodore-64/phase-0/tier-2/lesson-023-main.png)

You're reading port $DC00 sixty times per second, the same technique
that powered the smooth controls in *Impossible Mission*.
```

**Screenshot placement:**
- AFTER code block
- BEFORE detailed explanation
- Use descriptive alt text
- Relative path starting with `/images/`

### **Step 9: Update Tier Landing Page** (If New Lesson)

Edit `/website/src/pages/commodore-64/phase-0/tier-2/index.astro`:

```javascript
const lessons = [
  // ... existing lessons ...
  {
    number: 23,
    title: "Joystick-Controlled Sprites",
    description: "Real-time hardware input, the foundation of every C64 game",
    status: "published"  // or "draft", "wip"
  }
];
```

### **Step 10: Extract Vault References**

As you write lessons that reference games, demos, programmers, or hardware, extract those references for The Vault:

Create `/docs/vault-todo.md` (or append to it):

```markdown
## Vault References from Lesson 23

**Games:**
- [ ] **Impossible Mission** - Joystick control system, Dennis Caswell, Epyx 1984
  - Referenced in: Phase 0, Tier 2, Lesson 23
  - Technique: Real-time joystick port reading at $DC00

**Programmers:**
- [ ] **Dennis Caswell** - Creator of Impossible Mission
  - Referenced in: Phase 0, Tier 2, Lesson 23

**Hardware:**
- [x] **VIC-II** - Already in Vault
- [x] **Joystick ports** - Covered in CIA chip entry
```

**Why this matters:**
- The Vault provides historical context for techniques
- Learners can explore the games that pioneered techniques
- Creates interconnected web of retro gaming knowledge
- References can be filled in later as batch task

**Vault entry format** (when you do write them):
```markdown
---
layout: ../../layouts/VaultLayout.astro
title: "Impossible Mission"
subtitle: "Dennis Caswell's espionage platformer"
summary: "Released in 1984, *Impossible Mission* combined smooth animation, digitized speech, and fiendish puzzle-solving."
system_tags: [C64, Atari 8-bit, Apple II]
tech_tags: ["Platformers", "Smooth scrolling", "Digitized speech"]
years: [1984]
---

## Overview
[Game description, what made it special]

## Lesson connections
- Phase 0, Tier 2, Lesson 23: Joystick control system
- Phase 3, Tier 1, Lesson 201: Smooth sprite animation

## See also
- [Dennis Caswell](/vault/dennis-caswell)
- [Epyx](/vault/epyx)
```

### **Step 11: Update Pattern Library References**

If this lesson uses or creates code patterns, update the pattern library metadata:

**If pattern exists** (e.g., `sound/sid-initialization`):
1. Open the pattern MDX file
2. Add this lesson number to `lessonsAppearIn` frontmatter
3. Verify pattern "See Also" section mentions this lesson

**If pattern needs to be created:**
1. Extract the core technique from your lesson's WOW moment
2. Create new pattern file following [Pattern Library Analysis](PATTERN-LIBRARY-ANALYSIS.md)
3. Follow existing pattern structure (Overview → Pattern → Variations → Mistakes → Integration)
4. Cross-reference back to this lesson

**Example update to existing pattern:**
```yaml
---
title: "SID Initialization"
lessonsAppearIn: "Lessons 10, 11, 32, 40, 48"  # Added lesson 10
---
```

**Patterns commonly referenced in Tier 1:**
- `sound/sid-initialization` (L10, L11)
- `input/keyboard-polling` (L12)
- `data/read-data-pattern` (L6)

**Missing patterns to create during Tier 1:**
- `vic-ii/border-background-colors` (L7)
- `screen/direct-writing` (L8)
- `petscii/character-graphics` (L9)
- `random/rnd-generation` (L13)
- `timing/ti-jiffy-clock` (L15)

See [PATTERN-LIBRARY-ANALYSIS.md](PATTERN-LIBRARY-ANALYSIS.md) for complete integration strategy.

### **Step 12: Commit Everything Together**

```bash
git add website/src/pages/commodore-64/phase-0/tier-2/lesson-023.mdx
git add code-samples/commodore-64/phase-0/tier-2/lesson-023/main.bas
git add website/public/images/lessons/commodore-64/phase-0/tier-2/lesson-023-main.png
git add docs/vault-todo.md
git commit -m "feat(commodore64-phase0): Add lesson 23 - Joystick sprite control

- Read hardware port $DC00 for joystick input
- Update sprite positions in real-time loop
- Same technique used in Impossible Mission
- 35-line interactive demo with smooth control
- Extracted Vault references for later

Phase: 0, Tier: 2, Lesson: 23/64"
```

**Commit message format:**
```
<type>(scope): Brief description

- Bullet point: what's taught
- Bullet point: what's created
- Bullet point: historical connection
- Technical details

Phase: N, Tier: N, Lesson: N/total
```

**Types:** `feat`, `fix`, `docs`, `refactor`
**Scopes:** `commodore64-phase0`, `commodore64-phase1`, `spectrum-phase0`, `nes-phase0`, etc.

---

## Quality Checklist

**⚠️ REMINDER: You should have completed Step 5 (MANDATORY Pre-Completion Verification) BEFORE reaching this checklist.**

If you skipped Step 5, GO BACK and complete it now. Do not proceed without running all verification steps.

Before committing:

- [ ] **Magic Test passed:** 3+ of 5 questions answered "yes"
- [ ] **Archetype appropriate:** Right pattern for this concept
- [ ] **Frontmatter complete:** All required fields present
- [ ] **Code validated:** `validate-basic.sh` passes
- [ ] **Code runs:** Tested in VICE without errors
- [ ] **Screenshot captured:** Impressive moment shown
- [ ] **Screenshot referenced:** Properly linked in MDX
- [ ] **Tone correct:** Respects hardware and learner, no hype, no formula
- [ ] **Honesty:** BASIC speed limitations acknowledged where relevant
- [ ] **Experiments invited:** "Try changing X" suggestions included
- [ ] **Vault references extracted:** If historical connections are used, add to vault-todo.md
- [ ] **Pattern library updated:** If pattern exists, `lessonsAppearIn` updated; if new technique, pattern created
- [ ] **British English:** colour, learnt, programme (where appropriate)
- [ ] **No indentation:** BASIC code line numbers flush left
- [ ] **Self-directed friendly:** Works standalone, prerequisites stated

---

## Time Estimates

Per lesson (Phase 0 BASIC):
- **Planning:** 10-15 minutes (including pattern library check)
- **Writing content:** 30-45 minutes
- **Coding program:** 15-30 minutes
- **Testing in VICE:** 5-10 minutes
- **Screenshot capture:** 2-3 minutes
- **Documentation updates:** 5-10 minutes (vault + pattern library)
- **Pattern creation** (if needed): +30-60 minutes
- **Total:** ~1-2 hours per lesson (2-3 hours if creating new pattern)

For 64 Phase 0 lessons: ~64-128 hours of authoring work (spread across weeks/months)
For 5 missing Tier 1 patterns: ~3-5 hours additional (one-time investment)

---

## Helper Scripts Reference

### `validate-basic.sh`
Syntax check all BASIC files using petcat:

```bash
./scripts/validate-basic.sh
```

**Output:**
```
Validating Commodore 64 BASIC lesson files (Phase 0)...
[PASS] code-samples/commodore-64/phase-0/tier-1/lesson-001/main.bas
[PASS] code-samples/commodore-64/phase-0/tier-1/lesson-002/main.bas
...
Summary: 64/64 files passed syntax validation
```

### `quick-vice.sh`
Load lesson in VICE:

```bash
# Using Phase/Tier/Lesson path
./scripts/quick-vice.sh commodore-64/phase-0/tier-2/lesson-023

# Using full file path
./scripts/quick-vice.sh code-samples/commodore-64/phase-0/tier-2/lesson-023/main.bas

# Without warp mode (normal speed)
./scripts/quick-vice.sh commodore-64/phase-0/tier-2/lesson-023 nowarp
```

---

## Platform-Specific Notes

### **C64 BASIC (Phase 0)**
- **Validator:** `petcat -w2 -text`
- **Line format:** No indentation, flush left
- **Line count guideline:** 20-40 lines for main program
- **Memory addresses:** Use both hex ($D000) and decimal (53248)
- **Chip names:** VIC-II (video), SID (sound), CIA (I/O)

### **C64 Assembly (Phases 1-8, Future)**
- **Assembler:** ACME or ca65
- **More complex timing:** Cycle-accurate screenshots critical
- **Multiple screenshots:** Often need sequence showing animation
- **Deeper hardware:** Direct register manipulation, raster tricks

### **Other Platforms (Future)**
Each platform will have:
- Platform-specific validation script
- Emulator-specific launch script
- Platform documentation in `/docs/platforms/[system]/`

---

## Troubleshooting

### **VICE won't load file**
- Check file path is correct (use tab-completion)
- Verify file has `.bas` or `.prg` extension
- Try absolute path instead of relative
- Check file permissions (`chmod 644 file.bas`)

### **Screenshot quality poor**
- Capture VICE window directly, not whole screen
- Use native emulator resolution (no scaling)
- PNG format only (lossless)
- Ensure VICE window has focus when capturing

### **Syntax validation fails**
- Check for unmatched quotes in strings
- Verify all keywords are BASIC V2 compatible
- Line numbers must be 0-63999
- Check DATA statement formatting

### **Program doesn't produce impressive result**
- Review Magic Test questions
- Check if historical connection is clear
- Verify visual/audio feedback is immediate
- Consider if experiment invitation is compelling
- May need different archetype (Challenge? Deep Dive?)

### **Lesson feels formulaic**
- Try different archetype for this concept
- Start with result, explain after (invert structure)
- Add more experimentation opportunities
- Strengthen historical connection
- Consider breaking into smaller focused lessons

---

## See Also

- [LESSON-ARCHETYPES.md](LESSON-ARCHETYPES.md) - Detailed archetype guide
- [PATTERN-LIBRARY-ANALYSIS.md](PATTERN-LIBRARY-ANALYSIS.md) - Pattern library integration strategy **← READ THIS**
- [VAULT-WORKFLOW.md](VAULT-WORKFLOW.md) - Historical reference and timeline guide
- [PHASE-0-CURRICULUM.md](PHASE-0-CURRICULUM.md) - Complete 64-lesson curriculum specification
- [TIER-1-CURRICULUM-REVIEW.md](TIER-1-CURRICULUM-REVIEW.md) - Existing lessons vs. new curriculum analysis
- [Pattern Library](../website/src/pages/commodore-64/phase-0/patterns/) - 33 reusable C64 BASIC patterns (browse online)
- [PROJECT_OVERVIEW.md](../PROJECT_OVERVIEW.md) - Curriculum structure and philosophy
- [CLAUDE.md](../CLAUDE.md) - Project coding standards
- [README.md](../README.md) - Project philosophy
- [archive/vice-harness-experiment/README.md](../lesson-pipeline/archive/vice-harness-experiment/README.md) - Why we don't automate screenshots

---

**Remember:** You're teaching learners to stand on the shoulders of giants by touching the same metal the legends touched. Respect the hardware. Respect the learner. Show the lineage. Let the magic emerge naturally from the act of creation.
