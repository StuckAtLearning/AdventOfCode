import re
from typing import Tuple, Set


def read_file_with_double_new_line(file_name: str) -> list[list[str]]:
    with open(file_name, 'r', encoding='utf-8') as file:
        data = file.read().split("\n\n")
    data_list = [i.split("\n") for i in data]

    file.close()
    return data_list


def read_file_with_new_line(file_name: str) -> list[str]:
    with open(file_name, 'r', encoding='utf-8') as file:
        data = file.read().split("\n")

    file.close()
    return data


def parse_int_only(file_info: list[list[str]], extra_parser: None | list[str]) -> dict[int, list[int]]:
    parsed_input = dict()
    for identifier in range(len(file_info)):
        for info in file_info[identifier]:
            parsed_info = [int(s) for s in re.findall(r'\d+', info)]
            parsed_input[identifier + 1] = parsed_info
    # if extra_parser:
    #     for identifier, parsed_info in parsed_input.items():
    #
    return parsed_input


# def parse_two_state_grid(file_info: list[list[str]], marker: str, start_index_one=False) -> \
#         tuple[set[tuple[int, int]], set[tuple[int, int]]]:
#     marked_coords = set()
#     unmarked_coords = set()
#     for y in range(len(file_info)):
#         for x in range(len(file_info[y])):
#             coord_x, coord_y = x, y
#             if start_index_one:
#                 coord_x += 1
#                 coord_y += 1
#             if file_info[y][x] == marker:
#                 marked_coords.add((coord_x, coord_y))
#             else:
#                 unmarked_coords.add((coord_x, coord_y))
#     return marked_coords, unmarked_coords


def parse_grid(file_info: list[list[str]], states: [str], start_index_one=False) -> \
        dict[str, set[tuple[int, int]]]:
    grid_coords = dict()
    for marker in states:
        grid_coords[marker] = set()
    for y in range(len(file_info)):
        for x in range(len(file_info[y])):
            for marker in states:
                coord_x, coord_y = x, y
                if start_index_one:
                    coord_x += 1
                    coord_y += 1
                if file_info[y][x] == marker:
                    grid_coords[marker].add((coord_x, coord_y))
    return grid_coords


