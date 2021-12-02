from utils import answer1, answer2, get_input

ANSWER1 = None
ANSWER2 = None

commands = get_input("day_02_input")

horizontal = 0
depth = 0
for command in commands:
    direction, distance = command.split()
    distance = int(distance)
    match direction:
        case "forward":
            horizontal += distance
        case "down":
            depth += distance
        case "up":
            depth -= distance

ANSWER1 = answer1(horizontal * depth)

horizontal = 0
depth = 0
aim = 0
for command in commands:
    direction, distance = command.split()
    distance = int(distance)
    match direction:
        case "forward":
            horizontal += distance
            depth += aim * distance
        case "down":
            aim += distance
        case "up":
            aim -= distance

ANSWER2 = answer2(horizontal * depth)
