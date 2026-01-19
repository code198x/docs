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

- **Website**: Astro 5.x with MDX content
- **Routing**: File-based in `/website/src/pages/`
- **Data**: Astro content collections for games, units, platforms, vault, patterns
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

**Build uses Docker; screenshot/video uses native spectrum-emu.**

```bash
# Build ZX Spectrum snapshot (pasmonext assembler - Docker)
docker run --rm \
  -v /Users/stevehill/Projects/Code198x/code-samples:/code-samples \
  ghcr.io/code198x/sinclair-zx-spectrum:latest \
  pasmonext --sna /code-samples/sinclair-zx-spectrum/game-01-ink-war/unit-XX/inkwar.asm \
                  /code-samples/sinclair-zx-spectrum/game-01-ink-war/unit-XX/inkwar.sna

# Capture screenshot (native spectrum-emu)
~/Projects/spectrum-emu/target/release/spectrum-screenshot \
  /Users/stevehill/Projects/Code198x/code-samples/sinclair-zx-spectrum/game-01-ink-war/unit-XX/inkwar.sna \
  /Users/stevehill/Projects/Code198x/website/public/images/sinclair-zx-spectrum/game-01-ink-war/unit-XX/screenshot.png \
  --wait 50

# Capture screenshot with input injection (skip title, show gameplay)
~/Projects/spectrum-emu/target/release/spectrum-screenshot \
  /Users/stevehill/Projects/Code198x/code-samples/sinclair-zx-spectrum/game-01-ink-war/unit-XX/inkwar.sna \
  /Users/stevehill/Projects/Code198x/website/public/images/sinclair-zx-spectrum/game-01-ink-war/unit-XX/screenshot.png \
  --input /Users/stevehill/Projects/Code198x/code-samples/sinclair-zx-spectrum/game-01-ink-war/unit-XX/inputs/gameplay.txt

# Capture video with audio (native spectrum-emu)
~/Projects/spectrum-emu/target/release/spectrum-video \
  /Users/stevehill/Projects/Code198x/code-samples/sinclair-zx-spectrum/game-01-ink-war/unit-XX/inkwar.sna \
  /Users/stevehill/Projects/Code198x/website/public/videos/sinclair-zx-spectrum/game-01-ink-war/unit-XX/gameplay.mp4 \
  --wait 50 --duration 500 \
  --input /Users/stevehill/Projects/Code198x/code-samples/sinclair-zx-spectrum/game-01-ink-war/unit-XX/inputs/gameplay.txt
```

**spectrum-screenshot options:**
- `--wait, -w N` - Wait N frames before capture (default: 0)
- `--input, -i FILE` - Execute input script from file

**spectrum-video options:**
- `--wait, -w N` - Wait N frames before recording (default: 0)
- `--duration, -d N` - Record for N frames (default: 500, ~10 seconds at 50fps)
- `--input, -i FILE` - Execute input script from file
- `--fps N` - Output frame rate (default: 50)
- `--scale, -s N` - Scale factor 1-4 (default: 2)
- `--no-audio` - Disable audio capture

**Supported formats:** `.sna`, `.z80`, `.tap`, `.tzx`

**Input Script Format** (text file, one action per line):
```text
# Comment
wait 50              # Wait 50 frames
tap Space 10         # Press Space for 10 frames
tap Q 10             # Press Q for 10 frames
key_down O           # Hold O key down
wait 20
key_up O             # Release O key
joy_tap Fire 5       # Joystick fire for 5 frames
```

**Input scripts location:** Store alongside code samples in `inputs/` subdirectory:
```
code-samples/sinclair-zx-spectrum/game-01-ink-war/unit-XX/
  inkwar.asm
  inkwar.sna
  inputs/
    title-screen.txt    # Show title only
    gameplay.txt        # Skip title, show gameplay
```

### C64 Build and Screenshot Commands

**Note:** Use `c64-dev:latest` (built locally from `commodore-64-dev/`). Build with: `cd commodore-64-dev && docker build -t c64-dev:latest .`

**Requires:** C64 ROMs in `/commodore-64-dev/roms/` (gitignored, never commit):
- `kernal-901227-03.bin`
- `basic-901226-01.bin`
- `chargen-901225-01.bin`

Original zipped ROMs available at `~/Projects/Code198x/C64/Firmware/`. Extract and rename to the above filenames.

```bash
# Build C64 PRG (ACME assembler)
docker run --rm \
  -v /Users/stevehill/Projects/Code198x/code-samples:/code-samples \
  c64-dev:latest \
  acme -f cbm -o /code-samples/commodore-64/game-01-sid-symphony/unit-XX/symphony.prg \
  /code-samples/commodore-64/game-01-sid-symphony/unit-XX/symphony.asm

# Capture C64 screenshot (title screen)
docker run --rm \
  -v /Users/stevehill/Projects/Code198x/code-samples:/code-samples \
  -v /Users/stevehill/Projects/Code198x/website/public/images:/images \
  -v /Users/stevehill/Projects/Code198x/commodore-64-dev/roms:/roms \
  -v /Users/stevehill/Projects/Code198x/commodore-64-dev/scripts:/scripts \
  -w /code-samples/commodore-64/game-01-sid-symphony/unit-XX \
  c64-dev:latest bash /scripts/c64-screenshot.sh \
    symphony.asm \
    /images/commodore-64/game-01-sid-symphony/unit-XX/screenshot.png

# Capture C64 screenshot (skip title, show menu/gameplay)
# Games with SCREENSHOT_MODE support will skip directly to the menu
docker run --rm \
  -v /Users/stevehill/Projects/Code198x/code-samples:/code-samples \
  -v /Users/stevehill/Projects/Code198x/website/public/images:/images \
  -v /Users/stevehill/Projects/Code198x/commodore-64-dev/roms:/roms \
  -v /Users/stevehill/Projects/Code198x/commodore-64-dev/scripts:/scripts \
  -w /code-samples/commodore-64/game-01-sid-symphony/unit-XX \
  c64-dev:latest bash /scripts/c64-screenshot.sh \
    symphony.asm \
    /images/commodore-64/game-01-sid-symphony/unit-XX/screenshot.png \
    --define SCREENSHOT_MODE=1
```

**Screenshot Mode:**
Games from Unit 17+ support `SCREENSHOT_MODE` compile-time flag:
- When `SCREENSHOT_MODE=1`, the game skips the title screen and shows the menu
- Add to game source: `!ifndef SCREENSHOT_MODE { SCREENSHOT_MODE = 0 }`
- Use conditional: `!if SCREENSHOT_MODE = 1 { ... } else { ... }`

**c64-screenshot.sh options:**
- `--define KEY=VALUE` - Pass define to ACME assembler
- `--cycles N` - CPU cycles before capture (default: 5000000)

```bash
# Capture C64 video (with input injection)
docker run --rm \
  -v /Users/stevehill/Projects/Code198x/code-samples:/code-samples \
  -v /Users/stevehill/Projects/Code198x/website/public/videos:/videos \
  -v /Users/stevehill/Projects/Code198x/commodore-64-dev/roms:/roms \
  -v /Users/stevehill/Projects/Code198x/commodore-64-dev/scripts:/scripts \
  -w /code-samples/commodore-64/game-01-sid-symphony/unit-XX \
  c64-dev:latest bash /scripts/c64-video.sh \
    symphony.asm \
    /videos/commodore-64/game-01-sid-symphony/unit-XX/gameplay.mp4 \
    --wait 5 --duration 20 --input /scripts/inputs/symphony-demo.sh
```

**c64-video.sh options:**
- `--wait SECONDS` - Wait before recording (default: 5)
- `--duration SECONDS` - Recording length (default: 10)
- `--input SCRIPT` - Input injection script
- `--define KEY=VALUE` - Pass define to ACME assembler
- `--fps N` - Frame rate (default: 50)
- `--scale N` - Scale factor 1-4 (default: 2)
- `--joystick PORT` - Joystick port 1 or 2 (default: 2)

**Input Scripts** (in `/commodore-64-dev/scripts/inputs/`):
- `symphony-demo.sh` - Navigate menu and play notes in SID Symphony

**Joystick Mapping:** Arrow keys for directions, Right Ctrl for fire.

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

# Capture NES video (with input injection)
docker run --rm \
  -v /Users/stevehill/Projects/Code198x/code-samples:/code-samples \
  -v /Users/stevehill/Projects/Code198x/website/public/videos:/videos \
  -v /Users/stevehill/Projects/Code198x/nintendo-entertainment-system-dev/scripts:/scripts \
  code198x/nintendo-entertainment-system:latest \
  nes-video \
    /code-samples/nintendo-entertainment-system/game-01-neon-nexus/unit-XX/nexus.nes \
    /videos/nintendo-entertainment-system/game-01-neon-nexus/unit-XX/gameplay.mp4 \
    --wait 3 --duration 15 --input /scripts/inputs/start-game.sh
```

**nes-video.sh options:**
- `--wait SECONDS` - Wait before recording (default: 3)
- `--duration SECONDS` - Recording length (default: 10)
- `--input SCRIPT` - Input injection script
- `--fps N` - Frame rate (default: 60)
- `--scale N` - Scale factor 1-4 (default: 2)

**Input Scripts** (in `/nintendo-entertainment-system-dev/scripts/inputs/`):
- `start-game.sh` - Press Start to begin game

**Controller Mapping:** Arrow keys = D-pad, Z = A, X = B, Return = Start, Shift = Select.

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

## Content Collections

The website uses Astro content collections for structured data. Collections are defined in `/website/src/content/config.ts`.

### Games Collection (`src/content/games/`)

Nested by platform, one file per track. Defines game catalogue (name, tagline, skills, status). Does **not** store unit counts — those are computed from units collection.

```
games/
├── commodore-64/
│   ├── assembly.yaml    # 16 assembly games
│   └── basic.yaml       # 8 BASIC gateway games
├── sinclair-zx-spectrum/
├── commodore-amiga/
└── nintendo-entertainment-system/
```

### Units Collection (`src/content/units/`)

Nested by platform and track. One file per game. **Single source of truth** for unit counts, availability, and phase definitions.

```
units/
├── commodore-64/
│   ├── assembly/
│   │   ├── game-01-sid-symphony.yaml
│   │   └── ...
│   └── basic/
├── sinclair-zx-spectrum/
└── ...
```

### Helper Functions (`src/lib/`)

```typescript
// Games with computed counts
import { getGamesWithCounts } from '../lib/games';
const games = await getGamesWithCounts('commodore-64', 'assembly');

// Unit details
import { getUnitsEntry, getPhases, getUnits } from '../lib/units';
const entry = await getUnitsEntry('commodore-64', 'assembly', 'game-01-sid-symphony');
```

### Adding/Updating Units

1. Edit the units YAML file: `src/content/units/[platform]/[track]/[game].yaml`
2. Set `available: true` for published units
3. Unit counts are computed automatically — no need to update games collection

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

## Design Context

### Users
Learners of all ages who want to understand how computers actually work by building complete games on vintage platforms. They range from curious beginners to experienced developers seeking deeper knowledge. They come with a sense of wonder about the machines that shaped computing history, and they want to feel that same magic the original bedroom coders felt.

### Brand Personality
**Three words:** Authentic, Educational, Reverent

**Voice:** Warm but never condescending. Technical but never dry. The tone of someone who genuinely loves these machines sharing knowledge with someone who wants to understand them. We teach machines, not frameworks — and we mean it.

**Emotional goal:** Nostalgic wonder — recapturing the "magic of discovery" feeling. That moment when a kid typed in code from a magazine and watched the screen come alive. The interface should make learners feel they're about to unlock something real.

### Aesthetic Direction
**Visual tone:** Warm retro-technical. Period-appropriate without ironic pastiche. The visual language of early computing magazines (CRASH, ZZAP!64, Your Sinclair) meets modern usability.

**Key elements:**
- Platform-specific branding (C64 blue, Spectrum rainbow, NES red, Amiga orange)
- Authentic retro effects used sparingly (scanlines, copper bars, CRT glow)
- Light mode default (cream/beige evoking C64 case plastic), dark mode available
- JetBrains Mono for code, Inter for body — clean and readable
- Generous spacing, clear hierarchy, inviting rather than intimidating

**Anti-references (explicitly avoid):**
- Slick startup aesthetic: gradient blobs, excessive whitespace, generic "modern" feel
- Gaudy retro pastiche: neon vaporwave, pixel art overload, ironic kitsch
- Dense academic style: dry documentation dumps, intimidating walls of text

### Design Principles

1. **Authentic over decorative** — Retro elements should be genuine (actual platform colours, real visual effects those machines produced), not generic "pixel art" decoration. If it didn't exist on the actual hardware, question whether it belongs.

2. **Inviting over intimidating** — Assembly language is scary enough. The interface should feel approachable and warm, making complex topics feel achievable. Clear visual hierarchy, generous whitespace, progressive disclosure.

3. **Platform identity matters** — Each system has its own visual DNA. The C64 section should feel different from the Spectrum section. Use platform colours consistently; hero sections and accents should immediately signal which machine you're learning about.

4. **Substance over flash** — Avoid purely decorative animations. When motion exists, it should enhance understanding or provide subtle delight (copy button feedback, hover states). Never distract from the content.

5. **Readable code is sacred** — Code blocks are where learning happens. Dark backgrounds, clear syntax highlighting, comfortable font size. Never sacrifice code readability for aesthetic choices.

---

**Version:** 5.7
**Last Updated:** 2026-01-15
**Status:** Added Design Context section for UI/UX guidance
