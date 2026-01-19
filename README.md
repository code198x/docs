# Code Like It's 198x - Documentation

This repository contains curriculum specifications, platform references, and content creation workflows for the Code Like It's 198x project.

## What Is This Project?

Code Like It's 198x teaches retro game development through complete, playable games. Learners build real games on vintage platforms - Commodore 64, ZX Spectrum, Amiga, NES - using the same techniques developers used in the 1980s and 1990s.

No emulation wrappers. No modern engines. Direct hardware access, assembly language, and the satisfaction of making a 40-year-old machine do something impressive.

## How The Curriculum Works

Each platform has a sequence of games, ordered by complexity:

- **Games** are complete, playable projects (8-32 units each)
- **Units** are 60-120 minute sessions producing working results
- **Skills compound** through the sequence - Game 1 teaches fundamentals, Game 16 produces commercial-quality work

See [CURRICULUM-SPECIFICATION.md](CURRICULUM-SPECIFICATION.md) for the full model.

## Repository Structure

```
/
├── curriculum/                    # Game sequences and curricula
│   ├── commodore-64-curriculum.md
│   ├── sinclair-zx-spectrum-curriculum.md
│   ├── commodore-amiga-curriculum.md
│   ├── nintendo-nes-curriculum.md
│   ├── assembly/                  # Future platform assembly stubs
│   │   ├── sega-mega-drive/
│   │   ├── atari-st/
│   │   ├── bbc-micro/
│   │   └── ...
│   ├── basic/                     # BASIC curricula and stubs
│   │   ├── commodore-64/
│   │   ├── sinclair-zx-spectrum/
│   │   ├── commodore-amiga/
│   │   ├── bbc-micro/
│   │   └── ...
│   ├── patterns/                  # Reusable code patterns
│   └── reference/                 # Planning and reference docs
│
├── platforms/                     # Platform-specific references
│   ├── commodore-64/              # Hardware refs, quick guides
│   ├── sinclair-zx-spectrum/
│   ├── commodore-amiga/
│   └── nintendo-entertainment-system/
│
├── CURRICULUM-SPECIFICATION.md    # How curricula work
├── UNIT-SPECIFICATION.md          # How to format unit files
├── PATTERN-LIBRARY-SPECIFICATION.md
├── VAULT-SPECIFICATION.md
└── CONTENT-CREATION-WORKFLOW.md
```

## Key Documents

| Document | Purpose |
|----------|---------|
| [CURRICULUM-SPECIFICATION.md](CURRICULUM-SPECIFICATION.md) | The games model, unit structure, pedagogical approach |
| [UNIT-SPECIFICATION.md](UNIT-SPECIFICATION.md) | Technical formatting for unit files |
| [VAULT-SPECIFICATION.md](VAULT-SPECIFICATION.md) | Encyclopedia of people, companies, games, techniques |
| [PATTERN-LIBRARY-SPECIFICATION.md](PATTERN-LIBRARY-SPECIFICATION.md) | Reusable code patterns by platform |
| [CONTENT-CREATION-WORKFLOW.md](CONTENT-CREATION-WORKFLOW.md) | End-to-end content creation process |

## Platform Status

### Assembly Curricula (Main)

| Platform | Language | Curriculum | Status |
|----------|----------|------------|--------|
| Commodore 64 | 6510 Assembly | [16 games, 1,536 units](curriculum/commodore-64-curriculum.md) | Game sequence defined |
| ZX Spectrum | Z80 Assembly | [16 games, 1,536 units](curriculum/sinclair-zx-spectrum-curriculum.md) | Game sequence defined |
| NES | 6502 Assembly | [16 games, 1,536 units](curriculum/nintendo-nes-curriculum.md) | Game sequence defined |
| Amiga | 68000 Assembly | [16 games, 2,048 units](curriculum/commodore-amiga-curriculum.md) | Game sequence defined |

### BASIC Gateway Curricula (Optional)

| Platform | Language | Curriculum | Status |
|----------|----------|------------|--------|
| Commodore 64 | BASIC V2 | [8 games, 512 units](curriculum/basic/commodore-64/) | Game sequence defined |
| ZX Spectrum | Sinclair BASIC | [8 games, 512 units](curriculum/basic/sinclair-zx-spectrum/) | Game sequence defined |
| Amiga | AMOS/Blitz BASIC | [16 games](curriculum/basic/commodore-amiga/) | Game sequence defined |

### Future Platforms (Stub Curricula)

Stub curricula have been created for future platforms. See:
- [curriculum/assembly/](curriculum/assembly/) - Assembly stubs (Mega Drive, Atari ST, BBC Micro, SNES, etc.)
- [curriculum/basic/](curriculum/basic/) - BASIC stubs (BBC BASIC, Locomotive, STOS/GFA, MSX-BASIC)
- [curriculum/reference/future-platforms-complete.md](curriculum/reference/future-platforms-complete.md) - Full platform roadmap

## Related Repositories

This documentation repository is one of three:

- **docs** (this repo) - Specifications and references
- **website** - Astro site serving the curriculum
- **code-samples** - Compiled, tested code for each unit

## Contributing

All units must:

1. Align with the curriculum specification
2. Compile and run on the target platform
3. Include verified screenshots
4. Use British English (except "program" for computer programs)

See [CONTENT-CREATION-WORKFLOW.md](CONTENT-CREATION-WORKFLOW.md) for the full process.
