from collections import Counter, deque
from utils import answer1, answer2, get_input

ANSWER1 = None
ANSWER2 = None

puzzle_input = get_input("day_14_input")

start_polymer = deque(puzzle_input[0])

transformations = {}
for instruction in puzzle_input[2:]:
    input_side, output_side = instruction.split(" -> ")
    transformations[input_side] = output_side

for i in range(10):
    for j in range(len(start_polymer) - 1):
        start_polymer.rotate()
        start_polymer.appendleft(transformations[start_polymer[-1] + start_polymer[0]])

    start_polymer.rotate()

counter = Counter(start_polymer)
freqencies = counter.most_common()

ANSWER1 = answer1(freqencies[0][1] - freqencies[-1][1])

ANSWER2 = answer2(ANSWER2)
# for i in range(30):
#     print(i)
#     for j in range(len(start_polymer) - 1):
#         start_polymer.rotate()
#         start_polymer.appendleft(transformations[start_polymer[-1] + start_polymer[0]])

#     start_polymer.rotate()

# counter = Counter(start_polymer)
# freqencies = counter.most_common()

# ANSWER2 = answer2(freqencies[0][1] - freqencies[-1][1])
