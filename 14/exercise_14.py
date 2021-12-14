import sys
sys.path.append("..")
import helpers
from collections import Counter

elements = ['BCHN']


def get_individual_element_count(chunk_counter):
    elements = Counter({"B": 0,
                "C": 0,
                "H": 0,
                "N": 0})
    # for chunk in chunk_counter:
    #     for char in chunk:
    #         elements[char] += chunk_counter[chunk]
    # for element in elements:
    #     elements[element] = elements[element] // 2
    # return elements
    for chunk in chunk_counter:
        print(chunk)
        elements[chunk[0]] += chunk_counter[chunk]
    return elements




def parse_rules(input_data):
    formula = input_data[0]
    recipes = {}
    for line in input_data[2:]:
        reagents, product = line.split(" -> ")
        recipes[reagents] = product
    return formula, recipes


def do_insertion(formula, recipes):
    new_formula = [formula[0]]
    for idx in range(len(formula) - 1):
        chunk = "".join(formula[idx:idx+2])
        if chunk in recipes:
            new_formula.append(recipes[formula[idx:idx+2]])
        new_formula.append(formula[idx + 1])
    return "".join(new_formula)


def do_it_with_counters(formula, recipes):
    pass


def part_one(input_filename):
    input_data = helpers.parse_input(input_filename)

    formula, recipes = parse_rules(input_data)
    print(recipes)
    for step in range(10):
        formula = do_insertion(formula, recipes)
        print(formula)
    element_counter = Counter(formula)
    most_common = element_counter.most_common(1)
    least_c = element_counter.most_common()[:-1-1:-1]
    print (most_common)
    print(least_c)

    return (most_common[0][1] - least_c[0][1])



    return "*** NO INPUT SUPPLIED ***"
    # do stuff here
    output = input_data
    return output

def part_two(input_filename):
    input_data = helpers.parse_input(input_filename)
    formula, recipes = parse_rules(input_data)
    chunks = [formula[idx: idx + 2] for idx in range(len(formula) - 1)]
    chunk_counter = Counter(chunks)
    for step in range(40):
        new_counter = Counter()
        for chunk in chunk_counter:
            if chunk in recipes:
                resultant_chunks = [chunk[0] + recipes[chunk], recipes[chunk] + chunk[1]]
                for res_chunk in resultant_chunks:
                    if res_chunk in new_counter:
                        new_counter[res_chunk] += chunk_counter[chunk]
                    else:
                        new_counter[res_chunk] = chunk_counter[chunk]
            else:
                if chunk in new_counter:
                    new_counter[chunk] += chunk_counter[chunk]
                else:
                    new_counter[chunk] = chunk_counter[chunk]
        chunk_counter = new_counter
    element_count = get_individual_element_count(chunk_counter)
    # element_count[input_data[0]] += 1
    element_count[formula[-1]] += 1
    most_common = element_count.most_common(1)
    least_c = element_count.most_common()[:-1-1:-1]
    print (most_common)
    print(least_c)
    return ((most_common[0][1]) - (least_c[0][1]))

    # for step in range(40):
    #     print(step)
    #     formula = do_insertion(formula, recipes)
    # element_counter = Counter(formula)
    # most_common = element_counter.most_common(1)
    # least_c = element_counter.most_common()[:-1-1:-1]
    # return (most_common[0][1] - least_c[0][1])


    return "*** NO INPUT SUPPLIED ***"
    # do stuff here
    output = input_data
    return output

if __name__ == "__main__":
    print("*** PART ONE ***\n")
    print(f"Test result = {part_one('inputtest.txt')}\n")
    print(f"REAL RESULT = {part_one('input.txt')}\n\n")
    print("*** PART TWO ***\n")
    print(f"Test result = {part_two('inputtest.txt')}\n")
    print(f"REAL RESULT = {part_two('input.txt')}\n\n")
