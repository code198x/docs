# Site imagery coverage and priorities

Imagery is uneven across the site. Lessons already contain substantial capture and visual-component work, while several prominent section openings and technical essays make readers reconstruct spatial ideas from prose and code. We should first correct two existing illustrations, then develop useful section introductions and a small explanatory-diagram tranche. A picture on every page or heading would not address those needs.

[Website tracker #802](https://github.com/code198x/website/issues/802) owns the new work. Existing biography imagery, machine-photo reconciliation and capture-readiness issues retain their scope.

## Scope and evidence

The source inventory covers **2,243 Markdown/MDX content files** at [website main 7412570](https://github.com/code198x/website/tree/7412570891a79c0485b3d894cefd4cf74eb924eb). It separately lists explicit image markers, Figure references, inline SVG/canvas markers and other component references. It strips frontmatter and fenced code; it does not expand components or infer image quality from file counts. It excludes Astro page/template files from those content totals; their important surfaces were inspected separately.

Live Chromium inspection covered **25 routes at 1440px and 390px**, including section entries, system pages, two technical essays and three actual lessons: **50 page loads**, all HTTP 200. The first twenty routes completed at 16:49 UTC on 16 October 2026; the teaching sample and defect follow-up were checked separately the same day. The browser evidence does not identify the deployed commit. Navigation prominence and explanatory need determine the priority here; traffic analytics were not available.

This is an imagery/content audit with bounded visual inspection, not a full accessibility, legal, performance or execution audit. A sampled canvas existing does not prove the experiment ran correctly. A screenshot or image count does not establish that an illustration is useful or accurate.

## Existing visual coverage

| Authored collection | Files | Files with image or Figure markers | Other relevant evidence |
|---|---:|---:|---|
| Curriculum | 605 | 333 | 291 reference Figure; 42 have direct image markers. Other files use diagrams, tables, bits/register components, experiments and players. These counts overlap. |
| Field Notes | 9 | 3 | Figure and FieldVideo references also appear. |
| From the Metal | 14 | 0 | CodeFigure presents code with captions; byte-order and bitmask articles have no separate spatial diagrams in the live sample. |
| Patterns | 71 | 0 | The template adds PatternExample to the progress-bar entry; an authored-body scan alone would miss it. One body references AssembleAndRun. |
| Timeline records | 44 | 0 | The Timeline landing template supplies illustrated stories independently of record bodies. |
| Updates | 15 | 0 | No blanket illustration requirement is justified for update text. |
| Vault | 1,485 | 9 | Eight reference Figure and one has a direct image marker; the current imagery checker accounts for 15 assets in nine manifests. |

Source marker totals are not rendered coverage percentages. A code/output comparison, trace table or live bit experiment may explain more than a raster image. Conversely, a figure containing only code may leave an address layout hard to understand.

### Prominent live surfaces

| Surface | Observed visual treatment | Audit disposition |
|---|---|---|
| Homepage | Eleven main-content images, including course results and four physical machines; three labelled SVG movement comparisons | Preserve the existing visual approach. No homepage-wide image replacement is needed. |
| Start Here | Two course-result figures | Preserve; consider only a specific navigation need later. |
| Systems | Four main physical-machine photographs plus catalogue/poster references | Reconcile remaining photo work in docs #10; do not recommission the existing four. |
| C64 and Amiga landings | A machine photograph and game capture each | Preserve subjects; repair the Amiga desktop overflow. |
| Foundations and Basics | Captioned pseudocode/output illustration, despite zero raster images | Existing visual explanation; not a missing-image defect. |
| Counting in Twos opening | Text-led module outline | Its first lesson has three figures; zero raster images at the opening is not evidence that the subject lacks visual teaching. |
| Pattern Library | A labelled three-state progress-bar illustration | Preserve the concrete-result concept, but correct its colours. |
| Timeline | Two main-content story images | Already illustrated at the entry point; no blanket picture-per-event task. |
| Craft | Prose, module lists and a seven-counter paper-game activity; no separate figure or diagram in the inspected page | Strong opportunity for a useful activity illustration and section introduction. |
| Maths for Games opening | Text-led module outline | Its first lesson is a prose/code experiment. Assess a specific explanatory need; the homepage already uses the dice capture. |
| From the Metal | Fourteen linked essay cards; no visual subject/example at the opening | A verified byte-order or bitfield figure could introduce what readers will investigate. |
| Demoscene | Text-led production/group/event directory | A specific captured effect would show the work the directory describes. |
| Curriculum | Text-led explanation of layers and routes | The route-map decision already belongs to docs #10; this audit does not adopt a map. |
| Setup, Teaching and Family | Mainly prose, lists and small icons | Later candidates where a workflow or relationship would materially help; photographs are not automatically needed. |
| Vault contents | Two feature captures and explained article connections | Preserve these; individual-subject imagery remains sparse. First history subjects stay in #801. |

The sampled Meteor Storm lesson renders a Spectrum screen canvas and magnified bitmap canvas. Its absence of an img element would be a particularly misleading reason to call it visually empty.

## Prioritised findings

### Correct the progress-bar illustration first

**Owner:** [#803](https://github.com/code198x/website/issues/803).

`src/components/PatternExample.astro` colours each filled cell by its position. At 50/100 the live illustration contains blue and yellow cells; at 100/100 it contains blue, yellow, red and white bands. The caption says the colours follow the listing.

The maintained `sinclair-zx-spectrum/patterns/basic/progress-bar.bas` instead chooses one colour for the whole filled portion: red for 0–9 lit cells, yellow for 10–18 and green for 19–28. The article explicitly describes those thresholds. Thus 50/100 should show fourteen yellow cells, and 100/100 twenty-eight green cells. Zero lights no cells. The misleading picture appears on both the Pattern Library opening and the individual pattern page.

Fix the visual model, include a low nonzero example, and check boundaries against the routine rather than pinning the current component values. Preserve the distinction between an illustration and an emulator capture.

### Keep the Amiga capture inside its column

**Owner:** [#804](https://github.com/code198x/website/issues/804).

At 1440px, `/systems/commodore-amiga/` has a 1499px-wide document. Its Flock figure, image and caption are 768px wide and extend to approximately x=1499.2. The 390px sample does not overflow. This is a confirmed media-layout defect; the fix should respect the capture's actual grid, aspect ratio, readable scale and bounded caption. Check sibling pages if a shared rule changes.

### Give section openings useful visual introductions

**Owner:** [#805](https://github.com/code198x/website/issues/805).

Start with Craft and Demoscene, then consider reusing the explanatory figure for From the Metal. The Craft's existing counter game supplies a concrete activity; a named published demo and specific effect supply a subject for Demoscene. Prepare a proposed treatment alongside or beneath the introduction, or as a linked result feature, within the current page design.

This explicitly includes section-header imagery. It does not require a photographic banner, image background or global change to every heading. `MagazineSectionHeading.astro` is currently a typography/intro component; changing it globally before selecting useful subjects would affect pages that already work well. Agree the bounded visual treatment before implementation, keeping headings, navigation and text alternatives useful when an image is unavailable.

### Publish three explanatory figures

**Owner:** [#806](https://github.com/code198x/website/issues/806).

- **Byte order:** show `$1234` stored at `$2000`/`$2001`, comparing low-byte-first and high-byte-first storage. The current essay supplies captioned code; the spatial address/byte comparison is the missing visual.
- **Bitmasks:** label the existing ULA byte fields and one set/clear operation, keeping unrelated bits visibly unchanged. Verify the technical mapping before drawing and inspect reusable existing bit/register components.
- **Craft counter game:** show the existing seven counters and a legal move, with the win/lose-last-counter rule change. Do not imply an optimal strategy that the illustration has not established.

Generate factual values from the model, preserve text equivalents and source qualifications, and reuse the Craft figure for the opening where appropriate. Static figures can satisfy this scope; new interaction needs an agreed reason. Later rendering-pattern result images remain candidates rather than a requirement to illustrate all 71 entries.

## Reused work and duplicate checks

Open and closed issue inventories were read for the website and docs repositories (268 website issues and nine docs issues returned). Titles and bodies were checked for images, photos, diagrams, headers, section entries, discovery and related work. The recent #800 PR already owns the credit/cross-link edits; it does not own imagery implementation.

| Existing owner | Relationship to this audit |
|---|---|
| [Website #801](https://github.com/code198x/website/issues/801) | First biography/theme imagery and the recorded Hamilton/Johnson/Vaughan shortlist. Keep its licensing, portrait-policy and permission distinctions. |
| [Docs #10](https://github.com/code198x/docs/issues/10) | Physical-machine image scope/rights/design reconciliation, syllabus summaries and the undecided curriculum route map. Four core machine photos now render; reconcile those remaining checkboxes with current evidence rather than duplicating sourcing. |
| [Docs #3](https://github.com/code198x/docs/issues/3) | Execution/capture readiness for six next-tier machines, with per-configuration verification. A visible poster is not a completed authoring/capture workflow. |
| [Website #798](https://github.com/code198x/website/issues/798) | The two initial Vault reading paths; coordinate any feature imagery with those selections. |
| [Website #749](https://github.com/code198x/website/issues/749) | First-session verification beyond Chromium viewport checks. This audit's desktop/phone layout observations do not close it. |
| [Closed website #411](https://github.com/code198x/website/issues/411) | Existing byte-to-hex illustration work. Reuse its implementation where suitable; do not recommission that same figure. |

No existing open issue was found owning the progress-bar colour mismatch, the specific Amiga capture overflow or the bounded opening/three-figure tranche. [#802](https://github.com/code198x/website/issues/802) has four native child issues, all read back with reciprocal parent links.

## Verification and limits

All sampled pages returned 200. The low naturalWidth values initially observed on five system posters were checked independently: BBC Micro, MSX, CPC, VIC-20 and Master System poster URLs all returned **200**. The catalogue disclosure was closed; lazy or hidden images are not evidence of missing files. They were not reported as broken images.

The existing Vault imagery checker passed: fifteen images across nine manifests. The scoped Impeccable detector returned no findings for the inspected homepage, Craft, Curriculum and section-heading component; it cannot measure editorial usefulness or catch the verified factual mismatch by itself.

The inventory's component-aware counts, fifty live observations, poster requests, actual progress-bar colours and Amiga overflow are saved with this report. Screenshots of the [Craft phone page](craft-390.png), [From the Metal desktop page](from-the-metal-1440.png) and [progress-bar page](progress-bar-evidence.png) preserve representative visual evidence. The Craft and From the Metal screenshots were visually inspected. No whole-site build, new image acquisition, website implementation or publication is claimed by this audit.

Reproduce the source-marker inventory with `node inventory.cjs /path/to/website` from this directory. The script records the checkout revision and writes `content-inventory.json`. Its literal-marker limits above are deliberate; verify proposed gaps against their components and rendered pages before commissioning a visual.
