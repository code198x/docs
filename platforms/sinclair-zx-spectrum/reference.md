# ZX Spectrum

## Toolchain

| Component | Tool | Notes |
|-----------|------|-------|
| Assembler | pasmonext | `pasmonext --sna` → `.sna` snapshot |
| Docker image | `ghcr.io/code198x/sinclair-zx-spectrum:latest` | |
| Emulator | Emu198x | Screenshots via `/scripts/spectrum-screenshot.sh` or Emu198x directly |
| ROMs | Not needed | Spectrum ROMs are open source |

## Build command

```bash
docker run --rm -v $(pwd)/code-samples:/code-samples ghcr.io/code198x/sinclair-zx-spectrum:latest \
  pasmonext --sna /code-samples/input.asm /code-samples/output.sna
```

## Assembly dialect

Z80 assembly via pasmonext. Language detection in `CodeFromFile` maps Spectrum paths to `z80` highlighting.

## Gotchas

- **No ROMs needed** — Spectrum ROMs are freely distributable under Amstrad's blanket permission, and pasmonext outputs .sna snapshots that skip the ROM entirely.
- **Screenshot source**: prefer Emu198x for screenshots when available (matches the project's own emulator).
