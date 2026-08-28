# Code198x docs

> Read [`PRINCIPLES.md`](PRINCIPLES.md) first. [`MANIFESTO.md`](MANIFESTO.md) is why the project exists.

This repo owns Code198x curriculum specifications, platform references, decisions, and content workflow docs.

## Umbrella context

The umbrella context is [`../../AGENTS.md`](../../AGENTS.md); cross-project decisions live in [`../../decisions/`](../../decisions/). Hardware facts cite the 198x source-of-truth layers rather than becoming canonical inside curriculum docs.

## Current launch context

October 2026 is the public launch target. The launch surface is the four core platforms, each with a complete on-ramp at the current Definition of Done bar:

- ZX Spectrum
- Commodore 64
- Commodore Amiga
- Nintendo Entertainment System

Current shipped/planned state lives in the website module catalogues and git, not in prose trackers. Decision records explain the rationale.

## Working rules

- Keep this repo focused on specs, platform references, curriculum decisions, and content workflow docs.
- Put binding Code198x decisions in `decisions/`.
- Put formal format/structure rules in `specifications/`.
- Put learner-facing system material in `platforms/`.
- Use British English, except use “program” for computer programs.
- Treat hardware facts as derived from `reference/`, `syntheses/`, and Emu198x knowledge.
- Update `index.md` when adding or moving docs that future sessions need to find.

## Current layout

| Path | Purpose |
|---|---|
| `index.md` | Navigation map. |
| `decisions/` | Binding Code198x decision records. |
| `specifications/` | Formal specs for curriculum, units, briefs, Vault, Pattern Library, content model, and voice. |
| `platforms/` | Per-platform reference, curriculum framing, and per-game docs. |
| `infrastructure/` | Docker, capture pipeline, Astro, and testing notes. |
| `tracker/` | Plans, research, and design sketches; not authoritative live status. |
| `log.md` | Append-only event log. |

## State source

Project state is read from the website catalogues, unit files, shipped files, and git. Prose docs carry rationale and navigation.
