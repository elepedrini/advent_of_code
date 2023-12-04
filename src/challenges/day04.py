import re

from src.config import CONFIG


def get_numbers_list(input_str: str):
    """
    Returns a list with all numbers extracted from a string
    """
    return [int(m.group()) for m in re.finditer(r"\d+", input_str)]


def get_matches(line: str):
    """
    Returns a set with all numbers that are matched in the winning numbers
    and observed numbers in a given line
    """
    winning_ns = get_numbers_list(line[line.find(":") : line.find("|")])
    observed_ns = get_numbers_list(line[line.find("|") :])
    return set(observed_ns) & set(winning_ns)


def part1(fn: str = "day04.txt") -> int:
    f = open(CONFIG["data_dir"] + fn)
    res = 0
    for line in f.readlines():
        matched_ns = get_matches(line)
        if matched_ns:
            res += 2 ** (len(matched_ns) - 1)
    return res


def part2(fn: str = "day04.txt") -> int:
    f = open(CONFIG["data_dir"] + fn)
    data = f.readlines()
    cards = {}
    for i in range(1, len(data) + 1):
        cards[i] = 1

    for line in data:
        card_id = int(line[5 : line.find(":")])
        matched_ns = get_matches(line)

        for i in range(1, len(matched_ns) + 1):
            cards[card_id + i] += 1 * cards[card_id]

    return sum(cards.values())


if __name__ == "__main__":
    print("Part 1: ", part1())  # 17782
    print("Part 2: ", part2())  # 8477787
