"""Guard what the expansion step proposes, asks and refuses to merge."""

import csv
import json
import tempfile
import unittest
from pathlib import Path

from check_vault_candidates import FIELDS, load_backlog
from expand_vault_entry import apply, expand

FAKE_GRAPH = '''
import json, sys
GRAPH = json.loads({graph!r})
args = sys.argv[1:]
offset = int(args[args.index("--offset") + 1]) if "--offset" in args else 0
command = [a for a in args if not a.startswith("--") and not a.isdigit()]
if command[0] == "resolve":
    items = GRAPH["resolve"].get(command[1], [])
    print(json.dumps({{"items": items}}))
else:
    edges = GRAPH["edges"].get(args[-1], [])
    page = edges[offset:offset + 100]
    print(json.dumps({{"edges": {{"items": page, "has_more": offset + 100 < len(edges)}}}}))
'''


def entity(entity_id: int, kind: str, name: str) -> dict:
    return {"kind": "entity", "id": entity_id, "type": kind, "name": name, "suspect": 0}


def found(entity_id: int, kind: str, name: str) -> dict:
    return {"entity": entity(entity_id, kind, name), "match": "normalised_exact"}


def published(subject: dict, game_id: int, game: str) -> dict:
    return {
        "relation": "published",
        "source": subject,
        "destination": {"kind": "release", "game": entity(game_id, "game", game)},
        "evidence": {"source": "crash-38.txt", "recorded_page": 75},
    }


class ExpansionTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.website = self.root / "website"
        vault = self.website / "src/content/vault"
        for path, title in [
            ("companies/acme", "Acme Software"),
            ("games/jetpac", "Jetpac"),
            ("games/galaxian", "Galaxian"),
            ("systems/atari-st", "Atari ST"),
            ("systems/msx", "MSX"),
        ]:
            (vault / path).parent.mkdir(parents=True, exist_ok=True)
            (vault / f"{path}.mdx").write_text(f'---\ntitle: "{title}"\n---\nBody', encoding="utf-8")
        (self.website / "astro.config.mjs").write_text(
            "export default { redirects: {\n    '/vault/games/old-name': '/vault/games/jetpac',\n  }\n};",
            encoding="utf-8",
        )
        self.queue = self.root / "vault-candidates.csv"
        self.write_queue(
            {"id": "VC-0001", "subject": "The Dark Wheel", "category": "books"},
            {"id": "VC-0002", "subject": "IBM PC", "category": "systems"},
        )
        self.acme = entity(10, "publisher", "Acme Software")
        self.graph = {"resolve": {}, "edges": {}}

    def write_queue(self, *rows: dict[str, str]) -> None:
        with self.queue.open("w", newline="", encoding="utf-8") as handle:
            writer = csv.DictWriter(handle, fieldnames=FIELDS, lineterminator="\n")
            writer.writeheader()
            for row in rows:
                writer.writerow(
                    dict.fromkeys(FIELDS, "")
                    | {"status": "needs-triage", "why": "Named.", "link_from": "systems/msx"}
                    | row
                )

    def entry(self, body: str) -> None:
        (self.website / "src/content/vault/companies/acme.mdx").write_text(
            f'---\ntitle: "Acme Software"\n---\n{body}', encoding="utf-8"
        )

    def run_expand(self):
        script = self.root / "knowledge.py"
        script.write_text(FAKE_GRAPH.format(graph=json.dumps(self.graph)), encoding="utf-8")
        return expand("companies/acme", self.website, load_backlog(self.queue), script)

    def test_an_emphasised_unknown_game_is_proposed_with_its_category(self) -> None:
        self.entry("Acme's best game was *Cyberun*. **Developer:** someone. *Graphics* were fine.")
        self.graph["resolve"]["Cyberun"] = [found(5, "game", "CYBERUN")]
        result = self.run_expand()
        self.assertEqual([(p.subject, p.category) for p in result.new], [("Cyberun", "games")])

    def test_known_subjects_are_never_proposed_again(self) -> None:
        self.entry("*Jet-Pac*, *Old Name*, *Galaxians*, [*Bubbler*](/vault/games/bubbler) and *Atari ST*.")
        result = self.run_expand()
        self.assertEqual(result.new, [])
        self.assertEqual(result.questions, [])

    def test_a_named_candidate_gains_link_from_instead_of_a_new_row(self) -> None:
        self.entry("Ian Bell wrote *Dark Wheel*, and it ran on the *IBM PC*.")
        result = self.run_expand()
        self.assertEqual(sorted(i for i, _ in result.link_from), ["VC-0001", "VC-0002"])
        self.assertEqual(result.new, [])

    def test_a_near_match_is_a_question_not_a_proposal(self) -> None:
        self.entry("Ported to the *Atari ST Plus*.")
        self.graph["resolve"]["Atari ST Plus"] = [found(7, "machine", "Atari ST Plus")]
        result = self.run_expand()
        self.assertEqual(result.new, [])
        self.assertIn("nearly matches", result.questions[0])

    def test_a_name_with_no_known_category_is_a_question(self) -> None:
        self.entry("Its tagline was *Programmer of the Year*.")
        result = self.run_expand()
        self.assertEqual(result.new, [])
        self.assertIn("category isn't known", result.questions[0])

    def test_and_splits_only_names_whose_parts_are_all_known(self) -> None:
        self.entry("On *MSX and IBM PC*. Founded by *Tim and Chris Example*.")
        result = self.run_expand()
        self.assertEqual([i for i, _ in result.link_from], ["VC-0002"])
        self.assertTrue(any("Tim and Chris Example" in q for q in result.questions))
        self.assertFalse(any(q.startswith("'Tim'") for q in result.questions))

    def test_two_identities_of_one_type_are_a_question_and_never_merged(self) -> None:
        self.entry("Nothing emphasised.")
        self.graph["resolve"]["Acme Software"] = [
            found(10, "publisher", "Acme Software"),
            found(11, "publisher", "ACME SOFTWARE"),
        ]
        self.graph["edges"]["10"] = [published(self.acme, 1, "Rocket Run")] * 2
        result = self.run_expand()
        self.assertEqual(result.new, [])
        self.assertIn("matches 2 graph identities", result.questions[0])

    def test_the_most_specific_type_is_read_rather_than_an_advert(self) -> None:
        self.entry("Nothing emphasised.")
        self.graph["resolve"]["Acme Software"] = [
            found(10, "publisher", "Acme Software"),
            found(12, "advertiser", "ACME SOFTWARE"),
        ]
        self.graph["edges"]["10"] = [published(self.acme, 1, "ROCKET RUN")] * 2
        result = self.run_expand()
        self.assertEqual([(p.subject, p.category) for p in result.new], [("Rocket Run", "games")])
        self.assertIn("crash-38.txt p75", result.new[0].evidence)

    def test_thin_or_catalogue_only_neighbours_are_not_proposed(self) -> None:
        self.entry("Nothing emphasised.")
        self.graph["resolve"]["Acme Software"] = [found(10, "publisher", "Acme Software")]
        person = {"kind": "entity", "id": 3, "type": "publisher", "name": "Bell, Ian", "suspect": 0}
        self.graph["edges"]["10"] = [
            published(self.acme, 1, "One Record"),
            {**published(self.acme, 2, "x"), "destination": person},
            {**published(self.acme, 2, "x"), "destination": person},
        ]
        self.assertEqual(self.run_expand().new, [])

    def test_apply_adds_rows_and_links_and_the_backlog_still_validates(self) -> None:
        self.entry("Played *Cyberun* on the *IBM PC*.")
        self.graph["resolve"]["Cyberun"] = [found(5, "game", "CYBERUN")]
        result = self.run_expand()
        self.assertEqual(apply(self.queue, result), 1)
        rows = {row["id"]: row for row in load_backlog(self.queue)}
        self.assertEqual(rows["VC-0003"]["subject"], "Cyberun")
        self.assertEqual(rows["VC-0003"]["status"], "needs-triage")
        self.assertEqual(rows["VC-0003"]["link_from"], "companies/acme")
        self.assertEqual(rows["VC-0002"]["link_from"], "systems/msx;companies/acme")


if __name__ == "__main__":
    unittest.main()
