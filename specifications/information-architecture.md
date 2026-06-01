# Information Architecture Specification

**Version:** 3.1
**Last Updated:** 2026-05-29
**Status:** Reconciled with the shipped synthesis build (supersedes v2.1, 2026-01-19).
**Companion file:** Wireframe canvas at `code198x/website-design` project root (`index.html`).

## Build status (2026-05-29)

What the synthesis build actually ships, against this spec:

- **Live & on-spec:** homepage · system landings · track overviews · game landings · unit pages · `/vault/` (+ entries, with "Referenced in lessons" backlinks) · `/patterns/` (+ browse facets) · `/about/` · `/setup/` · `/browse/` hub · `/contribute/` · the **status-tier system + never-404 stubs** · country codes on fleet pills · media primitives (`Photo`/`AudioClip`/`VideoEmbed`) available to authors.
- **As-built divergence from this spec:** the fleet's three lenses are **path URLs** (`/systems`, `/systems/by-maker`, `/systems/by-tier`), not `?by=` query params — clean paths won over query strings. The timeline's region lens should follow the same path form (`/timeline/by-region`) when built. The content collection is `systems` (renamed from `platforms`).
- **Pending:** the unit two-layout split (BASIC marginalia / Assembly sidebar — a focused session per the design notes); the timeline **six swim-lanes** + region atlas (currently decade cards + decade detail); the `by-genre` / `by-technique` browse facets (honest scaffolds until games/units carry those tags); pattern-entry backlinks (mechanism built, no inline pattern links yet); the footer "open-source band + colophon" shape.

## What changed from v2.1

v2.1 assumed four platforms going live in parallel and a `/curriculum/` + `/learn/` URL split. Reality has moved on:

| Concern | v2.1 | v3.0 |
|---|---|---|
| **Scope** | 4 platforms | ≈ 50 machines, 1975 → 2005, four decades |
| **Game count** | 16 per platform | Variable — dozens per machine, eventually |
| **URL prefixes** | `/curriculum/{platform}/`, `/learn/{platform}/...` | Dropped. Platform is the root. |
| **Coming-soon platforms** | Implicit | First-class tier system, always visible, never 404 |
| **Cross-cutting** | One `/vault/`, one `/patterns/` | Adds `/timeline/`, `/browse/`, `/contribute/` as top-level destinations |
| **Geography** | Absent | First-class — `/browse/by-region/`, country tags on machines, timeline events tagged by country |
| **Culture** | Vault only | Timeline carries hardware alongside people, companies, games, culture, world events |
| **Media** | Screenshots | Photos, video, audio, plus heavy outbound links to trusted archives |
| **Voice / Community** | Implicit | Free · open source · forever. `/contribute/` is a first-class destination. Everything is GitHub-flow. |

---

## Core principles

1. **Honest about what's live.** Every machine has a status tier — Live / Next / Planned / Edge of domain / Beyond. Status is visible on every card. Coming-soon pages exist as real URLs with subscribe boxes, never 404s.
2. **Platform is the root.** The URL `/sinclair-zx-spectrum/shadowkeep/unit-01/` is shorter, more readable, and survives reorganisation. No `/curriculum/` or `/learn/` segment.
3. **Computing didn't happen in a vacuum.** The timeline is its own destination. Hardware sits next to people, companies, games, culture, and world events.
4. **The site brand is platform-neutral.** Site chrome (nav, footer, accents) is house-coloured. Each platform's identity lives inside its own pages — the Spectrum rainbow only appears on Spectrum pages.
5. **One vault, many platforms.** All cross-cutting reference content lives in the shared `/vault/`. Patterns are platform-specific (`/patterns/{platform}/...`) because the code is platform-specific.
6. **Media throughout.** Photos, video clips, audio samples on every appropriate entry. Heavy outbound linking to trusted archives (Wikipedia, World of Spectrum, HVSC, archive.org). A recurring "Further afield" pattern.
7. **Community-built.** The ambition exceeds one person. `/contribute/` is a top-level destination. All contribution happens via GitHub issues / PRs.

---

## Top-level structure

Six top-level destinations. Plus `/about/`, `/how-to-use/`, and the system/game/unit hierarchy.

```
/
├── /systems/            The fleet — ≈ 50 machines, 1975 → 2005
├── /timeline/           Rich history — hardware + people + culture + world
├── /vault/              Encyclopedia — shared across all systems
├── /patterns/           Code library — production-ready patterns per system
├── /browse/             Discovery — cuts sideways across the fleet
├── /contribute/         Call for help — open source, GitHub-flow
│
├── /{system-slug}/                                           ← system landing
│   └── /{system-slug}/{track-slug}/                           ← track overview
│       └── /{system-slug}/{track-slug}/game-{NN}-{game-slug}/  ← game landing
│           └── .../unit-{NN}/                                  ← unit page
│
└── /about/              Mission, how it works, credits, licensing, archive
```

### Terminology note

"System" is the structural term — the directory name, the URL segment, the content collection key, the nav item. We picked it for its period-correct precision: in 1985, Crash reviewed *systems*, not *platforms*. Inside editorial prose use whichever word reads better in context; "platform" is fine wherever it flows naturally, and we don't enforce it.

---

## URL patterns

### System landing
`/{system-slug}/`
- Slug is full, descriptive: `sinclair-zx-spectrum`, `commodore-64`, `nintendo-entertainment-system`, `commodore-amiga`, `bbc-micro`, etc.
- This is the **QR-code entry point** for flyer campaigns. Distinct from `/`.

### Track segment
`/{system-slug}/{track-slug}/`
- Explicit on every system with multiple tracks. Examples: `/sinclair-zx-spectrum/basic/`, `/sinclair-zx-spectrum/assembly/`, `/commodore-amiga/amos/`.
- Single-track systems (e.g. NES, assembly-only) still get an explicit track segment for consistency: `/nintendo-entertainment-system/assembly/`.
- A bare `/{system-slug}/` lands on the system overview with both track cards.

### Module landing
`/{system-slug}/{track-slug}/{module-slug}/`
- Examples: `/sinclair-zx-spectrum/assembly/shadowkeep/`, `/commodore-64/assembly/sid-symphony/`, `/sinclair-zx-spectrum/basic/lucky-number/`.
- The `{module-slug}` is a **bare identity** — no `game-NN-` prefix. Canonical order is the module catalogue's array position (`src/content/modules/{system}/{track}.yaml`), not anything in the slug. See [decisions/modules-not-games.md](../decisions/modules-not-games.md).
- Renaming *and* re-ordering are free — re-ordering is a data edit (catalogue position), not a URL change, so no redirect is needed. Shipped pre-module URLs keep working via redirects in `astro.config.mjs`.

### Unit page
`/{system-slug}/{track-slug}/{module-slug}/unit-{NN}/`
- Examples: `/sinclair-zx-spectrum/assembly/shadowkeep/unit-01/`.
- Unit page lives at `unit-NN.mdx` inside the module's directory. No descriptive slug — unit titles change but the number is stable. This matches existing Astro routing.

### Cross-cutting
- `/timeline/` and `/timeline/by-region/` (path-based, matching the fleet lenses — not `?by=`)
- `/vault/{category}/{slug}/` — `/vault/people/rob-hubbard/`, `/vault/hardware/sid-6581/`, `/vault/games/knight-lore/`, `/vault/publications/crash/`
- `/patterns/{system-slug}/{category}/{pattern-slug}/`
- `/browse/by-{axis}/` — `by-system`, `by-era`, `by-region`, `by-genre`, `by-technique`, `by-difficulty`
- `/contribute/`, `/contribute/good-first-issues/`, `/contribute/ways-to-help/`

### Status conventions
- **Live**: full content, no prefix
- **Next / Planned / Edge / Beyond**: page exists, contains stub content + subscribe form + link to GitHub issue for that machine
- Nothing ever 404s. A machine with no content yet has a placeholder page that says "we will eventually do X — track progress in #142".

---

## Page types

Each page type below has a winner from the wireframe canvas. Where two variants survive, both are valid for different contexts.

### 1. Homepage  ·  `/`

**Winner:** Magazine voice + docs structure (HomeBlend).

**Purpose:** Welcome anyone arriving with no context. Show what's ready today; hint at the four-decade ambition; invite contribution.

**Sections, top to bottom:**
1. **Top nav** — house brand wordmark, neutral. Links: Platforms · Timeline · Vault · Patterns · Browse · Contribute · About.
2. **Hero band** — handwritten headline "Make a real game, on a real old machine." House rule beneath. Paragraph + two primary CTAs ("Start with ZX Spectrum →", "How this works").
3. **Fleet stat block** — sidebar card on the hero row: ≈50 machines · ~16 games/machine · 6 regions · 1 live now · ∞ contributors welcome. "Free · Open source · Forever" rubric. Buttons: "Open the fleet →", "Help build it →".
4. **What's ready · what's next** — hero card (Spectrum, live) + three "next" platform cards (C64 / NES / Amiga). Each card shows: platform motif, name, year+region, tagline, status stamp. Border to `/platforms/`.
5. **Four decades · pick a year** — six decade cards (1975-79 through 2000-05). Highlighted middle two — "where the curriculum lives." Link to `/timeline/`.
6. **Pillar cards** — four cards: Vault, Patterns, Timeline, Browse. Each shows its URL, title, one-line description.
7. **Honest ask band** — high-contrast call-to-action: "≈ 50 machines · dozens of games each · one of me. Free, open source, forever. Pick a tile →". Links to `/contribute/`.
8. **Footer** — open-source band on top (WANTED stamp + GitHub link + Contribute CTA), wordmark + five-column nav below (Platforms / Reference / Contribute / The shed).

**Background atmosphere:** halftone newsprint dot pattern + a giant faded "198x" ghost word, behind content.

### 2. Platform landing  ·  `/{platform-slug}/`

**Winner:** Magazine welcome with track fork.

**Purpose:** The QR-code entry point. The visitor may know nothing about the platform OR be a returning hobbyist; the page must serve both.

**Sections:**
1. **Hero** — "You found us · Welcome to the {Platform}, friend." Handwritten headline. Per-platform rainbow / stripe accent. Platform motif placed top-right.
2. **The machine band** — machine silhouette / photo + spec table (CPU, RAM, display, sound, storage) + "Further afield" external links (Wikipedia, period archive, community forum).
3. **Track fork** — two large cards: a "gentle" track (BASIC or similar HLL) and a "flagship" track (assembly). For platforms with no BASIC track, one card.
4. **While you're here** — three cards: Vault entries scoped to this platform, Patterns scoped to this platform, "What's not here yet" with subscribe form.
5. **Footer** as global.

**Background atmosphere:** scanlines + per-platform ghost-word tinted in the platform's accent colour (e.g. red "ZX" for Spectrum).

### 3. Curriculum overview  ·  `/{platform-slug}/{track}/`

**Two winners — both valid:**
- **A · Magazine Table of Contents** — every game listed like a magazine article with handwritten title, blurb, page number. Canonical organisation.
- **C · Guided flowchart** — a recommended path through tracks for first-time visitors. Lives at `/{platform-slug}/start/` or as an alternate view.

Use both. TOC is the default; Guided is the "I'm new, where do I start?" mode.

### 4. Game landing  ·  `/{platform-slug}/{game-slug}/`

**Winner:** Magazine feature spread (GameMagazineSpread).

**Purpose:** Sell the game; show what you'll build; orient new arrivals into the unit sequence.

**Sections:**
1. **Hero** — "Game N · of M to follow" kicker. Big handwritten name. Per-platform stripe. One-paragraph pitch positioning the game in its canonical lineage (e.g. "in the lineage of Atic Atac, Knight Lore, Cybernoid II").
2. **Video preview** — embedded gameplay clip of attract loop or representative play, running on real hardware.
3. **Three engine commitments** — bullet list. What this game proves, technically.
4. **Build setup photo** — real photograph of the hardware + dev environment.
5. **Arcs / phases sidebar** — visible status per arc ("NOW" / "2027" / "2027-8"). Big CTA: "Begin Arc 1, Unit 1 →".
6. **Tools you'll need** — Fuse, Pasmonext, 30 min/session.
7. **In the lineage of** — "Further afield" external links: World of Spectrum / Wikipedia / period magazines for each canonical reference.

**Background atmosphere:** pixel grid + light CRT scanlines.

### 5. Unit page  ·  `/{platform-slug}/{game-slug}/{unit-slug}/`

**Two winners — context-dependent:**
- **A · Magazine type-in (marginalia)** — for BASIC track units. Drop cap, code listing centred, sticky-note Vault/Pattern references in the margin. Reads like an Usborne 1984 type-in.
- **B · Docs sidebar** — for Assembly track units. Left rail of all units in the game, main column body, right rail with citations / patterns / downloads / progress.

Track preference is metadata on the unit; the renderer picks the layout. Both share content structure and frontmatter.

**Required content sections (both layouts):**
1. Breadcrumb + unit number + estimated time + difficulty
2. **What you'll build** — wonder-first framing
3. **Getting started** — code listing
4. **Common pitfalls** — bulleted list
5. **Watch · what we just built** — video clip of expected output
6. **What you've learnt** — bullet summary
7. **Try this** — three optional exercises
8. **Further afield** — Vault + Pattern citations + external links

**Background atmosphere:** halftone (subtle — must not interfere with reading).

### 6. The Fleet  ·  `/platforms/`

**Three lenses on the same data, all valid:**
- **A · Timeline by decade** — default. Six decade columns, all machines plotted chronologically. Status badges visible.
- **B · By manufacturer** — `/systems/by-maker/`. Atari / Commodore / Sinclair / Acorn / Nintendo / Sega / Apple etc.
- **C · Commitment tiers** — `/systems/by-tier/`. Live / Next / Planned / Edge / Beyond honest tier table.

*(As built: the lenses are path URLs, server-rendered, not `?by=` query params — clean paths preferred. The decade view is `/systems/`.)*

Every machine entry shows: year · maker · name · kind (home/console/handheld/micro) · country code · status badge.

**Background atmosphere:** blueprint graph paper.

### 7. The Timeline  ·  `/timeline/`

**Winner:** Six swim-lanes 1975 → 2005, with a Country Atlas variant at `/timeline/by-region/`.

**Swim lanes:**
- **Systems** — every machine launch
- **People** — Rob Hubbard, Yannes, Stamper brothers, Romero+Carmack...
- **Companies** — Microsoft founded, Atari crash, Commodore bankruptcy, Rare founded...
- **Games** — landmark releases
- **Culture** — Star Wars, MTV, Walkman, Blade Runner, Akira, The Matrix...
- **World** — Vietnam ends, Thatcher elected, Berlin Wall, USSR dissolves, 9/11...

Every event is tagged with country (UK, US, JP, EU, SU, AS) and links to its detail page in /vault/ where possible. Filterable by lane, country, decade.

**Background atmosphere:** halftone, low opacity to keep the timeline scannable.

### 8. Vault  ·  `/vault/`

**Winner:** Magazine-style entries.

**Categories** (each at `/vault/{cat}/`): People · Games · Companies · Hardware · Techniques · Events · Publications · Demos.

**Entry template:**
- Type badge + name + dates + role
- **Polaroid / portrait** with caption
- **Quick facts table** — sidebar
- **Body article** — drop cap, magazine-class prose, ~300-600 words
- **Listen** — audio clips where applicable (Hubbard tunes, BBC chimes, etc.)
- **Watch** — video embeds
- **Notable works** — bullet list with cross-links
- **Related in The Vault** — tag cloud
- **Further afield** — heavy outbound links (official sites, Wikipedia, fan archives, demoscene)
- **Referenced in lessons** — backlinks to units that cite this entry

**Background atmosphere:** halftone.

### 9. Pattern Library  ·  `/patterns/{platform}/{category}/`

**Winner:** Magazine entries with metadata as marginalia.

**Categories per platform:** Rendering · Audio · Input · Physics · AI · Optimisation · Framework · Data.

**Entry template:**
- Hero: pattern name + introduced-in lineage
- Overview paragraph
- **Code listing** — annotated, ready to copy
- **How it works** — prose
- **Variations** — bulleted list
- **Performance notes**
- **Watch · see it in motion** — before/after video clip
- **Marginalia sidebar:** difficulty stars · introduced in · prerequisites · evolution chain · used in units · related Vault entries

**Background atmosphere:** pixel grid (digital tooling).

### 10. Browse  ·  `/browse/`

Six axes:
- `/browse/by-platform/` — list, no surprise
- `/browse/by-era/` — decade-grouped
- `/browse/by-region/` — UK / US / JP / EU / SU / AS, each with machines + companies + magazines + timeline events
- `/browse/by-genre/` — Platformer, shooter, puzzle, adventure...
- `/browse/by-technique/` — Sprite multiplexing, scrolling, collision...
- `/browse/by-difficulty/` — Foundation → Capstone

A `/browse/` hub shows all six axes + wander prompts ("Every platformer in the curriculum", "What shipped in 1986", "Machines that came out of Britain", "Lessons that cite Rob Hubbard").

### 11. Contribute  ·  `/contribute/`

**Purpose:** Honest ask. Recruit contributors. Set expectations.

**Sections:**
1. **Hero** — "I can't build all of this alone." Stamped "WANTED" in marginalia.
2. **How it works** — four-step GitHub flow: 1. File an issue → 2. Discuss → 3. Open a PR → 4. Merge & ship.
3. **The deal** — free / open source / forever / MIT code / CC-BY prose / public archive.
4. **Ways to help** — port a methodology, author a game, fill a vault entry, submit a pattern, test on real iron, illustrate, edit.
5. **Open issues right now** — grid of currently open GitHub issues with #numbers.
6. **What you get / won't get / the bar.**

**Background atmosphere:** halftone + giant ghost "HELP" word.

---

## Cross-cutting systems

### Site chrome
- **Nav:** Top horizontal docs nav (NOT a magazine masthead). Wordmark left, link list right (Platforms · Timeline · Vault · Patterns · Browse · Contribute · About), search at far right.
- **Footer:** Open-source band on top (WANTED stamp + GitHub link + Contribute CTA), then five-column nav (wordmark + colophon / Platforms / Reference / Contribute / The shed).
- **House accent colour:** deep newsprint brown (`--house: #3a2c1f`), with a brick highlight (`--house-2: #c25a3a`). Used for global rules, accent bars, CTA tinting.

### Per-platform identity tokens
Inside any `/{platform-slug}/...` page, two additional surface treatments come into play:
- **`PStripe`** — a 2-band coloured stripe used as an underline / accent. Each platform has primary + secondary tokens (Spectrum red+yellow, C64 blue, NES red+black, Amiga orange+purple, BBC navy+cream, CPC navy+orange, MSX grey+red, Atari ST grey+red, Game Boy LCD green).
- **`PlatformMotif`** — a recognisable visual fingerprint. Spectrum: rainbow + attribute hatching. C64: blue boot screen + READY. prompt. NES: black grid + red wordmark. Amiga: Workbench checker. BBC: cream + BASIC prompt. Game Boy: dot-matrix LCD. Used as decorative band on platform / game pages.

These are placeholders — production should swap in real illustrations or photographs.

### Atmospheric backgrounds
Each page type has a default atmospheric wash, blended at low opacity:
- **Homepage**: halftone + ghost "198x"
- **Platform landing**: scanlines + ghost platform-name
- **Game landing**: pixel grid + light scanlines
- **Unit page**: halftone (subtle)
- **Fleet**: blueprint graph paper
- **Timeline**: halftone
- **Vault directory + entries**: halftone
- **Patterns directory + entries**: pixel grid
- **Contribute**: halftone + ghost "HELP"

These are CSS layers — they're meant to convey *feel*, not to be precious about rendering.

### Media surfacing
Three primitives, used on every entry where appropriate:
- **`<Photo>`** — polaroid-framed image with caption
- **`<VideoEmbed>`** — film-perforation framed YouTube / archive.org embed
- **`<AudioClip>`** — waveform line + caption + source attribution (HVSC etc.)

### External links — "Further afield"
A recurring boxout pattern. Each page that documents real-world subjects (people, machines, games, techniques) carries a "Further afield" block linking to:
- Official sites where they exist (robhubbard.co.uk)
- Wikipedia
- Trusted archives (World of Spectrum, HVSC, archive.org, Mobygames)
- Active community forums
- YouTube channels with high-quality material

These links are first-class. They're not "see also" footnotes — they're celebrated.

### Vault/Pattern surfacing in units
Two valid surfacing modes:
- **Marginalia** (magazine type-in layout, used for BASIC units) — sticky-note Vault/Pattern references in the margin, in the reading flow
- **Sidebar** (docs layout, used for Assembly units) — right rail with "This unit cites" / "Related patterns" / "Downloads" / "Progress"

Both layouts share identical *content* — the surfacing is a layout decision per track.

---

## Status tiers — the honest-ambition system

Every machine has a status. Every status has visual treatment. No machine is ever "missing".

| Tier | Meaning | Visual treatment | Page content |
|------|---------|------------------|--------------|
| **Live** | Currently shipping content | Solid border, drop shadow, full motif, status stamp "LIVE" | Full curriculum + games + units |
| **Next** | Methodology validated, in build | Yellow tint, status stamp "NEXT" | Skeleton + ETA + subscribe form + GitHub issue link |
| **Planned** | Skeleton document only | Thin border, neutral | Spec page + subscribe form + GitHub issue link |
| **Edge of domain** | Hardware strains the methodology | Dashed border, dimmed | Honest writeup of why this strains the methodology + issue link |
| **Beyond** | Outside the canon | Dashed border, more dimmed | Brief acknowledgement, link to external resources |

Status is visible:
- On every `/platforms/` card
- On every homepage "next up" card
- On every fleet pill
- In timeline events (the "Systems" lane shows status colour)
- In `/browse/` results

---

## Geography as a facet

Every machine carries a country code (UK, US, JP, EU, SU, AS). Used:
- On every fleet pill (top-right corner of card)
- As a filter on the timeline (`?country=UK`)
- As one of the six Browse axes (`/browse/by-region/`)
- In platform hero kickers ("Live · UK · 1982")

That's it. Regions are metadata and a facet, not destinations. If a contributor wants to write a "Bedroom coders of Britain" feature, it lives as a Vault article — we don't promise the page exists before someone writes it.

---

## Mobile

The QR-code entry point demands mobile-first design for the platform landing page. For curriculum reading (unit pages), desktop is the assumed reading mode because the learner is at a keyboard. The site is responsive but not mobile-equivalent — type-in code listings benefit from width.

- `<768px`: single column, drawer nav (hamburger), Vault/Pattern surfacing collapses to "▾" disclosure
- `768-1023px`: optional sidebar
- `1024px+`: full layout with sidebar / marginalia

---

## SEO / metadata

Standard `<title>` format:
`{Specific} | {Context} | Code Like It's 198x`

Examples:
- `Unit 3: Reading the Keyboard | Lucky Number · Spectrum BASIC | Code Like It's 198x`
- `Rob Hubbard | People | The Vault | Code Like It's 198x`
- `Shadowkeep | ZX Spectrum Assembly | Code Like It's 198x`

Schema.org structured data:
- Units → `LearningResource` + `Course` hierarchy
- Vault people → `Person`
- Vault games → `VideoGame`
- Vault hardware → `Product` (subtype unclear; investigate)
- Timeline events → `Event`

OpenGraph image per page: generated from a template (handwritten title on paper background + relevant motif).

---

## Contribute → GitHub flow

All contribution happens on `github.com/code198x`. The site never accepts user content directly; it's a build artefact.

| Action | Where |
|--------|-------|
| File an idea | Issue on the relevant repo |
| Discuss approach | Discussion or comment thread |
| Open a draft | Branch + draft PR |
| Submit work | PR with code + prose + assets |
| Get reviewed | PR review with reference to the methodology spec |
| Ship | Merge → site rebuilds within minutes |

Issue templates:
- `port-a-platform.md`
- `author-a-game.md`
- `fill-a-vault-entry.md`
- `submit-a-pattern.md`
- `illustration-request.md`
- `bug-report.md`

`good-first-issue` labels surfaced on `/contribute/`.

---

## Open questions

Things I want feedback on before this becomes binding:

1. **Visual translation.** When this moves out of wireframes, several decisions remain: real typeface choices, real illustration commissioning, atmospheric-background production rendering (vs. CSS scaffolding), per-platform motif art direction. Not strictly an IA question — but it's the next milestone.

## Settled (was open in draft)

- **"Systems" vs "Platforms":** Systems. The structural term — URL segments, content collections, nav items — is *systems*. Editorial prose may use either word.
- **Track-fork URLs:** explicit `/{system-slug}/{track-slug}/...` segments on every system, including single-track systems.
- **Game / unit numbering:** zero-padded `game-{NN}-` and `unit-{NN}` (no unit slug) prefixes in URLs. Matches the existing Astro routing convention; no migration cost. Re-ordering requires a redirect.
- **About vs colophon:** keep the existing `/about/`. No `/colophon/`.
- **Regions:** facet only — country tag on machines + `/browse/by-region/`. No dedicated regional pages. If contributors write rich regional features later, they live as Vault entries.
- **Timeline + extra collections:** `src/content/timeline/`, `src/content/architectures/`, `src/content/manufacturers/`, `src/content/vault-categories/`, `src/content/pattern-categories/`, `src/content/pattern-difficulties/` already exist in the website repo. v3 designs around what's there, not on top of it.

---

## Version history

- **3.1 (2026-05-29):** Reconciled with the shipped synthesis build. Recorded what's live, the as-built divergences (fleet lenses are path URLs `/systems/by-maker` · `/systems/by-tier`, not `?by=`; content collection renamed `platforms` → `systems`), and what's pending (unit two-layout split, timeline swim-lanes, genre/technique browse facets). Added the Build status section.
- **3.0 (2026-05-26):** Reframed for the four-decade ≈50-machine fleet. Dropped `/curriculum/` and `/learn/` URL prefixes — platform is the root. Explicit track segments + zero-padded `game-{NN}-` / `unit-{NN}` URL numbering (matches existing Astro routing, no migration cost). Added `/timeline/`, `/browse/`, `/contribute/` as top-level destinations. Status-tier system. Geography as first-class. Media + external-links pattern. Per-platform identity tokens. Atmospheric backgrounds. GitHub-flow contribute model. Two valid unit-page layouts (marginalia for BASIC, sidebar for Assembly). Magazine-style Vault and Pattern entries.
- **2.1 (2026-01-19):** Updated unit counts; variable per-game unit counts.
- **2.0 (2026-01-07):** Complete rewrite for games/units model.
- **1.0 (2025-01-15):** Original — phases/tiers/lessons model.
