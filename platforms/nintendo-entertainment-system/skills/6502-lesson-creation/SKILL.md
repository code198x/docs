---
name: nes-6502-lesson-creation
description: Use when creating or editing NES 6502 Assembly lessons - provides platform-specific compilation, validation, and screenshot capture for Phase 3 of the content creation workflow
---

# NES 6502 Assembly Lesson Creation

**Role:** Technical execution for Phase 3 (Validation) of the Content Creation Workflow.

**Prerequisite:** Read `/docs/CONTENT-CREATION-WORKFLOW.md` first. This skill provides NES-specific technical details, not the full workflow.

---

## When to Use

Use this skill during **Phase 3 (Validation)** when:
- Assembling NES code with ca65/ld65
- Capturing screenshots with FCEUX emulator
- Validating PPU/APU register usage
- Checking for NES-specific pitfalls (especially VBlank timing)

**Do NOT use for:**
- C64 lessons (use C64-specific skills)
- Other platforms (use platform-specific skills)

---

## NES 6502 Rules

### iNES Header Required

```asm
.segment "HEADER"
    .byte "NES", $1A      ; Magic string
    .byte 2               ; 2 * 16KB PRG-ROM
    .byte 1               ; 1 * 8KB CHR-ROM
    .byte $00             ; Mapper 0, horizontal mirroring
    .byte $00, $00, $00, $00, $00, $00, $00, $00
```

### Vectors Required

```asm
.segment "VECTORS"
    .word nmi_handler     ; $FFFA: NMI (VBlank)
    .word reset_handler   ; $FFFC: RESET
    .word irq_handler     ; $FFFE: IRQ/BRK
```

### VBlank Timing (FUNDAMENTAL)

**PPU updates ONLY during VBlank!**

```asm
; Wait for VBlank
wait_vblank:
    BIT $2002         ; Read PPUSTATUS
    BPL wait_vblank   ; Wait until bit 7 set

; PPU writes in NMI handler ONLY
nmi_handler:
    ; Safe to update PPU here
    LDA #$00
    STA $2006
    RTI
```

### No Illegal Opcodes

Unlike C64, NES uses strict 6502 - no illegal opcodes.

---

## Phase 3: Validation (Technical Details)

### Step 3.1: Assemble with ca65

```bash
cd /code-samples/nintendo-entertainment-system/phase-X/tier-Y/lesson-NNN/

ca65 example-1.asm -o example-1.o
echo $?  # Must be 0
```

### Step 3.2: Link with ld65

```bash
ld65 -C nes.cfg example-1.o -o example-1.nes
echo $?  # Must be 0
```

**nes.cfg (linker config):**
```
MEMORY {
    HEADER: start=$0000, size=$0010, fill=yes;
    PRG:    start=$8000, size=$8000, fill=yes;
    CHR:    start=$0000, size=$2000, fill=yes;
}
SEGMENTS {
    HEADER:  load=HEADER, type=ro;
    CODE:    load=PRG, type=ro, start=$8000;
    VECTORS: load=PRG, type=ro, start=$FFFA;
    CHR:     load=CHR, type=ro;
}
```

### Step 3.3: Semantic Validation

```bash
python3 /scripts/validate-nes-asm.py example-1.asm
```

**Checks:**
- ✅ PPU writes only during VBlank
- ✅ Sprite limits (8/scanline, 64 total)
- ✅ Valid PPU/APU addresses
- ✅ iNES header present
- ✅ Vectors defined

### Step 3.4: Screenshot Capture (FCEUX)

```bash
fceux example-1.nes
# Press F12 or File → Screenshot
```

Save to `/website/public/images/nintendo-entertainment-system/phase-X/tier-Y/lesson-NNN/screenshot-1.png`

### Step 3.5: Screenshot Verification (MANDATORY)

**Use Read tool to VIEW every screenshot:**

```
✅ CORRECT: "Read screenshot-1.png - shows NES graphics with sprites,
   background tiles visible, no visual corruption."

❌ WRONG: "Screenshot verified ✅" (too vague)
```

---

## Memory Map

| Range | Purpose |
|-------|---------|
| $0000-$07FF | RAM (2KB) |
| $2000-$2007 | PPU registers |
| $4000-$4017 | APU/Controller |
| $8000-$FFFF | PRG-ROM |
| $FFFA-$FFFF | Vectors |

---

## PPU Registers

| Address | Register | Purpose |
|---------|----------|---------|
| $2000 | PPUCTRL | Control |
| $2001 | PPUMASK | Enable sprites/bg |
| $2002 | PPUSTATUS | VBlank flag |
| $2005 | PPUSCROLL | Scroll position |
| $2006 | PPUADDR | PPU address |
| $2007 | PPUDATA | PPU data |

---

## Common Pitfalls

### 1. PPU Writes Outside VBlank
```asm
❌ WRONG:
main_loop:
    STA $2006          ; Outside VBlank - glitches!

✅ CORRECT:
nmi_handler:
    STA $2006          ; During VBlank - safe
    RTI
```

### 2. Missing iNES Header
```asm
❌ WRONG: ; No header - emulator won't load!
✅ CORRECT: .segment "HEADER" ...
```

### 3. Missing Vectors
```asm
❌ WRONG: ; No vectors - emulator doesn't know where to start!
✅ CORRECT: .segment "VECTORS" .word nmi, reset, irq
```

### 4. Exceeding Sprite Limits
```asm
❌ WRONG: ; 10 sprites on same scanline - dropout!
✅ CORRECT: ; Distribute sprites across scanlines
```

---

## Required Files

| File | Location |
|------|----------|
| Lesson MDX | `/website/src/pages/nintendo-entertainment-system/phase-X/tier-Y/lesson-NNN.mdx` |
| Source (.asm) | `/code-samples/nintendo-entertainment-system/phase-X/tier-Y/lesson-NNN/example-1.asm` |
| ROM (.nes) | `/code-samples/nintendo-entertainment-system/phase-X/tier-Y/lesson-NNN/example-1.nes` |
| Screenshot | `/website/public/images/nintendo-entertainment-system/phase-X/tier-Y/lesson-NNN/screenshot-1.png` |

---

## Quick Reference Commands

```bash
# Assemble + link
ca65 example-1.asm -o example-1.o
ld65 -C nes.cfg example-1.o -o example-1.nes

# Semantic validation
python3 /scripts/validate-nes-asm.py example-1.asm

# Screenshot
fceux example-1.nes
# Press F12
```

### VBlank Wait Template
```asm
wait_vblank:
    BIT $2002
    BPL wait_vblank
```

---

## Platform-Specific Resources

**Quick references** (in `/docs/platforms/nintendo-entertainment-system/`):
- `hardware/NES-QUICK-REFERENCE.md` - PPU/APU registers
- `hardware/6502-QUICK-REFERENCE.md` - 6502 instructions

---

## The Bottom Line

**This skill provides:** Assembly, linking, validation, and screenshot capture for NES lessons.

**The main workflow provides:** Planning, creation, integration, and publication steps.

**Zero tolerance for:**
- Missing iNES header (won't load)
- PPU writes outside VBlank (corruption)
- Missing reset vector (won't start)
- Unverified screenshots
