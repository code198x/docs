# Information architecture

Navigation serves the connected curriculum in [Project purpose](../PROJECT.md). Readers can enter through a system, a shared concept, a game, the Vault or a reusable pattern. A recommended route should state the knowledge it uses and why a link helps, without assuming attendance elsewhere.

## Implemented route families

| Route | Role |
|---|---|
| `/curriculum/`, `/foundations/`, `/craft/` | Curriculum and shared-subject discovery |
| `/foundations/{module}/unit-NN/`, `/craft/{module}/unit-NN/` | Shared lessons where authored |
| `/systems/` | Fleet, with maker and tier views |
| `/systems/{system}/{track}/{module}/unit-NN/` | System-specific guided lessons |
| `/vault/{category}/{slug}/` | Encyclopaedic context |
| `/patterns/{system}/{track}/{category}/{slug}/` | Machine/language-specific reusable techniques |
| `/patterns/cross-platform/{category}/{slug}/` | Techniques whose explanation genuinely transfers |
| `/timeline/`, `/browse/` | Historical and cross-cutting discovery |
| `/setup/`, `/about/`, `/contribute/`, `/colophon/` | Practical help, purpose, participation and credits |

The website route files and catalogues determine exact routes and availability. Existing redirects must remain intact when moving content; a documentation change is not authorisation to break published lesson links.

## Connections and honest status

Keep enough explanation in the lesson to continue. Add selected links to deeper shared explanations, a relevant Vault entry or a pattern demonstrating the technique elsewhere. Link back from those resources to complete games where useful. Inspect existing entries first and use canonical explanations rather than duplicates.

“Requires” describes knowledge or runtime resources, not proof that the reader completed a named unit. Navigation should make optional preparation available without presenting a fixed course as the only way in. Record missing useful entries for subsequent authoring rather than linking to imaginary pages.

Show coming-soon and incomplete material honestly. Distinguish curriculum availability, emulator readiness and assembler support. Fleet status names currently include `live`, `next`, `planned`, `edge` and `beyond`; these labels need assessment against the family's support-surface scope before any redesign. Do not equate an older status label with a permanent curriculum exclusion.

## Presentation

House styling is system-neutral; each system can express its own character within its pages. Shared navigation, media and typography use the existing components and tokens. Avoid multiplying top-level modules merely because a topic is important. See [Website implementation](../infrastructure/astro-site.md) and the [component assessment](../infrastructure/curriculum-components.md).
