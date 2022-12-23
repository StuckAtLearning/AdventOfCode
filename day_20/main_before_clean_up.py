import copy

import ReadFileFunctions as RFF


def convert_input_into_list(input_file_path):
    input_file = RFF.read_file_with_new_line(input_file_path)
    input_file = [int(i) for i in input_file]

    return input_file


def part_1(input_list):
    # part 2 only:
    input_list = [i * 811589153 for i in input_list]

    look_up_list = [i for i in range(len(input_list))]
    new_order = look_up_list[:]

    for mix in range(10):
        for i in range(len(look_up_list)):
            assert i == look_up_list[i]
            current_ele = input_list[i]
            look_up_ele = look_up_list[i]
            # print(new_order, 'step', i, 'moving', current_ele, current_ele % len(input_list))
            new_ele_index = (new_order.index(look_up_ele) + current_ele) % (len(input_list) - 1)
            # elif current_ele > 0:
            #     new_ele_index = (new_order.index(look_up_ele) + current_ele) % (len(input_list) - 1)
            #     if new_ele_index > len(input_list):
            #         new_ele_index = new_ele_index % (len(input_list) - 1)# + abs(new_ele_index // len(input_list))) % len(input_list)
            # else:
            #     new_ele_index = new_order.index(look_up_ele) + current_ele
            #     if new_ele_index < 0:
            #         new_ele_index = new_ele_index % (len(input_list) - 1)# - abs(new_ele_index // len(input_list))) % len(input_list)
            #
            new_order.remove(look_up_ele)
            new_order.insert(new_ele_index, look_up_ele)

    moved_list = list()
    for index in new_order:
        moved_list.append(input_list[index])

    # print(moved_list)

    return moved_list


def calculate_sum(ordered_list: list):
    zero_index = ordered_list.index(0)
    count_sum = 0
    count_sum += (ordered_list[(zero_index + 1000) % len(ordered_list)])
    count_sum += (ordered_list[(zero_index + 2000) % len(ordered_list)])
    count_sum += (ordered_list[(zero_index + 3000) % len(ordered_list)])

    return count_sum


if __name__ == "__main__":
    # part 1 test:
    input_file_list = convert_input_into_list("real_input.txt")
    ordered_input_list = part_1(input_file_list)
    print(calculate_sum(ordered_input_list))

    # part 1 answer:
    # input_file_list = convert_input_into_list("real_input.txt")
    # ordered_input_list = part_1(input_file_list)
    # print(calculate_sum(ordered_input_list))