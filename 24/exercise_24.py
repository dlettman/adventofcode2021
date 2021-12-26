import sys
sys.path.append("..")
import helpers


class Compooper(object):

    def __init__(self, input_data, inputs, debug=False):
        self.debug = debug
        self.input_data = input_data
        self.memory = {'w': 0,
                       'x': 0,
                       'y': 0,
                       'z': 0}
        self.inputs = inputs
        self.pointer = 0
        self.version_total = 0

    def run_program(self):
        for line in self.input_data:
            command = line.split(" ")[0]
            if command == "inp":
                self.inp_com(line)
            elif command == "add":
                self.add_com(line)
            elif command == "mul":
                self.mul_com(line)
            elif command == "div":
                self.div_com(line)
            elif command == "mod":
                self.mod_com(line)
            elif command == "eq":
                self.eq_test(line)

    def get_value_or_register(self, value):
        if value.islower():
            try:
                return self.memory[value]
            except KeyError:
                return 0
        else:  # value is int
            return int(value)

    def inp_com(self, command):
        target_register = command.split(" ")[1]
        value = next(self.inputs)
        if self.debug:
            print("saving input ", value, " to ", target_register)
        self.memory[target_register] = value

    def add_com(self, command):
        value_a, value_b = command.split(" ")[1:]
        value_a = self.get_value_or_register(value_a)
        value_b = self.get_value_or_register(value_b)
        if self.debug:
            print("adding")
        self.memory[command.split(" ")[1]] = value_a + value_b

    def mul_com(self, command):
        value_a, value_b = command.split(" ")[1:]
        value_a = self.get_value_or_register(value_a)
        value_b = self.get_value_or_register(value_b)
        if self.debug:
            print("multiplying")
        self.memory[command.split(" ")[1]] = value_a * value_b

    def div_com(self, command):
        value_a, value_b = command.split(" ")[1:]
        value_a = self.get_value_or_register(value_a)
        value_b = self.get_value_or_register(value_b)
        if self.debug:
            print("dividing")
        self.memory[command.split(" ")[1]] = value_a // value_b

    def mod_com(self, command):
        value_a, value_b = command.split(" ")[1:]
        value_a = self.get_value_or_register(value_a)
        value_b = self.get_value_or_register(value_b)
        self.memory[command.split(" ")[1]] = value_a % value_b

    def eq_test(self, command):
        value, target_register = command.split(" ")[1:]
        value = self.get_value_or_register(value)
        return 1 if self.memory[target_register] == value else 0


def part_one(input_filename, inputs):
    input_data = helpers.parse_input(input_filename)
    compooper = Compooper(input_data, iter(inputs), debug=True)
    compooper.run_program()
    print(compooper.memory)

def build_p1_inputs():
    list_of_lists = []
    for n in range(11111111111111, 99999999999999):
        num_string = str(n)
        if "0" not in num_string:
            list_of_lists.append([int(item) for item in num_string])
    print(list_of_lists)



def part_two(input_filename):
    input_data = helpers.parse_input(input_filename)
    if not input_data:
        return "*** NO INPUT SUPPLIED ***"
    # do stuff here
    output = input_data
    return output

if __name__ == "__main__":
    print("*** PART ONE ***\n")
    print(build_p1_inputs())
    # print(f"Test result = {part_one('inputtest.txt', [32])}\n")
    # print(f"REAL RESULT = {part_one('input.txt')}\n\n")
    # print("*** PART TWO ***\n")
    # print(f"Test result = {part_two('inputtest.txt')}\n")
    # print(f"REAL RESULT = {part_two('input.txt')}\n\n")
