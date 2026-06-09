# Decision: October 2026 Launch Spec

> **AMENDED 2026-05-29 by [spectrum-assembly-gentle-ramp.md](spectrum-assembly-gentle-ramp.md).**
> The assembly launch artefact (#1 below) is reframed from "Shadowkeep Arcs 1–2, 32 units" to
> **the gentle assembly opening: the Primer + a complete tiny first game + the start of the
> re-scoped (cell-based) Shadowkeep.** Judged more achievable and a better first experience — a
> learner *finishes* a real game in assembly by October, with the hardest engineering (pre-shift /
> Y-sort / masking) off the critical path and deferred to later games. The Shadowkeep-specific cut
> hierarchy below is superseded for the assembly artefact; re-derive against the new opening.

> **AMENDED 2026-06-03 — C64 promoted to a second launch platform (focus sequenced, not widened).**
> The time pressure that forced "Spectrum only" eased, and the Spectrum has now *validated the
> gentle-ramp methodology* — Meet the Machine and a complete Gloaming shipped, the precondition the
> C64 skeleton was explicitly waiting on. C64 is therefore promoted from "wholesale deferred /
> coming-soon card" to **the second platform brought to the finishable bar**, by applying the same
> ramp: a **C64 Primer** (a "Meet the Machine" equivalent — the 6502, the VIC-II and hardware
> sprites, SID, the memory map) plus **Starfield** re-scoped to its real ~16 units (the 112 stub
> units dropped), finished to the Definition of Done and marked complete — "a real game you finish"
> on a second machine. The C64 **flagship (Cadence)** and **C64 BASIC** stay deferred, exactly as
> Shadowkeep's later arcs and BASIC Volumes 2–4 are. **NES and Amiga remain deferred** — focus is
> *sequenced* to a second platform, not *widened* to four, so the "erodes the bar" reasoning below
> still holds. Supersedes the "Spectrum only" / "C64 … defer wholesale" framing below, for C64 only.
> Track plan: [commodore-64/assembly-skeleton.md](../platforms/commodore-64/assembly-skeleton.md).
> **AMENDED 2026-06-09 — launch widened, deliberately, to all four core platforms.**
> Confirmed by Steve: shipping a complete on-ramp on **every core platform** *is* the launch, and a
> far stronger one than "Spectrum only." The Spectrum-only framing was an artefact of Crash! Live
> being a Spectrum-focused event — not a scope ceiling. The October launch is now **all four live
> platforms — Spectrum, C64, Amiga, NES — each with a complete, finishable on-ramp**, shipping **as
> much as possible at the full DoD bar**:
> - **Spectrum** — the assembly opening (Meet the Machine, Gloaming, Shadowkeep Arc 1) plus a large
>   BASIC track (17 games live, more in progress).
> - **C64** — assembly Primer + Starfield, *and* a complete BASIC volume (Meet C64 BASIC + 8 First
>   Programs). BASIC was previously "deferred."
> - **Amiga** — three on-ramps: Meet AMOS, Meet Blitz, and the assembly Meet the Machine.
> - **NES** — the assembly Meet the Machine.
>
> This is the gentle-ramp methodology **generalised**: every machine gets a finishable on-ramp;
> flagships (Cadence, Nightshade, Exodus, the Amiga/NES games, BASIC Volumes 2–4) stay
> **coming-soon and sequenced**. The "widening erodes the bar" warning is *preserved*, not broken —
> the expansion is in the **on-ramp layer** (complete primers at bar), not premature flagships.
> **"Ship as much as possible" replaces "trim count to protect the bar" as the operating stance** —
> the bar itself is unchanged: nothing ships below the 9-item DoD, but anything that clears it ships
> rather than being held to a count. The "Spectrum only / C64-second / NES+Amiga deferred" framing
> in the amendments above and the body below is superseded; the per-unit DoD bar and the four
> structural Spectrum artefacts still stand, now joined by the other three platforms' on-ramps.

**Status:** Active. October is a target, not a hard deadline — the project is close to having enough to ship. Shadowkeep scope set by [shadowkeep-32-unit-commitment.md](shadowkeep-32-unit-commitment.md); BASIC by [spectrum-basic-32-games.md](spectrum-basic-32-games.md). The two structural artefacts (landing page, vault) are spec'd in this doc.

**Date:** 2026-05-06 | **Updated:** 2026-05-26

## The decision

The October 2026 Crash! Live launch ships **Spectrum only**. C64, NES, and
Amiga defer wholesale to post-launch — coming-soon cards on the site, full
design preserved in the per-platform `assembly-skeleton.md` drafts under `platforms/`.

The Spectrum launch is **four artefacts at full quality bar**:

1. **The gentle assembly opening** — the Primer ("Meet the Machine"), a *complete* tiny first game, and the start of the re-scoped (cell-based) Shadowkeep, at the atmospheric bar of *Atic Atac* and *Knight Lore*. A learner finishes a real game in assembly by October; the hardest engineering is off the critical path. The shipped cell-snapped units largely survive into this opening. Per [spectrum-assembly-gentle-ramp.md](spectrum-assembly-gentle-ramp.md) and [shadowkeep-32-unit-commitment.md](shadowkeep-32-unit-commitment.md).
2. **Spectrum BASIC Volume 1 (8 games) complete** — Usborne 1984 bar, every topic passes DoD. Per [spectrum-basic-32-games.md](spectrum-basic-32-games.md) (full curriculum is 32 games / 4 volumes / 8 per volume; Volumes 2-4 ship post-October through ~2028-29).
3. **Spectrum landing page** — designed for QR-code visitors arriving from
   Crash! Live flyers and t-shirts.
4. **Spectrum vault: review pass + referenced gap-fill** — every entry linked
   from a shipped unit must exist.

If scope needs trimming, count is cut, never the bar. The cut hierarchy in
§ Cut hierarchy below is binding.

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

Per [shadowkeep-32-unit-commitment.md](shadowkeep-32-unit-commitment.md) (Shadowkeep cuts):

1. Trim Shadowkeep Arc 2 sub-arcs back-to-front (2.4 → 2.3 → 2.2 → 2.1). Arc 1 alone (16 units) is the absolute floor.
2. Only then begin BASIC V1 game cuts — and only below a 4-game floor.
3. Landing page and vault cuts are last resort.

Vault completeness is protected. Quality bar stays full at every step.

## Out of scope (explicit)

- C64 **flagship (Cadence)** and C64 BASIC — coming-soon (but the C64 **Primer + Starfield** are promoted to launch per the 2026-06-03 amendment above). NES / Nightshade, Amiga / Exodus — coming-soon cards.
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
changes (with rationale captured as a log entry below), and reflect
deferred work in the module catalogues (coming-soon cards).

## Anchored in

- [state-lives-in-catalogues.md](state-lives-in-catalogues.md) — project state lives in the `modules/*.yaml` catalogues + git, not in prose.
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
| 2026-06-03 | C64 promoted to a second launch platform: a C64 Primer + Starfield (re-scoped to its real ~16 units; the 112 auto-generated stub units dropped) brought to the finishable bar. Trigger: time pressure eased and the Spectrum validated the gentle-ramp (Meet the Machine + a complete Gloaming shipped — the precondition the C64 skeleton was waiting on). C64 flagship (Cadence) and C64 BASIC stay deferred; NES/Amiga remain deferred. Focus *sequenced* to a second platform, not *widened* to four. |
