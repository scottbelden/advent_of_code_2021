from utils import answer1, answer2, get_input_as_str

ANSWER1 = None
ANSWER2 = None

fishies = [int(f) for f in get_input_as_str("day_06_input").split(",")]

memoized = {}


def get_children(initial_state, total_days, memoized, space):
    children = 0

    if answer := memoized.get((initial_state, total_days)):
        return answer

    if initial_state >= total_days:
        children = 0
    else:
        remaining_days = total_days - (initial_state + 1)

        while True:
            children += 1 + get_children(8, remaining_days, memoized, space + 1)
            remaining_days -= 7
            if remaining_days >= 0:
                continue
            else:
                break

    memoized[(initial_state, total_days)] = children
    return children


total_fish = 0
TOTAL_DAYS = 80
for fish in fishies:
    total_fish += 1 + get_children(fish, TOTAL_DAYS, memoized, 0)


ANSWER1 = answer1(total_fish)

total_fish = 0
TOTAL_DAYS = 256
for fish in fishies:
    total_fish += 1 + get_children(fish, TOTAL_DAYS, memoized, 0)

ANSWER2 = answer2(total_fish)
