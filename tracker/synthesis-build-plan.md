# Plan: Synthesis design-system build

**Status:** Draft — ready to execute. **Date:** 2026-05-29.
**Repo:** `website` (Astro). **Reference:** [`docs/design/synthesis/`](../design/synthesis/).

## Concept (the landing)

The site's visual language is a **synthesis**: the shipped production system's
*architecture* (the bones) carrying the fanzine exploration's period *soul*, as one
coherent language whose character density is **dialled by surface** — loud on
discovery, calm on reading. It is not a pivot to the fanzine and not the current
brutalist-mono production left as-is.

Binding decisions (read first):
[visual-direction-synthesis](../decisions/visual-direction-synthesis.md) ·
[website-design-zoning](../decisions/website-design-zoning.md) ·
[systems-not-platforms](../decisions/systems-not-platforms.md) ·
[system-url-structure](../decisions/system-url-structure.md).

Worked reference: seven surfaces + the canonical token sheet in
[`docs/design/synthesis/`](../design/synthesis/) — `synthesis.css` (light + warm-dark
tokens, contrast contract at the top), `homepage`, `fleet`, `system-landing`,
`game-landing`, `unit-page`, `vault-entry`, `planned-stub`.

## Approach: evolve, don't rebuild

Production already ships the bones — `src/layouts/Layout.astro` token block, the
67-platform manifest + hue-collision audit, `SystemCard`/`VaultCard`, `prose.css`, the
lesson diagrams (`SpriteGrid`/`RegisterBits`/`MemoryMap`), Shiki, Pagefind, Inter +
JetBrains Mono via the Astro Font API, a two-way theme toggle. The synthesis is
**additive and corrective**, not greenfield: re-role the type, add Caveat + the soul
primitives, apply zoning, swap to warm-dark. We change the existing site surface by
surface; we do not start a new one.

`synthesis.css` maps directly onto the `Layout.astro` token block — it is the seed, not
throwaway CSS.

---

## Phase 0 — Foundations (gates everything)

- **Tokens.** Replace the `Layout.astro` `:root` with the `synthesis.css` light tokens;
  add the `[data-theme="dark"]` warm-dark block. *Done when* every existing page still
  renders and a manual `data-theme="dark"` on `<html>` produces warm "ink on dark
  paper".
- **Fonts.** Add **Caveat** to `astro.config.mjs` font set (Inter + JetBrains Mono
  already present). *Done when* `--font-script` resolves to Caveat with no layout shift.
- **Type re-role (the de-genericiser).** Headings → Inter 800/900 sentence case (drop
  mono-uppercase default); body → Inter; JetBrains Mono → machine-voice only
  (code/labels/badges/eyebrows); Caveat → display/accent, ~28px floor. *Done when* no
  heading or body text renders in mono-uppercase, and Caveat appears only at ≥28px.
- **Theme control = Auto / Light / Dark.** Extend the existing two-way toggle to
  three-way; Auto follows `prefers-color-scheme`; Light/Dark persist (localStorage);
  inline no-FOUC `<head>` script applies before paint. *Done when* Auto tracks the OS,
  overrides persist across reloads, and there's no flash.
- **Contrast contract.** Enforce: `--fg-2` for small informational text; `--fg-muted`
  decorative/large-only; tier de-emphasis via border style, never text opacity. *Done
  when* an axe/contrast pass shows no body/label text below AA.

## Phase 1 — Shared components + new primitives

- **Re-skin existing:** nav (logo unchanged, mono links, the theme control), footer,
  `SystemCard`/`VaultCard`, buttons, badges, status pills, eyebrow/kicker, `prose.css`
  (the unit reading surface), code blocks (Shiki + per-language left rule).
- **New primitives** (from the reference): Caveat display heading, drop cap (per-letter
  spacing — see risks), pull-quote, sticky-note marginalia, `Photo` (polaroid),
  `AudioClip` (waveform), `VideoEmbed` (film perforations), "Further afield" block, the
  Spectrum rainbow (Spectrum pages only), house rule, atmosphere layers
  (paper/halftone/pixel-grid/scanline), and the five tier treatments
  (Live/Next/Planned/Edge/Beyond).
- *Done when* each primitive is a reusable Astro component with the contrast contract
  and dark-mode baked in, demoed on a kitchen-sink page.

## Phase 2 — Surfaces (launch-critical order)

Each maps to a reference mock. Order reflects the October Spectrum-only launch.

1. **Spectrum system landing** (`/sinclair-zx-spectrum/`) — QR entry point,
   mobile-first. *Launch artefact.* → `system-landing.html`
2. **Unit page** — one calm reading template; BASIC vs assembly differ by
   character-density flag, not separate templates. → `unit-page.html`
3. **Game landing** (Shadowkeep) — video, engine commitments, arc rail, Begin-Unit-1.
   → `game-landing.html`
4. **Vault entry** — editorial long-form + media primitives. *Launch artefact
   (Spectrum vault).* → `vault-entry.html`
5. **Homepage** — neutral chrome, platform colour only in cards. → `homepage.html`
6. **Fleet** (`/systems/`) — honest tiers, three lenses. → `fleet.html`
7. **Planned-tier stub** — never-404; the Fleet links here. → `planned-stub.html`
8. **Track/curriculum overview** — game-card grid + "new here?" affordance (derivable
   from the homepage card pattern; no dedicated mock).

URLs follow [system-url-structure](../decisions/system-url-structure.md): system-rooted,
explicit `{track}` segment, `game-{NN}-`, `unit-{NN}`. Nav/structure use **"Systems"**.

## Phase 3 — Honesty plumbing (can parallel Phase 2)

- **Manifest-drive all status/counts.** Homepage stats, Fleet pills/tiers, "what's not
  here yet", game `N/NN` progress read from `src/content/platforms/*` + `units/*` — never
  hand-typed. *Done when* flipping a platform `status` updates every surface with no
  copy edits.
- **Never-404.** Every system slug renders: live → full landing, non-live → the Planned
  stub, both from the manifest. *Done when* a coming-soon slug returns a real stub page,
  not a 404.

## Phase 4 — Polish / a11y / launch hygiene

`:focus-visible` states everywhere; `prefers-reduced-motion` honoured (caret/blink,
hover transitions); drop-cap per-letter robustness; OG-image template; SEO title format
`{Specific} | {Context} | Code Like It's 198x`; Pagefind result styling; responsive QA
(QR landing on a real phone); real assets swapped in; provenance pass on Spectrum vault.

## Phase 5 — Docs reconcile

Land IA **v3** into `docs/specifications/information-architecture.md` (currently v2.1 —
contradicts the decisions on Systems naming and track-in-URL). Retire the v2.1 drift.

---

## Launch-critical path (October, Spectrum-only)

Phase 0 → Phase 1 → Phase 2 items **1–7** + Phase 3. Everything else (other systems'
toggles, full polish, non-Spectrum surfaces) is post-launch. Per
[october-2026-launch-spec](../decisions/october-2026-launch-spec.md), cut count, never
the bar.

## Risks / watch-items

- **Dark hard-shadows** — solved with a warm offset lighter than the page; verify per
  surface.
- **Drop cap** is letter-fragile in Caveat — needs per-letter tuning or a robust fallback.
- **Warm-dark vs production cool-slate** — ratified warm; ensure no slate remnants leak back in.
- **Manifest as single source** — the honesty pitch dies if any surface drifts from it.
- **Don't gold-plate the mocks** — they're reference; build the real thing in Astro.

## Anchored in

- Decisions: [visual-direction-synthesis](../decisions/visual-direction-synthesis.md),
  [website-design-zoning](../decisions/website-design-zoning.md),
  [systems-not-platforms](../decisions/systems-not-platforms.md),
  [system-url-structure](../decisions/system-url-structure.md),
  [october-2026-launch-spec](../decisions/october-2026-launch-spec.md).
- Reference: [`docs/design/synthesis/`](../design/synthesis/).
