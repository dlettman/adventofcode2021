import sys
sys.path.append("..")
import helpers
from collections import Counter


def get_individual_element_count(chunk_counter):
    elements = Counter()
    for chunk in chunk_counter:
        elements[chunk[0]] += chunk_counter[chunk]
    return elements


def solve(counter):
    most_common = counter.most_common(1)
    least_common = counter.most_common()[:-2:-1]
    return (most_common[0][1] - least_common[0][1])


def parse_rules(input_data):
    formula = input_data[0]
    recipes = {}
    for line in input_data[2:]:
        reagents, product = line.split(" -> ")
        recipes[reagents] = product
    return formula, recipes


def do_insertion(formula, recipes):  # AKA Naive solution
    new_formula = [formula[0]]
    for idx in range(len(formula) - 1):
        # Every possible chunk has a recipe
        new_formula.append(recipes[formula[idx:idx+2]])
        new_formula.append(formula[idx + 1])
    return "".join(new_formula)


def do_it_with_counters(chunk_counter, recipes):  # AKA Optimized solution
    new_counter = Counter()
    for chunk in chunk_counter:
        resultant_chunks = [chunk[0] + recipes[chunk], recipes[chunk] + chunk[1]]
        for res_chunk in resultant_chunks:
            new_counter[res_chunk] += chunk_counter[chunk]
    return new_counter


def part_one(input_filename):
    input_data = helpers.parse_input(input_filename)
    formula, recipes = parse_rules(input_data)
    for step in range(10):
        formula = do_insertion(formula, recipes)
    element_counter = Counter(formula)
    return solve(element_counter)


def part_two(input_filename):
    input_data = helpers.parse_input(input_filename)
    formula, recipes = parse_rules(input_data)
    chunks = [formula[idx: idx + 2] for idx in range(len(formula) - 1)]
    chunk_counter = Counter(chunks)
    for step in range(40):
        chunk_counter = do_it_with_counters(chunk_counter, recipes)
    element_count = get_individual_element_count(chunk_counter)
    element_count[formula[-1]] += 1  # Last element gets left out by our de-duping
    return solve(element_count)


if __name__ == "__main__":
    print("*** PART ONE ***\n")
    print(f"Test result = {part_one('inputtest.txt')}\n")
    print(f"REAL RESULT = {part_one('input.txt')}\n\n")
    print("*** PART TWO ***\n")
    print(f"Test result = {part_two('inputtest.txt')}\n")
    print(f"REAL RESULT = {part_two('input.txt')}\n\n")
