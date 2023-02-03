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
    return parsed_input


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


