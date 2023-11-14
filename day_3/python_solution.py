import InputManager as im
from GridHandler import GridHandler as gh


def parse_input_path_info(input_file_path: str) -> str:
    return im.read_file(input_file_path)


def get_visited_locations(path_info: str, start_location: tuple[int, int] = (0, 0)) -> set[tuple[int, int]]:
    path_directions = im.parse_directions(path_info)
    seen_location = {start_location}
    for direction in path_directions:
        next_location = gh.move_coord(current_coord=start_location, step=direction)
        start_location = next_location
        seen_location.add(start_location)
    return seen_location


def get_visited_locations_with_robot(path_info: str) -> int:
    santa_path = ''.join([path_info[i] for i in range(0, len(path_info), 2)])
    robot_path = ''.join([path_info[i] for i in range(1, len(path_info), 2)])

    santa_locations = get_visited_locations(santa_path)
    robot_locations = get_visited_locations(robot_path)

    return len(santa_locations.union(robot_locations))


def get_answers():
    elf_path_info = parse_input_path_info("day_3/real_input.txt")
    part_1_answer = len(get_visited_locations(elf_path_info))
    part_2_answer = get_visited_locations_with_robot(elf_path_info)
    return part_1_answer, part_2_answer


if __name__ == '__main__':
    print(get_answers())


