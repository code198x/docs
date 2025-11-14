# Lesson Adaptation Agent

**Type**: Agent (Autonomous execution)
**Priority**: P3 (Future)
**Status**: Specification
**Complexity**: Very High

---

## Purpose

Adapts existing lesson from one platform to another (e.g., C64 → NES), accounting for hardware differences, instruction set changes, and platform-specific constraints. Not a simple translation - requires understanding lesson concept and reimplementing appropriately for target platform.

---

## When to Use

Use when:
- Expanding curriculum to new platform
- Similar concept exists on source platform
- Lesson translates well to target platform hardware

**Do NOT use when:**
- Concept is platform-specific (e.g., C64 SID chip, NES PPU scrolling)
- Hardware differences make adaptation impractical
- Lesson requires completely different approach on target platform

---

## Inputs

### Required
- **Source lesson path**: `/website/src/pages/{source-platform}/phase-{N}/tier-{N}/lesson-{NNN}.mdx`
- **Target platform**: `commodore-64`, `nintendo-entertainment-system`, `sinclair-zx-spectrum`, `commodore-amiga`
- **Target phase/tier**: Where adapted lesson will live

### Optional
- **Adaptation notes**: Specific changes required (e.g., "Use PPU scrolling instead of hardware scrolling")
- **Code rewrite strategy**: `translate` (direct instruction mapping) or `reimagine` (concept-driven rewrite)

---

## What It Does

### Phase 1: Analysis

1. **Read source lesson MDX**
   - Extract lesson concept/objective
   - Identify code examples
   - Note hardware-specific operations

2. **Read source code samples**
   - Parse source platform code (BASIC/assembly)
   - Identify patterns and techniques
   - Extract hardware register access

3. **Assess adaptability**
   - Check if concept translates to target platform
   - Identify hardware equivalents
   - Flag platform-specific challenges

4. **Generate adaptation report**
   ```
   Source: C64 Phase 0 Tier 1 Lesson 007 (Border Colour)
   Target: NES Phase 0 Tier 1 Lesson 007

   Concept: Changing border/background colour via hardware register
   Adaptability: HIGH (both platforms have colour control)

   Hardware mapping:
   - C64: POKE 53280 ($D020) = border colour
   - NES: Write to PPU palette ($3F00) = background colour

   Challenges:
   - NES requires VBlank timing (C64 doesn't)
   - NES has separate background/sprite palettes
   - NES colour values different (0-63 vs 0-15)

   Strategy: REIMAGINE (different timing, different palette model)
   ```

### Phase 2: Code Adaptation

1. **Create target platform code**
   - Rewrite code for target instruction set
   - Map hardware operations to target equivalents
   - Add platform-specific requirements (VBlank, sprite limits, etc.)
   - Follow target platform skill guidelines

2. **Compile and validate**
   - Use platform-specific compilation commands
   - Run semantic validator
   - Fix compilation errors

3. **Test in emulator**
   - Load code in target emulator
   - Verify output matches concept
   - Document any behavioral differences

### Phase 3: Content Adaptation

1. **Adapt lesson MDX**
   - Rewrite hardware references for target platform
   - Update code examples in MDX
   - Adjust explanations for target architecture
   - Update memory addresses/registers
   - Maintain lesson structure and tone

2. **Update "From the Vault" section**
   - Link to target platform-specific resources
   - Reference target platform games/developers

3. **Update "Quick Reference" section**
   - Target platform memory map
   - Target platform register addresses
   - Target platform-specific syntax

### Phase 4: Screenshot Capture

**STOP and report:**
```
Adaptation complete. Manual screenshot capture required.

Code compiled successfully:
  /code-samples/{target-platform}/phase-{N}/tier-{N}/lesson-{NNN}/example-1.{ext}

Load in {target-emulator} and capture screenshots:
  1. Launch: {emulator-command}
  2. Capture: {screenshot-method}
  3. Save to: /website/public/images/{target-platform}/phase-{N}/tier-{N}/lesson-{NNN}/screenshot-1.png

Resume with: Continue lesson-adaptation-agent with screenshot verification
```

**User manually captures screenshots.**

### Phase 5: Verification

1. **Verify screenshots with READ tool**
   - Check screenshots exist
   - Visually inspect output
   - Confirm matches target platform expectations

2. **Run validation suite**
   - lesson-validation skill
   - screenshot-verification skill
   - british-english-check skill
   - code-comment-check skill
   - Platform-specific validation

3. **Generate completion report**
   ```
   Adapted lesson ready:

   Files created:
   - /website/src/pages/nintendo-entertainment-system/phase-0/tier-1/lesson-007.mdx
   - /code-samples/nintendo-entertainment-system/phase-0/tier-1/lesson-007/example-1.asm
   - /code-samples/nintendo-entertainment-system/phase-0/tier-1/lesson-007/example-1.nes
   - /website/public/images/nintendo-entertainment-system/phase-0/tier-1/lesson-007/screenshot-1.png

   Validation: ✅ All checks passed

   Differences from source:
   - VBlank timing required (new constraint)
   - Palette write instead of direct colour write
   - Assembly syntax (6502 vs 6510 minor differences)

   Navigation updates pending:
   Run navigation-update-agent to add to tier index.
   ```

---

## Decisions It Makes

### Adaptation Strategy
- **Translate**: Direct instruction mapping (e.g., C64 6510 → NES 6502, mostly compatible)
- **Reimagine**: Concept-driven rewrite (e.g., C64 sprites → NES sprites, different registers/limits)

### Hardware Mapping
- Identifies equivalent hardware features
- Maps registers/memory addresses
- Adjusts for platform-specific constraints

### Code Style
- Follows target platform skill guidelines
- Preserves lesson pedagogical intent
- Maintains comment density and quality

### Content Adjustments
- Rewrites hardware-specific explanations
- Updates memory maps and references
- Adjusts examples for target architecture

---

## User Involvement

**User provides:**
1. Source lesson selection
2. Target platform and location
3. Manual screenshot capture (Phase 4)
4. Final approval of adapted lesson

**User reviews:**
- Adaptation report (Phase 1)
- Compiled code output
- Adapted lesson MDX
- Validation results

---

## Platform Compatibility Matrix

### Source → Target Adaptability

| Source → Target | C64 BASIC | C64 ASM | NES ASM | ZX BASIC | ZX ASM | Amiga BASIC | Amiga ASM |
|-----------------|-----------|---------|---------|----------|--------|-------------|-----------|
| **C64 BASIC**   | -         | Medium  | Low     | High     | Low    | High        | Low       |
| **C64 ASM**     | Medium    | -       | Medium  | Low      | Medium | Low         | Low       |
| **NES ASM**     | Low       | Medium  | -       | Low      | Medium | Low         | Low       |
| **ZX BASIC**    | High      | Low     | Low     | -        | Medium | High        | Low       |
| **ZX ASM**      | Low       | Medium  | Medium  | Medium   | -      | Low         | Low       |
| **Amiga BASIC** | High      | Low     | Low     | High     | Low    | -           | Medium    |
| **Amiga ASM**   | Low       | Low     | Low     | Low      | Low    | Medium      | -         |

**Key:**
- **High**: Concept and syntax translate well (BASIC to BASIC, similar constraints)
- **Medium**: Concept translates, but syntax/hardware requires significant adaptation (6510 ↔ 6502 ↔ Z80)
- **Low**: Concept may not translate (different architecture, e.g., 8-bit ↔ 32-bit)

### Specific Adaptation Examples

**High Adaptability (BASIC to BASIC):**
- C64 BASIC → ZX BASIC: Print, loops, variables (syntax differences minor)
- C64 BASIC → Amiga AMOS: Similar concepts, more powerful hardware

**Medium Adaptability (Assembly, similar CPUs):**
- C64 6510 ASM → NES 6502 ASM: Same instruction set, different hardware registers
- C64 6510 ASM → ZX Z80 ASM: Different instruction set, similar constraints

**Low Adaptability (Fundamentally different):**
- Any 8-bit ASM → Amiga 68K ASM: 8-bit vs 32-bit, completely different architecture
- BASIC → Assembly: Pedagogical approach too different

---

## Adaptation Strategies by Concept

### Universal Concepts (High Adaptability)

**Variables, arithmetic, loops, conditionals:**
- Strategy: TRANSLATE (direct syntax mapping)
- Example: C64 `FOR I=1 TO 10` → ZX `FOR I=1 TO 10`
- Challenges: Minor syntax differences (ZX requires `LET`)

**Display text:**
- Strategy: TRANSLATE with coordinate adjustments
- Example: C64 `PRINT "HELLO"` → NES assembly text rendering
- Challenges: NES requires PPU tile writes, no PRINT statement

**Read input:**
- Strategy: REIMAGINE (hardware varies significantly)
- Example: C64 joystick (CIA) → NES controller (4016/4017 registers)
- Challenges: Different register layouts, polling methods

### Platform-Specific Concepts (Low Adaptability)

**C64 SID sound:**
- Adaptability: LOW (NES has APU, Amiga has Paula, ZX has BEEP)
- Strategy: Find platform equivalent (NES square wave, Amiga sample playback)

**NES PPU scrolling:**
- Adaptability: LOW (C64/ZX have different scrolling methods)
- Strategy: Use platform's native scrolling (C64 hardware scroll, ZX software scroll)

**Amiga blitter:**
- Adaptability: LOW (other platforms lack dedicated blitter)
- Strategy: Software equivalent or skip concept

### Hardware Registers (Medium to Low)

**Colour control:**
- C64: $D020 (border), $D021 (background)
- NES: PPU palette ($3F00)
- ZX: BORDER/PAPER/INK commands
- Amiga: Copper palette registers
- Strategy: REIMAGINE with platform-specific timing/palette model

**Sprites:**
- C64: VIC-II sprite registers ($D000-$D02F)
- NES: OAM sprite table ($0200-$02FF)
- ZX: Software sprites only
- Amiga: Hardware sprites + BOBs
- Strategy: REIMAGINE with platform sprite capabilities

---

## Workflow Checklist

**Phase 1: Analysis**
- [ ] Read source lesson MDX
- [ ] Read source code samples
- [ ] Assess adaptability (High/Medium/Low)
- [ ] Generate adaptation report
- [ ] User reviews report and approves adaptation

**Phase 2: Code Adaptation**
- [ ] Create target platform code
- [ ] Compile with platform-specific toolchain
- [ ] Run semantic validator
- [ ] Fix any compilation/validation errors

**Phase 3: Content Adaptation**
- [ ] Adapt lesson MDX (hardware references, explanations)
- [ ] Update code examples in MDX
- [ ] Update "From the Vault" links
- [ ] Update "Quick Reference" section
- [ ] Maintain lesson structure and tone

**Phase 4: Screenshot Capture (Manual)**
- [ ] Stop agent, provide screenshot instructions
- [ ] User loads code in target emulator
- [ ] User captures screenshots
- [ ] User resumes agent with screenshot verification

**Phase 5: Verification**
- [ ] Verify screenshots with READ tool
- [ ] Run lesson-validation skill
- [ ] Run screenshot-verification skill
- [ ] Run british-english-check skill
- [ ] Run code-comment-check skill
- [ ] Run platform-specific validation
- [ ] Generate completion report
- [ ] Navigation updates (run navigation-update-agent)

---

## Anti-Patterns

### 1. Direct Instruction Translation Without Understanding

**Anti-pattern:**
```asm
; C64 6510
LDA #5
STA $D020

; "Translated" to NES (WRONG!)
LDA #5
STA $D020    ; This address doesn't exist on NES!
```

**Why wrong:** Hardware registers differ across platforms.

**Fix:** Understand concept (change colour), map to NES equivalent (PPU palette write during VBlank).

### 2. Ignoring Platform-Specific Constraints

**Anti-pattern:**
```asm
; C64 can write to VIC-II anytime
LDA #0
STA $D020

; NES adaptation (WRONG!)
LDA #0
STA $3F00    ; Must be during VBlank!
```

**Why wrong:** NES PPU requires VBlank timing.

**Fix:** Add VBlank wait before PPU writes.

### 3. Adapting Inappropriate Concepts

**Anti-pattern:**
Adapting C64 SID music lesson to ZX Spectrum (which only has BEEP).

**Why wrong:** Platforms too different, concept doesn't translate.

**Fix:** Create new ZX-appropriate sound lesson (BEEP effects, timing).

### 4. Losing Pedagogical Intent

**Anti-pattern:**
Source lesson teaches "simple colour change" but adapted lesson introduces complex palette programming.

**Why wrong:** Complexity creep changes lesson objective.

**Fix:** Keep concept simple on target platform, match source lesson's pedagogical level.

### 5. Not Updating Hardware References

**Anti-pattern:**
Adapted lesson still says "POKE 53280" when target platform is NES.

**Why wrong:** Confuses learners, incorrect information.

**Fix:** Update all hardware references to target platform.

---

## Example Adaptation

### Source: C64 Phase 0 Tier 1 Lesson 007 (Border Colour)

**Concept:** Change border colour via hardware register

**Source code (C64 BASIC):**
```basic
10 rem change border to black
20 poke 53280,0
30 rem change border to white
40 poke 53280,1
```

**Source explanation:**
- Memory address 53280 ($D020) controls border colour
- Values 0-15 select colours

### Target: NES Phase 0 Tier 1 Lesson 007

**Concept:** Change background colour via PPU palette

**Adapted code (NES 6502 ASM):**
```asm
; iNES header
.segment "HEADER"
    .byte "NES", $1A
    .byte 2, 1, 0, 0

; Code
.segment "CODE"
reset:
    ; Wait for PPU warm-up
    bit $2002
:   bit $2002
    bpl :-

    ; Write palette during VBlank
    lda #$3F
    sta $2006       ; PPU address high
    lda #$00
    sta $2006       ; PPU address low ($3F00)

    lda #$0F        ; Black
    sta $2007       ; Write to palette

    ; Infinite loop
loop:
    jmp loop

; Vectors
.segment "VECTORS"
    .word 0, reset, 0
```

**Adapted explanation:**
- PPU palette at $3F00 controls background colour
- Must write during VBlank (PPU warm-up wait)
- Colour values 0-63 (different from C64's 0-15)

**Adaptation notes:**
- Concept maintained: Change background colour
- Hardware differs: PPU palette vs VIC-II register
- New constraint: VBlank timing required
- Format differs: Assembly vs BASIC (Phase 0 NES uses assembly)

---

## Dependencies

**Skills required:**
- Platform-specific lesson creation skills (all 7)
- lesson-validation
- screenshot-verification
- british-english-check
- code-comment-check

**Agents required:**
- navigation-update-agent (after adaptation complete)

**Infrastructure:**
- Compilation toolchains for all platforms
- Emulators for all platforms
- Semantic validators for all platforms

---

## Complexity Notes

**Why "Very High" complexity?**

1. **Cross-platform knowledge:** Must understand hardware/software for all platforms
2. **Concept abstraction:** Must extract lesson concept independent of platform
3. **Hardware mapping:** Must find equivalent features across different architectures
4. **Constraint awareness:** Must respect platform-specific limitations
5. **Pedagogical preservation:** Must maintain lesson's teaching intent
6. **Code generation:** Must write correct, idiomatic code for target platform
7. **Content adaptation:** Must rewrite explanations for target platform

**Fallback strategy:**

If adaptation proves too complex, agent should:
1. Report adaptation challenges
2. Recommend creating new lesson from scratch
3. Provide detailed notes on concept mapping for manual creation

---

## Integration with Other Agents

**Called by:**
- curriculum-planning-agent (when expanding to new platforms)

**Calls:**
- navigation-update-agent (after successful adaptation)
- lesson-validation skill (verification phase)
- Platform-specific skills (for code creation/compilation)

**Works with:**
- lesson-creation-agent (for creating from scratch when adaptation infeasible)

---

## The Bottom Line

**Lesson adaptation automates cross-platform curriculum expansion:**

1. **Analyze** source lesson concept and code
2. **Map** hardware features to target platform equivalents
3. **Adapt** code for target instruction set and constraints
4. **Rewrite** lesson content for target platform
5. **Manual screenshots** (user captures after code ready)
6. **Validate** adapted lesson with full verification suite
7. **Report** differences and completion status

**Zero tolerance for:**
- Direct translation without understanding (loses correctness)
- Ignoring platform constraints (code won't work)
- Adapting inappropriate concepts (wastes time)
- Losing pedagogical intent (confuses learners)
- Incorrect hardware references (wrong information)

**When adaptation is infeasible, recommend creating new lesson from scratch. Cross-platform adaptation is powerful but not universal - some concepts don't translate.**
