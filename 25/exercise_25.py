import sys
sys.path.append("..")
import helpers


def build_map(input_data):
    down_cucumbers = set()
    right_cucumbers = set()
    for y, line in enumerate(input_data):
        for x, char in enumerate(line):
            if char == "v":
                down_cucumbers.add((x, y))
            elif char == ">":
                right_cucumbers.add((x, y))
    return down_cucumbers, right_cucumbers


def part_one(input_filename):
    input_data = helpers.parse_input(input_filename)
    max_y = len(input_data) - 1
    max_x = len(input_data[0]) - 1
    down_cucumbers, right_cucumbers = build_map(input_data)
    step = 0
    changed = True
    while changed:
        print(step)
        print("\n".join(print_debug(down_cucumbers, right_cucumbers, max_x, max_y)))
        step += 1
        new_rc = set()
        new_dc = set()
        changed = False
        for cucumber in right_cucumbers:
            x_to_eval = 0 if cucumber[0] == max_x else (cucumber[0] + 1)
            coord_to_eval = (x_to_eval, cucumber[1])
            if coord_to_eval not in down_cucumbers and coord_to_eval not in right_cucumbers:
                new_rc.add((x_to_eval, cucumber[1]))
                changed = True
            else:
                new_rc.add(cucumber)
        right_cucumbers = new_rc
        for cucumber in down_cucumbers:
            y_to_eval = 0 if cucumber[1] == max_y else (cucumber[1] + 1)
            coord_to_eval = (cucumber[0], y_to_eval)
            if coord_to_eval not in down_cucumbers and coord_to_eval not in right_cucumbers:
                new_dc.add((cucumber[0], y_to_eval))
                changed = True
            else:
                new_dc.add(cucumber)
        down_cucumbers = new_dc
    return step


def print_debug(dc, rc, max_x, max_y):
    map = []
    for y in range(max_y + 1):
        line = []
        for x in range(max_x + 1):
            if (x, y) in rc:
                line.append(">")
            elif (x, y) in dc:
                line.append("v")
            else:
                line.append(".")
        map.append(line)
    return ["".join(line) for line in map]


def part_two(input_filename):
    input_data = helpers.parse_input(input_filename)
    if not input_data:
        return "*** NO INPUT SUPPLIED ***"
    # do stuff here
    output = input_data
    return output

if __name__ == "__main__":
    print("*** PART ONE ***\n")
    print(f"Test result = {part_one('inputtest.txt')}\n")
    print(f"REAL RESULT = {part_one('input.txt')}\n\n")
    # print("*** PART TWO ***\n")
    # print(f"Test result = {part_two('inputtest.txt')}\n")
    # print(f"REAL RESULT = {part_two('input.txt')}\n\n")
