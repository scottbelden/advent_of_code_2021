from utils import answer1, answer2, get_input

ANSWER1 = None
ANSWER2 = None

puzzle_input = get_input("day_13_input")

dots = set()
for line in puzzle_input:
    if line and not line.startswith("fold"):
        strx, stry = line.split(",")
        dots.add((int(strx), int(stry)))
    elif line.startswith("fold"):
        _, _, fold_line = line.split()
        axis, str_value = fold_line.split("=")
        value = int(str_value)

        if axis == "y":
            stationary = {dot for dot in dots if dot[1] < value}
            moves = {
                (row, (2 * value) - column) for row, column in dots if column > value
            }
            dots = stationary | moves
        else:
            stationary = {dot for dot in dots if dot[0] < value}
            moves = {((2 * value) - row, column) for row, column in dots if row > value}
            dots = stationary | moves
        break

ANSWER1 = answer1(len(dots))

dots = set()
for line in puzzle_input:
    if line and not line.startswith("fold"):
        strx, stry = line.split(",")
        dots.add((int(strx), int(stry)))
    elif line.startswith("fold"):
        _, _, fold_line = line.split()
        axis, str_value = fold_line.split("=")
        value = int(str_value)

        if axis == "y":
            stationary = {dot for dot in dots if dot[1] < value}
            moves = {
                (row, (2 * value) - column) for row, column in dots if column > value
            }
            dots = stationary | moves
        else:
            stationary = {dot for dot in dots if dot[0] < value}
            moves = {((2 * value) - row, column) for row, column in dots if row > value}
            dots = stationary | moves

sorted_x = sorted(dots)
max_x = sorted_x[-1][0]
max_y = sorted_x[-1][1]

output = [[" " for i in range(max_x + 1)] for j in range(max_y + 1)]

for column, row in sorted_x:
    output[row][column] = "*"

for row in output:
    print("".join(row))

ANSWER2 = answer2("RHALRCRA")
