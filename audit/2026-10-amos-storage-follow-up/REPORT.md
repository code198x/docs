# AMOS storage after the live disk-change fix

Native persistence of `stages/arcade/styled-board.amos` is verified on the
fixed Emu198x source `6ff929f366e8762d5d5b9dadf53367b2cc692821`.
This is a revision-specific follow-up to the
[complete-frame audit](../2026-10-amos-bank-or-risk-complete-frames/REPORT.md),
whose pinned pre-fix storage failure remains valid evidence.

The [immutable native record](https://github.com/emu198x/docs/tree/a35897e2b965b6ec20063d4e2749bce1d412b1cf/plans/2026-10-19-amiga-native-save-investigation/fix) retains exact requests, drive/CIA queries,
validator output, source/binary identities, captures and test logs. The source
fix is [Emu198x #1881](https://github.com/emu198x/emu198x/pull/1881), addressing
[#1877](https://github.com/emu198x/emu198x/issues/1877). It awaits review/merge;
version 0.34.2 alone does not identify the fixed build.

## What is verified

The same stock PAL A1200, 2 MiB chip RAM, no fast RAM and lawful AMOS
Professional 2.00 runtime save the full 17,734-byte native program onto a
separate empty OFS data disk. Generic `load_media` is used throughout.
`verify` and `manifest` pass, and the saved program and disk equal the previous
successful explicit-notification control byte for byte.

An independently cold-booted editor loads the saved file, reports no syntax
errors, and runs it. Returning the requested system disk allows runtime/font
access to complete. The game rolls six and banks six. Seven captures match
the successful control exactly. Original ROM and runtime hashes are unchanged.

The defect was in live insertion policy: generic loading acknowledged
/DSKCHANGE before the guest could observe it. The drive already modelled the
signal. The fixed runtime preserves notification after execution starts and
retains startup, reset and snapshot behaviour. This does not qualify every
Amiga variant or all disk-writing workloads.

## What remains separate

The original full verifier still rejects its recorded pre-fix filesystem.
Do not turn that historical failure green or relabel its captures. Use this
follow-up for the current endpoint's persistence claim and the earlier record
for rendering, sound and game cases it ran.

The native audit uses scripted host tools for disk insertion and export.
Those tools establish authoring verification, not a beginner-ready desktop
export workflow. A learner on an emulator must know how their host retains
and exports modified disk images before ending the session. An emulator
snapshot alone does not test native program persistence.

Authored lesson drafts, human presentation/listening acceptance and an
uncoached learner trial are separate from these storage and execution checks.
No public lesson or released-runtime claim follows from this record.
