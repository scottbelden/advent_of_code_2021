from collections import defaultdict
from utils import answer1, answer2, get_input

ANSWER1 = None
ANSWER2 = None

puzzle_input = get_input("day_22_input")

cubes = defaultdict(int)

for line in puzzle_input:
    on_off, rest = line.split(" ")
    x_part, y_part, z_part = rest.split(",")

    x_min, x_max = x_part[2:].split("..")
    y_min, y_max = y_part[2:].split("..")
    z_min, z_max = z_part[2:].split("..")

    x_min = max(-50, int(x_min))
    y_min = max(-50, int(y_min))
    z_min = max(-50, int(z_min))
    x_max = min(50, int(x_max))
    y_max = min(50, int(y_max))
    z_max = min(50, int(z_max))

    value = 1 if on_off == "on" else 0

    for x in range(x_min, x_max + 1):
        for y in range(y_min, y_max + 1):
            for z in range(z_min, z_max + 1):
                cubes[(x, y, z)] = value


ANSWER1 = answer1(sum(cubes.values()))

ANSWER2 = answer2(ANSWER2)
