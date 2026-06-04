# Docker Toolchains

Each platform has a Docker image containing its assembler. Images are hosted on GitHub Container Registry.

> **Interim tooling.** These images are the current build path, but the
> destination is the family's own assembler, **Asm198x** (capture moves to
> **Emu198x** separately). They retire **per-platform** — once Asm198x produces
> that platform's loadable artifact and a real unit is verified end-to-end —
> never a big-bang delete, and no new features land here meanwhile. The current
> gate is the *output container*: Amiga (hunk-exe) and NES (`.nes`) are already
> covered by Asm198x; C64 (`.prg`) and Spectrum (`.sna`) need an output container
> first. See the umbrella decision
> [Code198x dev-tooling migration](../../../decisions/code198x-dev-tooling-migration.md).

## Images

| Platform | Image | Assembler |
|----------|-------|-----------|
| C64 | `ghcr.io/code198x/commodore-64:latest` | ACME |
| ZX Spectrum | `ghcr.io/code198x/sinclair-zx-spectrum:latest` | pasmonext |
| Amiga | `ghcr.io/code198x/commodore-amiga:latest` | vasm |
| NES | `ghcr.io/code198x/nintendo-nes:latest` | ca65 + ld65 |

## Build repos

Each Docker image has its own repo:
- `commodore-64-dev`
- `sinclair-zx-spectrum-dev`
- `commodore-amiga-dev`
- `nintendo-entertainment-system-dev`

## Volume mount gotcha

Always mount the `/code-samples` directory, not individual files. Docker caches inodes — editing a mounted file may not reflect inside the container. Mount the parent directory instead.
