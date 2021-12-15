import sys
import heapq
sys.path.append("..")
import helpers


NEIGHBORS = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def create_map(input_data, scale_factor):
    rows = []
    coord_risk_dict = {}
    for y_iter in range(scale_factor):
        for row in input_data:
            new_row = []
            for x_iter in range(scale_factor):
            # for x_iter in range(1):
                new_row += ([int(item) + x_iter + y_iter for item in row])
            for idx, num in enumerate(new_row):
                if num > 9:
                    new_row[idx] = num - 9
            rows.append(new_row)
    for y, row in enumerate(rows):
        for x, value in enumerate(row):
            coord_risk_dict[(x, y)] = value
    return coord_risk_dict


def part_one(input_filename):  #  AKA solution if you can only go down or right
    input_data = helpers.parse_input(input_filename)
    input_data = [[int(item) for item in sublist] for sublist in input_data]
    max_x = len(input_data[0])
    max_y = len(input_data)
    # do first row
    for idx in range(1, max_x):
        input_data[0][idx] = input_data[0][idx] + input_data[0][idx-1]
    # do first column
    for idx in range(1, max_x):
        input_data[idx][0] = input_data[idx][0] + input_data[idx-1][0]
    for y in range(1, max_y):
        for x in range(1, max_x):
            if input_data[x-1][y] < input_data[x][y-1]:
                input_data[x][y] = input_data[x][y] + input_data[x-1][y]
            else:
                input_data[x][y] = input_data[x][y] + input_data[x][y-1]
    return input_data[max_y - 1][max_x - 1] - input_data[0][0]


def part_two(input_filename):  # AKA Dijkstra's
    input_data = helpers.parse_input(input_filename)
    scale_mod = 5
    bigmap = create_map(input_data, scale_mod)
    max_x = len(input_data[0] * scale_mod)
    max_y = len(input_data * scale_mod)
    total_risks = {key: None for key in bigmap.keys()}
    total_risks[(0, 0)] = 0
    queue = [(0, 0, 0)]
    while not total_risks[(max_x - 1), (max_y - 1)]:
        risk, x, y = heapq.heappop(queue)
        for delta_x, delta_y in NEIGHBORS:
            new_x, new_y = x + delta_x, y + delta_y
            if 0 <= new_x < max_x and 0 <= new_y < max_y and not total_risks[(new_x, new_y)]:
                total_risks[(new_x, new_y)] = risk + bigmap[(new_x, new_y)]
                heapq.heappush(queue, (total_risks[(new_x, new_y)], new_x, new_y))
    return total_risks[(max_x - 1, max_y - 1)]


if __name__ == "__main__":
    print("*** PART ONE ***\n")
    print(f"Test result = {part_one('inputtest.txt')}\n")
    print(f"Test 2 result = {part_one('inputtest2.txt')}\n")
    print(f"REAL RESULT = {part_one('input.txt')}\n\n")
    print("*** PART TWO ***\n")
    print(f"Test result = {part_two('inputtest.txt')}\n")
    print(f"Test result = {part_two('inputtest2.txt')}\n")
    print(f"REAL RESULT = {part_two('input.txt')}\n\n")
