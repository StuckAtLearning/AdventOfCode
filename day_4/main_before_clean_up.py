import ReadFileFunctions as RFF
import HelperFunctions as HF
from collections import Counter


def part_1(test_input_file):
    test_input = RFF.read_file_with_new_line(test_input_file)

    count = 0
    for single_input in test_input:
        # parsing the input
        pairings = single_input.split(",")
        left = (pairings[0].split("-")[0], pairings[0].split("-")[1])
        right = (pairings[1].split("-")[0], pairings[1].split("-")[1])

        # check if the left input fully engulf the right input
        if (int(left[0]) <= int(right[0])) and (int(left[1]) >= int(right[1])):
            count += 1
        # check the other way around
        elif (int(left[0]) >= int(right[0])) and (int(left[1]) <= int(right[1])):
            count += 1

    return count


def part_2(test_input_file):
    test_input = RFF.read_file_with_new_line(test_input_file)
    count = 0
    for single_input in test_input:
        pairings = single_input.split(",")
        left = (int(pairings[0].split("-")[0]), int(pairings[0].split("-")[1]))
        right = (int(pairings[1].split("-")[0]), int(pairings[1].split("-")[1]))

        # using sets to check overlaps
        left_set = set(range(left[0], left[1]+1))
        right_set = set(range(right[0], right[1]+1))

        if left_set & right_set:
            count += 1

    return count


if __name__ == '__main__':
    # print(part_1("test_input.txt"))
    print(part_1("real_input.txt"))

    # print(part_2("test_input.txt"))
    print(part_2("real_input.txt"))

    # answers:
    # 496
    # 847

