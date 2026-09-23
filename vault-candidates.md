# Vault entry candidates

Subjects the Vault mentions but has no entry for, with the entries that should link to each one once it exists. Reviewers add to this list as they work through batches (see [the Vault specification](specifications/vault.md#reviewing-existing-entries)). When an entry is written, add its links from the pages named here and remove its row.

A candidate earns an entry by helping a reader of an existing entry or lesson, not by being mentioned. Check that no entry already covers the subject under another name first. The website's `node scripts/vault-candidates.mjs` surfaces emphasised names across the whole Vault and is a useful source for new rows.

Paths are Vault entries (`category/slug`) in the website repository.

## Machines and hardware

| Candidate | Category | Why | Link from |
|---|---|---|---|
| Sinclair ZX80 | systems | The first of Sinclair's three computers; its keyword entry and syntax checking carried into the ZX81 and Spectrum. The systems collection has it; the Vault does not. **Queued for batch 2.** | `companies/sinclair-research`, `people/clive-sinclair`, `people/steven-vickers`, `systems/zx81`, `systems/zx-spectrum` |
| Sinclair Microdrive | hardware | The Spectrum's and QL's tape-loop storage, central to the QL's troubles | `companies/sinclair-research`, `systems/sinclair-ql`, `systems/zx-spectrum` |
| ZX Interface 2 | hardware | Sinclair's joystick and ROM-cartridge interface; Ultimate's early games came out on cartridge for it | `companies/sinclair-research`, `companies/ultimate` |
| MK14 | systems | Science of Cambridge's kit micro, Sinclair's first computer product | `companies/sinclair-research`, `people/clive-sinclair` |
| Grundy NewBrain | systems | Designed at Sinclair Radionics, sold on, and released two years later | `companies/sinclair-research` |

## People

| Candidate | Category | Why | Link from |
|---|---|---|---|
| Richard Altwasser | people | Designed the Spectrum's hardware and its ULA logic | `systems/zx-spectrum`, `hardware/ula`, `companies/sinclair-research`, `people/steven-vickers` |
| John Grant | people | Co-wrote the Spectrum ROM with Steven Vickers, on contract from Nine Tiles | `people/steven-vickers`, `systems/zx-spectrum`, `systems/zx81` |
| Chris Curry | people | Co-founded Science of Cambridge with Sinclair, then Acorn | `companies/sinclair-research`, `people/clive-sinclair`, `companies/acorn-computers` |

## Companies and organisations

| Candidate | Category | Why | Link from |
|---|---|---|---|
| Nine Tiles | companies | The contractor that wrote Sinclair's BASIC ROMs | `people/steven-vickers`, `systems/zx81`, `systems/zx-spectrum` |
| Amstrad | companies | Bought Sinclair's computer business in 1986 and made the +2 and +3; the Vault has the CPC but not the company | `companies/sinclair-research`, `systems/zx-spectrum`, `people/clive-sinclair`, `systems/amstrad-cpc` |
| Timex | companies | Sinclair's US partner (Timex Sinclair) and one of its 1985 creditors | `companies/sinclair-research`, `systems/zx81`, `systems/zx-spectrum` |
| Ferranti | companies | Made the uncommitted logic arrays in the ZX81 and Spectrum | `hardware/ula`, `systems/zx81` |
| Sinclair Radionics | companies | Sinclair's earlier company; its collapse explains how Sinclair Research began | `companies/sinclair-research`, `people/clive-sinclair` |
| Jupiter Cantab | companies | Founded by ex-Sinclair engineers to make the Jupiter Ace | `companies/sinclair-research`, `systems/jupiter-ace` |

## Magazines

| Candidate | Category | Why | Link from |
|---|---|---|---|
| Personal Computer Games | magazines | A key 1983–85 source for Manic Miner, Matthew Smith and the Liverpool scene | `games/manic-miner`, `people/matthew-smith` |
| Personal Computer News | magazines | Dated Manic Miner's release (August 1983 review) | `games/manic-miner`, `people/matthew-smith`, `systems/zx81` |

## Games

| Candidate | Category | Why | Link from |
|---|---|---|---|
| Miner 2049er | games | The game the Manic Miner entry names as its model (as *Miner 49'er*) | `games/manic-miner` |
| Styx | games | Matthew Smith's first Bug-Byte release | `people/matthew-smith`, `games/manic-miner` |
| Alien 8 | games | Ultimate's second Filmation game, after Knight Lore | `companies/ultimate`, `games/knight-lore` |
| Nightshade | games | Ultimate's scrolling Filmation II game | `companies/ultimate` |
| Underwurlde | games | The second Sabreman game | `companies/ultimate`, `games/sabre-wulf` |
| Lunar Jetman | games | Jetpac's sequel | `companies/ultimate`, `games/jetpac` |
