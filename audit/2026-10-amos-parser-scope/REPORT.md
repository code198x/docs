# AMOS parser scope research

This audit inventories existing text sources and identifies release/extension
questions for the [parser proposal](../../platforms/commodore-amiga/amos/parser-scope.md).
It does not implement a parser, test another AMOS release or establish language
compatibility. Research date: 20 October 2026.

## Sample inventory

`inventory.json` records 62 tracked `.amos` text files from samples revision
`b7f7dd9c07892f3c618ef52465772349887b4065`: 45 Bank or Risk files and 17 older
`meet-amos` files. Every file has a byte count, line count and SHA-256. Successive
game stages repeat constructs; occurrence counts are not independent test counts.
No binary native programs or runtime media are included.

`inventory.py` uses a reviewed list of statement-head candidates, masks quoted
text, counts selected symbols outside strings and notes lexical features. It is
**not an AMOS lexer or parser**. It cannot establish grammar, argument validity,
command availability, missing definitions or execution. Bare-name candidates
include procedure calls; strings may contain AMAL which the outer counts omit.
Its keyword list is not a proposed complete command set. Zero unclassified lines
means the inventory categories cover these sources, not that AMOS accepts them.

Reproduce against a clean checkout of the pinned samples revision:

```sh
python3 inventory.py /path/to/code-samples --check
```

The script resolves its recorded output beside itself. Without `--check` it
regenerates the JSON; review that change before committing. An empty source tree
is an error. A different revision or source hash makes the comparison fail.

## Primary evidence consulted

[sources.json](sources.json) records public source locations, precise locators,
text/source hashes where read and evidence status. Hashes of local manual text
identify the consulted extraction, not the original PDF. These are original
manuals/newsletters and published implementation material, not a new grammar
specification. The manual catalogue is available through the
[preservation project](https://gitlab.com/amigasourcecodepreservation/amos-classic-documentation).

| Evidence | Relevant finding | Limit |
| --- | --- | --- |
| AMOS Compiler guide, supplement “What's new in AMOS”, printed p. xi | Names 1.1, 1.2, 1.23 and 1.3 and describes changes. | Does not enumerate every later patch. |
| AMOS Pro guide, history 1.1 and Editor 4.1 | Names 1.21/1.34 and describes Check 1.3, bank limits and header choice. | 1.2/1.21 labels need reconciliation; a header is not a full release identifier. |
| AMOS Club newsletters 1x04, 1x05–06, 2x02 and 2x04 | Numbered extensions and pre-1.3 changes; names 1.32/1.34/1.36; reports a compiled 1.34 Wait Key failure. | Contemporary reports and adverts, not new native observations. |
| *Ultimate AMOS*, opening product comparison | Names Creator 1.35 alongside Easy and Pro. | A release lead, not a complete update history. |
| Easy AMOS guide, opening description | Establishes the separate product and its manual. | Release labels and command-level differences remain to research. |
| Pro Compiler guide, Quick Start and Updating, pp. 1–3 | Separates source-product acceptance from Pro 2.x editor integration. | Each original compiler release still needs identification. |
| TOME Series IV guide, introduction/installation | Independently versioned extension, added commands and missing-extension errors. | No TOME parser or runtime qualification here. |

The pinned official [1.12 news](https://github.com/AOZ-Studio/AMOS-Professional-Official/blob/533b4b1f5acd604814513f78e02c7b4796cb0531/AMOS/Accessories/AMOSPro_Help/LatestNews_112.Txt)
compares with 1.00 and distinguishes the old Compiler extension from Pro's later
compiler. The [2.0 news](https://github.com/AOZ-Studio/AMOS-Professional-Official/blob/533b4b1f5acd604814513f78e02c7b4796cb0531/AMOS/Accessories/AMOSPro_Help/LatestNews_200.Txt)
describes richer extension forms, a corrected string/integer test and an integer
multiplication fix. These motivate separate syntax, static-check and semantic
cases; we did not execute those cases in this task.

The same pinned source's
[version macro](https://github.com/AOZ-Studio/AMOS-Professional-Official/blob/533b4b1f5acd604814513f78e02c7b4796cb0531/%2BVersion.s),
[token table](https://github.com/AOZ-Studio/AMOS-Professional-Official/blob/533b4b1f5acd604814513f78e02c7b4796cb0531/%2BLib.s)
and [interpreter configuration](https://github.com/AOZ-Studio/AMOS-Professional-Official/blob/533b4b1f5acd604814513f78e02c7b4796cb0531/%2BInterpreter_Config.s)
provide implementation research starting points. No token table was promoted to
a grammar and no source was copied into a new implementation.

Author-owned [Unity releases](https://github.com/AmiDARK/AmosProfessionalUnity-Official-Releases/tree/c0293f1b9094022f31dfa1fd8b0a374c252cf1f8)
and [source](https://github.com/AmiDARK/AmosProfessionalUnity-SourceCode/tree/eaec8534f383ed8f7457cb43629ab5dbe080a55e)
were identified to keep later branches visible. This establishes repository
identity only. It is not a branch/release census or compatibility assessment.
The [AMCAF manual](https://www.ultimateamiga.com/HostedProjects/AMOSFactory/AMCAFguide/manual/miscellaneous.html)
provides another independently versioned extension candidate; its Audio Lock
section explicitly interacts with the supplied music extension.

## Verification and remaining work

The inventory comparison passes for the pinned clean source tree. A deliberately
changed recorded inventory is rejected, and an empty source selection is rejected.
All recorded source hashes are independently recomputed. Local proposal links,
JSON parsing, privacy constraints, Python lint/format and prose checks are checked
before commit. These checks qualify the research artefacts, not an AMOS parser.

The next approval is the implementation home and a bounded first parser design,
after strengthening Creator/Easy/release evidence. No new project, dependency,
shared parser framework, executable language implementation, native emulator
session or public lesson change was created. The learner setup/export work stays
open independently. There is still no uncoached learner result.
