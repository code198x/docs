# Commodore 64

## Toolchain

| Component | Tool | Notes |
|-----------|------|-------|
| Assembler | ACME | `acme -f cbm` → `.prg` |
| Docker image | `ghcr.io/code198x/commodore-64:latest` | Mount `/code-samples` not individual files |
| Emulator | Emu198x (when available) | Screenshots via `/scripts/c64-screenshot.sh` |
| ROMs | `~/Projects/Reference/commodore/c64/extracted/` | Symlinked from `commodore-64-dev/roms/` |

## Build command

```bash
docker run --rm -v $(pwd)/code-samples:/code-samples ghcr.io/code198x/commodore-64:latest \
  acme -f cbm -o /code-samples/output.prg /code-samples/input.asm
```

## Assembly dialect

6502 assembly via ACME. Language detection in `CodeFromFile` maps C64 paths to `6502` highlighting.

## Gotchas

- **Docker volume mounts**: always mount `/code-samples` directory, not individual files. Docker caches inodes, so edited mounted files may not reflect in container.
- **ROM requirements**: ROMs must be symlinked from `~/Projects/Reference/` — not committed to the repo.
- **Screenshot timing**: simple programs need ~50 frames wait. Programs that load from disk/tape need 500+.
