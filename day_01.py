from utils import answer1, answer2, get_input_as_int

ANSWER1 = None
ANSWER2 = None

depths = get_input_as_int("day_01_input")

increase_counter = 0
for index, depth in enumerate(depths):
    if index == 0:
        continue
    elif depth > depths[index - 1]:
        increase_counter += 1

ANSWER1 = answer1(increase_counter)

increase_counter = 0
for index, depth in enumerate(depths):
    if index < 3:
        continue
    elif depth > depths[index - 3]:
        increase_counter += 1

ANSWER2 = answer2(increase_counter)
