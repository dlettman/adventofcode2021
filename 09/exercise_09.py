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
                print(f"low point found: ({x},{y}) {char}")
                risk += int(char) + 1
    return risk

def part_two(input_filename):
    input_data = helpers.parse_input(input_filename)
    low_points = get_low_points(input_data)
    basins = []
    # coords are tuples of (x, y)
    for low_point in low_points:
        basin = [low_point]
        print(f"basin = {basin}")
        found_a_new_one = True
        while found_a_new_one:
            found_a_new_one = False
            new_basin = basin
            for point in basin:
                print(f"basin = {basin}")
                x, y = point[0], point[1]
                char = input_data[y][x]
                for mod in [(y + 1), (y - 1)]:
                    try:
                        if 9 > int(input_data[mod][x]) > int(char):
                            if mod >= 0:
                                if (x, mod) not in basin:
                                    found_a_new_one = True
                                    new_basin.append((x, mod))
                    except IndexError:
                        pass
                for mod in [(x + 1), (x - 1)]:
                    try:
                        if 9 > int(input_data[y][mod]) > int(char):
                            if mod >= 0:
                                if (mod, y) not in basin:
                                  found_a_new_one = True
                                  new_basin.append((mod, y))
                    except IndexError:
                        pass
            basin = new_basin
        basins.append(len(basin))
    top_3 = sorted(basins)[-3:]
    return reduce((lambda x, y: x * y), top_3)




if __name__ == "__main__":
    print("*** PART ONE ***\n")
    # print(f"Test result = {part_one('inputtest.txt')}\n")
    # print(f"REAL RESULT = {part_one('input.txt')}\n\n")
    print("*** PART TWO ***\n")
    print(f"Test result = {part_two('inputtest.txt')}\n")
    print(f"REAL RESULT = {part_two('input.txt')}")
