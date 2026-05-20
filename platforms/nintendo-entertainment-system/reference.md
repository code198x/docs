# Nintendo Entertainment System

## Toolchain

| Component | Tool | Notes |
|-----------|------|-------|
| Assembler | ca65 + ld65 | Two-step: assemble then link → `.nes` |
| Docker image | `ghcr.io/code198x/nintendo-nes:latest` | |
| Emulator | Emu198x (when available) | Screenshots via `nes-screenshot` Docker command |
| ROMs | Not needed | |

## Build command

```bash
docker run --rm -v $(pwd)/code-samples:/code-samples ghcr.io/code198x/nintendo-nes:latest \
  sh -c "ca65 /code-samples/input.asm -o /tmp/output.o && ld65 /tmp/output.o -C /code-samples/config.cfg -o /code-samples/output.nes"
```

## Assembly dialect

6502 (ca65 syntax — slightly different from ACME). Language detection maps NES paths to `ca65` highlighting.

## Gotchas

- **Two-step build**: ca65 assembles to object files, ld65 links with a config. Both steps needed.
- **Linker config**: each project needs a `.cfg` file defining memory regions (PRG-ROM, CHR-ROM, etc.).
- **No ROMs needed** — NES cartridge format is self-contained.
