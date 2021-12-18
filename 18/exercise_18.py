import sys
from math import floor, ceil
sys.path.append("..")
import helpers


def convert_to_mixedlist(input_string):
    result_list = []
    for char in input_string:
        if char.isdigit():
            result_list.append(int(char))
        else:
            result_list.append(char)
    return result_list


def do_addition(sf_number):
    changed = True
    # print(f"sf number = {sf_number}")
    while changed:
        # print("".join([str(item) for item in sf_number]))
        changed = False
        nest_level = 0
        for idx, item in enumerate(sf_number):
            changed = False
            if item == '[':
                nest_level += 1
            elif item == ']':
                nest_level -= 1
            elif item == ',':
                continue
            else:  # item is int
                # print(nest_level)
                if nest_level > 4:  # explode
                    # print("explode!")
                    first_number = item
                    # print("first number = ", first_number)
                    second_number = sf_number[idx + 2] # skip comma
                    # print("second number = ", second_number)
                    for back_idx, back_item in enumerate(sf_number[idx-1: 0: -1]): # iterate backwards through list, add number to first number that shows up
                        if type(back_item) == int:
                            # print("found back number:", back_item)
                            sf_number[idx-(1+back_idx)] = back_item + first_number
                            break
                    for front_idx, front_item in enumerate(sf_number[idx+3::]):
                        if type(front_item) == int:
                            # print("found second number")
                            # print(front_idx, front_item)
                            # print("!!!!", idx, sf_number)
                            sf_number[idx + 3 + front_idx] = front_item + second_number
                            break
                    # cut off one set of parens, both numbers, and separating comma
                    sf_number = sf_number[0:idx -1] + [0] + sf_number[idx+4::]
                    changed = True
                    break
        if not changed:  # split
            for idx, item in enumerate(sf_number):
                if type(item) == int:
                    if item > 9:
                        # print("split!")
                        first_number = floor(item / 2)
                        second_number = ceil(item / 2)
                        sf_number = sf_number[0:idx] + ['[', first_number, ',', second_number, ']'] + sf_number[idx + 1:]
                        changed = True
                        break

    return "".join([str(item) for item in sf_number])


def calcluate_magnitude(mixed_list):
    mixed_list = [item for item in mixed_list if item != ","]
    # print("calcing magnnitde ", mixed_list)
    last_chunk = []
    changed = True
    mini_mag = 0
    while changed:
        changed = False
        for idx, char in enumerate(mixed_list):
            if char == '[': # discard chunk
                last_chunk = []
            elif char == ']':
                # print("last chunk = ", last_chunk)
                mini_mag = [(last_chunk[0] * 3 + last_chunk[1] * 2)]
                # try:
                new_mixed_list = mixed_list[0:idx - 3] + mini_mag + mixed_list[idx + 1:]
                # except IndexError:
                #     new_mixed_list = mixed_list[0:idx - 4] + mini_mag + mixed_list[idx + 1:]
                mixed_list = new_mixed_list
                changed = True
                break
            else:
                last_chunk.append(char)
    return mini_mag[0]

def joinit(mixed_list):
    return "".join([str(item) for item in current_equation])

def part_one(input_filename):
    input_data = helpers.parse_input(input_filename)
    current_equation = input_data[0]
    for line in input_data[1:]:
        # print("current_equation = ", current_equation )
        joined = ['['] + convert_to_mixedlist(current_equation) + [','] + convert_to_mixedlist(line) + [']']
        # print("joined = ", joined)
        current_equation = do_addition(joined)
        current_equation = "".join([str(item) for item in current_equation])
        # print("current_equation = ", current_equation )
    return calcluate_magnitude(convert_to_mixedlist(current_equation))


def part_two(input_filename):
    input_data = helpers.parse_input(input_filename)
    sums = []
    for line1 in input_data:
        for line2 in input_data:
            if line1 != line2:
                joined = ['['] + convert_to_mixedlist(line1) + [','] + convert_to_mixedlist(line2) + [']']
                result = do_addition(joined)
                result = "".join([str(item) for item in result])
                sums.append(calcluate_magnitude(convert_to_mixedlist(result)))
    return max(sums)

    current_equation = input_data[0]
    for line in input_data[1:]:
        # print("current_equation = ", current_equation )
        joined = ['['] + convert_to_mixedlist(current_equation) + [','] + convert_to_mixedlist(line) + [']']
        # print("joined = ", joined)
        current_equation = do_addition(joined)
        current_equation = "".join([str(item) for item in current_equation])
        # print("current_equation = ", current_equation )
    return calcluate_magnitude(convert_to_mixedlist(current_equation))




if __name__ == "__main__":
    print("*** PART ONE ***\n")
    # print("return!", do_addition((helpers.parse_input('inputtest2.txt'))))
    print(f"Test result = {part_one('inputtest2.txt')}\n")
    print(f"REAL RESULT = {part_one('input.txt')}\n\n")
    # print("*** PART TWO ***\n")
    print(f"Test result = {part_two('inputtest2.txt')}\n")
    print(f"REAL RESULT = {part_two('input.txt')}\n\n")
