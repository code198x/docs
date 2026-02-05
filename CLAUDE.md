# Code198x

Retro game dev education. Complete games on vintage platforms (C64, ZX Spectrum, Amiga, NES).

## Critical Rules
- **7 separate git repos** — check all with `git status` before committing
- **Code samples in `/code-samples/`** — never inline in MDX; use `CodeFromFile` component
- **British English** — colour, learnt, centre (exception: "program" not "programme")
- **Verify every screenshot** — use Read tool, check for errors, document what you see

## Repositories
| Repo | Purpose |
|------|---------|
| `website` | Astro 5.x site |
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
| C64 | `c64-dev:latest` | `acme -f cbm` | `.prg` |
| ZX Spectrum | `ghcr.io/code198x/sinclair-zx-spectrum:latest` | `pasmonext --sna` | `.sna` |
| Amiga | `amiga-dev:latest` | `vasmm68k_mot -Fhunkexe -kick1hunks` | executable |
| NES | `code198x/nintendo-entertainment-system:latest` | `ca65` + `ld65` | `.nes` |

## Screenshot/Video Tools
- **C64**: Docker script `/scripts/c64-screenshot.sh` (ROMs symlinked from `~/Projects/Reference/`)
- **Amiga**: Docker script `/scripts/amiga-screenshot.sh` (requires Kickstart ROM in `~/Projects/Reference/amiga/Firmware/`)
- **NES**: Docker `nes-screenshot` command
- **ZX Spectrum**: Use Emu198x when available

Options: `--wait N` (frames), `--input FILE` (input script), `--duration N` (video)

## Content Collections
```
src/content/
├── games/{platform}/{track}.yaml    # Game catalogue
└── units/{platform}/{track}/{game}.yaml  # Unit details (source of truth for counts)
```

Helper: `getGamesWithCounts(platform, track)`, `getUnitsEntry(platform, track, game)`

## CodeFromFile Usage
```mdx
import CodeFromFile from "@components/CodeFromFile.astro";
<CodeFromFile src="commodore-64/game-01-sid-symphony/unit-08/symphony.asm" />
```

Language auto-detected from path (Z80 for spectrum, 68000 for amiga, ca65 for NES, 6502 for C64).

## Key Docs
- **Curriculum model**: `/docs/CURRICULUM-SPECIFICATION.md`
- **Unit formatting**: `/docs/UNIT-SPECIFICATION.md`
- **Platform curricula**: `/docs/curriculum/{platform}-curriculum.md`
- **Platform refs**: `/docs/platforms/{platform}/`

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
If YAML validation fails, check `src/content/config.ts` for schema. Common issue: missing required fields in frontmatter.
