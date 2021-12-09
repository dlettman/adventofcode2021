import sys
from functools import reduce
sys.path.append("..")
import helpers


def get_low_points(input_data):
    low_points = []
    for y, line in enumerate(input_data):
        for x, char in enumerate(line):
            low_point = True
            for mod in [(y + 1), (y - 1)]:
                try:
                    if int(input_data[mod][x]) <= int(char):
                        if mod >= 0:
                            low_point = False
                except IndexError:
                    pass
            for mod in [(x - 1), (x + 1)]:
                try:
                    if int(input_data[y][mod]) <= int(char):
                        if mod >= 0:
                            low_point = False
                except IndexError:
                    pass
            if low_point:
                low_points.append((int(x), int(y)))
    return low_points


def part_one(input_filename):
    input_data = helpers.parse_input(input_filename)
    risk = 0
    low_points = get_low_points(input_data)
    for low_point in low_points:
        x, y = low_point[0], low_point[1]
        risk += int(input_data[y][x]) + 1
    return risk


def part_two(input_filename):
    input_data = helpers.parse_input(input_filename)
    low_points = get_low_points(input_data)
    basins = []
    # coords are tuples of (x, y)
    for low_point in low_points:
        basin = [low_point]
        added_a_new_point = True
        while added_a_new_point:
            added_a_new_point = False
            new_basin = basin
            for point in basin:
                x, y = point[0], point[1]
                char = input_data[y][x]
                for mod in [(y + 1), (y - 1)]:
                    try:
                        if 9 > int(input_data[mod][x]) > int(char):
                            if mod >= 0:
                                if (x, mod) not in basin:
                                    added_a_new_point = True
                                    new_basin.append((x, mod))
                    except IndexError:
                        pass
                for mod in [(x + 1), (x - 1)]:
                    try:
                        if 9 > int(input_data[y][mod]) > int(char):
                            if mod >= 0:
                                if (mod, y) not in basin:
                                  added_a_new_point = True
                                  new_basin.append((mod, y))
                    except IndexError:
                        pass
            basin = new_basin
        basins.append(len(basin))
    return reduce((lambda a, b: a * b), sorted(basins)[-3:])


if __name__ == "__main__":
    print("*** PART ONE ***\n")
    print(f"Test result = {part_one('inputtest.txt')}\n")
    print(f"REAL RESULT = {part_one('input.txt')}\n\n")
    print("*** PART TWO ***\n")
    print(f"Test result = {part_two('inputtest.txt')}\n")
    print(f"REAL RESULT = {part_two('input.txt')}")
