import sys
sys.path.append("..")
import helpers


def part_one(input_filename):
    input_data = helpers.parse_input(input_filename)
    input_data = [int(item) for item in input_data]
    increase_count = 0
    previous_measurement = None
    for measurement in input_data:
        if previous_measurement:
            if measurement > previous_measurement:
                increase_count += 1
        previous_measurement = measurement
    return increase_count

    # alternate smartypants answer:
    # return len([item for idx, item in enumerate(input_data[1:]) if int(item) > int(input_data[idx])])


def part_two(input_filename):
    input_data = helpers.parse_input(input_filename)
    input_data = [int(item) for item in input_data]
    increase_count = 0
    previous_measurement = None
    for idx in range(len(input_data) - 2):
        measurement = sum(input_data[idx:idx + 3])
        if previous_measurement:
            if measurement > previous_measurement:
                increase_count += 1
        previous_measurement = measurement
    return increase_count


if __name__ == "__main__":
    print("*** PART ONE ***\n")
    print(f"Test result = {part_one('inputtest.txt')}\n")
    print(f"REAL RESULT = {part_one('input.txt')}\n\n")
    print("*** PART TWO ***\n")
    print(f"Test result = {part_two('inputtest.txt')}\n")
    print(f"REAL RESULT = {part_two('input.txt')}\n\n")
