# https://github.com/shemetz/advent_of_code_2023/blob/main/day24.py
import itertools
import z3 as z3

def parse_input(input_file):
    parsed_input = list()
    with open(input_file) as file:
        for line in file:
            position, velocity = line.split(" @ ")
            px, py, pz = position.split(", ")
            vx, vy, vz = velocity.split(", ")
            parsed_input.append((
                (int(px), int(py), int(pz)),
                (int(vx), int(vy), int(vz))
            ))
    return parsed_input


def get_m_and_b(hailstone):  # y = mx + b
    ((px, py, _), (vx, vy, _)) = hailstone
    return vy/vx, py - (vy/vx)*px


    # find intersection
    # ax + b = cx + d
    # ax - cx = d - b
    # x(a - c) = d - b
    # x = (d - b) / (a - c)
def part_1(parsed_input, test_area):
    intersection_counter = 0
    for hailstone_a, hailstone_b in itertools.combinations(parsed_input, 2):
        hailstone_a_m, hailstone_a_b = get_m_and_b(hailstone_a)
        hailstone_b_m, hailstone_b_b = get_m_and_b(hailstone_b)
        if hailstone_a_m == hailstone_b_m: # a // b
            continue

        ix = (hailstone_b_b - hailstone_a_b) / (hailstone_a_m - hailstone_b_m)
        iy = hailstone_a_m * ix + hailstone_a_b

        t1 = (ix - hailstone_a[0][0]) / hailstone_a[1][0]
        t2 = (ix - hailstone_b[0][0]) / hailstone_b[1][0]

        if t1 < 0 or t2 < 0:
            continue

        if test_area[0] <= ix <= test_area[1] and test_area[0] <= iy <= test_area[1]:
            intersection_counter += 1

    return intersection_counter


# I actually have no idea how this works
def part_2(parsed_input, test_area):
    pxr, pyr, pzr, vxr, vyr, vzr = z3.Reals("pxr pyr pzr vxr vyr vzr")
    solver = z3.Solver()

    for i, h in enumerate(parsed_input[:3]):
        variable_i = z3.Real(f"t{i}")
        solver.add(variable_i > 0)
        solver.add(pxr + variable_i * vxr == h[0][0] + variable_i * h[1][0])
        solver.add(pyr + variable_i * vyr == h[0][1] + variable_i * h[1][1])
        solver.add(pzr + variable_i * vzr == h[0][2] + variable_i * h[1][2])
    solver.check()
    total = sum(solver.model()[var].as_long() for var in [pxr, pyr, pzr])
    return total


def main():
    parsed_input = parse_input("real_input.txt")
    # test_area = (7, 27)
    test_area = (200000000000000, 400000000000000)
    part_1_answer = part_1(parsed_input, test_area)
    part_2_answer = part_2(parsed_input, test_area)
    print(part_1_answer)
    print(part_2_answer)


main()
