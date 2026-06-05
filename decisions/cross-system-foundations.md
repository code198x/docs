# Decision seed: a cross-system foundation layer

**Status:** SUPERSEDED — 2026-06-05 by
[`front-of-curriculum-architecture.md`](front-of-curriculum-architecture.md), which
promoted this seed into the accepted Foundations layer. Kept for the design lineage;
read the architecture doc for the binding decision.

## The idea

Before the per-system "Meet the Machine" on-ramps, a **layer of cross-system
foundational primers** — concepts identical on every machine, taught once,
machine-independent. Number systems was the first candidate; the layer may hold
more.

## What belongs upstream — the test (and the risk)

A concept earns a place in the cross-system layer only if **all three** hold:

1. **Identical across machines** — no platform-specific substance is lost by
   teaching it abstractly.
2. **Teachable without a specific machine** — pure concept, or only trivial
   illustration needed.
3. **Teaching it once removes real redundancy** — every per-machine primer would
   otherwise re-teach it.

**The risk to respect: over-extraction.** "Meet the Machine" works *because* it
teaches concepts **through a concrete machine** — you see the border turn red, the
block appear. Pull too much upstream and the foundation primers go dry and abstract
while the machine primer goes thin. When in doubt, teach it concretely in Meet the
Machine, not abstractly upstream. The cross-system layer is for what is genuinely
*machine-independent*, not for everything that's *common*.

## Candidates, tiered

**Tier 1 — clear (pure concept, no machine needed):**
- **Number systems** — binary / hex / decimal, place value, two's complement.
  ([`number-systems-primer.md`](number-systems-primer.md))
- **Bit logic / Boolean** — AND / OR / XOR / NOT, masking, shifting. Pure logic,
  identical on every CPU; pairs so tightly with number systems it may be one primer.

**Tier 2 — universal *game-dev* models (conceptual, before the specific chip):**
- **How a display works** — pixels, raster scan, the framebuffer, refresh / frame
  rate, colour and palettes, dithering. The universal raster-CRT model before the
  VIC-II / ULA specifics. Distinctively a *game-dev* foundation.
- **How sound works** — waveforms, pitch = frequency, volume = amplitude, ADSR
  envelopes, channels. Before SID / AY / Paula.

**Tier 3 — universal but better kept concrete / per-machine** (the heart of "Meet
the Machine"; at most a light upstream intro, else they gut the machine primer):
- The **CPU model** (fetch–decode–execute, registers, machine code vs assembly).
- The **memory model** (addresses, the memory map, memory-mapped I/O).
- The **game loop / real-time model** (input → update → render per frame, frame sync).
- **2D space / coordinates** (x/y, origin, signed offsets, velocity).

## Sequence

```
BASIC / general programming → [cross-system foundations] → Meet the Machine (per-system) → first game → flagship
```

## Open questions

- Which of Tier 2 / 3 actually become primers vs stay just-in-time in Meet the Machine.
- One combined "how computers work" primer, or several small focused ones.
- Built natively to the raised bar; the whole layer follows the exemplar (which
  proves the bar first). Foundation-completion, not breadth — so likely *welcomed*
  by the depth-first bar rather than gated by it, but decide that explicitly when promoting.
