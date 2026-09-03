# Decision: what earns a machine a place in the fleet

The fleet is a claim about the curriculum's intent. The Vault is an encyclopedia. They take different machines for different reasons, and conflating them is what makes "why not every computer ever made?" feel unanswerable.

## The decision

**A machine earns a fleet entry when the curriculum has a position on it.** Not when it was important, not when it was interesting, and not when it existed — those are the Vault's tests, and the Vault is where a machine goes when they are the only ones it passes.

A position is one of four:

| `tier` | The position | |
|---|---|---|
| `live` | Lessons exist and ship. | We teach this. |
| `next` | Validated, in build. | We are teaching this. |
| `planned` | Skeleton and a way to be told when lessons land. | We intend to teach this. |
| `edge` | Strains the method — vector displays, 3D-first hardware, add-on-dependent machines. | We have looked and it does not fit cleanly. |
| `beyond` | Outside the curriculum's domain, but the curriculum points at it. | We teach *about* this without teaching *on* it. |

The five are a spectrum of commitment, and every one of them is a commitment. A machine with none of these positions has no fleet entry, however much it mattered.

## The bar for `beyond`, which is the one that gets stretched

`beyond` is the loosest tier and therefore the one that decides whether the fleet stays finite. Its test is **the curriculum already points at this machine and a reader following the reference needs somewhere to land.**

The DEC PDP-1 qualifies: the curriculum treats *Spacewar!* (1962) as the origin of the field, and a learner following that reference should not arrive nowhere. The PDP-10 qualifies through *Colossal Cave Adventure* and *Zork*. See [`period-extends-to-the-1960s.md`](../../../decisions/period-extends-to-the-1960s.md).

A machine that *could* be pointed at does not qualify. The test is that something in the curriculum or the Vault's connective tissue already reaches for it and finds nothing.

## Why this is not "everything in the world"

The worry is reasonable: once historical importance is admitted as a reason, every machine ever built has a case, and 156 entries becomes 1,560.

It does not, because historical importance is **the Vault's** test, not the fleet's. The Vault takes a machine because it mattered. The fleet takes a machine because we have said something about teaching it — even if what we have said is "not on this one".

So the honest answer to *why is the PDP-8 here and not the Honeywell 316* is not that one matters more. It is that a fleet entry is a sentence the curriculum has committed to, and we have not written one about the Honeywell.

## The PDP-8

Included, at `beyond`, on the same grounds as its siblings: the period decision admits it, and a fleet that carries the PDP-1 and PDP-10 while omitting the machine between them tells a reader something untrue about the family.

This is the weakest of the three cases — the period record names no specific program for it, where the others have *Spacewar!*, *Adventure* and *Zork*. Recorded as a judgement rather than a derivation, so that a later reader can disagree with it knowingly.

## What this does not decide

- **Whether a machine gets a Vault entry.** A far broader test, and not this record's business.
- **Emulation or toolchain support.** Independent surfaces — see [`support-surfaces.md`](../../../decisions/support-surfaces.md). A core existing implies nothing about a fleet position, and a fleet position implies nothing about a core.

## Drift triggers

- Adding a machine because it is famous, without a sentence saying what the curriculum's position on it is.
- Reaching for `planned` as the default. It means *we intend to teach this*, and 122 machines already carry that intention.
- Using `beyond` for a machine nothing points at. That is the tier that turns the fleet into a database dump.
- Arguing a machine in on historical importance alone. That argument belongs to the Vault and always wins there; it does not transfer.
- Treating the fleet's size as the thing to control. The constraint is that every entry is a position, not that there are few of them.

## Relates to

- [`../../../decisions/support-surfaces.md`](../../../decisions/support-surfaces.md) — the three independent support surfaces; orthogonal to this.
- [`../../../decisions/period-extends-to-the-1960s.md`](../../../decisions/period-extends-to-the-1960s.md) — what admitted the PDP machines.
- [`website-information-architecture.md`](website-information-architecture.md) — `tier` as the single source of readiness.
