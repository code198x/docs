# Decision: regional release titles

**Status:** Draft (Claude, 2026-08-08) — awaiting Steve's approval. Triggered by a Vault
genre entry citing *X-COM: UFO Defense*, the North American title, in a passage about the
British press. In the UK and Europe the game was *UFO: Enemy Unknown*.

## The decision

**Name a work as the sources covering it named it.**

Where a title differs by market, the Vault leads with the title used in the market whose
sources the entry draws on, and notes the alternative. For entries sourced from the British
magazine archive, that means the British title.

    UFO: Enemy Unknown          (UK/EU, 1994)   — lead
    X-COM: UFO Defense          (US)            — note

## Why this framing, and not "British first"

"British first" is the wrong rule and an uncomfortable phrase. The principle is
bibliographic, not patriotic: a citation and the title it carries should agree. An entry
whose evidence is a *CRASH* review is describing the object British readers bought, under
the name printed on the box they bought it in. Using the American title there is a small
factual error dressed as a house style.

Stated this way the rule generalises, which "British first" does not. The scope model treats
world computing history as first-class rather than Anglosphere-with-exceptions, so an entry
drawing on *Zzap!* (IT), *Pixel* (GR) or *576KByte* (HU) should carry the title that
readership knew — the same rule, applied honestly.

## Practice

- **Lead with the source-market title**, in the entry title and throughout the prose.
- **Note the alternative** once, near first use or in Fast facts.
- **Slugs are not retitled** just for this. A slug is an address; changing it breaks links
  for no reader benefit. `games/x-com-ufo-defense.mdx` may keep its filename while its
  `title:` and prose lead with *UFO: Enemy Unknown*.
- **Where the entry has no single source market** — a cross-period overview, a modern game —
  use the title most readers will recognise and note the variant.

## Scale: this is cheap to adopt now, and would not be later

Measured 2026-08-08 against the magazine archive. Of the **244** Vault games released
1980-1994 — the window the British corpus covers — **exactly one** never appears under its
Vault title in the corpus, and that one is not a market-title problem: *"Dizzy: The Ultimate
Cartoon Adventure"* is the packaging subtitle, and the magazines simply say *Dizzy* (4,600
pages). The catalogue is effectively already compliant.

⚠ **So there is no back-catalogue pass to do**, and this record should not be read as
commissioning one. The rule costs nothing to follow from here and prevents a class of error
that gets expensive once hundreds more entries exist. Adopting it while the count is zero is
the entire point.

The one known exception is `vault/games/x-com-ufo-defense.mdx`, which leads with the American
title. Worth fixing when that entry is next touched; not worth a special trip.

⚠ Note the asymmetry that made this measurable: the *sources* are consistent even where the
Vault might not be, so the corpus can audit the catalogue at any time. Re-run the check
rather than assuming, and expect the count to rise as coverage extends into markets whose
titles diverge more sharply than the UK/US pair does.

## Why it needed writing down

Three corrections in one session ran the same way — `isometric` treated as a genre, `arcade`
misread as provenance, and this. Each time the model default was American and modern, and
each time the corpus or Steve said otherwise. The failure is systematic enough to deserve a
rule rather than a series of catches.

## See also

- [British English](british-english.md) — spelling, a separate matter from proper nouns.
