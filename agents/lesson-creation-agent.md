# Lesson Creation Agent

**Type:** Autonomous multi-step execution agent
**Invoked via:** Task tool with `subagent_type: general-purpose`
**Priority:** P1 (High - major time saver)
**Complexity:** High

---

## Purpose

Autonomously creates a complete lesson with all required files:
- Code samples (compiled and tested)
- Screenshots (captured and verified)
- Lesson MDX file
- Navigation updates across all levels
- Complete validation

---

## What It Does

The agent executes the complete lesson creation workflow autonomously:

1. **Reads lesson specification** from curriculum document
2. **Creates code files** in correct platform/phase/tier/lesson directory
3. **Compiles code** using platform-specific toolchain (creates loadable files)
4. **STOPS and instructs user** on screenshot capture
5. **Waits for screenshots** - User captures manually in emulator
6. **Verifies screenshots** show correct output (no errors) using READ tool
7. **Creates lesson MDX** following archetype structure
8. **Runs validation** using all relevant skills
9. **Updates navigation** at tier/phase/platform/home levels
10. **Reports completion** or errors with specific details

---

## Input Required

The agent needs:

**Lesson Specification:**
- Platform (e.g., "commodore-64", "sinclair-zx-spectrum")
- Phase number (e.g., 0, 1)
- Tier number (e.g., 1, 2)
- Lesson number (e.g., 7, 16)
- Path to curriculum spec file

**Example:**
```
Platform: sinclair-zx-spectrum
Phase: 0
Tier: 1
Lesson: 7
Curriculum: /docs/sinclair-zx-spectrum/phase-0/tier-1/lesson-007.md
```

---

## Decisions Agent Makes Autonomously

The agent makes these implementation decisions without asking:

1. **File naming** - Uses standard conventions (example-1.bas, example-2.bas)
2. **Screenshot instructions** - Generates exact emulator commands for user
3. **Navigation text** - Formats lesson descriptions for navigation files
4. **Section order** - Arranges MDX sections following lesson archetype
5. **Code formatting** - Applies platform-specific formatting rules
6. **Validation order** - Runs validation checks in logical sequence

---

## Skills Agent MUST Use

The agent must use these skills (not optional):

**Mandatory Skills:**
1. **lesson-creation-workflow** - Follow complete 7-step workflow
2. **lesson-validation** - Run all validation checks
3. **screenshot-verification** - Verify screenshots show correct output
4. **curriculum-alignment-check** - Ensure lesson matches spec
5. **voice-tone-check** - Check for marketing speak, forbidden sections
6. **british-english-check** - Verify British English spellings
7. **strategic-alignment-check** - Verify alignment with project principles

**Platform-Specific Skills:**
- **c64-lesson-creation** (if C64 BASIC)
- **c64-6510-lesson-creation** (if C64 assembly)
- **zx-lesson-creation** (if ZX Spectrum BASIC)
- **zx-z80-lesson-creation** (if ZX Spectrum assembly)
- **nes-lesson-creation** (if NES)
- **amiga-lesson-creation** (if Amiga BASIC)
- **amiga-68k-lesson-creation** (if Amiga assembly)

---

## Agent Behavior

### Success Path - Part 1 (Code Creation)

1. Reads curriculum spec completely
2. Creates all code files in correct locations
3. Compiles code successfully (creates loadable .tap/.prg/.nes files)
4. **STOPS and reports:**
   ```
   Code created and compiled successfully.

   FILES CREATED:
   - /code-samples/.../lesson-NNN/example-1.bas
   - /code-samples/.../lesson-NNN/example-1.tap

   NEXT STEP (MANUAL):
   1. Load example-1.tap in Fuse emulator
   2. Capture screenshot to: /website/public/images/.../lesson-NNN/example-1.png
   3. Verify output matches curriculum spec
   4. Re-invoke agent with: continue_from=screenshot_verification
   ```

### Success Path - Part 2 (After Screenshots)

5. Verifies screenshots exist and show correct output (no errors)
6. Creates lesson MDX with all required sections
7. Runs all validation skills (all pass)
8. Updates navigation at all levels
9. Reports: "Lesson NNN created successfully. All validation passed."

### Error Path

If ANY step fails:
1. Agent stops immediately
2. Reports specific failure with details
3. Lists what completed successfully
4. Lists what failed and why
5. Does NOT continue to next steps
6. Does NOT create partial navigation updates

**Example error report:**
```
Lesson creation FAILED at step 3 (code compilation).

Completed:
✓ Read curriculum spec
✓ Created code files

Failed:
✗ Compilation error in example-2.bas
  Line 25: ?SYNTAX ERROR

Next steps:
- Fix syntax error in example-2.bas
- Re-run agent from step 3
```

---

## User Involvement

**Phase 1 - Code Creation:**
- User provides lesson spec details
- Agent creates and compiles code
- Agent stops with instructions

**Manual Screenshot Step:**
- User loads compiled code in emulator
- User captures screenshots manually
- User saves to correct location

**Phase 2 - Lesson Completion:**
- User re-invokes agent with continue_from flag
- Agent verifies screenshots
- Agent creates lesson MDX
- Agent runs validation
- Agent updates navigation

**After completion:** User reviews:
- Final lesson file
- Screenshots (already captured)
- Code samples
- Navigation updates

**User can:** Accept, request changes, or reject

---

## Platform-Specific Requirements

### Commodore 64 BASIC
- **Compiler:** `petcat -w2 -o output.prg -- input.bas`
- **Screenshot:** `x64sc -autostart example.prg -limitcycles 20000000 -VICIIdsize -exitscreenshot [path] +sound`
- **Validator:** `python3 scripts/validate-c64-basic.py`
- **Code style:** lowercase keywords, no indentation, flush left

### ZX Spectrum BASIC
- **Compiler:** `zmakebas -o output.tap input.bas`
- **Screenshot:** Fuse screenshot method or automated script
- **Validator:** `python3 scripts/validate-zx-basic.py`
- **Code style:** Platform-specific conventions

### NES Assembly
- **Compiler:** `ca65 input.s -o input.o && ld65 input.o -C nes.cfg -o output.nes`
- **Screenshot:** FCEUX with lua script or manual capture
- **Validator:** `python3 scripts/validate-nes-asm.py`
- **Code style:** ca65 syntax

### Commodore Amiga
- **Compiler:** `vasm` (specific flags per language)
- **Screenshot:** FS-UAE screenshot
- **Validator:** `python3 scripts/validate-68k-asm.py` or AMOS validator
- **Code style:** Platform-specific

---

## File Locations

The agent creates files in these exact locations:

**Code samples:**
```
/code-samples/{platform}/phase-{N}/tier-{N}/lesson-{NNN}/
├── example-1.bas (or .s, .asm, etc.)
├── example-1.prg (or .nes, .tap, etc.)
├── example-2.bas
└── example-2.prg
```

**Screenshots:**
```
/website/public/images/{platform}/phase-{N}/tier-{N}/lesson-{NNN}/
├── example-1.png
└── example-2.png
```

**Lesson MDX:**
```
/website/src/pages/{platform}/phase-{N}/tier-{N}/lesson-{NNN}.mdx
```

**Navigation files to update:**
```
/website/src/pages/{platform}/phase-{N}/tier-{N}/index.astro
/website/src/pages/{platform}/phase-{N}/index.astro (if first in tier)
/website/src/pages/{platform}/index.astro (if first in phase)
/website/src/pages/index.mdx (if milestone)
```

---

## Invocation Pattern

### Phase 1: Code Creation

```javascript
Task tool invocation:
{
  subagent_type: "general-purpose",
  description: "Create lesson code and compile",
  prompt: `You are creating lesson code for the Code Like It's 198x project.

LESSON SPECIFICATION:
- Platform: {platform}
- Phase: {N}
- Tier: {N}
- Lesson: {NNN}
- Curriculum spec: {path-to-curriculum-spec}

YOUR TASK - PHASE 1 (CODE CREATION):
1. Read curriculum spec completely
2. Create code files in /code-samples/{platform}/phase-{N}/tier-{N}/lesson-{NNN}/
3. Compile code using platform-specific toolchain
4. STOP and provide screenshot instructions

Use {platform-specific-skill} for code formatting and compilation.

DO NOT:
- Try to capture screenshots (emulators resist automation)
- Create lesson MDX yet (wait for screenshots)
- Update navigation yet (wait for full validation)

STOP AFTER COMPILATION with this report:
"Code created and compiled successfully.

FILES CREATED:
[list all .bas/.s and compiled .tap/.prg/.nes files]

NEXT STEP (MANUAL):
1. Load {compiled-file} in {emulator-name}
2. Capture screenshot to: {exact-path}
3. After screenshots captured, re-invoke with continue_from=screenshot_verification"

Execute code creation now.`
}
```

### Phase 2: Lesson Completion

```javascript
Task tool invocation:
{
  subagent_type: "general-purpose",
  description: "Complete lesson with validation",
  prompt: `You are completing lesson {NNN} for the Code Like It's 198x project.

CONTEXT:
Phase 1 completed - code created and compiled.
Screenshots captured manually by user.

LESSON SPECIFICATION:
- Platform: {platform}
- Phase: {N}
- Tier: {N}
- Lesson: {NNN}
- Curriculum spec: {path-to-curriculum-spec}

YOUR TASK - PHASE 2 (LESSON COMPLETION):
1. Verify screenshots exist at /website/public/images/{platform}/phase-{N}/tier-{N}/lesson-{NNN}/
2. Use screenshot-verification skill to check screenshot content (READ tool)
3. Create lesson MDX following Discovery/Challenge/Synthesis archetype
4. Run ALL validation skills
5. Update navigation at tier/phase/platform levels

MANDATORY SKILLS TO USE:
1. screenshot-verification - Verify screenshots show correct output (no errors)
2. curriculum-alignment-check - Match curriculum spec
3. voice-tone-check - Proper tone, no marketing speak
4. british-english-check - British spellings
5. strategic-alignment-check - Strategic principles
6. lesson-validation - All validation checks

IF ANY VALIDATION FAILS:
- Stop immediately
- Report specific failure
- Do NOT update navigation

REPORT:
If successful: "Lesson {NNN} created successfully. All validation passed. Navigation updated."
If failed: "Validation FAILED: [specific issue]. Fix required before navigation update."

Execute lesson completion now.`
}
```

---

## Dependencies

**Required infrastructure:**
- Platform-specific compilers installed
- Screenshot scripts/tools available
- Semantic validators present
- All validation skills accessible
- Navigation file structure exists

**Curriculum documents:**
- Platform curriculum specs exist and are complete
- Lesson specs have all required details

---

## Success Metrics

**Agent succeeds if:**
- All code files compile without errors
- All screenshots show correct output (no error messages)
- Lesson MDX follows archetype structure
- All validation skills pass
- Navigation updated at all required levels
- No manual intervention required

**Agent fails if:**
- Any compilation error
- Screenshot shows error message or blank screen
- Any validation skill fails
- Navigation not updated
- Requires user input mid-execution

---

## Testing the Agent

**Test with:**
1. Simple lesson (5-10 lines of code, 1 screenshot)
2. Medium lesson (20-30 lines, 2 screenshots)
3. Complex lesson (40+ lines, 3+ screenshots)
4. Lesson with deliberate error (compilation should fail correctly)

**Verify:**
- Agent completes all steps autonomously
- Error handling is clear and actionable
- Validation catches issues before navigation updates
- Final output matches curriculum spec exactly

---

## Common Failure Modes

**Failure 1: Screenshot shows error**
- **Cause:** Code has runtime error not caught by compilation
- **Detection:** Phase 2 screenshot-verification catches this with READ tool
- **Fix:** User must fix code and recapture screenshot before Phase 2
- **Prevention:** Test code in emulator during screenshot capture

**Failure 2: Screenshot missing or wrong location**
- **Cause:** User saved screenshot to incorrect path
- **Detection:** Phase 2 checks file existence before proceeding
- **Fix:** Move screenshot to correct location or recapture
- **Prevention:** Follow exact path from Phase 1 instructions

**Failure 3: Navigation not updated**
- **Cause:** Agent forgets final step or validation failed
- **Fix:** lesson-creation-workflow skill enforces navigation update
- **Prevention:** Only update navigation after all validation passes

**Failure 4: Curriculum mismatch**
- **Cause:** Agent improvised instead of following spec
- **Detection:** curriculum-alignment-check skill catches this in Phase 2
- **Fix:** Revise lesson MDX to match curriculum spec
- **Prevention:** Read spec completely in Phase 1

**Failure 5: Marketing speak in lesson**
- **Cause:** Agent used hype language in MDX
- **Detection:** voice-tone-check skill catches this in Phase 2
- **Fix:** Remove marketing language, use technical terms
- **Prevention:** Follow exemplar lessons, avoid exclamation marks

---

## The Bottom Line

**This agent replaces manual lesson creation. It must:**
1. Follow all skills systematically
2. Make no assumptions (read specs completely)
3. Validate everything before navigation updates
4. Report errors clearly
5. Create production-ready lessons autonomously

**Zero tolerance for:**
- Skipping validation
- Partial navigation updates
- Screenshots with errors
- Code that doesn't compile
- Curriculum mismatches
