import sys
sys.path.append("..")
import helpers


def part_one(input_filename):
    input_data = helpers.parse_input(input_filename)
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
    # print(dots)
    new_dots = set()
    # print(folds)
    for fold in folds[:1]:
        print(fold)
        fold_axis_coordinate = int(fold[0])
        print(f"fold axis co = {fold_axis_coordinate} f1 = {fold[1]}")
        if fold[1] == "x":
            print("fold = x")
            for dot in dots:
                x, y = dot[0], dot[1]
                if x > fold_axis_coordinate:
                    # print("found one")
                    # print(f"{(fold_axis_coordinate - (fold_axis_coordinate - x), y)}")
                    new_dots.add((fold_axis_coordinate - (x - fold_axis_coordinate), y))
                else:
                    new_dots.add((x, y))
        elif fold[1] == "y":
            # print(fold)
            fold_axis_coordinate = int(fold[0])
            for dot in dots:
                x, y = dot[0], dot[1]
                if y > fold_axis_coordinate:
                    # print("y greater")
                    new_dots.add((x, fold_axis_coordinate - (y - fold_axis_coordinate)))
                else:
                    # print("y not greater")
                    new_dots.add((x, y))
    # print(new_dots)
    return len(new_dots)
        # elif fold[1] == "y":
        #     for y in range(fold_axis_coordinate):
        #         pass


def part_two(input_filename):
    input_data = helpers.parse_input(input_filename)
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
    # print(dots)
    # print(folds)
    for fold in folds:
        new_dots = set()
        print(fold)
        fold_axis_coordinate = int(fold[0])
        print(f"fold axis co = {fold_axis_coordinate} f1 = {fold[1]}")
        if fold[1] == "x":
            print("fold = x")
            for dot in dots:
                x, y = dot[0], dot[1]
                if x > fold_axis_coordinate:
                    new_dots.add((fold_axis_coordinate - (x - fold_axis_coordinate), y))
                else:
                    new_dots.add((x, y))
        elif fold[1] == "y":
            fold_axis_coordinate = int(fold[0])
            for dot in dots:
                x, y = dot[0], dot[1]
                if y > fold_axis_coordinate:
                    new_dots.add((x, fold_axis_coordinate - (y - fold_axis_coordinate)))
                else:
                    new_dots.add((x, y))
        dots = new_dots.copy()

    max_x = max([item[0] for item in dots])
    max_y = max([item[1] for item in dots])

    for y in range(max_y + 1):
        string = ""
        for x in range(max_x + 1):
            if (x,y) in dots:
                string += "#"
            else:
                string += " "
        print(string)

if __name__ == "__main__":
    print("*** PART ONE ***\n")
    print(f"Test result = {part_one('inputtest.txt')}\n")
    print(f"REAL RESULT = {part_one('input.txt')}\n\n")
    print("*** PART TWO ***\n")
    print(f"Test result = {part_two('inputtest.txt')}\n")
    print(f"REAL RESULT = {part_two('input.txt')}\n\n")
