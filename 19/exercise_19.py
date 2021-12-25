import itertools
import sys
from operator import add
from itertools import product, permutations
sys.path.append("..")
import helpers


ORIENTATIONS = list(itertools.product((1, -1), (1, -1), (1, -1)))


def get_all_rotations(x, y, z):
    output = []
    swapsies = list(itertools.permutations((x, y, z)))
    for swap in swapsies:
        for orientation in ORIENTATIONS:
            output.append(tuple(l * r for l, r in zip(swap, orientation)))
    return output


def parse_scanner_data(input_data):
    current_scanner = None
    scanner_data = set()
    scanner_dict = {}
    for line in input_data:
        if not line:
            scanner_dict[current_scanner] = scanner_data
            current_scanner = None
            scanner_data = set()
        elif line[0:3] == "---":
            current_scanner = int(line.split(" ")[2])
        else:
            x, y, z = line.split(",")
            scanner_data.add((int(x), int(y), int(z)))
    scanner_dict[current_scanner] = scanner_data
    return scanner_dict


def get_rotated_coords(scanner_idx, rotation_idx, scanner_dict):
    return {get_all_rotations(point[0], point[1], point[2])[rotation_idx] for point in scanner_dict[scanner_idx]}


def find_matchup(scanner_1, scanner_2, scanner_dict):
    scanner_2_rotations = {n: set() for n in range(48)}
    for point in scanner_dict[scanner_2]:
        rotations = get_all_rotations(point[0], point[1], point[2])
        for idx, point in enumerate(rotations):
            scanner_2_rotations[idx].add(point)
    for rotation in scanner_2_rotations:
        for beacon_a in scanner_dict[scanner_1]:
            for beacon_b in scanner_2_rotations[rotation]:
                overlap = 0
                offset = (beacon_a[0] - beacon_b[0], beacon_a[1] - beacon_b[1], beacon_a[2] - beacon_b[2])
                for nested_beacon_b in scanner_2_rotations[rotation]:
                    hypothetical_beacon = tuple(map(add, nested_beacon_b, offset))
                    if hypothetical_beacon in scanner_dict[scanner_1]:
                        overlap += 1
                if overlap >= 12:
                    print("found some overlap!")
                    scanner_2_rotations[rotation] = set([tuple(map(add, beacon, offset)) for beacon in scanner_2_rotations[rotation]])
                    return (offset, scanner_2_rotations[rotation])
    return None



def part_one_and_two(input_filename):
    input_data = helpers.parse_input(input_filename)
    scanner_dict = parse_scanner_data(input_data)
    locked_in = set([0])
    offsets = set()
    while len(locked_in) < len(scanner_dict):
        for scanner in scanner_dict:
            if scanner != 0 and scanner not in locked_in:
                matchup = find_matchup(0, scanner, scanner_dict)
                if matchup:
                    scanner_dict[0] = scanner_dict[0].union(matchup[1])
                    locked_in.add(scanner)
                    offsets.add(matchup[0])
                    print("locked in = ", locked_in)
                    print("offsets = ", offsets)
    print("max offsets = ", find_max_manhattan(offsets))
    return len(scanner_dict[0])


def find_max_manhattan(offsets):
    max_offset = 0
    for offset_1 in offsets:
        for offset_2 in offsets:
            if offset_1 != offset_2:
                offset_x = abs(offset_1[0] - offset_2[0])
                offset_y = abs(offset_1[1] - offset_2[1])
                offset_z = abs(offset_1[2] - offset_2[2])
                total_offset = sum([offset_x, offset_y, offset_z])
                if total_offset > max_offset:
                    max_offset = total_offset
    return max_offset


def find_max_manhattan_from_file(offsets_file):
    input_data = helpers.parse_input(offsets_file)
    offsets = [item[1:-1] for item in input_data]
    offsets = [item.split(", ") for item in offsets]
    offsets = [[int(subitem) for subitem in item] for item in offsets]
    return find_max_manhattan(offsets)


if __name__ == "__main__":
    print("*** BOTH PARTS ***\n")
    print(f"Test result = {part_one_and_two('inputtest.txt')}\n")
    print(f"REAL RESULT = {part_one_and_two('input.txt')}")
