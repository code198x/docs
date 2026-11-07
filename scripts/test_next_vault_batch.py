"""Guard how a Vault batch is chosen: the lanes' share, demand order and named lists."""

import tempfile
import unittest
from pathlib import Path

from check_vault_candidates import FIELDS
from next_vault_batch import GUIDE_MINIMUM, article_words, choose, length_guides, named


def row(number: int, scope: str, refs: int = 0, status: str = "needs-triage") -> dict[str, str]:
    return dict.fromkeys(FIELDS, "") | {
        "id": f"VC-{number:04d}",
        "subject": f"Subject {number}",
        "category": "games",
        "scope": scope,
        "status": status,
        "why": "A reason.",
        "link_from": ";".join(f"games/ref-{number}-{n}" for n in range(refs)) or "games/example",
    }


class ChooseTests(unittest.TestCase):
    def setUp(self) -> None:
        self.rows = [
            row(1, "region:uk;period:1980s", refs=9),
            row(2, "region:us;period:1980s", refs=8),
            row(3, "region:us;period:1990s", refs=7),
            row(4, "region:japan;period:1980s", refs=3),
            row(5, "region:japan;period:1990s", refs=2),
            row(6, "region:ussr;period:1980s", refs=1),
            row(7, "region:us;period:1960s", refs=1),
            row(8, "region:uk;period:1980s", refs=20, status="published"),
            row(9, "region:uk;period:1980s", refs=19, status="in-progress"),
            row(10, "region:us;period:1980s", refs=6, status="ready"),
        ]

    def ids(self, size: int) -> list[tuple[str, str]]:
        return [(r["id"], why) for r, why in choose(self.rows, size)]

    def test_a_third_comes_from_the_lanes_taken_in_turn(self) -> None:
        # Six rounds up to two lane picks: world first, then early; four by
        # demand, where the 1990s VC-0003 waits behind every 1980s subject.
        self.assertEqual(
            self.ids(6),
            [
                ("VC-0004", "world"),
                ("VC-0007", "early"),
                ("VC-0001", "demand"),
                ("VC-0002", "demand"),
                ("VC-0010", "demand"),
                ("VC-0006", "demand"),
            ],
        )

    def test_old_machines_come_first_then_their_era_then_later_subjects(self) -> None:
        self.rows = [
            row(1, "region:us;period:1990s", refs=30),
            row(2, "region:uk;period:1980s", refs=20),
            row(3, "region:uk;period:1980s", refs=1) | {"category": "systems"},
            row(4, "region:us;period:1970s", refs=2) | {"category": "hardware"},
            row(5, "region:us;period:2000s", refs=40) | {"category": "systems"},
        ]
        self.assertEqual([i for i, _ in self.ids(5)], ["VC-0004", "VC-0003", "VC-0002", "VC-0005", "VC-0001"])
        # Among later subjects demand alone decides; machines get no extra place there.

    def test_the_world_lane_keeps_its_rotation_within_each_tier(self) -> None:
        self.rows = [
            row(1, "region:japan;period:1980s", refs=9) | {"category": "systems"},
            row(2, "region:japan;period:1980s", refs=8) | {"category": "systems"},
            row(3, "region:brazil;period:1980s", refs=1) | {"category": "systems"},
            row(4, "region:ussr;period:1990s", refs=50) | {"category": "systems"},
        ]
        self.assertEqual(self.ids(9)[:3], [("VC-0001", "world"), ("VC-0003", "world"), ("VC-0002", "world")])

    def test_the_world_lane_rotates_regions(self) -> None:
        # Japan ranks higher, but the USSR gets the second world place.
        self.rows = [r for r in self.rows if r["id"] != "VC-0007"]
        self.assertEqual(self.ids(9)[:3], [("VC-0004", "world"), ("VC-0006", "world"), ("VC-0005", "world")])

    def test_only_waiting_work_is_chosen(self) -> None:
        chosen = {i for i, _ in self.ids(20)}
        self.assertNotIn("VC-0008", chosen)
        self.assertNotIn("VC-0009", chosen)
        self.assertIn("VC-0010", chosen)
        self.assertEqual(len(chosen), 8)

    def test_empty_lanes_leave_the_whole_batch_to_demand(self) -> None:
        self.rows = [r for r in self.rows if r["id"] in {"VC-0001", "VC-0002", "VC-0003"}]
        self.assertEqual([why for _, why in self.ids(3)], ["demand"] * 3)

    def test_a_named_list_keeps_its_order_and_rejects_unavailable_work(self) -> None:
        self.assertEqual([r["id"] for r, _ in named(self.rows, ["VC-0006", "VC-0001"])], ["VC-0006", "VC-0001"])
        for ids, message in [
            (["VC-0099"], "unknown candidate"),
            (["VC-0008"], "published, not waiting"),
            (["VC-0009"], "in-progress, not waiting"),
            (["VC-0001", "VC-0001"], "appears twice"),
        ]:
            with self.subTest(ids=ids), self.assertRaisesRegex(ValueError, message):
                named(self.rows, ids)



class LengthGuideTests(unittest.TestCase):
    def test_only_the_article_counts(self) -> None:
        text = '---\ntitle: "X"\nsummary: "one two three"\n---\nimport Sources from "@components/Sources.astro";\n\nFour words of prose.\n\n<Figure src="a.png" alt="many words here" />\n\n<Sources>\n\n- A source with words.\n'
        self.assertEqual(article_words(text), 4)

    def test_guides_follow_each_category_and_small_ones_borrow_the_whole_vault(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            vault = Path(temp) / "src/content/vault"
            for category, count, words in (("systems", GUIDE_MINIMUM, 100), ("demos", 2, 1000)):
                (vault / category).mkdir(parents=True)
                for n in range(count):
                    (vault / category / f"e{n}.mdx").write_text("---\nt: x\n---\n" + "w " * (words + n), encoding="utf-8")
            guides = length_guides(Path(temp))
            self.assertEqual(guides["systems"], {"median": 104, "p90": 108, "entries": GUIDE_MINIMUM})
            self.assertNotIn("demos", guides)
            self.assertEqual(guides["*"]["entries"], GUIDE_MINIMUM + 2)

if __name__ == "__main__":
    unittest.main()
