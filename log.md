# Wiki Log

---

## 2026-06-02 — Stale engine-first Shadowkeep docs rewritten / archived

**Type:** docs hygiene (anti-drift)

The Shadowkeep design/engineering docs predated the 2026-05-29 re-pace and would actively mislead (they spec pre-shifted/masked sprites, a Y-sort object system, and decoupled tile-map collision — none of which the cell-based Place uses). Rewritten or relocated so they can't steer future work wrong:

- **brief.md → v3.0.** Rewritten for the cell-based Place + module model: pass 1 = the Place; engine is Gloaming's (carried, not rebuilt); **bitmap dithering** named the signature technique; the three engine commitments flagged as *relocated*; the 64-unit/four-arc scope replaced with a module trajectory (counts illustrative); build status (Units 1–12) added. Genre / ancestors / atmosphere / audio / anti-goals / vault carried forward, reworded off the old engine.
- **Archived to `superseded/`** (with a README): engineering-plan, sprite-shifter, object-system, tile-map, memory-budget — frozen as-was; the relocated techniques map to Smooth Motion / Overlap / Greypeak, to be lifted when those games are built.
- **beeper-spec.md** kept and repointed — it feeds sub-arc 1.4; audio survives the re-pace untouched.
- **tracker/revamp.md** Shadowkeep section *body* rewritten (module trajectory, relocated-engine note, fixed pointers), not just banner-flagged.

Decision records left as-is (they correctly carry amendment banners — history matters there). Residual, deliberately separate: a track-wide reconciliation (the "powers-of-2 locked decision", the pending ~1,000-edit modules-not-games migration).

---

## 2026-06-02 — Shadowkeep reset to the cell-based Place; Units 1–12 authored

**Type:** content (curriculum authoring) + records reconciliation

Reset Shadowkeep from the old engine-first slice to the cell-based **Place** and authored it end-to-end through sub-arcs 1.1–1.3 (12 units), then consolidated.

- **Records first.** Reconciled the Shadowkeep records to the module model + no-fixed-counts: amended `decisions/shadowkeep-32-unit-commitment.md` and `shadowkeep-four-arc-framing.md` (counts illustrative; **pass 1 = the Place**; Arc 2 + Arcs 3–4 become later *revisit modules*); per-unit-plan gained a Module-shape section; catalogue entry tagged `game: shadowkeep, pass: 1`. Consistent with the 2026-06-01 modules-not-games keystone (whose full ~1,000-edit migration is still pending Steve's go).
- **Reset.** Old engine-first Units 1–8 retired (preserved in git); module reset to a coming-soon Place (Gloaming-shaped yaml, Place index); orphaned old assets cleaned.
- **Authored 1.1–1.3 (Units 1–12).** Hooded Figure (identity) · The First Hall (**bitmap dithering** for textured/shaded stone — Steve's idea, the chief addition beyond the outline) · A Place to Move (Gloaming's movement/collision; save/restore over texture) · The Keep's Hand (room-as-data: palette + ASCII map) · The Room Graph · Through the Doorway (edge-matched re-entry) · The Hero Remembers (per-room RAM state + chalk persistence) · Three Rooms (designed keep) · Light and Shadow (dither-density lighting from a torch) · Furnishings (decoration; blocking-by-brightness) · Mood through Constraint (per-room falloff) · A Keep with Character (multi-torch nearest-light). Each verified on Emu198x; build 1742→1754 pages.
- **Consolidation pass.** QA: all `CodeFromFile` refs resolve, all screenshots present, British English clean, unit numbers match, build green. Fixed unit `game:` frontmatter 3→2 (the index−1 convention; index stays 3). Updated this log, the revamp tracker (current-state banner over the superseded engine-first detail), and the per-unit plan's build status.

**Remaining for the Place:** sub-arc 1.4 *The Keep Has a Voice* (audio — SFX driver, the gold goal, a beeper theme, the title→explore→win→title loop, real hardware). The 8-unit October-cut floor (1.1–1.2) is met.

**Deferred:** bump Emu198x video-capture quality (mp4 averages fine dithering to flat colour), then recapture the dither-heavy units (2, 3, 9–12) with motion video.

---

## 2026-06-01 — Keystone: "Modules, not games" (design accepted, migration pending)

**Type:** curriculum architecture decision (binding) — model change

[`modules-not-games.md`](decisions/modules-not-games.md). The curriculum's unit of sequencing is the **module**, not the game. A *game* is a buildable artefact a module *teaches*; **one game can be taught by several modules** (revisits — the spiral model at game scale: build Gloaming, later revisit it to make movement glide). Module kinds: `game` / `teaching` (the Primer) / `interval`. Slugs are bare identities (`gloaming`, `shadowkeep`, `meet-the-machine`) with **no number** — order lives in the catalogue, so inserting a module renames nothing.

Arrived at via two reframes in one session: "games are really just modules" → "this opens revisiting a game a second time." Drafting it confirmed it dissolves a stack of tensions: the original **Gloaming-vs-Shadowkeep `game-01` collision** (now just two slugs), the Primer's "game 0" hack (it's the first module), the catalogue-numbering cascade (order is data), intervals (a module kind), the stale-16-vs-gentle-ramp lineup (reorder, don't rename), Shadowkeep's arcs (later revisit modules), and number-in-slug fragility (gone).

**Migration is planned but NOT executed** — ~1,000 edits across three repos + published URLs (7 catalogue YAMLs, 78 units YAMLs, 324 `game:` fields, 338 slug-ref files, ~93 dirs × 3 mirrors, helpers/layouts/routing, + redirects for shipped URLs). Sequenced + build-verified in the record; awaiting Steve's go. Then: wire the Primer as module 1, reconcile the lineup to gentle-ramp order, add revisit modules. Records to amend after: curriculum-structure, between-game-intervals (promote intervals to a module kind), gentle-ramp, CLAUDE.md, unit spec.

---

## 2026-06-01 — Primer expanded to 15 beats (arithmetic, bit-logic, 16-bit added on merit)

**Type:** content (curriculum authoring) — extends the 12-beat Primer below

Reviewing "are there other primer-appropriate topics we need?" surfaced one clear gap and two defensible ones — all added on merit (explicitly **not** to hit a round count; the no-fixed-unit-counts rule was named and held against the powers-of-2 pull):
- **12 Adding and Taking Away** — `inc`/`dec`/`add`/`sub` + the carry flag. The clear gap: a BASIC-literate learner couldn't do `x = x + 1`. Pays off the carry deferred at Test, Then Jump. (cyan border, verified.)
- **13 Working With Bits** — `and`/`or`/`xor` to clear/set/flip. The Primer could *test* a bit (Beat 8) but not change one; Gloaming ORs in BRIGHT. (magenta border, verified.)
- **14 Bigger Than a Byte** — 16-bit register pairs + `add hl, de` to step by N. Gloaming Unit 1 already uses `add hl, de` for wall sides. (red column, verified.)

Placed as a "round-out-your-fluency-before-the-game" block (12–14) so only the capstone renumbered (**The Machine Trusts You** 12 → **15**); all deferrals held at this position (carry was already deferred; `bit` introduced at input; 16-bit follows the pointer beat). **The memory-map** topic was judged interval material, *not* a beat — the one that would have reached 16 for neatness; declined. Final Primer length **15**, emergent not targeted.

Recovery note: authoring the new Beat 12 in `unit-12/` clobbered the capstone's MDX + screenshot there (its source survived); moved `no-safety-net.asm` → `unit-15`, rebuilt, re-captured, rewrote the capstone MDX at unit-15; fixed Beat 11's forward-ref.

---

## 2026-06-01 — Primer fully authored (12 beats, to Definition of Done)

**Type:** content (curriculum authoring) — the assembly track's opening artefact

The **Primer** ("Meet the Machine") is drafted end-to-end — all 12 units assemble on pasmonext → `primer.sna`, run on Emu198x, and have verified screenshots; magazine prose; `CodeFromFile` listings + Try-this samples; one-concept-per-unit throughout. Working-tree drafts (uncommitted) at `website/.../assembly/primer/unit-01..12.mdx`, `code-samples/.../primer/unit-01..12/`, `website/public/images/.../primer/unit-01..12/`.

**Final beat list (machine model → control flow → mindset):** 1 Assemble and Run · 2 LD Is Not LET · 3 Everything Is a Number · 4 A Street of Numbered Boxes · 5 The Screen Is Memory · 6 Colour Is a Separate Map · 7 Test, Then Jump · 8 The Machine Can Hear You · 9 **A Finger on the Boxes** (pointer — split out during authoring, Steve approved) · 10 Counting Toward Zero · 11 Call, Return, and a Stack You Can See · 12 The Machine Trusts You.

**Design calls made while authoring:**
- **`HL`/pointer split.** The outline had loops at beat 9 using `ld hl`; per one-concept, pointer was split into its own beat (9) ahead of DJNZ (10). Outline bannered, not renumbered.
- **`HL` deferred from beat 5** (screen showpiece uses only beat 4's direct store) → paid off in beat 9.
- **Chip-vs-tool seam at beat 7:** label case-sensitivity + leading-dot local labels named as *pasmonext's* rules, not the Z80's (Steve's framing). Verified empirically: mnemonics/registers case-insensitive, labels case-sensitive.
- **Two cliff-hangers planted and deferred:** screen-thirds layout (beat 5 → an interval, per [between-game-intervals.md](decisions/between-game-intervals.md)); full keyboard matrix (beat 8 → the tiny game).
- **Verified-not-assumed facts:** `ld a, 300` wraps silently to 44 (no error); the four literal notations emit identical `$41`; `out` only takes `A`.
- **Interactive capture technique** discovered for beat 8 (hold a key headlessly via a raw `input` script step) — saved to behavioural memory; Gloaming movement units reuse it.

**Still open:** wiring the Primer into the content collection is blocked on the deferred catalogue-numbering decision (frontmatter `game: 0` is a provisional placeholder; not yet routed). The Primer needs a real name (working slug "primer"). The two cliff-hangers await the tiny game / first interval.

---

## 2026-06-01 — In-curriculum WASM playground (door held open)

**Type:** exploratory design note

Captured [`in-curriculum-wasm-playground.md`](decisions/in-curriculum-wasm-playground.md) (status: held open, not binding). An in-page edit→assemble→run loop (WASM Asm198x + Emu198x core embedded in a unit) is a **post-launch multiplier, not an October gate** — launch is content-gated, Fuse + downloadable `.sna` is the shippable runtime, ~4-month runway must protect content. Key point recorded: **content authored now is forward-compatible** — every `CodeFromFile`-referenced `.asm` becomes a `CodePlayground` exhibit with no rewrite; screenshots stay as preview/fallback/OG. This is *why* the "code in files, never inline" rule is also future-proofing. Sequencing when the time comes: Asm198x→WASM first (cheap, clean single-binary Rust), then the Emu198x core (already headless/GUI-decoupled, proven by the capture pipeline), then swap the component. Distinct from Forge198x (standalone IDE, umbrella, deferred) but shares the WASM-tooling dependency.

---

## 2026-06-01 — Primer Beats 1–2 authored; between-game intervals (door held open)

**Type:** content (curriculum authoring) + exploratory design note

**Authored** the first two Primer units end-to-end to the Definition of Done (working-tree drafts): `primer/unit-01.mdx` "Assemble and Run" (the build-run loop; `OUT`/border) and `primer/unit-02.mdx` "LD Is Not LET" (registers; `LD` between registers, shown via a round-trip A→B→A on the border). Both assemble on pasmonext → `primer.sna` and have verified Emu198x screenshots (red border u1, cyan u2). The Primer's lesson surface is the *register/memory view*; where a beat's idea is invisible on screen, the border is reused as a visible proxy.

**Verified, not assumed (two prose-facing facts):** pasmonext mnemonics/registers are case-**insensitive** but labels are case-**sensitive** (so u1's case note is scoped to instruction names; the label gotcha is deferred to Beat 7 where learners first write their own label). `ld a, 300` assembles **silently and wraps** to the low 8 bits (44) — it does *not* error; reframed as a "no safety net" Try-this in u2.

**`game: 0`** is a provisional frontmatter placeholder for the unnumbered Primer, pending the deferred catalogue-numbering decision; not yet wired into the content collection.

**Exploratory note added** — [`between-game-intervals.md`](decisions/between-game-intervals.md) (status: door held open, not binding). Recurring *intervals* between games that step out of application into the academic layer (the Primer is the prototype). A third axis alongside spiral (deepen a technique in a richer game) and deprecation pairs (replace a naive technique): intervals consolidate *knowledge* outside the per-game technique budget, and are the natural place to pay off deliberately-planted cliff-hangers. Open: cadence, core-vs-optional, numbering, first interval. Live constraint: don't foreclose it (keep numbering able to slot unnumbered intervals; keep planting cliff-hangers).

**Files (uncommitted working-tree drafts):** `website/.../primer/unit-01.mdx`, `unit-02.mdx`; `code-samples/.../primer/unit-01/border.asm`, `unit-02/registers.asm` (+ `.sna`s); `website/public/images/.../primer/unit-0{1,2}/screenshot.png`; `docs/decisions/between-game-intervals.md`; `docs/specifications/unit.md` (one-concept principle); this entry.

---

## 2026-06-01 — Assembly gradualism: unit-level discipline + deprecation-pairs (binding)

**Type:** curriculum design decision (binding) — pedagogy, extends the gentle ramp

**Trigger:** Authoring Gloaming Unit 1 (the tiny first game) prompted the question of how to evolve the assembly curriculum so concepts are introduced gradually rather than all at once. Surveying the decisions folder first showed most of the proposed principles were **already binding** — `spiral-and-incremental.md` ("one new capability per unit") and `incremental-code-samples.md` (≤5–8-line diff; "too much new code is the signal to split"). The assembly cliff (Shadowkeep units of 230/396/515 lines) was therefore a **compliance gap**, not a missing principle: the diff discipline was written BASIC-first (line numbers, 10-step renumbering) and never enforced on assembly.

**Decision (filed by responsibility, not folded into one doc):**
- **Amended `incremental-code-samples.md`** with an *Assembly tracks* section: the diff rule restated for a track with no line numbers (measure in *instructions*; comments + `equ` vocabulary excluded; a coherent data block = one change like a BASIC `DATA` statement; BASIC rules 2/3/7 don't apply — labels are position-independent). Added the assembly compliance debt to *Implications* and three assembly drift triggers.
- **New `deprecation-pairs.md`**: formalises the *teach-the-naive-version-first, motivate-the-upgrade-by-its-felt-limit* pedagogy (+ name-the-assumption-out-loud, vocabulary-before-syntax). Distinguished from spiral: spiral **deepens** a technique that stays; a deprecation pair **replaces** a deliberately-naive one. Gloaming is the root of the track's deprecation tree.
- **Pointer added to `spectrum-assembly-gentle-ramp.md`**: per-game budget there; per-unit discipline in incremental-code-samples; naive-first pedagogy in deprecation-pairs.

**Downstream (not done here):** propagate the *unit = one concept* rule into `docs/specifications/unit.md`; the gentle-ramp Shadowkeep re-pace must bring its 230/396/515-line units into compliance; reconcile the stale 16-game assembly catalogue to the gentle-ramp lineup (without pre-stubbing empty routed games).

**Files (uncommitted working-tree drafts, left for review):** `docs/decisions/incremental-code-samples.md`, `docs/decisions/deprecation-pairs.md` (new), `docs/decisions/spectrum-assembly-gentle-ramp.md`, this entry.

---

## 2026-05-29 — Spectrum Assembly: gentle complexity ramp + Shadowkeep re-scope

**Type:** curriculum design decision (binding) — track-structure re-plan

**Trigger:** Review of the Spectrum Assembly track's difficulty ramp. Shadowkeep (game 1) was carrying two of the curriculum's hardest loads at once — assembly-from-zero *and* the whole track's commercial-engine Trunk (pre-shifted sprites, masking, Y-sort, tile-map collision), which `spectrum-assembly-track.md` had it "introduce" for every later game to inherit. The shipped 8-unit slice shows the cliff (asm lines: u1–3 ≈50 → u4 230 → u5 396 → u6 515). Re-pacing within 32 units fixes the slope but not the ceiling.

**Decision:** New governing decision [`spectrum-assembly-gentle-ramp.md`](decisions/spectrum-assembly-gentle-ramp.md). One rule generates it: **≤1–2 major new techniques per game; split or insert where the lineup over-packs.** Consequences: a **Primer** ("Meet the Machine"; programming-literacy floor, BASIC-first *recommended* not gated) and a **tiny first game** now precede Shadowkeep; **Shadowkeep is re-scoped** to the cell-based atmospheric flick-adventure its own *Atmosphere* headline already names (commercial bar via art / lighting / audio — the Manic Miner / Atic Atac route); the **advanced rendering Trunk relocates** to Greypeak + two small inserts (Smooth Motion → Overlap), each motivated by a felt limitation. Ordering is **hybrid** (early sequence monotonic; later volumes assume competence). This is the same move the genre-honesty redistribution already made for combat / parser / etc., applied to technique instead of genre.

**October reframe:** launch artefact shifts from "Shadowkeep Arcs 1–2, 32 units" to "the gentle assembly opening — Primer + complete tiny game + start of re-scoped Shadowkeep". More achievable; hardest engineering off the critical path; the shipped cell-snapped units largely survive.

**Records amended** (AMENDED banners): `spectrum-assembly-track.md`, `shadowkeep-32-unit-commitment.md`, `shadowkeep-four-arc-framing.md`, `spectrum-assembly-per-game-scope.md`, `october-2026-launch-spec.md`; `per-unit-plan.md` bannered superseded-pending-re-pace.

**Downstream (not done here):** full unit-by-unit re-pace of Shadowkeep to cell-based; authoring of the Primer + tiny-game units; real names for the two inserts + the tiny game; `Code198x/CLAUDE.md`'s launch-context line still reads "Arcs 1+2 at 32 units / 8 of 32 shipped" and should be updated to the opening framing.

Commits: docs `86a8406`, `33d11a0`, `5e6b606`, `2adc78b`, `736d05b`, `cc80ae7`, + this entry.

---

## 2026-05-29 — Quiz Master (game 10) review: two crashes + title-screen bug

**Type:** bug fix (curriculum code) + prose sync + screenshots

**Correction to the entry below:** the dead-`9000` cleanup was deferred on the premise of "no crash risk." That premise was **wrong**. The survey only checked for `GO SUB 9000` *callers*; it missed **fall-through**. In Quiz Master, units 01–09 run off the end of their logic (no `STOP`/`GO TO`) straight into the dead `9000`, which references undefined `y`/`a$` → `Variable not found, 9000:1` after the player finishes. So "dead" ≠ "harmless." Removed `9000`/`9010` from all 10 Quiz Master units now (crash fix, not deferred tidying); units end cleanly with the `0 OK` report. **Any future fall-through check must look at each unit's last logic line, not just `GO SUB` references.**

**Second crash (units 02–03):** `Nonsense in BASIC, 190:1`. The question `READ q$,…` started at the first DATA line, which held the numeric answer key (line 550) — added prematurely, before unit-04 introduces the array code that consumes it. Reading numbers into string variables crashes. Fix (user-chosen): remove line 550 from units 01–03; the answer key debuts in unit-04 where it is read into the array and explained. Dropped unit-01's "mysterious line 550" foreshadow accordingly.

**Title-screen bug (unit-10):** "Press any key to start" used `INK 0` on the black `PAPER 0` title → invisible; and the trophy `PLOT/DRAW` sat physically before the prompt so it only rendered by execution-order luck. Reordered, gave the prompt white `INK 7` and the trophy gold `INK 6`, moved the prompt clear of the trophy.

**Prose/structure:** unit-10 falsely declared "Volume 1 complete / Ten games"; the catalogue puts Quiz Master as game 2 of Volume 2 (Cipher opened it). Replaced with a Locksmith pointer; relocated the cumulative-skills recap to Touchdown (game 8, the true end of Volume 1), reframed to the eight First Programs games. Corrected unit-10 line count (70→53) and unit-01 framing (the question is hardcoded, not from DATA).

Commits: code-samples `9a04582`, website `52b7ec2e`.

---

## 2026-05-29 — Tracked: curriculum-wide dead `9000` subroutine cleanup

**Type:** deferred hygiene task (not yet started)

**Trigger:** During the Cipher (game 9) review, the template centring subroutine `9000 PRINT AT y, (32 - LEN a$) / 2; BRIGHT 1; a$ / 9010 RETURN` was found defined but never called in units 01–07, then wired up (live) in units 08–09. A survey across the Spectrum BASIC track showed this is a track-wide pattern, not a Cipher quirk.

**Survey results (dead = defined-but-never-called units / live = called units):**

| Game | dead | live |
|------|------|------|
| 06 bright-spark | 9 | 1 |
| 09 cipher | 7 | 2 |
| 10 quiz-master | 10 | 0 (never called anywhere) |
| 11 locksmith | 6 | 3 |
| 13 three-in-a-row | 7 | 4 |

(03 oracle-stone, 05 dice-roller, 07 hi-lo, 08 touchdown, 12 sonar, 14 the-caverns, 15 yearfall: 0 dead — `9000` called in every unit that defines it.)

**Decision:** Do NOT clean piecemeal (would create cross-game inconsistency and violates the stay-on-target rule mid-review). Instead, do a deliberate pass *after* the game-by-game review finishes. The pass should: (1) remove `9000`/`9010` from units that never call them; (2) keep them where live; (3) introduce the subroutine in prose at the unit where it first becomes live — currently no unit's prose explains it. `game-10-quiz-master` is the priority case: `9000` is dead in all 10 units, so it can be removed outright there.

**Notes:** No crash risk in any of these (the dead copies are unreachable — guess/main loops exit via unconditional `GO TO`, not fall-through). Distinct from the earlier fall-through crashes in bright-spark/hi-lo/touchdown, which were already fixed with `STOP` guards / removal where a *conditional* exit fell into `9000`.

---

## 2026-05-19 — Project README updated with domain framing

**Type:** public-facing README update

**Files edited:** `docs/README.md`

**Changes:**

1. **Opening "What Is This Project?" section** rewritten with the domain framing surfaced in the methodology survey: *"retro raster-era hardware-craft game development through the canon."* Added inspired-by-not-clones language. Removed generic "retro game development" framing in favour of the more-precise claim.
2. **New "What this is, and what it isn't" section** added — names the bounded domain (8-16-bit, raster-display, hardware-constrained, ~1977-1995) and what's outside (modern engine-mediated, mobile, 3D-first, vector-display). Names the methodology generalisation finding (11+ retro platforms generalise cleanly; 2 strain; 2 break honestly outside the domain).
3. **"How The Curriculum Works" section** updated — unit counts changed from "8-32 units each" to "8-80+ units each, depending on canonical depth" (honest to per-game-scope decision). Added "inspired-by-not-clones" bullet with canon references (Atic Atac, Manic Miner, Elite, Lords of Midnight).
4. **Assembly Curricula Platform Status table** — Spectrum row updated to v0.3 figures (44 entries / 6 volumes / ~2,396 units; Shadowkeep 64 units across 4 arcs; October ships Arcs 1-2 = 32 units). C64 / NES / Amiga rows note "pre-methodology" status (concept locked, not yet at v0.3-methodology bar).
5. **BASIC Gateway Platform Status table** — Spectrum BASIC row updated to v6.4 (32 games / 4 volumes; V1 ships October 2026). Note about 11-game rename.
6. **Future Platforms section** — cross-references the methodology-generalisation-survey for pressure-test findings.

**Notes:** The user explicitly said "this is EXACTLY what I had in mind" when the *"retro raster-era hardware-craft game development through the canon"* framing emerged from the stress-test. README update lands that framing as the project's public-facing claim. Bounded-domain framing replaces vaguer "retro game development" framing across the doc.

---

## 2026-05-19 — Methodology pushed to breaking point (stress-test pass)

**Type:** methodology stress-test extension

**File edited:** `knowledge/curriculum/methodology-generalisation-survey.md` — appended "Pushing further" section

**Notes:** User asked whether the methodology *ever* reaches a problem. Pushed test further beyond the comfortable 11-system population to find real breakage points. Five more systems tested:

- **Atari 2600 (1977)** — first genuine strain. Trunk Layer 1 (Framebuffer) doesn't translate — no framebuffer, race-the-beam architecture. Trunk needs significant reframing. Methodology *survives* with rework.
- **Vectrex (1982)** — **first system where Trunk Layers 1-2 *cannot* meaningfully translate.** Vector display, no framebuffer, no sprite concept; colour from physical plastic overlays. Cross-cutting axes survive but Trunk + Branches need replacement. *Pattern reaches a real boundary here.*
- **PlayStation / N64 (1994-1996)** — second real strain. 3D-first hardware *promotes Branch E to Trunk*. Trunk Layer 1 (Framebuffer) becomes secondary. Methodology survives but Trunk fundamentally reframes for the 3D era.
- **Modern mobile / Steam-Itch indie (2007+)** — **methodology leaves its domain entirely.** Engine-mediated development; hardware abstraction; engagement-loop / monetisation / certification concerns replace hardware-craft. Trunk + Branches + Engineering Practices + Layer model all become irrelevant. Naming convention and per-game design-concept axis survive at the conceptual level.

**Bounded domain identified:** Raster-display, hardware-constrained, framebuffer-based, 8-16-bit-era (1977-1995) home computers and consoles. ~30-40 platforms fit cleanly. Methodology *strains* at edges (2600 earliest, PSX/N64 latest). *Breaks* on Vectrex (graphics paradigm — vector not raster) and modern mobile/indie (development paradigm — engine-mediated not metal).

**Verdict: methodology is a genuine framework with a defensible domain, not a universal claim.** A real bounded methodology is a stronger result than "it works everywhere." Code198x's methodology can honestly describe itself as "retro raster-era hardware-craft game development through the canon" — that's a real, bounded, and defensible scope.

---

## 2026-05-19 — Methodology generalisation survey (8 additional systems)

**Type:** methodology pressure-test (no skeleton, no commit)

**File created:** `knowledge/curriculum/methodology-generalisation-survey.md`

**Files edited:** `knowledge/index.md` — new Curriculum entry

**Notes:** Following the C64 / NES / Amiga lightweight skeletons, user asked whether the Spectrum methodology generalises to *more* systems. Pressure-tested across: Apple II, Atari 8-bit, Game Boy / GBC, SNES, Sega Master System, Sega Mega Drive, BBC Micro, Dragon 32/64.

**Result: methodology generalises across all 11 systems surveyed.** No major framework cracks. What varies per platform:

- **Branch G (audio hardware)** is platform-specific by design — Apple speaker, Atari POKEY, GB 4-channel, SNES SPC700+samples, SMS PSG, Mega Drive YM2612 FM, BBC SN76489, Dragon speaker
- **Engineering Practices** is CPU-specific — Z80 / 6502 / 65C816 / 68000 / 6809 / Z80-derivative idioms
- **Trunk Layer 2 (The Sprite)** varies by hardware affordance — software-sprite era only on Spectrum (and BBC arguably); hardware sprites from the start on most others
- **Canon balance** varies — Apple II is RPG-heavy, NES is platformer-heavy, SNES is JRPG-heavy, Amiga is sim-heavy; methodology accommodates
- **Unique design vocabulary per platform** earns its own branch or cross-cutting note — Apple II hi-res NTSC artifacting, Atari ANTIC display lists, SNES Mode 7, BBC mode-switching, Mega Drive FM, Game Boy portability

**Closest CPU-parallel to Spectrum:** Game Boy (Z80-derivative LR35902) and SMS (literal Z80). Spectrum's Engineering Practices content transfers ~85% to Game Boy and ~95%+ to SMS.

**Closest structural parallel to Spectrum:** BBC Micro — also has both a strong BASIC tradition AND a strong Assembly tradition. Elite (the canonical) originated on BBC. The dual-track structure (Spectrum BASIC + Spectrum Assembly) maps cleanly to BBC.

**Most-different platform surveyed:** Dragon 32/64 — MC6809 is the first non-Z80/non-6502 CPU the methodology has encountered. Methodology fits but canon is thin (smaller scope per game count).

This survey does NOT commit to expanding the Code198x platform list (stays at 4: C64, Spectrum, Amiga, NES). It does NOT design skeletons for any of the 8 surveyed systems. It is purely a pressure-test of the framework's generality — methodological confidence, not roadmap.

---

## 2026-05-19 — Cross-platform lightweight skeletons (C64 / NES / Amiga)

**Type:** lightweight curriculum skeletons (no per-game commit)

**Files created:**
- `knowledge/curriculum/c64-track-skeleton.md`
- `knowledge/curriculum/nes-track-skeleton.md`
- `knowledge/curriculum/amiga-track-skeleton.md`

**Files edited:**
- `knowledge/index.md` — three new Curriculum entries

**Notes:** User asked when to produce skeleton specs for the other systems. Honest answer: the Spectrum methodology is build-unvalidated, applying full structure to three more platforms before validation is premature, and the project's own October-2026-launch-spec defers C64/NES/Amiga whole. **Lightweight skeleton** is the middle path: North Star + volume themes + ~16 candidate games per platform, with no commitments to per-game scope, naming, or tech-tree.

Cross-platform methodology generalisation findings:

- **C64** — methodology generalises cleanly. Branch G is SID-specific (replaces AY+128K), Engineering Practices are 6502-specific. No major framework gaps.
- **NES** — methodology mostly generalises but Trunk Layers need rework (no software-sprite era), Branch B (Platformer) is much heavier than Spectrum, Branch D less prominent. APU replaces beeper/AY/SID as Branch G content.
- **Amiga** — methodology generalises **least cleanly**. 68000 + custom chips + sampled audio = fundamentally different from 8-bit. Trunk Layers may need full reframing. Engineering Practices most different. AGA could be a native L+1 layer (parallel to Spectrum's 128K).

The skeletons are stamped "post-October" and "no-commit" — they exist to **reserve canonical references**, **surface cross-platform pattern opportunities**, and **sanity-check methodology generality** without locking the curriculum design until Spectrum's first build round validates the framework.

Full structural treatment for any other platform deferred until at least Shadowkeep Arc 1 ships (~Aug 2026), realistically mid-2027 onward.

---

## 2026-05-19 — Spectrum Assembly per-game scope audit captured

**Type:** new decision (per-game scope estimates)

**Files created:**
- `knowledge/decisions/spectrum-assembly-per-game-scope.md` — first-draft unit-count estimates for all 44 entries in the Spectrum Assembly track. Total: 2,396 units. Per-volume / per-tier breakdowns; cut hierarchy refined with scope as input; multi-decade shipping timeline.

**Files edited:**
- `knowledge/decisions/spectrum-assembly-track.md` — added "Extended by" section linking the new per-game-scope decision
- `knowledge/index.md` — added per-game-scope decision entry

**Notes:** Per-game scope was the highest-leverage open item from the v0.3 pending list — it unlocks per-game spec drafts (43 docs still to write) by setting honest budgets first. Three findings worth surfacing in the decision doc:

1. **Three Tier 1 games are bigger than v0.2 implied.** V1.6 Embergate (80u), V1.7 The Lantern Path (80u), V3.20 Edge of Iron (64u) all inherited primary teaching from Shadowkeep's Arc 3-4 redistribution (combat / classes / dialogue / branching narrative).
2. **Six games at ≥80 units (heavy hitters):** Coldstar (Elite, 96), The Marchlands (Next tilemap RPG, 88), Whitewinter, Embergate, The Lantern Path, Coreworks (all 80). Three from redistribution; three canonically large traditions.
3. **Eight productions at ≤32 units** — Jetpac/Voidlift was small, 3D Monster Maze/Long Passage was small, demoscene productions are focused. Honest to canon; not inflated for uniformity.

Total ~2,396 units is ~67% of memory's 3,584-units-per-platform direction-of-travel — healthy. Spectrum Assembly is honest at this scope.

**Flagged for future review:** #8 The Last Banner (Lothlorien wargame, 48u) — canon-thin relative to Smith/Ultimate/Singleton/Crow lineage. Possible Tier 3 demotion candidate if timeline tightens.

**Numbers are first-draft floors, not schedule commitments.** Multi-decade horizon explicit. Cut hierarchy refined: V6 cuts first (276u), then V5 (104u), then late additions (196u), then Tier 2 within volumes by inverse-canonical-weight. Tier 1 games 1-16 are the floor.

---

## 2026-05-19 — October-relevant + Maintenance batch

**Type:** comprehensive doc updates across multiple files

**October-relevant items completed:**

1. **BASIC curriculum spec v6.4 rename application** — `docs/curriculum/basic/sinclair-zx-spectrum/sinclair-zx-spectrum-basic-curriculum.md`:
   - Headline concepts table (slots 3, 9, 11-15, 18, 20-22, 25-32) updated with v6.4 names
   - Embedded concepts table (V1-V2-V3-V4 entries) updated with v6.4 names
   - V4 Pt 1/Pt 2 names applied (Rooftops, Stonefall, Dorin, Thornwood for Pt 1; Skyhold, Deepworks, Dungeons of Dorin, Thornwood Manor for Pt 2)
2. **MDX slot-3 rename check** — no in-progress slot-3 content exists (the built directories are at v5/v6.1 slot positions, not v6.3/v6.4). Nothing to rename.
3. **Read-alongside + modern-equivalent lines per Shadowkeep unit** — `knowledge/curriculum/shadowkeep-32-unit-plan.md`: all 32 units now carry 2 additional metadata lines citing a canonical Spectrum-era moment + a contemporary game using the same idea. ~64 new lines.

**Maintenance items completed:**

4. **V4 BASIC Pt 2 naming workshop** — pending from v6.3, applied 2026-05-19. Pattern: *Pt 1 shorter name, Pt 2 longer/heavier name*. Skyhold (V4.27), Deepworks (V4.28), Dungeons of Dorin (V4.31), Thornwood Manor (V4.32). V4 Pt 1 names also slightly adjusted (Rooftops, Stonefall, Dorin, Thornwood — shorter versions). All first-draft, needs-workshop. Applied to: `knowledge/curriculum/revamp.md`, `docs/curriculum/basic/sinclair-zx-spectrum/sinclair-zx-spectrum-basic-curriculum.md`, `~/.claude/projects/.../memory/spectrum-basic-games-progress.md`.
5. **Vault audit (2026-05-19)** — gaps appended to `knowledge/curriculum/lesson-references.md`. ~50 vault entries identified as missing for the curriculum's full citation coverage. Categorised by Tier 1 (modern equivalents in Shadowkeep — 5 entries, October-visible), Tier 2 (Assembly lineup canonical games + people + companies — ~35 entries), Tier 3 (BASIC cross-references — mostly already covered). None block October launch; Shadowkeep's primary per-unit references already exist in vault (Atic Atac, Knight Lore, Sabre Wulf, Manic Miner, JSW, Cybernoid, Hobbit). Modern-equivalent vault entries (Hyper Light Drifter, Stardew Valley, Death's Door, Disasterpeace) are October-visible but currently absent — recommended Tier 1 priority.
6. **BASIC games-progress memory full rewrite at v6.4 lineup** — `~/.claude/projects/.../memory/spectrum-basic-games-progress.md` body fully replaced. 32-game lineup with v6.4 names; V4 Pt 2 names applied; orphaned MDX list refreshed for v6.4.
7. **`wiki/`→`knowledge/` path correction** — `docs/CLAUDE.md` updated (root CLAUDE.md is a symlink so picks this up automatically). Four artefact descriptions updated from "Phase 1 / 16 games" framing to current "Arcs 1+2 / 8 games" + cross-references to current decision docs.

**Notes:** Closes the October-relevant + Maintenance items the user identified. Remaining open: per-game scope audit + per-game spec drafts + structural axes work (Engineering Practices matrix, Production Craft items, L+1 sequencing, L+4 specifics) + naming workshop iteration. Those are for separate conversations.

---

## 2026-05-19 — Quick-wins tidying batch (post-Shadowkeep-refinements)

**Type:** doc maintenance across multiple files

**Files edited:**
- `knowledge/decisions/spectrum-assembly-track.md` — Branch A description expanded to name the revised flick-adventure-honest content (items / world / persistence / secrets & lore / atmospheric cycles / multiple keeps / endings / completion) and explicitly exclude the redistributed RPG/parser techniques
- `docs/curriculum/basic/sinclair-zx-spectrum/sinclair-zx-spectrum-basic-curriculum.md` — title bumped to v6.4 DRAFT; warning section updated for v6.4 with the 11-rename list; new v6.4 DRAFT changelog entry added
- `~/.claude/projects/.../memory/spectrum-basic-games-progress.md` — banner added noting v6.3/v6.4 supersede the v6.2 tables below; rewrite pending
- `~/.claude/projects/.../memory/spectrum-assembly-v0.1-reframe.md` — `wiki/`→`knowledge/` path correction
- `~/.claude/projects/.../memory/spectrum-assembly-v0.2-reframe.md` — same path correction
- `~/.claude/projects/.../memory/spectrum-assembly-v0.3-reframe.md` — same path correction; weird relative path fixed to clean reference
- `knowledge/curriculum/revamp.md` — deadline section updated with Shadowkeep four-arc + Spectrum Assembly track structure + v6.4 references; all 11 BASIC renames applied to V1/V2/V3 lineup tables; new "Status 2026-05-19 (later same day)" entry summarising today's decisions

**Notes:** Tidying batch consolidating today's batch of decisions and revisions across documentation. No structural decisions — just propagating already-approved changes through the documents that need them.

Still pending after this batch: BASIC v6.4 names need application to the headline-concepts table in the curriculum spec doc; per-game spec sections in the spec doc still describe v6.2 (won't be touched until those sections are written); MDX rename for slot 3 (Magic 8-Ball → Oracle Stone) if any drafted content exists.

---

## 2026-05-19 — Shadowkeep 32-unit plan refinements applied (v0.1 audit changes)

**Type:** curriculum content (canonical doc refinement)

**Files edited:**
- `knowledge/curriculum/shadowkeep-32-unit-plan.md` — comprehensive refinement applying the v0.1 audit changes per `knowledge/decisions/shadowkeep-four-arc-framing.md`

**Changes applied:**
1. **Position in curriculum section** added at top — names Shadowkeep as Volume 1 Game 1, flick-adventure tradition, headline *Atmosphere (Sense of Place)*.
2. **Design-concept line added to every unit** (all 32) — names what the unit teaches at the design level, alongside the existing Contribution / Code primitive / Art deliverable lines. Satisfies DoD point 10.
3. **Six unit reframes** completed:
   - U14 (*A glimpse of gold*) — explicitly introduces SFX driver (was implicit later); pickup is its first use
   - U15 (*The composed theme*) — pure beeper composition focus; driver moved to U14
   - U18 (*Door creaks*) — per-object animation state machine as primary technique (was reinforcement-only)
   - U20 (*Floor and shadow*) — variety as mood palette; per-room palette table introduced
   - U24 (*A different threat*) — behaviour tables as primary technique (was loose "second NPC"); seeds V3 shooter AI
   - U28 (*The keep grows*) — room-graph data structure as primary technique; seeds V2.10 Hollowhalls and Shadowkeep Arc 3.2
4. **Embedded Design Concepts section** added (before Time budget) — Atmosphere through restraint / Authored level design / Animation budget / Identity through silhouette / Audio as place / Polish as discipline, with which units surface each.
5. **DoD extended** with point 10 — "Design concept made explicit in the prose."
6. **Post-October Arcs 3-4 outline** added (after DoD) — full sub-arc-level outline of revised flick-adventure-honest content per the four-arc-framing decision. Includes ship gates and an explicit "what Arcs 3-4 do NOT teach" section pointing redirected techniques to V1.4 / V1.6 / V1.7 / V3.17 / V3.20.

**Notes:** This is the October-relevant prose work for Shadowkeep. The 32-unit October budget is unchanged; what changed is *how each unit is described and what it makes explicit*. Per-unit MDX writing for Shadowkeep can now anchor to clear design concepts and the named embedded concepts.

Read-alongside and modern-equivalent lines per unit (audit point 3) are NOT yet applied — pending separate workshop session where vault entries can be reviewed for each unit's best cross-reference.

---

## 2026-05-19 — Shadowkeep Arc 3-4 genre-honesty revision

**Type:** decision revision (same-day)

**Files edited:**
- `knowledge/decisions/shadowkeep-four-arc-framing.md` — Arc 3.4 reframed from *A World That Listens* (menu dialogue + quest state) to *Secrets and Lore* (hidden rooms / lore fragments / active items / bestiary). Arc 4 reframed from *Heroes and Stories* (combat / classes / XP / branching narrative) to *The Greater World* (atmospheric cycles / multiple keeps / collection-based endings / completion). Added "Genre honesty" section noting the redistribution table.
- `~/.claude/projects/.../memory/spectrum-assembly-v0.3-reframe.md` — added "Genre-honesty revision" section
- `~/.claude/projects/.../memory/MEMORY.md` — Shadowkeep entry updated with the revision

**Notes:** Honest-question audit ("are there techniques we should push out of Shadowkeep?") identified that Arc 3.4 + Arc 4 in original drafts drifted Shadowkeep from flick-adventure tradition (Atic Atac / Knight Lore / Sabre Wulf / Pentagram / Underwurlde) into RPG/parser/shooter territory. 14+ techniques redistributed to their canonical-legend games:

- Combat state machine → V3.20 Edge of Iron + V1.6 Embergate
- Spell system, class data, XP/level, class-conditional, item-class binding → V1.6 Embergate
- Projectile in object list → V3.17 Hostraider
- Menu dialogue, quest state, multi-NPC dialogue, branching narrative, multiple endings (narrative), main-quest state machine → V1.7 The Lantern Path
- Location-graph data, Singleton-class day/night → V1.4 Whitewinter

Shadowkeep stays at 64 units total. Arc shapes revised in content, not count. Cross-game prerequisite seeding still works with cleaner primary ownership. October 2026 launch scope unchanged (Arcs 1-2 untouched).

---

## 2026-05-19 — Four decisions captured from Spectrum Assembly + BASIC reframe brainstorm

**Type:** decisions (four new + two extensions)

**Files created in `knowledge/decisions/`:**
- `inspired-by-not-clones-naming.md` — naming convention: curriculum games are inspired by canon, not clones; 10-principle convention
- `spectrum-assembly-track.md` — 44-entry track structure across 6 volumes; layer model L0/L+1/L+3/L+4a/L+4b; three-axis design pattern; tech-tree with branches A-G; three cross-cutting axes
- `shadowkeep-four-arc-framing.md` — extends 32-unit commitment with Arcs 3-4 post-October (Beyond the Walls / Heroes and Stories); per-unit refinements to Arcs 1-2; October scope unchanged
- `spectrum-basic-v6.4-renames.md` — 11 BASIC games renamed under inspired-by-not-clones (Cut A — all 11, not just active trademarks)

**Files edited:**
- `knowledge/decisions/spectrum-basic-32-games.md` — title bumped to v6.4; lineup updated with 11 v6.4 names; cross-reference to v6.4-renames doc
- `knowledge/decisions/shadowkeep-32-unit-commitment.md` — added "Extended by" section pointing to shadowkeep-four-arc-framing; log row added
- `knowledge/index.md` — five new Decision entries
- `~/.claude/projects/.../memory/spectrum-basic-v6.4-reframe.md` — fixed slot 8 Touchdown reference (game name stays Touchdown; Descent is the player-facing concept)
- `~/.claude/projects/.../memory/MEMORY.md` — V1 ship line corrected (slot 8 = Touchdown, not Descent)

**Notes:** Brainstorm output captured in memory as v0.1 / v0.2 / v0.3 (Spectrum Assembly) and v6.4 (Spectrum BASIC). Four decisions reflect approved-as-drafted proposals from `knowledge/proposals/` (now emptied). October 2026 launch scope (Shadowkeep 32 units; Volume 1 = 8 games) unchanged by any of these decisions — all additions and extensions are post-October work, with the exception of per-unit prose refinements to Shadowkeep Arcs 1-2 that fit within existing 32-unit budget.

Per-game spec drafts (for the 43 non-Shadowkeep Assembly games) and per-game scope audit are the natural next steps. Volume 1 BASIC games with v6.4 names (Banner, Lucky Number, Oracle Stone, Reflex, Dice Roller, Bright Spark, Hi-Lo, Touchdown) ship for October.

---

## 2026-05-14 — Unit 3 working plan captured for the next session

**Type:** planning artifact
**Pages created:** `knowledge/curriculum/shadowkeep-unit-3-plan.md`
**Pages edited:** `knowledge/index.md` (added the plan to the Curriculum section)

**Notes:** Unit 3 is the most ambitious unit in Phase 1 — it introduces bitmap memory (with the Spectrum's three-thirds quirk), 8×8 pixel art design (UDG-style stone-block texture for the walls, hooded-thief sprite for the hero), the bitmap+attribute composition model, and the `player_under` cell-preservation pattern that Unit 4 will lean on for movement. Authoring Unit 3 properly is a session of focused work, and the user prefers to start a fresh session for it without re-explaining the context.

The captured plan is self-contained:
- Story arc and working title (*The Hero Arrives*)
- Continuity hooks back to Units 1 and 2 (start from Unit 2's `04-the-great-hall.asm` as the base)
- Four stages with their new ideas and acceptance criteria
- New concepts list (bitmap memory, three-thirds, 8×8 pixel design, tiling, sprite-as-bitmap, player_under)
- Seven diagrams to author
- Visual artefacts to produce (4 .asm files, 4 screenshots, MDX of ~500-600 lines)
- Acceptance criteria matching Units 1 and 2's bar
- Forward hook to Unit 4 (*Stride*) — the `player_under` byte becomes load-bearing
- References to brief, spec, design doc, pattern siblings (units 1 and 2 MDX), and the binding decisions

Any session starting cold from `knowledge/index.md` will see the Unit 3 plan and can execute against it without re-derivation.

---

## 2026-05-14 — Phase 1 Unit 2 reauthored as "The Great Hall Rises"

**Type:** curriculum content (significant rewrite to Unit 1's bar)

**Files created:**
- `code-samples/sinclair-zx-spectrum/game-01-shadowkeep/unit-02/01-one-row.asm` — Stage 1: BORDER+LDIR setup, DJNZ to draw one 22-cell wall row
- `code-samples/.../unit-02/02-the-grid.asm` — Stage 2: nested DJNZ to fill 22×16 solid block with WALL, introduces push/pop and row-advance arithmetic
- `code-samples/.../unit-02/03-the-room.asm` — Stage 3: data-driven nested DJNZ reading from `room_data` table; uniform "walls + floor" room
- `code-samples/.../unit-02/04-the-great-hall.asm` — Stage 4: same drawing code, hand-designed great hall data with stepped altar and gold cascade
- `website/public/images/.../unit-02/01-one-row.png` through `04-the-great-hall.png` — four progressive screenshots

**Files edited:**
- `code-samples/.../unit-02/Makefile` — pattern-rule build for the four staged `.asm` files
- `website/src/content/curriculum/sinclair-zx-spectrum/assembly/game-01-shadowkeep/unit-02.mdx` — fully rewritten as four-stage walkthrough with diagrams; magazine voice

**Files removed:**
- `code-samples/.../unit-02/shadowkeep.asm`, `.tap`, `.sna` — single-file layout replaced by the four staged files

**Story arc:** "The Great Hall Rises." Unit 1 left the keep awake (BORDER + dark stone + three torches). Unit 2 builds the room atop it: one row of stone → solid 22×16 block (introducing nested DJNZ) → hollow walls + floor (introducing data-driven drawing) → the great hall with altar and gold (same code, different data).

**New concepts introduced in Unit 2:**
- `DJNZ target` — the Z80's tightest two-instruction loop (decrement B, jump if not zero)
- Nested DJNZ — outer/inner counter relationship, with `push bc`/`pop bc` preserving the outer count across the inner loop's clobber
- The stack — what `push`/`pop` actually do, SP, matched pairs
- 16-bit pointer arithmetic from 8-bit pieces — `LD A, E` / `ADD A, n` / `LD E, A` with `JR NC, skip` / `INC D` for carry into the high byte
- HL and DE as a read/write pointer pair — `LD A, (HL)` reads, `LD (DE), A` writes, `INC HL`/`INC DE` advance
- Data-driven rendering — drawing code that's room-agnostic, room identity in `room_data` table

**Diagrams in the MDX:**
- The 32×24 screen with the room's footprint at rows 2–17, cols 5–26; HUD strip above, atmospheric framing below
- Address formula re-applied: `$5800 + (2 × 32) + 5 = $5845`
- DJNZ semantics with worked iteration trace
- Push/pop visualisation with SP and BC state across the inner loop
- Row-advance arithmetic explaining the `32 - 22 = 10` skip
- Data-driven layout: how 352 bytes at `room_data` map to attribute memory

**Atmospheric continuity:** Unit 2 begins with the BORDER+LDIR setup from Unit 1's final stage, so the keep is dark from the first instruction. The room then *rises* against that dark stone — the screenshots show the room appearing in clear contrast against the keep's interior, not against BASIC's default canvas.

**Forward hook:** the unit's "What's next" section sets up Unit 3 (the hero + UDG textures for walls) — the keep is about to have a person in it, and the walls are about to look like actual stone rather than blue rectangles.

**Verified:** all four `.sna` files build via Docker pasmonext; all four screenshots captured via the SNA pipeline; the MDX references all assets correctly.

---

## 2026-05-14 — Phase 1 Unit 1 reauthored as "The Keep Wakes"

**Type:** curriculum content (significant expansion)

**Files created:**
- `code-samples/sinclair-zx-spectrum/game-01-shadowkeep/unit-01/01-the-dark.asm` — Stage 1: BORDER black + LDIR-fill the screen in dark stone
- `code-samples/.../unit-01/02-first-torch.asm` — Stage 2: one yellow cell at $5990
- `code-samples/.../unit-01/03-two-torches.asm` — Stage 3: read + OR + write the brighter neighbour at $5991
- `code-samples/.../unit-01/04-flickering.asm` — Stage 4: FLASH + BRIGHT + yellow at $598F
- `website/public/images/.../unit-01/01-the-dark.png` through `04-flickering.png` — four progressive screenshots
- `website/public/videos/.../unit-01/04-flickering.mp4` — 4-second autoplay video of Stage 4 showing the FLASH cycle in motion

**Files edited:**
- `code-samples/.../unit-01/Makefile` — pattern-rule build for the four staged `.asm` files
- `website/src/content/curriculum/sinclair-zx-spectrum/assembly/game-01-shadowkeep/unit-01.mdx` — fully rewritten as four-stage walkthrough with diagrams; embedded video at top and at Stage 4

**Files removed:**
- `code-samples/.../unit-01/shadowkeep.asm`, `.tap`, `.sna` — single-file layout replaced by the four staged files

**Story arc:** "The keep wakes." The reader steps into a dark keep, sets the BORDER black, washes the playable area in dark stone (LDIR cascade), lights the first torch (write), reads it back, brightens it (OR), places the brighter torch (write), and finally writes a third torch with the FLASH bit set — a flame struggling against the magic taint.

**New concepts introduced in Unit 1 (up from 6 in the original):**
- `OUT (port), A` — talking to hardware via I/O ports; BORDER colour via port `$FE`
- `LDIR` — block-fill / block-copy in one instruction; the cascade idiom (`DE = HL + 1`, seed at `HL`)
- 16-bit register-pair immediate loads (`LD HL, addr`, `LD DE, addr`, `LD BC, count`)
- FLASH attribute bit (bit 7) — the hardware twitching INK and PAPER twice a second

**Diagrams in the MDX:**
- Attribute memory layout (32×24 grid with address formula)
- Attribute byte bit decomposition (with four worked examples: `$08`, `$30`, `$70`, `$F0`)
- Port `$FE` write semantics (BORDER bits 0-2, speaker bit 4, MIC bit 3)
- LDIR cascade trace (step-by-step, showing the byte propagating from `$5800` forward)
- OR bit math (`$30 OR $40 = $70` shown in binary)
- Memory state after each stage (which addresses changed, which didn't)

**Atmospheric framing:** the unit is no longer "two yellow cells on a grey BASIC canvas" — it's a story about the keep's first lights kindling. Magazine voice. Every byte explicitly written by the reader, no hidden setup, every state traceable in the diagrams.

**Video:** the FLASH-bit lesson required moving video. Embedded MP4 (autoplay, loop, muted, playsinline) with the still PNG as poster fallback. Captured via `scripts/emu-video-spectrum.sh` against the Stage 4 `.sna`, 200 frames = ~4 seconds of native PAL = 8 FLASH cycles visible.

**Verified:** all four `.sna` files build via Docker pasmonext; all four screenshots captured via the SNA pipeline; the MP4 plays via ffmpeg / browsers; the MDX references all assets correctly.

---

## 2026-05-14 — Orphaned non-Spectrum capture skills deleted

**Type:** cleanup
**Deleted (6 skill directories in `.claude/skills/`):**
- `screenshot-c64/SKILL.md`
- `video-c64/SKILL.md`
- `screenshot-amiga/SKILL.md`
- `video-amiga/SKILL.md`
- `screenshot-nes/SKILL.md`
- `video-nes/SKILL.md`

**Notes:** Follow-up to the legacy capture-script cleanup. These skills referenced MCP servers (`mcp__emu-c64__*`, `mcp__emu-amiga__*`, `mcp__emu-nes__*`) that no longer exist in `.mcp.json`, and the underlying binaries (`emu198x-c64`, `emu198x-amiga`, `emu198x-nes`) don't have `--mcp` support yet. The skills were non-functional in two layers.

Surviving capture skills: `screenshot-spectrum/SKILL.md` and `video-spectrum/SKILL.md` — both reference `mcp__emu-spectrum__*` and align with the single MCP server still registered.

When C64 / NES / Amiga curricula become active post-October and Emu198x adds `--mcp` support for those binaries, fresh skills can be created from the Spectrum pattern.

---

## 2026-05-14 — Legacy capture-script cleanup across all four platforms

**Type:** cleanup

**Deleted (directories in 4 separate dev repos):**
- `commodore-64-dev/scripts/` (c64-screenshot.sh, c64-video.sh, inputs/*)
- `sinclair-zx-spectrum-dev/scripts/` (spectrum-screenshot.sh, spectrum-video.sh, inputs/*)
- `commodore-amiga-dev/scripts/` (amiga-screenshot.sh, amiga-video.sh, inputs/*)
- `nintendo-entertainment-system-dev/scripts/` (nes-screenshot.sh, nes-video.sh, inputs/*)

These were the pre-Emu198x generation: xdotool / X-display / Docker-VICE driven, predating the unified Emu198x scripting model. Nothing modern referenced them.

**Deleted (broken non-Spectrum scripts in `scripts/`):**
- `scripts/emu-screenshot-c64.sh`
- `scripts/emu-screenshot-amiga.sh`
- `scripts/emu-screenshot-nes.sh`
- `scripts/emu-video-c64.sh`
- `scripts/emu-video-amiga.sh`
- `scripts/emu-video-nes.sh`

These called binaries with the old `emu-c64` / `emu-amiga` / `emu-nes` naming that no longer exists (current binaries are `emu198x-{platform}`). When the C64 / NES / Amiga curricula become active post-October, fresh scripts will be written from the Spectrum pattern.

**Fixed:**
- `scripts/emu-screenshot-spectrum.sh` — was broken per its own TODO (targeted a `--model` flag never implemented). Rewritten to mirror `emu-video-spectrum.sh` / `emu-audio-spectrum.sh`: `.sna` input, `load_snapshot` + `run_frames` + `save_screenshot`. Smoke-tested on Unit 1 — produces a valid PNG.

**Updated:**
- `code-samples/scripts/mcp-capture-spectrum-screenshot.sh` — switched from `.tap` + autoload + tape-stop wait to `.sna` + load_snapshot. JSON-RPC sequence dropped from 4 tool calls (load_media / autoload_tape / wait_for_query_bool / run_frames-100) to 2 (load_snapshot / run_frames-10).
- `.mcp.json` — was registering four MCP servers (`emu-c64`, `emu-spectrum`, `emu-nes`, `emu-amiga`) pointing at binaries that don't exist. Three of them were doubly broken: even with corrected paths, only `emu198x-spectrum` currently supports `--mcp` — verified by trying `--mcp --help` on each. Now contains a single `emu-spectrum` entry with the correct path. The other three platforms' MCP integration is upstream work in Emu198x.

**Total impact:** ~25 items removed, 2 scripts rewritten/updated, 1 config file rationalised.

**Flagged for next decision (not in this pass):**

Six skills now reference MCP servers that no longer exist in `.mcp.json`:
- `.claude/skills/screenshot-c64/SKILL.md` (`mcp__emu-c64__*`)
- `.claude/skills/video-c64/SKILL.md`
- `.claude/skills/screenshot-amiga/SKILL.md` (`mcp__emu-amiga__*`)
- `.claude/skills/video-amiga/SKILL.md`
- `.claude/skills/screenshot-nes/SKILL.md` (`mcp__emu-nes__*`)
- `.claude/skills/video-nes/SKILL.md`

These skills weren't functional before today either (the underlying binaries lacked `--mcp`), but now they're explicitly orphaned at the `.mcp.json` layer. Options: (a) delete them and recreate fresh when each platform's curriculum becomes active, (b) leave them as-is documenting the intended future shape, or (c) add status banners marking them as non-functional pending upstream Emu198x work. User call when ready.

---

## 2026-05-14 — Video + audio scripts updated to SNA; media-capture-pipeline page rewritten

**Type:** tooling + doc reconciliation
**Files edited:**
- `scripts/emu-video-spectrum.sh` (input switched from `.tap` + autoload-tape to `.sna` via `load_snapshot`; `--frames` and new `--settle` options; doc header rewritten)
- `knowledge/infrastructure/screenshot-pipeline.md` → renamed to `media-capture-pipeline.md` (the page now covers screenshot, video, *and* audio); content fully rewritten to reflect the SNA-based Spectrum pipeline and to flag the legacy-script status of the other three platforms
- `knowledge/index.md` (index entry updated for the renamed page)

**Files created:**
- `scripts/emu-audio-spectrum.sh` (new — WAV capture via `save_audio_capture`; mirrors the video script's interface with `--frames` + `--settle`; no ffmpeg dependency)

**Smoke-tested:**
- Audio script run on Unit 1's `.sna` produced a valid RIFF/WAV/16-bit PCM/mono/44.1 kHz file. Silent (Unit 1 just halts; no audio yet) but the pipeline functions.

**Why this matters:** Emu198x's `start_video_recording`, `stop_video_recording`, and `save_audio_capture` script steps were already exposed but the Code198x wrappers still used the old tape-based input. With the SNA-load capability from this morning's commit `ff02827`, all three media-capture flows (screenshot, video, audio) now share the same fast, tape-loader-free input path. The pipeline is uniform across mediums for the first time.

**Cleanups identified but not done (flagged):**
- Two legacy generations of capture scripts exist: `scripts/emu-*.sh` (modern, this work's target) and `{platform}-dev/scripts/{platform}-{screenshot,video}.sh` (xdotool/X-display era, pre-headless-Emu198x). The legacy scripts will be retired as each platform's curriculum reaches active work.
- The `code-samples/scripts/capture-spectrum-screenshot.sh` higher-level per-unit wrapper exists alongside the lower-level `scripts/emu-screenshot-spectrum.sh`. Both are useful at different layers; documented in the new page.
- The `.claude/skills/{screenshot,video}-spectrum/SKILL.md` skills drive the same underlying Emu198x capability via MCP rather than shell. Convergence on one driver may be worth post-October.

---

## 2026-05-14 — Screenshot capture pipeline switched to SNA load

**Type:** tooling
**Files edited:**
- `code-samples/scripts/capture-spectrum-screenshot.sh` (script JSON body switched from `load_media`/`autoload_tape`/`wait_for_query_bool` to a single `load_snapshot` step; input changed from `.tap` to `.sna`; header docs rewritten)
- `website/src/content/curriculum/sinclair-zx-spectrum/assembly/game-01-shadowkeep/unit-01.mdx` (one phrase updated — removed "with whatever the tape loader left at the top" reference; the new screenshot is a clean BASIC canvas with no tape-loader header)
- `website/public/images/sinclair-zx-spectrum/game-01-shadowkeep/unit-01/screenshot.png` (recaptured under the new pipeline)

**Background:** Emu198x commit `ff02827` ("LoadSnapshot: route .sna / .z80 / .zip through portable parsers") landed today, making `ScriptStep::LoadSnapshot` accept portable snapshot formats in addition to the runtime's own postcard format. Local `emu198x-spectrum` rebuilt at `target/release` from that commit.

**What this changes for Code198x:**

- Screenshot capture no longer needs `.tap` + autoload-tape + wait-for-tape-stop (~2000-frame budget per shot). The new pipeline is `load_snapshot` + 10 frames + `save_screenshot` — orders of magnitude faster.
- `Bytes: <name>` tape-loader header disappears from every screenshot — what readers see is now the actual end state of the unit's code, not the loader's residue. Pedagogically cleaner.
- `.tap` remains in the Makefile because it's still the canonical format for real-hardware testing (Spectrum Next loads from `.tap` / `.tzx`). Screenshot pipeline now uses `.sna`; real-hardware loading uses `.tap`. Both build from the same `.asm` via pasmonext.

**Verified:** Unit 1 recaptured. Clean grey-white canvas, two yellow cells dead centre with the BRIGHT differential visible between them. Matches the (lightly updated) MDX description.

**Forward work:** when authoring Phase 1 Units 2–8, the new pipeline applies automatically — no per-unit changes needed.

---

## 2026-05-13 — Phase 1 Unit 1 expansion: first unit authored against v1 brief

**Type:** curriculum content
**Files edited:**
- `website/src/content/curriculum/sinclair-zx-spectrum/assembly/game-01-shadowkeep/unit-01.mdx` (expanded from 215 to ~280 lines)
- `code-samples/sinclair-zx-spectrum/game-01-shadowkeep/unit-01/shadowkeep.asm` (extended from 2 working instructions to 5)
- `code-samples/sinclair-zx-spectrum/game-01-shadowkeep/unit-01/shadowkeep.tap`, `shadowkeep.sna` (rebuilt)
- `website/public/images/sinclair-zx-spectrum/game-01-shadowkeep/unit-01/screenshot.png` (recaptured)
- `knowledge/curriculum/revamp.md` (Phase 1 Unit 1 marked complete in outstanding work)

**Title change:** "A Coloured Block" → "Foundation: A Coloured Block" (matches audit's *Foundation* lens while preserving the evocative original).

**What changed in the MDX:**

- Added **"The keep's vocabulary"** section — visual-discipline seed introducing the full cell-type table (floor, wall, doors, treasure, key, hazard, exit) before any code. Sets atmospheric and design context for the entire Phase 1, not just Unit 1's two cells.
- Added **"Reading is a question"** section — folds in the attribute-read content from the deleted old `unit-02.mdx`.
- Added **"AND and OR — bit by bit"** section — folds in the bit-manipulation content from old `unit-02.mdx`, refactored to introduce both operations together.
- Replaced **"Try this: two cells"** with **"Try this: build a wall"** — three blue cells in a row beneath the original two yellow ones, hinting at room construction (motivates Unit 2's `DJNZ` loops).
- Added **"Try this: move the read"** — demonstrates that read returns whatever's actually in memory, not what you wrote, by reading from an unwritten cell.
- Expanded **"What you'll learn"** from 6 items to 10 (added the read/OR/AND/vocabulary items).
- Expanded **"If it doesn't work"** to cover the new failure modes.
- Updated **"What's next"** to point to the new Unit 2 (*A beautiful room*) instead of the old Unit 2 (which has been folded into this unit).

**What changed in the ASM:**

- Added two new instruction blocks: `ld a, ($5990)` (read), `or $40` (modify), `ld ($5991), a` (write). Total working instructions: 5.
- Result: two yellow cells side by side at row 12 cols 16–17. The right one is BRIGHT.

**Multi-disciplinary check (against `BRIEF-SPECIFICATION.md` Sections 6–9):**

- **Code:** assembles cleanly via Docker pasmonext; runs on Spectrum 48K boot.
- **Visual:** the keep-vocabulary table in the MDX provides the visual seed for Phase 1. The screenshot shows two yellow cells with a visible brightness difference — small but the demonstration of "byte modification → visible state change" is present.
- **Audio:** n/a for Unit 1 (audio surfaces in Unit 7).
- **Level design:** the vocabulary table establishes the cell-type design that drives every subsequent unit's level work.
- **Polish:** prose at magazine voice; MDX flow and pacing tested by re-read; if-it-doesn't-work section comprehensive.

**Definition of Done (per `knowledge/curriculum/revamp.md`):**
- [x] MDX written, magazine voice, length appropriate
- [x] Code listing assembles cleanly (Docker pasmonext)
- [x] Code listing runs correctly on the emulator (verified via emu198x-spectrum script-mode capture)
- [ ] Code listing runs correctly on real hardware (Spectrum Next) — pending hardware-side verification
- [x] At least one screenshot captured and verified
- [x] All `<CodeFromFile>` snippets exist in code-samples and assemble
- [x] "Try this" experiments tested and produce the described result (the new ones — bit-flip, read-from-unwritten-cell, three-cell wall — match described outcomes)
- [x] "If it doesn't work" troubleshooting reflects actual failure modes
- [ ] All cross-references resolve — no vault/pattern-library cross-references yet in this unit (will be added during Phase 1 vault gap-fill)

**First brief-format-driven unit complete.** The 14-section brief and the Phase 1 audit translate cleanly into actual authoring; the multi-disciplinary lens (visual seed, polish prose) is a real shift from code-only teaching, and produces measurably richer content per unit.

---

## 2026-05-13 — Shadowkeep Phase 1 audit executed

**Type:** cleanup + structural rework
**Files deleted (30 items total):**

Shadowkeep unit MDX files (15):
- `website/src/content/curriculum/sinclair-zx-spectrum/assembly/game-01-shadowkeep/unit-{02..16}.mdx`

Shadowkeep code-samples directories (15):
- `code-samples/sinclair-zx-spectrum/game-01-shadowkeep/unit-{02..16}/`

**Pages edited:** `knowledge/curriculum/revamp.md` (outstanding-work checklist revised to reflect post-audit state — 8-unit Phase 1 structure replaces 16-unit list; surviving unit-01 noted as needs-expansion; new units 2–8 listed by title).

**Preserved:** `unit-01.mdx` and `code-samples/.../unit-01/` (the surviving 2026-05-06 rewrite).

**Notes:** Phase 1 audit per the v1 Shadowkeep brief. The 15 pre-revamp draft unit files (Units 2–16, all dated 2026-02-06) were authored under the code-led model and pre-date the multi-disciplinary commitment. Keeping them as apparently-current spec would have created exactly the confusion the user has been ruling out throughout today's work.

The audit produced an 8-unit Phase 1 structure against the v1 brief:

| # | New title | Old units absorbed | Discipline lens |
|---|---|---|---|
| 1 | Foundation | 1 + 2 | code, visual seed |
| 2 | A beautiful room | 3 + 8 | visual-led, framework |
| 3 | The hero | 5 | visual-led, sprite craft |
| 4 | Stride | 4 + 6 + 7 | code, input + physics |
| 5 | Two rooms | 9 | framework, spatial design |
| 6 | Pickup and goal | 11 + 15 (trimmed) | game state, level design |
| 7 | The beeper sings | 14 | audio-led |
| 8 | The keep stands | 16 | polish-led, integration |

Phase 2 (post-October) absorbs what Phase 1 dropped: full 9-room engine (old Unit 10), keys/locked-doors (old Unit 12), hazards (old Unit 13). The Phase 2 content will be authored fresh against the v1 brief, not built from the deleted pre-revamp drafts — though git preserves those drafts if Phase 2 authoring wants to glance at the old technical material.

**Pressure-test outcome:** the v1 brief's Section 11 (Phase trajectory) and the audit decisions are now aligned. Future authoring sessions for Phase 1 work from the brief directly; no pre-revamp draft content remains to bias the new work toward old framing.

**Git preserves:** all 30 deleted items recoverable via `git log --diff-filter=D --follow -- <path>`.

---

## 2026-05-13 — Shadowkeep v1 brief captured (first brief against BRIEF-SPECIFICATION.md)

**Type:** new artifact
**Pages created:** `docs/curriculum/assembly/sinclair-zx-spectrum/briefs/shadowkeep-brief.md` (and the new `briefs/` directory).

**Notes:** First game brief authored against `BRIEF-SPECIFICATION.md` v1.0. Covers all 14 required sections plus the optional Risks section.

Key commitments codified in the brief:

- **256 units across 17 phases.** Phase 1 = 8 units (October vertical slice), Phase 2 = 8 units (Arc 1 completion to small game), Phases 3–17 = 16 units each.
- **Period-faithful constraint position across all phases.** No modern-scene techniques planned — Shadowkeep demonstrates that real 1980s-period work reaches mid-tier full-price quality on its own merits.
- **Six-arc trajectory:** Arc 1 (small complete game, Phases 1–2), Arc 2 (animation and life, Phases 3–5), Arc 3 (scale and persistence, Phases 6–8), Arc 4 (narrative and polish, Phases 9–10), Arc 5 (128K and production, Phases 11–14), Arc 6 (compatibility and packaging, Phases 15–17).
- **17 × 5 = 85-cell multi-axis ship-test table** with per-phase pass criteria across code/visuals/audio/level/polish.
- **Pattern Library extractions inventoried** across the framework/rendering/input/physics/audio/ai categories.
- **Vault tie-in gaps surfaced** — Atic Atac, Sabre Wulf, Ultimate Play the Game, Knight Lore, Hewson Consultants, several hardware pages, AY-3-8912. Drives vault completeness work.
- **Risk register (optional section used)** — multi-room engine spike, beeper composition, hero cell-preservation edges, authoring-rate vs October deadline, hardware testing, acceleration assumption.

**Brief format pressure-test results:** the 14-section format worked cleanly throughout. Section 4 (Core experience) accommodated Shadowkeep's slow-paced exploration without strain (the original "core verb" framing wouldn't have). Sections 6–9 (visual/audio/level/polish) each produced substantive content that wasn't in the earlier 10-section draft. The multi-axis ship test table for 17 phases is large but readable.

**Forward work flagged by the brief:**

- Phase 1 audit — which 8 of the 16 existing Shadowkeep unit MDX files become the vertical slice.
- Vault gap-fill — entries flagged in Section 14 need verification or creation.
- Phases 2 → 3 → 4 multi-room engine prototyping (the design's biggest technical spike).
- Beeper title composition (per existing `shadowkeep-beeper-spec.md`).

---

## 2026-05-13 — BRIEF-SPECIFICATION.md v1.0 captured

**Type:** new spec document
**Pages created:** `docs/BRIEF-SPECIFICATION.md`

**Notes:** Formal specification for game design briefs. Codifies the 14-section format that emerged from today's strategic discussion and the pressure-test of the old 10-section format against Shadowkeep.

**Structural changes from the old 10-section format:**

- Section 4 renamed from "Core verb" to "Core experience." The original framing strained on Shadowkeep — slower-paced exploration didn't fit "every second the player does X." New section accepts either a tight gameplay verb or a description of the texture of engagement.
- Section 5 (Constraint envelope) becomes Constraint position. Three-tier taxonomy per `decisions/constraint-position.md`.
- Sections 6, 7, 8, 9 are new and first-class — Visual / Audio / Level / Polish direction. Required, per `decisions/real-retro-games.md`. Multi-disciplinary commitment now structural in the brief.
- Section 11 (Phase trajectory) revised — each phase declares techniques + revisits (spiral) + constraint position if varies + phase-end deliverable.
- Section 12 (Ship test) revised — multi-axis pass criteria per phase, not a single sentence.
- Optional Risks section noted; not required.

**Anchored in** all six substantive decisions captured today, plus pattern-library decision. Includes brief quality checklist for self-review before authoring begins.

**Forward work flagged by this spec:**
- v1 Shadowkeep launch brief against this format (next sensible task per the path).
- Shadowkeep Phase 1 audit (which 8 units of the existing 16-unit spine become the vertical slice) — informed by but not blocked on the brief.
- Brief format will likely iterate as it meets more games; v2 expected after 2–3 real briefs land.

---

## 2026-05-13 — Cross-platform v4.0 cleanup (orphan files, stale BASIC dirs, all-platform outlines)

**Type:** cleanup
**Files / directories deleted:**

C64 v4.0 outline files (4):
- `docs/curriculum/assembly/commodore-64/game-0{1..4}-full-game-outline-c64-{nova-storm,coldframe,warfront,sidereal}.md`

NES v4.0 outline files (4):
- `docs/curriculum/assembly/nintendo-nes/game-0{1..4}-full-game-outline-nes-{dash,wyrdstone,abyssal-gate,starweave}.md`

Amiga v4.0 outline files (4):
- `docs/curriculum/assembly/commodore-amiga/game-0{1..4}-full-game-outline-amiga-{exodus,duskfall,redline,horizons}.md`

Orphan Shadowkeep snippet files (3 + the empty parent):
- `code-samples/sinclair-zx-spectrum/game-01-shadowkeep/unit-01/snippets/0{1..3}-{border,one-cell,walls-and-floor}.asm`
- The now-empty `snippets/` directory.

Stale Spectrum BASIC game directories (9 each in website/src/content and code-samples — 18 dirs total):
- `game-02-bomb-defusal`, `game-03-colour-flood`, `game-05-word-scramble`, `game-07-treasure-hunt` (duplicate parallel dirs alongside their canonical wire-panic / bright-spark / letter-soup / tail-chase siblings)
- `game-09-word-worm`, `game-11-draughts`, `game-12-battleships`, `game-13-lattice`, `game-16-the-cursed-manor` (old non-canonical names explicitly flagged in `knowledge/curriculum/revamp.md`; canonical replacements brick-bash / tarmac / ink-spill / rooftops / thornwood-manor not yet built)

**Total deleted:** 12 outline files + 3 orphan snippets + 1 empty dir + 18 stale BASIC dirs = 34 items.

**Pages edited:** none in this pass (a previous log entry today recorded the Spectrum-curriculum-doc v5.0 update which already noted some of this).

**Notes:** Follow-up sweep after the user's "I don't want any confusion" prompt. Same logic as the Spectrum-outline kill: v4.0 outlines documented the previous 128/256/512/512 code-led plan at the wrong unit scale, and (for C64 Nova Storm and NES Dash) the wrong Game 1 designs (replaced by Cadence and Nightshade respectively per `decisions/commercial-bar-revamp.md`). The Amiga `game-01-full-game-outline-amiga-exodus.md` was the pre-redesign Exodus (Lemmings-flavoured); current Exodus is the Lost-Vikings-flavoured redesign.

The stale BASIC dirs had been flagged in `revamp.md` for months ("need replacing — directory rename + content replacement, not just MDX edits") but weren't being acted on. The 9 dirs holding ~80 stale MDX/BAS files each were a substantial future-confusion risk; killing them now means the 5 missing canonical games (brick-bash, tarmac, ink-spill, rooftops, thornwood-manor) get built fresh under the v5.0 bar rather than evolved from old-name predecessors.

**User-call deferred:** The 12 future-platform stub curriculum docs in `docs/curriculum/assembly/{acorn-archimedes,amstrad-cpc,atari-8-bit,atari-st,bbc-micro,game-boy,msx,sega-master-system,sega-mega-drive,snes,turbografx-16,vectrex}/` were considered for kill but left in place. They self-label as "Status: Future — Stub Entry" so don't actively contradict current scope, though they invite the drift trigger from `curriculum-structure.md`. User chose to keep them this pass.

Git history preserves all deleted content. Retrieval as before: `git log --diff-filter=D --follow -- <path>`.

---

## 2026-05-13 — Deleted v4.0 game outline files (drift-cleanup follow-up)

**Type:** cleanup
**Files deleted:**
- `docs/curriculum/assembly/sinclair-zx-spectrum/game-01-full-game-outline-zx-spectrum-gravelight.md`
- `docs/curriculum/assembly/sinclair-zx-spectrum/game-02-full-game-outline-zx-spectrum-ionfire.md`
- `docs/curriculum/assembly/sinclair-zx-spectrum/game-03-full-game-outline-zx-spectrum-grimstone.md`
- `docs/curriculum/assembly/sinclair-zx-spectrum/game-04-full-game-outline-zx-spectrum-dawnreach.md`

**Pages edited:** `docs/curriculum/assembly/sinclair-zx-spectrum/sinclair-zx-spectrum-curriculum.md` (v5.0 changelog entry amended to note the deletion).

**Notes:** Follow-up to the drift-cleanup pass earlier today. The four v4.0 game outline files were retained in v4.0 ("preserved... for reference" per the v4.0 changelog) but had become apparently-current spec by appearance, despite documenting the 128/256/512/512 code-led plan and (for `game-01`) the abandoned Gravelight Game 1 design. With no cross-references from other live documents, the files were unambiguous future-confusion risk rather than useful raw material — fresh briefs at 256 multi-disciplinary units will be written from the v5.0 curriculum doc + the seven captured decisions, not from these outlines.

Git history preserves the deleted content. Retrieval: `git log --diff-filter=D --follow -- <path>` finds the deletion commit; `git show <commit>^:<path>` reads the v4.0 content.

---

## 2026-05-13 — Drift cleanup against the seven new decisions

**Type:** reconciliation
**Pages edited:**
- `docs/curriculum/assembly/sinclair-zx-spectrum/sinclair-zx-spectrum-curriculum.md` (full rewrite to v5.0)
- `knowledge/curriculum/shadowkeep-phase-1-design.md` (status banner + framing updates: commercial reference, Arc 1 / Phase 1+2 split, vertical slice, phase plan)
- `knowledge/curriculum/revamp.md` (multiple targeted edits: at-a-glance status, hard-deadline scope, locked decisions bar + pattern, cut hierarchy, October scope item 1, Shadowkeep priority 1 header, phase plan table → arc structure, outstanding work spine reference, log entry)

**Notes:** Reconciliation pass following the seven decisions captured today. Resolved the persistent Gravelight/Shadowkeep naming drift in the formal curriculum spec, and aligned the live revamp tracker and the Shadowkeep Phase 1 design doc to the new structural framing (vertical slice / Arc 1 / 256-unit total / mid-tier full-price / spiral progression).

**Out of scope for this pass (known stale):**
- `website/src/content/curriculum/sinclair-zx-spectrum/assembly/game-01-shadowkeep/index.mdx` — visitor-facing copy still uses "1984 Ultimate-tier" framing; needs touch-up during the Phase 1 audit / vertical-slice rewrite, not during drift cleanup.
- The 16 existing unit MDX files — same audit will determine which survive, which are reworked, which are cut.
- Brief format itself — the 10-section format needs extending to 13–14 sections (visual/audio/level/polish direction as first-class fields); v1 Shadowkeep launch brief drafts against the new format.

---

## 2026-05-13 — Pattern Library flow and categorisation captured (seventh, sequence complete)

**Type:** decision
**Pages created:** `decisions/pattern-library.md`
**Pages edited:** `index.md`

**Notes:** Final decision in the sequence — lighter-touch than the others. Codifies the existing Pattern Library architecture and corrects two earlier framing errors that surfaced during the design discussion: **patterns are populated from curriculum** (not the reverse), and **technique-based categorisation** (ai/audio/framework/input/physics/rendering, plus language-specific where useful, plus cross-platform) rather than the gameplay/presentation/shell/production split I'd initially proposed.

Polish content (title screens, attract modes, options menus) decomposes into compositions of existing categories — not a separate library bucket. "Ship It"-type content is curriculum, and the patterns it surfaces go into the existing technique categories.

Sequence complete. Seven decisions captured today: `real-retro-games`, `october-2026-vertical-slice`, `phase-boundaries`, `constraint-position`, `spiral-and-incremental`, `curriculum-structure`, `pattern-library`. Forward work flagged in multiple decisions: curriculum-doc reconciliation (Gravelight/Shadowkeep drift, per-game unit count revision, Game 3 scope), brief format revision to 13–14 multi-disciplinary sections, Shadowkeep design-doc spiral-progression addition.

---

## 2026-05-13 — Curriculum structure locked (sixth of sequence)

**Type:** decision
**Pages created:** `decisions/curriculum-structure.md`
**Pages edited:** `index.md`

**Notes:** Sixth decision in the sequence — the structural commitment that operationalises the multi-disciplinary bar at curriculum scale. **4 platforms × 4 games × 256 units = 4,096 units total**, mid-tier full-price quality bar at game endpoint (Hewson/Gremlin/Mikro-Gen/Durell era, ~£7.95).

Revises v4.0 curriculum doc's per-game unit counts (128/256/512/512 → 256/256/256/256). Per-game phase structure is per-brief; phase sizes are powers of 2; Phase 1 of each game is conventionally an 8-unit vertical slice (from `october-2026-vertical-slice.md`).

**Acceleration assumption named as load-bearing.** The 4,096-unit total is viable only if authoring accelerates through pattern reuse, workflow maturation, LLM assistance, and eventually contributors. Realistic acceleration probably brings later games to 60–70% of Game 1's per-platform time — not the 10× speedup needed for short-project math. If acceleration doesn't materialise, scope cuts (fewer games per platform, fewer platforms, or longer timeline) are the response.

Forward-flags curriculum-doc reconciliation: per-game counts need revising, the Gravelight/Shadowkeep naming drift needs resolving, and Game 3 (Grimstone, isometric adventure) was sized for Knight Lore scale and may need design adjustment to fit 256 units. All deferred until each game's brief is touched in turn.

---

## 2026-05-13 — Spiral + incremental progression model captured (fifth of sequence)

**Type:** decision
**Pages created:** `decisions/spiral-and-incremental.md`
**Pages edited:** `index.md`

**Notes:** Fifth decision in the sequence. Curriculum uses two progression models at different scales: **incremental scaffold within phases** (each unit adds one capability, preserved from existing Shadowkeep design doc), **spiral progression across phases** (each phase revisits earlier work at a richer level — animation deepens movement, scale deepens room engine, depth deepens audio).

Names the failure modes the hybrid avoids: spiral within a phase is pedagogically muddled (each unit reopens previous units); pure incremental across phases is boring and lets skills atrophy. Both scales need their own model.

Brief Section 7 now declares two things per phase: *what's new* (incremental) + *what revisits earlier work* (spiral). The "revisits" line is the explicit spiral declaration. Phase boundaries are budgeted-for refactoring points, not unplanned scope creep.

Forward-flags reconciliation work: the existing Shadowkeep design doc names "incremental scaffold" but is silent on the across-phase model; needs an addition when next touched.

---

## 2026-05-13 — Constraint position taxonomy captured (fourth of sequence)

**Type:** decision
**Pages created:** `decisions/constraint-position.md`
**Pages edited:** `index.md`

**Notes:** Fourth decision in the sequence. Replaces the loose "could-have-shipped" framing with an explicit three-tier taxonomy: **period-faithful** (techniques common in commercial era product), **period-possible** (existed but rare in commercial use), **modern scene** (hardware allowed it; codified later, typically 2010s onwards through demoscene/homebrew collaboration).

Each game declares its position in brief Section 5. If the position varies across phases, Section 7 names the per-phase mapping. Most games likely move along the spectrum — early phases period-faithful, later phases incorporating period-possible or modern-scene work.

Names the failure mode: misrepresenting modern-scene techniques as "what 1987 looked like." A Phase 4 Shadowkeep using Saukas-era 8x1 multicolour is a 1987-spec game built with 2025 knowledge, not a 1987 commercial game. The taxonomy makes that distinction explicit rather than papering over it.

Per-platform reference pages in `knowledge/platforms/` will carry the detailed technique inventories per position.

---

## 2026-05-13 — Phase-boundary gating rule captured (third of sequence)

**Type:** decision
**Pages created:** `decisions/phase-boundaries.md`
**Pages edited:** `index.md`

**Notes:** Third decision in the sequence. Structural rule that makes the multi-disciplinary commitment operational at phase scale: pedagogy sets the sequence within a phase; commercial bar gates the output at every phase boundary. Different scales, different winners — pedagogy wins per-unit, commercial bar wins per-phase.

Codifies what `commercial-bar-revamp.md` declared ("phases must be complete games") into a structural rule for brief Section 7 and phase-end review. Names the failure mode it prevents: the gravitational pull of code-led pedagogy quietly deferring game-completeness phase by phase (the original Dash/Starfield/Exodus pattern).

Forward-references the forthcoming spiral-progression decision — the phase-end gate applies on every spiral revisit, not just the first time through.

---

## 2026-05-13 — October 2026 launch reframed as vertical slice (second of sequence)

**Type:** decision
**Pages created:** `decisions/october-2026-vertical-slice.md`
**Pages edited:** `decisions/october-2026-launch-spec.md` (status banner added — Shadowkeep portion partially superseded), `index.md`

**Notes:** Second decision in the sequence. Shadowkeep's October deliverable shifts from "16-unit Phase 1 complete game" to "8-unit vertical slice." Less content, higher per-unit ambition, marketed as a vertical slice — *demonstration of the bar* rather than a complete first chapter. The remaining three October artefacts (BASIC games, landing page, vault) are unchanged.

Cut hierarchy revised: vertical slice can trim 8 → 4 units before BASIC count cuts begin. Below 4 units, the slice fails to demonstrate the bar and the cut should fall elsewhere.

The supersede is partial — the launch spec carries a status banner pointing to the new decision rather than a full SUPERSEDED marker. Schema doesn't formally describe partial supersedes; this pattern keeps the still-valid parts of the older doc in force without forcing a rewrite.

---

## 2026-05-13 — Real-retro-games decision captured (first of a sequence)

**Type:** decision
**Pages created:** `decisions/real-retro-games.md`
**Pages edited:** `index.md` (added decision to the Decisions section)

**Notes:** First in a sequence of decisions emerging from a long design discussion. Captures the master commitment: Code198x builds real retro games, not toy examples — code, visuals, audio, level design, and polish co-equal from the brief downward. Builds on `commercial-bar-revamp.md`; sharpens the bar from "budget label 1986–1991" to **mid-tier full-price** (Hewson/Gremlin/Mikro-Gen/Durell era, ~£7.95).

Triggered by pressure-testing the Game 1 brief format on Shadowkeep and discovering the existing 9-room Phase 1 ships at Mastertronic-budget scale despite the "1984 Ultimate-tier" framing. The technique-led brief format was silently underweighting visuals/audio/level/polish; this decision elevates them to first-class.

Subsequent decisions in the sequence (forthcoming): October launch as vertical slice; pedagogy-sequences/commercial-bar-gates-phase-ends; constraint position taxonomy; spiral + incremental hybrid progression; curriculum structure (4 platforms × 4 games × 256 units per game, internal phase structure TBD, mid-tier full-price target, acceleration assumption load-bearing).

---

## 2026-05-06 — Emu198x wired into Code198x screenshot pipeline

**Type:** tooling
**Files created:** `code-samples/scripts/capture-spectrum-screenshot.sh`

**Notes:** Built `emu198x-script-spectrum` (the headless runner already living in the Emu198x repo) and wrapped it in a one-line shell helper. Takes `<game-dir> <unit-number>`, loads the unit's `.tap`, runs `--autoload-tape` + `--wait-for-tape-stop`, captures a PNG into `website/public/images/.../unit-NN/screenshot.png`. Phase 1 screenshot work goes from "wire up Fuse manually 16 times" to one shell command per unit.

**Implementation notes:**
- The script binary's `--load-snapshot` uses a postcard-encoded internal snapshot, **not** the SNA48 format pasmonext produces. So the `.sna` files we build are useless here — the route is `--tape` + `--autoload-tape`.
- Resulting screenshots show the BASIC tape loader's "Bytes: <name>" header at the top, on the standard grey-white BASIC canvas. That's correct: Unit 1 doesn't clear the screen (it has nothing to clear it *with* until `ldir` lands in Unit 3). The MDX has been rewritten to call this out as a teaching point — "a surgical change, only the cell we wrote changed" — rather than fudge it.
- Default ROM path: `~/.emu198x/roms/sinclair-zx-spectrum-48k/48.rom`. Default Emu198x checkout: `~/Projects/Emu198x`. Both overridable via env vars (`SPECTRUM_ROM`, `EMU198X`, `EMU198X_BIN`).

This unblocks Definition of Done item #4 (screenshots per unit) for the entire Spectrum assembly track. Same approach should work for the C64, NES, and Amiga via their respective `emu198x-script-*` binaries (not yet wired up).

---

## 2026-05-06 — Shadowkeep Unit 1 MDX + .asm rewritten to new Phase 1 spine

**Type:** curriculum draft
**Files edited:**
- `website/src/content/curriculum/sinclair-zx-spectrum/assembly/game-01-shadowkeep/index.mdx` (rewrote — 128-units claim removed, Phase 1 spine table added, flagship-insight section, phase-plan disclosure, magazine voice)
- `website/src/content/curriculum/sinclair-zx-spectrum/assembly/game-01-shadowkeep/unit-01.mdx` (rewrote tighter — single attribute write, single cell on screen; old version overshot into Unit 3 territory; revised opening to be honest about the un-cleared canvas)
- `code-samples/sinclair-zx-spectrum/game-01-shadowkeep/unit-01/shadowkeep.asm` (rewrote — eight-line minimal program: load A, store to $5990, halt loop)
- `website/public/images/sinclair-zx-spectrum/game-01-shadowkeep/unit-01/screenshot.png` (regenerated — old screenshot was from the previous version's full hand-drawn room and didn't match the new code; new one captured via emu198x-script-spectrum)

**Notes:** First MDX/asm pair drafted under the new incremental-scaffold pattern and the new commercial-bar voice. Unit 1 is now genuinely *one byte at one address* — every wall/floor/treasure beat moves into Units 2-3 where the new spine puts them. Snippet files (01-border.asm, 02-one-cell.asm, 03-walls-and-floor.asm) are now orphaned in code-samples; left in place for Phase 1 cleanup pass rather than removed mid-task. Next: Unit 2 MDX (reading attributes back, AND/OR for bit fields).

---

## 2026-05-06 — Shadowkeep Phase 1 design and beeper spec landed

**Type:** new artifact
**Pages created:** `curriculum/shadowkeep-phase-1-design.md`, `curriculum/shadowkeep-beeper-spec.md`
**Pages edited:** `curriculum/revamp.md` (Shadowkeep section now points at the design doc, outstanding-work checklist updated), `index.md` (both new docs surfaced)
**Notes:** Full Phase 1 design for Shadowkeep persisted to disk — premise (haunted keep, recover the Heart), commercial reference (Atic Atac × Sabre Wulf 1984 Ultimate), 16-unit incremental spine, 8-cell-type attribute vocabulary, 22×16 cell room grid, 9-room (3×3) Phase 1 layout, risks, open questions. Beeper composition spec persisted alongside — single-voice 48K beeper, ~30-60s title loop, D minor, 110 BPM suggested, structural breakdown across statement/variation/bridge/return, reference tracks, submission format. In-game music explicitly out of Phase 1 scope (period-correct silence). Next: composition + Unit 1 MDX draft + Units 9-10 prototype (the multi-room engine spike).

---

## 2026-05-05 — Curriculum revamp project, comprehensive scope and principles

**Type:** decision + tracker + new artifact
**Pages created:** `decisions/commercial-bar-revamp.md`, `curriculum/revamp.md`, `curriculum/lesson-references.md`
**Pages edited:** `curriculum/writing-voice.md` (extended with magazine-class framing)
**Notes:** Substantial single-day project initiation covering strategy, scope, principles, and operational artifacts.

Core decisions locked:
- **Bars:** assembly = commercial 1986; BASIC = Usborne 1984 on-ramp.
- **Voice (site-wide):** magazine-class — *Crash* / *Zzap!64* / *Your Sinclair* / *ACE*.
- **Unit counts:** powers of 2, nested. Per-game 8-512 (climbing bar). Platform totals up to 8192.
- **Quality bar:** non-negotiable. Cut count when runway tightens, never bar.
- **Definition of Done:** 9-item checklist per unit (incl. cross-references resolve).
- **Cross-referencing discipline:** every unit links to vault and patterns; catalogued in lesson-references.md.

October Crash! Live deadline drives everything:
- Shadowkeep (priority 1, multi-phase, DONE at Phase 4 probable, 8 possible). Phase 1 = October floor. **Incremental scaffold pattern**, not type-in.
- All 16 BASIC games at Usborne bar.
- Spectrum vault reviewed + gaps filled.
- Polished Spectrum landing page.
- C64/NES/Amiga deferred to coming-soon for October; Cadence design preserved for January-onward work.

Cut hierarchy under runway pressure: drop Shadowkeep phases (4 → 3 → 2 → floor at Phase 1) before touching BASIC games.

---

## 2026-04-05 — Initial seed

**Type:** ingest
**Sources:** CLAUDE.md, docs/UNIT-SPECIFICATION.md, docs/CONTENT-CREATION-WORKFLOW.md, accumulated session knowledge
**Pages created:** 10 pages across platforms/, curriculum/, infrastructure/, decisions/
**Notes:** Seeded from existing project documentation and session knowledge. Formal specs remain in docs/; wiki captures experience applying them.
