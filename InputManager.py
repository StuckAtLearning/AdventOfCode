import re
from typing import Tuple, Set


def read_file_with_double_new_line(file_name: str, parse_int: bool = True) -> list[list[str | int]]:
    with open(file_name, 'r', encoding='utf-8') as file:
        data = file.read().split("\n\n")
    if parse_int:
        data_list = list()
        for i in data:
            input_line = i.split('\n')
            grouped_data = list()
            for j in input_line:
                if j.isdigit():
                    grouped_data.append(int(j))
                else:
                    int_input_line = parse_int_in_line(j)
                    grouped_data.append(int_input_line)
            data_list.append(grouped_data)
    else:
        data_list = [i.split("\n") for i in data]
    file.close()
    return data_list


def read_file_with_single_new_line(file_name: str, parse_int: bool = True) -> list[str]:
    with open(file_name, 'r', encoding='utf-8') as file:
        data_list = file.read().split("\n")
    if parse_int:
        data_list = [int(i) if i.isdigit() else parse_int_in_line(i) for i in data_list]
    file.close()
    return data_list


def parse_int_in_line(input_line: str) -> list[int]:
    parsed_input_line = [int(i) for i in re.findall(r'\d+', input_line)]
    return parsed_input_line


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


