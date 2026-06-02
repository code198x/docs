# Superseded — Shadowkeep engine-first specs (frozen 2026-06-02)

These documents spec the **original engine-first Shadowkeep** — the 2026-05-18
"32-unit, two-arc" plan ([shadowkeep-32-unit-commitment.md](../../../../../decisions/shadowkeep-32-unit-commitment.md),
since amended). That design was built on three commercial-bar engine changes:
**pre-shifted, masked sprites; a Y-sorted object system; and tile-map collision
decoupled from the attribute layer.**

On **2026-05-29** Shadowkeep was re-paced ([spectrum-assembly-gentle-ramp.md](../../../../../decisions/spectrum-assembly-gentle-ramp.md))
and later reset to the **cell-based _Place_** — pass 1 of a game taught across
several modules. The Place **carries Gloaming's engine**: cell-snapped movement,
single-draw sprites with save/restore, attribute-coupled collision, bitmap
dithering for stone and light. It does **not** pre-shift, mask, Y-sort, or
decouple collision. So these specs are **not current guidance for Shadowkeep.**

They are kept — not deleted — because the three techniques were **relocated, not
dropped.** They become the load-bearing lessons of later *rendering games*:

| Spec | Relocated technique | New home |
|---|---|---|
| `sprite-shifter.md` | pre-shifted + masked sprite drawing | Smooth Motion (pre-shift), Overlap (masking) |
| `object-system.md` | Y-sorted depth + dispatched draw | Greypeak (Y-sort + isometric) |
| `tile-map.md` | collision decoupled from the attribute layer | the rendering games |
| `engineering-plan.md` | execution plan for the whole old engine | reference only |
| `memory-budget.md` | 48 KB budget for the old engine | reference only |

**Frozen as-was.** Their internal cross-links and "32-unit / Arc 1+2" framing
are of their time and are not maintained. Lift the engineering from them when
the rendering games are built; do not follow them for the Place.

**Current sources of truth:** [`../brief.md`](../brief.md),
[`../per-unit-plan.md`](../per-unit-plan.md), the amended
[`shadowkeep-32-unit-commitment.md`](../../../../../decisions/shadowkeep-32-unit-commitment.md) +
[`shadowkeep-four-arc-framing.md`](../../../../../decisions/shadowkeep-four-arc-framing.md),
[`modules-not-games.md`](../../../../../decisions/modules-not-games.md), and
[`curriculum-structure.md`](../../../../../decisions/curriculum-structure.md).
