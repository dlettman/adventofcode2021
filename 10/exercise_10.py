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
    score = 0
    for line in input_data:
        opener_queue = []
        for char in line:
            if char in open_close_map:
                opener_queue.append(char)
            else:
                if char == open_close_map[opener_queue[-1]]:
                    opener_queue.pop()
                else:
                    score += scoring_map[char]
                    break
    return score




    return output

def part_two(input_filename):
    input_data = helpers.parse_input(input_filename)
    incomplete_lines = []
    incomplete_line_scores = []
    for line in input_data:
        corrupted = False
        opener_queue = []
        for char in line:
            if char in open_close_map:
                opener_queue.append(char)
            else:
                if char == open_close_map[opener_queue[-1]]:
                    opener_queue.pop()
                else:
                    corrupted = True
        if not corrupted:
            incomplete_lines.append(line)
    for line in incomplete_lines:
        opener_queue = []
        for char in line:
            if char in open_close_map:
                opener_queue.append(char)
            else:
                if char == open_close_map[opener_queue[-1]]:
                    opener_queue.pop()
        line_score = 0
        while opener_queue:
            line_score = line_score * 5
            line_score += scoring_map_2[open_close_map[opener_queue[-1]]]
            opener_queue.pop()
        incomplete_line_scores.append(line_score)
    print(incomplete_line_scores)
    middle_index = (len(incomplete_line_scores))//2
    return (sorted(incomplete_line_scores)[middle_index])

if __name__ == "__main__":
    print("*** PART ONE ***\n")
    print(f"Test result = {part_one('inputtest.txt')}\n")
    print(f"REAL RESULT = {part_one('input.txt')}\n\n")
    print("*** PART TWO ***\n")
    print(f"Test result = {part_two('inputtest.txt')}\n")
    print(f"REAL RESULT = {part_two('input.txt')}\n\n")
