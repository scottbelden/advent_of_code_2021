from collections import defaultdict
from utils import answer1, answer2, get_input

ANSWER1 = None
ANSWER2 = None

# 0: 6
# 1: 2
# 2: 5
# 3: 5
# 4: 4
# 5: 5
# 6: 6
# 7: 3
# 8: 7
# 9: 6


puzzle_input = get_input("day_08_input")

easy_digit = 0
for line in puzzle_input:
    inputs, outputs = line.split(" | ")
    for output in outputs.split():
        if len(output) in {2, 3, 4, 7}:
            easy_digit += 1

ANSWER1 = answer1(easy_digit)

total_sum = 0
for index, line in enumerate(puzzle_input):
    inputs, outputs = line.split(" | ")
    input_lengths = defaultdict(list)
    for input_ in inputs.split():
        input_lengths[len(input_)].append(input_)

    seven_digit_segments = set(input_lengths[3][0])
    one_digit_segments = set(input_lengths[2][0])
    four_digit_segments = set(input_lengths[4][0])
    eight_digit_segments = set(input_lengths[7][0])

    TOP = seven_digit_segments - one_digit_segments

    for num in input_lengths[6]:
        if len(set(num) & one_digit_segments) == 1:
            six_digit_segments = set(num)
            BOTTOM_RIGHT = set(num) & one_digit_segments
            TOP_RIGHT = one_digit_segments - BOTTOM_RIGHT
            break

    for num in input_lengths[5]:
        if len(set(num) & seven_digit_segments) == 3:
            three_digit_segments = set(num)
            MIDDLE = three_digit_segments & four_digit_segments - one_digit_segments
            BOTTOM = three_digit_segments - seven_digit_segments - MIDDLE
            TOP_LEFT = four_digit_segments - three_digit_segments
            BOTTOM_LEFT = (
                set(input_lengths[7][0])
                - TOP
                - TOP_LEFT
                - TOP_RIGHT
                - MIDDLE
                - BOTTOM_RIGHT
                - BOTTOM
            )
            break

    two_digit_segments = TOP | TOP_RIGHT | MIDDLE | BOTTOM_LEFT | BOTTOM
    five_digit_segments = TOP | TOP_LEFT | MIDDLE | BOTTOM_RIGHT | BOTTOM

    set_to_int = {
        tuple(
            sorted(TOP | TOP_LEFT | TOP_RIGHT | BOTTOM_LEFT | BOTTOM_RIGHT | BOTTOM)
        ): "0",
        tuple(sorted(one_digit_segments)): "1",
        tuple(sorted(TOP | TOP_RIGHT | MIDDLE | BOTTOM_LEFT | BOTTOM)): "2",
        tuple(sorted(three_digit_segments)): "3",
        tuple(sorted(four_digit_segments)): "4",
        tuple(sorted(TOP | TOP_LEFT | MIDDLE | BOTTOM_RIGHT | BOTTOM)): "5",
        tuple(sorted(six_digit_segments)): "6",
        tuple(sorted(seven_digit_segments)): "7",
        tuple(sorted(eight_digit_segments)): "8",
        tuple(sorted(TOP | TOP_LEFT | TOP_RIGHT | MIDDLE | BOTTOM_RIGHT | BOTTOM)): "9",
    }

    output_num = ""
    for output in outputs.split():
        output_num += set_to_int[tuple(sorted(set(output)))]

    total_sum += int(output_num)

ANSWER2 = answer2(total_sum)
