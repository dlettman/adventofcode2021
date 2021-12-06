import sys
from collections import Counter

sys.path.append("..")
import helpers


def part_one(input_filename):  # AKA naive solution
    input_data = helpers.parse_input(input_filename)
    input_data = input_data[0].split(",")
    fishies = [int(item) for item in input_data]
    new_fish = []
    for day in range(80):
        for fish in fishies:
            if fish == 0:
                new_fish.append(6)
                new_fish.append(8)
            else:
                new_fish.append(fish - 1)
        fishies = new_fish.copy()
        new_fish = []
    return len(fishies)


def part_two(input_filename):  # AKA big brain solution
    input_data = helpers.parse_input(input_filename)
    input_data = input_data[0].split(",")
    input_data = [int(item) for item in input_data]
    fishies = Counter(input_data)
    new_fish = {}
    for day in range(256):
        for fish in fishies:  # keys are timers
            if fish == 0:
                new_fish[8] = fishies[fish]
                if 6 not in new_fish:
                    new_fish[6] = fishies[fish]
                else:
                    new_fish[6] += fishies[fish]
            else:
                if fish - 1 not in new_fish:
                    new_fish[fish - 1] = fishies[fish]
                else:
                    new_fish[fish - 1] += fishies[fish]
        fishies = new_fish.copy()
        new_fish = {}
    return sum(fishies.values())


if __name__ == "__main__":
    print("*** PART ONE ***\n")
    print(f"Test result = {part_one('inputtest.txt')}\n")
    print(f"REAL RESULT = {part_one('input.txt')}\n\n")
    print("*** PART TWO ***\n")
    print(f"Test result = {part_two('inputtest.txt')}\n")
    print(f"REAL RESULT = {part_two('input.txt')}\n\n")
