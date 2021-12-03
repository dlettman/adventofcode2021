import sys
from collections import Counter

sys.path.append("..")
import helpers


def part_one(input_filename):
    input_data = helpers.parse_input(input_filename)
    most_common_digits = []
    swap_mapping = {"0": "1", "1": "0"}
    for column in zip(*input_data):
        most_common_digits.append("1" if column.count("1") > column.count("0") else "0")
    gamma_rate = int("".join(most_common_digits), 2)
    epsilon_rate = int("".join([swap_mapping[char] for char in most_common_digits]), 2)
    return f"gamma rate = {gamma_rate}, epsilon rate = {epsilon_rate}, product = {gamma_rate * epsilon_rate}"


def find_rating(input_data, element="oxygen"):
    for idx in range(len(input_data[0])):
        remaining_numbers = len(input_data)
        one_count = Counter([item[idx] for item in input_data])["1"]
        if one_count >= (remaining_numbers / 2):
            keep_it = "1" if element == "oxygen" else "0"
        else:
            keep_it = "0" if element == "oxygen" else "1"
        input_data = [number for number in input_data if number[idx] == keep_it]
        if len(input_data) == 1:
            return input_data[0]


def part_two(input_filename):
    input_data = helpers.parse_input(input_filename)
    oxygen_rating = find_rating(input_data, element="oxygen")
    c02_rating = find_rating(input_data, element="c02")
    return f"oxygen = {oxygen_rating}, c02 = {c02_rating}. Decimal product = {int(oxygen_rating, 2) * int(c02_rating, 2)}"


if __name__ == "__main__":
    print("*** PART ONE ***\n")
    print(f"Test result = {part_one('inputtest.txt')}\n")
    print(f"REAL RESULT = {part_one('input.txt')}\n\n")
    print("*** PART TWO ***\n")
    print(f"Test result = {part_two('inputtest.txt')}\n")
    print(f"REAL RESULT = {part_two('input.txt')}")
