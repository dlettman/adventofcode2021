import sys
from functools import reduce
sys.path.append("..")
import helpers


# types of packet =
# literal: total length = 20 (5 hex chars)
# operator lt 0: total length = 20 (5 hex chars)
# operator lt 1: total length = 16 (4 hex chars)


# def parse_packet(packet):
#     version = packet[0:3]
#     id = packet[3:6]
#     if id == 4:  # literal
#         number_a = packet[6:11]
#         number_b = packet[11:16]
#         number_c = packet[16:21]
#     else:  # operator
#         length_type = packet[3]
#         if length_type == 0: # Next 15 bits indicate length
#             length = packet[4:19]
#         elif length_type == 1: # Next 11 bits represent number of sub-packets
#             length = packet[4:15]

def product(lst):
    return reduce(lambda x, y: x * y, lst)

def mysum(lst):
    return reduce(lambda x, y: x + y, lst)

def greaterthan(lst):
    return 1 if lst[0] > lst[1] else 0

def lessthan(lst):
    return 1 if lst[0] < lst[1] else 0

def equalto(lst):
    return 1 if lst[0] == lst[1] else 0

operator_function_map = {
    '000':  mysum,  # sum
    '001':  product,  # multiply
    '010':  min,  # min
    '011':  max,  # max
    '101':  greaterthan,  # greater than, always 2 subpackets
    '110':  lessthan,  # less than
    '111':  equalto,  # equal to
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
        # print(f"PROCESSING PACKET, POINTER = {self.pointer}")
        version, type = self.get_header()
        # print("version = ", version, "type = ", type)
        self.version_total += int(version, 2)
        self.pointer += 6
        if self.pointer == len(self.input_data) - 1:
            return
        if type == '100':  # literal
            return self.process_literal_packet()
        else:  # sum
            return self.process_operator_packet(type)


            ''' apply these functions to the literals within 
                and evaluate the big dang thing '''


    def process_literal_packet(self):
        number_payload = ""
        # print(self.pointer)
        while True:
            bit_prefix = self.input_data[self.pointer]
            self.pointer += 1
            number_payload += self.input_data[self.pointer : self.pointer + 4]
            self.pointer += 4
            if bit_prefix == '0':
                break
        number_payload = int(number_payload, 2)
        # print("number payload = ", number_payload)
        return number_payload


    def process_operator_packet(self, type):
        length_type = self.input_data[self.pointer]
        # print("length type = ", length_type)
        self.pointer += 1
        literal_list = []
        if length_type == '0':
            length_bin = self.input_data[self.pointer:self.pointer + 15]
            self.pointer += 15
            subpacket_total_length = int(length_bin, 2)
            # print(subpacket_total_length)
            subpacket_end_pos = self.pointer + subpacket_total_length
            while self.pointer < subpacket_end_pos:
                literal_list.append(self.process_packet())
        elif length_type == '1':
            length = self.input_data[self.pointer:self.pointer + 11]
            self.pointer += 11
            number_of_subpackets = int(length, 2)
            for packet in range(number_of_subpackets):
                literal_list.append(self.process_packet())
        # print("ll = ", literal_list)
        result = operator_function_map[type](literal_list)
        # print(result)
        return result
        # return operator_function_map[type](literal_list)



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
    # print(f"Test result = {part_one('inputtest.txt')}\n")
    print(f"REAL RESULT = {part_one('input.txt')}\n\n")
    print("*** PART TWO ***\n")
    # print(f"Test result = {part_two('inputtest.txt')}\n")
    print(f"REAL RESULT = {part_two('input.txt')}\n\n")
