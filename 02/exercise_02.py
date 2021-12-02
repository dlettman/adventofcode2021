import sys
sys.path.append("..")
import helpers


def part_one(input_filename):
    input_data = helpers.parse_input(input_filename)
    input_data = [item.split(' ') for item in input_data]
    horizontal, depth = 0, 0
    for command, value in input_data:
        if command == "forward":
            horizontal += int(value)
        elif command == "down":
            depth += int(value)
        elif command == "up":
            depth -= int(value)
    return f"horizontal = {horizontal}, depth = {depth}, product = {horizontal * depth}"


def part_two(input_filename):
    input_data = helpers.parse_input(input_filename)
    input_data = [item.split(' ') for item in input_data]
    horizontal, depth, aim = 0, 0, 0
    for command, value in input_data:
        if command == "forward":
            horizontal += int(value)
            depth += int(value) * aim
        elif command == "down":
            aim += int(value)
        elif command == "up":
            aim -= int(value)
    return f"horizontal = {horizontal}, depth = {depth}, product = {horizontal * depth}"


if __name__ == "__main__":
    print("*** PART ONE ***\n")
    print(f"Test result = {part_one('inputtest.txt')}\n")
    print(f"REAL RESULT = {part_one('input.txt')}\n\n")
    print("*** PART TWO ***\n")
    print(f"Test result = {part_two('inputtest.txt')}\n")
    print(f"REAL RESULT = {part_two('input.txt')}")
