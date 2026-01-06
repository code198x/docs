# Technical TODO

Technical debt, infrastructure improvements, and non-curriculum tasks.

For curriculum roadmap (future games/units), see `/docs/curriculum/*.md`.

---

## Infrastructure

- [ ] Add syntax highlighting for 68000 assembly (Amiga uses `asm` but could benefit from dedicated grammar)
- [ ] Add syntax highlighting for Z80 assembly (ZX Spectrum)
- [ ] Consider adding download buttons to CodeFromFile component (download .asm file directly)
- [ ] Add "Copy to clipboard" button to code blocks

## Build & CI

- [ ] Add build verification for code-samples (compile all .asm files in CI)
- [ ] Add link checker to catch broken internal links
- [ ] Consider caching code-samples checkout in CI for faster builds

## Content Quality

- [ ] Audit screenshots across all units (verify no error screens, blank outputs)
- [ ] Run British English spell checker across all MDX files
- [ ] Verify all "Build It. Run It." sections have correct commands per platform

## Code Samples

- [ ] Add README.md to each game folder in code-samples explaining the build process
- [ ] Consider adding pre-built binaries (.prg, .tap, .nes, .adf) for users without toolchains
- [ ] Add license file to code-samples repo

## Documentation

- [ ] Update CLAUDE.md to reference new CodeFromFile workflow
- [ ] Document the extraction scripts in scripts/
- [ ] Add contributor guide if accepting external contributions

## Future Platforms (if expanding)

- [ ] Atari 2600 - would need 6502 variant support
- [ ] Atari ST - would need 68000 (shared with Amiga)
- [ ] BBC Micro - would need 6502 + BASIC

---

*Last updated: 2026-01-06*
