from collections import defaultdict
from utils import answer1, answer2, get_input

ANSWER1 = None
ANSWER2 = None

vents = get_input("day_05_input")

counts = defaultdict(int)
for vent in vents:
    left, right = vent.split(" -> ")
    x1s, y1s = left.split(",")
    x2s, y2s = right.split(",")

    x1 = int(x1s)
    y1 = int(y1s)
    x2 = int(x2s)
    y2 = int(y2s)

    if x1 == x2:
        miny = min(y1, y2)
        for i in range(miny, miny + abs(y2 - y1) + 1):
            counts[(x1, i)] += 1
    elif y1 == y2:
        minx = min(x1, x2)
        for i in range(minx, minx + abs(x2 - x1) + 1):
            counts[(i, y1)] += 1
    else:
        continue

overlaps = sum([1 for count in counts.values() if count > 1])
ANSWER1 = answer1(overlaps)

counts = defaultdict(int)
for vent in vents:
    left, right = vent.split(" -> ")
    x1s, y1s = left.split(",")
    x2s, y2s = right.split(",")

    x1 = int(x1s)
    y1 = int(y1s)
    x2 = int(x2s)
    y2 = int(y2s)

    if x1 == x2:
        miny = min(y1, y2)
        for i in range(miny, miny + abs(y2 - y1) + 1):
            counts[(x1, i)] += 1
    elif y1 == y2:
        minx = min(x1, x2)
        for i in range(minx, minx + abs(x2 - x1) + 1):
            counts[(i, y1)] += 1
    else:
        dy = 1 if y2 - y1 > 0 else -1
        dx = 1 if x2 - x1 > 0 else -1
        lenx = abs(x2 - x1)

        for i in range(lenx + 1):
            counts[(x1 + (i * dx), y1 + (i * dy))] += 1

overlaps = sum([1 for count in counts.values() if count > 1])
ANSWER2 = answer2(overlaps)
