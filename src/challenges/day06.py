import re
from typing import Dict, List

from src.config import CONFIG


def extract_numbers(text: str) -> List[int]:
    return [int(t.group()) for t in re.finditer(r"\d+", text)]


def count_winning_combs(data_map: Dict) -> int:
    res = 1
    for i, t in enumerate(data_map["time"]):
        winning_cnt = 0
        for hold_ms in range(1, t):
            dist = (t - hold_ms) * hold_ms
            if dist > data_map["distance"][i]:
                winning_cnt += 1
        res *= winning_cnt
    return res


def part1(fn: str = "day06.txt") -> int:
    f = open(CONFIG["data_dir"] + fn)
    data = f.read()
    data_map = {
        "time": extract_numbers(data.split("\n")[0]),
        "distance": extract_numbers(data.split("\n")[1]),
    }

    return count_winning_combs(data_map)


def part2(fn: str = "day06.txt") -> int:
    f = open(CONFIG["data_dir"] + fn)
    data = f.read()
    data_map = {
        "time": [int(data[5 : data.find("\n")].replace(" ", ""))],
        "distance": [int(data[data.find("\n") + 10 :].replace(" ", ""))],
    }

    return count_winning_combs(data_map)


if __name__ == "__main__":
    print("Part 1: ", part1())  # 449820
    print("Part 2: ", part2())  # 42250895
