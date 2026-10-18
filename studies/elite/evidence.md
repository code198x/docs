# Elite — evidence and limits

Research pass: 18 October 2026. Reader-facing scope: the original BBC Micro trading/flying experience, with the disc release’s mission distinction stated briefly. This is a substantial first reading draft, not historical sign-off or a complete played career.

## Executed artefact

The already-held `elite.ssd` fixture accompanying jsbeeb supplied the run. SHA256: `548dc8f36378d4f216bb882e465a4fa07474724fae2de8f3af4d08727019d6e6`. Its README identifies a fixed-up version of the disk posted by Ian Bell, correcting a docked/flight Bad command problem. This is not asserted to be an unmodified authenticated launch disk. No binary, disk, source or firmware is distributed.

jsbeeb 1.13.1, repository revision `7a2f543777ce6cdc220074fa7eaa9c163c0a356b`, BBC B-DFS1.2 configuration with its existing Video implementation. Headless Node runner imports its TestMachine/Video source without editing the vendor or installing dependencies. Audio is not captured. A 1024×1024 RGBA output framebuffer is cropped `(264,80,776,592)` to 512×512. This is the emulator’s rendered display geometry, not a claim that the BBC’s logical bitmap is 256 square pixels. No smoothing, compositing or retouching is applied.

Boot sequence: run six million CPU cycles; hold Shift, soft reset and run eight million, release Shift, then run 25 million. Answer N (100,000 cycles held, then 100,000 released), run five million; press Space, run one million. The new commander screen shows Lave, 100.0 Cr, 7.0 light years, Harmless, Clean, front pulse laser. Display market via host F7 (BBC f7), chart via F5 (BBC f5), and launch via host F10 (BBC f0). All keypresses use the same 100,000 held/released cycle pair. Market and chart each followed by one million cycles; launch by six million then a further ten million. The three retained images are market, chart and final front view. Cycle counts identify the bounded session; they do not establish input latency, original-hardware performance or every flight feature.

## Claim ledger

| Claim | Check and limit |
|---|---|
| Commander starting state and market/chart contents | Own bounded run, inspected images. Food 3.6 Cr/t, 16t available at observed starting market. Do not imply universal price/stock. |
| 12t costs 43.2 Cr, leaving 56.8 | Our arithmetic from the visible price; not a completed purchase or profitable executed round trip. |
| Launch, front view, monochrome world and coloured instruments | Own selected run/capture. No successful docking, fighting, trading circuit or mission completion claimed. |
| Controls, jump-drive mass blocking, equipment, trade relationships, weapons | Original guide sections and released manual text comparison. Preview-only items excluded: no claim of implemented anti-missile missiles, generation ships or every atmospheric lore statement. |
| Scanner and docking rules | Mark Moxon’s source analyses; analysed source and diagrams inspected, not independently instrumented flight measurements. Numerical tolerances deliberately omitted from main prose. |
| 256 systems, eight galaxies | Original cassette ELITED at `6ba1c7f633926501e687d9f1acfe76606e9467d7`: BASIC lines 1460–1470 chart loop uses 8-bit X wrap; line 4392 masks galaxy counter with 7. Inspection, not own execution of a universe generator. |
| Seed properties / model representation / split-screen | Moxon’s named analyses, cross-checked against visible display and original ELITED system-generation block where relevant. These are modern source analyses, not contemporary developer quotations. |
| Trading authorship | Segre’s 1984 account and Braben’s later FAQ differ; the study preserves uncertainty and joint authorship. No definitive allocation inferred. |
| Institution, support, testing | Segre’s contemporary interview; Braben’s attributed retrospective credit to Johnson-Davies. No invented contract, deadline or finances. |
| Price and achievement competition | Original Acornsoft advertisement in Acorn User 27, October 1984, PDF page 19 (a two-page advertising spread in the preservation file). BBC cassette £14.95, BBC disc £17.65. Distinguish preview review’s different prices. |
| Package fiction and contributors | Original guide’s 2015 preface; Acorn News December 1984 p.3. Bell qualifies Dugeon/Holdstock attributions as probable; study preserves that qualification. |
| Early reported sales | Segre: 13,000 within two weeks and a forecast, not an audited final total. Acorn News’s promotional later figure is not silently treated as independent corroboration. |
| Broader SF comparisons | Our comparison, not a creator-attributed influence claim. The accessed FAQ does not establish a specific film or Traveller influence on a particular feature; do not invent that chain. |
| Sound and later ports | BBC/C64 distinction in Moxon’s separate music analyses and existing Vault sources. No audio captured or distributed; no claim all classic Elites share one soundtrack. |

Original documentary texts were inspected from the authors’ preserved HTTP archive; an HTTPS alias has a certificate mismatch and was not fetched by disabling TLS checks. Public sources identify their original publications and the archive. Downloaded magazine/guide material remains research scratch, not part of this change.

## Imagery and review

Three small self-captured images illustrate specific criticism, with sufficient game/publisher/year/platform credits. [Capture manifest](captures/manifest.json) retains media identity, tool, transformation and output hashes. Their inclusion does not grant rights in Elite’s text or graphics. The original trading-loop diagram has wide/phone forms and describes relationships without prescribing a winning route. [Header provenance](artwork/provenance.json) labels an imagined scene; the illustrated ship and orbital port are not a reconstruction of the BBC game’s actual models.

No borrowed screenshot, complete map, full manual, game binary/source, audio, video or winning mission walkthrough is published. Owner reading, historical/editorial review and publication approval remain outstanding. Further full-game play would strengthen a later revision, but must not be claimed on the strength of this selected launch session.
