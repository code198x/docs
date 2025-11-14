---
name: c64-lesson-creation
description: Use when creating or editing C64 BASIC lessons - enforces platform-specific compilation, validation, screenshot capture, and C64-specific requirements
---

# C64 BASIC Lesson Creation

## Overview

This skill guides creation of C64 BASIC (Commodore BASIC V2) lessons with platform-specific validation, compilation, and screenshot capture. It extends the generic lesson-creation-workflow with C64-specific requirements.

---

## ⚠️ CRITICAL VERIFICATION REQUIREMENTS

**Before claiming ANY lesson is complete, you MUST:**

### 1. Screenshot Verification (MANDATORY)

**Use Read tool to VIEW every screenshot and provide evidence:**

```
✅ CORRECT: "Read screenshot-1.png - shows green platforms, red player sprite at Y=100, status text 'HP: 20/20'. NO error messages visible."

❌ WRONG: "Screenshot verified ✅" (too vague, not acceptable)
❌ WRONG: "Screenshot captured successfully" (didn't verify content)
```

**Check for error messages** (these = automatic failure):
- `?SYNTAX ERROR IN [line]` → Syntax error, fix immediately
- `?UNDEF'D STATEMENT ERROR IN [line]` → Missing GOSUB target
- `?ILLEGAL QUANTITY ERROR IN [line]` → Value out of range (negative coordinates, etc.)
- Blank screen → Initialization bug or program crash

**If ANY error found:** Fix code, recompile, recapture, re-verify. Repeat until clean.

### 2. Reserved Variables (C64 BASIC V2)

**NEVER use these reserved system variables:**
- `ST` - I/O status register (read-only, causes SYNTAX ERROR if written)
- `TI` - Jiffy clock (60Hz counter, can conflict with game timing)
- `TI$` - Time string (HH:MM:SS format, can cause issues)

**Use instead:**
- `GS` - Game state
- `CT` - Custom timer
- `SC` - Score
- `HP` - Health points
- Any other non-reserved 1-2 letter variable name

**Validation command:**
```bash
# Check for reserved variables
grep -iE '\<(st|ti|ti\$)\>' example-1.bas
# Should return nothing (no matches)
```

### 3. GOSUB Target Verification

**Every GOSUB must have a corresponding line number.**

**Validation command:**
```bash
# Find all GOSUB calls
grep -i "gosub" example-1.bas

# For each target line number, verify it exists
grep "^[target] " example-1.bas
```

**Example:**
```basic
100 GOSUB 1000   ← Line 1000 MUST exist
...
1000 REM SUBROUTINE  ← Target exists ✓
```

Missing target → `?UNDEF'D STATEMENT ERROR IN [line]`

### 4. Initialization Validation

**Common initialization bugs:**

```basic
❌ WRONG:
100 CX=0:LX=0    ← Camera and last camera both 0
110 IF ABS(CX-LX)<8 THEN RETURN   ← TRUE on first frame, skips first draw!

✅ CORRECT:
100 CX=0:LX=-999   ← Forces first draw (ABS(0-(-999)) = 999 >= 8)
```

**Other common issues:**
- Arrays not dimensioned: `DIM PX(10), PY(10)`
- Variables not initialized: All game variables should have initial values
- First-run behavior: Test that program works correctly on first execution

### 5. Verification Evidence Required

**When claiming verification complete, you MUST provide:**

- [ ] "Used Read tool to view screenshot-1.png"
- [ ] "Describe what I saw: [specific visible elements]"
- [ ] "Confirmed NO error messages visible"
- [ ] "Checked for reserved variables - none found"
- [ ] "Verified all GOSUB targets exist"
- [ ] "Compilation successful: petcat exit code 0"

**Not acceptable:** "All verification complete ✅" (no evidence)

## When to Use

Use when:
- Creating new C64 BASIC lesson
- Editing existing C64 BASIC lesson
- Validating C64 BASIC lesson before commit

**Do NOT use for:**
- C64 6510 Assembly lessons (use c64-6510-lesson-creation instead)
- Other platforms (use platform-specific skills)

---

## Prerequisites

**Before starting, ensure:**

1. **lesson-creation-workflow skill** - Read generic workflow first
2. **Curriculum alignment** - Read `/docs/commodore-64/PHASE-N-CURRICULUM.md`
3. **Tools installed:**
   - `petcat` (VICE tools) - BASIC tokenizer/detokenizer
   - `x64sc` (VICE emulator) - For screenshot capture
   - Python 3 - For semantic validator

---

## C64 BASIC Language Rules

**Critical requirements for C64 BASIC V2:**

### 1. NO Indentation
```basic
✓ CORRECT:
10 PRINT "HELLO"
20 FOR I=1 TO 10
30 PRINT I
40 NEXT I

✗ WRONG:
10 PRINT "HELLO"
20 FOR I=1 TO 10
30   PRINT I    ← NO INDENTATION
40 NEXT I
```

**Why:** BASIC V2 doesn't support indentation. All line numbers flush left.

### 2. Lowercase Keywords in .bas Files

```basic
✓ CORRECT (.bas file):
10 print "hello"
20 poke 53280,0

✗ WRONG (.bas file):
10 PRINT "hello"    ← Uppercase causes petcat issues
20 POKE 53280,0
```

**Why:** petcat expects lowercase keywords in source files.

**But:** Display uppercase in MDX lesson content (readability).

### 3. BASIC V2 Limitations

**HAS:**
- `AND`, `OR` operators (contrary to some docs)
- `LEFT$`, `RIGHT$`, `MID$`, `LEN` string functions
- `PEEK`, `POKE` for hardware access
- `SYS` for machine code calls

**DOES NOT HAVE:**
- `WHILE`/`WEND` (use `FOR` or `GOTO`)
- `DO`/`LOOP` (use `FOR` or `GOTO`)
- `CASE`/`SWITCH` (use `IF`/`THEN`/`ELSE` chains)
- Advanced string functions (`INSTR`, `REPLACE`, etc.)
- `ELSE` on same line as `IF` (must use separate line)

### 4. British English Exception

**"Program" not "Programme"** for computer programs (only exception to British English rule).

---

## Required Files Checklist

For C64 BASIC lesson NNN in Phase X, Tier Y:

- [ ] `/website/src/pages/commodore-64/phase-X/tier-Y/lesson-NNN.mdx`
- [ ] `/code-samples/commodore-64/phase-X/tier-Y/lesson-NNN/example-1.bas`
- [ ] `/code-samples/commodore-64/phase-X/tier-Y/lesson-NNN/example-1.prg` (compiled)
- [ ] `/code-samples/commodore-64/phase-X/tier-Y/lesson-NNN/example-2.bas` (if applicable)
- [ ] `/code-samples/commodore-64/phase-X/tier-Y/lesson-NNN/example-2.prg` (if applicable)
- [ ] `/website/public/images/commodore-64/phase-X/tier-Y/lesson-NNN/screenshot-1.png`
- [ ] `/website/public/images/commodore-64/phase-X/tier-Y/lesson-NNN/screenshot-2.png` (if applicable)

---

## Compilation Process

### Step 1: Validate BASIC Syntax

**Before compilation, check:**

```bash
# Check for indentation (MUST be none)
grep "^[0-9]* " code-samples/.../lesson-NNN/example-1.bas

# Should show all lines starting with line number + space (no extra spaces)
```

**Common syntax issues:**
- Indented lines
- Missing line numbers
- Uppercase keywords (should be lowercase in .bas)
- Invalid BASIC V2 commands (WHILE, DO, etc.)

### Step 2: Run Semantic Validator (MANDATORY)

**Run BEFORE petcat - catches errors petcat cannot detect!**

```bash
cd /code-samples/commodore-64/phase-X/tier-Y/lesson-NNN/

# C64 BASIC semantic validator - MUST PASS
python3 /scripts/validate-c64-basic.py example-1.bas
```

**Semantic checks (NEW validations from Tier 3 learnings):**
- ✅ **Reserved variables (ST, TI, TI$)** - causes ?SYNTAX ERROR
- ✅ **Array re-dimensioning** - DIM same array twice
- ✅ **GOSUB/GOTO to non-existent lines** - causes ?UNDEF'D STATEMENT ERROR
- ✅ **Duplicate line numbers** - confusing behavior
- ✅ **FOR/NEXT mismatches** - loop errors
- ✅ POKE addresses in valid ranges
- ✅ Screen memory ($0400-$07E7)
- ✅ Colour memory ($D800-$DBE7)
- ✅ VIC-II registers ($D000-$D02E)
- ✅ SID registers ($D400-$D41C)
- ✅ CIA registers ($DC00-$DC0F)
- ✅ Invalid memory writes (ROM areas)
- ✅ BASIC V2 compatibility (no WHILE/DO/CASE)

**Validator output examples:**
```
✅ example-1.bas passed all semantic checks

❌ ERRORS in example-1.bas:
   ❌ Line 20: Reserved variable 'ST' cannot be assigned to (causes ?SYNTAX ERROR)
   ❌ Line 40: Array 'A' re-dimensioned (already DIM'd at line 30)
   ❌ Line 50: GOSUB to non-existent line 2000 (causes ?UNDEF'D STATEMENT ERROR)
```

**If validator shows errors:** Fix them before proceeding to petcat!

### Step 3: Compile with petcat

**Only run after semantic validator passes!**

```bash
# Compile BASIC to PRG
petcat -w2 -o example-1.prg -- example-1.bas

# Check exit code
echo $?  # Should be 0 (success)
```

**Flags explained:**
- `-w2` = BASIC V2 (C64)
- `-o example-1.prg` = Output file
- `-- example-1.bas` = Input file

**Common petcat errors:**
- `petcat: error: ...` → Syntax error in BASIC
- `petcat: warning: ...` → Usually safe to ignore
- Exit code != 0 → Compilation failed

**Note:** Petcat only tokenizes - it does NOT do semantic validation! Always run the semantic validator first.

---

## Screenshot Capture

### Method: VICE x64sc Emulator

**C64 screenshots use x64sc (accurate C64 emulation).**

### Step 1: Load Compiled Program

```bash
# From lesson-NNN directory
x64sc -autostart example-1.prg
```

**Emulator opens with program auto-running.**

### Step 2: Capture Screenshot

**Manual capture (recommended):**
1. Let program run to interesting point
2. Press `Alt+S` (or menu: Screenshot → Save screenshot)
3. Save as PNG to `/website/public/images/commodore-64/phase-X/tier-Y/lesson-NNN/screenshot-1.png`

**Automated capture (for static output):**
```bash
x64sc -autostart example-1.prg \
  -limitcycles 20000000 \
  -VICIIdsize \
  -exitscreenshot /website/public/images/commodore-64/phase-X/tier-Y/lesson-NNN/screenshot-1.png \
  +sound
```

**Flags explained:**
- `-limitcycles 20000000` = Run ~20 seconds then exit
- `-VICIIdsize` = Normal screen size (not double)
- `-exitscreenshot [path]` = Save screenshot on exit
- `+sound` = Disable sound (faster)

**When to use automated:**
- Static output (text display, simple graphics)
- Repeatable (same output every run)

**When to use manual:**
- Interactive programs (joystick, keyboard input)
- Animation/scrolling (capture interesting frame)
- Random elements (need specific screenshot)

### Step 3: Verify Screenshot

**Use READ tool to view screenshot:**

```bash
# Read screenshot to verify
Read("/website/public/images/commodore-64/phase-X/tier-Y/lesson-NNN/screenshot-1.png")
```

**Check for:**
- ✓ Expected output visible
- ✓ Not blank screen (program crashed)
- ✓ Not error message ("SYNTAX ERROR", "ILLEGAL QUANTITY")
- ✓ Correct colours
- ✓ Text readable (not garbled PETSCII)

**Use screenshot-verification skill for comprehensive check.**

---

## C64-Specific Validation

### 1. Memory Map Validation

**Valid C64 BASIC memory ranges:**

| Range | Purpose | Write | Read |
|-------|---------|-------|------|
| `$0400-$07E7` | Screen RAM | ✓ | ✓ |
| `$D800-$DBE7` | Colour RAM | ✓ | ✓ |
| `$D000-$D02E` | VIC-II | ✓ | ✓ |
| `$D400-$D41C` | SID | ✓ | ✓ |
| `$DC00-$DC0F` | CIA #1 | ✓ | ✓ |
| `$DD00-$DD0F` | CIA #2 | ✓ | ✓ |
| `$0002-$00FF` | Zero page | ✓ | ✓ (careful!) |
| `$A000-$BFFF` | BASIC ROM | ✗ | ✓ |
| `$E000-$FFFF` | KERNAL ROM | ✗ | ✓ |

**Check code for:**
```bash
# Find all POKEs
grep -in "poke" example-1.bas

# Validate addresses are in writable ranges
```

### 2. PETSCII vs Screen Codes

**Common mistake:** Confusing PETSCII codes with screen codes.

**PETSCII codes** (for `PRINT`, `CHR$`):
- Clear screen: `CHR$(147)`
- Colour codes: `CHR$(144-159)` for text colour
- Reverse on: `CHR$(18)`
- Reverse off: `CHR$(146)`

**Screen codes** (for `POKE` to screen memory):
- Different mapping than PETSCII
- Space = 32 (PETSCII) but 0 (screen code)
- Letters: A=1, B=2, ..., Z=26 (screen codes)

**Validation:**
```bash
# Check for screen code POKEs
grep -in "poke.*1024" example-1.bas

# Ensure using correct codes (not PETSCII for screen memory)
```

### 3. VIC-II Register Usage

**Common VIC-II operations in lessons:**

| Address | Register | Purpose |
|---------|----------|---------|
| 53280 | $D020 | Border colour |
| 53281 | $D021 | Background colour |
| 53248-53264 | $D000-$D010 | Sprite X/Y positions |
| 53269 | $D015 | Sprite enable |
| 53287-53294 | $D027-$D02E | Sprite colours |

**Validation:**
```bash
# Find VIC-II POKEs
grep -iE "poke.*532[0-9]{2}" example-1.bas

# Common mistakes:
# - POKE 532800 instead of 53280 (typo)
# - POKE 53280,16 (colour out of range 0-15)
```

### 4. SID Register Usage

**Common SID operations:**

| Address | Register | Purpose |
|---------|----------|---------|
| 54272 | $D400 | Voice 1 frequency low |
| 54273 | $D401 | Voice 1 frequency high |
| 54276 | $D404 | Voice 1 control |
| 54296 | $D418 | Volume/filter mode |

**Validation:**
```bash
# Find SID POKEs
grep -iE "poke.*542[0-9]{2}" example-1.bas
```

### 5. Line Number Range

**Valid: 0-63999**

**Common mistakes:**
- Line number 64000+ (invalid)
- Negative line numbers (invalid)
- Non-sequential (warning, but valid)

```bash
# Check line numbers
awk '/^[0-9]+/ {print $1}' example-1.bas | sort -n
```

---

## Anti-Patterns (C64 BASIC Specific)

### 1. Busy-Wait Loops Without Checks

**Anti-pattern:**
```basic
100 REM wait for key
110 IF PEEK(197)=64 THEN 110  ← Busy loop, wastes CPU
```

**Better:**
```basic
100 REM wait for key
110 GET K$ : IF K$="" THEN 110  ← Built-in keyboard buffer check
```

### 2. Clearing Screen in Loop

**Anti-pattern:**
```basic
100 PRINT CHR$(147)  ← Clear screen
110 PRINT "SCORE:";SCORE
120 GOTO 100  ← Causes flicker
```

**Better:**
```basic
100 PRINT CHR$(147)
110 POKE 214,0 : PRINT  ← Cursor to top
120 PRINT "SCORE:";SCORE
130 GOTO 110  ← Update only score area
```

### 3. String Concatenation in Loops

**Anti-pattern:**
```basic
100 A$=""
110 FOR I=1 TO 100
120 A$=A$+"X"  ← String grows, gets slow
130 NEXT I
```

**Better:**
```basic
100 FOR I=1 TO 100
110 PRINT "X";  ← Direct output, no string growth
120 NEXT I
```

### 4. Forgetting to Restore Registers

**Anti-pattern:**
```basic
100 POKE 53280,0  ← Change border
...
500 END  ← Border stays black after program ends
```

**Better:**
```basic
100 B=PEEK(53280) : REM save original
110 POKE 53280,0
...
500 POKE 53280,B : END  ← Restore on exit
```

---

## Integration with Other Skills

**After code creation, run these skills:**

1. **lesson-validation** - Generic validation
2. **curriculum-alignment-check** - Verify matches curriculum
3. **screenshot-verification** - Verify screenshots correct
4. **british-english-check** - Language validation
5. **voice-tone-check** - Voice consistency

---

## Complete Workflow Checklist

### Phase 1: Preparation

- [ ] Read curriculum spec for lesson
- [ ] Check if mismatched lesson exists (archive if needed)
- [ ] Create code sample directory
- [ ] Create screenshot directory

### Phase 2: Code Creation

- [ ] Write example-1.bas (lowercase keywords, no indentation)
- [ ] Validate BASIC V2 syntax (no WHILE/DO/CASE)
- [ ] **MANDATORY: Run semantic validator (`python3 /scripts/validate-c64-basic.py example-1.bas`)**
- [ ] **MANDATORY: Fix all errors reported by validator before proceeding**
- [ ] Compile with petcat → example-1.prg (must succeed with exit code 0)
- [ ] Create example-2.bas if needed (repeat validator + petcat for each file)

**The semantic validator automatically checks:**
- Reserved variables (ST, TI, TI$ not used)
- GOSUB/GOTO targets exist
- No array re-dimensioning
- No duplicate line numbers
- FOR/NEXT matching
- Memory addresses in valid ranges
- Initialization issues

### Phase 3: Screenshot Capture

- [ ] Load example-1.prg in x64sc
- [ ] Capture screenshot (manual or automated)
- [ ] Save to correct location
- [ ] **CRITICAL: Use Read tool to VIEW screenshot**
- [ ] **CRITICAL: Describe what you see (sprites, text, colors)**
- [ ] **CRITICAL: Verify NO error messages (?SYNTAX, ?UNDEF'D, ?ILLEGAL)**
- [ ] **CRITICAL: Verify NOT blank screen**
- [ ] If errors found: fix code, recompile, recapture, re-verify
- [ ] Capture additional screenshots if needed (repeat verification for each)

### Phase 4: Lesson MDX Creation

- [ ] Create lesson-NNN.mdx
- [ ] Uppercase BASIC keywords in MDX (display format)
- [ ] Include code samples with explanations
- [ ] Add screenshots
- [ ] British English (except "program" for software)

### Phase 5: Validation

- [ ] Run lesson-validation skill
- [ ] Run curriculum-alignment-check
- [ ] Run screenshot-verification
- [ ] Run british-english-check
- [ ] Run voice-tone-check
- [ ] Fix any issues

### Phase 6: File Verification

- [ ] ls code-samples/.../lesson-NNN/ (all files present)
- [ ] ls website/public/images/.../lesson-NNN/ (all screenshots present)
- [ ] ls website/src/pages/.../lesson-NNN.mdx (lesson file present)

### Phase 7: Navigation Update

- [ ] Update tier-N.astro with new lesson
- [ ] Update phase-N.astro if new tier
- [ ] Update commodore-64.astro if new phase

---

## Quick Reference

### Compilation
```bash
petcat -w2 -o example-1.prg -- example-1.bas
```

### Screenshot (Automated)
```bash
x64sc -autostart example-1.prg -limitcycles 20000000 -VICIIdsize \
  -exitscreenshot /path/to/screenshot-1.png +sound
```

### Screenshot (Manual)
```bash
x64sc -autostart example-1.prg
# Press Alt+S to capture
```

### Semantic Validation
```bash
python3 /scripts/validate-c64-basic.py example-1.bas
```

### Common Memory Addresses
```basic
53280  REM border colour ($D020)
53281  REM background colour ($D021)
1024   REM screen memory start ($0400)
55296  REM colour memory start ($D800)
```

---

## Common Mistakes

**Mistake 1: Indented code**
- **Symptom:** petcat fails or produces wrong output
- **Fix:** Remove all indentation, line numbers flush left

**Mistake 2: Uppercase keywords in .bas**
- **Symptom:** petcat tokenization issues
- **Fix:** Use lowercase in .bas files

**Mistake 3: Blank screenshot**
- **Symptom:** Screenshot shows blank/crashed screen
- **Fix:** Check for runtime errors, verify code with manual run first

**Mistake 4: Using BASIC V7 commands**
- **Symptom:** "SYNTAX ERROR" when running
- **Fix:** Only use BASIC V2 commands (no WHILE/DO/CASE)

**Mistake 5: Screen codes vs PETSCII confusion**
- **Symptom:** Wrong characters on screen
- **Fix:** Use screen codes (0-63) for POKE to screen memory, PETSCII for PRINT

**Mistake 6: POKEing to ROM**
- **Symptom:** No effect or system crash
- **Fix:** Only POKE to writable memory ($0000-$9FFF, $C000-$CFFF, $D000-$DFFF)

---

## Platform-Specific Resources

**Essential docs:**
- `/docs/VIC-II-QUICK-REFERENCE.md` - Screen, sprites, colours
- `/docs/SID-QUICK-REFERENCE.md` - Sound synthesis
- `/docs/CIA-QUICK-REFERENCE.md` - Joystick, keyboard
- `/docs/PETSCII-AND-SCREEN-CODES.md` - Character codes
- `/docs/START-HERE.md` - Navigation to other references

**Avoid unless needed:**
- `/docs/VIC-II-REFERENCE.md` (90KB - full hardware specs)
- `/docs/6526-CIA-REFERENCE.md` (80KB - electrical specs)

---

## The Bottom Line

**C64 BASIC lessons require:**
1. Lowercase keywords in .bas files, NO indentation
2. petcat compilation to .prg
3. Semantic validation (memory addresses, BASIC V2 limits)
4. VICE x64sc screenshot capture
5. PETSCII vs screen code awareness
6. British English (except "program")

**Zero tolerance for:**
- Indented code
- Uncompiled .bas files (must have .prg)
- Unverified screenshots (blank screens, error messages)
- BASIC V7 commands in V2 code
- American spellings (except "program")

**Every C64 BASIC lesson must compile, run, and display expected output verified with screenshots.**
