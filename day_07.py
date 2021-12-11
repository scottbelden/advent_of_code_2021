from statistics import median
from utils import answer1, answer2, get_input

ANSWER1 = None
ANSWER2 = None

puzzle_input = get_input("day_07_input")
crabs = [int(c) for c in puzzle_input[0].split(",")]

ideal_horizontal = median(crabs)

total_fuel = 0
for crab in crabs:
    total_fuel += abs(crab - ideal_horizontal)

ANSWER1 = answer1(int(total_fuel))


def bisect(min_value, max_value):
    last_round = False
    if min_value + 1 == max_value:
        last_round = True

    if last_round:
        halfway = max_value
    else:
        halfway = round((min_value + max_value) / 2)

    total_fuel_halfway = 0
    for crab in crabs:
        distance = abs(crab - halfway)
        total_fuel_halfway += distance * (distance + 1) / 2

    total_fuel_halfway_left = 0
    for crab in crabs:
        distance = abs(crab - (halfway - 1))
        total_fuel_halfway_left += distance * (distance + 1) / 2

    if last_round:
        return min(total_fuel_halfway_left, total_fuel_halfway)
    elif total_fuel_halfway_left < total_fuel_halfway:
        return bisect(min_value, halfway - 1)
    else:
        return bisect(halfway, max_value)


min_crab = min(crabs)
max_crab = max(crabs)

ANSWER2 = answer2(int(bisect(min_crab, max_crab)))
