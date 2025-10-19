---
name: C64 Lesson Creation
description: Complete workflow for creating curriculum-aligned C64 BASIC lessons with verification
when_to_use: when creating or editing C64 BASIC lessons for Code Like It's 198x
version: 1.0.0
languages: BASIC, Assembly
---

# C64 Lesson Creation

## Overview

Creating C64 lessons by "luck and judgment" leads to curriculum drift, broken code, and missing files. This skill enforces the complete verified workflow.

**Core principle:** Curriculum authority + verified code + complete artifacts = shippable lesson.

**This is NOT optional. Follow every step or the lesson will have problems.**

## The Iron Law

```
NO LESSON COMPLETION CLAIMS WITHOUT:
1. Curriculum alignment verified
2. Code compiled with petcat
3. Screenshots captured
4. All files in correct locations
5. Evidence shown for each
```

## The Complete Workflow

### Phase 1: Curriculum Verification (MANDATORY FIRST)

**STOP. Before writing ANY code or content:**

```
1. READ: /CRITICAL-CURRICULUM-AUTHORITY.md (project root)
2. READ: /docs/PHASE-0-CURRICULUM.md - find lesson N specification
3. VERIFY: Does current lesson-NNN.mdx match curriculum spec?

   IF NO MATCH:
     - Archive to _archive/lesson-NNN-OLD-[description].mdx.bak
     - Start fresh from curriculum spec

   IF MATCH:
     - Proceed to edit existing lesson

4. CREATE TODO LIST: Use TodoWrite for all steps below
```

**DO NOT SKIP THIS. Curriculum drift is the #1 failure mode.**

### Phase 2: Reference Loading

**Load START-HERE.md, then quick references only:**

```
1. READ: /docs/START-HERE.md (navigation guide)
2. IDENTIFY: What topics does this lesson cover?
3. LOAD: Only the relevant quick references (12-13KB each):
   - Joystick/keyboard? → CIA-QUICK-REFERENCE.md
   - Sprites/colors? → VIC-II-QUICK-REFERENCE.md
   - Assembly? → 6510-QUICK-REFERENCE.md
   - Character codes? → PETSCII-AND-SCREEN-CODES.md
   - Memory layout? → C64-MEMORY-MAP.md
   - KERNAL calls? → KERNAL-ROUTINES-REFERENCE.md

4. AVOID: Comprehensive references (80-90KB) unless you need:
   - Pin configurations
   - Electrical specs
   - Hardware timing diagrams
```

**Evidence required:** "Loaded [specific quick reference] for [specific topic]"

### Phase 3: Code Sample Creation

**Create BASIC code samples with progressive complexity:**

```
1. PLAN: What code examples demonstrate this lesson's concept?
   - Simple example (5-10 lines)
   - Complex example (10-20 lines) - optional

2. CREATE: Code samples in /code-samples/commodore-64/phase-0/tier-1/lesson-NNN/
   - example-1.bas (simple)
   - example-2.bas (complex, if needed)

3. VERIFY BASIC SYNTAX:
   - NO indentation (BASIC V2 requirement)
   - Lowercase keywords in .bas files (petcat requirement)
   - Line numbers flush left
   - No advanced features (stick to BASIC V2)
   - British English in comments (colour, learnt)
   - BUT: "program" not "programme" for computer programs

4. COMPILE WITH PETCAT:
   cd /code-samples/commodore-64/phase-0/tier-1/lesson-NNN/
   petcat -w2 -o example-1.prg -- example-1.bas

   ✅ EXIT CODE 0 = compilation success
   ❌ EXIT CODE 1 = syntax error - FIX BEFORE PROCEEDING

5. SHOW EVIDENCE:
   - "petcat compiled example-1.bas successfully"
   - Show any syntax errors and fixes
   - Show .prg files created
```

**CRITICAL:** If petcat fails, the BASIC code is broken. Fix it or the lesson is incomplete.

### Phase 4: Screenshot Capture

**Generate screenshots using VICE emulator:**

```
1. ENSURE: .prg files exist (Phase 3 verified)

2. CREATE: Screenshot directory if needed
   mkdir -p /website/public/images/commodore-64/phase-0/tier-1/lesson-NNN/

3. CAPTURE: Screenshots for each example
   x64sc -autostart example-1.prg \
         -limitcycles 20000000 \
         -VICIIdsize \
         -exitscreenshot /website/public/images/commodore-64/phase-0/tier-1/lesson-NNN/example-1.png \
         +sound

4. VERIFY FILES EXIST:
   ls -lh /website/public/images/commodore-64/phase-0/tier-1/lesson-NNN/

   ✅ Show screenshot file sizes
   ❌ Missing screenshots = incomplete lesson

5. SHOW EVIDENCE:
   - "Screenshot captured: example-1.png (XXX KB)"
   - List all screenshot files with sizes
```

**DO NOT claim screenshots exist without showing ls output.**

### Phase 5: Lesson MDX Creation

**Write lesson content following established structure:**

```
1. READ EXAMPLE STRUCTURE:
   - Read lesson-007.mdx or lesson-008.mdx as template
   - Note section structure (flexible, adapt as needed)

2. CREATE: /website/src/pages/commodore-64/phase-0/tier-1/lesson-NNN.mdx

3. REQUIRED SECTIONS (adapt as needed for concept):
   - Opening (custom title)
   - The One-Minute Tour (bullet points)
   - Example Programme (code + explanation)
   - Experiment Section (variations to try)
   - Concept Expansion (why it works)
   - Game Integration (how games use this)
   - From the Vault (reference links)
   - Quick Reference (tables/addresses)
   - What You've Learnt (bullet summary)

4. CODE FORMATTING IN MDX:
   - UPPERCASE keywords for display (POKE not poke)
   - NO indentation (line numbers flush left)
   - Include line numbers
   - Add explanatory comments

5. IMAGE REFERENCES:
   - Use relative paths: /images/commodore-64/phase-0/tier-1/lesson-NNN/example-1.png
   - Verify image paths match Phase 4 screenshot locations

6. VERIFY CHECKLIST:
   - [ ] British English (colour, learnt)
   - [ ] "program" not "programme"
   - [ ] No "Insight" blocks
   - [ ] No "WOW Moment" sections
   - [ ] Matches curriculum specification
   - [ ] All code examples included
   - [ ] All screenshot references valid
```

### Phase 6: Final Verification (MANDATORY)

**Complete verification before claiming lesson is done:**

```
1. CURRICULUM ALIGNMENT:
   ✅ Re-read PHASE-0-CURRICULUM.md lesson N spec
   ✅ Verify lesson teaches specified concepts
   ✅ Show: "Lesson covers: [list curriculum requirements]"

2. CODE COMPILATION:
   ✅ Re-run petcat on all .bas files
   ✅ Show: "All code samples compile successfully"
   ❌ ANY errors = lesson incomplete

3. FILE CHECKLIST:
   ✅ Code samples exist: ls /code-samples/.../lesson-NNN/
   ✅ .prg files exist: ls /code-samples/.../lesson-NNN/*.prg
   ✅ Screenshots exist: ls /website/public/images/.../lesson-NNN/
   ✅ Lesson MDX exists: ls /website/src/pages/.../lesson-NNN.mdx
   ✅ Show output for each ls command

4. BRITISH ENGLISH VERIFICATION:
   ✅ Grep for American spellings:
      grep -i "color\|behavior\|favorite" lesson-NNN.mdx
      (Should return nothing or only in code comments)
   ✅ Verify "program" used for computer programs (not "programme")

5. FORMATTING VERIFICATION:
   ✅ Check no indentation in code blocks
   ✅ Check line numbers flush left
   ✅ Check UPPERCASE keywords in MDX
   ✅ Check lowercase keywords in .bas files

6. EVIDENCE SUMMARY:
   Required before completion claim:
   - Curriculum spec quoted
   - petcat output shown (all files)
   - File listings shown (all directories)
   - Grep results shown
   - Any issues found and fixed
```

**ONLY AFTER showing all evidence above can you claim lesson is complete.**

## Common Failures - STOP

| Red Flag | Why It's Wrong | Fix |
|----------|----------------|-----|
| "Code should work" | Didn't run petcat | Run petcat, show output |
| "Lesson is complete" | No file listings shown | Show ls for all locations |
| "Matches curriculum" | Didn't re-read spec | Quote curriculum spec |
| "Screenshots captured" | No evidence shown | Show ls output with sizes |
| "Verified British English" | Didn't run grep | Run grep, show results |
| Using "programme" for computer programs | Wrong convention | Use "program" for software |
| "Following template" | Didn't read example lessons | Read lesson-007/008 first |
| Loading comprehensive refs | Wasting context | Use quick references only |

## Rationalization Prevention

| Excuse | Reality |
|--------|---------|
| "I checked the curriculum earlier" | Re-check before completion |
| "petcat worked last time" | Re-run for each file |
| "Screenshots probably captured" | SHOW ls output |
| "It's just a small edit" | Full verification still required |
| "I'm confident the code works" | Confidence ≠ petcat success |
| "Quick references probably enough" | Load START-HERE.md first |

## TodoWrite Integration

**MANDATORY:** Create todos for each phase:

```javascript
[
  {content: "Verify curriculum alignment for lesson N", status: "in_progress", activeForm: "Verifying curriculum"},
  {content: "Load relevant quick references from START-HERE.md", status: "pending", activeForm: "Loading references"},
  {content: "Create code samples and compile with petcat", status: "pending", activeForm: "Creating code samples"},
  {content: "Capture screenshots with VICE", status: "pending", activeForm: "Capturing screenshots"},
  {content: "Write lesson MDX following template", status: "pending", activeForm: "Writing lesson"},
  {content: "Run final verification checklist", status: "pending", activeForm: "Verifying completion"}
]
```

**Update status as you complete each phase. Mark completed ONLY after showing evidence.**

## File Location Quick Reference

```
Curriculum Spec:
  /CRITICAL-CURRICULUM-AUTHORITY.md
  /docs/PHASE-0-CURRICULUM.md

Navigation:
  /docs/START-HERE.md

Quick References (load these):
  /docs/CIA-QUICK-REFERENCE.md (12KB)
  /docs/VIC-II-QUICK-REFERENCE.md (13KB)
  /docs/6510-QUICK-REFERENCE.md (13KB)
  /docs/PETSCII-AND-SCREEN-CODES.md (12KB)
  /docs/C64-MEMORY-MAP.md (15KB)
  /docs/KERNAL-ROUTINES-REFERENCE.md (13KB)

Code Samples:
  /code-samples/commodore-64/phase-0/tier-1/lesson-NNN/example-1.bas
  /code-samples/commodore-64/phase-0/tier-1/lesson-NNN/example-1.prg

Screenshots:
  /website/public/images/commodore-64/phase-0/tier-1/lesson-NNN/example-1.png

Lesson File:
  /website/src/pages/commodore-64/phase-0/tier-1/lesson-NNN.mdx

Archive (if curriculum mismatch):
  /website/src/pages/commodore-64/phase-0/tier-1/_archive/lesson-NNN-OLD.mdx.bak
```

## Example: Complete Lesson Creation

**User asks:** "Create lesson 7 about border colors"

```
✅ CORRECT APPROACH:

1. READ /CRITICAL-CURRICULUM-AUTHORITY.md
2. READ /docs/PHASE-0-CURRICULUM.md - find Lesson 7
3. VERIFY: "Lesson 7 should teach: The First Color (POKE 53280/53281, rainbow border)"
4. CREATE TODOS using TodoWrite (6 phases)
5. LOAD /docs/START-HERE.md
6. LOAD /docs/VIC-II-QUICK-REFERENCE.md (need $D020/$D021 registers)
7. CREATE /code-samples/.../lesson-007/example-1.bas:
   10 rem rainbow border
   20 for i=0 to 15
   30 poke 53280,i
   40 for d=1 to 100:next d
   50 next i
   60 goto 20

8. COMPILE:
   $ petcat -w2 -o example-1.prg -- example-1.bas
   [Show output: success]

9. CAPTURE SCREENSHOT:
   $ x64sc -autostart example-1.prg -limitcycles 20000000 ...
   $ ls -lh /website/public/images/.../lesson-007/
   [Show: example-1.png 24K]

10. CREATE lesson-007.mdx following lesson-008 structure
11. FINAL VERIFICATION:
    - Re-read curriculum spec [show quote]
    - Re-run petcat [show success]
    - ls code samples [show files]
    - ls screenshots [show files]
    - grep American spellings [show none found]
    - Verify formatting [show checklist complete]

12. CLAIM: "Lesson 7 complete. Evidence shown above."


❌ WRONG APPROACH:

"I'll create lesson 7 about border colors. The code should work, I've written the lesson file, and I think all the screenshots are there. Lesson complete!"

[No curriculum check, no petcat output, no file listings, no evidence = INCOMPLETE]
```

## When Things Go Wrong

**petcat compilation fails:**
```
1. READ error message carefully
2. IDENTIFY syntax error line number
3. FIX .bas file
4. RE-RUN petcat
5. SHOW: "Fixed syntax error on line X, petcat now succeeds"
6. CONTINUE to next phase
```

**Screenshot capture fails:**
```
1. CHECK .prg file exists
2. VERIFY command syntax
3. CHECK directory exists
4. RE-RUN with corrected command
5. SHOW: ls output proving screenshot exists
6. CONTINUE to next phase
```

**Curriculum mismatch discovered:**
```
1. ARCHIVE current lesson: lesson-NNN-OLD-[description].mdx.bak
2. START FRESH from curriculum specification
3. DO NOT edit mismatched lesson
4. SHOW: "Archived mismatched lesson, creating from curriculum spec"
```

## Integration with Other Skills

**This skill works with:**
- **verification-before-completion**: Applied in Phase 6
- **TodoWrite**: Phase tracking throughout
- **START-HERE.md**: Reference navigation in Phase 2

**This skill REPLACES:**
- Ad-hoc lesson editing
- "I think the code works" claims
- Loading comprehensive references by default
- Curriculum drift through forgetfulness

## The Bottom Line

**Every lesson must:**
1. Match curriculum specification (verified by quote)
2. Compile with petcat (verified by command output)
3. Have screenshots (verified by ls output)
4. Follow formatting rules (verified by grep/checklist)
5. Show evidence for each claim

**No shortcuts. No "it should work". No completion claims without evidence.**

**This workflow exists because lessons created without it have had:**
- Broken code that doesn't compile
- Missing screenshots
- Wrong concepts (curriculum drift)
- American English (should be British)
- Indented code (BASIC V2 violation)

**Follow this skill or the lesson will have problems. Non-negotiable.**

---

**Version:** 1.0.0
**Created:** 2025-10-18
**Purpose:** Eliminate "luck and judgment" lesson creation
