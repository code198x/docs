# Next-tier baseline — lighting up the ready four

**Purpose:** The plan-shape for taking the `next`-tier systems from "validated,
in build" to shipped on-ramps. This is a plan, not a status board — current
state is queryable (`npm run surfaces:gaps` in the website repo reads the
`emu198x` / `devReady` flags and cross-checks the Emu198x crates), and per
[state-lives-in-catalogues](../decisions/state-lives-in-catalogues.md) it stays
there.

**Bottom line:** Four of the six `next` systems — **VIC-20, Master System, BBC
Micro, MSX** — already have an Emu198x core, full Asm198x ISA coverage, and
completed toolchain research choosing the family-native path. For each, the
baseline is three gates in sequence, each with a visible flip. The other two
(**CPC, Atari ST**) are blocked on the emulator surface and are parked below.

---

## The three gates

Every ready system passes the same gates, in order. Each gate ends in a
there-or-not artefact — a flag flip or a shipped page — so progress is never a
judgement call.

1. **Core verification → `emu198x: true`.** The core exists; the bar is
   boots-and-validates plus **capture parity** (the shots/video a unit needs
   come out right — timing, input scripting, exact frame). Core bugs found here
   are Emu198x issues, filed not fixed from this side.
2. **End-to-end toolchain → `devReady: true`.** Assemble with Asm198x, frame
   into the platform container, boot the artefact in the core. The container is
   the only real gap per each platform's TOOLCHAIN-RESEARCH (all four
   assemblers are done; see the per-system table). Program framing (`.prg`,
   `.sms`, `.rom` headers) is Asm198x packaging-roadmap work; media mastering
   (`.ssd`, `.cas`, `.d64`) is Build198x demand-gate work.
3. **On-ramp curriculum → `tier: live`.** The established shape per the
   [gentle-ramp decision](../decisions/spectrum-assembly-gentle-ramp.md): a
   "Meet the Machine" primer plus one complete, finishable first game, at the
   full 8-item DoD bar. Plus the website artefacts every live platform has:
   landing page, getting-started, module catalogue, code-samples.

Gates 1 and 2 are cheap and can run as one pass across all four systems.
Gate 3 is the expensive editorial work and is per-system, post-launch scope.

---

## The ready four

| | VIC-20 | Master System | BBC Micro | MSX |
|---|---|---|---|---|
| CPU | 6502 | Z80 | 6502 | Z80 |
| Container gap | `.prg` (2-byte header; shared with C64) | `.sms` (raw ROM; flat `.bin` is nearly valid) | `.ssd`/`.dsd`/`.uef` (real mastering work) | `.rom` cartridge (16/32 KB + header) |
| Gap owner | Asm198x framing | Asm198x framing | Build198x mastering | Asm198x framing |
| Toolchain research | [done](../platforms/commodore-vic-20/TOOLCHAIN-RESEARCH.md) | [done](../platforms/sega-master-system/TOOLCHAIN-RESEARCH.md) | [done](../platforms/bbc-micro/TOOLCHAIN-RESEARCH.md) | [done](../platforms/msx/TOOLCHAIN-RESEARCH.md) |
| Primer subject | The 22-column machine: VIC chip, ~5 KB RAM, constraint as character | The console after NES: VDP tiles, no BASIC, cartridge-first | MODEs, the OS ROM, sideways ROM discipline | Slots, the BIOS, TMS9918 VDP |

**Suggested order:** VIC-20 → Master System → BBC Micro → MSX. The first two
have near-trivial container gaps; the BBC's `.ssd` is the first real Build198x
mastering item; MSX's cartridge header sits between. Order within gate 3 is
editorial and can differ.

These are the first platforms with **no Docker toolchain to retire** — they
scaffold straight onto Asm198x + Emu198x per the
[dev-tooling-migration decision](../../decisions/code198x-dev-tooling-migration.md),
and each one proven strengthens the migration case for the launch four.

### Per-system punch-list (identical shape, four instances)

- [ ] Core boots-and-validates + capture parity verified → flip `emu198x`
- [ ] Container emitted (Asm198x or Build198x per table) and boots in core
- [ ] End-to-end proven: source → artefact → boot → capture → flip `devReady`
- [ ] Meet the Machine primer written (subject per table)
- [ ] First-game brief written (per [brief spec](../specifications/brief.md))
- [ ] First game shipped at DoD bar; landing page + getting-started + catalogue
- [ ] `tier: live`

---

## Parked: CPC and Atari ST

Both are `next`-tier, ISA-covered (Z80 / 68000), and have **no Emu198x core and
no docs scaffolding**. Their gate 1 is an Emu198x scope decision, which the
curriculum does not owe (per the
[support-surfaces decision](../../decisions/support-surfaces.md)) but which
everything downstream waits on. The CPC is a long-standing wanted target, so if
either moves, it moves via an Emu198x conversation first — nothing in this
document unblocks them.
