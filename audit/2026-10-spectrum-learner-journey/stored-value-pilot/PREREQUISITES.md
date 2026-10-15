# Stored-value prerequisite map

Source inspection: 15 October 2026, website
`290146661779c23562c089adf61b71ee50d693d4`, samples
`e3cf3694b7122adb5f383029a3c9e8c33c9d784b`. This map describes authored
explanations, not measured learner comprehension. File paths below are relative
to the website's `src/content/curriculum/` unless stated otherwise.

| Surface and file | Knowledge used | Explained locally | Useful earlier support |
| --- | --- | --- | --- |
| Foundations `basics/unit-03.mdx` | Instruction order, quotation marks, simple addition | Literal text versus calculated value; `SHOW` joins with comma, adding no space | Basics units 1–2 introduce instructions and sequence. |
| Foundations `basics/unit-04.mdx` | Sequence, `SHOW`, text/value distinction | Variable name, assignment, replacement, stable name and changing contents; trace table | Unit 3 explains output punctuation. The final link leads to Meet BASIC lesson 2. |
| BASIC `sinclair-zx-spectrum/basic/meet-basic/unit-02-remember-and-save.mdx` | Enter/run/edit numbered lines; keyboard symbols for manual target entry | Complete greeting; `LET`, string and `n$`, literal versus variable, `PRINT` semicolon, missing-name report; source/tape/snapshot distinctions, save/reload | Opening lesson and module keyboard table are linked. Foundations units 3–4 are linked as optional explanations, with punctuation differences stated. |
| Assembly `sinclair-zx-spectrum/assembly/meet-assembly/unit-02.mdx` | Assemble/run, register A, address, `ld`, labels, hexadecimal, hold loop | Bit/byte, `%` binary, `defb` assembly-time emission, memory-read/write parentheses, bitmap and attribute addresses, separate copies, replacement write | Lesson 1 defines host/target, assembler/machine code, A, addresses, labels, `org`, `jr` and source versus bytes; no BASIC dependency. |
| Vault `techniques/variables-memory.mdx` (under `src/content/vault/`) | Addresses, pointers, byte sizes, BASIC dialects, arrays, heaps and collection | Specific C64 and Spectrum storage layouts with sources and examples | Optional depth after the core objective. Its detailed implementation discussion is unsuitable as a required first explanation of variables. This suitability assessment is editorial inference, not a learner observation. |

The shared objective is read/replace reasoning, not a claim that all three
surfaces use the same storage model. In Foundations, a variable is an explanatory
named box. BASIC looks up a language variable. An assembly label names an
address; loading A copies a byte, and storing A writes to a separate destination.
Changing one copy does not automatically change the others.

## Confirmed finding and limits

[Website #689](https://github.com/code198x/website/issues/689) covers the false
claim that showing a value makes the computer forget it. It appears in unit 3's
transition and unit 4's introduction. The existing unit 4 trace and BASIC/assembly
examples already require stored values to remain available after reads.

The correction should explain retention directly, then ask for a prediction
before revealing a repeated-read/replacement trace. A green build would establish
that this renders; it would not establish that learners understand the model.

No new blocking dependency between the three routes is justified. Do not add
Foundations as a gate or force this advanced Vault article into the beginner
sequence. Whether an optional link to a shallower reference would help remains
a learner-research question, not a confirmed navigation defect.

This samples Basics only. The wider #114 work still needs objective/prerequisite
coverage for numbers/bits, logic, game maths and other shared modules. Assembly
lesson 2 uses bit representation, but this pilot does not audit all binary or
hexadecimal teaching by implication.
