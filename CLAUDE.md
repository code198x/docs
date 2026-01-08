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

**Version:** 5.1
**Last Updated:** 2026-01-08
**Status:** Added all 7 repositories to documentation
