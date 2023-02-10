import InputManager as im
import GridHandler as gh


def parse_input_path_info(input_file_path: str) -> str:
    return im.read_file(input_file_path)


def get_visited_locations(path_info: str):
    start_location = (0, 0)
    next_location = gh.move_coord(current_coord=start_location, step=path_info)



if __name__ == '__main__':

    elf_path_info = parse_input_path_info("day_3/real_input.txt")
    print(elf_path_info)


