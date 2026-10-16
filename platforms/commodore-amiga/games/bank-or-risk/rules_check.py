"""Check proposed rules under an ideal die; this does not execute AMOS."""

from collections.abc import Callable
from fractions import Fraction
from functools import cache
from typing import Literal, NamedTuple


class Outcome(NamedTuple):
    phase: str
    displayed_total: int
    awarded_points: int


def roll_outcome(total: int, die: int) -> Outcome:
    if not 0 <= total < 21 or not 1 <= die <= 6:
        raise ValueError("Expected an active total and a die value from 1 to 6")
    new_total = total + die
    if new_total > 21:
        return Outcome("bust", new_total, 0)
    if new_total == 21:
        return Outcome("perfect", new_total, 21)
    return Outcome("active", new_total, 0)


def outcome_errors(classify: Callable[[int, int], Outcome]) -> list[str]:
    fixtures = (
        (0, 1, Outcome("active", 1, 0)),
        (0, 6, Outcome("active", 6, 0)),
        (14, 6, Outcome("active", 20, 0)),
        (15, 6, Outcome("perfect", 21, 21)),
        (16, 6, Outcome("bust", 22, 0)),
        (20, 1, Outcome("perfect", 21, 21)),
        (20, 6, Outcome("bust", 26, 0)),
    )
    return [
        f"total {total}, die {die}: expected {expected}, got {classify(total, die)}"
        for total, die, expected in fixtures
        if classify(total, die) != expected
    ]


Policy = Literal["safe", "optimal"]


@cache
def success_probability(
    rounds_left: int, needed: int, total: int, policy: Policy
) -> Fraction:
    if needed <= 0:
        return Fraction(1)
    if rounds_left == 0 or needed > 21 * rounds_left:
        return Fraction(0)
    bank = (
        success_probability(rounds_left - 1, needed - total, 0, policy)
        if total > 0
        else Fraction(-1)
    )
    roll = roll_probability(rounds_left, needed, total, policy)
    if policy == "safe":
        return bank if total >= 16 else roll
    return max(bank, roll)


def roll_probability(
    rounds_left: int, needed: int, total: int, policy: Policy
) -> Fraction:
    outcomes = []
    for die in range(1, 7):
        result = roll_outcome(total, die)
        if result.phase == "active":
            probability = success_probability(
                rounds_left, needed, result.displayed_total, policy
            )
        else:
            probability = success_probability(
                rounds_left - 1, needed - result.awarded_points, 0, policy
            )
        outcomes.append(probability)
    return sum(outcomes, Fraction(0)) / 6


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def main() -> None:
    require(not outcome_errors(roll_outcome), "Correct rule failed boundary fixtures")

    def wrong_equality(total: int, die: int) -> Outcome:
        if total + die >= 21:
            return Outcome("bust", total + die, 0)
        return roll_outcome(total, die)

    def wrong_bust_score(total: int, die: int) -> Outcome:
        if total + die > 21:
            return Outcome("bust", total + die, total + die)
        return roll_outcome(total, die)

    require(bool(outcome_errors(wrong_equality)), "Equal-limit mutation passed")
    require(bool(outcome_errors(wrong_bust_score)), "Bust-score mutation passed")
    print("PASS: boundary fixtures; equal-limit and bust-score mutations rejected")

    for total in range(21):
        busts = sum(roll_outcome(total, die).phase == "bust" for die in range(1, 7))
        require(busts == max(0, total - 15), f"Wrong risk count at {total}")
        if total >= 15:
            print(f"At {total}: {busts} of 6 next-roll outcomes bust")
    print("PASS: all 126 active-total/die combinations checked for bust risk")

    require(success_probability(5, 80, 0, "safe") == 1, "Safe policy can miss 80")
    require(success_probability(0, 0, 0, "optimal") == 1, "Target equality failed")
    require(success_probability(0, 1, 0, "optimal") == 0, "Extra round permitted")
    require(success_probability(4, 90, 0, "optimal") == 0, "Bust remains winnable")
    safe = success_probability(5, 90, 0, "safe")
    optimal = success_probability(5, 90, 0, "optimal")
    require(0 < safe < optimal < 1, "Target does not reward decisions under risk")
    print("PASS: safe policy guarantees 80; target/final-round/unreachable bounds")
    print(f"Five rounds, target 90, bank-at-16 policy: {float(safe):.6%}")
    print(f"Five rounds, target 90, optimal target policy: {float(optimal):.6%}")

    for needed, expected in ((30, "bank"), (39, "roll")):
        bank = success_probability(1, needed - 16, 0, "optimal")
        roll = roll_probability(2, needed, 16, "optimal")
        require(bank != roll, "Context comparison is tied")
        choice = "bank" if bank > roll else "roll"
        require(choice == expected, f"Unexpected choice with {needed} needed")
        print(
            f"Two rounds left, total 16, {needed} needed: {choice}; "
            f"bank {float(bank):.6%}, roll {float(roll):.6%}"
        )
    print("PASS: the same current total calls for different choices by session need")
    print("Exact rational enumeration; ideal die; no AMOS or player trial claimed")


if __name__ == "__main__":
    main()
