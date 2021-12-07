import sys
sys.path.append("..")
import helpers

def part_one(input_filename):
    input_data = helpers.parse_input(input_filename)[0].split(",")
    input_data = [int(item) for item in input_data]
    best_solution = None
    for i in range(max(input_data)):
        total_diff = 0
        for crab_pos in input_data:
            fuel_cost = abs(crab_pos - i)
            total_diff += fuel_cost
        if not best_solution:
            best_solution = total_diff
        if total_diff < best_solution or not best_solution:
            best_solution = total_diff
    return best_solution


def part_two(input_filename):
    input_data = helpers.parse_input(input_filename)[0].split(",")
    input_data = [int(item) for item in input_data]
    best_solution = None

    dist_map = {}
    cost_so_far = 0
    for x in range(max(input_data) + 1):
        cost_so_far += x
        dist_map[x] = cost_so_far
    print(dist_map)

    for i in range(max(input_data)):
        total_diff = 0
        for crab_pos in input_data:
            total_diff += dist_map[abs(i - crab_pos)]
        if not best_solution:
            best_solution = total_diff
        if total_diff < best_solution or not best_solution:
            best_solution = total_diff
    return best_solution




if __name__ == "__main__":
    print("*** PART ONE ***\n")
    print(f"Test result = {part_one('inputtest.txt')}\n")
    print(f"REAL RESULT = {part_one('input.txt')}\n\n")
    print("*** PART TWO ***\n")
    print(f"Test result = {part_two('inputtest.txt')}\n")
    print(f"REAL RESULT = {part_two('input.txt')}")
