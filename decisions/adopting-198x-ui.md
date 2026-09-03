# Decision: the website adopts 198x-ui, after CRASH! Live

**Status:** ACCEPTED — 2026-09-03. Executes the deferred half of
[`198x/decisions/family-visual-identity.md`](https://github.com/198x/198x/blob/main/decisions/family-visual-identity.md),
which settled the family's wordmark, palette and type roster on 2026-08-20 and
recorded the Code198x move as sequenced for the October launch, "not a verdict".
**This record owns sequencing and migration mechanics only.** Decisions about
what the site looks like live in
[`website-visual-language.md`](website-visual-language.md), which was reconciled
against the family record on the same day. Where this record touched the visual
language — the type roles, the chunky shadow, how diagrams theme — those
decisions have moved there and are summarised here only as the thing being
migrated to.

## What the spike found

Measured on 2026-09-03 in a throwaway worktree against `main` at `0030f425`,
with the kit at `v0.5.1`.

The migration builds clean. **78 files, +437/−430, `npm run build` exit 0**, and
no component needed rewriting — it is token substitution plus a change of which
face does which job.

**31 of the site's 68 root tokens map onto the kit directly.** Of the 37 that do
not, most are not gaps:

| Category | Count | Disposition |
|---|---|---|
| Status and difficulty colours | 12 | Stay site-local. The identity record's drift trigger keeps a data axis inside its chart. |
| Platform colours | 8 | Not a token gap. Move to the kit's `machines.json`, which carries 156 systems against the site's 8. |
| Extra surfaces | 7 | **Real gap.** `bg-secondary`, `read`, `surface-translucent`, `accent-dark` have no kit equivalent. |
| Off-ladder spacing | 4 | **Real gap.** `space-5/10/14/20` are not on the kit's 4px ladder. |
| Chunky shadows | 2 | **Resolved 2026-09-03: retired.** They were a conflict rather than a gap — `website-visual-language.md` named the chunky offset shadow as part of the structural signature, and the kit's lift ladder is soft-only. The shadow is retired there; square corners and 3px borders carry the signature alone, and the site takes the kit's ladder. |
| Paper texture | 2 | Stay site-local. Decoration the kit does not carry. |
| Layout | 2 | Stay site-local. The kit is components, not layouts. |

That left roughly 13 genuine decisions. Retiring the chunky shadow settles two
of them, so **11 remain**: the four off-ladder spacing steps and the seven extra
surfaces.

## The decision

### 1. Reading copy moves to the serif — this is the migration's payload

Decided in [`website-visual-language.md`](website-visual-language.md) § *Type*.
Recorded here because it sizes the work: `Layout.astro` sets `body` to the
interface face and unit prose inherits it, so the change is three lines and it
is the one a reader sees. The palette shift is subtle; the face change is not.

### 2. The plate replaces the logo, and the homepage carries the full name

The mark becomes `[ CODE | 198x ]`, from the kit's `Plate`. `logo-horizontal.svg`
and `logo-198x.svg` retire from both sites that use them — the nav, and the footer, which is the
one a swap misses.

**The identity record did not say what happens to "Like It's".** It makes the
plate the wordmark in §1 and allocates Nebula Sans to "the slogan" in §4, but
the flagship is named *Code Like It's 198x* — in `og:site_name`, in the `<title>`
suffix, and in both logo files. Leaving that unanswered is what stalled the swap.

Answered here: the plate is the mark everywhere, and the **full name appears on
the homepage** as part of the branding push. The plate's `aria-label` carries
`Code Like It's 198x`, so the accessible name keeps the site's real name even
where the mark reads `CODE | 198x`.

This needs writing back into the identity record, which is the binding one.

### 3. The kit ships from npm as `@198x/ui`

The `@198x` scope is registered. The kit becomes a real dependency with real
semver, lockfile-pinned, replacing `fetch-ui.sh` cloning into a gitignored
`_198x-ui/` with no lockfile and no integrity check, plus the `predev`/`prebuild`
hook every consuming site currently needs.

The five sites already on `fetch-ui.sh` move one at a time; the pinned-tag
mechanism keeps working while they do. They are pinned at `v0.3.1` against a kit
at `v0.5.1`, so they are already behind.

### 4. Three components change hands

| Component | Where it goes | Why |
|---|---|---|
| `ThemeToggle` | **Promote to the kit** | `tokens.css` declares the three-state theme contract — `[data-theme]` light, dark, and absence meaning system — and ships nothing to drive it. The site's toggle is 126 lines, has no imports, and implements exactly that contract. Every family site that wants theming is currently reinventing it. |
| `SiteNav` trailing slot | **Kit change** | `SiteNav` has no slots. The site's bar carries four links plus search plus the theme toggle. A slot lets a host mount those without the kit learning what they are. |
| `SiteNav` mobile disclosure | **Kit change** | Its whole mobile story is `flex-direction: column` at 40rem. That is right for a landing page with three links and wrong for six controls. |
| `Breadcrumbs` | **Promote to the kit** | Split the way `SiteNav` already splits: the kit renders a trail it is handed, the host resolves it. The site's version imports `getAllPlatforms` and carries a label map, but that is data resolution and it stays here. The rendering is generic. |
| `ImageComparison` | **Promote to the kit** | 260 lines, no imports. Emu198x's whole job is fidelity, and emulator output against real hardware is a before/after slider exactly. Asm198x can show source against output. |
| `Figure` | **Promote to the kit** | Every site shows captioned images, and it carries the credit and licence machinery every site needs the moment it reuses third-party imagery. |
| `TableOfContents` | **Promote to the kit** | 273 lines, no imports. Asm198x reference pages and the Emu198x docs both want one. |
| A generic `Callout` | **New in the kit** | Not `SetupCallout`, which is Docker- and platform-specific and stays. The *shape* — a bordered aside carrying a role — is wanted on every docs surface. |

Probably, once a second consumer appears: the media primitives `VideoEmbed`,
`VideoPlayer` and `AudioClip`. Play198x is a media player and Emu198x shows
captures; `AudioClip`'s own header already calls it "an IA v3 media primitive".

`Search` stays site-local: 233 lines and 22 Pagefind references. The kit must not
depend on a search index. `Attribution` stays too — with credit on `Figure`, what
is left of it is magazine and archive sourcing, which is Vault work.

**`ThemeToggle` rolls out across the family**, not only into the kit. Every site
inherits the three-state contract the moment it takes the kit's tokens, and a
contract with no control is what left the site carrying its own.

**The extraction rule, alongside "components, not layouts".** The kit takes a
component when a **second site needs it**, not when one looks generic.
The six teaching diagrams make the case: `SpriteEditor`, `MemoryMap`,
`RegisterBits`, `SpectrumBitmapLayout`, `FlowDiagram` and `SpriteGrid` are 1,842
lines with no imports between them, which makes them look like prime candidates.
No imports means self-contained, not generic — they are curriculum pedagogy and
they stay. Without this rule the shared layer becomes a dumping ground three
sites have to negotiate over, which is the failure "components, not layouts" was
written against.

### 5. `Figure` loses its platform frames

`Figure` could wrap an image in a per-machine CRT treatment — a coloured outer
glow and an inset vignette over the picture. Ten call sites used one; six passed
`frame="none"` to opt out.

It goes because decoration over a capture is wrong on a site where a capture is
evidence: a screen that should look like a CRT should look that way when it is
captured. It also removes the component's only tie to a fixed list of four
machines, which was the blocker on promoting it. If per-machine framing returns
it reads `machines.json` and its 156 systems.

### 6. Section headings lose their coloured rule

A short coloured bar sat before every `h2` — five declarations across four
files, in three sizes and three colours, the machine colour twice and the rust
accent twice. It is decoration attached to a heading, competing with the heading
at the moment the heading is doing its job.

Worth being exact about why it goes: **the record permits it.** §3's axis table
lists "content markers, cards, headings, platform badges" as places machine
colour may appear. This was allowed rather than required, and removing it is a
judgement about how the pages read, not a compliance fix.

### 7. Diagrams are SVG, and the kit gives them six tokens

Diagrams get used more widely across the family, drawn as SVG.

**Why SVG rather than monospace figures.** A figure drawn in box-drawing
characters renders at the mercy of the reader's font stack: the Spectrum memory
map in the machine briefing had to be redrawn in plain ASCII because the mono
face carries no `┌ ─ ┤` glyphs and fell back to a proportional font, so the
verticals missed the horizontals. SVG has no such failure mode.

**The theming, which is not much.** Six tokens in the kit, resolving per theme
through `light-dark()` like everything else. The rule that diagrams use only
these, and nothing hardcoded, belongs to
[`website-visual-language.md`](website-visual-language.md):

| Token | Job |
|---|---|
| `--h-dia-ground` | the diagram's own background |
| `--h-dia-ink` | labels and text |
| `--h-dia-line` | strokes, rules, axes |
| `--h-dia-fill` | neutral block fill |
| `--h-dia-fill-alt` | a second fill, for banding |
| `--h-dia-accent` | the one thing the diagram is pointing at |

An author writes `fill="var(--h-dia-fill)"` and never thinks about themes again.
`currentColor` covers the rest for free, since SVG inherits `color`.

**Inline SVG only.** Custom properties do not cross into an externally
referenced file, so a diagram shipped as a `.svg` and dropped in with `<img src>`
cannot see these tokens and cannot be themed. Diagrams are Astro components that
emit inline `<svg>`. This is the thing to get wrong — exporting flat SVGs from a
drawing tool is the obvious move and it forecloses theming entirely.

**What the identity record already constrains.** §3's axis table applies
unchanged: machine colour may appear, project colour may not, and a diagram that
colours categories is a chart — its colours live inside it, keyed to a legend.

**The six existing diagrams stay here and get ported.** `MemoryMap`,
`RegisterBits`, `SpectrumBitmapLayout`, `FlowDiagram`, `SpriteGrid` and
`SpriteEditor` are curriculum pedagogy and do not move. But **none of the six
reacts to theme** — no `data-theme` or `prefers-color-scheme` rule between them,
and 38 hardcoded colours, including `#1a1714`, which is the kit's *dark* page
base sitting in a light-mode diagram. Porting them onto the six tokens is what
makes them correct, and it is separable from moving anything.

### 8. OG images are generated per page

The current one is a single static PNG shared by roughly 2,300 pages, and it
breaks the identity record in four places:

- **`198x` is the coloured element** and the prefix is not. §1's drift trigger
  forbids colouring the `198x` cell; this is that inversion exactly.
- **Four filled machine badges.** Drift trigger 1: a project hue never leaves the
  plate.
- **The retired cool palette** — navy ground, blue accent. Reintroducing teal as
  a family colour is itself a drift trigger.
- **The name set as plain type with no plate**, which is verbatim the problem §1
  was written to solve.

Replaced by build-time generation, so a unit or a Vault entry shares as itself
rather than as a generic card. This adds an image pipeline and a dependency, and
that dependency gets asked about before it lands.

## Sequence

**Before CRASH! Live — three things.**

1. **Retire Caveat.** Already decided by the identity record; deferred there only
   to be done alongside the type move. **It is 80 declarations across 46 files** —
   corrected 2026-09-03. This record first said ten across eight, a figure taken
   from a grep truncated by `head` and never rechecked; the identity record's own
   estimate of five components is wrong for the same reason. Caveat carries most
   of the site's display headings, not a handful of components.

   The hazard is leading, not count: fifty of the eighty declarations pair the
   face with a `line-height` under 1.0, down to 0.7. That is safe for a script
   face with a small x-height and untested for a text serif. Checked
   rather than assumed — every sub-0.85 case is a single line or a single glyph,
   and the longest module title on the site wraps to two lines at 0.82 and
   clears. No line-heights needed changing.
2. **Drop the heading rules.** Purely subtractive, five declarations, no rule
   broken and nothing orphaned — `--systemColor` and `--sys` keep six and
   thirteen other uses between them.
3. **Fix `--color-text-muted`.** `website-visual-language.md` already rules that
   `#94a3b8` is "decorative and large-only, never small informational text", so
   this is the site breaking **its own** record, not only the kit's guidance. It is `#94a3b8` — byte-identical to the kit's
   `--h-ink-faint`, which the kit marks *decorative and large only, never small
   informational text*, at 2.27:1. The site's token name invites exactly the use
   the kit forbids. This is a bug, not a restyle, and it is not contingent on any
   of the above.

**After CRASH! Live — everything else**, in this order: publish `@198x/ui`;
adopt tokens behind a shim; move reading copy to the serif; swap the plate;
promote `ThemeToggle` and extend `SiteNav`; generate OG images; then delete the
shim by resolving the 13 real gaps one at a time.

The shim matters. Redefining the site's 68 tokens in terms of the kit's is how
the migration lands in one reviewable step instead of rewriting 4,753 lines of
component CSS, and it is what the spike did.

## What the spike also turned up

Not migration work, recorded so it is not rediscovered:

- The dark block in `Layout.astro` restates **33 tokens** that the kit's
  `light-dark()` collapses to none.
- `src/pages/[platform].astro:236` references `--font-family-base`, which is
  defined nowhere and has never rendered.
- The machine→colour mapping now exists in **three** places: the site's
  `content/systems/*.yaml`, a hand-kept copy in `Layout.astro` that the identity
  record already flags as drift, and the kit's `machines.json`.
- **The drop cap is not the problem — Caveat was.** Set in Literata it renders as
  an ordinary serif drop cap. Whether it stays is a separate call, but it is not
  broken once the script face goes.

## Why this was written

Raised by Steve on 2026-09-03 while reviewing the Spectrum machine briefing,
where the handwriting face and the drop cap were the visible complaint. The
spike was commissioned to size the whole migration rather than patch those two.
Written down because the identity record's Code198x deferral reads as
a rejection — it says so itself — and because the wordmark question it left open
is the thing that would stall this again.
