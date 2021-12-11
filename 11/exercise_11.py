import sys
sys.path.append("..")
import helpers

neighbors = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]


def flash(x, y, input_data):
    for delta_x, delta_y in neighbors:
        affected_x, affected_y = x + delta_x, y + delta_y
        try:
            if affected_x >= 0:
                if affected_y >= 0:
                    input_data[affected_y][affected_x] += 1
        except IndexError:
            pass
    return input_data


def increment(input_data):
    for y, line in enumerate(input_data):
        for x in range(len(line)):
            input_data[y][x] += 1
    return input_data


def do_flashies(input_data, flashed):
    flashing = True
    while flashing:
        flashing = False
        for y, line in enumerate(input_data):
            for x in range(len(line)):
                if input_data[y][x] > 9:
                    if (x, y) not in flashed:
                        flashing = True
                        flashed.add((x, y))
                        input_data = flash(x, y, input_data)
    return input_data


def reset(input_data, flashed):
    for x, y in flashed:
        input_data[y][x] = 0
    flashed = set()
    return input_data, flashed


def part_one(input_filename):
    input_data = helpers.parse_input(input_filename)
    input_data = [[int(item) for item in sublist] for sublist in input_data]
    flashes = 0
    flashed = set()
    for step in range(100):
        input_data = increment(input_data)
        input_data = do_flashies(input_data, flashed)
        flashes += len(flashed)
        input_data, flashed = reset(input_data, flashed)
    return flashes


def part_two(input_filename):
    input_data = helpers.parse_input(input_filename)
    input_data = [[int(item) for item in sublist] for sublist in input_data]
    flashed = set()
    for step in range(10000000000000000000):
        input_data = increment(input_data)
        input_data = do_flashies(input_data, flashed)
        if len(flashed) == len(input_data) * len(input_data[0]):
            return step + 1 # steps are not 0-indexed
        input_data, flashed = reset(input_data, flashed)
    return "*** YOU DIED ***"


if __name__ == "__main__":
    print("*** PART ONE ***\n")
    print(f"Test result = {part_one('inputtest.txt')}\n")
    print(f"REAL RESULT = {part_one('input.txt')}\n\n")
    print("*** PART TWO ***\n")
    print(f"Test result = {part_two('inputtest.txt')}\n")
    print(f"REAL RESULT = {part_two('input.txt')}\n\n")
