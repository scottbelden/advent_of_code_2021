from utils import answer1, answer2, get_input_as_str

ANSWER1 = None
ANSWER2 = None

puzzle_input = get_input_as_str("day_17_input")

_, x_and_y = puzzle_input.split(": ")
x_range, y_range = x_and_y.split(", ")
x_min, x_max = x_range[2:].split("..")
y_min, y_max = y_range[2:].split("..")

x_min = int(x_min)
x_max = int(x_max)
y_min = int(y_min)
y_max = int(y_max)


def simulate(x_vel, y_vel):
    max_height = 0
    x_current = 0
    y_current = 0

    while True:
        x_current += x_vel
        y_current += y_vel

        if y_vel > 0:
            max_height = y_current

        if x_min <= x_current <= x_max and y_min <= y_current <= y_max:
            # in target
            return max_height
        elif x_current > x_max or y_current < y_min:
            # over shot
            return None

        y_vel -= 1
        if x_vel > 0:
            x_vel -= 1
        elif x_vel < 0:
            x_vel += 1


test_x = 1
while True:
    if (test_x * (test_x + 1)) / 2 >= x_min:
        break
    test_x += 1

max_height = 0
test_y = 1
tests_remaining = 50
while True:
    if output := simulate(test_x, test_y):
        max_height = output
        tests_remaining = 50
    elif tests_remaining == 0:
        break
    else:
        tests_remaining -= 1
    test_y += 1

ANSWER1 = answer1(max_height)

total_hits = 0
while test_x <= x_max:
    test_y = -90
    tests_remaining = 200

    while True:
        if simulate(test_x, test_y) is not None:
            tests_remaining = 50
            total_hits += 1
        elif tests_remaining == 0:
            break
        else:
            tests_remaining -= 1
        test_y += 1

    test_x += 1


ANSWER2 = answer2(total_hits)
