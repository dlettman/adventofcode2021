import sys
sys.path.append("..")
import helpers
from collections import deque, Counter

def part_one(input_filename):
    input_data = helpers.parse_input(input_filename)
    paths = build_paths_dict(input_data)
    print(paths)
    paths_in_progress = deque([["start"]])
    complete_paths = []
    while paths_in_progress:
        current_path = paths_in_progress.popleft()
        print(f"current path = {current_path}")
        possible_next_steps = paths[current_path[-1]] if current_path[-1] in paths else None
        valid_next_steps = []
        if possible_next_steps:
            for next_step in possible_next_steps:
                if next_step.islower() and next_step in current_path:
                    pass
                elif next_step == "end":
                    complete_paths.append(current_path + ["end"])
                else:
                    valid_next_steps.append(next_step)
            for step in valid_next_steps:
                paths_in_progress.append(current_path + [step])
        else:
            pass
    return len(complete_paths)


def build_paths_dict(input_data):
    paths = {}
    for item in input_data:
        start, dest = item.split('-')
        if start not in paths:
            paths[start] = [dest]
        else:
            paths[start].append(dest)
        if dest not in paths:
            paths[dest] = [start]
        else:
            paths[dest].append(start)
    return paths





    if not input_data:
        return "*** NO INPUT SUPPLIED ***"
    # do stuff here
    output = input_data
    return output

def part_two(input_filename):
    input_data = helpers.parse_input(input_filename)
    paths = build_paths_dict(input_data)
    print(paths)
    paths_in_progress = deque([["start"]])
    complete_paths = []
    while paths_in_progress:
        current_path = paths_in_progress.popleft()
        print(f"current path = {current_path}")
        small_cave_visited_twice = False
        visited_caves = Counter(current_path)
        for cave in visited_caves:
            if cave.islower() and visited_caves[cave] == 2:
                small_cave_visited_twice = True
        possible_next_steps = paths[current_path[-1]] if current_path[-1] in paths else None
        valid_next_steps = []
        if possible_next_steps:
            for next_step in possible_next_steps:
                if next_step == "end":
                    complete_paths.append(current_path + ["end"])
                elif next_step.islower() and next_step in current_path and small_cave_visited_twice:
                    pass
                elif next_step == "start":
                    pass
                else:
                    valid_next_steps.append(next_step)
            for step in valid_next_steps:
                paths_in_progress.append(current_path + [step])
        else:
            pass
    return len(complete_paths)

if __name__ == "__main__":
    print("*** PART ONE ***\n")
    print(f"Test result = {part_one('inputtest.txt')}\n")
    print(f"REAL RESULT = {part_one('input.txt')}\n\n")
    print("*** PART TWO ***\n")
    print(f"Test result = {part_two('inputtest.txt')}\n")
    print(f"REAL RESULT = {part_two('input.txt')}\n\n")
