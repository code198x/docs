# Commodore Amiga

## Toolchain

| Component | Tool | Notes |
|-----------|------|-------|
| Assembler | vasm (m68k, mot syntax) | `vasmm68k_mot -Fhunkexe -kick1hunks` → executable |
| Docker image | `ghcr.io/code198x/commodore-amiga:latest` | |
| Emulator | Emu198x (when available) | Screenshots via `/scripts/amiga-screenshot.sh` |
| ROMs | Kickstart ROM required | `~/Projects/Reference/amiga/Firmware/` — **not distributable** |

## Build command

```bash
docker run --rm -v $(pwd)/code-samples:/code-samples ghcr.io/code198x/commodore-amiga:latest \
  vasmm68k_mot -Fhunkexe -kick1hunks -o /code-samples/output /code-samples/input.asm
```

## Assembly dialect

68000 assembly via vasm (Motorola syntax). Language detection maps Amiga paths to `68000` highlighting.

## Gotchas

- **Kickstart ROM is not distributable** — learners must supply their own. Document this clearly in getting-started guides.
- **Screenshot timing**: Amiga boots slowly in emulation. Use `--wait` with high frame counts.
- **ADF creation**: use the `build-amiga-adf` skill to create bootable disk images from executables.
