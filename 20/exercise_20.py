import sys
sys.path.append("..")
import helpers


NEIGHBORS = [(-1, -1), (0, -1), (1, -1), (-1, 0), (0, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]


class AlgoString(object):

    def __init__(self, algo_string):
        self.algo_dict = {idx: val for idx, val in enumerate(algo_string)}

    def get_algo_value(self, three_by_three_array):
        bin_string = ""
        for char in three_by_three_array:
            if char == "#":
                bin_string += "1"
            else:  # "."
                bin_string += "0"
        return self.algo_dict[int(bin_string, 2)]


class Map(object):

    def __init__(self, map, algo_string):
        self.map = self.parse_map(map)
        self.algo_string = AlgoString(algo_string)
        self.step = 0
        self.infinity_char= "."
        self.max_x = max([item[0] for item in self.map])
        self.min_x = min([item[0] for item in self.map])
        self.max_y = max([item[1] for item in self.map])
        self.min_y = min([item[1] for item in self.map])

    @staticmethod
    def parse_map(input_data):
        active_cells = set()
        for y, line in enumerate(input_data):
            for x, char in enumerate(line):
                if char == "#":
                    active_cells.add((x, y))
        return active_cells

    def cycle(self):
        new_map = set()
        for y in range(self.min_y - 1, self.max_y + 2):
            for x in range(self.min_x - 1, self.max_x + 2):
                three_by_three_array = []
                for delta_x, delta_y in NEIGHBORS:
                    if not (self.min_x <= x + delta_x <= self.max_x) or not (self.min_y <= y + delta_y <= self.max_y):
                        three_by_three_array.append(self.infinity_char)
                    elif (x + delta_x, y + delta_y) in self.map:
                        three_by_three_array.append("#")
                    else:
                        three_by_three_array.append(".")
                if self.algo_string.get_algo_value(three_by_three_array) == "#":
                    new_map.add((x, y))
        self.infinity_char = self.compute_infinity_char()
        self.step += 1
        self.map = new_map
        self.max_x = max([item[0] for item in self.map])
        self.min_x = min([item[0] for item in self.map])
        self.max_y = max([item[1] for item in self.map])
        self.min_y = min([item[1] for item in self.map])

    def compute_infinity_char(self):
        three_by_three_array = ["."] * 9
        for n in range(self.step):
            three_by_three_array = self.algo_string.get_algo_value(three_by_three_array)
        return self.algo_string.get_algo_value(three_by_three_array)

    def print_map(self):
        map_printout = []
        for y in range(self.min_y - 1, self.max_y + 2):
            line = []
            for x in range(self.min_x - 1, self.max_x + 2):
                if not self.min_x <= x <= self.max_x and not self.min_y <= y <= self.max_y:
                    line.append(self.infinity_char)
                else:
                    line.append("#" if (x, y) in self.map else ".")
            line = "".join(line)
            map_printout.append(line)
        return "\n".join(map_printout)


def parse_map_and_algo_string(input_data):
    algo_line = input_data[0]
    map = input_data[2:]
    return map, algo_line


def part_one(input_filename):
    input_data = helpers.parse_input(input_filename)
    map, algo_string = parse_map_and_algo_string(input_data)
    map = Map(map, algo_string)
    # print(map.print_map())
    map.cycle()
    # print(map.print_map())
    map.cycle()
    # print(map.print_map())
    return len(map.map)


def part_two(input_filename):
    input_data = helpers.parse_input(input_filename)
    map, algo_string = parse_map_and_algo_string(input_data)
    map = Map(map, algo_string)
    for n in range(50):
        map.cycle()
    return len(map.map)


if __name__ == "__main__":
    print("*** PART ONE ***\n")
    print(f"Test result = {part_one('inputtest.txt')}\n")
    print(f"REAL RESULT = {part_one('input.txt')}\n\n")
    print("*** PART TWO ***\n")
    print(f"Test result = {part_two('inputtest.txt')}\n")
    print(f"REAL RESULT = {part_two('input.txt')}\n\n")
