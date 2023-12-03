import re
from typing import Dict, List
from uuid import UUID, uuid4

from pydantic import BaseModel

from src.config import CONFIG


# Entities
class NumberSpan(BaseModel):
    start: int
    end: int


class NumbersMapItem(BaseModel):
    id: UUID
    number: int
    row: int
    col_span: NumberSpan


class NumbersMap(BaseModel):
    values: List[NumbersMapItem]


class SymbolsMapItem(BaseModel):
    row: int
    col: int


class SymbolsMap(BaseModel):
    values: List[SymbolsMapItem]


# Functions
def open_file(fn: str) -> List[str]:
    f = open(CONFIG["data_dir"] + fn)
    return f.readlines()


def get_numbers_map(data: List[str]) -> NumbersMap:
    map_numbers = []  # [(number, x, (y_start, y_end)), ...]
    for i in range(len(data)):
        line = data[i]
        map_numbers_in_line = [
            NumbersMapItem(
                id=uuid4(),
                number=int(n.group()),
                row=i,
                col_span=NumberSpan(start=n.span()[0], end=n.span()[1]),
            )
            # find all numbers in a row
            for n in re.finditer(r"\d+", line.strip())
        ]
        map_numbers.extend(map_numbers_in_line)
    return map_numbers


def get_symbols_map(data) -> SymbolsMap:
    map_symbols = []  # list of (x, y) pos of symbols
    for i in range(len(data)):
        line = data[i]
        map_symbols_in_line = [
            SymbolsMapItem(row=i, col=n.start())
            # find all symbols in a row
            for n in re.finditer(r"[^0-9.]", line.strip())
        ]
        map_symbols.extend(map_symbols_in_line)
    return map_symbols


def get_part_numbers_sum(numbers_map: NumbersMap, symbols_map: SymbolsMap) -> int:
    res = {"sum_part1": 0, "sum_part2": 0}
    IDs = []
    for s in symbols_map:
        part_numbers_len = 0
        gear_ratio = 1
        for n in numbers_map:
            if (
                (n.col_span.start - 1 <= s.col <= n.col_span.end)
                and (n.row - 1 <= s.row <= n.row + 1)
                and (n.id not in IDs)  # do not count same number multiple times
            ):
                IDs.append(n.id)
                part_numbers_len += 1
                gear_ratio *= n.number
                res["sum_part1"] += n.number

        if part_numbers_len == 2:
            res["sum_part2"] += gear_ratio
    return res


def main(fn: str) -> Dict:
    data = open_file(fn)
    numbers_map = get_numbers_map(data)
    symbols_map = get_symbols_map(data)
    return get_part_numbers_sum(numbers_map, symbols_map)


def part1(fn: str = "day03.txt") -> int:
    return main(fn)["sum_part1"]


def part2(fn: str = "day03.txt") -> int:
    return main(fn)["sum_part2"]


if __name__ == "__main__":
    print("Part 1: ", part1())  # 556057
    print("Part 2: ", part2())  # 82824352
