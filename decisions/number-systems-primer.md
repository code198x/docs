# Decision seed: a cross-system "number systems" primer

**Status:** SUPERSEDED — 2026-06-05 by
[`front-of-curriculum-architecture.md`](front-of-curriculum-architecture.md), which
promoted this seed into the accepted Foundations layer (Number Systems becomes a
Foundations module). Kept for the design lineage; read the architecture doc for the
binding decision.

## The idea

Teach foundational number systems — decimal / binary / hex, place value,
bits / nibbles / bytes, signed values (two's complement), why computers count in
binary, conversion between bases — as a **separate, cross-system primer**, *before*
the per-system "Meet the Machine" assembly on-ramps. Truly ground-up: don't assume
number literacy; build it first.

## Why cross-system

Binary is binary on a C64, a Spectrum, an Amiga, a NES — the concepts are
machine-independent. **One primer serves every platform**: learn it once, apply it
everywhere. It mirrors "Meet the Machine" as a universal series name — this is the
**on-ramp before the on-ramp.** (Working title only: "Meet the Numbers" / "How
Computers Count" — name not chosen.)

## Where it sits

```
BASIC / general programming  →  Number Systems  →  Meet the Machine (per-system asm)  →  first game  →  flagship
```

It's the **bridge into assembly**, where hex / binary / bits become load-bearing.
The BASIC track barely needs them; assembly needs them constantly — so this is
specifically the foundation the assembly on-ramp stands on.

## Knock-on — it strengthens the existing primers

Today "Meet the Machine" teaches number concepts *in passing* (C64 u3 *Everything
Is a Number*, u13 *Working With Bits*, u14 *Bigger Than a Byte*). With a
number-systems primer upstream, Meet the Machine can **assume** that literacy and
stay focused on the *machine* — leaner, and it finally gives the primer a real
"comes off the back of" predecessor (the continuity gap we found in Starfield was
the absence of exactly this kind of upstream module).

## Relation to the raised bar

New content → **built natively to the bar** (incremental milestones, multi-media,
saved-script honest captures) from the start. A strong candidate for the *first*
content built new-to-bar rather than converted, since it's greenfield and
foundational. It follows the exemplar (which proves the bar first).

Depth-vs-breadth: this **completes the foundation** of the on-ramp — it is not a
third system. Arguably depth, not the breadth the bar gates. Worth deciding
explicitly when promoting.

## Open questions

- Name.
- Universal, or assembly-track-specific? (Does the BASIC track want it too?)
- Scope — how many concepts / units.
- Does it need a *machine* at all, or is it pure concept + tiny illustrations
  (and if it runs anything, on which emulator)?
