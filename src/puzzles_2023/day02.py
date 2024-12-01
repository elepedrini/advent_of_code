import re
from typing import List, Tuple

from src.config import CONFIG


def get_occurrences_by_color(line: str, color: str) -> List:
    """
    Returns a list of occurrences of a given color in a line.
    """
    return [int(el.split()[0]) for el in re.findall(r"\d+ {}".format(color), line)]


def get_max_occurrences(line: str) -> Tuple[int]:
    """
    Calculate the maximum occurrences of each color in a given line.

    Returns:
        Tuple[int]: A tuple containing the maximum occurrences of
            red, green, and blue respectively.
    """
    return (
        max(get_occurrences_by_color(line, "red")),
        max(get_occurrences_by_color(line, "green")),
        max(get_occurrences_by_color(line, "blue")),
    )


def part1(fn: str = "day02_p1.txt") -> int:
    f = open(CONFIG["data_dir"] + fn)
    res = 0
    max_allowed = (12, 13, 14)  # R G B

    for line in f.readlines():
        game_id = int(re.search(r"\d+", line).group())
        max_observed = get_max_occurrences(line)
        if all(max_observed[i] <= max_allowed[i] for i in range(3)):
            res += game_id
    return res


def part2(fn: str = "day02_p1.txt") -> int:
    f = open(CONFIG["data_dir"] + fn)
    res = 0

    for line in f.readlines():
        max_observed = get_max_occurrences(line)
        prod = 1
        for n in max_observed:
            prod *= n
        res += prod

    return res


if __name__ == "__main__":
    print("Part 1: ", part1())  # 2176
    print("Part 2: ", part2())  # 63700
