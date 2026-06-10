# Lineup replan — Amiga · C (PROPOSAL — not applied, SKETCH ONLY)

> **Status: future-spur sketch for review.** Not applied. **Not a full lineup** —
> one short section placing where a C track *would* fit, after Assembly matures,
> and what makes it distinct. No catalogue is proposed; nothing to write into
> `modules/` yet. When/if C earns a real lineup, it gets its own full replan doc
> matching the [`spectrum-assembly.md`](spectrum-assembly.md) template.

## Where C fits

C is a **fourth Amiga path, deferred** — sketched here so the family knows the
slot exists, not scheduled. It sits **after the Assembly track matures**: C on
the Amiga is most honestly taught *once a learner has met the custom chips by
hand*, because the interesting C lesson is the **opposite** trade — letting the
**Amiga OS libraries** do the heavy lifting you previously poked registers for.

C is **not "above" assembly** and **not a graduation from AMOS/Blitz** — same
peer-paths rule as the BASIC fork (`decisions/amiga-basic-amos-and-blitz.md`).
It is a *systems* path with a different centre of gravity: the operating system,
not the bare metal and not a batteries-included game language.

## What makes the C track distinct

| Axis | AMOS | Blitz | Assembly | **C (future)** |
|---|---|---|---|---|
| Centre of gravity | built-in game verbs | compiled speed + hardware | the bare custom chips | **the OS libraries** |
| You reach the screen via | `Screen`/`Bob` | Slices/Shapes/Blit | bitplane + Copper pokes | **`graphics.library` / Intuition** |
| The lesson | immediacy | speed without the OS | the metal | **portable, OS-friendly systems code** |

The distinct C lessons, none of which the other three teach:

- **Intuition** — windows, screens, menus, gadgets, the event loop: writing a
  program that is a *good Amiga citizen*, multitasking-friendly, not a
  system-takeover.
- **graphics.library / layers.library** — drawing through the OS rather than
  seizing the hardware; RastPorts, BitMaps, blitting via the OS.
- **Exec** — messages, ports, libraries, tasks: the multitasking kernel that
  AMOS/Blitz/asm-takeover games mostly bypass.
- **Portable C idioms** — structs, pointers, headers, the toolchain — a bridge
  to modern systems programming the BASIC and asm tracks don't offer.

## Toolchain (period-authentic, deferred)

- **vbcc** (maintained, free, cross-compilable — the licensing-clean modern
  choice) and/or **SAS/C** (the period-canonical commercial compiler) as the
  historical reference point. Stance to confirm at lineup time: teach on **vbcc**
  for a clean pipeline, framed against SAS/C as what the era shipped on — the
  same "maintained toolchain, period-authentic feature set" pattern the BASIC
  fork uses (AmiBlitz3-for-BB2, AMOS Pro).
- **Pipeline gate:** like AmiBlitz3, a real C/OS workflow likely wants more than
  emu198x-amiga's current single-floppy/ADF model (headers, linker, a
  Workbench environment) — so the track is **gated on the same Emu198x hard-disk
  capability** that gates AmiBlitz3, plus an Asm198x/toolchain conversation.
  This is a reason it's a *future* spur, not a near-term one.

## A plausible distinct shape (sketch — illustrative, not a lineup)

If it were built, the C track would climax on **OS-citizen** software, not arcade
spectacle — the thing the other three structurally avoid:

- A primer — *Meet C on the Amiga* — Intuition window, event loop, drawing
  through `graphics.library`.
- A couple of small **OS-native applications** (a tool, a simple utility with
  menus/gadgets) — genres the game tracks never touch, chosen precisely because
  they show C+OS strengths.
- One game built *through the OS* (windowed, multitasking-friendly) to contrast
  directly with the same genre done as an asm system-takeover — the C analogue
  of the AMOS-vs-Blitz contrast lesson.

That contrast — *play nicely with the OS* vs *seize the machine* — is the C
track's reason to exist. Spelling out the full ladder/spine/lineup waits until
Assembly is mature and the toolchain pipeline is proven.

## Settled

- **C is a deferred fourth path**, sequenced after Assembly, distinct by its
  OS-library centre of gravity. Peer, not a rank above assembly.

## Still open

- **Trigger to promote** C from sketch to a full replan doc: Assembly track
  substantially shipped **and** the Emu198x hard-disk / toolchain pipeline
  (shared with the AmiBlitz3 gate) proven.
- **vbcc vs SAS/C** teaching-toolchain stance — decide at lineup time.
- Whether C is even in scope for the October-2026 launch window (almost
  certainly not — it's post-launch). Confirm it's parked, not pulled forward.
