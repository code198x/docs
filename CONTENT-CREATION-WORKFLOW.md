# Content Creation Workflow

**Last Updated:** 2025-11-15
**Purpose:** Complete end-to-end guide for creating curriculum lessons, from initial planning through publication
**Scope:** Universal workflow applying to all platforms and phases

---

## Overview and Philosophy

**Purpose:** Complete end-to-end guide for creating curriculum lessons, from initial planning through publication.

**Scope:** Universal workflow applying to all platforms and phases, with platform-specific and phase-specific sections where needed.

**Core Principles:**
- **Curriculum alignment is mandatory** - No work begins without verified alignment to specifications
- **Quality over speed** - Three core criteria must be met
- **Platform skills handle execution** - This workflow defines process, platform skills execute technical details
- **Integration by design** - Vault, Pattern Library, and cross-references built in, not bolted on

**Lesson Archetypes (Design Tools, Not Labels):**

Lessons fall into natural patterns. Content communicates purpose; no visual markers needed.

- **Discovery** - Standard teaching lesson (most common)
- **Challenge** - Problem-solving exercise using recent skills
- **Synthesis** - Combining multiple concepts into complete program
- **Deep Dive** - Hardware internals and "why it works"
- **Tutorial** - Step-by-step guided construction
- **Showcase** - Demonstrates what's possible (inspirational, before teaching)

**Three Core Quality Criteria:**

1. **It Works Fast** - Immediate visible/audible feedback, creates something impressive
2. **It's Real** - Hardware connection visible, honest about limitations
3. **It's Clear** - Focused concept, builds logically, invites experimentation

---

## Workflow Phases

The workflow has **five main phases**, each with detailed steps:

### Phase 1: Planning (Pre-Work)
**Purpose:** Verify curriculum alignment and make key decisions before writing begins.

**Steps:**
- Locate and read lesson specification (LESSON-SPECIFICATION.md, PHASE-N-SPECIFICATION.md, platform curriculum)
- Verify current lesson matches specification (if editing existing)
- Choose lesson archetype based on concept
- Identify prerequisites from previous lessons
- Check for existing Pattern Library entries
- Identify required Vault entries (hardware chips, essential context)

**Hard Stop:** If lesson doesn't match curriculum specification, STOP. Follow decision matrix (archive mismatch, don't edit).

### Phase 2: Creation
**Purpose:** Write lesson content and working code.

**Steps:**
- Write lesson MDX following structure
- Create runnable code examples
- Write clear explanations
- Include experimentation suggestions
- Tag potential patterns as you write (lightweight tracking)

### Phase 3: Validation
**Purpose:** Ensure code works and lesson meets quality criteria.

**Steps:**
- Platform-specific code validation (delegate to platform skill)
- Runtime testing (no crashes, correct output)
- Apply three quality criteria
- Screenshot/media capture and verification
- British English check

### Phase 4: Integration
**Purpose:** Connect lesson to broader curriculum ecosystem.

**Steps:**
- Create required Vault entries (hardware, essential context)
- Track nice-to-have Vault entries for later
- Update pattern tags/notes
- Cross-reference related lessons
- Update navigation

### Phase 5: Publication
**Purpose:** Commit and make lesson available.

**Steps:**
- Final verification checklist
- Commit with proper message format
- Update tier landing page
- Mark lesson as published

---

## Phase 1: Planning (Detailed)

### Step 1.1: Curriculum Alignment Verification (MANDATORY)

**Before creating or editing ANY lesson:**

1. **Locate specification** (check in order):
   - Individual lesson spec: `docs/{platform}/phase-{N}/tier-{N}/lesson-{NNN}.md`
   - Tier overview: `docs/{platform}/phase-{N}/tier-{N}/README.md`
   - Phase curriculum: `docs/{platform}/PHASE-{N}-CURRICULUM.md`
   - Platform overview: `docs/{platform}/overview.md`

2. **Read specification completely** - Note title, objectives, key concepts, prerequisites

3. **If editing existing lesson, compare:**
   - Does current title match spec? ✅/❌
   - Do learning objectives match? ✅/❌
   - Do key concepts match? ✅/❌

**Decision Matrix:**

- **All ❌ (Complete Mismatch):** Archive current lesson (`lesson-NNN-OLD.mdx.bak`), create new lesson from spec
- **Mixed ✅❌ (Partial Match):** Archive current, extract reusable elements, create new lesson
- **All ✅ (Strong Match):** Proceed with editing, document minor differences in commit

**Hard Stop:** If specification doesn't exist at ANY level, STOP. Cannot create lesson without specification.

### Step 1.2: Archetype Selection

Choose archetype based on what you're teaching:
- New concept/technique → **Discovery**
- Consolidating recent skills (problem) → **Challenge**
- Consolidating recent skills (building something) → **Synthesis**
- Hardware internals explanation → **Deep Dive**
- Step-by-step guided construction → **Tutorial**
- Inspirational demonstration → **Showcase**

### Step 1.3: Prerequisites and Context

- List concepts from previous lessons this builds on
- Identify BASIC/Assembly knowledge required
- Check Pattern Library for existing patterns covering this technique
- Note which hardware chips will be discussed

### Step 1.4: Required Vault Entries Check

Identify **must-create** Vault entries:
- Hardware chips mentioned (VIC-II, SID, CIA, etc.)
- Core platform components (memory maps, character sets)
- Essential context the lesson depends on

Track **nice-to-have** for later:
- Games referenced
- Programmers/designers mentioned
- Companies/publishers

---

## Phase 2: Creation (Detailed)

### Step 2.1: Lesson Structure

**File Location:** `/website/src/pages/{platform}/phase-{N}/tier-{N}/lesson-{NNN}.mdx`

**Frontmatter (YAML):**
```yaml
---
layout: ../../../../layouts/LessonLayout.astro
title: "[Clear, Descriptive Title]"
game: "Commodore 64 BASIC" # or platform language
system: "C64" # platform code
phase: 0
tier: 1
lessonNumber: 1
totalLessons: 64
prevLesson: "/{platform}/phase-{N}/tier-{N}/lesson-{NNN}" # or null
nextLesson: "/{platform}/phase-{N}/tier-{N}/lesson-{NNN}" # or null
objectives:
  - 'First learning objective'
  - 'Second learning objective'
  - 'Third learning objective'
---
```

**Content Sections (adapt as needed for archetype):**

1. **Opening** - Context and motivation (2-4 sentences)
2. **Key Concepts** - Bullet points of what's covered
3. **Example Program** - Simple demonstration with explanation
4. **Experiment Section** - Variations to try, more complex example
5. **How It Works** - Technical explanation, hardware details
6. **Game Integration** - Practical applications
7. **From the Vault** - Links to Vault entries (if relevant)
8. **Quick Reference** - Tables, addresses, syntax for this lesson
9. **What You've Learnt** - Summary and next lesson preview

**Important:** Structure is flexible. Adapt sections to lesson archetype and content.

### Step 2.2: Code Examples

**Location:** `/code-samples/{platform}/phase-{N}/tier-{N}/lesson-{NNN}/example-N.{ext}`

**Requirements:**
- Must run standalone (all DATA, all setup)
- **Phase 0:** NO indentation (BASIC line numbers flush left)
- **Phase 1+:** Follow platform assembly conventions
- Use chip names in comments (VIC-II, SID, not "video chip")
- Include clear comments explaining key concepts
- Progressive complexity (simple example → complex example)

### Step 2.3: Pattern Tagging (Lightweight)

As you write, note reusable techniques:
- Add comment in code: `REM PATTERN: SID initialization sequence`
- Or note in lesson planning doc: "Pattern candidate: sprite MSB handling"

Don't create Pattern Library entries yet - just tag for later extraction.

### Step 2.4: Writing Guidelines

**Tone:**
- Conversational but precise
- British English (colour, learnt, programme for non-code)
- Use "program" for computer programs
- Name hardware designers/engineers when relevant
- Let concepts speak for themselves - no hype

**Avoid:**
- Excessive exclamation marks
- Forced historical connections every lesson
- Claiming BASIC and Assembly are equivalent speed
- Apologizing for hardware limitations
- Formulaic openings

---

## Phase 3: Validation (Detailed)

### Step 3.1: Code Validation (MANDATORY)

**Delegate to platform-specific skill** - Each platform has validation requirements:

**Phase 0 (BASIC) - Example C64:**
```bash
# Syntax validation
petcat -text -o /dev/null -- example-1.bas

# Generate executable
petcat -w2 -o example-1.prg -- example-1.bas

# Runtime test (no crashes, no errors)
x64sc -autostart example-1.prg -limitcycles 100000000 +sound +confirmonexit
echo $? # Must be 0
```

**Phase 1+ (Assembly):**
- Platform-specific assembler (ACME, ca65, vasm, sjasmplus)
- Semantic validation if available
- Runtime testing in emulator

**See platform skill for complete validation process** (commodore-64-basic-lesson-creation, zx-spectrum-assembly-lesson-creation, etc.)

**Required:** All validation must pass before proceeding. Fix errors immediately.

### Step 3.2: Apply Three Quality Criteria

Ask these questions:

**1. Does It Work Fast?**
- Something visible/audible within 10 seconds? ✅/❌
- Creates something impressive or useful? ✅/❌

**2. Is It Real?**
- Hardware connection visible (chip names, addresses)? ✅/❌
- Honest about limitations (BASIC speed, constraints)? ✅/❌

**3. Is It Clear?**
- Concept is focused (one main thing)? ✅/❌
- Builds on previous lessons logically? ✅/❌
- Invites experimentation (clear parameters to modify)? ✅/❌

**Quality Bar:** At least 2/3 criteria strongly met. If not, revise lesson.

### Step 3.3: Screenshot and Audio Capture

**When to capture:**
- After code validation passes
- When impressive moment is visible/audible
- For each major example in lesson

**Screenshot Capture:**
- Platform-specific (see platform skill for emulator instructions)
- PNG format (lossless)
- Descriptive filenames: `lesson-NNN-main.png`, `lesson-NNN-step1.png`
- Location: `/website/public/images/lessons/{platform}/phase-{N}/tier-{N}/lesson-{NNN}/`

**Audio Capture (for sound/music lessons):**
- Capture audio output from emulator
- WAV or OGG format (lossless or high-quality)
- Descriptive filenames: `lesson-NNN-sound.wav`, `lesson-NNN-music.ogg`
- Location: `/website/public/media/lessons/{platform}/phase-{N}/tier-{N}/lesson-{NNN}/`

**Platform Considerations:**
- **PAL vs NTSC timing differences** - SID frequencies differ between PAL (50Hz) and NTSC (60Hz)
- Specify which timing used in lesson
- Note differences in lesson if relevant: "PAL C64 used for audio examples; NTSC timing will be slightly higher pitch"

**Screenshot Verification (CRITICAL):**

Use Read tool to VIEW every screenshot after capture:
1. **Describe visible elements** - sprites, text, colors, game state
2. **Check for error messages** - `?SYNTAX ERROR`, `?ILLEGAL QUANTITY ERROR`, etc. = automatic failure
3. **Check for blank screens** - indicates crash or initialization bug
4. **Verify expected output matches actual screenshot**

**Audio Verification (for sound lessons):**

Listen to captured audio and verify:
1. **Correct frequency** - Use frequency analyzer if needed for precise tones
2. **No distortion or clipping** - Check waveform for clean signal
3. **Expected sound** - Triangle wave sounds like triangle, not noise
4. **Timing correct** - Note duration, rhythm matches code
5. **PAL/NTSC noted** - Document which system timing was used

If errors found: Fix code → Revalidate → Recapture → Re-verify (repeat until clean)

**No claiming "verified ✅" without Read tool evidence (screenshots) and listening verification (audio).**

### Step 3.4: British English Check

Run grep pattern to find American spellings:
```bash
grep -n "color\|flavor\|center\|learned" lesson-NNN.mdx
```

**Exceptions:** The word "program" for computer programs (not "programme")

---

## Phase 4: Integration (Detailed)

### Step 4.1: Vault Entry Creation

**Required entries (create before lesson completion):**

Create Vault entries for:
- Hardware chips discussed (VIC-II, SID, CIA, etc.)
- Core platform components (memory maps, character sets, PETSCII)
- Essential context the lesson depends on

**Vault entry location:** `/website/src/pages/vault/{category}/{entry-name}.mdx`

**Vault Categories (14 total):**
- `hardware` - Chips, components (VIC-II, SID, CIA, etc.)
- `games` - Game titles
- `people` - Programmers, designers, musicians, artists
- `companies` - Publishers, developers
- `platforms` - Platform overviews
- `techniques` - Programming techniques
- `events` - Historical milestones
- `culture` - Demoscene, magazines, communities
- `publications` - Magazines, books, manuals
- `tools` - Development tools, utilities
- `peripherals` - Hardware add-ons
- `formats` - File formats (SID, PRG, TAP, etc.)
- `concepts` - Programming concepts
- `terminology` - Glossary entries

**Basic Vault entry structure:**
```yaml
---
layout: ../../../layouts/VaultLayout.astro
title: "[Component Name]"
subtitle: "[Brief description]"
summary: "[One-sentence overview]"
system_tags: [C64, Spectrum, ...]
tech_tags: ["Hardware", "Graphics", ...]
years: [1982]
---

## Overview
[What it is, what it does]

## Technical Details
[Registers, addresses, capabilities]

## Lesson Connections
- Phase 0, Tier 1, Lesson 7: Border colors
- Phase 0, Tier 2, Lesson 18: Sprite positioning

## See Also
- [Related Vault Entry](/vault/{category}/related)
```

**Nice-to-have entries (track for later):**

Add to `/docs/vault-todo.md`:
```markdown
## From Lesson NNN

**Games:**
- [ ] **Game Name** - Description, Developer, Publisher Year
  - Referenced in: Phase N, Tier N, Lesson NNN
  - Technique: What technique was mentioned

**People:**
- [ ] **Person Name** - Role, notable work
  - Referenced in: Phase N, Tier N, Lesson NNN
```

### Step 4.2: Pattern Library Tagging

**During lesson creation, you tagged potential patterns.**

Now formalize the tracking:

Add to lesson frontmatter or planning doc:
```yaml
patternCandidates:
  - "SID initialization sequence"
  - "Sprite MSB handling for X > 255"
  - "Joystick port polling loop"
```

**Pattern extraction happens after tier completion** (see Step 4.3)

### Step 4.3: Post-Tier Pattern Extraction (After Tier Complete)

**When you've completed all lessons in a tier:**

1. **Review all pattern tags** from the tier's lessons
2. **Identify recurring techniques** that appear in multiple lessons
3. **Create Pattern Library entries systematically**
4. **Backfill cross-references** to lessons using each pattern

**Pattern entry location:** `/website/src/pages/{platform}/patterns/{category}/{pattern-name}.mdx`

**Combined approach:**
- Tag patterns during creation (lightweight, don't block)
- Systematic extraction after tier (comprehensive coverage)

### Step 4.4: Cross-References

**Update lesson with Vault links:**
```markdown
### From the Vault

- [VIC-II Chip](/vault/hardware/vic-ii) - Graphics chip register reference
- [Sprite System](/vault/hardware/sprites) - Hardware sprite capabilities
- [Impossible Mission](/vault/games/impossible-mission) - Pioneering platformer
```

**Update navigation if new lesson:**

Edit `/website/src/pages/{platform}/phase-{N}/tier-{N}/index.astro`:
```javascript
const lessons = [
  // ... existing lessons ...
  {
    number: NNN,
    title: "Lesson Title",
    description: "Brief description for tier overview",
    status: "published"
  }
];
```

---

## Phase 5: Publication (Detailed)

### Step 5.1: Final Verification Checklist

Before committing, verify ALL of these:

**Code:**
- [ ] All code examples validated (syntax + runtime)
- [ ] No crashes, no error messages in output
- [ ] PRG/executable files generated successfully
- [ ] Code follows platform conventions (no indentation for BASIC, etc.)

**Quality:**
- [ ] Three quality criteria met (It Works Fast, It's Real, It's Clear)
- [ ] Screenshots captured and verified with Read tool
- [ ] Audio captured and verified (for sound lessons)
- [ ] No error messages or blank screens in screenshots
- [ ] British English throughout (except "program" for code)

**Curriculum:**
- [ ] Matches lesson specification exactly
- [ ] Prerequisites clearly stated
- [ ] Builds logically on previous lessons
- [ ] Objectives in frontmatter match content

**Integration:**
- [ ] Required Vault entries created (hardware, essential context)
- [ ] Nice-to-have Vault entries tracked in vault-todo.md
- [ ] Pattern candidates tagged for later extraction
- [ ] Vault links included in "From the Vault" section
- [ ] Navigation updated (tier landing page)

### Step 5.2: Commit Workflow

**Stage all related files:**
```bash
git add website/src/pages/{platform}/phase-{N}/tier-{N}/lesson-{NNN}.mdx
git add code-samples/{platform}/phase-{N}/tier-{N}/lesson-{NNN}/*.{bas,prg,asm,bin}
git add website/public/images/lessons/{platform}/phase-{N}/tier-{N}/lesson-{NNN}/*.png
git add website/public/media/lessons/{platform}/phase-{N}/tier-{N}/lesson-{NNN}/*.{wav,ogg}
git add website/src/pages/vault/{category}/*.mdx  # if created Vault entries
git add docs/vault-todo.md  # if tracked nice-to-have entries
git add website/src/pages/{platform}/phase-{N}/tier-{N}/index.astro  # if updated navigation
```

**Commit message format:**
```
<type>(<scope>): <brief description>

- Learning objective 1
- Learning objective 2
- Key concept introduced
- Hardware chips covered
- Historical connection (if relevant)

Phase: N, Tier: N, Lesson: NNN/total

Vault entries created: [list if any]
Pattern candidates tagged: [list if any]
```

**Types:**
- `feat` - New lesson
- `fix` - Bug fix in existing lesson
- `docs` - Documentation updates
- `refactor` - Restructure without changing content

**Scopes:** `{platform}-phase{N}` (e.g., `c64-phase0`, `spectrum-phase0`, `nes-phase1`)

**Example:**
```
feat(c64-phase0): Add lesson 018 - Player-controlled sprites

- Read joystick port at $DC00 for hardware input
- Update sprite X/Y positions based on directional input
- Create real-time interactive control loop
- VIC-II sprite positioning, CIA joystick port

Phase: 0, Tier: 2, Lesson: 18/64

Vault entries created: hardware/cia (joystick registers)
Pattern candidates tagged: joystick-polling-loop
```

### Step 5.3: Mark as Published

Update lesson status in tier landing page (if not already done in Step 4.4):

```javascript
{
  number: NNN,
  title: "Lesson Title",
  description: "Brief description",
  status: "published"  // was "draft" or "wip"
}
```

### Step 5.4: Push to Repository

```bash
git push origin <branch-name>
```

**Note:** Follow project git workflow for branching/merging (see CLAUDE.md or project README)

### Step 5.5: Update Landing Pages

**Update as appropriate based on milestone:**

**Tier Landing Page (every lesson):**
- Location: `/website/src/pages/{platform}/phase-{N}/tier-{N}/index.astro`
- Update lesson list with new/updated lesson
- Mark status as "published"

**Phase Landing Page (when completing tier):**
- Location: `/website/src/pages/{platform}/phase-{N}/index.astro`
- Update tier completion status
- Update lesson count
- Add tier summary/accomplishments if tier complete

**Platform Landing Page (when completing phase):**
- Location: `/website/src/pages/{platform}/index.astro`
- Update phase completion status
- Update total lesson count for platform
- Highlight recent completions

**Homepage (major milestones):**
- Location: `/website/src/pages/index.astro`
- Update when:
  - Platform Phase 0 complete (first playable curriculum)
  - Platform fully complete (all phases)
  - New platform launched
  - Major milestone (100 lessons, 1000 lessons, etc.)

**What constitutes "appropriate":**
- Single lesson → Tier landing only
- Tier complete → Tier + Phase landing
- Phase complete → Tier + Phase + Platform landing
- Major milestone → All levels including Homepage

---

## Platform-Specific Details

**Universal workflow applies to all platforms, with platform-specific validation:**

### Commodore 64
- **Phase 0:** See `commodore-64-basic-lesson-creation` skill
- **Phase 1+:** See `commodore-64-assembly-lesson-creation` skill

### ZX Spectrum
- **Phase 0:** See `zx-spectrum-basic-lesson-creation` skill
- **Phase 1+:** See `zx-spectrum-assembly-lesson-creation` skill

### Amiga
- **Phase 0:** See `amiga-amos-lesson-creation` skill
- **Phase 1+:** See `amiga-assembly-lesson-creation` skill

### NES/Famicom
- **No Phase 0** (no BASIC available)
- **Phase 1+:** See `nes-assembly-lesson-creation` skill

**Each skill provides:**
- Platform-specific validation commands
- Emulator configuration
- Common pitfalls for that platform
- Screenshot capture workflow
- Audio capture workflow (for platforms with sound chips)
- File structure requirements

**Platform Skills Naming Convention:**
- `{platform}-basic-lesson-creation` (Phase 0)
- `{platform}-amos-lesson-creation` (Amiga Phase 0 - AMOS BASIC)
- `{platform}-assembly-lesson-creation` (Phase 1+)

---

## Phase-Specific Considerations

### Phase 0 (BASIC) - Gateway Language

**Focus:**
- Game-first approach for novices/children
- Proving concepts before assembly
- Honest about speed limitations
- Foundation for assembly understanding

**Key Requirements:**
- NO indentation (line numbers flush left on most platforms)
- British English (colour, learnt) BUT "program" for code
- Acknowledge BASIC is slower, assembly is faster
- Show hardware addresses and chip names
- Create impressive results within BASIC constraints
- **C64 BASIC variable names:** Only first TWO characters are significant
  - `f1x` and `f1y` are BOTH read as `f1` (collision!)
  - Use distinct first-two-char names: `fx`/`fy`, `gx`/`gy`, `px`/`py`
  - Good: `fx`, `fy`, `gx`, `gy`, `px`, `py`, `sc`, `hp`
  - Bad: `f1x`, `f1y` (both become `f1`), `score1`, `score2` (both become `sc`)

**Typical Lesson Structure:**
- Simple example (5-15 lines)
- More complex example (20-40 lines)
- Experimentation suggestions
- "Assembly lessons will show full-speed techniques" where relevant

### Phase 1+ (Assembly) - Hardware Mastery

**Focus:**
- Professional-level techniques
- Direct hardware control
- Cycle-accurate timing
- Real-time game development

**Key Requirements:**
- Cycle counting for timing-critical sections
- Register usage documentation
- Memory-efficient techniques
- Comment WHY, not WHAT

**Typical Lesson Structure:**
- Concept explanation with hardware details
- Assembly implementation
- Optimization discussion
- Complete working example with cycle counts

**Differences in Validation:**
- **Phase 0:** Syntax validation + runtime test
- **Phase 1+:** Assembly + linking + runtime test + timing verification

**Differences in Quality Criteria:**
- **Phase 0:** "It Works Fast" = within 10 seconds (BASIC speed)
- **Phase 1+:** "It Works Fast" = instant/real-time (assembly speed)

---

## Emergency Procedures

**What to do when things go wrong:**

### Emergency 1: Edited Wrong Lesson (Doesn't Match Curriculum)

**You accidentally edited a lesson that doesn't match the specification.**

**If uncommitted:**
```bash
git status  # Check what changed
git restore lesson-NNN.mdx  # Discard changes
```

**If committed but not pushed:**
```bash
git log -1  # Verify it's your commit
git revert HEAD  # Create revert commit
# OR
git reset --soft HEAD^  # Undo commit, keep changes in staging
```

**If pushed:**
1. Create new commit that fixes the issue
2. Follow proper alignment procedure from Phase 1
3. Document in commit message: "fix: Align lesson-NNN with curriculum specification"

**Then:** Return to Phase 1, Step 1.1 (Curriculum Alignment Verification)

### Emergency 2: Discovered Curriculum Drift Mid-Session

**You realize partway through that lesson doesn't match curriculum.**

**Steps:**
1. **STOP immediately**
2. Document changes: `git diff lesson-NNN.mdx > /tmp/changes.diff`
3. Revert changes: `git restore lesson-NNN.mdx`
4. Review diff: Check `/tmp/changes.diff` for universally useful edits (typo fixes, clarity improvements)
5. Follow proper alignment procedure from Phase 1
6. Apply salvaged edits ONLY if they support curriculum-aligned version

### Emergency 3: Code Validation Fails After Writing Lesson

**Validation errors after lesson is written.**

**Steps:**
1. Read error messages carefully
2. Fix code issues
3. Re-run validation
4. Regenerate executables (PRG/binary files)
5. Re-test runtime
6. If screenshots were captured, recapture after fixes
7. **Do NOT proceed to publication until validation passes**

**Common fixes:**
- Syntax errors → Check BASIC/assembly syntax reference
- Runtime errors → Check memory addresses, value ranges
- Reserved variables → Rename (e.g., ST → GS, TI → CT)
- Missing line numbers → Add target for GOSUB/GOTO

### Emergency 4: Screenshot Shows Errors or Blank Screen

**Screenshot verification revealed problems.**

**Steps:**
1. Identify error type:
   - Syntax error → Code has bugs, validation missed it
   - Runtime error → POKE out of range, illegal quantity
   - Blank screen → Initialization bug or crash
2. Fix code
3. Re-validate completely (syntax + runtime)
4. Recapture screenshot
5. Re-verify with Read tool
6. Repeat until clean

**Do NOT:**
- Publish lesson with error screenshots
- Assume error is "minor" and will be fixed later
- Skip re-verification after fixes

### Emergency 5: Committed Wrong Files or Broken Navigation

**Navigation broken, wrong files committed, etc.**

**Steps:**
```bash
git status  # See what's staged/committed
git log -3  # See recent commits

# If uncommitted:
git restore <file>  # Discard wrong changes
git add <correct-file>  # Stage correct files

# If committed but not pushed:
git reset --soft HEAD^  # Undo commit, keep changes
# Fix issues, re-stage correctly, commit again

# If pushed:
# Create fix commit with proper changes
```

### Emergency 6: Lost Work Due to Crash/Error

**Work lost, need to recover.**

**Prevention:**
- Commit frequently during creation
- Use git branches for experimentation
- Keep code samples in separate files (auto-saved by editor)

**Recovery:**
```bash
git reflog  # See all recent git actions
git checkout <commit-hash>  # Recover lost commits
git stash list  # Check for stashed changes
```

---

## Common Pitfalls and Troubleshooting

### Pitfall 1: Formulaic Writing

**Problem:** Every lesson starts the same way: "You're controlling the same hardware as..." or "This is the technique that powered..."

**Solution:**
- Vary your openings completely
- Let concepts speak for themselves
- Historical connections only when genuinely illuminating
- Trust the hardware to be compelling

### Pitfall 2: Skipping Curriculum Alignment

**Problem:** "I know what this lesson should teach" → write lesson → doesn't match specification

**Solution:**
- **ALWAYS** read specification first (Phase 1, Step 1.1)
- Hard stop on mismatches
- Specifications exist for a reason

### Pitfall 3: Claiming Validation Passed Without Evidence

**Problem:** "Code validated ✅" but no screenshot verification, no Read tool check

**Solution:**
- **MUST** run validation commands
- **MUST** verify screenshots with Read tool
- **MUST** listen to audio for sound lessons
- **MUST** check exit codes
- Evidence before assertions, always

### Pitfall 4: Indentation in BASIC Code

**Problem:** Adding indentation for readability in .bas files breaks BASIC V2 compatibility

**Solution:**
- Line numbers flush left, always (Phase 0)
- No exceptions
- Validation will catch this (petcat will fail)

### Pitfall 5: Reserved Variables in C64 BASIC

**Problem:** Using ST, TI, TI$ causes crashes or unexpected behavior

**Solution:**
- Use GS (game state), CT (custom timer), SC (score), HP (health)
- Never use ST, TI, TI$ as variables
- Check with grep: `grep -iE '\<(st|ti|ti\$)\>' *.bas`

### Pitfall 6: Sprite MSB Not Handled

**Problem:** Sprite X > 255 wraps to left side of screen

**Solution:**
- Always handle $D010 (53264) MSB register
- Introduce in first sprite positioning lesson
- All subsequent sprite lessons must handle correctly

### Pitfall 7: Pattern Library Forgotten

**Problem:** Finish tier without extracting patterns, lose track of reusable techniques

**Solution:**
- Tag patterns during creation (lightweight)
- Systematic extraction after tier completion
- Combined approach ensures comprehensive coverage

### Pitfall 8: Nice-to-Have Vault Entries Block Progress

**Problem:** Trying to write complete game/programmer bios before completing lesson

**Solution:**
- Required entries (hardware) before completion
- Nice-to-have entries (games, people) tracked for later
- vault-todo.md is your friend

### Pitfall 9: Quality Criteria Ignored

**Problem:** Lesson published without checking "It Works Fast, It's Real, It's Clear"

**Solution:**
- Apply three criteria in Phase 3 (Validation)
- At least 2/3 must be strongly met
- If not, revise lesson before publication

### Pitfall 10: Screenshot Timing Issues

**Problem:** Screenshot captured too early (loading screen) or too late (after program ends)

**Solution:**
- Capture when impressive moment is visible
- Use emulator cycle limits or pause functionality
- Verify with Read tool that screenshot shows expected output

### Pitfall 11: Audio Frequency Errors

**Problem:** SID/AY/sound chip frequencies incorrect, sounds wrong

**Solution:**
- Verify frequency calculations in code
- Use frequency analyzer for precise tones
- Note PAL vs NTSC differences
- Listen to captured audio, don't assume it's correct

---

## Time Estimates

**Per lesson estimates (varies by complexity and archetype):**

### Phase 0 (BASIC)

**Discovery Lesson (Standard):**
- Planning and curriculum alignment: 10-15 minutes
- Writing content: 30-45 minutes
- Coding examples: 15-30 minutes
- Validation and testing: 10-15 minutes
- Screenshot/audio capture and verification: 5-10 minutes
- Integration (Vault/patterns): 10-15 minutes
- **Total: 1.5-2.5 hours**

**Synthesis Lesson (More Complex):**
- Planning: 15-20 minutes
- Writing: 45-60 minutes
- Coding: 30-45 minutes
- Validation: 15-20 minutes
- Screenshots/audio: 10-15 minutes
- Integration: 15-20 minutes
- **Total: 2-3 hours**

**Challenge Lesson:**
- Planning: 10-15 minutes
- Writing (with hints): 30-45 minutes
- Coding (problem + solution): 20-30 minutes
- Validation: 10-15 minutes
- Screenshots: 5-10 minutes
- Integration: 10-15 minutes
- **Total: 1.5-2.5 hours**

### Phase 1+ (Assembly)

**Discovery Lesson:**
- Planning: 15-20 minutes
- Writing: 45-60 minutes
- Coding (with cycle counting): 45-60 minutes
- Validation: 15-20 minutes
- Screenshots/audio: 10-15 minutes
- Integration: 15-20 minutes
- **Total: 2.5-3.5 hours**

**Synthesis Lesson (Assembly):**
- Planning: 20-30 minutes
- Writing: 60-90 minutes
- Coding: 60-90 minutes
- Validation: 20-30 minutes
- Screenshots/audio: 15-20 minutes
- Integration: 20-30 minutes
- **Total: 3.5-5 hours**

### Additional Time Investments

**Required Vault Entries (First Time):**
- Hardware chip entry: 30-45 minutes
- Platform component entry: 20-30 minutes

**Nice-to-Have Vault Entries (Batch Creation):**
- Game entry: 15-20 minutes
- Person entry: 10-15 minutes
- Company entry: 10-15 minutes

**Pattern Library Extraction (After Tier):**
- Review tier for patterns: 30-45 minutes
- Create pattern entry: 20-30 minutes per pattern
- Backfill cross-references: 15-20 minutes
- **Total: 2-4 hours per tier** (depending on patterns identified)

### Tier Completion Estimates

**Phase 0 Tier (16 lessons):**
- Lessons: 24-40 hours
- Pattern extraction: 2-4 hours
- Vault entries: 3-6 hours (if creating new hardware entries)
- **Total: 29-50 hours per tier**

**Phase 1+ Tier (16 lessons):**
- Lessons: 40-56 hours
- Pattern extraction: 3-5 hours
- Vault entries: 2-4 hours
- **Total: 45-65 hours per tier**

**Note:** Times decrease with experience and when reusing established patterns/Vault entries.

---

## Quick Reference Summary

### The Five Phases

1. **Planning** - Verify curriculum alignment, choose archetype, identify prerequisites
2. **Creation** - Write content and code, tag patterns
3. **Validation** - Code validation, quality criteria, screenshot/audio verification
4. **Integration** - Vault entries, pattern tagging, cross-references
5. **Publication** - Final checks, commit, update navigation

### Hard Stops (Must Complete Before Proceeding)

- ❌ No curriculum specification → STOP, cannot create lesson
- ❌ Lesson doesn't match specification → STOP, archive and rewrite
- ❌ Code validation fails → STOP, fix before proceeding
- ❌ Screenshot shows errors → STOP, fix and recapture
- ❌ Audio sounds wrong → STOP, fix and recapture
- ❌ Quality criteria not met → STOP, revise lesson

### Three Quality Criteria

1. **It Works Fast** - Immediate feedback, impressive result
2. **It's Real** - Hardware visible, honest limitations
3. **It's Clear** - Focused concept, logical progression, invites experimentation

**Quality Bar:** At least 2/3 strongly met

### Six Lesson Archetypes

- **Discovery** - Standard teaching (most common)
- **Challenge** - Problem-solving exercise
- **Synthesis** - Combining concepts
- **Deep Dive** - Hardware internals
- **Tutorial** - Step-by-step construction
- **Showcase** - Inspirational demonstration

### Required Before Completion

- [ ] Curriculum alignment verified
- [ ] Code validated (syntax + runtime)
- [ ] Screenshots verified with Read tool
- [ ] Audio verified (for sound lessons)
- [ ] Quality criteria met (2/3+)
- [ ] Required Vault entries created (hardware)
- [ ] Pattern candidates tagged
- [ ] British English checked
- [ ] Navigation updated

### Vault Categories (14 total)

hardware, games, people, companies, platforms, techniques, events, culture, publications, tools, peripherals, formats, concepts, terminology

### Platform Skills Naming

- `{platform}-basic-lesson-creation` (Phase 0)
- `{platform}-amos-lesson-creation` (Amiga Phase 0)
- `{platform}-assembly-lesson-creation` (Phase 1+)

Examples: `commodore-64-basic-lesson-creation`, `zx-spectrum-assembly-lesson-creation`

### Commit Message Format

```
<type>(<scope>): <brief description>

- Learning objective 1
- Learning objective 2

Phase: N, Tier: N, Lesson: NNN/total
```

Types: `feat`, `fix`, `docs`, `refactor`
Scopes: `{platform}-phase{N}`

---

## End of Content Creation Workflow

**Remember:** Quality over speed. Curriculum alignment is mandatory. Evidence before assertions, always.
