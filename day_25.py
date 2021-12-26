from copy import deepcopy
from utils import answer1, get_input

ANSWER1 = None

puzzle_input = get_input("day_25_input")

sea_floor = {}

for y_index, line in enumerate(puzzle_input):
    for x_index, char in enumerate(line):
        sea_floor[(x_index, y_index)] = char

y_rows = len(puzzle_input)
x_cols = len(puzzle_input[0])


def print_sea_floor(sea_floor):
    for y_index in range(y_rows):
        print("".join(sea_floor[(x_index, y_index)] for x_index in range(x_cols)))


num_rounds = 0
while True:
    num_rounds += 1
    moved = False
    new_sea_floor_1 = deepcopy(sea_floor)

    checks = [spot for spot, value in sea_floor.items() if value == ">"]

    # copy left column to the end
    for y_index in range(y_rows):
        sea_floor[(x_cols, y_index)] = sea_floor[(0, y_index)]

    # move east
    for x_index, y_index in checks:
        if sea_floor[(x_index + 1, y_index)] == ".":
            new_sea_floor_1[((x_index + 1) % x_cols, y_index)] = ">"
            new_sea_floor_1[(x_index, y_index)] = "."
            moved = True

    new_sea_floor_2 = deepcopy(new_sea_floor_1)

    # copy top row to the end
    for x_index in range(x_cols):
        new_sea_floor_1[(x_index, y_rows)] = new_sea_floor_1[(x_index, 0)]

    # move down
    for y_index in range(y_rows):
        for x_index in range(x_cols):
            if (
                new_sea_floor_1[(x_index, y_index)] == "v"
                and new_sea_floor_1[(x_index, y_index + 1)] == "."
            ):
                new_sea_floor_2[(x_index, (y_index + 1) % y_rows)] = "v"
                new_sea_floor_2[(x_index, y_index)] = "."
                moved = True

    if moved is False:
        break

    sea_floor = deepcopy(new_sea_floor_2)


ANSWER1 = answer1(num_rounds)
