# Amiga language openings: source and execution-contract audit

The AMOS and Blitz openings have maintained examples and useful concrete
explanations, but their setup and evidence contracts need work before we can
qualify a beginner's route. The strongest next improvement is to pin and exercise
one real editor/runtime configuration per language, then revise the setup from
that evidence. No public lesson rewrite is proposed in this source-first slice.

This begins [#116](https://github.com/stevehill1981/198x/issues/116) under the
[education epic](https://github.com/stevehill1981/198x/issues/110), after approved
[docs #93](https://github.com/code198x/docs/pull/93) merged at
`4d846313e3ef3f400066d278c522186ecf99b7b7`.
The [plan](../../plans/2026-10-16-amiga-opening-audit.md) bounds the work.
The successful [Foundations delivery sweep](../2026-10-foundations-publication/REPORT.md)
retains its own scope; it does not qualify Amiga execution.

## What we inspected

[Source identities](source.json) retain website
`405c0594d30af56ecdfdc1ee4b6c119dead20ab7`, samples
`82ef057bcc31a5d6c27aadf4175073693798ab8a` and the docs baseline.
The inventory counts **17 AMOS units and 15 Blitz units**, plus a setup page
and module overview for each. The full-track file counts are not a review of
later content. We read ten selected pages: both setups, both overviews and the
first three units of each track. The [objective map](OBJECTIVES.md) records
what those units ask readers to do and what they explain locally.

All six CodeFromFile includes resolve. Each capture manifest names the matching
source file; each driver's complete typed payload matches that source exactly.
We inspected all six existing screenshots. They show the described greeting,
placed AMOS text, AMOS score/name, Blitz graphics and Blitz byte result. Those
are existing images, not fresh execution. Their source hashes are retained;
we do not copy them into another evidence bundle or infer a compiler identity
from the appearance of a CLI window.

The six manifests name `commodore-amiga-amos` or `commodore-amiga-blitz`.
They do not themselves identify CPU/RAM, ROM/OS hashes, editor/compiler version
or an observed pass/fail result. The drivers specify typing and key actions,
not assertions that the correct words or graphics appeared. The inspected
Build Amiga Assembly CI job processes `.asm` files; its success does not qualify
`.amos` or `.bb2` execution. Other historical runs may exist; no absence claim
about the whole family evidence library follows from this bounded inspection.

## Findings and priority

1. **[Pin the runtime and fix setup requirements](https://github.com/code198x/website/issues/766).** The Blitz setup recommends
   AmiBlitz3, an A1200/accelerated A500 and Kickstart 3.0+, without specifying
   the memory/library contract of the IDE it links. The pinned
   [upstream README](https://github.com/AmiBlitz/AmiBlitz3/blob/5dd815f880d72c5285b380ef3ddebfa5766d0626/README.md)
   specifies a 68020, at least 8 MB RAM, 35 MB disk and its Workbench/library
   requirements, explicitly for the IDE rather than generated programs.
   The course does not name a tested AmiBlitz release or establish that the
   original Ted controls and all examples transfer unchanged. This is a
   documentation mismatch, not a fresh observed startup failure.
2. **[Bind first greetings to actual execution](https://github.com/code198x/docs/issues/94).** Qualify unit 1 in each language
   using named versions, machine configuration and lawful media. Observe the
   maintained greeting, edited words and a deliberate syntax error/repair.
   Use this result to settle the setup contract before scaling to later units.
3. **[Qualify broad performance and representation claims](https://github.com/code198x/website/issues/767).** Blitz 1 says
   compiled code runs many times faster without a workload or measurement.
   Blitz 3 describes AMOS numbers as a universally big, safe box; the selected
   sample/captures do not establish that language-wide range or safety contract.
   Blitz 2 extends its OS trade to every Amiga game. Preserve concrete mechanisms
   while sourcing the actual language rules and qualifying historical/cost claims.
   No benchmark, hardware conclusion or contrary universal claim is supplied here.

[Filed findings](findings.json) retain the specific issue bodies and URLs.
We searched existing all-state website/docs issues for the selected setup and
performance subjects before filing. The new tasks divide setup correction,
first-greeting execution and bounded claim review; they do not duplicate a new
implementation plan inside #116 or require identical AMOS/Blitz lessons.

## Sources and acquisition limits

[Upstream records](upstream.json) pin the inspected README revisions and hashes.
The official AMOS source repository identifies its source licence as MIT; this
alone does not establish permissions or contents for every disk distribution.
The course's blanket public-domain/download wording therefore needs artefact-
specific checking when the setup is qualified. The linked Aminet page returned
`HTTP 403` to our web fetch. Its availability and package contents remain unknown;
we do not diagnose a broken learner download from that tool response.

No runtime, ROM, Workbench disk or new dependency was downloaded or installed.
The command `emu198x-amiga --version` returned
`zsh:1: command not found: emu198x-amiga`; the inspected Homebrew executable list
exposed only `emu198x-spectrum`. This is a bounded tool observation, not proof
that no Amiga runtime exists elsewhere on the machine. No Amiga build, editor,
boot or runtime was attempted in this slice. Execution outcomes are **unqualified**,
not failed. No redistribution permission is inferred.

## Outcomes and next step

| Evidence | Outcome |
| --- | --- |
| Selected source/objective review | Ten pages read, six opening units mapped |
| Include/manifest/typing consistency | Six exact matches |
| Existing screenshots | Six inspected; appearances agree with selected lesson results |
| Named source-to-runtime qualification | Not performed; follow-up owns two first greetings |
| Current setup compatibility | Upstream mismatch identified; learner reproduction untested |
| Runtime performance comparison | Not measured |
| Actual learner understanding/transfer | Unknown; no learner available |
| Browser, assistive technology, physical touch, audio | Not exercised |

The concrete next slice is the paired first-greeting execution task. It should
settle the usable setup before we edit more prose or design broader exercises.
A learner trial remains valuable when someone is available; the small public
first-session pack need not expand into Amiga until its route is qualified.
#116 and the education/UX parents remain open.

[Validation](validation.json) checks the immutable file inventory, six exact
capture payloads, sample inclusion, issue references and local links. It also
rejects a changed typing payload and incorrect source hash. These are evidence
checks, not runtime tests. [SHA256SUMS](SHA256SUMS) covers the retained files.
Run `python3 audit/2026-10-amiga-opening/verify.py --website PATH --samples PATH`.
