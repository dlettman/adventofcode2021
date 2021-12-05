import sys
sys.path.append("..")
import helpers

def parse_lines(line):
    line = line.split(" -> ")
    line = [item.split(",") for item in line]
    line = [[int(x) for x in lst] for lst in line]
    return line


def get_diagonal_line(x1, y1, x2, y2):
    if y2 > y1:
        if x1 > x2:
            direction = (-1, 1)
        else:
            direction = (1, 1)
    else:
        # y1 > y2
        if x1 > x2:
            direction = (-1, -1)
        else:
            direction = (1, -1)
    points = []
    points.append((x2, y2))
    previous_point = (x1, y1)
    points.append(previous_point)
    while (previous_point[0] + direction[0], previous_point[1] + direction[1]) != (x2, y2):
        previous_point = (previous_point[0] + direction[0], previous_point[1] + direction[1])
        points.append(previous_point)
    return points


def part_one(input_filename):
    input_data = helpers.parse_input(input_filename)
    input_data = [parse_lines(line) for line in input_data]
    coordinate_counter = {}
    for line in input_data:
        # parse vertical
        if line[0][0] == line[1][0]:
            for y in range(min(line[0][1], line[1][1]), (max(line[0][1], line[1][1]) + 1)):
                if (line[0][0],y) not in coordinate_counter:
                    coordinate_counter[(line[0][0],y)] = 1
                else:
                    coordinate_counter[(line[0][0],y)] += 1
        # parse horizontal
        elif line[0][1] == line[1][1]:
            for x in range(min(line[0][0], line[1][0]), (max(line[0][0], line[1][0]) + 1)):
                if (x,line[0][1]) not in coordinate_counter:
                    coordinate_counter[x,line[0][1]] = 1
                else:
                    coordinate_counter[x,line[0][1]] += 1
    return len([key for key in coordinate_counter.keys() if coordinate_counter[key] >= 2])


def part_two(input_filename):
    input_data = helpers.parse_input(input_filename)
    input_data = [parse_lines(line) for line in input_data]
    coordinate_counter = {}
    for line in input_data:
        # parse vertical
        if line[0][0] == line[1][0]:
            for y in range(min(line[0][1], line[1][1]), (max(line[0][1], line[1][1]) + 1)):
                if (line[0][0],y) not in coordinate_counter:
                    coordinate_counter[(line[0][0],y)] = 1
                else:
                    coordinate_counter[(line[0][0],y)] += 1
        # parse horizontal
        elif line[0][1] == line[1][1]:
            for x in range(min(line[0][0], line[1][0]), (max(line[0][0], line[1][0]) + 1)):
                if (x,line[0][1]) not in coordinate_counter:
                    coordinate_counter[x,line[0][1]] = 1
                else:
                    coordinate_counter[x,line[0][1]] += 1
        else:
        # diagonal
            points = get_diagonal_line(line[0][0], line[0][1], line[1][0], line[1][1])
            for point in points:
                if point not in coordinate_counter:
                    coordinate_counter[point] = 1
                else:
                    coordinate_counter[point] += 1
    return len([key for key in coordinate_counter.keys() if coordinate_counter[key] >= 2])


if __name__ == "__main__":
    print("*** PART ONE ***\n")
    print(f"Test result = {part_one('inputtest.txt')}\n")
    print(f"REAL RESULT = {part_one('input.txt')}\n\n")
    print("*** PART TWO ***\n")
    print(f"Test result = {part_two('inputtest.txt')}\n")
    print(f"REAL RESULT = {part_two('input.txt')}")
