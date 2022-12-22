import copy

import ReadFileFunctions as RFF


def convert_input_into_list(input_file_path):
    input_file = RFF.read_file_with_new_line(input_file_path)
    input_file = [int(i) for i in input_file]

    return input_file


def part_1(input_list):
    new_order = input_list[:]
    copy_input = input_list[:]

    for i in range(len(input_list)):
        current_ele = input_list[i]
        if current_ele == 0:
            continue
        elif current_ele > 0:
            new_ele_index = new_order.index(current_ele) + current_ele
            if new_ele_index > len(input_list):
                new_ele_index = ((new_ele_index % len(input_list)) + abs(new_ele_index // len(input_list))) % len(input_list)
        else:
            new_ele_index = new_order.index(current_ele) + current_ele
            if new_ele_index < 0:
                new_ele_index = ((new_ele_index % len(input_list)) - abs(new_ele_index // len(input_list))) % len(input_list)
        new_order.remove(current_ele)
        new_order.insert(new_ele_index, current_ele)
        print(new_order)

    return new_order


def calculate_sum(ordered_list: list):
    zero_index = ordered_list.index(0)
    count_sum = 0
    count_sum += ordered_list[(zero_index + 1000) % len(ordered_list)]
    count_sum += ordered_list[(zero_index + 2000) % len(ordered_list)]
    count_sum += ordered_list[(zero_index + 3000) % len(ordered_list)]

    return count_sum


if __name__ == "__main__":
    # part 1 test:
    input_file_list = convert_input_into_list("test_input.txt")
    ordered_input_list = part_1(input_file_list)
    print(calculate_sum(ordered_input_list))

    # part 1 answer:
    # input_file_list = convert_input_into_list("real_input.txt")
    # ordered_input_list = part_1(input_file_list)
    # print(calculate_sum(ordered_input_list))