---
name: amiga-amos-lesson-creation
description: Use when creating or editing Amiga AMOS BASIC lessons - provides platform-specific compilation, validation, and screenshot capture for Phase 3 of the content creation workflow
---

# Amiga AMOS BASIC Lesson Creation

**Role:** Technical execution for Phase 3 (Validation) of the Content Creation Workflow.

**Prerequisite:** Read `/docs/CONTENT-CREATION-WORKFLOW.md` first. This skill provides AMOS-specific technical details, not the full workflow.

---

## When to Use

Use this skill during **Phase 3 (Validation)** when:
- Testing AMOS code in FS-UAE emulator
- Capturing screenshots with FS-UAE
- Validating AMOS-specific syntax
- Checking for Amiga-specific pitfalls

**Do NOT use for:**
- 68000 Assembly lessons (use `68k-lesson-creation` skill)
- Other platforms (use platform-specific skills)

---

## AMOS BASIC Rules

### Screen Management

```basic
Screen Open 0,320,256,16,Lowres    : Rem Open screen
Curs Off                           : Rem Hide cursor
Cls 0                              : Rem Clear to colour 0
Screen Close 0                     : Rem Clean up
```

### Hardware Sprites vs Bobs

**Hardware sprites:** 8 available, fast, simple
**Bobs (blitter objects):** Unlimited, flexible, blitter-drawn

```basic
Sprite 0,X,Y,1                     : Rem Hardware sprite
Bob 1,X,Y,1                        : Rem Software sprite (bob)
```

### Audio

```basic
Music 1                            : Rem Play music bank 1
Sam Play 1                         : Rem Play sample 1
Music Off                          : Rem Stop music
```

### Screen Modes

- Lowres: 320×256 (or 320×200 NTSC)
- Hires: 640×256
- Up to 32 colours on screen (from 4096 palette)

---

## Phase 3: Validation (Technical Details)

### Step 3.1: Semantic Validation

```bash
python3 /scripts/validate-amiga-amos.py example-1.amos
```

**Checks:**
- ✅ AMOS command syntax
- ✅ Screen dimensions valid
- ✅ Sprite/bob limits
- ✅ Resource cleanup (Screen Close)
- ✅ Memory management

### Step 3.2: Testing (AMOS Pro in Emulator)

```bash
# Run FS-UAE with AMOS Pro disk
fs-uae --amiga-model=A1200 amos-pro.adf

# Load .amos file in AMOS Pro
# Test/save as .adf
```

### Step 3.3: Screenshot Capture (FS-UAE - Manual)

```bash
fs-uae --amiga-model=A1200 example-1.adf
```

1. Run program
2. Capture via FS-UAE menu
3. Save to `/website/public/images/commodore-amiga/phase-X/tier-Y/lesson-NNN/screenshot-1.png`

### Step 3.4: Screenshot Verification (MANDATORY)

**Use Read tool to VIEW every screenshot:**

```
✅ CORRECT: "Read screenshot-1.png - shows Amiga screen with sprites,
   32 colours visible, no Guru Meditation error."

❌ WRONG: "Screenshot verified ✅" (too vague)
```

---

## Chip RAM vs Fast RAM

**Chip RAM:** Graphics, audio, sprites (limited, precious)
**Fast RAM:** Code, data (abundant)

```basic
❌ WRONG:
Screen Open 0,640,512,32,Hires     : Rem Huge chip RAM waste!

✅ CORRECT:
Screen Open 0,320,256,16,Lowres    : Rem Conservative
```

---

## Common Pitfalls

### 1. Not Using Blitter
```basic
❌ WRONG:
For I=0 To 100 : Plot X+I,Y : Next  ; Slow CPU plotting

✅ CORRECT:
Draw X,Y To X+100,Y                 ; Blitter-accelerated
```

### 2. Not Closing Resources
```basic
❌ WRONG:
Screen Open 0,320,256,16,Lowres
End                                 ; Screen left open!

✅ CORRECT:
Screen Open 0,320,256,16,Lowres
; ... code ...
Screen Close 0
End
```

### 3. Too Many/Large Screens
```basic
❌ WRONG:
Screen Open 0,320,256,32,Lowres
Screen Open 1,640,512,16,Hires     ; Memory exhausted!

✅ CORRECT:
Screen Open 0,320,256,16,Lowres    ; One reasonable screen
```

---

## Required Files

| File | Location |
|------|----------|
| Lesson MDX | `/website/src/pages/commodore-amiga/phase-X/tier-Y/lesson-NNN.mdx` |
| Source (.amos) | `/code-samples/commodore-amiga/phase-X/tier-Y/lesson-NNN/example-1.amos` |
| Disk image (.adf) | `/code-samples/commodore-amiga/phase-X/tier-Y/lesson-NNN/example-1.adf` |
| Screenshot | `/website/public/images/commodore-amiga/phase-X/tier-Y/lesson-NNN/screenshot-1.png` |

---

## Quick Reference Commands

```bash
# Semantic validation
python3 /scripts/validate-amiga-amos.py example-1.amos

# Test in emulator
fs-uae --amiga-model=A1200 example-1.adf

# Screenshot via FS-UAE menu
```

### AMOS Commands Summary

```basic
Screen Open 0,320,256,16,Lowres
Curs Off : Cls 0
Sprite 0,X,Y,1
Bob 1,X,Y,1
Draw X1,Y1 To X2,Y2
Music 1 : Sam Play 1
Wait Vbl
Screen Close 0
```

---

## Platform-Specific Resources

**Quick references** (in `/docs/platforms/commodore-amiga/`):
- `language/AMOS-QUICK-REFERENCE.md` - Commands, syntax
- `hardware/AMIGA-HARDWARE-REFERENCE.md` - Custom chips

---

## The Bottom Line

**This skill provides:** Testing, validation, and screenshot capture for AMOS lessons.

**The main workflow provides:** Planning, creation, integration, and publication steps.

**Zero tolerance for:**
- Not using blitter (slow code)
- Wasting chip RAM
- Not closing resources
- Unverified screenshots
