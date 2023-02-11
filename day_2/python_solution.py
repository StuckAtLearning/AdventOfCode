import InputManager as im


def parse_input_file(file_name: str) -> list[list[int]]:
    info = im.read_file(file_name)
    dimensions_info = im.group_file_info_with_single_new_line(info)
    parsed_dimensions_info = [im.parse_int_in_line(i) for i in dimensions_info]
    return parsed_dimensions_info


def get_surface_area(input_lines: list[list[int]]) -> int:
    surface_areas = [(lambda x, y, z: 2*x*y + 2*y*z + 2*x*z + min(x*y, y*z, x*z))(x, y, z) for [x, y, z] in input_lines]
    total_area = sum(surface_areas)
    return total_area


def get_ribbon_length(input_lines: list[list[int]]) -> int:
    ribbon_lengths = [(lambda x, y, z: min(2*x+2*y, 2*y+2*z, 2*x+2*z) + x*y*z)(x, y, z) for [x, y, z] in input_lines]
    total_length = sum(ribbon_lengths)
    return total_length


def get_answers():
    dimensions = parse_input_file("day_2/real_input.txt")
    part_1_answer = get_surface_area(dimensions)
    part_2_answer = get_ribbon_length(dimensions)
    return part_1_answer, part_2_answer


if __name__ == "__main__":
    get_answers()


