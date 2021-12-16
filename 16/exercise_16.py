import sys
from functools import reduce
sys.path.append("..")
import helpers


def product(lst):
    return reduce(lambda x, y: x * y, lst)


def greater_than(lst):
    return 1 if lst[0] > lst[1] else 0


def less_than(lst):
    return 1 if lst[0] < lst[1] else 0


def equal_to(lst):
    return 1 if lst[0] == lst[1] else 0


operator_function_map = {
    '000':  sum,  # sum
    '001':  product,  # multiply
    '010':  min,  # min
    '011':  max,  # max
    '101':  greater_than,  # greater than, always 2 subpackets
    '110':  less_than,  # less than, always 2 subpackets
    '111':  equal_to,  # equal to, always 2 subpackets
}


class Compooper(object):

    def __init__(self, input_data):
        self.input_data = input_data
        self.pointer = 0
        self.version_total = 0
        self.result = self.process_packet()

    def get_header(self):
        version_header = self.input_data[self.pointer:self.pointer + 3]
        type_id_header = self.input_data[self.pointer + 3: self.pointer + 6]
        return version_header, type_id_header

    def process_packet(self):
        version, packet_type = self.get_header()
        self.version_total += int(version, 2)
        self.pointer += 6
        if self.pointer == len(self.input_data) - 1:
            return
        if packet_type == '100':  # literal
            return self.process_literal_packet()
        else:
            return self.process_operator_packet(packet_type)

    def process_literal_packet(self):
        number_payload = ""
        while True:
            bit_prefix = self.input_data[self.pointer]
            self.pointer += 1
            number_payload += self.input_data[self.pointer: self.pointer + 4]
            self.pointer += 4
            if bit_prefix == '0':
                break
        number_payload = int(number_payload, 2)
        return number_payload

    def process_operator_packet(self, type):
        length_type = self.input_data[self.pointer]
        self.pointer += 1
        literal_list = []
        if length_type == '0':
            length_bin = self.input_data[self.pointer:self.pointer + 15]
            self.pointer += 15
            subpacket_total_length = int(length_bin, 2)
            subpacket_end_pos = self.pointer + subpacket_total_length
            while self.pointer < subpacket_end_pos:
                literal_list.append(self.process_packet())
        elif length_type == '1':
            length = self.input_data[self.pointer:self.pointer + 11]
            self.pointer += 11
            number_of_subpackets = int(length, 2)
            for packet in range(number_of_subpackets):
                literal_list.append(self.process_packet())
        return operator_function_map[type](literal_list)


def part_one(input_filename):
    input_data = helpers.parse_input(input_filename)[0]
    input_data = input_data.lower()
    input_data = "".join([bin(int(char, 16))[2:].zfill(4) for char in input_data])
    compooper = Compooper(input_data)
    return compooper.version_total


def part_two(input_filename):
    input_data = helpers.parse_input(input_filename)[0]
    input_data = input_data.lower()
    input_data = "".join([bin(int(char, 16))[2:].zfill(4) for char in input_data])
    compooper = Compooper(input_data)
    return compooper.result


if __name__ == "__main__":
    print("*** PART ONE ***\n")
    print(f"Test result = {part_one('inputtest.txt')}\n")
    print(f"REAL RESULT = {part_one('input.txt')}\n\n")
    print("*** PART TWO ***\n")
    print(f"Test result = {part_two('inputtest.txt')}\n")
    print(f"REAL RESULT = {part_two('input.txt')}\n\n")
