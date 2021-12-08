import sys
sys.path.append("..")
import helpers

easy_digit_map = {
    2: 1,
    3: 7,
    4: 4,
    7: 8
}


def part_one(input_filename):
    input_data = helpers.parse_input(input_filename)
    input_data = [line.split(" | ") for line in input_data]
    outputs = [item[1].split(" ") for item in input_data]

    total = 0
    for sublist in outputs:
        total += len([item for item in sublist if len(item) in easy_digit_map])
    return total


def part_two(input_filename):
    input_data = helpers.parse_input(input_filename)
    input_data = [line.split(" | ") for line in input_data]
    inputs = [item[0].split(" ") for item in input_data]
    outputs = [item[1].split(" ") for item in input_data]
    total = 0
    for input, output in zip(inputs, outputs):
        # we'll messily derive enough information to determine which number is which
        six_and_nine_and_zero = []
        for number in input + output:
            if len(number) == 6:
                if sorted(number) not in six_and_nine_and_zero:
                    six_and_nine_and_zero.append(sorted(number))
            elif len(number) == 4:
                four_set = set(number)
        one_set = set([number for number in input if len(number) == 2][0])
        six_set, nine_set, zero_set = None, None, None
        for item in six_and_nine_and_zero:
            if len(set(item).intersection(one_set)) == 1:
                six_set = set(item)
            elif len(set(item).intersection(four_set)) == 4:
                nine_set = set(item)
            else:
                zero_set = set(item)
        segment_e = zero_set.difference(nine_set)  # we'll use you later
        digit_list = []
        for digit in output:
            # go-go arbitrary deduction!
            if len(digit) in [2, 3, 4, 7]:  # handles 1, 4, 7, 8
                digit_list.append(easy_digit_map[len(digit)])
            elif len(digit) == 5:  # handles 2, 3, 5
                if len(set(digit).intersection(one_set)) == 2:
                    digit_list.append(3)
                elif segment_e.issubset(set(digit)):
                    digit_list.append(2)
                else:
                    digit_list.append(5)
            elif len(digit) == 6:  # Oh hey we have these guys already
                if set(digit) == zero_set:
                    digit_list.append(0)
                elif set(digit) == six_set:
                    digit_list.append(6)
                elif set(digit) == nine_set:
                    digit_list.append(9)
        total += int("".join([str(item) for item in digit_list]))
    return total


if __name__ == "__main__":
    print("*** PART ONE ***\n")
    print(f"Test result = {part_one('inputtest.txt')}\n")
    print(f"REAL RESULT = {part_one('input.txt')}\n\n")
    print("*** PART TWO ***\n")
    print(f"Test result = {part_two('inputtest.txt')}\n")
    print(f"REAL RESULT = {part_two('input.txt')}")
