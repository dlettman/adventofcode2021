import sys
sys.path.append("..")
import helpers

def part_one(input_filename):
    input = helpers.parse_input(input_filename)
    if not input:
        return "*** NO INPUT SUPPLIED ***"
    # do stuff here
    for idx, item1 in enumerate(input):
        for item2 in input[idx+1:]:
            if int(item1) + int(item2) == 2020:
                return f"{item1} * {item2} = {int(item1) * int(item2)}"
    output = input
    return output

def part_two(input_filename):
    input = helpers.parse_input(input_filename)
    if not input:
        return "*** NO INPUT SUPPLIED ***"
    for idx, item1 in enumerate(input):
        for idx2, item2 in enumerate(input[idx+1:]):
            for item3 in input[idx2+1:]:
                if int(item1) + int(item2) + int(item3) == 2020:
                    return f"{item1} * {item2} * {item3} = {int(item1) * int(item2) * int(item3)}"
    return output

if __name__ == "__main__":
    print("*** PART ONE ***\n")
    print(f"Test result = {part_one('inputtest.txt')}\n")
    print(f"REAL RESULT = {part_one('input.txt')}\n\n")
    print("*** PART TWO ***\n")
    print(f"Test result = {part_two('inputtest.txt')}\n")
    print(f"REAL RESULT = {part_two('input.txt')}\n\n")
