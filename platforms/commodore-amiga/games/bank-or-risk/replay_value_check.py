"""Analyse the five-round rescue extension under an ideal independent fair die."""

from __future__ import annotations

import json
from collections import defaultdict
from fractions import Fraction
from functools import cache

from rules_check import (
    RECOMMENDED,
    convolved_probability,
    round_distribution,
    success_probability,
)


@cache
def distribution(
    rounds: int, total: int, rescue: bool, threshold: int
) -> dict[int, Fraction]:
    """Bank at threshold; spend rescue on the first bust, then resume that policy."""
    if rounds == 0:
        return {0: Fraction(1)}
    if total >= threshold:
        return {
            score + total: p
            for score, p in distribution(rounds - 1, 0, rescue, threshold).items()
        }
    result: defaultdict[int, Fraction] = defaultdict(Fraction)
    for face in range(1, 7):
        value = total + face
        award = 0
        if value > 10:
            branch = (
                distribution(rounds, total, False, threshold)
                if rescue
                else distribution(rounds - 1, 0, False, threshold)
            )
        elif value == 10:
            award = 10
            branch = distribution(rounds - 1, 0, rescue, threshold)
        else:
            branch = distribution(rounds, value, rescue, threshold)
        for score, p in branch.items():
            result[score + award] += p / 6
    return dict(result)


@cache
def best_chance(rounds: int, needed: int, total: int, rescue: bool) -> Fraction:
    if needed <= 0:
        return Fraction(1)
    if rounds == 0 or needed > 10 * rounds:
        return Fraction(0)
    bank = best_chance(rounds - 1, needed - total, 0, rescue) if total else Fraction(-1)
    roll = Fraction(0)
    for face in range(1, 7):
        value = total + face
        if value > 10:
            accept = best_chance(rounds - 1, needed, 0, rescue)
            chance = (
                max(accept, best_chance(rounds, needed, total, False))
                if rescue
                else accept
            )
        elif value == 10:
            chance = best_chance(rounds - 1, needed - 10, 0, rescue)
        else:
            chance = best_chance(rounds, needed, value, rescue)
        roll += chance / 6
    return max(bank, roll)


@cache
def best_score(rounds: int, total: int, rescue: bool) -> Fraction:
    if rounds == 0:
        return Fraction(0)
    bank = total + best_score(rounds - 1, 0, rescue) if total else Fraction(-1)
    roll = Fraction(0)
    for face in range(1, 7):
        value = total + face
        if value > 10:
            accept = best_score(rounds - 1, 0, rescue)
            expectation = (
                max(accept, best_score(rounds, total, False)) if rescue else accept
            )
        elif value == 10:
            expectation = 10 + best_score(rounds - 1, 0, rescue)
        else:
            expectation = best_score(rounds, value, rescue)
        roll += expectation / 6
    return max(bank, roll)


def main() -> None:
    result = {
        "assumption": "Ideal independent fair die; exact policy calculations, not AMOS or human win rates",
        "settings": {"limit": 10, "rounds": 5, "target": 30},
        "policies": {},
    }
    for threshold in (5, 6, 7):
        # Independent one-round distribution convolved five times.
        one = round_distribution(10, threshold)
        convolution = {0: Fraction(1)}
        for _ in range(5):
            following: defaultdict[int, Fraction] = defaultdict(Fraction)
            for before, p in convolution.items():
                for award, q in one.items():
                    following[before + award] += p * q
            convolution = dict(following)
        plain = distribution(5, 0, False, threshold)
        assert plain == convolution
        baseline = sum(p for score, p in plain.items() if score >= 30)
        assert baseline == convolved_probability(RECOMMENDED, threshold)
        cases = {}
        for rescue in (False, True):
            values = distribution(5, 0, rescue, threshold)
            assert sum(values.values()) == 1
            assert all(0 <= score <= 50 and p > 0 for score, p in values.items())
            chance = sum(p for score, p in values.items() if score >= 30)
            expected = sum(score * p for score, p in values.items())
            cases["first_bust_rescue" if rescue else "no_rescue"] = {
                "reach_30_percent": float(chance * 100),
                "mean_final_score": float(expected),
                "exact_reach_30": str(chance),
            }
        assert (
            cases["first_bust_rescue"]["reach_30_percent"]
            >= cases["no_rescue"]["reach_30_percent"]
        )
        result["policies"][str(threshold)] = cases
    plain_optimal = best_chance(5, 30, 0, False)
    assert plain_optimal == success_probability(5, 30, 0, "optimal", 10)
    assert best_chance(5, 30, 0, True) >= plain_optimal
    assert best_score(5, 0, False) == 5 * best_score(1, 0, False)
    assert best_score(5, 0, True) > best_score(5, 0, False)
    # Equal upper bound is still reachable; below it is not. Rescue never raises 10 per round.
    assert best_chance(3, 30, 0, True) > 0
    assert best_chance(2, 30, 0, True) == 0
    assert best_chance(0, 1, 0, True) == 0
    result["target_optimising_maximum_percent"] = float(
        best_chance(5, 30, 0, True) * 100
    )
    result["score_optimising_mean"] = {
        "without_rescue": float(best_score(5, 0, False)),
        "with_rescue": float(best_score(5, 0, True)),
    }
    # Compare both choices at different opportunities; this is not a required learner policy.
    decisions = []
    for rounds in (1, 5):
        for total in (5, 8, 9):
            undo = best_score(rounds, total, False)
            accept = best_score(rounds - 1, 0, True)
            decisions.append(
                {
                    "rounds_including_current": rounds,
                    "pre_bust_total": total,
                    "undo_mean": float(undo),
                    "accept_mean": float(accept),
                    "score_policy_choice": "undo" if undo >= accept else "accept",
                }
            )
    result["example_rescue_decisions"] = decisions
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
