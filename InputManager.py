import re


def read_file(file_name: str) -> str:
    with open(file_name, 'r', encoding='utf-8') as file:
        file_info = file.read()
    return file_info


def group_file_info_with_double_new_line(file_info: str) -> list[list[str]]:
    return [i.split("\n") for i in file_info.split("\n\n")]


def group_file_info_with_single_new_line(file_info: str) -> list[str]:
    return file_info.split("\n")


def parse_int_in_line(input_line: str, include_negatives: bool = False) -> list[int]:
    if include_negatives:
        pattern = r'-?\d+'
        print(re.findall(pattern, input_line))
    else:
        pattern = r'\d+'
    return [int(i) for i in re.findall(pattern, input_line)]


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


