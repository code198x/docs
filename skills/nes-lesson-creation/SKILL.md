---
name: nes-lesson-creation
description: Use when creating or editing NES 6502 Assembly lessons - enforces platform-specific compilation, validation, screenshot capture, and NES-specific requirements
---

# NES 6502 Assembly Lesson Creation

## Overview

This skill guides creation of NES (Nintendo Entertainment System) 6502 assembly lessons with platform-specific validation, compilation, and screenshot capture. The NES has unique constraints: no BASIC, iNES header format, PPU/APU hardware, VBlank timing, and mapper requirements.

## When to Use

Use when:
- Creating new NES 6502 assembly lesson
- Editing existing NES assembly lesson
- Validating NES assembly lesson before commit

**Do NOT use for:**
- C64 lessons (use c64-lesson-creation or c64-6510-lesson-creation)
- Other platforms (use platform-specific skills)

---

## Prerequisites

**Before starting, ensure:**

1. **lesson-creation-workflow skill** - Read generic workflow first
2. **Curriculum alignment** - Read `/docs/nintendo-entertainment-system/PHASE-N-CURRICULUM.md`
3. **Tools installed:**
   - `ca65` (cc65 assembler) - 6502 assembler
   - `ld65` (cc65 linker) - With NES configuration
   - `fceux` (NES emulator) - For testing and screenshots
   - Python 3 - For semantic validator

---

## NES 6502 Assembly Rules

**Critical requirements for NES:**

### 1. iNES Header Required

**NES ROM files (.nes) need iNES header:**

```asm
; iNES header (16 bytes)
.segment "HEADER"
    .byte "NES", $1A      ; Magic string
    .byte 2               ; 2 * 16KB PRG-ROM
    .byte 1               ; 1 * 8KB CHR-ROM
    .byte $00             ; Mapper 0 (NROM), horizontal mirroring
    .byte $00             ; No special features
    .byte $00, $00, $00, $00, $00, $00, $00, $00  ; Padding
```

**Why:** NES emulators expect iNES format to know ROM configuration.

### 2. No Illegal Opcodes

**Unlike C64, NES uses strict 6502:**
- Only legal 6502 instructions
- No illegal opcodes (no LAX, SAX, DCP, etc.)
- Stricter than C64 6510

### 3. PPU (Picture Processing Unit) Access

**PPU registers ($2000-$2007):**

| Address | Register | Purpose |
|---------|----------|---------|
| $2000 | PPUCTRL | Control register |
| $2001 | PPUMASK | Mask register (enable sprites/bg) |
| $2002 | PPUSTATUS | Status register (VBlank flag) |
| $2003 | OAMADDR | OAM address |
| $2004 | OAMDATA | OAM data |
| $2005 | PPUSCROLL | Scroll position |
| $2006 | PPUADDR | PPU address |
| $2007 | PPUDATA | PPU data |

**Critical: PPU updates only during VBlank!**

### 4. VBlank Timing (Fundamental Constraint)

**NES screen draws 60 times/second:**
- Drawing phase: Cannot update PPU (~90% of frame)
- VBlank phase: Can update PPU (~10% of frame)

**Check VBlank:**
```asm
wait_vblank:
    BIT $2002         ; Read PPUSTATUS
    BPL wait_vblank   ; Wait until bit 7 set (VBlank)
```

**Space efficiency note:** Every cycle counts - tight loops preferred.

---

## Required Files Checklist

For NES lesson NNN in Phase X, Tier Y:

- [ ] `/website/src/pages/nintendo-entertainment-system/phase-X/tier-Y/lesson-NNN.mdx`
- [ ] `/code-samples/nintendo-entertainment-system/phase-X/tier-Y/lesson-NNN/example-1.asm`
- [ ] `/code-samples/nintendo-entertainment-system/phase-X/tier-Y/lesson-NNN/example-1.nes` (assembled+linked)
- [ ] `/code-samples/nintendo-entertainment-system/phase-X/tier-Y/lesson-NNN/example-1.chr` (CHR-ROM if needed)
- [ ] `/code-samples/nintendo-entertainment-system/phase-X/tier-Y/lesson-NNN/example-2.asm` (if applicable)
- [ ] `/code-samples/nintendo-entertainment-system/phase-X/tier-Y/lesson-NNN/example-2.nes` (if applicable)
- [ ] `/website/public/images/nintendo-entertainment-system/phase-X/tier-Y/lesson-NNN/screenshot-1.png`
- [ ] `/website/public/images/nintendo-entertainment-system/phase-X/tier-Y/lesson-NNN/screenshot-2.png` (if applicable)

---

## Compilation Process

### Step 1: Create NES Configuration File

**nes.cfg (linker configuration):**

```
MEMORY {
    HEADER: start=$0000, size=$0010, fill=yes, fillval=$00;
    PRG:    start=$8000, size=$8000, fill=yes, fillval=$FF;
    CHR:    start=$0000, size=$2000, fill=yes, fillval=$00;
}

SEGMENTS {
    HEADER:   load=HEADER, type=ro;
    CODE:     load=PRG,    type=ro, start=$8000;
    RODATA:   load=PRG,    type=ro;
    VECTORS:  load=PRG,    type=ro, start=$FFFA;
    CHR:      load=CHR,    type=ro;
}
```

### Step 2: Assemble with ca65

```bash
cd /code-samples/nintendo-entertainment-system/phase-X/tier-Y/lesson-NNN/

# Assemble to object file
ca65 example-1.asm -o example-1.o

# Check exit code
echo $?  # Should be 0 (success)
```

### Step 3: Link with ld65

```bash
# Link with NES configuration
ld65 -C nes.cfg example-1.o -o example-1.nes

# Check exit code
echo $?  # Should be 0 (success)
```

**Resulting .nes file contains:**
- 16-byte iNES header
- 32KB PRG-ROM (code)
- 8KB CHR-ROM (graphics)

### Step 4: Run Semantic Validator

```bash
# NES assembly semantic validator
python3 /scripts/validate-nes-asm.py example-1.asm
```

**Semantic checks:**
- PPU writes only during VBlank
- Sprite limit (8 per scanline, 64 total)
- Palette usage (4 palettes, 4 colours each)
- Valid PPU/APU addresses
- CHR-ROM/RAM configuration
- Mapper compatibility
- iNES header correctness

---

## Screenshot Capture

### Method: FCEUX Emulator

**NES screenshots use FCEUX.**

### Manual Capture

```bash
# Load ROM
fceux example-1.nes

# File → Screenshot (or F12 key)
# Screenshots saved to fceux screenshots directory
# Move to: /website/public/images/.../lesson-NNN/screenshot-1.png
```

###Automated Capture (Lua Script Required)

**FCEUX supports Lua scripting for automation:**

```lua
-- screenshot.lua
emu.frameadvance()  -- Advance to first frame
for i=1,60 do      -- Wait 1 second (60 frames)
    emu.frameadvance()
end
gui.savescreenshot("screenshot-1.png")
emu.exit()
```

```bash
fceux --loadlua screenshot.lua example-1.nes
```

**Note:** Lua script automation is complex - manual capture often easier.

---

## NES-Specific Validation

### 1. Memory Map

**NES memory layout (different from C64):**

| Range | Purpose | Writable |
|-------|---------|----------|
| $0000-$07FF | RAM (2KB, mirrored to $0800-$1FFF) | ✓ |
| $2000-$2007 | PPU registers | ✓ (VBlank only) |
| $4000-$4017 | APU/Controller registers | ✓ |
| $4020-$FFFF | Cartridge (PRG-ROM/RAM) | Mapper-dependent |
| $8000-$FFFF | PRG-ROM (code lives here) | ✗ (ROM) |
| $FFFA-$FFFB | NMI vector | ✓ (at build time) |
| $FFFC-$FFFD | RESET vector | ✓ (at build time) |
| $FFFE-$FFFF | IRQ/BRK vector | ✓ (at build time) |

**No zero page safety issues like C64 - full $0000-$07FF available for user code.**

### 2. VBlank Enforcement

**Critical: Never write PPU outside VBlank**

```asm
; CORRECT:
nmi_handler:
    ; VBlank started - safe to update PPU
    LDA #$00
    STA $2006      ; PPUADDR
    LDA #$00
    STA $2006
    ; ... update PPU ...
    RTI

; WRONG:
main_loop:
    LDA #$00
    STA $2006      ; Outside VBlank - causes visual glitches!
```

**Validation:**
```bash
# Check for PPU writes outside NMI handler
grep -n "STA \$200[0-7]" example-1.asm
# Should only appear in NMI handler
```

### 3. Sprite Limits

**Hardware limits:**
- 64 sprites total (OAM = Object Attribute Memory)
- 8 sprites per scanline
- More than 8 = flicker or dropout

**Space-efficient sprite management crucial for complex games.**

### 4. Palette Restrictions

**NES palette system:**
- 52 total colours available
- 4 background palettes (4 colours each)
- 4 sprite palettes (4 colours each)
- Colour 0 transparent for sprites

**Validation:**
```bash
# Check palette definitions
grep -n "palette" example-1.asm
```

### 5. Controller Input

**Controllers at $4016 (P1) and $4017 (P2):**

```asm
read_controller:
    LDA #$01
    STA $4016      ; Strobe controller
    LDA #$00
    STA $4016
    LDX #$08       ; 8 buttons
button_loop:
    LDA $4016      ; Read button state
    ; ... process ...
    DEX
    BNE button_loop
    RTS
```

---

## Anti-Patterns (NES Specific)

### 1. PPU Writes Outside VBlank

**Anti-pattern:**
```asm
game_loop:
    LDA sprite_x
    STA $2003      ; OAM write outside VBlank - glitches!
    JMP game_loop
```

**Fix:**
```asm
; Set flag, update in NMI
game_loop:
    LDA #$01
    STA update_flag
    ; ... wait for NMI ...

nmi_handler:
    LDA update_flag
    BEQ skip
    ; Update PPU here (during VBlank)
    LDA sprite_x
    STA $2003
skip:
    RTI
```

### 2. Not Checking VBlank Before PPU Access

**Anti-pattern:**
```asm
    LDA #$20
    STA $2006      ; Hope we're in VBlank?
```

**Fix:**
```asm
wait_vblank:
    BIT $2002
    BPL wait_vblank  ; Wait for VBlank flag
    LDA #$20
    STA $2006
```

### 3. Wasting ROM Space

**Anti-pattern:**
```asm
    .org $8000
    .res $100, $00   ; 256 bytes of zeros - waste!
```

**Fix:**
```asm
; Organize code tightly, use every byte efficiently
    .org $8000
start:
    ; Code immediately, no padding
```

### 4. Exceeding 8 Sprites Per Scanline

**Anti-pattern:**
```asm
; Put 10 sprites on same Y coordinate - dropout!
```

**Fix:**
```asm
; Stagger Y coordinates or use sprite multiplexing
; Distribute sprites across scanlines
```

### 5. Missing Reset Vector

**Anti-pattern:**
```asm
; No vectors defined - emulator won't know where to start!
```

**Fix:**
```asm
.segment "VECTORS"
    .word nmi_handler     ; $FFFA: NMI
    .word reset_handler   ; $FFFC: RESET
    .word irq_handler     ; $FFFE: IRQ/BRK
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

- [ ] Write example-1.asm with iNES header
- [ ] Define reset/NMI/IRQ vectors
- [ ] Implement VBlank waiting
- [ ] Check PPU writes only in NMI handler
- [ ] Create CHR-ROM data if needed
- [ ] Assemble with ca65 → example-1.o
- [ ] Link with ld65 + nes.cfg → example-1.nes
- [ ] Run semantic validator
- [ ] Create example-2.asm if needed

### Phase 3: Screenshot Capture

- [ ] Load example-1.nes in fceux
- [ ] Capture screenshot (F12 or menu)
- [ ] Move to correct location
- [ ] Verify screenshot with READ tool
- [ ] Capture additional screenshots if needed

### Phase 4: Lesson MDX Creation

- [ ] Create lesson-NNN.mdx
- [ ] Include assembly code with explanations
- [ ] Explain VBlank timing requirements
- [ ] Explain PPU/APU usage
- [ ] Add screenshots
- [ ] British English (except "program")

### Phase 5: Validation

- [ ] Run lesson-validation skill
- [ ] Run curriculum-alignment-check
- [ ] Run screenshot-verification
- [ ] Run british-english-check
- [ ] Run voice-tone-check
- [ ] Fix any issues

### Phase 6: File Verification

- [ ] ls code-samples/.../lesson-NNN/ (all files present, including .nes)
- [ ] ls website/public/images/.../lesson-NNN/ (all screenshots present)
- [ ] ls website/src/pages/.../lesson-NNN.mdx (lesson file present)

### Phase 7: Navigation Update

- [ ] Update tier-N.astro with new lesson
- [ ] Update phase-N.astro if new tier
- [ ] Update nintendo-entertainment-system.astro if new phase

---

## Quick Reference

### Compilation
```bash
ca65 example-1.asm -o example-1.o
ld65 -C nes.cfg example-1.o -o example-1.nes
```

### Screenshot
```bash
fceux example-1.nes
# F12 to capture
```

### iNES Header Template
```asm
.segment "HEADER"
    .byte "NES", $1A
    .byte 2               ; 2 * 16KB PRG
    .byte 1               ; 1 * 8KB CHR
    .byte $00, $00        ; Mapper 0, no features
    .byte $00, $00, $00, $00, $00, $00, $00, $00
```

### VBlank Wait
```asm
wait_vblank:
    BIT $2002
    BPL wait_vblank
```

### Reset Vector Template
```asm
.segment "VECTORS"
    .word nmi_handler
    .word reset_handler
    .word irq_handler
```

---

## Common Mistakes

**Mistake 1: Missing iNES header**
- **Symptom:** Emulator won't load ROM
- **Fix:** Add 16-byte iNES header

**Mistake 2: PPU writes outside VBlank**
- **Symptom:** Visual glitches, corruption
- **Fix:** Only write PPU in NMI handler

**Mistake 3: Missing vectors**
- **Symptom:** Emulator doesn't know where to start
- **Fix:** Define RESET/NMI/IRQ vectors at $FFFA-$FFFF

**Mistake 4: Not waiting for VBlank**
- **Symptom:** Unstable graphics
- **Fix:** BIT $2002, BPL loop

**Mistake 5: Exceeding sprite limits**
- **Symptom:** Sprite dropout, flicker
- **Fix:** Stay within 8 sprites/scanline, 64 total

**Mistake 6: Wasting ROM space**
- **Symptom:** Large .nes files, inefficiency
- **Fix:** Pack code tightly, no unnecessary padding

---

## Platform-Specific Resources

**Essential docs:**
- `/docs/NES-QUICK-REFERENCE.md` - PPU/APU registers, memory map
- `/docs/6502-QUICK-REFERENCE.md` - 6502 instruction set (no illegal opcodes)
- `/docs/START-HERE.md` - Navigation

---

## The Bottom Line

**NES lessons require:**
1. iNES header (16 bytes) for emulator compatibility
2. ca65/ld65 with NES configuration
3. VBlank timing enforcement (PPU writes only in NMI)
4. Sprite limits (8/scanline, 64 total)
5. Reset/NMI/IRQ vectors defined
6. Space-efficient code (ROM is limited)
7. British English (except "program")

**Zero tolerance for:**
- Missing iNES header (won't load)
- PPU writes outside VBlank (visual corruption)
- Missing reset vector (won't start)
- Wasting ROM space (inefficient)
- Unverified screenshots
- American spellings (except "program")

**Every NES lesson must assemble, link to .nes format, run in FCEUX, and display expected output verified with screenshots. VBlank timing is fundamental - no exceptions.**
