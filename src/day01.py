import regex as re 

### Part 1
DATA_DIR = "../input/"
DATA_FN = "day01_p1.txt"
f = open(DATA_DIR + DATA_FN)

tot_sum = 0
for line in f.readlines():
    m = re.findall(r"\d", line)
    if len(m)>0:
        tot_sum += int(m[0] + m[-1])

print("Part 1 solution: ", tot_sum)


### Part 2
DATA_DIR = "../input/"
DATA_FN = "day01_p2.txt"
f = open(DATA_DIR + DATA_FN)

numbers_map = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

tot_sum = 0
for line in f.readlines():
    m = re.findall(
        r"\d|one|two|three|four|five|six|seven|eight|nine", 
        line, overlapped=True
        )
    if len(m)>0:
        first_digit = numbers_map.get(m[0], m[0])
        last_digit = numbers_map.get(m[-1], m[-1])
        print(first_digit, last_digit)
        tot_sum += int(first_digit + last_digit)

print("Part 2 solution: ", tot_sum)

