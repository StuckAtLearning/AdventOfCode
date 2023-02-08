import InputManager as im


def get_surface_area(input_lines: list[list[int]]) -> int:
    surface_areas = [(lambda x, y, z: 2*x*y + 2*y*z + 2*x*z + min(x*y, y*z, x*z))(x, y, z) for [x, y, z] in input_lines]
    total_area = sum(surface_areas)
    return total_area


def get_ribbon_length(input_lines: list[list[int]]) -> int:
    ribbon_lengths = [(lambda x, y, z: min(2*x+2*y, 2*y+2*z, 2*x+2*z) + x*y*z)(x, y, z) for [x, y, z] in input_lines]
    total_length = sum(ribbon_lengths)
    return total_length


if __name__ == "__main__":
    dimensions = im.read_file("real_input.txt", parse_int=True)
    sa = get_surface_area(dimensions)
    print(sa)

    ribbon = get_ribbon_length(dimensions)
    print(ribbon)


