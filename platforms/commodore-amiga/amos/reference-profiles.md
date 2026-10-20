# AMOS reference installations: candidate set

**Research result, 20 October 2026.** We have one previously exercised native
installation: AMOS Professional 2.00. This pass identifies other candidate media
and checks their bytes read-only. It does not boot, install or qualify them.

The [parser scope](parser-scope.md) includes all original product lines and
release differences. A candidate below is a place to start obtaining evidence,
not permission to treat its label as an observed release version.

## First installation set

| Priority | Installation to establish | Present evidence | Next check |
| --- | --- | --- | --- |
| 1 | The already-tested Pro 2.00 profile | Editor version and typed/edit/repair/save/cold-load evidence exist. Original file bytes survive on the valid reconstructed system disk. | Retain the exact profile and start isolated syntax probes on fresh work copies. |
| 2 | Creator 1.36 | Candidate disk with recorded component hashes. Filesystem checker rejects its allocation bitmap. | Establish the release from the running environment and compare with manuals; qualify a working copy without writing to the source. |
| 3 | Easy AMOS 1.01 | Master Disc 1 candidate passes the filesystem check. It contains an installer and split `Disc1_*` payloads, not an installed environment. | Inspect the installer and required companion media, reconstruct an installation, then observe the version and editing loop. |
| 4 | Creator 1.1 and Pro 1.00 | Earlier candidate distributions have recorded component hashes; both fail filesystem checks. | Establish original-release baselines for later command and extension comparisons. |
| 5 | Pro 1.12 and update candidates | Candidate system and updater disks exist; updates are not complete installed profiles. | Establish the update chain and component identity, including the separately labelled 1.11 update. |
| 6 | AMOS Compiler 1.0 and Pro Compiler 2.00 | Compiler-labelled media are identified. Compiler 1.0 passes the filesystem check; the Pro Compiler disk does not. Neither was executed. | Establish installed compilers and compare source acceptance independently of editor acceptance. |

Creator 1.2, 1.31, 1.32, 1.34 and 1.35 candidates are also recorded. They remain
in the release comparison queue rather than being represented by 1.36. The new
1.31 and Pro 1.11 labels come from media/catalogue metadata; native and release
note reconciliation is pending. This is a bounded selection, not an exhaustive
survey of all patches, distributions, regions or later branches.

Do not collapse a numbered release into “latest AMOS”. Build one recorded
installation per evidence claim, including a compiler's independently identified
version and its dependencies. Two media with the same product/version label can
still launch different environments.

## The existing Pro 2.00 reference

The [executed baseline record](../../../audit/2026-10-amos-reference-profiles/executed-baseline.json)
retains original and working-disk identities and all 78 file hashes. Its execution
claims come from the immutable
[first-pair native audit](https://github.com/code198x/docs/blob/ffa0239359d982a55a985314f6a7f59be4527534/audit/2026-10-amos-first-lesson-pair/REPORT.md),
not a new runtime trial. That audit names emulator source
`6ff929f366e8762d5d5b9dadf53367b2cc692821`, PAL A1200, 2 MiB chip RAM, no fast
RAM and the Kickstart hash. A version label alone does not identify this build.

The source disk fails the filesystem check with:

```text
bitmap block 396: non-existent block 1768 is marked free
```

The reconstructed disk passes, and an independent comparison confirms that all
78 original files remain byte-identical. Its disk hash differs because its
filesystem layout differs. These results do not authorise silently replacing an
archival input; keep source media immutable and record the working copy's origin.

The configuration contains names for `AMOSPro.Lib`, Music, Compact, Requester and
I/O libraries. Their identities are recorded; string presence is not proof that
every command or extension path has executed. Earlier native sound cases are
separate evidence. No compiler or third-party extension qualification follows
from these observations.

The separately inspected Pro 2.00 candidate has the same 78 filenames. **77 files
match the tested distribution; `s/Startup-Sequence` differs.** See the
[distribution comparison](../../../audit/2026-10-amos-reference-profiles/pro-2.00-distribution-comparison.json).
Do not transfer the complete boot/input qualification to that candidate
because the executable/library files match. Startup, configuration and host keys
are part of a repeatable reference environment.

## What the candidate checks establish

The [candidate record](../../../audit/2026-10-amos-reference-profiles/candidate-media.json)
identifies 16 ADF payloads by SHA-256 and records selected component hashes. ZIP
CRC and supplied catalogue size/CRC/SHA-1 agree for each selected payload. This
establishes byte identity against those records, not authenticity, licensing,
freedom from malware or working language behaviour. Product labels and dates in
catalogue metadata have not been promoted to release-history facts.

The pinned Build198x checker reports **two sound filesystems and fourteen
rejections**. Most rejections concern free bits beyond the disk's block range;
Creator 1.34 also has a rejected bitmap-valid flag. Retain each diagnostic exactly.
This pass neither determines the historical allocation policy behind those bits
nor changes the checker. It is not evidence that fourteen disks fail to boot.

For each candidate, the next working-copy qualification needs:

1. Source media identity and companion/installer dependencies, with explicit
   redistribution permissions checked separately from availability.
2. Installed program, libraries, extensions, configuration and startup hashes.
   Record the running version display rather than relying only on disk labels.
3. Exact emulator/machine/ROM/input configuration and cold-boot path.
4. Typed message, deliberate error and repair, native save, complete restart and
   reopen; only then call it a working reference for that route.
5. Independent minimal syntax, type and runtime probes appropriate to the release.
   A working editing loop is not comprehensive language conformance.

Keep original distributions unchanged. If reconstruction is needed, establish
what changes, compare all preserved file bytes and record the output separately.
Installer unpacking may need its own investigation; do not treat a valid installer
filesystem as proof that its installed runtime has been identified.

## Extension references

Start the extension comparison with the supplied components whose bytes are
already recorded. Include absent/disabled/present cases and the exact config;
never identify an extension solely by its slot number. Then select one separately
versioned extension, such as TOME or AMOS 3D, with original documentation and a
qualified runtime. No third-party extension media were inspected in this pass.

The next implementation-home choice is described in
[ownership options](parser-ownership-options.md). These candidate findings do not
resolve that architectural decision or commission a parser implementation.
