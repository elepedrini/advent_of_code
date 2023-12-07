import collections
from collections import Counter
from typing import List

from pydantic import BaseModel

from src.config import CONFIG

HANDS_TYPE_MAP = {
    "five-of-a-kind": (7, {5: 1}),  # 1 card appears 5 times
    "four-of-a-kind": (6, {4: 1, 1: 1}),  # 1 card appears 4 times; 1 card appears once
    "full-house": (5, {3: 1, 2: 1}),
    "three-of-a-kind": (4, {3: 1, 1: 2}),
    "two-pair": (3, {2: 2, 1: 1}),
    "one-pair": (2, {2: 1, 1: 3}),
    "high-card": (1, {1: 5}),
}


class Hand(BaseModel):
    id: int
    cards: str
    type_value: int
    cards_value: List[int]
    bid: int


def get_card_count_map(hand: str, part: int) -> collections.Counter:
    c = Counter(hand)
    if part == 2:
        card_max = max(c, key=c.get)
        if "J" in c and card_max != "J":
            c[card_max] += c["J"]  # add J to the highest count
            c.pop("J")
    return c


def get_hand_type_value(hand: str, part: int) -> int:
    """Returns the hand type value based on the number of occurrences of each card"""
    # generated with the help of Copilot
    cards_cnt = dict(Counter(get_card_count_map(hand, part=part).values()))
    return next(
        (value[0] for key, value in HANDS_TYPE_MAP.items() if cards_cnt == value[1]),
        None,
    )


def get_cards_values(hand: str, part: int) -> List:
    cards = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
    if part == 2:
        cards.remove("J")
        cards.insert(0, "J")
    cards_map = {card: i for i, card in enumerate(cards)}
    return [cards_map[c] for c in hand]


def get_winnings(fn: str, part: int) -> int:
    f = open(CONFIG["data_dir"] + fn)

    data = [
        Hand(
            id=i,
            cards=hand.split()[0],
            type_value=get_hand_type_value(hand.split()[0], part=part),
            cards_value=get_cards_values(hand.split()[0], part=part),
            bid=int(hand.split()[1]),
        )
        for i, hand in enumerate(f.read().split("\n"))
        if hand != ""
    ]

    # assign a rank to each hand (within each hand type)
    type_value_cnt_cumul = {}  # type_value: n_hands (cumulative)
    cards_ranks = {}  # hand_id: rank (within same hand type)
    for type_value_i in range(1, len(HANDS_TYPE_MAP) + 1):
        cards_values = [
            (hand.id, hand.cards_value)
            for hand in data
            if hand.type_value == type_value_i
        ]
        type_value_cnt_cumul[type_value_i] = type_value_cnt_cumul.get(
            type_value_i - 1, 0
        ) + len(cards_values)
        cards_ranks.update(
            {
                c[0]: sorted(cards_values, key=lambda x: x[1]).index(c)
                for c in cards_values
            }
        )

    res = 0
    for hand in data:
        rank = (
            cards_ranks[hand.id] + type_value_cnt_cumul.get(hand.type_value - 1, 0) + 1
        )
        res += hand.bid * rank

    return res


def part1(fn: str = "day07.txt") -> int:
    return get_winnings(fn, part=1)


def part2(fn: str = "day07.txt") -> int:
    return get_winnings(fn, part=2)


if __name__ == "__main__":
    print("Part 1: ", part1())  # 249483956
    print("Part 2: ", part2())
