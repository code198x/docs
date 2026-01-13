# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

"Code Like It's 198x" - Retro game development education platform teaching programming through complete, playable games across vintage computing platforms.

**Curriculum Model:**
- Each platform has a sequence of complete games, ordered by complexity
- Each game contains 8, 16, or 32 units (60-120 minutes each)
- Each unit produces a working, runnable result
- Skills compound through the game sequence

**Platforms:**
- Commodore 64 (16 games + optional BASIC gateway)
- Sinclair ZX Spectrum (curriculum TBD)
- Commodore Amiga (curriculum TBD)
- Nintendo Entertainment System (assembly only, curriculum TBD)

See `/docs/CURRICULUM-SPECIFICATION.md` for the full curriculum model.

---

## Tech Stack

- **Website**: Astro 5.16+ with MDX content
- **Routing**: File-based in `/website/src/pages/` (no complex collections)
- **Code Samples**: Single source of truth in `/code-samples/`, imported via `CodeFromFile` component
- **Assembly Tools**: Docker containers per platform (ACME for C64, pasmonext for ZX, ca65 for NES, vasm for Amiga)
- **Version Control**: 7 separate git repositories (see below)

---

## Repositories

All repos live under `/Users/stevehill/Projects/Code198x/`:

| Repo | Purpose | Assembler/Tools |
|------|---------|-----------------|
| `website` | Astro site | — |
| `code-samples` | Working code for each unit | — |
| `docs` | Specifications & references | — |
| `commodore-64-dev` | Docker toolchain | ACME |
| `sinclair-zx-spectrum-dev` | Docker toolchain | pasmonext |
| `commodore-amiga-dev` | Docker toolchain | vasm |
| `nintendo-entertainment-system-dev` | Docker toolchain | ca65 |

**When committing:** Check all 7 repos with `git status`.

---

## Essential Commands

```bash
# Website Development (from /website directory)
npm install              # Install dependencies
npm run dev              # Dev server at localhost:4321
npm run build            # Production build
npm run preview          # Preview production build

# Docker Assembly Environment (from root)
docker-compose up -d                        # Start containers
docker-compose exec workspace bash          # Enter workspace
```

### ZX Spectrum Build and Screenshot Commands

```bash
# Build ZX Spectrum snapshot (pasmonext assembler)
docker run --rm \
  -v /Users/stevehill/Projects/Code198x/code-samples:/code-samples \
  ghcr.io/code198x/sinclair-zx-spectrum:latest \
  pasmonext --sna /code-samples/sinclair-zx-spectrum/game-01-ink-war/unit-XX/inkwar.asm \
                  /code-samples/sinclair-zx-spectrum/game-01-ink-war/unit-XX/inkwar.sna

# Capture screenshot (title screen only)
docker run --rm \
  -v /Users/stevehill/Projects/Code198x/code-samples:/code-samples \
  -v /Users/stevehill/Projects/Code198x/website/public/images:/images \
  ghcr.io/code198x/sinclair-zx-spectrum:latest \
  spectrum-screenshot \
    /code-samples/sinclair-zx-spectrum/game-01-ink-war/unit-XX/inkwar.sna \
    /images/sinclair-zx-spectrum/game-01-ink-war/unit-XX/screenshot.png \
    --wait 1

# Capture screenshot with input injection (skip title, show gameplay)
docker run --rm \
  -v /Users/stevehill/Projects/Code198x/code-samples:/code-samples \
  -v /Users/stevehill/Projects/Code198x/website/public/images:/images \
  ghcr.io/code198x/sinclair-zx-spectrum:latest \
  spectrum-screenshot \
    /code-samples/sinclair-zx-spectrum/game-01-ink-war/unit-XX/inkwar.sna \
    /images/sinclair-zx-spectrum/game-01-ink-war/unit-XX/screenshot.png \
    --wait 2 --input /scripts/inputs/claim-cells.sh
```

**Input Scripts** (in `/sinclair-zx-spectrum-dev/scripts/inputs/`):
- `claim-cells.sh` - Skip title screen, claim several cells to show gameplay

### C64 Build and Screenshot Commands

**Note:** Use `c64-dev:latest` (built locally from `commodore-64-dev/`). Build with: `cd commodore-64-dev && docker build -t c64-dev:latest .`

**Requires:** C64 ROMs extracted to `/tmp/c64roms/`:
- `kernal-901227-03.bin`
- `basic-901226-01.bin`
- `chargen-901225-01.bin`

```bash
# Build C64 PRG (ACME assembler)
docker run --rm \
  -v /Users/stevehill/Projects/Code198x/code-samples:/code-samples \
  c64-dev:latest \
  acme -f cbm -l /code-samples/commodore-64/game-01-sid-symphony/unit-XX/labels.txt \
  -o /code-samples/commodore-64/game-01-sid-symphony/unit-XX/symphony.prg \
  /code-samples/commodore-64/game-01-sid-symphony/unit-XX/symphony.asm

# Capture C64 screenshot (inline - handles ROMs, Xvfb, VICE, and scaling)
docker run --rm \
  -v /Users/stevehill/Projects/Code198x/code-samples:/code-samples \
  -v /Users/stevehill/Projects/Code198x/website/public/images:/images \
  -v /tmp/c64roms:/roms \
  c64-dev:latest bash -c "
cp /roms/*.bin /usr/share/vice/C64/
Xvfb :99 -screen 0 1024x768x24 &>/dev/null &
sleep 1
export DISPLAY=:99
x64sc -limitcycles 3500000 \
  -exitscreenshot /tmp/raw.png \
  -autostartprgmode 1 \
  -warp \
  +sound \
  /code-samples/commodore-64/game-01-sid-symphony/unit-XX/symphony.prg 2>/dev/null
convert /tmp/raw.png -filter point -resize 200% /images/commodore-64/game-01-sid-symphony/unit-XX/screenshot.png
"
```

**Key VICE flags:**
- `-limitcycles 3500000` - Run for ~3.5 seconds (PAL cycles)
- `-autostartprgmode 1` - Inject PRG directly into RAM
- `-exitscreenshot /path` - Save screenshot on exit
- `-warp` - Run at maximum speed
- `+sound` - Disable sound (faster, no audio errors)

### NES Build and Screenshot Commands

```bash
# Build NES ROM (ca65 assembler)
docker run --rm \
  -v /Users/stevehill/Projects/Code198x/code-samples:/code-samples \
  code198x/nintendo-entertainment-system:latest \
  bash -c "cd /code-samples/nintendo-entertainment-system/game-01-neon-nexus/unit-XX && \
           ca65 nexus.asm -o nexus.o && \
           ld65 -C nes.cfg nexus.o -o nexus.nes"

# Capture NES screenshot
docker run --rm \
  -v /Users/stevehill/Projects/Code198x/code-samples:/code-samples \
  -v /Users/stevehill/Projects/Code198x/website/public/images:/images \
  code198x/nintendo-entertainment-system:latest \
  nes-screenshot \
    /code-samples/nintendo-entertainment-system/game-01-neon-nexus/unit-XX/nexus.nes \
    /images/nintendo-entertainment-system/game-01-neon-nexus/unit-XX/screenshot.png \
    --wait 2 --crop
```

### Amiga Build, Screenshot, and Video Commands

**Note:** Use `amiga-dev:latest` (built locally from `commodore-amiga-dev/`). Build with: `cd commodore-amiga-dev && docker build -t amiga-dev:latest .`

```bash
# Build Amiga executable (vasm assembler)
# IMPORTANT: Use -kick1hunks for Kickstart 1.x compatibility
docker run --rm --entrypoint="" \
  -v /Users/stevehill/Projects/Code198x/code-samples:/code-samples \
  amiga-dev:latest \
  /bin/bash -c "cd /code-samples/commodore-amiga/game-01-signal/unit-XX && \
           vasmm68k_mot -Fhunkexe -kick1hunks -o signal signal.asm"

# Create bootable ADF disk image
docker run --rm --entrypoint="" \
  -v /Users/stevehill/Projects/Code198x/code-samples:/code-samples \
  amiga-dev:latest \
  /bin/bash -c "cd /code-samples/commodore-amiga/game-01-signal/unit-XX && \
           echo 'signal' > startup-sequence && \
           rm -f signal.adf && \
           xdftool signal.adf create && \
           xdftool signal.adf format 'Signal' && \
           xdftool signal.adf makedir s && \
           xdftool signal.adf boot install && \
           xdftool signal.adf write startup-sequence s/startup-sequence && \
           xdftool signal.adf write signal && \
           xdftool signal.adf protect signal e && \
           rm startup-sequence"

# Capture Amiga screenshot (requires Kickstart ROM at /tmp/kickstart/kick13.rom)
# Extract ROM first: cp "/path/to/Kickstart v1.3...rom" /tmp/kickstart/kick13.rom
docker run --rm --entrypoint="" \
  -v /Users/stevehill/Projects/Code198x/code-samples:/code-samples \
  -v /tmp/kickstart:/roms \
  -v /Users/stevehill/Projects/Code198x/website/public/images:/images \
  -v /Users/stevehill/Projects/Code198x/commodore-amiga-dev/scripts:/scripts \
  amiga-dev:latest \
  /bin/bash -c "/scripts/amiga-screenshot.sh \
    /code-samples/commodore-amiga/game-01-signal/unit-XX/signal.adf \
    /images/commodore-amiga/game-01-signal/unit-XX/screenshot.png \
    --wait 12"

# Capture Amiga video (with input injection to skip title screen)
docker run --rm --entrypoint="" \
  -v /Users/stevehill/Projects/Code198x/code-samples:/code-samples \
  -v /tmp/kickstart:/roms \
  -v /Users/stevehill/Projects/Code198x/website/public/videos:/videos \
  -v /Users/stevehill/Projects/Code198x/commodore-amiga-dev/scripts:/scripts \
  amiga-dev:latest \
  /bin/bash -c "/scripts/amiga-video.sh \
    /code-samples/commodore-amiga/game-01-signal/unit-XX/signal.adf \
    /videos/commodore-amiga/game-01-signal/unit-XX/gameplay.mp4 \
    --wait 12 --duration 15 --input /scripts/inputs/skip-title.sh"
```

**Input Scripts** (in `/commodore-amiga-dev/scripts/inputs/`):
- `skip-title.sh` - Press fire to skip title screen (Units 15-16)
- `demo-movement.sh` - Basic frog movement demo (Units 2-14)
- `signal-gameplay.sh` - Full gameplay demo with navigation

**Amiga DMACON Reference:**
- `$83a0` = Master + Copper + Sprites **+ Bitplanes** (DMAEN | BPLEN | COPEN | SPREN) - **USE THIS for sprites to work!**
- `$8280` = Master + Copper only (DMAEN | COPEN)
- `$83e0` = All DMA (DMAEN | BPLEN | COPEN | BLTEN | SPREN)

**IMPORTANT:** Even without bitplane graphics, sprites need BPLEN ($0100) enabled to render correctly.

---

## Repository Structure

```
Code198x/
├── website/                          # Astro website
├── code-samples/                     # Working code for each unit
├── docs/                             # Specifications & references
│   ├── platforms/                    # Platform-specific refs
│   ├── curriculum/                   # Game sequences (AUTHORITATIVE)
│   └── [specifications]              # CURRICULUM, UNIT, VAULT, PATTERN-LIBRARY
├── commodore-64-dev/                 # Docker toolchain (ACME)
├── sinclair-zx-spectrum-dev/         # Docker toolchain (pasmonext)
├── commodore-amiga-dev/              # Docker toolchain (vasm)
└── nintendo-entertainment-system-dev/ # Docker toolchain (ca65)
```

---

## Key Documentation Locations

### Specifications
- **Curriculum Model:** `/docs/CURRICULUM-SPECIFICATION.md` (how curricula work)
- **Unit Formatting:** `/docs/UNIT-SPECIFICATION.md` (how to format unit files)
- **Pattern Library:** `/docs/PATTERN-LIBRARY-SPECIFICATION.md`
- **Vault:** `/docs/VAULT-SPECIFICATION.md`

### Platform Curricula (AUTHORITATIVE for content)
- `/docs/curriculum/commodore-64-curriculum.md`
- `/docs/curriculum/sinclair-zx-spectrum-curriculum.md`
- `/docs/curriculum/commodore-amiga-curriculum.md`
- `/docs/curriculum/nintendo-nes-curriculum.md`

### Platform-Specific References
All organised under `/docs/platforms/[platform-name]/`:
- **C64:** hardware/, basic-v2/, graphics/, memory-and-io/, advanced/, tools/
- **ZX Spectrum:** language/, hardware/
- **Amiga:** language/, hardware/
- **NES:** hardware/

---

## Reference Document Strategy

**Platform-specific references are organised by platform:**

### Commodore 64
**Quick References** (for unit creation):
- Joystick/keyboard: `/docs/platforms/commodore-64/hardware/CIA-QUICK-REFERENCE.md`
- Sprites/colours: `/docs/platforms/commodore-64/hardware/VIC-II-QUICK-REFERENCE.md`
- Assembly instructions: `/docs/platforms/commodore-64/hardware/6510-QUICK-REFERENCE.md`
- Character codes: `/docs/platforms/commodore-64/hardware/PETSCII-AND-SCREEN-CODES.md`

**Common Errors:**
- BASIC V2: `/docs/platforms/commodore-64/basic-v2/C64-COMMON-ERRORS.md`
- 6510 Assembly: `/docs/platforms/commodore-64/advanced/6510-COMMON-ERRORS.md`

### Other Platforms
See `/docs/platforms/[platform-name]/` for platform-specific quick references and common errors documentation.

---

## Content Standards

### British English
- Use British spelling: colour, learnt, centre, organise
- **Exception:** "program" for computer programs (not "programme")
- Validate: `grep -E "color|behavior|center|organize" file.md`

### Code Sample Standards
- **Line numbers:** No indentation - all line numbers flush left
- **Keywords in .bas files:** Lowercase for compatibility (`poke`, `print`)
- **Keywords in MDX units:** Uppercase for readability (`POKE`, `PRINT`)
- **Progressive complexity:** Simple example → Complex example

### Screenshot Standards
- **Mandatory verification:** Use Read tool to view EVERY screenshot
- **Check for errors:** Look for error messages, blank screens, crashes
- **Document verification:** "Used Read tool - screenshot shows [specific elements]. NO error messages visible."
- **Never claim verification without evidence**

---

## CodeFromFile Architecture

**Code samples live in `/code-samples/`, not inline in MDX files.**

This prevents drift between lesson code and downloadable samples.

### Structure
```
code-samples/{platform}/{game}/{unit}/
  {main}.asm           # Complete runnable code
  snippets/
    01-section-name.asm
    02-section-name.asm
```

### Usage in MDX
```mdx
import CodeFromFile from "@components/CodeFromFile.astro";

<CodeFromFile src="commodore-64/game-01-sid-symphony/unit-08/symphony.asm" />
<CodeFromFile src="commodore-64/game-01-sid-symphony/unit-08/snippets/01-game-states.asm" />
```

### Language Auto-Detection
The component infers the correct syntax highlighting from the file path:
- `sinclair-zx-spectrum/*.asm` → Z80
- `commodore-amiga/*.asm` → 68000
- `nintendo-entertainment-system/*.asm` → ca65
- `commodore-64/*.asm` → 6502

---

## Common Pitfalls (Cross-Platform)

### Curriculum Drift
- ❌ Creating units that don't match curriculum specifications
- ✅ Always read curriculum FIRST, create unit that matches spec

### Unverified Code
- ❌ Writing code without compiling/testing
- ✅ Compile with platform tools, capture screenshots, verify output

### Screenshot Issues
- ❌ Screenshots showing error messages or blank screens
- ✅ Use Read tool to verify every screenshot shows correct output

### Language Inconsistency
- ❌ Mixing American and British English spellings
- ✅ Check with `grep -E "color|behavior|center|organize" file.md`

### Missing Files
- ❌ Creating unit without all required files in all locations
- ✅ Verify files in code-samples/, website/public/images/, and unit MDX

---

**Version:** 5.4
**Last Updated:** 2026-01-13
**Status:** Added C64 build and screenshot commands
