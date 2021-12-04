import sys
sys.path.append("..")
import helpers


class Cell(object):

    def __init__(self, number, active=False):
        self.number = number
        self.active = active

    def __repr__(self):
        return f"<{self.number}>"


class Board(object):

    def __init__(self):
        self.layout = []

    def __str__(self):
        return str(self.layout)

    def check_horizontal(self):
        for line in self.layout:
            win = True
            for cell in line:
                if not cell.active:
                    win = False
            if win:
                return line

    def check_vertical(self):
        for idx in range(len(self.layout[0])):
            win = True
            for line in self.layout:
                if not line[idx].active:
                    win = False
            if win:
                return [self.layout[0][idx], self.layout[1][idx], self.layout[2][idx], self.layout[3][idx], self.layout[4][idx]]

    def check_diagonal(self):
        # WHOOPS! Apparently squids don't play REAL bingo
        # win = True
        # for x, y in [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)]:
        #     if not self.layout[y][x].active:
        #         win = False
        #         break
        # if win:
        #     return [self.layout[0][0], self.layout[1][1], self.layout[2][2], self.layout[3][3], self.layout[4][4]]
        # win = True
        # for x, y in [(4, 0), (3, 1), (2, 2), (1, 3), (0, 4)]:
        #     if not self.layout[y][x].active:
        #         win = False
        #         break
        # if win:
        #     return [self.layout[4][0], self.layout[3][1], self.layout[2][2], self.layout[1][3], self.layout[0][4]]
        pass

    def sum_unmarked(self):
        sum = 0
        for line in self.layout:
            for cell in line:
                if not cell.active:
                    sum += int(cell.number)
        return sum


def create_boards(input_data):
    boards = [Board()]
    board = boards[0]
    for line in input_data[2:]:
        if line:
            numbers = (line.strip().split(" "))
            numbers = [number.strip() for number in numbers if number]
            board.layout.append([Cell(number) for number in numbers])
        else:
            boards.append(Board())
            board = boards[-1]
    return boards


def mark_number(boards, number):
    number = number.strip()
    for board in boards:
        for line in board.layout:
            for cell in line:
                if cell.number == number:
                    cell.active = True


def part_one(input_filename):
    input_data = helpers.parse_input(input_filename)
    called_numbers = input_data[0]
    boards = create_boards(input_data)
    for number in called_numbers.split(","):
        mark_number(boards, number)
        for board in boards:
            if board.check_vertical():
                return f"number = {number}, sum = {board.sum_unmarked()}, answer = {int(number) * board.sum_unmarked()}"
            elif board.check_horizontal():
                return f"number = {number}, sum = {board.sum_unmarked()}, answer = {int(number) * board.sum_unmarked()}"


def part_two(input_filename):
    input_data = helpers.parse_input(input_filename)
    called_numbers = input_data[0]
    boards = create_boards(input_data)
    for number in called_numbers.split(","):
        mark_number(boards, number)
        for board in boards:
            if board.check_vertical():
                if len(boards) == 1:
                    return f"number = {number}, sum = {boards[0].sum_unmarked()}, answer = {int(number) * boards[0].sum_unmarked()}"
                else:
                    boards.remove(board)
            elif board.check_horizontal():
                if len(boards) == 1:
                    return f"number = {number}, sum = {boards[0].sum_unmarked()}, answer = {int(number) * boards[0].sum_unmarked()}"
                else:
                    boards.remove(board)


if __name__ == "__main__":
    print("*** PART ONE ***\n")
    print(f"Test result = {part_one('inputtest.txt')}\n")
    print(f"REAL RESULT = {part_one('input.txt')}\n\n")
    print("*** PART TWO ***\n")
    print(f"Test result = {part_two('inputtest.txt')}\n")
    print(f"REAL RESULT = {part_two('input.txt')}")
