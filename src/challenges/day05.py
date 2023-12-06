import re

from src.config import CONFIG

SECTIONS = [
    "seeds:",
    "seed-to-soil map:",
    "soil-to-fertilizer map:",
    "fertilizer-to-water map:",
    "water-to-light map:",
    "light-to-temperature map:",
    "temperature-to-humidity map:",
    "humidity-to-location map:",
]


def part1(fn: str = "day05.txt") -> int:
    sections = SECTIONS
    data = open(CONFIG["data_dir"] + fn).read()

    seeds_str = data[data.find(sections[0]) : data.find(sections[1])]
    seeds = [int(t.group()) for t in re.finditer(r"\d+", seeds_str)]

    res = []

    for x in seeds:
        for i in range(1, len(sections)):
            section_data = data[data.find(sections[i]) :]
            if i < 7:
                section_data = data[data.find(sections[i]) : data.find(sections[i + 1])]
            section_ns = [int(t.group()) for t in re.finditer(r"\d+", section_data)]
            for j in range(1, len(section_ns) - 1, 3):
                if section_ns[j] <= x < section_ns[j] + section_ns[j + 1]:
                    x = x + (section_ns[j - 1] - section_ns[j])
                    break
        res.append(x)

    return min(res)


def part2(fn: str = "day05.txt") -> int:
    return None


if __name__ == "__main__":
    print("Part 1: ", part1())  # 318728750
    print("Part 2: ", part2())
