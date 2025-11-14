---
name: amiga-lesson-creation
description: Use when creating or editing Amiga AMOS BASIC lessons - enforces platform-specific compilation, validation, screenshot capture, and AMOS requirements
---

# Amiga AMOS BASIC Lesson Creation

## Overview

This skill guides creation of Amiga AMOS BASIC lessons. AMOS is Amiga-specific BASIC with built-in commands for sprites, bobs (blitter objects), screens, copper effects, and Paula audio. Far more powerful than C64/ZX BASIC but still accessible gateway language. FS-UAE emulator for testing.

## When to Use

- Creating/editing Amiga AMOS BASIC lessons
- **NOT** for 68000 assembly (use amiga-68k-lesson-creation)

## Prerequisites

1. **lesson-creation-workflow skill**
2. **Curriculum:** `/docs/commodore-amiga/PHASE-N-CURRICULUM.md`
3. **Tools:** AMOS Pro (in emulator), FS-UAE emulator, Python 3 validator

## AMOS BASIC Rules

### 1. AMOS-Specific Commands

**Screen management:**
```basic
Screen Open 0,320,256,16,Lowres    : Rem Open screen
Curs Off                           : Rem Hide cursor
Cls 0                              : Rem Clear to colour 0
```

**Sprite commands:**
```basic
Sprite 0,X,Y,1                     : Rem Hardware sprite 0
```

**Bob commands (blitter objects):**
```basic
Bob 1,X,Y,1                        : Rem Software sprite (bob)
```

**Audio:**
```basic
Music 1                            : Rem Play music bank 1
Sam Play 1                         : Rem Play sample 1
```

### 2. Screen Modes

**Amiga display modes:**
- Lowres: 320×256 (or 320×200 NTSC)
- Hires: 640×256
- Up to 32 colours on screen (from 4096 palette)
- Multiple screens (dual playfield)

### 3. Blitter Acceleration

**AMOS uses blitter for:**
- Bob movement (fast software sprites)
- Screen scrolling
- Block copies
- Much faster than CPU-only

**Space efficiency: Blitter is fast but plan data structures carefully.**

## Required Files Checklist

- [ ] `/website/src/pages/commodore-amiga/phase-X/tier-Y/lesson-NNN.mdx`
- [ ] `/code-samples/commodore-amiga/phase-X/tier-Y/lesson-NNN/example-1.amos` or `.abk`
- [ ] `/code-samples/commodore-amiga/phase-X/tier-Y/lesson-NNN/example-1.adf` (Amiga disk image)
- [ ] `/website/public/images/commodore-amiga/phase-X/tier-Y/lesson-NNN/screenshot-1.png`

## Compilation Process

**AMOS requires Amiga environment:**

### Option 1: AMOS Pro in Emulator

```bash
# Run FS-UAE with AMOS Pro disk
fs-uae --amiga-model=A1200 amos-pro.adf

# Load .amos file in AMOS Pro
# Test/save as .adf
```

### Option 2: AMOS Tokenizer Tools

```bash
# If tokenizer tools available
amos-tokenize example-1.amos -o example-1.abk
```

**Semantic validation:**
```bash
python3 /scripts/validate-amiga-amos.py example-1.amos
```

**Checks:**
- AMOS command syntax
- Screen dimensions valid
- Sprite/bob limits
- Audio bank references
- Memory management
- Intuition/Workbench compatibility

## Screenshot Capture (FS-UAE - Manual)

```bash
# Load disk image
fs-uae --amiga-model=A1200 example-1.adf

# Run program, capture screenshot via menu
# Save to /website/public/images/commodore-amiga/.../screenshot-1.png
```

## AMOS-Specific Validation

### Hardware Sprites vs Bobs

**Hardware sprites:** 8 available, simple, fast
**Bobs:** Unlimited (blitter-drawn), more flexible, slightly slower

**Choose based on need:**
- Simple objects → Hardware sprites
- Many objects → Bobs
- Mixed approach often best

### Screen Memory Management

**Multiple screens possible:**
```basic
Screen Open 0,320,256,16,Lowres
Screen Open 1,320,256,4,Lowres
Screen Display 0
```

**Don't waste memory: Each screen consumes chip RAM.**

### Paula Audio

**4 channels, sample playback:**
```basic
Sam Bank 1                         : Rem Load sample bank
Sam Play 1,1                       : Rem Play sample 1, channel 1
```

**Music:**
```basic
Music 1                            : Rem Play music module
Music Off                          : Rem Stop music
```

## Anti-Patterns

### 1. Not Using Blitter

**Anti-pattern:**
```basic
For I=0 To 100
  Plot X+I,Y                       : Rem Slow CPU plotting
Next I
```

**Fix:**
```basic
Draw X,Y To X+100,Y                : Rem Blitter-accelerated
```

### 2. Too Many Screens

**Anti-pattern:**
```basic
Screen Open 0,320,256,32,Lowres
Screen Open 1,640,512,16,Hires    : Rem Huge memory waste!
```

**Fix:**
```basic
Screen Open 0,320,256,16,Lowres   : Rem One screen, reasonable depth
```

### 3. Not Closing Resources

**Anti-pattern:**
```basic
Screen Open 0,320,256,16,Lowres
End                                : Rem Screen left open!
```

**Fix:**
```basic
Screen Close 0
End
```

### 4. Ignoring Chip/Fast RAM Distinction

**Principle: Chip RAM is precious (graphics/audio), Fast RAM is abundant (code/data).**

### 5. Wasting Blitter Bandwidth

**Principle: Blitter is fast but not infinite - plan sprite counts and sizes.**

## Complete Workflow Checklist

1. **Preparation:** Read curriculum, create directories
2. **Code Creation:** Write .amos, test in AMOS Pro/emulator
3. **Screenshot:** Manual capture with FS-UAE
4. **Lesson MDX:** Explain AMOS advantages over C64/ZX BASIC
5. **Validation:** Run all validation skills
6. **File Verification:** ls all locations
7. **Navigation Update:** Update indexes

## Quick Reference

### AMOS Commands
```basic
Screen Open 0,320,256,16,Lowres
Curs Off
Cls 0
Sprite 0,X,Y,1
Bob 1,X,Y,1
Draw X1,Y1 To X2,Y2
Music 1
Sam Play 1
Wait Vbl
Screen Close 0
```

### Limits
- Hardware sprites: 8
- Bobs: Limited by memory/blitter
- Colours on screen: 32 (from 4096 palette)
- Audio channels: 4

## Common Mistakes

1. **Not using blitter** - Slow CPU plotting
2. **Too many/large screens** - Chip RAM waste
3. **Not closing resources** - Memory leaks
4. **Ignoring chip/fast RAM** - Wrong allocation
5. **Exceeding sprite limits** - Visual glitches

## Platform-Specific Resources

**Essential docs:**
- `/docs/AMIGA-QUICK-REFERENCE.md` - AMOS commands, hardware
- `/docs/68000-QUICK-REFERENCE.md` - For assembly (not AMOS)
- `/docs/START-HERE.md` - Navigation

## The Bottom Line

**Amiga AMOS BASIC lessons require:**
1. AMOS Pro testing in FS-UAE
2. AMOS-specific commands (Screen Open, Sprite, Bob, etc.)
3. Blitter-aware programming
4. Chip RAM conservation
5. FS-UAE manual screenshot capture
6. Resource cleanup (Screen Close, etc.)
7. British English (except "program")

**Zero tolerance for:**
- Ignoring blitter (slow code)
- Wasting chip RAM (multiple huge screens)
- Not closing resources (memory leaks)
- Unverified screenshots
- American spellings (except "program")

**Every AMOS lesson must run in FS-UAE, use Amiga-specific features (sprites/bobs/blitter), and display expected output. AMOS is vastly more capable than C64/ZX BASIC - embrace the hardware.**
