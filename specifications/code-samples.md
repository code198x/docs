# Code Samples

All code lives in the `/code-samples/` repo, never inline in MDX.

## CodeFromFile component

```mdx
import CodeFromFile from "@components/CodeFromFile.astro";
<CodeFromFile src="commodore-64/game-01-sid-symphony/unit-08/symphony.asm" />
```

Language auto-detected from path:
- Spectrum paths → Z80 highlighting
- Amiga paths → 68000 highlighting
- NES paths → ca65 highlighting
- C64 paths → 6502 highlighting

## File naming

- `example-1.{ext}` — simple demonstration (5-15 lines)
- `example-2.{ext}` — complex/complete demonstration (15-40 lines)
- `{concept-name}.{ext}` — descriptive names for specific techniques

## Extensions by platform

| Platform | BASIC | Assembly |
|----------|-------|----------|
| C64 | `.bas` | `.asm` |
| ZX Spectrum | `.bas` | `.asm` |
| Amiga | `.amos` | `.asm` |
| NES | — | `.asm` |

## Key principle

Every code sample must compile/run and be verified with screenshots. The learner should be able to build and run after every unit.
