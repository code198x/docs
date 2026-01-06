# Technical TODO

Technical debt, infrastructure improvements, and non-curriculum tasks.

For curriculum roadmap (future games/units), see `/docs/curriculum/*.md`.

---

## Infrastructure

- [x] Add syntax highlighting for 68000 assembly (Amiga uses `asm` but could benefit from dedicated grammar)
- [x] Add syntax highlighting for Z80 assembly (ZX Spectrum)
- [ ] Consider adding download buttons to CodeFromFile component (download .asm file directly)
- [x] Add "Copy to clipboard" button to code blocks

## Build & CI

- [ ] Add build verification for code-samples (compile all .asm files in CI)
- [x] Add link checker to catch broken internal links
- [ ] Consider caching code-samples checkout in CI for faster builds

## Developer Experience

- [ ] Rework development environments - readers should be able to build code without downloading random packages
  - Consider Docker-based toolchains per platform
  - Or web-based assemblers/emulators
  - Document exact toolchain versions and sources

## Content Quality

- [ ] **CRITICAL: Generate missing screenshots** - ZX Spectrum, Amiga, and NES units have no screenshots
  - ZX Spectrum Ink War: 16 units missing screenshots
  - Amiga Hop: 16 units missing screenshots
  - NES Neon Nexus: 16 units missing screenshots
  - Link checker currently excludes `/images/` paths until fixed
- [ ] Audit screenshots across all units (verify no error screens, blank outputs)
- [ ] Run British English spell checker across all MDX files
- [ ] Verify all "Build It. Run It." sections have correct commands per platform

## Code Samples

- [ ] Add README.md to each game folder in code-samples explaining the build process
- [ ] Consider adding pre-built binaries (.prg, .tap, .nes, .adf) for users without toolchains
- [x] Add license file to code-samples repo

## Documentation

- [x] Update CLAUDE.md to reference new CodeFromFile workflow (local file, not version controlled)
- [ ] Document the extraction scripts in scripts/
- [ ] Add contributor guide if accepting external contributions

## Future Platforms (if expanding)

- [ ] Atari 2600 - would need 6502 variant support
- [ ] Atari ST - would need 68000 (shared with Amiga)
- [ ] BBC Micro - would need 6502 + BASIC

---

*Last updated: 2026-01-06*
*Z80 and 68k syntax highlighting added: 2026-01-06*
*Link checker CI added: 2026-01-06*
