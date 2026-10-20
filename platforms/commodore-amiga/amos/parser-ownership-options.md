# Lang198x owns the language tools

**Ownership agreed, 20 October 2026.** Steve registered Lang198x and included
language-server tools in its scope. The adopted cross-project boundary lives in
the [umbrella decision](https://github.com/stevehill1981/198x/blob/dd9bdfa0cf272fb87763c15afa45f6b35e0978e2/decisions/lang198x-language-tools.md).
That record is the authority; this page routes the AMOS research to it.

Lang198x is the home for language frontends, analysis, release/extension profiles
and language services, including LSP delivery. Code198x consumes the tooling;
Forge198x can consume its services as the future workbench. A first AMOS parser
and language server still need their own bounded implementation designs.

The [migration inventory](https://github.com/stevehill1981/198x/blob/dd9bdfa0cf272fb87763c15afa45f6b35e0978e2/docs/brainstorms/2026-10-20-lang198x-migration-inventory.md)
identifies existing Spectrum AST/parser code in Format198x and language-oriented
BASIC linting in Build198x as candidates for assessment. Existing tokenised-file
codecs, build conversion and assembly semantics retain their current owners.
The decision does not move code, change published APIs or require a family-wide
reorganisation before AMOS work can progress.

The [reference candidates](reference-profiles.md) and [parser scope](parser-scope.md)
remain the AMOS investigation inputs. Their native qualification and syntax
coverage gaps remain open; choosing an owner does not fill them. Current parser,
protocol, package and repository implementation choices are still to make.
