---
name: verification-before-completion
description: Use when completing ANY task - requires running verification commands and confirming output before making success claims. Evidence before assertions, always.
---

# Verification Before Completion

**The Golden Rule: Evidence before assertions. Always.**

## When to Use

Use this skill when:
- Claiming a task is complete
- Reporting that code compiles
- Stating that tests pass
- Asserting that a bug is fixed
- Confirming that output is correct
- Verifying that files were created
- Any situation where you're making a success claim

**In other words:** Use this skill before claiming ANYTHING is done.

---

## The Problem

**Anti-pattern (what NOT to do):**
```
❌ "Compilation successful ✅"
❌ "Screenshot verified ✅"
❌ "All tests passing ✅"
❌ "Fixed the bug ✅"
❌ "Files created successfully ✅"
```

**Why wrong?** No evidence. These are assertions without proof.

---

## The Solution

**Before claiming success, you MUST:**

### 1. Run the Verification Command

Execute the actual command/tool that proves the claim:
- Compilation? Run the compiler and capture output
- Tests? Run the test suite and show results
- Screenshot? Use Read tool to view the image
- Files created? Use ls to list them
- Bug fixed? Test the specific scenario that was broken

### 2. Check the Output

Don't just run the command - **verify the output**:
- Exit code = 0 (success)?
- No error messages?
- Expected results present?
- No unexpected warnings?

### 3. Describe What You Saw

Provide specific details, not vague confirmations:
```
✅ "Compiled with petcat - exit code 0, no error messages, generated example-1.prg (2.3KB)"

✅ "Ran tests - 15/15 passed, output shows all assertions succeeded, execution time 2.4s"

✅ "Used Read tool on screenshot - shows green platforms, red player sprite at Y=150, status text 'HP: 20/20', NO error messages visible"

✅ "Listed files with ls - found example-1.bas (1.8KB), example-1.prg (1.4KB), screenshot-1.png (2.1KB)"

✅ "Tested bug scenario - player no longer falls through floor, Y coordinate correctly clamped to 200"
```

### 4. Only Then Claim Success

After providing evidence, you can make the claim:
```
✅ "Compilation successful - exit code 0, PRG file generated"
✅ "Screenshot verified - shows working gameplay, no errors"
✅ "All tests passing - 15/15 passed in 2.4s"
✅ "Bug fixed - floor collision now working correctly"
```

---

## Examples

### Example 1: Code Compilation

**❌ WRONG:**
```
Agent: "Compiled the code successfully ✅"
```

**✅ CORRECT:**
```
Agent: "Running petcat compilation..."
[Uses Bash tool: petcat -w2 -o example-1.prg -- example-1.bas]
Agent: "Compilation output shows exit code 0, no errors. Generated example-1.prg (2.3KB). Compilation successful ✅"
```

### Example 2: Screenshot Verification

**❌ WRONG:**
```
Agent: "Screenshot captured and verified ✅"
```

**✅ CORRECT:**
```
Agent: "Captured screenshot, now verifying..."
[Uses Read tool: Read("screenshot-1.png")]
Agent: "Read screenshot - shows title screen 'CRYSTAL CAVERNS', menu options 1-3 visible, blue background with white text. NO error messages present. Screenshot verified ✅"
```

### Example 3: Test Results

**❌ WRONG:**
```
Agent: "All tests passing ✅"
```

**✅ CORRECT:**
```
Agent: "Running test suite..."
[Uses Bash tool: npm test]
Agent: "Test output shows 15 tests, 15 passed, 0 failed. Execution time 2.4s. All assertions succeeded. All tests passing ✅"
```

### Example 4: Bug Fix

**❌ WRONG:**
```
Agent: "Fixed the bug ✅"
```

**✅ CORRECT:**
```
Agent: "Testing the bug scenario..."
[Uses Bash tool: x64sc -autostart buggy-program.prg]
[Uses Read tool to check screenshot]
Agent: "Tested scenario - player sprite now stays at Y=200 when landing on platform. Previously fell through to Y=255. Screenshot shows player standing on green platform. Bug fixed ✅"
```

### Example 5: File Creation

**❌ WRONG:**
```
Agent: "Files created successfully ✅"
```

**✅ CORRECT:**
```
Agent: "Verifying files created..."
[Uses Bash tool: ls -lh lesson-033/]
Agent: "Listed directory - found example-1.bas (1.8KB), example-1.prg (1.4KB), screenshot-1.png (2.1KB), lesson-033.mdx (15KB). All required files present. Files created successfully ✅"
```

---

## Verification Methods by Claim Type

| Claim Type | Verification Method | Evidence Required |
|------------|-------------------|-------------------|
| "Code compiles" | Run compiler | Exit code 0, no errors, output file exists |
| "Tests pass" | Run test suite | N/N passed, 0 failed, specific test names |
| "Screenshot correct" | Read tool | Describe visible elements, confirm no errors |
| "Files created" | ls command | List files with sizes, confirm all present |
| "Bug fixed" | Test bug scenario | Describe old behavior vs new behavior |
| "Output correct" | Read/view output | Describe specific output contents |
| "Performance improved" | Benchmark/measure | Show before/after numbers with units |
| "Links work" | Click/test links | Report which links tested, where they go |

---

## Red Flags (You're About To Fail)

If you catch yourself about to say these WITHOUT evidence, STOP:

- "Successfully completed ✅"
- "All checks passed ✅"
- "Verified and working ✅"
- "Everything looks good ✅"
- "No issues found ✅"
- "Ready to proceed ✅"

**These are empty claims without proof.**

---

## The Verification Loop

```
1. Make a claim → 2. Provide evidence → 3. Confirm success

If evidence shows failure:
  → Fix the issue
  → Return to step 1
  → Repeat until evidence confirms success
```

**Never skip the evidence step.**

---

## Integration with Other Skills

This skill complements:
- **lesson-creation** - Verify screenshots, code compilation
- **testing** - Verify test results before claiming pass
- **debugging** - Verify bug is actually fixed
- **deployment** - Verify deployment succeeded
- **code-review** - Verify review checklist items

**Use this skill at the END of any other skill that makes success claims.**

---

## Summary

**Before claiming any task is complete:**

1. ☐ Run the verification command/tool
2. ☐ Check the output (exit codes, error messages)
3. ☐ Describe what you saw (specific details)
4. ☐ Only then make the success claim

**Remember:** Evidence before assertions. Always.

**Not acceptable:** "Verified ✅" without proof
**Acceptable:** "Ran [command], saw [specific results], therefore verified ✅"
