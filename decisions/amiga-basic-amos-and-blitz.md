# Decision: Amiga BASIC — Two-Track Fork (AMOS + Blitz)

## The decision

The Amiga BASIC curriculum is a **deliberate two-track fork** — an **AMOS**
track and a **Blitz** track — taught as a *cultural survey of a real
historical split*, not as two interchangeable BASICs. The two tracks exist to
make the **contrast** the lesson: interpreted-and-immediate versus
compiled-and-near-the-metal.

Three calls fix the shape:

1. **Both tracks, distinct roles.** AMOS is the approachable, primitives-first
   on-ramp and the authentic UK bedroom-coder / PD artefact. Blitz is the
   compiled, performance-aware, "ship a real game" track that bridges toward the
   assembly track. Neither teaches the same techniques twice in two languages —
   each climaxes on what the other *cannot* do.
2. **Blitz first.** Despite AMOS being the gentler language, the **Blitz track
   is built and shipped first** because it is licensing-clean and pipeline-ready
   today, whereas AMOS carries two stacked frictions (binary redistribution +
   tokenised source) that need resolving before its track can stand up. Blitz
   proves the Amiga-BASIC pipeline; AMOS follows once its open actions close.
3. **Teach on the maintained toolchains, within a period-authentic feature
   set.** Blitz is taught on **AmiBlitz3** (the living Apache-2.0 descendant),
   writing within the original Blitz BASIC 2 feature set. AMOS is taught on
   **AMOS Professional** (not AMOS 1.3, not AOZ).

This record **formalises and supersedes the framing of** the existing working
skeleton [platforms/commodore-amiga/basic-skeleton.md](../platforms/commodore-amiga/basic-skeleton.md),
which already gestures at both tracks but predates the verified licensing facts
below and still uses the retired fixed-count framing ("512 units / 8 games ×
64"). Unit and game counts here are **illustrative**, per
[curriculum-structure.md](curriculum-structure.md) and
[modules-not-games.md](modules-not-games.md); the powers-of-2 / fixed-count
framing is retired. Budget is on techniques-per-game and the quality bar, not
unit totals.

## Why

The Amiga is the odd one out among the systems. On a Spectrum or C64 the
machine's built-in BASIC is the obvious spine of a BASIC track. The Amiga's
stock **AmigaBASIC** (Microsoft-written) was slow, clunky, and dropped by
Commodore because it broke on later Kickstarts and AGA. There is no authentic
"just use the built-in BASIC" path for Amiga game development. The real Amiga
BASIC story **is** AMOS and Blitz — they are the proper options, not a
compromise.

The two are a genuine fork, not two flavours of one thing:

- **AMOS** (François Lionet, 1990; descendant of STOS on the Atari ST) —
  interpreted, with its own editor and tokenised format, game primitives baked
  in (Bobs, sprites, screens, double-buffer, music) reachable in a line or two.
  The UK PD / shareware scene ran on it. A walled garden: you learn *AMOS*,
  largely not *the Amiga*.
- **Blitz BASIC 2** (Mark Sibly / Acid Software, New Zealand, ~1991) — compiles
  to native 68k, fast, reaches into Amiga libraries and hardware. Behind
  actually-shipped commercial games. Steeper, more structured.

Teaching both shows there is no single right tool — different problems reward
different approaches — and it gives the Amiga something no other system in the
fleet can offer (see the abstraction ladder below).

## The fork is the curriculum

The principle that keeps "both" honest: **structure for contrast, not
coverage.** If a learner finishes both tracks and the only difference they felt
was syntax, the doubling failed. Each track must climax on what the other
structurally cannot do.

- **AMOS climax** — lean into immediacy and built-in primitives: Bobs, sprites,
  AMOS music, the seconds-long edit-run loop. A genre that *suits* high-level
  primitives (a sprite-driven arcade game). The lesson: how far you get, how
  fast, when the language hands you game verbs.
- **Blitz climax** — pick something that would crawl under interpreted AMOS:
  many objects, smooth scrolling, native speed, reaching into libraries. This is
  where the curriculum reveals *why* the scene graduated to Blitz — and where
  Worms earns its name-drop.

## Sequencing: Blitz first

> **Superseded by reality — see "Update 2026-06-09" below.** AMOS shipped first.
> The "Blitz is the easier track to stand up" reasoning assumed scriptable CLI
> compilation *under our emulator*, which turned out false: emu198x-amiga is
> single-floppy (ADF only; no HDF) and AmiBlitz3 needs a hard disk. The text
> below is preserved as the 2026-06-02 position.

Counter-intuitive (AMOS is the easier *language*) but correct (Blitz is the
easier *track to stand up*). Blitz/AmiBlitz is licensing-clean, plain-text, and
scriptably compilable today — it fits the build-and-screenshot pipeline with no
preconditions. AMOS needs a licensing conversation (or a from-source build) and
tokeniser tooling before its track can run in CI. So Blitz goes first and proves
the pipeline; AMOS follows once its open actions close.

The order also tells the historical story for free: AMOS was the entry drug the
bedroom scene came in on; Blitz is where people went to ship serious work.

## Update 2026-06-09 — pipeline reality (AMOS shipped first; Blitz path revised)

Three facts overturn the sequencing above, learned by building:

1. **AMOS shipped first, and works.** The complete **Meet AMOS** primer (17 units)
   is built and live. The tokeniser snag was sidestepped entirely: we **type ASCII
   source into the AMOS editor** via a headless `type_string` and press F1 — no
   `.AMOS` round-trip needed. The AMOS Pro System disk **self-boots** into its
   editor on emu198x-amiga (a500-plus / KS2.04, single floppy). See
   [[code198x:amos-pro-headless-pipeline]] (global KB) for the proven recipe.

2. **emu198x-amiga is single-floppy; AmiBlitz3 cannot run on it.** The emulator
   exposes one `--disk` (ADF only; its MCP layer states *"Only `adf` is wired
   today; `hdf`/`ipf` reserved"*). **AmiBlitz3** needs a **35 MB hard disk, 8–12 MB
   RAM, 68020+, Workbench 2.1+**, and has **no documented CLI compiler** (IDE
   only). So the record's "Blitz pipeline-ready, fits the Docker build directly"
   is false *for our emulator*: standing AmiBlitz3 up is substantial **Emu198x**
   work (HDF mount + a WB/AmiBlitz3 HD image + a 68020/Fast-RAM model + a
   non-interactive compile path). AmiBlitz3 remains the **licensing-clean shipping
   target**, gated on that Emu198x capability.

3. **Original Blitz BASIC 2 is the AMOS-parallel short-term path — full pipeline
   PROVEN end-to-end.** The real **BB2 v1.60 "Amiga Format" single-disk** coverdisk
   release **self-boots** into the Ted editor on emu198x-amiga (a500-plus / **KS2.04**
   — under KS1.3 the editor's console fails to open; 2.04's ROM console is required)
   once its `s/startup-sequence` is edited to launch `blitz2` directly (same trick as
   the AMOS template). **ASCII source types in via the existing Amiga `type_string`**
   with correct syntax-highlighting and symbols (US keymap matches), and BB2 source is
   **plain text** (no tokeniser — more git-friendly than AMOS).

   **Compile-and-run trigger: `right-Amiga + X`** (the Compiler menu's COMPILE/RUN
   command key; RUN = ⌘M, CREATE FILE = ⌘E). The BB2 User Guide's *prose* shortcut
   list omits these, but the Compiler **menu itself** shows the command keys — so
   there IS a keyboard trigger, no fragile mouse-menu navigation needed. The full
   loop **boot → `type_string` → right-Amiga+X → capture** produces the compiled
   program's output ("Blitz 2 CLI Window"). The Blitz analogue of the AMOS F1 flow.
   **Verified end-to-end 2026-06-09.**

   *History: this was briefly blocked because the right mouse button didn't open
   Intuition menus headless (emu198x [#63](https://github.com/emu198x/emu198x/issues/63),
   fixed same day) — but the menu turned out unnecessary once the `right-Amiga+X`
   command key was found. The earlier `right-Amiga+R` test did nothing only because
   Amiga-R = Replace; the qualifier path was fine.*

**Revised sequencing:** AMOS first (done). Blitz authored short-term on **BB2 (AF
single-disk)** within the BB2 feature set (forward-compatible with AmiBlitz3);
AmiBlitz3 becomes the
licensing-clean CI/shipping toolchain once Emu198x gains hard-disk support. The
"contrast, not coverage" principle and the BB2-feature-set constraint are unchanged.

## The three-rung abstraction ladder

The fork gives the Amiga a teaching spine no other system in the fleet has —
three rungs of abstraction on one machine, building roughly comparable games:

> AMOS (high-level, interpreted) → Blitz (compiled, touches the hardware) →
> 68000 assembly (the metal)

Design the Blitz track as the deliberate bridge *into* the assembly track, not a
dead end. A learner climbs down toward the hardware one rung at a time.

## Licensing — verified

Researched against primary sources, 2026-06-02. **The two tracks are not
symmetric.** Blitz is clean across the board; AMOS carries a real, unavoidable
binary-redistribution snag.

| Item | AMOS | Blitz / AmiBlitz |
|------|------|------------------|
| **Source licence** | AMOS Professional **source is MIT** (Lionet, Apr 2020) — but MIT covers *source only* | **AmiBlitz3 is Apache-2.0** (confirmed via GitHub API, formalised v3.11.0, Nov 2024) |
| **Binary / disk redistribution** | **No primary source licenses the runtime / ADF disks** — tolerated abandonware, not granted | Apache-2.0 covers the whole toolchain — clean redistribution, no copyleft |
| **Original-vs-version** | Use **AMOS Professional**, not AMOS 1.3 (weaker "BSD-style" 2001 release, unverified text) | Use **AmiBlitz3**, not original 1993 BB2 binaries (no open licence; `nitrologic/blitz2` source disclaims rights) |
| **Viable-modern-dev (tier test)** | Murky — preservation forks, no maintained official line | Strong — actively maintained, latest v3.11.4 (Mar 2026) |

**The binary snag is sharper than "link, don't bundle."** Telling learners where
to download AMOS does not solve CI: Code198x builds and screenshots code in a
Docker image, so the build environment itself must contain the AMOS runtime —
that is de facto redistribution. So the AMOS track has only two real paths:

1. **Get an explicit grant from Lionet** (reachable via AOZ Studio; the MIT
   source release signals he would likely agree to redistributing AMOS Pro disks
   in a free educational course). His written reply becomes the licence basis.
2. **Build AMOS Pro from its MIT source** and ship that binary under MIT.
   Legally cleanest, but non-trivial — it is 68k assembly needing a
   cross-assembler. (Notably the kind of thing Asm198x exists to do.)

**AOZ Studio is ruled out** — Lionet's modern JS-transpiler successor is not
period-authentic (no 68k, no ADF, no Amiga OS).

Verified facts worth keeping:

- **Worms (Team17, 1995) was written in Blitz BASIC 2** — direct quote from
  Team17's Debbie Bestwick (MCV/Develop retrospective). Andy Davidson originally
  entered it in an *Amiga Format* Blitz BASIC competition.
- **Skidmarks (Acid, 1993)** — "95% written in Blitz BASIC" (Nostalgia Nerd).
  Both Worms and Skidmarks are Acid-adjacent, but the Worms attribution is
  independently well-sourced.
- **AmiBlitz3 is additive over BB2** — redimensionable arrays, dynamic lists,
  more function args, etc. are opt-in extensions. Original BB2 code compiles on
  AmiBlitz3; the reverse is not guaranteed. So "teach on AmiBlitz3, stay within
  the period BB2 feature set" works.

Sources (primary, captured 2026-06-02):

- AMOS Pro MIT release — <https://github.com/AOZ-Studio/AMOS-Professional-Official>
- AMOS Pro release announcement — <https://www.amigans.net/modules/newbb/viewtopic.php?topic_id=8218>
- AmiBlitz3 (Apache-2.0) — <https://github.com/AmiBlitz/AmiBlitz3>
- AmiBlitz3 v3.11.0 release notes (Apache-2.0 added) — <https://github.com/AmiBlitz/AmiBlitz3/releases/tag/v3.11.0>
- Original BB2 source, rights disclaimed — <https://github.com/nitrologic/blitz2>
- Worms / Blitz BASIC (Bestwick quote) — <https://mcvuk.com/business-news/history-lesson-the-story-of-worms/>
- Skidmarks / Blitz BASIC — <https://www.nostalgianerd.com/skidmarks-amiga-review/>
- AOZ Studio (ruled out) — <https://www.aoz.studio/story>

## Workflow and tooling implications

The build-and-screenshot pipeline ([examples-as-files-and-screenshots.md](examples-as-files-and-screenshots.md),
[incremental-code-samples.md](incremental-code-samples.md)) lands very
differently on the two tracks:

- **Blitz: green light.** Plain-text `.ab3` source (git-friendly, diff-able) and
  confirmed CLI compilation —
  `AmiBlitz3 -s "DH0:src.ab3" -e RAM:out.exe` — runs scriptably under emulation.
  No tokeniser round-trip; fits the Docker build directly. One housekeeping
  item: confirm with the AmiBlitz maintainer that no files retain GPL provenance
  from before the Apache relicence, before bundling the toolchain.
- **AMOS: amber.** Source is **tokenised inside the editor**, so the track needs
  a tokeniser / detokeniser round-trip to keep readable source in git and feed
  the build. That tooling stacks on top of the binary-redistribution decision
  above. This is the single biggest reason AMOS is sequenced second.

## Open actions

> **2026-06-09 additions (Blitz-track gating, from the build):**
> - [x] ~~**Right-mouse-button Intuition menus in emu198x-amiga**~~ — **moot.** Filed as emu198x #63 and fixed same day, but the BB2 compile trigger turned out to be the keyboard command key **`right-Amiga+X`** (no menu needed). Full BB2 compile-and-run pipeline proven end-to-end 2026-06-09.
> - [ ] **BB2-ADF redistribution** — original Blitz BASIC 2 binaries have no open licence (`nitrologic/blitz2` disclaims rights). Same tolerated-for-local-capture / not-for-CI status as the AMOS Pro ADF below. The AF coverdisk version was a deliberate free giveaway, but that is not a formal redistribution grant — do **not** bundle into CI/curriculum unresolved.
> - [ ] **AmiBlitz3 on emu198x-amiga** *(Emu198x session — gates the licensing-clean shipping toolchain).* Needs HDF mount + a WB/AmiBlitz3 hard-disk image + a 68020/Fast-RAM model + a non-interactive compile path. Large; not required for short-term BB2 authoring.
>
> The original AMOS-track actions below are largely **resolved in practice**: AMOS shipped via type-into-editor (no tokeniser needed), and "AMOS in Emu198x" is proven. Only AMOS-ADF *redistribution* (for CI) remains genuinely open — same bucket as BB2-ADF.

These gate the AMOS track (not the Blitz track) and are explicit TODOs:

- [~] **AMOS redistribution** — either secure an explicit grant from Lionet for
  AMOS Pro disk images in a free educational curriculum, **or** commit to
  building AMOS Pro from its MIT source. Decide which; record the outcome here.
  *In progress: outreach asking whether the MIT release covers redistributing a
  runtime built from source, with a compiled-runtime fallback. First send via the
  AMOS-Professional-Official GitHub contact email bounced (stale). **Sent
  2026-06-02 via LinkedIn DM** (existing connection — linkedin.com/in/francoislionet,
  he returned to active posting ~April 2026). Awaiting reply. Build-from-source
  remains the fallback path if no grant comes.*
- [ ] **AMOS source round-trip** — design / source the tokeniser-detokeniser so
  AMOS source can live as plain text in git and build in CI.
- [ ] **AMOS in Emu198x** — confirm Emu198x can host the AMOS editor/runtime and
  screenshot non-interactively (its interactive editor is the risk).
- [ ] **AmiBlitz GPL-provenance check** — open an issue asking the maintainer to
  confirm the whole AmiBlitz3 tree is Apache-2.0 with no GPL-encumbered files,
  before bundling the toolchain. (Belt-and-braces; Apache-2.0 is the stated
  licence.)
- [ ] **Emu198x + AmiBlitz CLI build** — confirm the scriptable compile runs
  cleanly headless in the Code198x Docker build.

## Relationship to existing docs

- [platforms/commodore-amiga/basic-skeleton.md](../platforms/commodore-amiga/basic-skeleton.md)
  — the working skeleton this record formalises. Its two-track structure stands;
  its **fixed-count framing ("512 units / 8 games × 64") is superseded** by the
  illustrative-counts position. Its commercial-proof examples were **checked
  against primary sources 2026-06-02 and corrected**: *Guardian* was
  misattributed to AMOS — it is an Acid Software title coded by Mark Sibly (the
  creator of Blitz BASIC) in Blitz BASIC + 68k asm, so it moved to the Blitz
  column as a showcase; *Ultimate Soccer Manager* had no AMOS source and was
  removed. The verified AMOS examples are now *Scorched Tanks* (AMOS Pro),
  *Flight of the Amazon Queen*, *Valhalla: Lord of Infinity*, and *Jetstrike*
  (the last two spot-checked 2026-06-02 — Jetstrike confirmed by a first-person
  developer interview, "primarily AMOS" with 68k extensions; only *Lord of
  Infinity* of the Valhalla trilogy is source-confirmed, so the series claim was
  narrowed to that title). The Blitz examples (*Worms*, *Skidmarks*, *Super
  Skidmarks*, *Guardian*) are verified.
- [platforms/commodore-amiga/amiga-common-errors.md](../platforms/commodore-amiga/amiga-common-errors.md)
  and the AMOS command reference under `language/` — existing AMOS-track
  material; consistent with this record.

## Drift triggers

- **Treating AMOS and Blitz as interchangeable** — teaching the same techniques
  in both. The fork only earns its cost if each track climaxes on what the other
  cannot do. Restating the same lesson in two BASICs is the failure mode.
- **Sequencing AMOS first** because it is the easier language. The decision is
  Blitz-first on *track-readiness* grounds; reversing it re-opens the licensing
  and tokeniser snags before the pipeline is proven.
- **Bundling AMOS binaries / ADF disks into the curriculum or CI image** without
  closing the redistribution open action. "It's abandonware, everyone shares it"
  is exactly the reasoning this record rejects — tolerated ≠ licensed.
- **Teaching on AMOS 1.3, original 1993 Blitz BASIC 2 binaries, or AOZ Studio**
  instead of AMOS Professional / AmiBlitz3. Each is the wrong artefact for a
  different reason (weaker licence / no licence / not period-authentic).
- **Reaching for AmiBlitz3-only language features** in curriculum code. Write
  within the period-authentic BB2 feature set; AmiBlitz3 supports it as a
  superset.
- **Reintroducing fixed unit counts** ("8 games × 64 units") as targets. Counts
  are illustrative; budget is per-technique and the quality bar.
- **Framing the built-in AmigaBASIC as the BASIC track.** It was weak, dropped,
  and Kickstart/AGA-incompatible. The authentic Amiga BASIC story is AMOS and
  Blitz.

## Status

Active. Captured 2026-06-02. Formalises the two-track structure already sketched
in [platforms/commodore-amiga/basic-skeleton.md](../platforms/commodore-amiga/basic-skeleton.md);
adds the verified licensing position, the Blitz-first sequencing, the
abstraction-ladder framing, and the open actions that gate the AMOS track.

Descends from [curriculum-structure.md](curriculum-structure.md),
[modules-not-games.md](modules-not-games.md),
[inspired-by-not-clones-naming.md](inspired-by-not-clones-naming.md),
[real-retro-games.md](real-retro-games.md),
[examples-as-files-and-screenshots.md](examples-as-files-and-screenshots.md).
Precedent for a BASIC-track decision: [spectrum-basic-32-games.md](spectrum-basic-32-games.md).

## Log

| Date | Event |
|------|-------|
| 2026-06-02 | Captured. Two-track fork formalised; AMOS-vs-Blitz licensing verified against primary sources; Blitz-first sequencing set; AMOS open actions enumerated. |
| 2026-06-02 | Skeleton's commercial-proof attributions checked. *Guardian* (Acid/Sibly, Blitz) was miscredited to AMOS → moved to Blitz column; *Ultimate Soccer Manager* unsourced → removed. AMOS examples corrected to Scorched Tanks, Flight of the Amazon Queen, Valhalla, Jetstrike. |
| 2026-06-02 | AMOS-redistribution outreach to François Lionet. GitHub contact email bounced (stale); sent instead via LinkedIn DM (existing connection). Awaiting reply; build-from-source held as fallback. |
| 2026-06-09 | **AMOS shipped first** — complete Meet AMOS primer (17 units) built and live, via type-into-editor (no tokeniser). Sequencing reality recorded; see "Update 2026-06-09". |
| 2026-06-09 | **Pipeline reality found.** emu198x-amiga is single-floppy (no HDF) → AmiBlitz3 (35 MB HD / 8–12 MB / 68020 / WB2.1+ / no CLI) can't run on it; demoted to licensing-clean shipping target gated on Emu198x HD work. |
| 2026-06-09 | **BB2 short-term path spiked.** Real BB2 v1.60 AF single-disk self-boots into Ted on a500-plus/KS2.04; ASCII source types via `type_string` (syntax-highlighted, plain-text). |
| 2026-06-09 | **BB2 pipeline PROVEN end-to-end.** Compile-and-run trigger is the keyboard command key **`right-Amiga+X`** (Compiler→COMPILE/RUN); the loop boot→type→⌘X→capture produces the program's output. emu198x #63 (right-button menus) fixed same day but proved unnecessary. Blitz track unblocked. |
