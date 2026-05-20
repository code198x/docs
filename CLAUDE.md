# Code198x

Retro game dev education. Complete games on vintage platforms (C64, ZX Spectrum, Amiga, NES).

## Session start (October 2026 launch anchor)

Before writing any code, state in the conversation which October launch artefact this session serves. The launch ships **Spectrum only** — see [`decisions/october-2026-launch-spec.md`](decisions/october-2026-launch-spec.md) for the binding scope and cut hierarchy.

The four launch artefacts:

1. **Shadowkeep** — Spectrum assembly Volume 1 Game 1; Arcs 1+2 at 32 units for October at commercial bar. Full four-arc framing for the complete game lives in `docs/decisions/shadowkeep-four-arc-framing.md` (Arcs 3-4 post-October). 16-unit Phase 1 framing is superseded by 32-unit two-arc commitment.
2. **Spectrum BASIC Volume 1** — 8 games at Usborne bar (v6.4 names: Banner, Lucky Number, Oracle Stone, Reflex, Dice Roller, Bright Spark, Hi-Lo, Touchdown). Full 32-game / 4-volume curriculum at `docs/decisions/spectrum-basic-32-games.md`; Volumes 2-4 are post-October.
3. **Spectrum landing page** — for QR-code visitors arriving from Crash! Live flyers and t-shirts.
4. **Spectrum vault** — review pass + referenced gap-fill.

If the requested work doesn't serve one of these — C64 / NES / Amiga work, Cadence / Nightshade / Exodus, Shadowkeep Arcs 3+ or other Spectrum Assembly Games 2-44, BASIC Volumes 2-4, pattern library or vault expansion not downstream of a shipped unit — **name it as post-October**, and ask whether to proceed or defer. Don't silently expand the October pile. Once the user confirms post-October work, proceed; the rule is to flag it, not to refuse it.

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
- **Platform curricula**: `docs/curriculum/{platform}-curriculum.md` (restructuring to `docs/platforms/{system}/` in Phase 1b)
- **Platform refs**: `docs/platforms/{platform}/`
- **Live tracker**: `docs/tracker/revamp.md` (arriving in Phase 1b)
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

For cross-project knowledge, read `/Users/stevehill/Projects/wiki/index.md`.

Update docs pages when you learn something future sessions need.
