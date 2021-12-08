import sys
sys.path.append("..")
import helpers

digit_segment_count = {
    0: 6,
    1: 2,
    2: 5,
    3: 5,
    4: 4,
    5: 5,
    6: 6,
    7: 3,
    8: 7,
    9: 6
}

easy_digit_map = {
    2: 1,
    3: 7,
    4: 4,
    7: 8
}

five_overlap_count_map = {
    0: 5,
    1: 3,
    2: 2,
}

# six_overlap_count_map = {
#     2: 6
#
# }

# 2, 3, & 5,  6 & 9

digit_segment_map = {
    1: "cf",
    2: "acdeg",
    3: "acdfg",
    4: "bcdf",
    5: "abdfg",
    6: "abdfge",
    7: "acf",
    8: "abcdefg",
    9: "abcdfg"
}

def part_one(input_filename):
    input_data = helpers.parse_input(input_filename)
    input_data = [line.split(" | ") for line in input_data]
    inputs = [item[0].split(" ") for item in input_data]
    outputs = [item[1].split(" ") for item in input_data]
    print(inputs)
    print(outputs)

    total = 0
    for sublist in outputs:
        for item in sublist:
            if len(item) in [2, 4, 3, 7]:
                total += 1
    return total

def part_two(input_filename):
    input_data = helpers.parse_input(input_filename)
    input_data = [line.split(" | ") for line in input_data]
    inputs = [item[0].split(" ") for item in input_data]
    outputs = [item[1].split(" ") for item in input_data]
    total = 0
    for input, output in zip(inputs, outputs):
        six_and_nine_and_zero = []
        for number in input + output:
            if len(number) == 6:
                if sorted(number) not in six_and_nine_and_zero:
                    six_and_nine_and_zero.append(sorted(number))
            elif len(number) == 4:
                four_set = set(number)
        print(f"six and nine and zero = {six_and_nine_and_zero}")
        one_set = set([number for number in input if len(number) == 2][0])
        six_set = None
        nine_set = None
        zero_set = None
        for item in six_and_nine_and_zero:
            print(f"int = {set(item).intersection(one_set)}")
            print(f"len = {len(set(item).intersection(one_set))}")
            if len(set(item).intersection(one_set)) == 1:
                six_set = set(item)
            elif len(set(item).intersection(four_set)) == 4:
                nine_set = set(item)
            else:
                zero_set = set(item)
        segment_c = six_set.intersection(one_set)
        segment_e = zero_set.difference(nine_set)
        # print(f"one set = {one_set}")
        # print(f"zero set = {zero_set}")
        # print(f"nine set = {nine_set}")
        # print(f"six set = {six_set}")
        # print(f"seg c = {segment_c}")
        print(f"seg e = {segment_e}")
        one_set = set([number for number in input if len(number) == 2][0])
        # we have what we need
        digit_list = []
        for digit in output:
            if len(digit) in [2, 3, 4, 7]:
                digit_list.append(easy_digit_map[len(digit)])
            elif len(digit) == 5: # 2, 3, & 5
                print(f"set = {set(digit)}")
                if len(set(digit).intersection(one_set)) == 2: # 3
                    digit_list.append(3)
                elif segment_e.issubset(set(digit)): # 5
                    digit_list.append(2)
                else:
                    digit_list.append(5)

                # print(f"digit = {set(digit)}")
                # print(segment_e.union(segment_c))
                # overlap_count = len(set(digit).intersection(segment_e.union(segment_c)))
                # print(f"overlap count = {set(digit).intersection(segment_e.union(segment_c))}")
                # print(f"appending {five_overlap_count_map[overlap_count]}")
                # digit_list.append(five_overlap_count_map[overlap_count])
            elif len(digit) == 6:
                if set(digit) == zero_set:
                    digit_list.append(0)
                elif set(digit) == six_set:
                    digit_list.append(6)
                elif set(digit) == nine_set:
                    digit_list.append(9)
        print(f"digit_list = {digit_list}")
        total += int("".join([str(item) for item in digit_list]))
    return total







if __name__ == "__main__":
    print("*** PART ONE ***\n")
    # print(f"Test result = {part_one('inputtest.txt')}\n")
    # print(f"REAL RESULT = {part_one('input.txt')}\n\n")
    print("*** PART TWO ***\n")
    print(f"Test result = {part_two('inputtest.txt')}\n")
    print(f"REAL RESULT = {part_two('input.txt')}")
