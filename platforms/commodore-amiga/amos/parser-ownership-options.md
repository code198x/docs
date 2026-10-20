# Where the language tools should live

**Recommendation for discussion, 20 October 2026.** Give the language tools a
standalone sibling home, with Code198x as the first consumer. Its name and repo
have not been chosen. This is an ownership proposal, not an adopted family rule,
a request to create an organisation or a parser implementation design.

The demand now includes AMOS versions and extensions, later Blitz, and the same
approach for other languages. The useful product is language analysis even when
it emits no runnable program. That responsibility should remain independently
usable by curriculum checks, future editor tooling and later compilers.

## Existing decisions that matter

- The [Build198x BASIC decision](https://github.com/build198x/build198x/blob/f7016398deb1fff9dc1efb6713dfab8c7bacf2d0/decisions/demand-gate-basic.md)
  already supplies listing conversion/linting and explicitly leaves parser and
  language-server ownership to a later specification. Its
  [specification](https://github.com/build198x/docs/blob/e0956f3c630f1c462196e5bf9612687014e1aac2/specs/2026-09-26-basic-verb.md)
  anticipates lossless per-dialect trees and editor diagnostics. This is related
  demand to reconcile, not evidence that a parser already exists there.
- The [Asm198x infrastructure direction](https://github.com/asm198x/asm198x/blob/47fc51643eb98ecdd5ef2f64cfc5035bee52997e/decisions/llvm-alike-legacy-assembly-infrastructure.md)
  anticipates future frontends and reusable machine/artifact layers, but
  explicitly does not decide a higher-level compiler frontend or a new crate.
  Its current instruction/assembly AST is not automatically an AMOS tree.
- The [Build198x boundary](https://github.com/stevehill1981/198x/blob/main/decisions/build198x-build-tools.md)
  is converting, packing and mastering machine-ready data/media. Tokenising
  authored BASIC fits its adopted conversion lane; source analysis alone needs
  an explicit decision rather than being added because it is tooling.
- [Forge198x](https://github.com/stevehill1981/198x/blob/main/decisions/forge198x-ide.md)
  is a deferred workbench consuming tool backends. Choosing a language engine's
  home does not open the IDE project.
- The [general-tools principle](https://github.com/stevehill1981/198x/blob/main/decisions/family-tools-are-general.md)
  makes the curriculum a priority consumer, not a correctness boundary.
  [Format graduation](https://github.com/stevehill1981/198x/blob/main/decisions/formats-graduate-to-their-own-projects.md)
  remains relevant to a later tokenised-file codec; it does not assign source
  language semantics to Format198x now.

## Options

| Home | Why choose it | Cost and conditions |
| --- | --- | --- |
| **Dedicated language-tooling sibling — recommended** | Gives parsing, release/extension profiles, diagnostics and later language semantics one explicit owner across languages. Consumers can use analysis without an assembler, emulator or course checkout. | Requires an umbrella ownership decision and a name/repo choice. It must earn any shared internals through actual language needs; a new home does not justify a universal grammar, IDE or runtime. |
| Asm198x, with an explicit frontend scope decision | Could put eventual code generation near reusable machine/layout/artifact layers. Existing source/diagnostic facilities are worth assessing. | Parsing is useful before code generation. The current direction leaves higher-level frontends undecided; adopting this home needs a clear public scope and dependency boundary. Do not force AMOS into assembly AST nodes. |
| Temporary Code198x implementation | The first consumer and current corpus already live here; a disposable research experiment could start with little organisational work. | Curriculum ownership is a poor permanent boundary for general language tools. Extraction becomes necessary as tools acquire independent consumers. Keep research records here, but avoid shipping a permanent parser hidden in sample or audit scripts. |

Build198x and Format198x remain potential consumers/providers at their existing
conversion/format seams. No move of the current Spectrum/C64 lint or tokeniser
code is proposed. Emu198x continues to execute machines and provide independent
original-runtime observations; it need not depend on the host parser to boot.

## Recommended first boundary

The dedicated tool would own language-specific text parsing and diagnostics,
release/extension profiles and comparison cases. Preserve source locations and
unsupported/unknown distinctions as the [scope proposal](parser-scope.md)
requires. Decide packaging and a first AMOS implementation design after ownership
is agreed; this document does not pick a parser framework or dependency.

Code198x keeps lessons, maintained teaching samples and teaching checks. Shared
language acceptance cases must be independently useful beyond those listings;
reuse or reference corpus inputs with explicit ownership rather than creating
competing canonical copies.

A future compiler may consume Asm198x's machine/artifact layers if a concrete
lowering experiment shows they fit. An interpreter has a separate runtime
contract. Neither future justifies coupling the first parser to an assembler
pipeline or constructing a cross-language intermediate representation now.

The recommendation would change if an independently useful frontend experiment
showed that Asm198x's existing reusable seams already fit the analysis product
without assembly coupling. Inspect that evidence before duplicating facilities.

## Decision needed before implementation

Choose between a dedicated language-tooling sibling and an explicit Asm198x
frontend scope. The temporary Code198x option is available for research, not my
recommended shipping home.

An adopted choice affects sibling responsibilities, so record it in the umbrella
`decisions/` layer and route the relevant project contexts to it. Update the
BASIC parser/LSP planning reference there as part of the design; do not quietly
start a second unrelated parser programme. Repository creation, dependencies,
implementation design and any old-code migration remain subsequent explicit
steps. The [reference candidates](reference-profiles.md) can be investigated
independently while this decision is pending.
