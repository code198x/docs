# Code198x

Retro game dev education. Complete games on vintage platforms (C64, ZX Spectrum, Amiga, NES).

## Umbrella context

This project lives under `~/Projects/198x/` alongside `Emu198x`. The umbrella binds rules that span both projects — see [`../../CLAUDE.md`](../../CLAUDE.md) and [`../../decisions/`](../../decisions/). Most relevantly: hardware reference is **layered**. The primary library at `~/Projects/198x/reference/` is the source of truth (datasheets, manuals, magazines with sidecar metadata); `Emu198x/knowledge/` is a codebase-tied distillation; this project's `docs/platforms/` should be curriculum-flavoured and cite the library for facts. Full layered model and citation rules at [`../../decisions/shared-hardware-reference-canon.md`](../../decisions/shared-hardware-reference-canon.md).

## Launch context (October 2026 target)

October 2026 (Crash! Live) is the launch target, not a hard deadline. The project is close to having enough Spectrum content to ship. See [`decisions/october-2026-launch-spec.md`](decisions/october-2026-launch-spec.md) for scope and quality bar.

The four launch artefacts:

1. **Shadowkeep** — Spectrum assembly Volume 1 Game 1; Arcs 1+2 at 32 units at commercial bar. 8 of 32 units shipped; the remaining 24 are the main body of work. Full four-arc framing at `docs/decisions/shadowkeep-four-arc-framing.md`.
2. **Spectrum BASIC Volume 1** — 8 games at Usborne bar. **Done.** V2 work (Cipher onward) has started.
3. **Spectrum landing page** — for QR-code visitors. **Done** (initial version shipped).
4. **Spectrum vault** — review pass + referenced gap-fill. **In progress.**

No session-start gate — work on whatever makes sense. The quality bar and cut hierarchy remain valid regardless of timeline.

## Critical Rules
- **7 separate git repos** — check all with `git status` before committing
- **Code samples in `/code-samples/`** — never inline in MDX; use `CodeFromFile` component
- **British English** — colour, learnt, centre (exception: "program" not "programme")
- **Verify every screenshot** — use Read tool, check for errors, document what you see

## Repositories
| Repo | Purpose |
|------|---------|
| `website` | Astro 6.x site |
| `code-samples` | Working code per unit |
| `docs` | Specs & curriculum |
| `commodore-64-dev` | Docker + ACME |
| `sinclair-zx-spectrum-dev` | Docker + pasmonext |
| `commodore-amiga-dev` | Docker + vasm |
| `nintendo-entertainment-system-dev` | Docker + ca65 |

## Commands
```bash
# Website
cd website && npm run dev    # Dev server :4321
npm run build                # Prod build (runs Pagefind)

# Build assembly (pattern for all platforms)
docker run --rm -v $(pwd)/code-samples:/code-samples <image> <assembler> <args>
```

## Platform Build Quick Reference
| Platform | Image | Assembler | Output |
|----------|-------|-----------|--------|
| C64 | `ghcr.io/code198x/commodore-64:latest` | `acme -f cbm` | `.prg` |
| ZX Spectrum | `ghcr.io/code198x/sinclair-zx-spectrum:latest` | `pasmonext --sna` | `.sna` |
| Amiga | `ghcr.io/code198x/commodore-amiga:latest` | `vasmm68k_mot -Fhunkexe -kick1hunks` | executable |
| NES | `ghcr.io/code198x/nintendo-nes:latest` | `ca65` + `ld65` | `.nes` |

## Screenshot/Video Tools
- **C64**: Docker script `/scripts/c64-screenshot.sh` (ROMs symlinked from `~/Projects/Reference/`)
- **Amiga**: Docker script `/scripts/amiga-screenshot.sh` (requires Kickstart ROM in `~/Projects/Reference/amiga/Firmware/`)
- **NES**: Docker `nes-screenshot` command
- **ZX Spectrum**: Use Emu198x when available

Options: `--wait N` (frames), `--input FILE` (input script), `--duration N` (video)

## Content Collections
```
src/content/
├── curriculum/                          # MDX pages (units, game indexes, getting-started)
│   └── {platform}/{track}/{game}/       #   Rendered by src/pages/[...slug].astro
├── games/{platform}/{track}.yaml        # Game catalogue
└── units/{platform}/{track}/{game}.yaml # Unit details (source of truth for counts)
```

Three MDX page collections share `src/content/curriculum/` as base directory:
- `unit-pages` — `**/unit-*.mdx` (480 files, Zod-validated frontmatter)
- `game-pages` — `**/index.mdx` (94 game index pages)
- `getting-started-pages` — `**/getting-started.mdx` (4 setup guides)

Computed fields (layout, prevLesson, nextLesson, totalUnits, system, gameName) are derived from entry path in the `[...slug].astro` catch-all route — **never in frontmatter**.

Helper: `getGamesWithCounts(platform, track)`, `getUnitsEntry(platform, track, game)`

## CodeFromFile Usage
```mdx
import CodeFromFile from "@components/CodeFromFile.astro";
<CodeFromFile src="commodore-64/game-01-sid-symphony/unit-08/symphony.asm" />
```

Language auto-detected from path (Z80 for spectrum, 68000 for amiga, ca65 for NES, 6502 for C64).

## Key Docs
- **Curriculum model**: `docs/specifications/curriculum.md`
- **Unit formatting**: `docs/specifications/unit.md`
- **Brief format**: `docs/specifications/brief.md`
- **Decisions (binding)**: `docs/decisions/`
- **Platform curricula**: `docs/platforms/{system}/{assembly,basic,assembly-skeleton,basic-skeleton}.md`
- **Per-game briefs**: `docs/platforms/{system}/games/{slug}/brief.md` (plus other per-game design docs)
- **Platform refs**: `docs/platforms/{system}/reference.md` (plus existing hardware/language/graphics subdirs)
- **Live tracker**: `docs/tracker/revamp.md`
- **Event log**: `docs/log.md`

## Design Context
- **Users**: Learners wanting to understand how computers work through building games
- **Voice**: Warm, technical, never condescending — "we teach machines, not frameworks"
- **Visual**: Platform-specific branding (C64 blue, Spectrum rainbow, NES red, Amiga orange)
- **Anti-patterns**: Slick startup aesthetic, gaudy vaporwave, dense academic walls of text

## Known Gotchas

### Docker Volume Mounts
Always mount `/code-samples` not individual files. Docker caches inode, so editing mounted files may not reflect in container.

### ROM Requirements
All ROMs consolidated in `~/Projects/Reference/` — project folders symlink there.
- **C64**: `commodore-64-dev/roms/` → `Reference/commodore/c64/extracted/`
- **Amiga**: Requires Kickstart ROM in `Reference/amiga/Firmware/` (not distributable)
- **Spectrum**: No ROMs needed (open source)
- **NES**: No ROMs needed

### Screenshot Timing
Use `--wait N` to let program initialise before capture. Typical values:
- Simple programs: 50 frames
- Loading from tape: 500+ frames
- Animation loops: match frame count to loop

### Astro Content Collections
If YAML validation fails, check `src/content.config.ts` for schema. Common issue: missing required fields in frontmatter.

### MDX Page Locations
Unit, game index, and getting-started MDX files live in `src/content/curriculum/`, **not** `src/pages/`. The `src/pages/` directory only contains `.astro` files (overview pages, dynamic routes, the `[...slug].astro` catch-all).

## Documentation layout

Project documentation lives entirely in `docs/`. There is no separate "knowledge" or "wiki" layer — that split was retired (drift-generator).

- `docs/index.md` — top-level navigation map. Read first.
- `docs/decisions/` — binding decision records. Always check before proposing changes that contradict them.
- `docs/specifications/` — formal specs (curriculum, unit, brief, vault, pattern-library; writing-voice arrives in Phase 1b).
- `docs/platforms/` — per-platform reference + curriculum + per-game briefs. (System-first restructure lands in Phase 1b.)
- `docs/infrastructure/` — Docker, capture pipeline, Astro site notes.
- `docs/log.md` — append-only event log.
- `docs/tracker/` — live status. (Lands in Phase 1b.)

For cross-project knowledge spanning Code198x and Emu198x, see `../../CLAUDE.md` (umbrella) and `../../decisions/`. For personal cross-cutting knowledge, see `~/knowledge/`.

Update docs pages when you learn something future sessions need.
