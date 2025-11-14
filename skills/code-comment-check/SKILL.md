---
name: code-comment-check
description: Use when validating code sample comments - enforces adequate comment density, clarity, and learning-appropriate explanations for lesson code
---

# Code Comment Check

## Overview

This skill validates code sample comments to ensure adequate density and clarity for learning. Educational code requires more comments than production code - learners need explanations of WHY, not just WHAT. Checks comment density (1 comment per 2-3 lines), comment quality, and anti-patterns.

## When to Use

Use when:
- Creating new lesson code samples
- Reviewing existing lesson code for comment quality
- lesson-validation detects sparse comments
- Code seems under-commented

**Do NOT use for:**
- Production code (different standards)
- Very short examples (< 5 lines don't need heavy comments)
- Obvious code (PRINT "HELLO" doesn't need comment)

---

## Comment Density Standards

### Target Density by Code Length

**5-10 lines:** 1 comment per 2-3 lines
**11-20 lines:** 1 comment per 2 lines
**21+ lines:** 1 comment per 2 lines + section headers

**Example (Good density):**

```basic
10 REM initialize game state
20 LET SCORE=0
30 LET LIVES=3
40 REM display initial values
50 PRINT "SCORE:";SCORE
60 PRINT "LIVES:";LIVES
70 REM main game loop
80 REM (more code here)
```

**8 lines, 4 comments = 50% density ✓**

**Example (Too sparse):**

```basic
10 LET SCORE=0
20 LET LIVES=3
30 PRINT "SCORE:";SCORE
40 PRINT "LIVES:";LIVES
50 REM main loop
60 REM (more code here)
```

**6 lines, 1 comment = 16% density ✗**

---

## Checking Comment Density

### Step 1: Count Lines of Code

**Exclude:**
- Empty lines
- Comment-only lines

**Count:**
- Executable lines
- Data lines

```bash
# Count non-empty, non-comment lines in BASIC
grep -Ec "^[0-9]+ [^REM]" example-1.bas

# Count non-comment lines in assembly
grep -Ec "^    [A-Z]" example-1.asm
```

### Step 2: Count Comments

**BASIC:**
```bash
# Count REM statements
grep -c "REM" example-1.bas

# OR inline comments (;)
grep -c ";" example-1.bas
```

**Assembly:**
```bash
# Count semicolon comments
grep -c ";" example-1.asm
```

### Step 3: Calculate Density

```
Comment Density = (Comments / Lines of Code) × 100%

Target: 33-50% (1 comment per 2-3 lines)
Acceptable: 25-60%
Too sparse: < 25%
Too dense: > 60%
```

**Example calculation:**

```
20 lines of code
8 comments
Density = (8 / 20) × 100% = 40% ✓ Good
```

---

## Comment Quality Guidelines

### 1. Explain WHY, Not WHAT

**Bad (explains WHAT):**
```basic
100 LET X=5          REM set X to 5
```

**Good (explains WHY):**
```basic
100 LET X=5          REM sprite starting position
```

**Bad:**
```asm
    LDA #0           ; Load A with 0
```

**Good:**
```asm
    LDA #0           ; Clear accumulator for border colour
```

### 2. Section Headers for Long Code

**For 20+ line examples, use section comments:**

```basic
100 REM === INITIALIZATION ===
110 LET SCORE=0
120 LET LIVES=3
...
200 REM === MAIN GAME LOOP ===
210 REM check input
220 ...
```

```asm
; === SETUP ROUTINE ===
setup:
    LDA #0
    ...

; === MAIN LOOP ===
main_loop:
    JSR check_input
    ...
```

### 3. Explain Hardware Operations

**Always comment hardware access:**

```basic
100 POKE 53280,0     REM border colour black
110 POKE 53281,6     REM background colour blue
120 POKE 53269,255   REM enable all 8 sprites
```

```asm
    LDA #$00
    STA $D020        ; Border colour (VIC-II)
    STA $D021        ; Background colour (VIC-II)
```

### 4. Explain Magic Numbers

**Never leave unexplained numbers:**

**Bad:**
```basic
100 FOR I=1024 TO 2023
```

**Good:**
```basic
100 FOR I=1024 TO 2023   REM screen memory range ($0400-$07E7)
```

**Bad:**
```asm
    LDA #147
```

**Good:**
```asm
    LDA #147         ; PETSCII clear screen
```

### 5. Reference Memory Addresses

**Always show hex for POKE/PEEK:**

```basic
100 POKE 53280,0     REM border colour ($D020)
110 X=PEEK(56320)    REM joystick port 2 ($DC00)
```

### 6. Explain Algorithm Steps

**Multi-step operations need breakdown:**

```basic
100 REM convert score to string
110 S$=STR$(SCORE)
120 REM remove leading space
130 IF LEFT$(S$,1)=" " THEN S$=RIGHT$(S$,LEN(S$)-1)
140 REM pad with zeros
150 S$=STRING$(5-LEN(S$),"0")+S$
```

---

## Comment Anti-Patterns

### 1. Commented-Out Code

**Anti-pattern:**
```basic
100 LET X=5
110 REM LET X=10
120 PRINT X
```

**Fix:** Remove commented-out code (not for learning)

### 2. TODO Markers

**Anti-pattern:**
```basic
100 REM TODO: add sound here
110 PRINT "HELLO"
```

**Fix:** Complete code or remove TODO (lessons should be finished)

### 3. Obvious Comments

**Anti-pattern:**
```basic
100 PRINT "HELLO"    REM print hello
```

**Fix:** Remove obvious comment (or add WHY context if needed)

### 4. Wrong Comments

**Anti-pattern:**
```basic
100 LET X=10         REM sprite X position
110 LET Y=20         REM sprite X position  ← WRONG! Should be Y
```

**Fix:** Update comment to match code

### 5. Excessive Density

**Anti-pattern:**
```basic
100 REM initialize variable X to starting value
110 LET X=5          REM set X to 5
```

**Fix:** Consolidate comments, remove redundancy

---

## Platform-Specific Comment Styles

### C64 BASIC

**REM statements:**
```basic
10 REM clear screen
20 PRINT CHR$(147)
```

**Inline (if supported by display):**
```basic
10 PRINT CHR$(147)   : REM clear screen
```

### NES 6502 Assembly

**Semicolon comments:**
```asm
    LDA #$00         ; Clear accumulator
    STA $2000        ; PPUCTRL (disable NMI)
```

### ZX Spectrum BASIC

**REM statements:**
```basic
10 REM initialize
20 LET X=5
```

### Amiga 68000 Assembly

**Semicolon comments:**
```asm
    MOVE.L #0,D0     ; Clear D0
    LEA $DFF000,A5   ; Custom chip base
```

---

## Validation Checklist

**For each code sample:**

- [ ] Comment density 25-60%
- [ ] All hardware operations explained
- [ ] All magic numbers explained
- [ ] Memory addresses show hex equivalent
- [ ] WHY explained, not just WHAT
- [ ] Section headers for 20+ lines
- [ ] No commented-out code
- [ ] No TODO markers
- [ ] No wrong/outdated comments
- [ ] British English in comments

---

## Automated Checks

### Check Density

```bash
#!/bin/bash
# check-comment-density.sh

FILE=$1

# Count lines (excluding empties and pure comments)
LINES=$(grep -Ec "^[0-9]+ [^REM]" "$FILE")

# Count comments
COMMENTS=$(grep -c "REM" "$FILE")

# Calculate density
DENSITY=$((COMMENTS * 100 / LINES))

echo "Lines: $LINES"
echo "Comments: $COMMENTS"
echo "Density: ${DENSITY}%"

if [ "$DENSITY" -lt 25 ]; then
  echo "❌ Too sparse (< 25%)"
  exit 1
elif [ "$DENSITY" -gt 60 ]; then
  echo "⚠ Too dense (> 60%)"
  exit 1
else
  echo "✓ Good density (25-60%)"
  exit 0
fi
```

### Check for Anti-Patterns

```bash
# Check for commented-out code (BASIC)
grep -n "^[0-9]+ REM [A-Z]" example-1.bas

# Check for TODO markers
grep -in "TODO\|FIXME\|HACK" example-1.bas

# Check for wrong comments (assembly)
# (requires manual review)
```

---

## Integration with Other Skills

**This skill is used by:**

1. **lesson-validation** - Checks comment density as part of validation
2. **Platform-specific skills** - Reference for code sample standards

**After fixing comments:**

Run lesson-validation to verify overall lesson quality.

---

## Quick Reference

### Target Densities
```
5-10 lines:  1 comment / 2-3 lines (33-50%)
11-20 lines: 1 comment / 2 lines (50%)
21+ lines:   1 comment / 2 lines + section headers
```

### Good Comment Practices
- Explain WHY, not WHAT
- Comment all hardware operations
- Explain all magic numbers
- Show hex for memory addresses
- Section headers for long code
- British English

### Anti-Patterns to Avoid
- Commented-out code
- TODO markers
- Obvious comments
- Wrong/outdated comments
- Excessive density (> 60%)

### Check Density (Quick)
```bash
# BASIC
LINES=$(grep -Ec "^[0-9]+ [^REM]" file.bas)
COMMENTS=$(grep -c "REM" file.bas)
echo $((COMMENTS * 100 / LINES))%

# Assembly
LINES=$(grep -Ec "^    [A-Z]" file.asm)
COMMENTS=$(grep -c ";" file.asm)
echo $((COMMENTS * 100 / LINES))%
```

---

## The Bottom Line

**Code comment check ensures learning-appropriate comments:**
1. Target density: 25-60% (1 comment per 2-3 lines)
2. Explain WHY, not just WHAT
3. All hardware operations commented
4. All magic numbers explained
5. Section headers for long code (20+ lines)
6. British English in comments

**Zero tolerance for:**
- Sparse comments (< 25% density)
- Commented-out code (confusing)
- TODO markers (incomplete work)
- Wrong/outdated comments (misleading)
- Unexplained hardware/magic numbers (learners lost)

**Educational code requires more comments than production code. Every line should teach, not just execute.**
