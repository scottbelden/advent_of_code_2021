from utils import answer1, answer2, get_input

ANSWER1 = None
ANSWER2 = None

puzzle_input = get_input("day_09_input")

rows = len(puzzle_input)
columns = len(puzzle_input[0])

matrix = [[10 for i in range(columns + 2)] for j in range(rows + 2)]

for r_idx, row in enumerate(puzzle_input):
    for c_idx, char in enumerate(row):
        matrix[r_idx + 1][c_idx + 1] = int(char)

total_risk = 0
for r_idx, row in enumerate(matrix):
    for c_idx, height in enumerate(row):
        if (
            height < matrix[r_idx - 1][c_idx]
            and height < matrix[r_idx + 1][c_idx]
            and height < matrix[r_idx][c_idx - 1]
            and height < matrix[r_idx][c_idx + 1]
        ):
            total_risk += height + 1

ANSWER1 = answer1(total_risk)


def get_basin(row, column, points):
    if (row, column) in points:
        return

    height = matrix[row][column]
    if height < 9:
        points.add((row, column))
        get_basin(row - 1, column, points)
        get_basin(row + 1, column, points)
        get_basin(row, column - 1, points)
        get_basin(row, column + 1, points)


basins = []

for r_idx, row in enumerate(matrix):
    for c_idx, height in enumerate(row):
        if (
            height < matrix[r_idx - 1][c_idx]
            and height < matrix[r_idx + 1][c_idx]
            and height < matrix[r_idx][c_idx - 1]
            and height < matrix[r_idx][c_idx + 1]
        ):
            points = set()
            get_basin(r_idx, c_idx, points)
            basins.append(len(points))

basins.sort()

ANSWER2 = answer2(basins[-1] * basins[-2] * basins[-3])
