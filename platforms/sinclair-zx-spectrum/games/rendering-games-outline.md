# The Rendering Games — Smooth Motion → Overlap → Greypeak (outline)

> **Status:** Draft outline, 2026-05-29, per
> [`spectrum-assembly-gentle-ramp.md`](../../../../decisions/spectrum-assembly-gentle-ramp.md).
> These three games **spread the advanced rendering Trunk** that the old plan crammed into
> Shadowkeep. They come *after* Shadowkeep (cell-based), each motivated by a felt limitation of the
> one before. "Smooth Motion" and "Overlap" are working titles (small games); **Greypeak** is the
> named Volume 1 *Depth* game. Unit counts are **illustrative, not targets** — described here by
> capability. Each gets its own folder when spec'd.

## Why these three, in this order

The chain is a **dependency chain *and* a felt-need chain** — each game answers a frustration the
learner earned in the previous one, and each technique needs the previous technique to work:

| Game | Felt limitation it answers | Major technique | Needs |
|------|----------------------------|-----------------|-------|
| **Smooth Motion** | Shadowkeep's hero jumps a whole cell — jerky | Pre-shifted sprites (sub-cell movement) | Shadowkeep's cell sprite |
| **Overlap** | The smooth sprite is a solid box — it smears over scenery and can't share space with another sprite | Masked sprite drawing | pre-shifted sprites |
| **Greypeak** | Masked sprites draw in fixed order — a sprite "behind" wrongly covers one in front; and the world is flat | Y-sort depth + isometric projection | pre-shift **and** masking |

After Greypeak the full Trunk (pre-shift + mask + Y-sort + iso) is composed, and **every later game
inherits it**. This is the Trunk that the gentle-ramp decision moved *out* of Shadowkeep — now
arriving one major at a time, each one wanted before it's taught.

This is the deprecation-pair pedagogy made literal: the learner shipped the simple version in an
earlier game (cell-snapped, single-draw, flat order) and *feels* its limit before meeting the
upgrade. That only works because Shadowkeep comes first.

---

## Smooth Motion *(working title)* — **pre-shifted sprites**

**The felt limit:** in Shadowkeep the hero moves a full 8-pixel cell per step. Side by side with
any arcade game it looks like it's hopping. The learner *wants* it to glide.

**The major:** pixel-level movement via **pre-shifted sprite tables** — and the realisation that
smoothness is a *drawing* problem, not a *movement* problem.

**Builds on:** Shadowkeep's cell sprite + save/restore; the Primer's bytes-and-shifts.

**Capability beats** (count not fixed):
- **Why it hops** — track position in *pixels*, not cells; the low 3 bits are the sub-cell offset.
- **One sprite, eight shifts** — an 8×8 sprite shifted 0–7 pixels right becomes up to 16 bits wide
  (two bytes per row). Pre-compute all eight shifts into a table (build-time or at start-up).
- **Pick the frame** — choose the pre-shifted frame from the low 3 bits of the X position.
- **Draw across two cells** — the shifted sprite spans two columns; write both bytes per row.
- **Save/restore, widened** — save and restore the now-two-wide background rectangle so the glide
  leaves no smear.
- **The glide** — move 1–2 pixels per frame; vertical sub-cell is just choosing the row address.
- **A small game** to make the smoothness the star.

**The limit it leaves (→ Overlap):** the sprite is still a *solid rectangle*. The moment it crosses
detailed scenery or another sprite, the saved-rectangle trick paints a visible box or erases what it
overlaps. Save/restore can't cope with two things sharing pixels.

---

## Overlap *(working title)* — **masked sprite drawing**

**The felt limit:** Smooth Motion's sprite carries a box of background with it. Over a plain floor
you don't notice; over decoration, or when two sprites touch, the box and the smear are obvious. The
learner *wants* sprites that pass cleanly over anything.

**The major:** **masked sprite drawing** — the sprite's transparent pixels let the background show
through, so nothing needs saving or restoring under the sprite at all.

**Builds on:** Smooth Motion's pre-shifted sprites (the **mask is pre-shifted too**).

**Capability beats** (count not fixed):
- **The mask** — a second bitmap marking which pixels are transparent.
- **AND then OR** — read the screen byte, AND the mask (punch a sprite-shaped hole), OR the sprite
  data, write it back. The background survives where the sprite is transparent.
- **Over scenery** — walk the sprite over pillars and decoration with no box, no smear.
- **Two sprites, one space** — overlapping sprites combine instead of erasing each other.
- **Pre-shifted masks** — the mask shifts with the sprite (closes the loop with Smooth Motion).
- **A small game** with sprites moving over a busy background.

**The limit it leaves (→ Greypeak):** masked sprites overlap cleanly but draw in *fixed order*. A
sprite that should be *behind* another still paints over it. And the world is flat — there's no way
to show one thing in front of or above another in space.

---

## Greypeak — **Y-sort depth + isometric projection** *(the named Depth game)*

Volume 1's *Depth (Spatial Illusion)* game — Ritman / Knight Lore isometric tradition. A **full
game with sub-arcs**, not a small insert; this is where the rendering Trunk finishes composing.

**The felt limit:** masked sprites overlap, but order is wrong, and the keep was flat. The learner
*wants* a world with depth — things in front of and behind each other, the Knight Lore look.

**The majors (two, spread across sub-arcs):** **Y-sort depth ordering** and **isometric projection**.

**Builds on:** pre-shift (Smooth Motion) **and** masking (Overlap) — iso sprites must move smoothly
*and* occlude cleanly, so both are prerequisites. This is why Greypeak sits third.

**Sub-arc headlines** (counts not fixed; full spec when it gets its own folder):
- **Back to front** — an object list sorted by Y, drawn far-to-near, so nearer (masked) sprites
  correctly occlude farther ones. Depth from draw order.
- **The isometric room** — iso projection: draw a 3D-looking room from a tile/height map.
- **Moving in space** — smooth, masked, depth-sorted movement through the iso room.
- **The illusion as a game** — Greypeak's spatial-illusion gameplay on the full stack.

**What it leaves:** nothing owed back down the chain — the Trunk is complete. Later volumes inherit
pre-shift + mask + Y-sort and specialise (scrolling, 3D, etc.) per the track decision's branches.

---

## Budget check (the point of this pass)

- **Smooth Motion:** one major (pre-shift). ✓
- **Overlap:** one major (masking). ✓
- **Greypeak:** two majors (Y-sort + iso) — appropriate for a *full game with sub-arcs*, each sub-arc
  staying at one or two; not a small insert. ✓
- Each is **motivated by the prior's felt limitation** and **needs the prior's technique** — strict
  dependency order, no leaps. The Trunk that overloaded Shadowkeep now spreads across three games,
  arriving exactly when wanted. The re-plan's core claim holds.

## Open for the author

- **Real names** for Smooth Motion and Overlap (working titles; small games — pick game vehicles
  whose fun *is* the technique: smoothness, clean overlap).
- **Greypeak's full per-unit spec** — its own folder + plan when it comes up the queue; this outline
  only fixes its place and prerequisites in the chain.
- Whether Smooth Motion and Overlap stay two small games or fold into one — keep them split unless a
  combined game still reads as one or two majors; the felt-limit handoff between them is the teaching.
