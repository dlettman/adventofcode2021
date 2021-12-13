import sys
sys.path.append("..")
import helpers


def get_dots_and_folds(input_data):
    dots = set()
    folds = []
    blank_idx = None
    for idx, line in enumerate(input_data):
        if not line:
            blank_idx = idx
            break
        else:
            dots.add((int(line.split(",")[0]), int(line.split(",")[1])))
    for line in input_data[(blank_idx + 1):]:
        folds.append([int(line.split("=")[1]), line.split("=")[0][-1]])
    return dots, folds


def fold_paper(dots, fold):
    new_dots = set()
    fold_coord = int(fold[0])
    if fold[1] == "x":
        for dot in dots:
            x, y = dot[0], dot[1]
            new_dots.add((x, y) if x <= fold_coord else ((fold_coord - (x - fold_coord)), y))
    elif fold[1] == "y":
        for dot in dots:
            x, y = dot[0], dot[1]
            new_dots.add((x, y) if y <= fold_coord else (x, (fold_coord - (y - fold_coord))))
    return new_dots


def part_one(input_filename):
    input_data = helpers.parse_input(input_filename)
    dots, folds = get_dots_and_folds(input_data)
    for fold in folds[:1]:
        new_dots = fold_paper(dots, fold)
    return len(new_dots)


def part_two(input_filename):
    input_data = helpers.parse_input(input_filename)
    dots, folds = get_dots_and_folds(input_data)
    for fold in folds:
        dots = fold_paper(dots, fold)

    max_x = max([item[0] for item in dots])
    max_y = max([item[1] for item in dots])

    for y in range(max_y + 1):
        string = ""
        for x in range(max_x + 1):
            string += ("#" if (x,y) in dots else " ")
        print(string)


if __name__ == "__main__":
    print("*** PART ONE ***\n")
    print(f"Test result = {part_one('inputtest.txt')}\n")
    print(f"REAL RESULT = {part_one('input.txt')}\n\n")
    print("*** PART TWO ***\n")
    part_two('inputtest.txt')
    print(f"Test result = ^^^^^^^^")
    part_two('input.txt')
    print(f"REAL RESULT = ^^^^^^^^")
