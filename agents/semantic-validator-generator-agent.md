# Semantic Validator Generator Agent

**Type**: Agent (Autonomous execution)
**Priority**: P3 (Future)
**Status**: Specification
**Complexity**: High

---

## Purpose

Generates platform-specific semantic validators (Python scripts) that detect errors compilers miss. Compilers check syntax, but not semantic correctness (e.g., using unsafe memory addresses, violating hardware timing constraints, exceeding hardware limits). Validators catch these before runtime.

---

## When to Use

Use when:
- Adding new platform to curriculum (need validator for that platform)
- Updating platform specifications (new checks required)
- Discovering new anti-patterns (add to validator)
- Validator tests fail (regenerate with fixes)

**Do NOT use when:**
- Just validating single lesson (use existing validator via lesson-validation)
- Platform validator already exists and works correctly

---

## Inputs

### Required
- **Platform**: `commodore-64`, `nintendo-entertainment-system`, `sinclair-zx-spectrum`, `commodore-amiga`
- **Language**: `basic`, `6510-asm`, `6502-asm`, `z80-asm`, `68k-asm`, `amos-basic`

### Optional
- **Specification file**: Platform-specific constraints (if not using defaults)
- **Output location**: Where to save validator (default: `/scripts/validate-{platform}-{language}.py`)
- **Test mode**: Generate with test cases (default: true)

---

## What It Does

### Phase 1: Load Platform Specification

1. **Read platform-specific constraints**

**C64 BASIC constraints:**
```yaml
platform: commodore-64
language: basic

constraints:
  memory:
    safe_range: [2049, 40959]  # $0801-$9FFF
    avoid_ranges:
      - [0, 2047]     # Zero page, stack, BASIC
      - [53248, 53294]  # VIC-II registers
      - [54272, 54295]  # SID registers
      - [56320, 56335]  # CIA registers

  syntax:
    max_line_length: 80
    max_line_number: 63999
    keywords_lowercase: true  # For .bas files

  hardware:
    vic_colors: [0, 15]
    sid_voices: [0, 2]
    sprites: [0, 7]

anti_patterns:
  - pattern: 'poke 0,'
    message: "POKE to zero page ($0000) - dangerous!"
  - pattern: 'poke [0-9]+,256'
    message: "POKE value > 255 - will overflow!"
  - pattern: 'for .* to [0-9]{6,}'
    message: "Loop limit exceeds 16-bit range"
```

**NES 6502 ASM constraints:**
```yaml
platform: nintendo-entertainment-system
language: 6502-asm

constraints:
  instructions:
    forbidden:
      - {opcode: 'SLO', reason: 'Illegal opcode'}
      - {opcode: 'RLA', reason: 'Illegal opcode'}
      # ... all illegal opcodes

  hardware:
    ppu_write_timing: 'vblank_only'  # Enforce VBlank
    sprite_limit: 8  # Per scanline
    oam_size: 256  # Bytes
    chr_rom_size: 8192  # Bytes

  memory:
    safe_zero_page: [0, 255]  # All ZP safe (no OS)
    ram_range: [0x0000, 0x07FF]
    ppu_registers: [0x2000, 0x2007]
    apu_registers: [0x4000, 0x4017]

anti_patterns:
  - pattern: 'STA \$200[0-7]'
    context: 'not_in_vblank'
    message: "PPU write outside VBlank - will glitch!"
  - pattern: 'LDA #\$FF[\n\r\s]+STA \$2000'
    message: "Writing $FF to PPUCTRL - enables NMI + bad settings"
```

**ZX Spectrum BASIC constraints:**
```yaml
platform: sinclair-zx-spectrum
language: basic

constraints:
  syntax:
    let_required: true  # ZX requires LET keyword
    print_at_order: 'y_x'  # Row first, column second

  hardware:
    screen_rows: [0, 21]  # 22 rows (0-21)
    screen_cols: [0, 31]  # 32 columns (0-31)
    colors: [0, 7]  # 8 colours
    beep_duration: [0, 9.999]

  memory:
    screen_memory: [16384, 22527]  # $4000-$57FF
    attributes: [22528, 23295]  # $5800-$5AFF

anti_patterns:
  - pattern: 'PRINT AT [2-9][0-9],'
    message: "PRINT AT row > 21 - out of bounds!"
  - pattern: 'INK [8-9]'
    message: "INK colour > 7 - invalid!"
  - pattern: '^[0-9]+ [A-Z]+=.+'
    message: "Missing LET keyword - required on ZX Spectrum!"
```

**Amiga 68K ASM constraints:**
```yaml
platform: commodore-amiga
language: 68k-asm

constraints:
  registers:
    preserve: [D0, D1, D2, D3, D4, D5, D6, D7, A0, A1, A2, A3, A4, A5, A6]
    never_modify: [A7]  # Stack pointer
    library_base: [A6]  # Exec library calls

  instructions:
    size_suffixes: ['.B', '.W', '.L']  # Required

  hardware:
    custom_chip_base: 0xDFF000
    registers:
      copper: [0xDFF080, 0xDFF088]
      blitter: [0xDFF040, 0xDFF074]
      paula: [0xDFF0A0, 0xDFF0D8]

  privilege:
    user_mode: true  # Most code runs in user mode
    supervisor_only:
      - 'MOVE to SR'
      - 'MOVE to USP'
      - 'RTE'
      - 'STOP'

anti_patterns:
  - pattern: 'MOVE\.[BWL] .+,A7'
    message: "Corrupting stack pointer (A7) - system crash!"
  - pattern: 'JSR'
    context: 'no_movem_before'
    message: "JSR without preserving registers - may corrupt caller!"
  - pattern: 'MOVE #.+,SR'
    context: 'user_mode'
    message: "Writing to SR in user mode - privilege violation!"
```

### Phase 2: Generate Validator Script

1. **Create Python validator template**

```python
#!/usr/bin/env python3
"""
Semantic validator for {Platform} {Language}

Generated by semantic-validator-generator-agent
Date: {generation-date}

Validates code for platform-specific semantic errors that
compilers don't catch (hardware constraints, unsafe memory, etc.)
"""

import re
import sys
from typing import List, Tuple

class {Platform}{Language}Validator:
    """Validates {Platform} {Language} code"""

    def __init__(self, code_file: str):
        self.code_file = code_file
        with open(code_file, 'r') as f:
            self.code = f.read()
        self.errors = []
        self.warnings = []

    def validate(self) -> bool:
        """Run all validation checks"""
        self.check_memory_safety()
        self.check_hardware_constraints()
        self.check_syntax_rules()
        self.check_anti_patterns()

        return len(self.errors) == 0

    def check_memory_safety(self):
        """Check for unsafe memory access"""
        # Generated based on platform constraints
        ...

    def check_hardware_constraints(self):
        """Check hardware-specific constraints"""
        # Generated based on platform constraints
        ...

    def check_syntax_rules(self):
        """Check platform-specific syntax requirements"""
        # Generated based on platform constraints
        ...

    def check_anti_patterns(self):
        """Check for known anti-patterns"""
        # Generated based on platform anti-patterns
        ...

    def report(self):
        """Print validation report"""
        if self.errors:
            print(f"❌ ERRORS ({len(self.errors)}):")
            for error in self.errors:
                print(f"  Line {error['line']}: {error['message']}")

        if self.warnings:
            print(f"⚠ WARNINGS ({len(self.warnings)}):")
            for warning in self.warnings:
                print(f"  Line {warning['line']}: {warning['message']}")

        if not self.errors and not self.warnings:
            print("✓ No issues found")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <code-file>")
        sys.exit(1)

    validator = {Platform}{Language}Validator(sys.argv[1])
    success = validator.validate()
    validator.report()

    sys.exit(0 if success else 1)
```

2. **Generate platform-specific check methods**

**Example: C64 BASIC memory safety check**

```python
def check_memory_safety(self):
    """Check for unsafe memory access in C64 BASIC"""

    # Check POKE to zero page (dangerous)
    for match in re.finditer(r'poke\s+(\d+)\s*,', self.code, re.IGNORECASE):
        address = int(match.group(1))
        line_number = self.get_line_number(match.start())

        if address < 256:
            self.errors.append({
                'line': line_number,
                'message': f"POKE to zero page (${address:02X}) - dangerous! Use $FB-$FE only."
            })

        elif 53248 <= address <= 53294:  # VIC-II
            # This is expected/acceptable
            pass

        elif address > 40959:  # Above BASIC area
            self.warnings.append({
                'line': line_number,
                'message': f"POKE to ${address:04X} - outside typical BASIC area"
            })

    # Check POKE value > 255 (will overflow)
    for match in re.finditer(r'poke\s+\d+\s*,\s*(\d+)', self.code, re.IGNORECASE):
        value = int(match.group(1))
        if value > 255:
            line_number = self.get_line_number(match.start())
            self.errors.append({
                'line': line_number,
                'message': f"POKE value {value} > 255 - will overflow to {value % 256}"
            })
```

**Example: NES VBlank timing check**

```python
def check_hardware_constraints(self):
    """Check NES-specific hardware constraints"""

    # Check PPU writes outside VBlank
    ppu_write_pattern = r'STA\s+\$200[0-7]'
    vblank_pattern = r'@?wait_?vblank:.*?BPL'

    # Find all PPU writes
    ppu_writes = list(re.finditer(ppu_write_pattern, self.code, re.IGNORECASE))

    # Find VBlank wait blocks
    vblank_blocks = list(re.finditer(vblank_pattern, self.code, re.IGNORECASE | re.DOTALL))

    for ppu_write in ppu_writes:
        # Check if this write is within a VBlank block
        in_vblank = False
        for vblank_block in vblank_blocks:
            if vblank_block.start() < ppu_write.start() < vblank_block.end():
                in_vblank = True
                break

        if not in_vblank:
            line_number = self.get_line_number(ppu_write.start())
            self.errors.append({
                'line': line_number,
                'message': "PPU write outside VBlank - will cause visual glitches!"
            })

    # Check sprite limit (8 per scanline)
    # (More complex - requires sprite Y position analysis)
    ...
```

**Example: ZX Spectrum LET keyword check**

```python
def check_syntax_rules(self):
    """Check ZX Spectrum syntax requirements"""

    # Check for missing LET keyword
    assignment_pattern = r'^(\d+)\s+([A-Z][A-Z0-9]*\$?)\s*='

    for match in re.finditer(assignment_pattern, self.code, re.MULTILINE):
        line_number = int(match.group(1))
        var_name = match.group(2)

        # Check if LET is present
        line_start = match.start()
        line_end = self.code.find('\n', line_start)
        line = self.code[line_start:line_end]

        if 'LET' not in line.upper():
            self.errors.append({
                'line': line_number,
                'message': f"Missing LET keyword for '{var_name}=' - required on ZX Spectrum!"
            })

    # Check PRINT AT coordinates
    print_at_pattern = r'PRINT\s+AT\s+(\d+)\s*,\s*(\d+)'

    for match in re.finditer(print_at_pattern, self.code, re.IGNORECASE):
        row = int(match.group(1))
        col = int(match.group(2))
        line_number = self.get_line_number(match.start())

        if row > 21:
            self.errors.append({
                'line': line_number,
                'message': f"PRINT AT row {row} > 21 - out of bounds!"
            })

        if col > 31:
            self.errors.append({
                'line': line_number,
                'message': f"PRINT AT col {col} > 31 - out of bounds!"
            })
```

**Example: Amiga 68K register preservation check**

```python
def check_hardware_constraints(self):
    """Check Amiga 68K-specific constraints"""

    # Find all subroutine definitions
    subroutine_pattern = r'^([a-z_][a-z0-9_]*):\s*$'
    subroutines = re.finditer(subroutine_pattern, self.code, re.MULTILINE | re.IGNORECASE)

    for sub_match in subroutines:
        sub_name = sub_match.group(1)
        sub_start = sub_match.end()

        # Find RTS for this subroutine
        rts_match = re.search(r'\bRTS\b', self.code[sub_start:], re.IGNORECASE)
        if not rts_match:
            continue

        sub_end = sub_start + rts_match.start()
        sub_code = self.code[sub_start:sub_end]

        # Check for MOVEM.L to save registers
        save_pattern = r'MOVEM\.L\s+.*,\s*-\(SP\)'
        restore_pattern = r'MOVEM\.L\s+\(SP\)\+\s*,.*'

        has_save = re.search(save_pattern, sub_code, re.IGNORECASE)
        has_restore = re.search(restore_pattern, sub_code, re.IGNORECASE)

        if not (has_save and has_restore):
            line_number = self.get_line_number(sub_match.start())
            self.warnings.append({
                'line': line_number,
                'message': f"Subroutine '{sub_name}' doesn't preserve registers - may corrupt caller!"
            })

    # Check for A7 (stack pointer) corruption
    a7_write_pattern = r'MOVE\.[BWL]\s+.+,\s*A7'
    for match in re.finditer(a7_write_pattern, self.code, re.IGNORECASE):
        line_number = self.get_line_number(match.start())
        self.errors.append({
            'line': line_number,
            'message': "Writing to A7 (stack pointer) - system crash likely!"
        })
```

### Phase 3: Generate Test Cases

1. **Create test suite**

**Test structure:**
```python
# tests/test_{platform}_{language}_validator.py

import pytest
from validators.validate_{platform}_{language} import {Platform}{Language}Validator

def test_safe_code_passes():
    """Test that valid code passes validation"""
    validator = {Platform}{Language}Validator('tests/fixtures/safe_example.{ext}')
    assert validator.validate() == True
    assert len(validator.errors) == 0

def test_unsafe_zero_page_fails():
    """Test that zero page POKE is detected"""
    validator = {Platform}{Language}Validator('tests/fixtures/unsafe_zp.{ext}')
    assert validator.validate() == False
    assert any('zero page' in err['message'].lower() for err in validator.errors)

def test_poke_overflow_fails():
    """Test that POKE value > 255 is detected"""
    validator = {Platform}{Language}Validator('tests/fixtures/poke_overflow.{ext}')
    assert validator.validate() == False
    assert any('overflow' in err['message'].lower() for err in validator.errors)

# ... more test cases ...
```

2. **Create test fixtures**

**Example: C64 BASIC safe code**
```basic
10 rem safe code example
20 poke 53280,0    : rem border colour (safe)
30 for i=1024 to 2023
40   poke i,160    : rem screen memory (safe)
50 next i
```

**Example: C64 BASIC unsafe code**
```basic
10 rem unsafe code example
20 poke 0,0        : rem zero page (UNSAFE!)
30 poke 53280,256  : rem overflow (UNSAFE!)
```

### Phase 4: Integration

1. **Save validator to `/scripts/` directory**
```bash
/scripts/validate-c64-basic.py
/scripts/validate-c64-6510-asm.py
/scripts/validate-nes-6502-asm.py
/scripts/validate-zx-basic.py
/scripts/validate-zx-z80-asm.py
/scripts/validate-amiga-amos.py
/scripts/validate-amiga-68k-asm.py
```

2. **Make executable**
```bash
chmod +x /scripts/validate-*.py
```

3. **Update platform-specific skills**

Add validator call to each platform skill:

```bash
# In c64-lesson-creation/SKILL.md:

## Validation
python3 /scripts/validate-c64-basic.py example-1.bas
echo $?  # Should be 0 (no errors)
```

4. **Generate completion report**

```markdown
# Validator Generated: C64 BASIC

**Generated:** 2025-11-05
**Platform:** commodore-64
**Language:** basic
**Output:** /scripts/validate-c64-basic.py

---

## Checks Implemented

### Memory Safety (3 checks)
- ✓ Zero page POKE detection (addresses < 256)
- ✓ POKE value overflow (values > 255)
- ✓ POKE to unsafe memory ranges

### Hardware Constraints (5 checks)
- ✓ VIC-II colour range (0-15)
- ✓ SID voice range (0-2)
- ✓ Sprite number range (0-7)
- ✓ Screen memory bounds (1024-2023)
- ✓ Hardware register access validation

### Syntax Rules (2 checks)
- ✓ Line number range (0-63999)
- ✓ Line length < 80 characters

### Anti-Patterns (4 checks)
- ✓ POKE to address 0
- ✓ POKE value > 255
- ✓ Loop limit > 65535
- ✓ Uninitialized variable usage

**Total checks:** 14

---

## Test Results

**Test suite:** tests/test_c64_basic_validator.py
**Tests passed:** 12/12 ✓
**Coverage:** 95%

---

## Integration

Updated skills:
- ✓ /docs/skills/c64-lesson-creation/SKILL.md (added validator call)

Updated agents:
- ✓ /docs/agents/lesson-creation-agent.md (references validator)

---

## Usage

```bash
# Validate C64 BASIC code
python3 /scripts/validate-c64-basic.py example-1.bas

# Exit code 0 = success, 1 = errors
echo $?
```

---
```

---

## Decisions It Makes

### Check Generation
- Which constraints to enforce (strict vs warnings)
- Regex patterns for detection
- Context-aware checks (e.g., PPU writes in VBlank blocks)

### Error Severity
- Errors (code will fail/crash) vs warnings (code works but suboptimal)
- Critical vs informational

### Test Coverage
- Which anti-patterns to test
- Edge cases to cover
- Positive vs negative test ratio

---

## User Involvement

**User provides:**
1. Platform and language selection
2. Platform specification file (if custom)
3. Review of generated validator

**User reviews:**
- Generated validator code
- Test results
- Integration with platform skills

**User decides:**
- Whether to accept generated validator
- Whether to add custom checks
- Whether to update specifications

---

## Anti-Patterns

### 1. Overly Strict Validation

**Anti-pattern:**
Flagging valid advanced techniques as errors.

**Why wrong:** Prevents legitimate optimizations.

**Fix:** Use warnings for "unusual but valid" patterns, errors only for "will crash/glitch".

### 2. Missing Context

**Anti-pattern:**
Flagging PPU writes as errors without checking if in VBlank block.

**Why wrong:** False positives discourage validator use.

**Fix:** Context-aware checks (analyze control flow, not just line-by-line).

### 3. Platform-Agnostic Checks

**Anti-pattern:**
Checking for "division by zero" on all platforms (not platform-specific).

**Why wrong:** Semantic validators are for platform-specific constraints, not general programming errors.

**Fix:** Focus on hardware constraints, memory safety, timing requirements (platform-specific only).

### 4. Untested Validators

**Anti-pattern:**
Generating validator without test suite.

**Why wrong:** Validators may have false positives/negatives.

**Fix:** Always generate comprehensive test suite with fixtures.

### 5. Not Integrating

**Anti-pattern:**
Generating validator but not updating platform skills to use it.

**Why wrong:** Validator exists but nobody uses it.

**Fix:** Automatically update platform-specific skills with validator call.

---

## Dependencies

**Skills required:**
- Platform-specific lesson creation skills (integration targets)

**Agents required:**
- None (reads specifications, generates code)

**Infrastructure:**
- Platform specification files (YAML or similar)
- Python 3.x (for validator runtime)
- pytest (for test suite)

---

## Complexity Notes

**Why "High" complexity?**

1. **Code generation:** Creating Python validators from specifications
2. **Regex patterns:** Complex pattern matching for various syntaxes
3. **Context awareness:** Analyzing control flow (VBlank blocks, subroutines)
4. **Test generation:** Comprehensive test suites with fixtures
5. **Integration:** Updating multiple files (skills, agents, scripts)

**Simplification strategies:**

- Start with simple line-by-line checks (no context awareness)
- Add context-aware checks incrementally
- Use templates for common check patterns

---

## Integration with Other Agents/Skills

**Called by:**
- Platform-specific skills (reference generated validators)
- lesson-creation-agent (runs validators during lesson creation)

**Calls:**
- None (generates files)

**Works with:**
- lesson-validation skill (validators are part of validation suite)

---

## The Bottom Line

**Semantic validator generation automates platform-specific error detection:**

1. **Load** platform specifications (constraints, anti-patterns)
2. **Generate** Python validator with all checks
3. **Create** test suite with fixtures
4. **Integrate** with platform-specific skills
5. **Report** checks implemented and test results

**Zero tolerance for:**
- Untested validators (false positives/negatives)
- Platform-agnostic checks (not semantic validation)
- Missing context (false positives)
- No integration (validator exists but unused)

**Semantic validators catch hardware-specific errors that compilers miss. Essential for quality lesson code that won't crash or glitch at runtime.**
