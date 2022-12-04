from typing import Tuple, Set, Any

import ReadFileFunctions as RFF
from typing import List


def parse_assignments(input_assignments: str) -> tuple[set[int], set[int]]:
    pairings = input_assignments.split(",")
    first_elf = (int(pairings[0].split("-")[0]), int(pairings[0].split("-")[1]))
    second_elf = (int(pairings[1].split("-")[0]), int(pairings[1].split("-")[1]))

    first_assignment = set(range(first_elf[0], first_elf[1] + 1))
    second_assignment = set(range(second_elf[0], second_elf[1] + 1))

    return first_assignment, second_assignment


# my naming creativity apparently flies out of the window when it hits Day 4, good to know
def part_1(test_input_file):
    work_assignments = RFF.read_file_with_new_line(test_input_file)
    overlap_count = 0
    for assignment in work_assignments:
        first_elf, second_elf = parse_assignments(assignment)
        # sets also work this way! subset <= another set is a thing!
        overlap_count += 1 if (first_elf <= second_elf) or (first_elf >= second_elf) else 0

    return overlap_count


def part_2(test_input_file):
    work_assignments = RFF.read_file_with_new_line(test_input_file)
    overlap_count = 0
    for assignment in work_assignments:
        first_elf, second_elf = parse_assignments(assignment)
        overlap_count += 1 if first_elf & second_elf else 0

    return overlap_count


if __name__ == '__main__':
    print(part_1("real_input.txt"))
    print(part_2("real_input.txt"))

    # answers:
    # 496
    # 847
