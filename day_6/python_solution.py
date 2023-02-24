import InputManager as im
import GridHandler as gh
from collections import Counter


def get_lights(coords: tuple[int, int, int, int]) -> set[tuple[int, int]]:
    start_x, start_y, end_x, end_y = coords
    return {(x, y) for x in range(start_x, end_x+1) for y in range(start_y, end_y+1)}


def follow_instructions(all_inputs: list[str]) -> int:
    # 0 is off, 1 is on
    lights_status = {coord: 0 for coord in gh.GridHandler.generate_grid_coords(1000, 1000)}
    for instruction in all_inputs:
        coords = im.parse_int_in_line(instruction)
        target_lights = get_lights(coords)
        if "toggle" in instruction:
            for light in target_lights:
                lights_status[light] = 1 if lights_status[light] == 0 else 0
        else:
            if "on" in instruction:
                new_status = 1
            else:
                new_status = 0
            for light in target_lights:
                lights_status[light] = new_status
    return Counter(lights_status.values())[1]


def follow_brightness_settings(all_inputs: list[str]) -> int:
    lights_status = {coord: 0 for coord in gh.GridHandler.generate_grid_coords(1000, 1000)}
    for instruction in all_inputs:
        coords = im.parse_int_in_line(instruction)
        target_lights = get_lights(coords)
        if "toggle" in instruction:
            new_status = 2
        elif "on" in instruction:
            new_status = 1
        else:
            new_status = -1
        for light in target_lights:
            lights_status[light] += new_status
            lights_status[light] = 0 if lights_status[light] < 0 else lights_status[light]
    return sum(lights_status.values())


def get_answers():
    input_file = im.read_file("day_6/real_input.txt")
    all_inputs = im.group_file_info_with_single_new_line(input_file)
    part_1_answer = follow_instructions(all_inputs)
    part_2_answer = follow_brightness_settings(all_inputs)
    return part_1_answer, part_2_answer


if __name__ == '__main__':
    print(get_answers())

