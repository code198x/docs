---
name: c64-basic-lesson-creation
description: Use when creating or editing C64 BASIC lessons - provides platform-specific compilation, validation, and screenshot capture for Phase 3 of the content creation workflow
---

# C64 BASIC Lesson Creation

**Role:** Technical execution for Phase 3 (Validation) of the Content Creation Workflow.

**Prerequisite:** Read `/docs/CONTENT-CREATION-WORKFLOW.md` first. This skill provides C64-specific technical details, not the full workflow.

---

## When to Use

Use this skill during **Phase 3 (Validation)** when:
- Compiling C64 BASIC code examples
- Capturing screenshots with VICE x64sc
- Validating memory addresses and BASIC syntax
- Checking for C64-specific pitfalls

**Do NOT use for:**
- C64 6510 Assembly lessons (use `6510-lesson-creation` skill)
- Other platforms (use platform-specific skills)

---

## C64 BASIC V2 Language Rules

### 1. NO Indentation
```basic
✓ CORRECT:
10 print "hello"
20 for i=1 to 10
30 print i
40 next i

✗ WRONG:
10 print "hello"
20 for i=1 to 10
30   print i    ← NO INDENTATION
40 next i
```

### 2. Lowercase Keywords in .bas Files
```basic
✓ CORRECT (.bas file): 10 print "hello"
✗ WRONG (.bas file): 10 PRINT "hello"
```
Display UPPERCASE in MDX lesson content for readability.

### 3. Reserved Variables (NEVER USE)
- `ST` - I/O status (read-only, causes SYNTAX ERROR if written)
- `TI` - Jiffy clock (conflicts with game timing)
- `TI$` - Time string

**Use instead:** `GS` (game state), `CT` (timer), `SC` (score), `HP` (health)

### 4. Two-Character Variable Significance
Only first TWO characters are significant:
- `f1x` and `f1y` both become `f1` (collision!)
- Use distinct names: `fx`/`fy`, `gx`/`gy`, `px`/`py`

### 5. BASIC V2 Limitations
**HAS:** `AND`, `OR`, `LEFT$`, `RIGHT$`, `MID$`, `LEN`, `PEEK`, `POKE`, `SYS`

**DOES NOT HAVE:** `WHILE`/`WEND`, `DO`/`LOOP`, `CASE`/`SWITCH`, `ELSE` on same line as `IF`

---

## Phase 3: Validation (Technical Details)

### Step 3.1: Semantic Validation (MANDATORY)

**Run BEFORE petcat - catches errors petcat cannot detect!**

```bash
cd /code-samples/commodore-64/phase-X/tier-Y/lesson-NNN/

python3 /scripts/validate-c64-basic.py example-1.bas
```

**Semantic checks include:**
- ✅ Reserved variables (ST, TI, TI$ not used)
- ✅ GOSUB/GOTO targets exist
- ✅ No array re-dimensioning
- ✅ No duplicate line numbers
- ✅ FOR/NEXT matching
- ✅ POKE addresses in valid ranges
- ✅ VIC-II, SID, CIA register validation
- ✅ BASIC V2 compatibility

**If errors found:** Fix before proceeding to petcat.

### Step 3.2: Compilation (petcat)

```bash
# Compile BASIC to PRG
petcat -w2 -o example-1.prg -- example-1.bas

# Verify success
echo $?  # Must be 0
```

**Flags:**
- `-w2` = BASIC V2 (C64)
- `-o example-1.prg` = Output file
- `-- example-1.bas` = Input file

### Step 3.3: Screenshot Capture

**Manual capture (interactive programs):**
```bash
x64sc -autostart example-1.prg
# Press Alt+S to capture, save to:
# /website/public/images/commodore-64/phase-X/tier-Y/lesson-NNN/screenshot-1.png
```

**Automated capture (static output):**
```bash
x64sc -autostart example-1.prg \
  -limitcycles 20000000 \
  -VICIIdsize \
  -exitscreenshot /website/public/images/commodore-64/phase-X/tier-Y/lesson-NNN/screenshot-1.png \
  +sound
```

### Step 3.4: Screenshot Verification (MANDATORY)

**Use Read tool to VIEW every screenshot and provide evidence:**

```
✅ CORRECT: "Read screenshot-1.png - shows green platforms, red player sprite
   at Y=100, status text 'HP: 20/20'. NO error messages visible."

❌ WRONG: "Screenshot verified ✅" (too vague)
❌ WRONG: "Screenshot captured successfully" (didn't verify content)
```

**Check for error messages (automatic failure):**
- `?SYNTAX ERROR IN [line]` → Fix syntax
- `?UNDEF'D STATEMENT ERROR IN [line]` → Missing GOSUB target
- `?ILLEGAL QUANTITY ERROR IN [line]` → Value out of range
- Blank screen → Initialization bug or crash

**If ANY error found:** Fix code → Recompile → Recapture → Re-verify

### Step 3.5: Platform-Specific Checks

**GOSUB Target Verification:**
```bash
# Find all GOSUB calls
grep -i "gosub" example-1.bas

# For each target, verify line exists
grep "^[target] " example-1.bas
```

**Reserved Variable Check:**
```bash
grep -iE '\<(st|ti|ti\$)\>' example-1.bas
# Should return nothing
```

**Indentation Check:**
```bash
# Lines should start with number, no leading spaces
grep "^ " example-1.bas
# Should return nothing
```

---

## Memory Map Validation

| Range | Purpose | Write | Read |
|-------|---------|-------|------|
| `$0400-$07E7` (1024-2023) | Screen RAM | ✓ | ✓ |
| `$D800-$DBE7` (55296-56295) | Colour RAM | ✓ | ✓ |
| `$D000-$D02E` (53248-53294) | VIC-II | ✓ | ✓ |
| `$D400-$D41C` (54272-54300) | SID | ✓ | ✓ |
| `$DC00-$DC0F` (56320-56335) | CIA #1 | ✓ | ✓ |
| `$A000-$BFFF` | BASIC ROM | ✗ | ✓ |
| `$E000-$FFFF` | KERNAL ROM | ✗ | ✓ |

---

## Common VIC-II Operations

| Address | Decimal | Purpose |
|---------|---------|---------|
| $D020 | 53280 | Border colour |
| $D021 | 53281 | Background colour |
| $D000-$D010 | 53248-53264 | Sprite X/Y positions |
| $D015 | 53269 | Sprite enable |
| $D027-$D02E | 53287-53294 | Sprite colours |

**Colour values:** 0-15 only (0=black, 1=white, 2=red, etc.)

---

## PETSCII vs Screen Codes

**PETSCII** (for `PRINT`, `CHR$`):
- Clear screen: `CHR$(147)`
- Colours: `CHR$(144-159)`
- Reverse on: `CHR$(18)`

**Screen codes** (for `POKE` to screen memory):
- Different mapping than PETSCII
- Space = 0 (not 32)
- Letters: A=1, B=2, ..., Z=26

---

## Common Pitfalls

### 1. Initialization Bug
```basic
❌ WRONG:
100 CX=0:LX=0    ← Both zero, first draw skipped

✅ CORRECT:
100 CX=0:LX=-999   ← Forces first screen draw
```

### 2. Sprite X > 255
```basic
❌ WRONG:
100 X=300
110 POKE 53248,X    ← Wraps to 44!

✅ CORRECT:
100 X=300
110 POKE 53248,X AND 255
120 IF X>255 THEN POKE 53264,PEEK(53264)OR 1:GOTO 140
130 POKE 53264,PEEK(53264)AND 254
140 REM SPRITE NOW AT X=300
```

### 3. Clearing Screen in Loop
```basic
❌ WRONG (flickers):
100 PRINT CHR$(147)
110 PRINT "SCORE:";SC
120 GOTO 100

✅ CORRECT:
100 PRINT CHR$(147)
110 POKE 214,0:PRINT
120 PRINT "SCORE:";SC
130 GOTO 110
```

### 4. Forgetting to Restore Registers
```basic
❌ WRONG:
100 POKE 53280,0
500 END  ← Border stays black

✅ CORRECT:
100 B=PEEK(53280)
110 POKE 53280,0
500 POKE 53280,B:END
```

---

## Required Files

For lesson NNN in Phase X, Tier Y:

| File | Location |
|------|----------|
| Lesson MDX | `/website/src/pages/commodore-64/phase-X/tier-Y/lesson-NNN.mdx` |
| Code (.bas) | `/code-samples/commodore-64/phase-X/tier-Y/lesson-NNN/example-1.bas` |
| Compiled (.prg) | `/code-samples/commodore-64/phase-X/tier-Y/lesson-NNN/example-1.prg` |
| Screenshot | `/website/public/images/commodore-64/phase-X/tier-Y/lesson-NNN/screenshot-1.png` |

---

## Quick Reference Commands

```bash
# Semantic validation
python3 /scripts/validate-c64-basic.py example-1.bas

# Compile
petcat -w2 -o example-1.prg -- example-1.bas

# Screenshot (automated)
x64sc -autostart example-1.prg -limitcycles 20000000 -VICIIdsize \
  -exitscreenshot screenshot-1.png +sound

# Screenshot (manual)
x64sc -autostart example-1.prg
# Press Alt+S

# Check for reserved variables
grep -iE '\<(st|ti|ti\$)\>' example-1.bas

# Check for indentation
grep "^ " example-1.bas
```

---

## Platform-Specific Resources

**Quick references** (in `/docs/platforms/commodore-64/`):
- `hardware/VIC-II-QUICK-REFERENCE.md` - Screen, sprites, colours
- `hardware/CIA-QUICK-REFERENCE.md` - Joystick, keyboard
- `hardware/PETSCII-AND-SCREEN-CODES.md` - Character codes

**Common errors:**
- `basic-v2/C64-COMMON-ERRORS.md` - BASIC pitfalls
- `advanced/6510-COMMON-ERRORS.md` - Assembly pitfalls

---

## The Bottom Line

**This skill provides:** Compilation, validation, and screenshot capture for C64 BASIC lessons.

**The main workflow provides:** Planning, creation, integration, and publication steps.

**Zero tolerance for:**
- Unverified screenshots (blank screens, error messages)
- Uncompiled code (must have .prg)
- Reserved variables (ST, TI, TI$)
- Indented code
