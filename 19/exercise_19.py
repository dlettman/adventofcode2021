import sys
sys.path.append("..")
import helpers

def part_one(input_filename):
    input = helpers.parse_input(input_filename)
    # do stuff here
    output = input
    return output

def part_two(input_filename):
    input = helpers.parse_input(input_filename)
    # do stuff here
    output = input
    return output

if __name__ == "__main__":
    print("*** PART ONE ***\n")
    print(f"Test result = {part_one('input1test.txt')}\n")
    print(f"REAL RESULT = {part_one('input1.txt')}\n\n")
    print("*** PART TWO ***\n")
    print(f"Test result = {part_two('input2test.txt')}\n")
    print(f"REAL RESULT = {part_two('input2.txt')}\n\n")
