# Drawing backlog reconciliation

All new work is in code198x/docs. These are family-sized gaps, not a machine-by-technique ticket explosion. Filing them does not merge pending PRs or start every implementation.

## Created

| Issue | Scope | Parent | Order |
| --- | --- | --- | --- |
| [#121: Expand drawing patterns from pixels and shapes to fonts across 30 systems](https://github.com/code198x/docs/issues/121) | parent | [Parent](https://github.com/code198x/docs/issues/117) | Drawing umbrella |
| [#122: Build bounded pixel, span and box routines on Spectrum, BBC Micro and Dragon](https://github.com/code198x/docs/issues/122) | pixels | [Parent](https://github.com/code198x/docs/issues/121) | Recommended first batch |
| [#123: Extract custom-glyph install and replacement on VIC-20, MSX1 and Game Boy](https://github.com/code198x/docs/issues/123) | glyphs | [Parent](https://github.com/code198x/docs/issues/121) | Recommended first batch |
| [#124: Add clipped lines, circles, ellipses and span-filled shapes](https://github.com/code198x/docs/issues/124) | geometry | [Parent](https://github.com/code198x/docs/issues/121) | Follow-up family |
| [#125: Draw fixed-width bitmap text at arbitrary pixel positions](https://github.com/code198x/docs/issues/125) | pixel-text | [Parent](https://github.com/code198x/docs/issues/121) | Follow-up family |
| [#126: Build text measurement, proportional layout and scaled-glyph variants](https://github.com/code198x/docs/issues/126) | layout | [Parent](https://github.com/code198x/docs/issues/121) | Follow-up family |
| [#127: Extend primitive backends to packed, attributed, ANTIC and planar displays](https://github.com/code198x/docs/issues/127) | bitmap-ports | [Parent](https://github.com/code198x/docs/issues/121) | Follow-up family |
| [#128: Extend font and pattern loading across the remaining writable-character paths](https://github.com/code198x/docs/issues/128) | glyph-ports | [Parent](https://github.com/code198x/docs/issues/121) | Follow-up family |
| [#129: Cover fixed-ROM and software-display drawing without inventing bitmap capabilities](https://github.com/code198x/docs/issues/129) | character-alternatives | [Parent](https://github.com/code198x/docs/issues/121) | Follow-up family |
| [#130: Define reusable drawing contracts for TIA kernels and MARIA display lists](https://github.com/code198x/docs/issues/130) | raster | [Parent](https://github.com/code198x/docs/issues/121) | Follow-up family |
| [#131: Connect drawing patterns to Maths for Games with worked geometry explanations](https://github.com/code198x/docs/issues/131) | maths | [Parent](https://github.com/code198x/docs/issues/121) | First-batch explanations and onward links |

Native GitHub sub-issues mirror all body links: #121 belongs to #117, and #122–#131 belong to #121. Parent checklist links every child; each child links its parent.

## Reused or kept separate

- [code198x/docs/issues/117](https://github.com/code198x/docs/issues/117) — Overall reusable-capability expansion parent.
- [code198x/website/issues/802](https://github.com/code198x/website/issues/802) — Existing imagery queue; drawing work is separate.
- [code198x/code-samples/pull/133](https://github.com/code198x/code-samples/pull/133) — Existing unmerged executed character regions, not duplicated.
- [code198x/website/pull/871](https://github.com/code198x/website/pull/871) — Existing unmerged character-region pages.
- [code198x/docs/issues/4](https://github.com/code198x/docs/issues/4) — Vectrex proposal outside current 30-system registry.
- [code198x/docs/issues/6](https://github.com/code198x/docs/issues/6) — Vectrex qualification outside current 30-system registry.

Closed samples #90 and website #690 remain completed correctness/evidence work. Existing geometry, character and sprite code is reuse material in the implementation tickets. No exact open drawing-family duplicate was found in the complete issue snapshot; issue #117 already supplies the broader parent.
