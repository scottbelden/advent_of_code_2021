from utils import answer1, answer2, get_line_separated_inputs

ANSWER1 = None
ANSWER2 = None

inputs = get_line_separated_inputs("day_04_input")
numbers = [int(num) for num in inputs[0][0].split(",")]


class Board:
    def __init__(self, grid, nums_to_call):
        self.grid = []
        for row in grid:
            self.grid += [int(n) for n in row.split()]

        self.lines = (
            set(self.grid[0:5]),
            set(self.grid[5:10]),
            set(self.grid[10:15]),
            set(self.grid[15:20]),
            set(self.grid[20:25]),
            set(self.grid[0:25:5]),
            set(self.grid[1:25:5]),
            set(self.grid[2:25:5]),
            set(self.grid[3:25:5]),
            set(self.grid[4:25:5]),
        )

        self.nums_to_call = nums_to_call

    def __str__(self):
        return str(self.grid)

    def __repr__(self):
        return self.__str__()

    # def bingo_value(self, nums_called):
    #     for line in self.lines:
    #         if line.issubset(nums_called):
    #             return sum(set(self.grid) - nums_called)

    def bingo_score(self):
        nums_called = set()
        for index, number in enumerate(self.nums_to_call):
            nums_called.add(number)

            for line in self.lines:
                if line.issubset(nums_called):
                    return sum(set(self.grid) - nums_called) * number, index


boards = [Board(board, numbers) for board in inputs[1:]]

# answer_1 = None
# nums_called = set()
# for number in numbers:
#     nums_called.add(number)

#     for board in boards:
#         if bingo_sum := board.bingo_value(nums_called):
#             answer_1 = bingo_sum * number
#             break

#     if answer_1:
#         break

results = [board.bingo_score() for board in boards]
results.sort(key=lambda x: x[1])

ANSWER1 = answer1(results[0][0])
ANSWER2 = answer2(results[-1][0])
