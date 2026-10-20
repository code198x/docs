# AMOS parser: versions, extensions and first deliverables

**Status: research proposal, 20 October 2026.** We want useful source analysis
before committing to execution or code generation. The research covers the AMOS
family, its releases and extensions. The first delivery can be smaller, with its
limits stated. No parser, interpreter or compiler is implemented by this proposal.

The same investigation method should apply to other languages. AMOS comes first;
Blitz follows as an independent language investigation. Shared implementation is
an option to earn through evidence, not a prerequisite.

## What a parser would give us

Read source into a syntax tree: a structured representation of statements,
expressions and blocks, with locations in the original text. Keep spelling,
comments and spacing available so diagnostics can point to what a learner typed.
A syntax tree alone need not preserve that material; retain source spans and tokens or
a concrete representation alongside it.

That enables listing checks, command inventories and later editor feedback. A
separate curriculum check could compare used constructs with what a lesson
introduces. Parsing alone cannot prove that a program runs, teaches well or uses
a supported command on a particular installation.

Offer separate results for:

- **Syntax:** can we structure the text, including incomplete editing input?
- **Static checks:** do commands, types, blocks and names satisfy the selected
  installation's rules, to the extent implemented?
- **Compatibility:** which named releases/extensions have evidence for this use?
- **Execution:** what the original runtime or compiler accepts and does.

A successful syntax result must not imply the other three passed. Unsupported
syntax and unknown compatibility need distinct results from invalid source.

## Describe an installation, not just “AMOS”

Record product/branch, exact release label, language/library component revisions,
interpreter or compiler mode, installed extensions and source representation.
Keep machine/OS details with runtime observations. Preserve literal version
labels; do not compare them as decimal numbers or assume chronological ordering.

A profile records each extension's identity, release, target product, component
hashes where available, configured number/order and evidence. A slot number is
not an identity. A label without a verified binary is a documentation claim,
not an executed reference installation. Do not infer the originating release
from a `.amos` suffix, a compatible header or commands shared by several releases.

If no exact profile is supplied, give candidate profiles and uncertainty. Never
silently select the newest Professional release. Unknown patch levels remain
unknown; evidence for one build does not fill every neighbouring release cell.

## Initial release ledger

This is a sourced starting ledger, **not a complete release catalogue**. Every
identified release should eventually have its own record, even when no language
change is known. Do not manufacture missing versions to fill a numeric sequence.
The source register in the [research audit](../../../audit/2026-10-amos-parser-scope/REPORT.md)
gives precise locators and separates observations from documentation.

| Product or branch | Evidence found | What remains to establish |
| --- | --- | --- |
| AMOS / The Creator 1.1 | Original compiler supplement calls it the original release; Pro's history dates its launch to June 1990. | Exact distribution identity and native acceptance baseline. Earlier labels, if found, need their own evidence. |
| Creator 1.2 and 1.21 | Compiler supplement groups flipping and bank changes under 1.2; Pro history names 1.21. | Reconcile those labels against disks/update notes. Do not treat them as synonyms. |
| Creator 1.23 | Compiler supplement identifies serial extension and utilities. | Exact bundled component versions and extension syntax. |
| Creator 1.3 | Compiler supplement documents the release and changed drawing/copy behaviour. | Native comparison with earlier releases and compiler variants. |
| Creator 1.32, 1.34, 1.36 | Contemporary AMOS Club newsletters name these releases. Pro history also names 1.34. | Verify each binary and update chain. The newsletter's reported 1.34 compiled `Wait Key` crash is a reproduction lead, not our observation. |
| Other Creator patch releases, including 1.35 | 1.35 is named in *Ultimate AMOS*; the current ledger is incomplete. | Acquire/reconcile original update notes; enumerate surviving patches and regional distributions without guessing. |
| Easy AMOS | Original 1992 guide defines a distinct product. | Establish release/build labels, command set, extension support and limits independently; it is not an alias for Creator or Pro. |
| AMOS Professional 1.00 | Pinned official 1.12 news explicitly compares with 1.00. | Identify the original distribution and probe its accepted forms. |
| Professional 1.12 | Official news details additions, fixes and manual corrections. | Convert the relevant changes into isolated acceptance/type/runtime cases. |
| Professional 2.00 / 2.x | Official version source says 2.00; 2.0 news describes changes; compiler guide requires a 2.x upgrade. | Reconcile release label with actual component hashes; audit differences rather than treating all Pro releases as one dialect. |
| AMOS Compiler and Pro Compiler | Separate original manuals. Pro Compiler accepts source from Creator, Easy and Pro, with an editor integration requirement for Pro 2.x. | Track compiler releases separately from source dialect and interpreter release. A compiler accepting source does not prove the Easy editor accepts it. |
| Later AMOS Professional derivatives | Author's AMOS Professional Unity release/source repositories are identified and pinned in the source register. | Catalogue branches, releases, fixes, syntax and extension ABI changes. They need distinct profiles, never automatic equivalence to original Pro 2.00. |
| Other descendants or ports | Reserve explicit lineage records when identified. | Distinguish an Amiga release from a related language or host reimplementation. Do not imply STOS or AOZ compatibility from ancestry. |

All original product lines belong in the investigation from the start. The
checked native baseline remains Professional 2.00; no Creator/Easy compatibility
trial was performed for this proposal. Later derivatives stay visible in the
ledger, with implementation breadth decided after their evidence is gathered.

The follow-up [reference installation plan](reference-profiles.md) separates
sixteen inspected media candidates from the previously executed Pro 2.00
profile. It retains filesystem failures, installer dependencies and a startup
script difference rather than treating media availability as qualification.
[Lang198x ownership](parser-ownership-options.md) is now agreed, including
language services/LSP. The umbrella decision owns that boundary and the review
gates for moving existing functionality.

## Differences worth testing first

The original documents already give concrete reasons to retain release identity:

1. Creator's compiler supplement records new command facilities in successive
   releases. Pro's editor also has a “Check 1.3” operation checking commands and
   banks above 16, and chooses a compatible file header. That header is not a
   complete declaration of the installation that wrote a file.
2. Pro 2.0 news describes a more capable extension system, including reserved
   variables and floating-point parameter forms. It also documents an erroneously
   accepted string/integer use and an integer multiplication fix. Syntax,
   static checking and execution can differ independently.
3. The AMOS Club's extension guidance describes number conflicts and changes
   before 1.3 that can shift later extension commands. Preserve this as a
   contemporary report to verify against the exact tokenised formats/runtime.
4. The original Pro Compiler guide distinguishes source acceptance from editor
   integration. Some examples can compile even when the Easy editor cannot run
   them. “Works with the compiler” is therefore a separate compatibility claim.

Record a minimal source, exact installation, accepted/rejected result, reported
location and any observable output for each case. Do not label old behaviour
corrected because a newer release behaves differently. Start with syntax
probes; a runtime discrepancy belongs in the semantic corpus, not a parser hack.

## Extensions are part of the language surface

Include the supplied Music, Compact, Requester, I/O and Compiler components as
well as third-party extensions. The pinned Pro configuration names these files;
Pro 2.0 even treats its main instruction set as an extension internally. A
“base language” profile must state which supplied components it includes.

For each extension, research keywords and aliases, statement/function/reserved
variable forms, argument types and omissions, result types, embedded languages,
release differences, product support, configuration number/order, dependencies,
conflicts and evidence/licensing. Syntax definitions must distinguish a known
but disabled extension from an unknown word. Do not load arbitrary extension
code into a host parser to discover its commands.

Use source/manual data to build declarative descriptions where it fits. Keep a
route for language-specific grammar when a signature list is insufficient.
Preserve ambiguous parses or report the conflict until native resolution is
known; “longest keyword wins” is not a substitute for AMOS's rules.

Early extension cases should include a supplied component and an independently
versioned extension such as AMOS 3D, TOME or AMCAF. This is a test-selection
proposal, not a claim of support for any of them. Test each with the extension
absent, present, mismatched and conflicting. Keep the base corpus usable without
third-party additions. Unknown token identities must remain recoverable if a
later file decoder encounters an unrecognised extension.

## Actual sample demand

The [reproducible inventory](../../../audit/2026-10-amos-parser-scope/inventory.json)
covers **62 tracked text sources** at samples revision
`b7f7dd9c07892f3c618ef52465772349887b4065`: 45 Bank or Risk sources and
17 older `meet-amos` sources. Counts include successive versions of the game;
they are not 62 independent language cases. The inventory measures textual
candidates and hashes, not valid syntax or compatibility.

| Surface | Existing examples | Parser work it motivates |
| --- | --- | --- |
| Opening messages | `stages/opening/message.amos`, `edited-message.amos` | Quoted strings, multiword `Wait Key`, command arguments and statement boundaries. |
| Choices and game state | `stages/opening/one-round.amos`, session stages | Numeric/string variables, suffixes, precedence, comparisons, nested `If`, `Repeat`, labels and `Gosub`/`Return`. |
| Shared drawing and text | Presentation and arcade stages | Coordinate pairs with `To`, optional command forms, hex colours, arrays, functions, nested `For` loops, buffer and font commands. |
| Sound | Cue stages and older `unit-15/sound.amos` | Distinguish `Play` from `Play Off`; `Set Envel`/`Wave` argument forms and ordinary `Wait` from `Wait Vbl`/`Wait Key`. |
| Procedures | Older `unit-06/divider.amos` | A bare procedure call as well as `Procedure`/`End Proc`; bare names cannot all be treated as unknown commands. |
| Animation | Older `unit-13/amal.amos` and `unit-17/theamosway.amos` | AMAL text inside strings, separate from the outer BASIC grammar. |

These examples order work. They do not define the whole valid language or
justify accepting only their exact spellings/argument shapes. Independent cases
must cover valid variations, boundaries and failures, including features absent
from the current samples.

## Input and embedded-language boundaries

Start with plain-text program listings. Specify encoding, line endings, tabs,
case, identifier characters, numeric notation, comments, quotes, separators and
location units before code. Keep byte offsets and displayed line/column mapping
explicit, including non-ASCII input and malformed encoding. The inventory's
UTF-8 source files do not establish the Amiga's source character rules.

Native tokenised `.AMOS` programs are a separate decoder/encoder surface:
headers, tokens, line records, banks and extension identities need independent
research and round-trip/error tests. Detect format by content plus declared mode;
do not send binary native files through the text parser because our text samples
share their suffix. Unsupported binary input needs a format diagnostic.

AMAL and Pro Interface are separate grammars, often carried in strings or banks.
Initially retain their source as opaque text and explicitly say embedded syntax
is unchecked. Later validate only recognised call sites/resources, preserve
inner-to-outer diagnostic locations and keep ordinary strings as data. Dynamic
string construction can make full static validation impossible; report that
limit. A valid AMOS wrapper does not validate the embedded program.

## Bounded delivery sequence

1. **Release and extension evidence.** Expand the ledger into component-pinned
   profiles. Establish Creator, Easy and Pro baselines and representative release
   differences. Label missing binaries/documents. Use the agreed Lang198x home
   and agree the first implementation design before adding code or dependencies.
2. **First useful text parser.** Propose the opening program surface with located
   syntax trees and explicit unsupported cases. Include valid variations and
   deliberately malformed input, not only our two message listings. Establish
   how incomplete edits recover without silently certifying the whole program.
3. **Grow to Bank or Risk.** Add each required construct with independent tests,
   then cross-check the unchanged maintained stages. Add static checks separately.
   Introduce version differences and a supplied-extension case early, before
   declaring one universal AMOS grammar finished.
4. **Show extension and release separation.** Add a selected third-party
   extension and older-release rejection cases. Test absent/unknown/conflicting
   profiles and keep unsupported/invalid results distinct.
5. **Broaden coverage.** Cover remaining original releases, library variants,
   native formats, embedded languages and selected derivatives in evidence-led
   increments. Publish a coverage matrix; never call partial support “all AMOS”.

For every supported construct, require an independent original implementation
comparison, boundary cases and a negative control that can fail. A parser may
accept valid syntax that fails at runtime; record that distinction. Where native
media is unavailable, label the result source/manual-checked, not executed.
Source/table extraction and native observations are complementary evidence.

Do not make the lessons wait for a host interpreter. Original AMOS remains the
execution baseline. Lang198x is the agreed owner; a parser framework, package API,
repository layout and implementation estimate have not been selected. The
umbrella decision also requires reviewing the existing Spectrum parser and
BASIC diagnostics before any migration, rather than creating competing copies.

## Blitz and other languages

After the AMOS evidence/profile work and first useful parser, make the same
bounded inventory for original Blitz BASIC releases, Blitz BASIC 2 and AmiBlitz,
including their libraries, resident definitions, macros and source formats where
applicable. Verify these facilities/version boundaries from their own manuals
and source. Existing AmiBlitz 3.13.0b evidence does not establish Blitz BASIC 2
compatibility, and an AMOS extension model must not be imposed on Blitz.

Reuse the method: inventory, release ledger, extension/dependency profiles,
located syntax, independent acceptance cases, explicit coverage and original
execution. Share code only where two implementations show a real common need,
such as diagnostic locations or corpus reporting. Do not design a universal
BASIC grammar or extension ABI in advance. Later interpreters/compilers remain
possible consumers, with their own semantic and runtime requirements.
