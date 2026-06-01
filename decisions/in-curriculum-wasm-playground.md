# Decision (exploratory): In-curriculum WASM playground

> **STATUS: Exploratory — door held open, not yet binding.** Noted 2026-06-01. Records the intent
> to eventually offer an in-page *edit → assemble → run* loop inside curriculum units — a WASM
> assembler ([Asm198x](../../../Asm198x/CLAUDE.md)) plus the [Emu198x](../../../Emu198x/CLAUDE.md)
> core, embedded in the lesson — and, more importantly, the reasoning that this is a **post-launch
> multiplier, not an October gate**, and that **content authored now is forward-compatible** with it.

## The idea

Today a learner reads a unit, copies the `.asm`, assembles it (Docker/pasmonext), and loads the
`.sna` in Fuse. A playground would collapse that into the page: edit the code, press run, watch the
border change *in the unit*. For a curriculum whose entire thesis is *"the screen is memory — write
a byte, see it change,"* that's the most direct possible delivery of the lesson.

## Why it's a multiplier, not a gate

- **October is content-gated**, and the shippable learner runtime is **Fuse + downloadable `.sna`**
  (see [october-2026-launch-spec.md](october-2026-launch-spec.md)). That flow is clunky but
  complete. The playground is additive polish — a strong *launch+1* headline ("now runnable in your
  browser"), not something the launch fails without.
- **The runway forces the call:** ~4 months to October. Pulling a WASM assembler *and* emulator
  onto that critical path would consume the content time that is the actual gate. Protect content.

## The reassurance: authoring now is forward-compatible

This is the load-bearing point. Every unit keeps its code in a real `.asm`, referenced by
`<CodeFromFile src="…">`, each a complete program that assembles with a verified result. That is
exactly what a playground consumes:

- `<CodeFromFile>` → `<CodePlayground>` later, pointing at the **same files**. No rewrite.
- The verified screenshots stay useful — the "what you'll see" preview, the no-JS fallback, the
  OG/SEO image.
- So the content corpus we write now is the playground's exhibit set. Authoring **compounds**; it
  does not race against replacement.

This also explains *why the "code in files, never inline" rule
([examples-as-files-and-screenshots.md](examples-as-files-and-screenshots.md)) is future-proofing*,
not just tidiness: inline code in MDX could never become a playground; a `CodeFromFile` reference
can. Keep authoring to that rule and the playground stays cheap to add.

## Sequencing (when the time comes — post-launch)

1. **Asm198x → WASM first.** It's the cheap, high-leverage half: a clean, single-binary Rust
   assembler is an ideal WASM target. Spike this first.
2. **Emu198x core → WASM.** The core already runs **headless today** (that's how this repo captures
   screenshots), so it's already decoupled from the GUI deps (winit/wgpu/muda) — the hard part of a
   port is done. Compile the core + a canvas renderer.
3. **Swap the component.** `CodeFromFile` → `CodePlayground` over the existing `.asm` corpus.

## Relationship to Forge198x

[Forge198x](../../../Forge198x/CLAUDE.md) is the *standalone* dev workbench (umbrella-scoped,
deferred, gated on Asm198x maturity). This note is a *different, lighter surface*: an inline lesson
widget in the curriculum site, not an IDE. They share the same WASM-tooling dependency (Asm198x +
Emu198x core to WASM); whichever is built first de-risks the other.

## What this constrains now

Nothing to build. The one live constraint is the discipline we already follow: **author every code
sample as a complete, `CodeFromFile`-referenced `.asm` with a verified result, never inline.** That
is the forward-compatible substrate — keep doing it and the door stays open.

## Status

Exploratory, 2026-06-01. Door held open. Promote to binding (with a build plan) post-launch, after
Asm198x matures. Relates to [october-2026-launch-spec.md](october-2026-launch-spec.md),
[examples-as-files-and-screenshots.md](examples-as-files-and-screenshots.md), and the Asm198x /
Emu198x / Forge198x sibling decisions.
