# Docker Toolchains

Each platform has a Docker image containing its assembler. Images are hosted on GitHub Container Registry.

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
