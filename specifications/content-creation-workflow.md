# Content Creation Workflow

**Version:** 3.0 · **Updated:** 2026-06-10
**Purpose:** End-to-end guide for creating a curriculum unit, from planning to publication.
**Scope:** All platforms and tracks.

> **v3.0 rewrite.** Reconciled to the current content model: **modules, not games**
> ([modules-not-games.md](../decisions/modules-not-games.md)), **state lives in the catalogue**
> ([state-lives-in-catalogues.md](../decisions/state-lives-in-catalogues.md)), MDX in **content
> collections** ([content-model.md](content-model.md)), and the **Docker / Emu198x** build-and-capture
> pipeline. The old `src/pages/game-NN-…` routing, hand-edited `index.astro` navigation, and
> native-emulator commands are gone.

---

## Philosophy

**Three core quality criteria** — a unit must strongly meet at least 2 of 3:

1. **It works fast** — visible/audible result quickly; something impressive or useful.
2. **It's real** — the hardware is visible (chip names, registers, addresses); honest about limits.
3. **It's clear** — one focused concept; builds logically on earlier units; invites experimentation.

**What we are:** game-first pedagogy (concepts through building games, never isolated theory),
hardware intimacy (direct register/chip access, no abstraction layers), original creation
(inspired-by, never reproductions), mastery through repetition, self-directed learning.

**What we are not:** nostalgia tourism · modern engines (Unity/Unreal/Godot — zero tolerance) ·
reproductions ("pixel-perfect Donkey Kong" — respect copyright) · shallow surveys · abstract theory.

**Unit archetypes** (design tools, not labels): Discovery (standard teaching, most common) ·
Challenge (problem using recent skills) · Synthesis (combine concepts into a complete program) ·
Deep Dive (hardware internals) · Tutorial (guided construction) · Showcase (inspirational).

---

## The five phases

Phases 1–5 apply to every unit; the **module-completion** pass runs when a module's last unit ships.

### Phase 1 — Planning

**Verify the unit against the lineup before writing.**

1. **Find the canonical lineup** — the track's catalogue
   (`website/src/content/modules/<platform>/<track>.yaml`) is the source of truth for *what exists
   and in what order*; the per-track **decision record** under `docs/decisions/` (e.g.
   `c64-assembly-lineup.md`) carries the *why* — the ladder, the per-game technique budget, the rung
   each module teaches. Per-game design detail is in the **brief** at
   `platforms/<system>/games/<slug>/brief.md`.
2. **Check the technique budget** — each game introduces **one** new major technique (two at most),
   and revisits the rest (per the track's decision record). If your unit pushes a game over budget,
   the fix is a split or an earlier unit — not a denser unit.
3. **Check prerequisites** — is every skill this unit leans on taught in an earlier unit (this game
   or a previous one)? If not: teach the prerequisite earlier, or simplify the technique.
4. **Note required Vault entries** — hardware chips and essential context the unit depends on (the
   must-create set); track nice-to-haves (games, people, companies) for later.

**Hard stops:** no catalogue/record entry for the module → stop (the lineup is decided in a decision
record, not invented in a unit). Prerequisites missing → stop (reorder or simplify).

### Phase 2 — Creation

**Unit MDX** — `website/src/content/curriculum/<platform>/<track>/<module-slug>/unit-NN.mdx`
(content collection; **no `game-NN-` prefix** — module slugs are bare, order comes from the catalogue
array). Module index page is `index.mdx`; the setup page is `getting-started.mdx`.

Frontmatter is **minimal** — `title`, `description`, `game` (the module's game number; 0 for
teaching/interval), `unit`, `tags`. Everything else (`layout`, `platform`, `track`, `totalUnits`,
prev/next, module slug, `system`) is **derived from the entry path** in `[...slug].astro` — never in
frontmatter ([unit.md](unit.md), [content-model.md](content-model.md)).

**Code samples** — `code-samples/<platform>/<track>/<module-slug>/unit-NN/<name>.<ext>`, embedded with
`CodeFromFile` (never inlined in MDX). Each sample must run standalone (all DATA, all setup). BASIC:
line numbers flush left, **no indentation**. Assembly: platform conventions; name chips in comments
(VIC-II, SID — not "the video chip"); comment *why*, not *what*.

**Standalone demos** (when a technique is complex, reused, or a Pattern Library candidate) —
`code-samples/<platform>/<track>/<module-slug>/techniques/<name>.<ext>`, 50–150 lines, one technique,
a header comment linking the teaching unit. Not everything needs one. Tag pattern candidates as you
write; extract Pattern Library entries *after* the module completes.

**Writing** — conversational but precise; British English (colour, learnt) except **"program"** for
code; name the engineers when it illuminates; no hype, no formulaic openings, no apologising for the
hardware. Vale enforces the house style ([writing-voice.md](writing-voice.md)).

### Phase 3 — Validation

**Build** with the platform's Docker image (per the root `CLAUDE.md` quick reference) — the toolchain
is migrating from these per-platform images to **Asm198x**, per-platform, never big-bang:

| Platform | Image | Assembler | Output |
|---|---|---|---|
| C64 | `ghcr.io/code198x/commodore-64` | `acme -f cbm` | `.prg` |
| ZX Spectrum | `ghcr.io/code198x/sinclair-zx-spectrum` | `pasmonext --sna` | `.sna` |
| Amiga | `ghcr.io/code198x/commodore-amiga` | `vasmm68k_mot -Fhunkexe` | executable |
| NES | `ghcr.io/code198x/nintendo-nes` | `ca65` + `ld65` | `.nes` |

**Capture** is moving from the per-platform screenshot scripts to **Emu198x** (`code-samples/_capture/`),
per-platform as each is proven. Capture a screenshot at the impressive moment (enough boot/wait frames
first); audio for sound units.

**Verify every screenshot with the Read tool** — describe what's on screen; any `?SYNTAX ERROR` /
`?ILLEGAL QUANTITY ERROR` / blank screen is an automatic failure. For audio, listen: correct
frequency, no clipping, right waveform, PAL/NTSC noted. **Never claim "verified" without Read-tool
evidence.** If anything's wrong: fix → rebuild → recapture → re-verify.

Then apply the three quality criteria (2/3 strongly met) and a British-English pass (Vale).

### Phase 4 — Integration

- **Vault entries** (content collection) for hardware chips and essential context the unit depends on;
  track nice-to-haves for later. Categories per [vault.md](vault.md).
- **Cross-reference** related units and add a "From the Vault" section linking the entries.
- **Pattern candidates** — tag now; extract after the module completes.

You do **not** hand-edit navigation. Prev/next, unit counts, the module's place in the track, and its
status are **all derived** from the content collection + the catalogue. To make a unit live, set its
`available: true` in the module's `units.yaml` and ensure the MDX exists — never by editing an
`index.astro` units array (that model is gone).

### Phase 5 — Publication

Set the unit/module status in the **catalogue** (`modules/<platform>/<track>.yaml` `status:` and the
module's `units.yaml` `available:`), not in prose — state lives in the catalogue. Then commit.

**Conventional commits**, track-scoped:

```
feat(<platform>-<track>): <effect, not implementation>

- what the unit teaches / the new technique
- the hardware touched

<why, if not obvious>
```

Scope is the **track** (`spectrum-assembly`, `c64-basic`, `amiga-blitz`, `nes-assembly`), not a
`game-NN`. Title describes the *effect*. Commit the MDX, the code samples, the images/media, and any
Vault entries together. Commit/push only when the work is verified and you've been asked to.

**Seven repos** — `website`, `code-samples`, `docs`, and the four `*-dev` toolchain repos. Always
`cd` into the specific sub-repo in the same shell call as the commit (cwd resets to the container; a
bare commit can sweep up the wrong tree). See [seven-repos.md](../decisions/seven-repos.md).

### Module completion

When a module's last unit ships: extract Pattern Library entries from the standalone demos
([pattern-library.md](pattern-library.md)); audit that every Vault/pattern cross-reference resolves;
confirm the built artefact runs start-to-finish; check British English throughout. The unit count and
"complete" status are read from the catalogue — there is no landing-page unit array to update.

---

## Definition of Done

A unit ships only when it passes the project's **9-item Definition of Done** bar (the quality gate the
launch spec holds everything to). In short: curriculum-aligned, builds, runs without error, screenshot
Read-verified, audio verified (sound units), 2/3 quality criteria, required Vault entries exist,
British English, cross-references resolve. Count is cut before the bar, never the reverse.

---

## Common pitfalls

- **Skipping lineup alignment** — "I know what this should teach" → it doesn't match the decided
  ladder. Read the catalogue + decision record first.
- **Claiming validation without evidence** — no Read-tool screenshot check, no audio listen, no exit
  code. Evidence before assertions, always.
- **Editing navigation by hand** — prev/next/status are derived; hand-edits drift. Use the catalogue.
- **Prose status claims** — "Volume 1 is complete" in a doc is not state; the catalogue is.
- **Indentation in BASIC** — line numbers flush left, no exceptions (the build will reject it).
- **C64 BASIC reserved/2-char variables** — never `ST`/`TI`/`TI$`; only the first two characters are
  significant, so `f1x`/`f1y` both collapse to `f1`. Use distinct 2-char names (`fx`/`fy`, `sc`, `hp`).
- **Sprite MSB unhandled** — X > 255 wraps; always handle `$D010`.
- **Screenshot timing** — captured pre-boot (blank) or after the program ends; capture the impressive
  moment, verify with Read.
- **Audio assumed correct** — verify frequency (PAL vs NTSC differs), listen for clipping.
- **Pattern Library forgotten** — tag during creation, extract after module completion.

---

## Quick reference

**Paths**
- Unit MDX — `website/src/content/curriculum/<platform>/<track>/<module-slug>/unit-NN.mdx`
- Module index / setup — `…/<module-slug>/index.mdx` · `…/<track>/getting-started.mdx`
- Catalogue (state) — `website/src/content/modules/<platform>/<track>.yaml`; unit detail — `units/…`
- Code samples — `code-samples/<platform>/<track>/<module-slug>/unit-NN/`
- Images — `website/public/images/<platform>/<track>/<module-slug>/unit-NN/`

**Hard stops:** no lineup entry · over the technique budget without a split · missing prerequisites ·
build fails · screenshot shows an error/blank · audio wrong · fewer than 2/3 quality criteria.

**Canonical references:** [modules-not-games.md](../decisions/modules-not-games.md) ·
[state-lives-in-catalogues.md](../decisions/state-lives-in-catalogues.md) ·
[content-model.md](content-model.md) · [unit.md](unit.md) · [brief.md](brief.md) ·
[pattern-library.md](pattern-library.md) · [vault.md](vault.md) ·
[writing-voice.md](writing-voice.md) · the per-track lineup record under `decisions/`.

---

**Remember:** quality over speed; the catalogue is the state; evidence before assertions, always.
