"""Guard ID allocation across open batch branches."""

import unittest

from candidate_ids import clashes, next_id


class CandidateIdTests(unittest.TestCase):
    def test_the_next_id_clears_main_and_every_open_batch(self) -> None:
        queues = {"main": {"VC-3188": "a"}, "vault-batch/x": {"VC-3204": "b"}, "vault-batch/y": {"VC-3195": "c"}}
        self.assertEqual(next_id(queues), "VC-3205")

    def test_a_new_id_given_elsewhere_to_another_subject_clashes(self) -> None:
        base = {"VC-0010": "Oric"}
        mine = base | {"VC-3189": "Tangerine"}
        self.assertEqual(clashes(mine, base, {"vault-batch/x": {"VC-3189": "CPS-2"}}),
                         ["VC-3189: 'Tangerine' here, 'CPS-2' on vault-batch/x"])
        self.assertEqual(clashes(mine, base, {"vault-batch/x": {"VC-3189": "Tangerine"}}), [])
        self.assertEqual(clashes(mine, base, {"vault-batch/x": {"VC-0010": "Oric"}}), [])


if __name__ == "__main__":
    unittest.main()
