import importlib

day_n = int(
    input(
        "Input the number corresponding to the day of the challenge you want to run: "
    )
)

# add leading 0 to single digit numbers
lib_name = f"day{day_n:02d}"

# dynamically import the module
module = importlib.import_module(f"challenges.{lib_name}")

# use getattr to dynamically import the part1 function from the module
day_fun_p1 = getattr(module, "part1")
day_fun_p2 = getattr(module, "part2")
print(f"Day {day_n} - Part1: {day_fun_p1()}")
print(f"Day {day_n} - Part2: {day_fun_p2()}")
