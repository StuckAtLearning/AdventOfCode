import itertools

import ReadFileFunctions as RFF
import ast
import functools
from typing import Union, List


"""
[1, 1, 3, 1, 1] [1, 1, 5, 1, 1]
[[1], [2, 3, 4]] [[1], 4]
[9] [[8, 7, 6]]
[[4, 4], 4, 4] [[4, 4], 4, 4, 4]
[7, 7, 7, 7] [7, 7, 7]
[] [3]
[[[]]] [[]]
[1, [2, [3, [4, [5, 6, 7]]]], 8, 9] [1, [2, [3, [4, [5, 6, 0]]]], 8, 9]
"""
# [[1], 1] [1, [1]] fine


# def insert_list_nooow(insert_list, completed_list):
#     inserted_list = list()
#     stack = completed_list
#     count = 0
#     while stack and insert_list:
#         item = stack.pop()
#         insert_item = insert_list.pop()
#         if isinstance(item, list):
#             inserted_list += [[insert_item]]
#             count += 1
#             stack.extend(item)
#         else:
#             insert_list.append(insert_item)
#     return inserted_list


def part_1(input_file_path: str) -> int:
    input_file = RFF.read_file_double_new_line(input_file_path)
    count = 1
    correct_order = list()
    for group in input_file:
        left = ast.literal_eval(group[0])
        right = ast.literal_eval(group[1])
        if non_recursive_comparator(left, right) == 1:
            correct_order.append(count)
        count += 1
    return sum(correct_order)


def part_2(input_file_path: str) -> int:
    input_file = RFF.read_file_double_new_line(input_file_path)
    input_list = list()
    for group in input_file:
        input_list.append(ast.literal_eval(group[0]))
        input_list.append(ast.literal_eval(group[1]))

    input_list.append([[2]])
    input_list.append([[6]])
    sorted_input_list = sorted(input_list, key=functools.cmp_to_key(non_recursive_comparator), reverse=True)

    divider_1 = sorted_input_list.index([[2]]) + 1
    divider_2 = sorted_input_list.index([[6]]) + 1
    decoder_key = divider_1 * divider_2
    return decoder_key


def non_recursive_comparator(left: int | list[int], right: int | list[int]) -> int:
    if (isinstance(left, int)) and (isinstance(right, int)):
        if left < right:
            return 1
        elif left == right:
            return 0
        return -1
    if (isinstance(left, list)) and (isinstance(right, list)):
        check_num = min(len(left), len(right))
        for i in range(check_num):
            if non_recursive_comparator(left[i], right[i]) == 1:
                return 1
            elif non_recursive_comparator(left[i], right[i]) == 0:
                continue
            return -1

        if len(left) == len(right):
            return 0
        elif check_num == len(left):
            return 1
        else:
            return -1
    if (isinstance(left, list)) and (isinstance(right, int)):
        new_right = [right]
        return non_recursive_comparator(left, new_right)
    if (isinstance(right, list)) and (isinstance(left, int)):
        new_left = [left]
        return non_recursive_comparator(new_left, right)


if __name__ == "__main__":
    # part_1_test_answer = part_1("advanced_test_input.txt.txt")
    # print(part_1_test_answer)
    # part_1_answer = part_1("real_input.txt")
    # print(part_1_answer)

    # part_2_test_answer = part_2("advanced_test_input.txt.txt")
    # print(part_2_test_answer)

    part_2_answer = part_2("real_input.txt")
    print(part_2_answer)
