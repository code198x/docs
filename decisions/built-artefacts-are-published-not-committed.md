# Decision: Built artefacts are published, not committed

> **STATUS: Active.** Decided 2026-08-27. Unit build outputs — `.adf`, `.nes`, `.sna`, `.prg`, and
> the Amiga executables — are built by the website's deploy from source and served from the site.
> They stop being committed to [`code-samples`](https://github.com/code198x/code-samples). The
> proof that a build is correct becomes the build itself plus a recorded hash, rather than a blob
> checked in once and never re-derived.

## What a learner gets

A downloadable program per unit, built from the source on the page by the same toolchain the unit
teaches. That is already the intended runtime — [`in-curriculum-wasm-playground.md`](in-curriculum-wasm-playground.md)
records the shippable flow as *"Fuse + downloadable `.sna`"*, with the in-page playground as a
later multiplier. This decision is what makes the download side of that real, and it wires up
`Emulator.astro`, which has existed unused because nothing populated `public/`.

## Why this is possible only now

Until 2026-08-27 the Amiga disk was mastered by `xdftool`, which stamps wall-clock time. Two
builds of unchanged source never matched, so a hash could not describe a program — only the moment
it was built. Committing the artefact was the only way to have a stable one, and even that drifted:
the capture manifest for `meet-the-machine/unit-07` carries a `relock_history` recording exactly
such a change.

`build198x adf` writes the Amiga epoch instead, so the same source now yields the same bytes on
every machine and every run. A hash in a manifest becomes a real check on the build rather than a
snapshot of one laptop.

## The evidence

Measured against a clean export of `HEAD`, with every build output removed first so nothing could
be mistaken for up to date:

| Platform | Rebuild vs committed |
|---|---|
| NES | **51 of 51 byte-identical** |
| Spectrum | **4 of 5 byte-identical** (the fifth is not built by `all`) |
| Amiga | 0 of 69 byte-identical — equivalent, not identical |

The Amiga disks carry the same files at the same sizes, the same block counts, and a boot block
byte-identical to `xdftool`'s `boot install boot1x`. They differ in three ways, none of them
content: the volume and file timestamps, the file protection bits (`----rwed` where the retired
`xdftool` recipe set `------e-`, both of which carry `e` and both of which run), and — for four
`flock` units — four bytes inside the executable, where the relocation offsets are listed in a
different order. A structural comparison of hunk payload and relocation sets shows those equal, and
the AmigaDOS loader applies relocations in any order.

**So the Amiga hashes re-lock once.** That is a one-time cost, paid deliberately, and it is the
reason to settle [build198x#26](https://github.com/build198x/build198x/issues/26) (caller-set
protection bits) before re-locking rather than after — otherwise the same 69 hashes change twice.

## Why not keep committing them

Not size. All 69 ADFs occupy about **70 KB** in the pack, because an 880K floppy holding a 200-byte
program is almost entirely zeros; one compresses to 1,337 bytes. The whole repository is 12.45 MiB,
of which `.wav` files are 6.33 MB. Anyone arguing this on weight is arguing about the wrong files.

The reasons are that a committed artefact proves nothing about whether the build still works, and
that the repository's own stated policy already says not to. `.gitignore` opens with `# Build
outputs` and lists `*.prg`, `*.bin`, `*.d64`, `*.tap`, `*.sna`. C64 obeys it exactly — zero tracked
`.prg`. Amiga and NES have no rule at all, `.sna` has one that five tracked files predate, and two
Amiga executables are ignored **by name** (`signal`, `hop`) while their siblings are tracked. This
decision finishes a rule that was half-applied, rather than inventing one.

## What must be true before artefacts leave the repository

In this order. The removal is last, not first.

1. The deploy builds every unit and publishes the results. Both tools ship Linux binaries —
   `asm198x` 0.0.35 and `build198x` 0.2.3 — so a standard runner suffices.
2. The build is proven against what is committed today: NES and Spectrum must still reproduce
   byte for byte, and the Amiga disks must remain equivalent by listing, block count and boot
   block.
3. `build198x#26` lands, and the Amiga capture manifests re-lock once against the settled bytes.
4. Only then do `*.adf`, `*.nes` and the Amiga executables join `*.prg` in `.gitignore`.

## What this changes for a fresh clone

`_capture/verify.py` hashes the artefact on disk against `media_sha256` and `executable_sha256`.
Once artefacts are not committed, `make verify` in a fresh clone fails until `make` has run. That
is correct — it is the check doing its job — but it reads as a broken test to someone who has not
built yet, so the unit READMEs must say to build first.

## Drift triggers

- **"Commit the artefact, it is only a few KB"** — the size was never the argument, and the answer
  does not change when the file is small. A blob checked in once records that a build worked on
  someone's laptop on some day. Publish it from a build instead.
- **"Reproduce the old bytes exactly so the hashes do not change"** — not possible for the Amiga,
  and not the goal. The disks are equivalent, not identical; the hashes re-lock once, deliberately.
- **"The site can just link to the file in the repository"** — that reintroduces the commit, and
  ties a public URL to a path in a source tree.
- **"Skip the build step, artefacts rarely change"** — a build that is not run is a build that has
  stopped working, and nobody finds out until a learner does.
