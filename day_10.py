import re
from utils import answer1, answer2, get_input

ANSWER1 = None
ANSWER2 = None

puzzle_input = get_input("day_10_input")

total_points = 0
for line in puzzle_input:
    while True:
        orig_len = len(line)
        line = line.replace("()", "")
        line = line.replace("[]", "")
        line = line.replace("{}", "")
        line = line.replace("<>", "")
        final_len = len(line)
        if final_len == orig_len:
            break

    points = 0
    start = 9999
    if match := re.search(r"(\(|\[|{|<)\)", line):
        if match.start() < start:
            start = match.start()
            points = 3
    if match := re.search(r"(\(|\[|{|<)\]", line):
        if match.start() < start:
            start = match.start()
            points = 57
    if match := re.search(r"(\(|\[|{|<)}", line):
        if match.start() < start:
            start = match.start()
            points = 1197
    if match := re.search(r"(\(|\[|{|<)>", line):
        if match.start() < start:
            start = match.start()
            points = 25137

    total_points += points


ANSWER1 = answer1(total_points)


all_scores = []
for line in puzzle_input:
    while True:
        orig_len = len(line)
        line = line.replace("()", "")
        line = line.replace("[]", "")
        line = line.replace("{}", "")
        line = line.replace("<>", "")
        final_len = len(line)
        if final_len == orig_len:
            break

    if re.search(r"(\(|\[|{|<)(\)|\]|}|>)", line):
        continue

    score = 0
    for char in reversed(line):
        score *= 5
        match char:
            case "(":
                score += 1
            case "[":
                score += 2
            case "{":
                score += 3
            case "<":
                score += 4

    if score > 0:
        all_scores.append(score)

num_scores = len(all_scores)
ANSWER2 = answer2(sorted(all_scores)[int((num_scores - 1) / 2)])
