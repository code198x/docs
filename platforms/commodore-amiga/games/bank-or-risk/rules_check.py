"""Compare proposed game settings under an ideal die; this does not execute AMOS."""

from collections import defaultdict
from collections.abc import Callable
from fractions import Fraction
from functools import cache
from typing import Literal, NamedTuple


class Outcome(NamedTuple):
    phase: str
    displayed_total: int
    awarded_points: int


class Setting(NamedTuple):
    limit: int
    rounds: int
    target: int


SETTINGS = (
    Setting(21, 5, 90),
    Setting(21, 5, 82),
    Setting(21, 10, 175),
    Setting(12, 5, 42),
    Setting(10, 5, 30),
    Setting(10, 5, 32),
    Setting(10, 5, 35),
)
RECOMMENDED = Setting(10, 5, 30)


def roll_outcome(total: int, die: int, limit: int) -> Outcome:
    if limit < 6 or not 0 <= total < limit or not 1 <= die <= 6:
        raise ValueError("Expected limit >= 6, active total and die value 1 to 6")
    new_total = total + die
    if new_total > limit:
        return Outcome("bust", new_total, 0)
    if new_total == limit:
        return Outcome("perfect", new_total, limit)
    return Outcome("active", new_total, 0)


def outcome_errors(classify: Callable[[int, int, int], Outcome]) -> list[str]:
    fixtures = (
        (0, 1, 10, Outcome("active", 1, 0)),
        (0, 6, 10, Outcome("active", 6, 0)),
        (3, 6, 10, Outcome("active", 9, 0)),
        (4, 6, 10, Outcome("perfect", 10, 10)),
        (5, 6, 10, Outcome("bust", 11, 0)),
        (9, 1, 10, Outcome("perfect", 10, 10)),
        (9, 6, 10, Outcome("bust", 15, 0)),
        (15, 6, 21, Outcome("perfect", 21, 21)),
        (16, 6, 21, Outcome("bust", 22, 0)),
    )
    return [
        f"total {total}, die {die}, limit {limit}: expected {expected}"
        for total, die, limit, expected in fixtures
        if classify(total, die, limit) != expected
    ]


Policy = int | Literal["optimal"]


@cache
def success_probability(
    rounds_left: int, needed: int, total: int, policy: Policy, limit: int
) -> Fraction:
    if needed <= 0:
        return Fraction(1)
    if rounds_left == 0 or needed > limit * rounds_left:
        return Fraction(0)
    bank = (
        success_probability(rounds_left - 1, needed - total, 0, policy, limit)
        if total > 0
        else Fraction(-1)
    )
    if isinstance(policy, int) and total >= policy:
        return bank
    roll = roll_probability(rounds_left, needed, total, policy, limit)
    return roll if isinstance(policy, int) else max(bank, roll)


def roll_probability(
    rounds_left: int, needed: int, total: int, policy: Policy, limit: int
) -> Fraction:
    outcomes = []
    for die in range(1, 7):
        result = roll_outcome(total, die, limit)
        if result.phase == "active":
            probability = success_probability(
                rounds_left, needed, result.displayed_total, policy, limit
            )
        else:
            probability = success_probability(
                rounds_left - 1, needed - result.awarded_points, 0, policy, limit
            )
        outcomes.append(probability)
    return sum(outcomes, Fraction(0)) / 6


def round_distribution(limit: int, threshold: int) -> dict[int, Fraction]:
    """Independent forward mass propagation, without the outcome classifier."""
    pending = [Fraction(0)] * limit
    pending[0] = Fraction(1)
    finished: defaultdict[int, Fraction] = defaultdict(Fraction)
    for total, mass in enumerate(pending):
        if total >= threshold:
            finished[total] += mass
            continue
        for die in range(1, 7):
            following = total + die
            if following > limit:
                finished[0] += mass / 6
            elif following == limit:
                finished[limit] += mass / 6
            else:
                pending[following] += mass / 6
    return dict(finished)


def convolved_probability(setting: Setting, threshold: int) -> Fraction:
    """Finish every round and sum scores, independently of target pruning."""
    one_round = round_distribution(setting.limit, threshold)
    require(sum(one_round.values()) == 1, "Round distribution lost probability")
    totals = {0: Fraction(1)}
    for _ in range(setting.rounds):
        following: defaultdict[int, Fraction] = defaultdict(Fraction)
        for secured, mass in totals.items():
            for score, probability in one_round.items():
                following[secured + score] += mass * probability
        totals = dict(following)
    require(sum(totals.values()) == 1, "Session distribution lost probability")
    return sum(
        (mass for score, mass in totals.items() if score >= setting.target),
        Fraction(0),
    )


def expected_rolls(limit: int, threshold: int) -> Fraction:
    """Mean rolls in one completed round under a fixed banking threshold."""
    values = [Fraction(0)] * limit
    for total in range(threshold - 1, -1, -1):
        values[total] = (
            1
            + sum(
                (values[total + die] for die in range(1, 7) if total + die < limit),
                Fraction(0),
            )
            / 6
        )
    return values[0]


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def main() -> None:
    require(not outcome_errors(roll_outcome), "Correct rule failed boundary fixtures")

    def wrong_equality(total: int, die: int, limit: int) -> Outcome:
        if total + die >= limit:
            return Outcome("bust", total + die, 0)
        return roll_outcome(total, die, limit)

    def wrong_bust_score(total: int, die: int, limit: int) -> Outcome:
        if total + die > limit:
            return Outcome("bust", total + die, total + die)
        return roll_outcome(total, die, limit)

    require(bool(outcome_errors(wrong_equality)), "Equal-limit mutation passed")
    require(bool(outcome_errors(wrong_bust_score)), "Bust-score mutation passed")
    print("PASS: boundary fixtures; equal-limit and bust-score mutations rejected")

    combinations = 0
    for limit in (10, 12, 21):
        for total in range(limit):
            busts = sum(
                roll_outcome(total, die, limit).phase == "bust" for die in range(1, 7)
            )
            require(busts == max(0, total + 6 - limit), "Wrong next-roll risk")
            combinations += 6
        safe = limit - 5
        require(
            success_probability(5, 5 * safe, 0, safe, limit) == 1,
            "Safe lower-bound guarantee failed",
        )
    require(combinations == 258, "Risk comparison silently dropped a limit")
    print(f"PASS: {combinations} total/die cases across limits 10, 12, 21")

    require(success_probability(0, 0, 0, "optimal", 10) == 1, "Equality failed")
    require(success_probability(0, 1, 0, "optimal", 10) == 0, "Extra round allowed")
    require(success_probability(4, 90, 0, "optimal", 21) == 0, "Bad reachability")
    old = success_probability(5, 90, 0, "optimal", 21)
    require(round(float(old) * 100, 6) == 76.795746, "Original result changed")

    print("limit rounds target | safe | fixed+1 | fixed+2 | optimal | after bust")
    comparisons = 0
    for setting in SETTINGS:
        limit, rounds, target = setting
        fixed = []
        for threshold in range(limit - 5, limit - 2):
            value = success_probability(rounds, target, 0, threshold, limit)
            require(
                value == convolved_probability(setting, threshold),
                f"Independent policy paths disagree: {setting}, {threshold}",
            )
            fixed.append(value)
            comparisons += 1
        optimal = success_probability(rounds, target, 0, "optimal", limit)
        recovery = success_probability(rounds - 1, target, 0, "optimal", limit)
        require(max(fixed) <= optimal <= 1, "Optimal value violates policy bound")
        require(0 <= recovery <= optimal, "Recovery exceeds a fresh challenge")
        values = " | ".join(
            f"{float(value):.6%}" for value in (*fixed, optimal, recovery)
        )
        print(f"{limit:5} {rounds:6} {target:6} | {values}")
    require(comparisons == 21, "Comparison matrix dropped a setting or policy")
    print("PASS: 21 fixed-policy cases agree exactly with independent convolution")

    limit, rounds, target = RECOMMENDED
    recovery = success_probability(rounds - 1, target, 0, "optimal", limit)
    safe = success_probability(rounds, target, 0, limit - 5, limit)
    moderate = success_probability(rounds, target, 0, limit - 4, limit)
    require(0 < recovery < 1, "Recommended recovery is impossible or guaranteed")
    require(0 < safe < moderate < 1, "No benefit to moderate risk at recommendation")
    for needed, expected in ((10, "bank"), (19, "roll")):
        bank = success_probability(1, needed - 6, 0, "optimal", limit)
        roll = roll_probability(2, needed, 6, "optimal", limit)
        require(bank != roll, "Context comparison is tied")
        choice = "bank" if bank > roll else "roll"
        require(choice == expected, "Context no longer changes the better choice")
        print(
            f"Limit 10, two rounds left, total 6, need {needed}: {choice}; "
            f"bank {float(bank):.6%}, roll {float(roll):.6%}"
        )
    print(
        "Mean rolls per completed round: "
        f"limit 21 / bank 16 = {float(expected_rolls(21, 16)):.6f}; "
        f"limit 10 / bank 6 = {float(expected_rolls(10, 6)):.6f}"
    )
    print("Exact ideal-die analysis; no AMOS, elapsed-time or learner trial claimed")


if __name__ == "__main__":
    main()
