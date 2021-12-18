import sys
from itertools import product
sys.path.append("..")
import helpers


def brute_force_it(input_filename, part_one=True):
    input_data = helpers.parse_input(input_filename)
    input_data = input_data[0].split(": ")[1]
    x_range, y_range = input_data.split(", ")
    x_range = x_range[2:].split("..")
    y_range = y_range[2:].split("..")
    x_range = [item for item in range(int(x_range[0]), int(x_range[1]) + 1)]
    y_range = [item for item in range(int(y_range[0]), int(y_range[1]) + 1)]
    bottom_of_y = min(y_range)
    top_of_x = max(x_range)
    bottom_of_x = min(x_range)
    good_coords = set(product(x_range, y_range))
    uber_max_y = -999999
    successful_velocities = 0
    for x in range(0, 313):
        for y in range(-110, 1000):
            x_pos = 0
            y_pos = 0
            x_vel = x
            y_vel = y
            max_y = -99999999
            for step in range(1000):
                x_pos += x_vel
                y_pos += y_vel
                if y_pos > max_y:
                    max_y = y_pos
                if x_vel > 0:
                    x_vel -= 1
                # elif x_vel < 0:  WHY WOULD I CARE ABOUT THIS?!
                #     x_vel += 1
                y_vel -= 1
                if x_pos > top_of_x:
                    break
                if (x_pos, y_pos) in good_coords:
                    if max_y > uber_max_y:
                        uber_max_y = max_y
                    successful_velocities += 1
                    break
                if x_vel == 0:
                    if not bottom_of_x - 1 <= x_pos <= top_of_x:
                        break
                if y < bottom_of_y:
                    break
    if part_one:
        return uber_max_y
    else:
        return successful_velocities
#

if __name__ == "__main__":
    print("*** PART ONE ***\n")
    print(f"Test result = {brute_force_it('inputtest.txt', part_one=True)}\n")
    print(f"REAL RESULT = {brute_force_it('input.txt', part_one=True)}\n\n")
    print("*** PART TWO ***\n")
    print(f"Test result = {brute_force_it('inputtest.txt', part_one=False)}\n")
    print(f"REAL RESULT = {brute_force_it('input.txt', part_one=False)}\n\n")
