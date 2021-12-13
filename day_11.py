from utils import answer1, answer2, get_input

ANSWER1 = None
ANSWER2 = None

puzzle_input = get_input("day_11_input")

matrix = {}

for r_idx, row in enumerate(puzzle_input):
    for c_idx, value in enumerate(row):
        matrix[(r_idx, c_idx)] = int(value)

TOTAL_BURSTS = 0


def spread(row, column):
    global TOTAL_BURSTS
    TOTAL_BURSTS += 1
    all_spots = [
        (row - 1, column - 1),
        (row - 1, column),
        (row - 1, column + 1),
        (row, column - 1),
        (row, column + 1),
        (row + 1, column - 1),
        (row + 1, column),
        (row + 1, column + 1),
    ]
    valid_spots = [spot for spot in all_spots if spot in matrix]

    for spot in valid_spots:
        matrix[spot] += 1
        if matrix[spot] == 10:
            spread(spot[0], spot[1])


ROUNDS = 100
for round_num in range(ROUNDS):
    for (row, column), value in matrix.items():
        matrix[(row, column)] += 1
        if value == 9:
            spread(row, column)

    for (row, column), value in matrix.items():
        if matrix[(row, column)] > 9:
            matrix[(row, column)] = 0


ANSWER1 = answer1(TOTAL_BURSTS)


for r_idx, row in enumerate(puzzle_input):
    for c_idx, value in enumerate(row):
        matrix[(r_idx, c_idx)] = int(value)

round_counter = 0
while True:
    round_counter += 1
    current_bursts = TOTAL_BURSTS
    for (row, column), value in matrix.items():
        matrix[(row, column)] += 1
        if value == 9:
            spread(row, column)

    if TOTAL_BURSTS - current_bursts == 100:
        break

    for (row, column), value in matrix.items():
        if matrix[(row, column)] > 9:
            matrix[(row, column)] = 0


ANSWER2 = answer2(round_counter)
