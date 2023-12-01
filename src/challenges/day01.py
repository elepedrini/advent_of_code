import regex as re

from src.config import CONFIG


def part1(fn: str = "day01_p1.txt") -> int:
    f = open(CONFIG["data_dir"] + fn)
    tot_sum = 0
    for line in f.readlines():
        m = re.findall(r"\d", line, overlapped=True)
        if len(m) > 0:
            tot_sum += int(m[0] + m[-1])
    return tot_sum


def part2(fn: str = "day01_p2.txt") -> int:
    f = open(CONFIG["data_dir"] + fn)
    numbers_map = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }
    tot_sum = 0
    for line in f.readlines():
        m = re.findall(
            r"\d|one|two|three|four|five|six|seven|eight|nine", line, overlapped=True
        )
        if len(m) > 0:
            first_digit = numbers_map.get(m[0], m[0])
            last_digit = numbers_map.get(m[-1], m[-1])
            tot_sum += int(first_digit + last_digit)
    return tot_sum


if __name__ == "__main__":
    print("Part 1: ", part1())
    print("Part 2: ", part2())
