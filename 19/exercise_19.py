import itertools
import sys
import numpy as np
import scipy
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


# def create_constellation(coord_set):
#     constellation = set()
#     for point in coord_set:
#         for point_2 in coord_set:
#             if point != point_2:
#                 constellation.add((point[0] - point_2[0], point[1] - point_2[1], point[2] - point_2[2]))
#     return constellation


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
    return scanner_dict


#
# def diff_constellations(scanner_1, scanner_2, scanner_dict):
#     scanner_1_constellation = create_constellation(scanner_dict[scanner_1])
#     scannner_2_rotations = {n: set() for n in range(0, 48)}
#     for point in scanner_dict[scanner_2]:
#         rotations = get_all_rotations(point[0], point[1], point[2])
#         for idx, point in enumerate(rotations):
#             scannner_2_rotations[idx].add(point)
#     scanner_2_constellations = []
#     for rotation in scannner_2_rotations:
#         scanner_2_constellations.append(create_constellation(scannner_2_rotations[rotation]))
#     probably_right_constellation = None
#     max_overlap = 0
#     for idx, constellation in enumerate(scanner_2_constellations):
#         overlap = len(constellation.intersection(scanner_1_constellation))
#         if overlap > max_overlap:
#             probably_right_constellation = (constellation, idx)
#             max_overlap = overlap
#     if probably_right_constellation:
#         print("probably right rotation idx is ", probably_right_constellation[1])
#         print("len int is ", max_overlap)
#     if probably_right_constellation:
#         return probably_right_constellation[1], max_overlap
#     else:
#         return None, 0


def get_rotated_coords(scanner_idx, rotation_idx, scanner_dict):
    print(scanner_dict[scanner_idx])
    return {get_all_rotations(point[0], point[1], point[2])[rotation_idx] for point in scanner_dict[scanner_idx]}


def find_matchup(scanner_1, scanner_2, scanner_dict):
    scanner_2_rotations = {}
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
                    if nested_beacon_b + offset in scanner_dict[scanner_1]:
                        overlap += 1
                if overlap >= 12:
                    return (offset, scanner_2_rotations[rotation])



def part_one(input_filename):
    input_data = helpers.parse_input(input_filename)
    scanner_dict = parse_scanner_data(input_data)
    constellation_dict = {}
    rotation_locked = set()
    for scanner in scanner_dict:
        constellation_dict[scanner] = create_constellation(scanner_dict[scanner])
    for scanner in scanner_dict:
        for other_scanner in scanner_dict:
            if scanner != other_scanner and other_scanner not in rotation_locked:
                probable_rotation, confidence = diff_constellations(scanner, other_scanner, scanner_dict)
                if confidence > 12:
                    print(f"found one (?!) - scanner {other_scanner} rotating to {probable_rotation}")
                    rotation_locked.add(other_scanner)
                    scanner_dict[other_scanner] = get_rotated_coords(other_scanner,probable_rotation, scanner_dict)


def part_two(input_filename):
    input_data = helpers.parse_input(input_filename)
    if not input_data:
        return "*** NO INPUT SUPPLIED ***"
    # do stuff here
    output = input_data
    return output


if __name__ == "__main__":
    print("*** PART ONE ***\n")
    print(f"Test result = {part_one('inputtest.txt')}\n")
    # print(f"REAL RESULT = {part_one('input.txt')}\n\n")
    # print("*** PART TWO ***\n")
    # print(f"Test result = {part_two('inputtest.txt')}\n")
    # print(f"REAL RESULT = {part_two('input.txt')}\n\n")
