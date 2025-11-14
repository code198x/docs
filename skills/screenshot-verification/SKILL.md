---
name: screenshot-verification
description: Use when verifying screenshots match lesson expectations - uses READ tool to systematically check for expected output, error messages, blank screens, and content accuracy before lesson publication
---

# Screenshot Verification

## Overview

Screenshots must show working program output that matches lesson claims. Simply checking "file exists" is insufficient - you must VIEW the screenshot and verify content systematically.

## When to Use

Use when:
- Validating new lesson screenshots
- Debugging screenshot issues
- Verifying screenshot shows expected output
- Checking for error messages or blank screens

**Never approve screenshot without viewing it with READ tool.**

## Verification Checklist

**Use TodoWrite to track:**

### 1. File Existence
```bash
ls -la website/public/images/{platform}/phase-{N}/tier-{N}/lesson-{NNN}/*.png
```

**Verify:** All expected screenshots present (example-1.png, example-2.png, etc.)

### 2. View Screenshot
**MUST use READ tool:**
```
Use READ tool on screenshot file path
```

**Do NOT:**
- Assume screenshot is correct without viewing
- Say "screenshot exists" without describing content
- Skip viewing because "confident" screenshot is correct

### 3. Systematic Content Check

For EACH screenshot, verify:

**a) No Error Messages**
- [ ] No "?SYNTAX ERROR"
- [ ] No "?ILLEGAL QUANTITY ERROR"
- [ ] No "?OUT OF MEMORY ERROR"
- [ ] No "?UNDEF'D STATEMENT ERROR"
- [ ] No other BASIC/assembly errors visible

**b) Not Blank/Black**
- [ ] Screen shows actual output
- [ ] Not just black screen
- [ ] Not stuck at prompt
- [ ] Program has executed

**c) Expected Output Present**
Read lesson description of what screenshot should show.
Check screenshot contains:
- [ ] Text claimed in lesson
- [ ] Graphics/sprites claimed
- [ ] Colors claimed
- [ ] UI elements claimed

**d) Code-Screenshot Match**
- [ ] Output matches what code would produce
- [ ] Values/calculations correct
- [ ] Sequence matches code logic

### 4. Platform-Specific Elements

**C64:**
- [ ] Border color (if mentioned)
- [ ] Background color (if mentioned)
- [ ] Text color and position
- [ ] Sprites (if applicable)
- [ ] READY prompt (if appropriate)

**ZX Spectrum:**
- [ ] Attribute colors correct
- [ ] No attribute clash (unless intentional)
- [ ] BASIC listing visible (if showing code)
- [ ] Copyright message if boot screen

**NES:**
- [ ] Tiles rendering correctly
- [ ] Sprites visible
- [ ] Background layers
- [ ] Status displays

**Amiga:**
- [ ] Workbench elements (if applicable)
- [ ] Colors/palette
- [ ] Graphics quality
- [ ] Text rendering

## Verification Report Template

```
SCREENSHOT VERIFICATION: lesson-{NNN}

File: {filename}
Lesson Claim: "{what lesson says screenshot shows}"

1. File Exists: [YES/NO]

2. Content Description:
   [Describe what screenshot actually shows]

3. Error Check: [PASS/FAIL]
   - Error messages visible: [YES/NO]
   - If YES: [list errors]

4. Expected Output: [PASS/FAIL]
   - Element 1: [present/missing] - [description]
   - Element 2: [present/missing] - [description]
   - (list all claimed elements)

5. Code Match: [PASS/FAIL]
   - Output matches code behavior: [YES/NO]
   - If NO: [explain discrepancy]

VERDICT: [ACCEPTABLE / NEEDS REPLACEMENT]
Reason: [explanation]
```

## Common Mistakes

**Mistake 1:** "Screenshot exists"
- **Fix:** Use READ tool. Describe what's shown.

**Mistake 2:** "Looks good"
- **Fix:** Check systematically against lesson claims.

**Mistake 3:** Missing error messages
- **Fix:** Explicitly check for "?ERROR" text.

**Mistake 4:** Assuming code works
- **Fix:** Verify output matches what code would produce.

**Mistake 5:** Not comparing to lesson claims
- **Fix:** Read lesson claim. Check each element present.

## Red Flags - Skipping Verification

If you:
- Approve screenshot without viewing
- Say "exists" without describing content
- Don't check for errors
- Skip because "confident"
- Don't compare to lesson claims

**STOP. Use READ tool. Check systematically.**

## Quick Reference

```
# View screenshot
Use READ tool on file path

# Systematic check:
1. No error messages?
2. Not blank/black?
3. Shows claimed output?
4. Matches code behavior?
5. Platform elements correct?

# Report findings with evidence
```

## Example Verification

**Good verification:**
```
SCREENSHOT VERIFICATION: lesson-007/example-1.png

Lesson Claim: "Interactive colour selector, border changes"

Content: Screenshot shows C64 with blue border, text "TRY DIFFERENT COLOURS:", prompt "COLOUR (0-15)?", READY prompt visible.

Error Check: PASS - No error messages visible
Expected Output: PASS
  - Blue border: PRESENT
  - Input prompt: PRESENT
  - READY prompt: PRESENT
Code Match: PASS - POKE 53280 would set border color

VERDICT: ACCEPTABLE
```

**Bad verification (don't do this):**
```
Screenshot exists and looks fine.
```

## The Bottom Line

**View every screenshot. Check systematically. Report evidence.**

"Exists" ≠ "correct." Use READ tool always.
