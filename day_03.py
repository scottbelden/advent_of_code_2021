from collections import defaultdict
from utils import answer1, answer2, get_input

ANSWER1 = None
ANSWER2 = None

numbers = get_input("day_03_input")

counter = defaultdict(int)
total_numbers = len(numbers)
for number in numbers:
    for index, digit in enumerate(number):
        counter[index] += int(digit)

gamma = ""
epsilon = ""

for index, count in counter.items():
    if count > total_numbers / 2:
        gamma += "1"
        epsilon += "0"
    else:
        gamma += "0"
        epsilon += "1"

ANSWER1 = answer1(int(gamma, 2) * int(epsilon, 2))

numbers_copy = [num for num in numbers]
index = -1
while True:
    if len(numbers_copy) == 1:
        oxygen_rating = numbers_copy[0]
        break

    index += 1
    zeroes = [num for num in numbers_copy if num[index] == "0"]
    ones = [num for num in numbers_copy if num[index] == "1"]

    if len(zeroes) > len(ones):
        numbers_copy = zeroes
    elif len(ones) > len(zeroes):
        numbers_copy = ones
    else:
        numbers_copy = ones

numbers_copy = [num for num in numbers]
index = -1
while True:
    if len(numbers_copy) == 1:
        c02_rating = numbers_copy[0]
        break

    index += 1
    zeroes = [num for num in numbers_copy if num[index] == "0"]
    ones = [num for num in numbers_copy if num[index] == "1"]

    if len(zeroes) < len(ones):
        numbers_copy = zeroes
    elif len(ones) < len(zeroes):
        numbers_copy = ones
    else:
        numbers_copy = zeroes

ANSWER2 = answer2(int(oxygen_rating, 2) * int(c02_rating, 2))
