data_dir = "data/data_2024/"
filename = "day01_p1.txt"


def read_data() -> tuple[list[int], list[int]]:
    f = open(data_dir + filename)
    left_list = []
    right_list = []

    for line in f.readlines():
        left_list.append(int(line.split()[0].strip()))
        right_list.append(int(line.split()[1].strip()))

    return left_list, right_list


def part1(left_list: list[int], right_list: list[int]) -> int:
    left_list_sorted = sorted(left_list)
    right_list_sorted = sorted(right_list)

    output = 0
    for i in range(len(left_list_sorted)):
        output += abs(right_list_sorted[i] - left_list_sorted[i])

    return output


def part2(left_list: list[int], right_list: list[int]) -> int:
    output = 0
    for el in left_list:
        output += el * right_list.count(el)
    return output


if __name__ == "__main__":
    left_list, right_list = read_data()
    print("Part 1: ", part1(left_list, right_list))  # 1319616
    print("Part 2: ", part2(left_list, right_list))  # 27267728
