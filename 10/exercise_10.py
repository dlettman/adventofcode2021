import sys
sys.path.append("..")
import helpers

scoring_map = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

open_close_map = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}

scoring_map_2 = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}


def part_one(input_filename):
    input_data = helpers.parse_input(input_filename)
    score = sum([is_line_corrupted(line)[1] for line in input_data])
    return score


def is_line_corrupted(line):
    opener_stack = []
    for char in line:
        if char in open_close_map:
            opener_stack.append(char)
        else:
            if char == open_close_map[opener_stack[-1]]:
                opener_stack.pop()
            else:
                return True, scoring_map[char]
    return False, 0


def part_two(input_filename):
    input_data = helpers.parse_input(input_filename)
    incomplete_lines = [line for line in input_data if not is_line_corrupted(line)[0]]
    incomplete_line_scores = []

    for line in incomplete_lines:
        opener_stack = []
        for char in line:
            if char in open_close_map:
                opener_stack.append(char)
            else:
                if char == open_close_map[opener_stack[-1]]:
                    opener_stack.pop()
        line_score = 0
        while opener_stack:
            line_score = line_score * 5
            line_score += scoring_map_2[open_close_map[opener_stack[-1]]]
            opener_stack.pop()
        incomplete_line_scores.append(line_score)
    middle_index = (len(incomplete_line_scores))//2
    return sorted(incomplete_line_scores)[middle_index]


if __name__ == "__main__":
    print("*** PART ONE ***\n")
    print(f"Test result = {part_one('inputtest.txt')}\n")
    print(f"REAL RESULT = {part_one('input.txt')}\n\n")
    print("*** PART TWO ***\n")
    print(f"Test result = {part_two('inputtest.txt')}\n")
    print(f"REAL RESULT = {part_two('input.txt')}\n\n")
