# Agents Overview

**Version:** 1.0
**Date:** 2025-11-04

---

## What Are Agents?

Agents are autonomous subagents invoked via the Task tool that execute complete workflows. Unlike skills (which provide guidance), agents make implementation decisions and complete multi-step tasks without user intervention.

**Think:** Skills = recipe book, Agents = chef

---

## Available Agents

### Production Agents (P1 Priority)

**1. lesson-creation-agent**
- **Purpose:** Create complete lesson from curriculum spec
- **Complexity:** High
- **Phases:** Two-phase (code creation → manual screenshots → lesson completion)
- **Use when:** Creating new lesson from curriculum specification
- **Doc:** [lesson-creation-agent.md](lesson-creation-agent.md)

**2. navigation-update-agent**
- **Purpose:** Update navigation files across all levels
- **Complexity:** Medium
- **Use when:** New lesson added, need to update tier/phase/platform indexes
- **Doc:** [navigation-update-agent.md](navigation-update-agent.md)

**3. curriculum-planning-agent**
- **Purpose:** Generate phase curriculum for new platform
- **Complexity:** High
- **Use when:** Expanding to new platform, need phase curriculum document
- **Doc:** [curriculum-planning-agent.md](curriculum-planning-agent.md)

### Content Expansion Agents (P2 Priority)

**4. vault-entry-agent (RECURSIVE)**
- **Purpose:** Create Vault entries with recursive cross-reference management
- **Complexity:** High
- **Recursion:** Creates stub entries for missing cross-references, bidirectional linking
- **Use when:** Creating Vault entry with potentially missing cross-references
- **Doc:** [vault-entry-agent.md](vault-entry-agent.md)

**5. pattern-extraction-agent**
- **Purpose:** Scan lessons, extract reusable patterns, generate pattern documentation
- **Complexity:** High
- **Use when:** Systematically documenting patterns from completed lessons
- **Doc:** [pattern-extraction-agent.md](pattern-extraction-agent.md)

**6. concept-mapping-agent**
- **Purpose:** Build CONCEPT-CROSS-REFERENCE.md from all platform curricula
- **Complexity:** Medium
- **Use when:** New platform added, need to update concept cross-reference
- **Doc:** [concept-mapping-agent.md](concept-mapping-agent.md)

**7. curriculum-audit-agent**
- **Purpose:** Comprehensive curriculum health check (missing files, broken links, validation)
- **Complexity:** Medium
- **Use when:** Regular maintenance, before releases, suspected structural issues
- **Doc:** [curriculum-audit-agent.md](curriculum-audit-agent.md)

---

## When to Use Each Agent

### Lesson Creation Workflow

**Scenario:** Creating a new lesson from curriculum specification

**Agent sequence:**
1. **curriculum-planning-agent** (if curriculum doesn't exist yet)
   - Generates complete phase curriculum document
   - Output: `/docs/{platform}/PHASE-{N}-CURRICULUM.md`

2. **lesson-creation-agent Phase 1**
   - Creates and compiles code
   - Stops with screenshot instructions
   - Output: Code files in `/code-samples/...`

3. **Manual screenshot capture** (you)
   - Load compiled code in emulator
   - Capture screenshots
   - Save to `/website/public/images/...`

4. **lesson-creation-agent Phase 2**
   - Verifies screenshots
   - Creates lesson MDX
   - Runs all validation skills
   - Output: Lesson file in `/website/src/pages/...`

5. **navigation-update-agent**
   - Updates tier/phase/platform indexes
   - Output: Updated index files

**Note:** lesson-creation-agent Phase 2 can optionally call navigation-update-agent, or you can run it separately.

---

### Curriculum Expansion Workflow

**Scenario:** Adding NES platform, need Phase 1 curriculum

**Agent sequence:**
1. **curriculum-planning-agent**
   - Input: NES platform, Phase 1, 512 lesson budget
   - Analyzes C64/ZX Phase 1 curricula
   - Generates NES-appropriate game selections
   - Output: `/docs/nintendo-entertainment-system/PHASE-1-CURRICULUM.md`

2. Review and adjust curriculum manually (if needed)

3. **lesson-creation-agent** (for each lesson in curriculum)
   - Creates lessons one by one following curriculum

---

### Navigation-Only Update

**Scenario:** Lesson already created, just need navigation update

**Agent:**
- **navigation-update-agent** only
- Provide lesson details
- Agent updates all required indexes

---

## Agent vs Manual Decision Tree

```
Need to create a lesson?
├─ Curriculum exists?
│  ├─ YES → lesson-creation-agent
│  └─ NO → curriculum-planning-agent first, then lesson-creation-agent
│
Need to update navigation only?
└─ navigation-update-agent

Need phase curriculum for new platform?
└─ curriculum-planning-agent
```

---

## Agent Invocation Patterns

### Quick Reference

**lesson-creation-agent Phase 1:**
```javascript
{
  subagent_type: "general-purpose",
  description: "Create lesson code and compile",
  prompt: "LESSON SPECIFICATION: Platform/Phase/Tier/Lesson/Curriculum-path..."
}
```

**lesson-creation-agent Phase 2:**
```javascript
{
  subagent_type: "general-purpose",
  description: "Complete lesson with validation",
  prompt: "CONTEXT: Phase 1 complete, screenshots captured. TASK: Verify/Create/Validate..."
}
```

**navigation-update-agent:**
```javascript
{
  subagent_type: "general-purpose",
  description: "Update navigation for new lesson",
  prompt: "NEW LESSON DETAILS: Platform/Phase/Tier/Lesson/Title/Description/Status..."
}
```

**curriculum-planning-agent:**
```javascript
{
  subagent_type: "general-purpose",
  description: "Generate phase curriculum for platform",
  prompt: "TARGET PLATFORM: Platform/Phase/Budget/Hardware. REFERENCES: C64/ZX..."
}
```

See individual agent documents for complete invocation patterns.

---

## Skills Agents Use

All agents use validation skills to ensure quality:

### lesson-creation-agent uses:
- lesson-creation-workflow
- {platform}-lesson-creation
- lesson-validation
- screenshot-verification
- curriculum-alignment-check
- voice-tone-check
- british-english-check
- strategic-alignment-check

### navigation-update-agent uses:
- (No skills - standalone file manipulation)

### curriculum-planning-agent uses:
- strategic-alignment-check (validates game selections)

---

## Agent Autonomy Levels

**High Autonomy (No User Input):**
- curriculum-planning-agent (generates complete document)
- navigation-update-agent (updates all files)

**Medium Autonomy (Manual Step Required):**
- lesson-creation-agent (requires manual screenshot capture between phases)

**All agents:**
- Report completion with details
- Stop on errors with specific diagnostics
- Do not ask questions mid-execution

---

## Error Handling

All agents follow this pattern:

1. **Detect error** at specific step
2. **Stop immediately** (do not continue)
3. **Report error** with step number and details
4. **List completed steps** (what succeeded)
5. **List failed steps** (what failed and why)
6. **Suggest fix** (what to do next)

**Example error report:**
```
AGENT FAILED at Step 3 (code compilation)

COMPLETED:
✓ Read curriculum spec
✓ Created code files

FAILED:
✗ Compilation error in example-2.bas:
  Line 25: ?SYNTAX ERROR

SUGGESTED FIX:
- Fix syntax error in example-2.bas line 25
- Re-invoke agent from Step 3 (compilation)
```

---

## Testing Agents

**Before production use, test each agent with:**

**lesson-creation-agent:**
- Simple lesson (5-10 lines, 1 screenshot)
- Medium lesson (20-30 lines, 2 screenshots)
- Complex lesson (40+ lines, 3+ screenshots)
- Lesson with intentional error (verify error handling)

**navigation-update-agent:**
- First lesson in existing tier
- First lesson in new tier
- First lesson in new phase
- Duplicate lesson number (verify error handling)

**curriculum-planning-agent:**
- New platform with similar capabilities (NES similar to C64)
- New platform with different capabilities (Amiga vs C64)
- Platform with unique constraints (Atari 2600)

---

## Agent Development Status

| Agent | Priority | Status | Tested | Production Ready |
|-------|----------|--------|--------|------------------|
| lesson-creation-agent | P1 | ✅ Spec complete | ⏳ Not tested | ❌ No |
| navigation-update-agent | P1 | ✅ Spec complete | ⏳ Not tested | ❌ No |
| curriculum-planning-agent | P1 | ✅ Spec complete | ⏳ Not tested | ❌ No |
| vault-entry-agent (RECURSIVE) | P2 | ✅ Spec complete | ⏳ Not tested | ❌ No |
| pattern-extraction-agent | P2 | ✅ Spec complete | ⏳ Not tested | ❌ No |
| concept-mapping-agent | P2 | ✅ Spec complete | ⏳ Not tested | ❌ No |
| curriculum-audit-agent | P2 | ✅ Spec complete | ⏳ Not tested | ❌ No |

**Next steps:**
1. Test P1 agents with sample inputs (lesson specs, navigation updates, curriculum generation)
2. Test P2 agents with real data (vault entries, pattern extraction, concept mapping, audit)
3. Refine based on test results
4. Mark as production-ready after successful tests

---

## The Bottom Line

**P1 Agents (Production workflow):**
- lesson-creation-agent: Complete lesson from spec (with manual screenshot step)
- navigation-update-agent: Update all navigation files
- curriculum-planning-agent: Generate phase curricula for new platforms

**P2 Agents (Content expansion and maintenance):**
- vault-entry-agent: Create Vault entries with recursive cross-reference management
- pattern-extraction-agent: Extract patterns from lessons, generate documentation
- concept-mapping-agent: Build CONCEPT-CROSS-REFERENCE.md from curricula
- curriculum-audit-agent: Comprehensive health check (missing files, broken links, validation)

**All agents:**
- Make implementation decisions autonomously
- Follow validation skills rigorously
- Report errors clearly
- Stop on failures (no partial updates)

**Use agents to save time on repetitive, multi-step tasks while maintaining quality through systematic validation.**
