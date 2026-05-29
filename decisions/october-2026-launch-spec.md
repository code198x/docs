# Decision: October 2026 Launch Spec

> **AMENDED 2026-05-29 by [spectrum-assembly-gentle-ramp.md](spectrum-assembly-gentle-ramp.md).**
> The assembly launch artefact (#1 below) is reframed from "Shadowkeep Arcs 1–2, 32 units" to
> **the gentle assembly opening: the Primer + a complete tiny first game + the start of the
> re-scoped (cell-based) Shadowkeep.** Judged more achievable and a better first experience — a
> learner *finishes* a real game in assembly by October, with the hardest engineering (pre-shift /
> Y-sort / masking) off the critical path and deferred to later games. The Shadowkeep-specific cut
> hierarchy below is superseded for the assembly artefact; re-derive against the new opening.

**Status:** Active. October is a target, not a hard deadline — the project is close to having enough to ship. Shadowkeep scope set by [shadowkeep-32-unit-commitment.md](shadowkeep-32-unit-commitment.md); BASIC by [spectrum-basic-32-games.md](spectrum-basic-32-games.md). The two structural artefacts (landing page, vault) are spec'd in this doc.

**Date:** 2026-05-06 | **Updated:** 2026-05-26

## The decision

The October 2026 Crash! Live launch ships **Spectrum only**. C64, NES, and
Amiga defer wholesale to post-launch — coming-soon cards on the site, full
design preserved in [revamp.md](../tracker/revamp.md).

The Spectrum launch is **four artefacts at full quality bar**:

1. **The gentle assembly opening** — the Primer ("Meet the Machine"), a *complete* tiny first game, and the start of the re-scoped (cell-based) Shadowkeep, at the atmospheric bar of *Atic Atac* and *Knight Lore*. A learner finishes a real game in assembly by October; the hardest engineering is off the critical path. The shipped cell-snapped units largely survive into this opening. Per [spectrum-assembly-gentle-ramp.md](spectrum-assembly-gentle-ramp.md) and [shadowkeep-32-unit-commitment.md](shadowkeep-32-unit-commitment.md).
2. **Spectrum BASIC Volume 1 (8 games) complete** — Usborne 1984 bar, every topic passes DoD. Per [spectrum-basic-32-games.md](spectrum-basic-32-games.md) (full curriculum is 32 games / 4 volumes / 8 per volume; Volumes 2-4 ship post-October through ~2028-29).
3. **Spectrum landing page** — designed for QR-code visitors arriving from
   Crash! Live flyers and t-shirts.
4. **Spectrum vault: review pass + referenced gap-fill** — every entry linked
   from a shipped unit must exist.

If scope needs trimming, count is cut, never the bar. Cut hierarchy lives in
[revamp.md](../tracker/revamp.md) and is binding.

## October bar definition

"October-ready" means **every shipped unit passes the 9-item Definition of
Done**, plus four artefact-level gates:

- **Assembly opening:** Primer complete; the tiny first game complete and playable end-to-end on Spectrum Next; the re-scoped Shadowkeep's opening units at the cell-based atmosphere bar. No pre-shift / Y-sort / masking in the October artefact — those teach later (Smooth Motion → Overlap → Greypeak) per [spectrum-assembly-gentle-ramp.md](spectrum-assembly-gentle-ramp.md).
- **BASIC games:** Volume 1 ships — 8 games at Usborne bar, every topic passes DoD. Topic counts variable per game (no fixed unit-count floor); rough V1 estimate ~30-50 topics across the 8 games. Volumes 2-4 ship through ~2028-29.
- **Landing page:** designed, copy finalised, navigation working, QR landing
  tested on a real phone from a printed flyer.
- **Vault:** every reference from a shipped unit resolves; review pass
  complete on existing Spectrum entries.

## Why this scope, not larger or smaller

**Larger (4 platforms):** Cadence, Nightshade, Exodus each need a 16-unit
spine, a game implementation, and (Cadence) a composed soundtrack. None of
that is October-realistic at full bar; trying erodes the bar. Coming-soon
cards are honest. Work resumes November.

**Smaller (Shadowkeep only):** BASIC is the on-ramp audience — kids,
beginners, returners. Without BASIC, launch reads as a demo, not a curriculum.

**Smaller (BASIC only, no Shadowkeep):** Misses the flagship proof — "computers taught at commercial-bar depth." Shadowkeep Arcs 1+2 demonstrate the bar.

**Smaller (drop the vault):** Vault review is fast and already protected in
the cut hierarchy. Cost-to-cut ratio doesn't favour cutting it.

## Cut hierarchy

Per [shadowkeep-32-unit-commitment.md](shadowkeep-32-unit-commitment.md) (Shadowkeep cuts) and [revamp.md](../tracker/revamp.md) (live tracker):

1. Trim Shadowkeep Arc 2 sub-arcs back-to-front (2.4 → 2.3 → 2.2 → 2.1). Arc 1 alone (16 units) is the absolute floor.
2. Only then begin BASIC V1 game cuts — and only below a 4-game floor.
3. Landing page and vault cuts are last resort.

Vault completeness is protected. Quality bar stays full at every step.

## Out of scope (explicit)

- C64 / Cadence, NES / Nightshade, Amiga / Exodus — coming-soon cards.
- Shadowkeep Arcs 3-4 — post-October per [shadowkeep-four-arc-framing.md](shadowkeep-four-arc-framing.md).
- Pattern library work not downstream of a shipped unit's reference.
- Vault expansion beyond review pass + referenced gap-fill.
- Aspirational platform totals (1024 / 2048 / 4096) — direction of travel,
  not spec.
- In-browser WASM Emu198x embed — post-launch.

## Form factor at the event

- **Flyers, t-shirt, QR code → site.** The site is the artefact.
- **Hardware testing target:** ZX Spectrum Next + Fuse emulator.
- **Audience entry:** QR code lands on the Spectrum landing page, not
  site root.

## Drift triggers

If you find yourself proposing any of the following, stop and re-consult
this spec:

- Extending Shadowkeep past 32 units before the first 32 ship ("just one more unit"). Surplus energy goes into polish within the 32, not new units.
- Adjusting the Definition of Done downward to fit timeline.

When a drift trigger fires: name it as drift, decide whether the spec
changes (with rationale captured as a log entry below), and capture
deferred work in [revamp.md](../tracker/revamp.md).

## Anchored in

- [revamp.md](../tracker/revamp.md) — live status, source of truth for in-flight work.
- [shadowkeep-32-unit-commitment.md](shadowkeep-32-unit-commitment.md) — Shadowkeep October scope.
- [shadowkeep-four-arc-framing.md](shadowkeep-four-arc-framing.md) — full Shadowkeep four-arc framing.
- [spectrum-basic-32-games.md](spectrum-basic-32-games.md) — BASIC lineup.
- [commercial-bar-revamp.md](commercial-bar-revamp.md) — bar definitions per track.
- [british-english.md](british-english.md), [seven-repos.md](seven-repos.md)

## Log

| Date | Event |
|---|---|
| 2026-05-06 | Spec lifted into a binding decision doc. Floor numbers pinned (BASIC 128, Shadowkeep 16). Stretch separated from spec. |
| 2026-05-26 | October reframed as target, not hard deadline. BASIC V1 done; landing page shipped; Shadowkeep 8/32 — close enough that urgency feels artificial. Session-start gate removed. Drift triggers trimmed to the two that still matter (scope creep past 32 units, DoD erosion). |
| 2026-05-29 | Assembly launch artefact reframed per [spectrum-assembly-gentle-ramp.md](spectrum-assembly-gentle-ramp.md): from "Shadowkeep Arcs 1–2, 32 units" to "Primer + complete tiny first game + start of re-scoped cell-based Shadowkeep". Hardest engineering (pre-shift / Y-sort / masking) deferred off the October critical path. |
