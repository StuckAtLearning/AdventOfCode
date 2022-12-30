import ReadFileFunctions as RFF


def parse_input(input_file_path):
    input_file = RFF.read_file_with_new_line(input_file_path)

    # parsing the maze into a list format and a coordinate format
    maze = input_file[:-2]
    max_length_line = max([len(line) for line in maze])
    maze_list = [i + (" " * (max_length_line - len(i))) for i in maze]
    maze_list = [[c for c in i] for i in maze_list]

    maze_coord_dict = dict()
    for row in range(len(maze_list)):
        for column in range(len(maze_list[row])):
            maze_coord_dict[(row + 1, column + 1)] = maze_list[row][column]
            # direction = maze_list[row][column]
            # maze_coord_dict[direction].append((row + 1, column + 1))

    # parsing the instruction part of the input (last line of the input file)
    instruction = input_file[-1]
    parsed_instruction = list()
    digit_meter = 0
    for i in range(len(instruction)):
        if not instruction[i].isdigit():
            step_count = int(instruction[digit_meter:i])
            parsed_instruction.append(step_count)
            parsed_instruction.append(instruction[i])
            digit_meter = i + 1

    if len(instruction) > digit_meter:
        parsed_instruction.append(instruction[digit_meter:])

    return maze_list, maze_coord_dict, parsed_instruction


def print_map(maze_coord_dict, maze_width, maze_length):
    maze_list = list()
    for row in range(maze_length):
        maze_list.append(list())
        for column in range(maze_width):
            maze_list[row].append(None)

    for coord, symbol in maze_coord_dict.items():
        row = coord[0] - 1
        column = coord[1] - 1
        maze_list[row][column] = symbol

    print('\n'.join(''.join(row) for row in maze_list))


def part_1(maze_coord_dict, maze_width, maze_length, instructions):
    # test input start at (1, 9)
    current_coord = (1, 51)
    current_direction_index = 0
    direction_list_right_90 = [">", "v", "<", "^"]
    current_direction = direction_list_right_90[current_direction_index]

    maze_coord_dict[current_coord] = current_direction
    for instruction in instructions:

        # instruction is to change direction
        if isinstance(instruction, str):
            if instruction == "L":
                current_direction_index = (current_direction_index - 1) % 4
                current_direction = direction_list_right_90[current_direction_index]
            elif instruction == "R":
                current_direction_index = (current_direction_index + 1) % 4
                current_direction = direction_list_right_90[current_direction_index]

        # instruction is to walk n steps
        elif isinstance(instruction, int):

            # to go right on the map
            if current_direction == ">":
                for step_num in range(instruction):
                    if current_coord[1] == maze_width:
                        next_coord = (current_coord[0], 1)
                    else:
                        next_coord = (current_coord[0], current_coord[1]+1)

                    # if the next coordinate is the wall, stop
                    if maze_coord_dict[next_coord] == "#":
                        break

                    # if the next coordinate reaches to the right edge of the map
                    elif maze_coord_dict[next_coord] == " ":
                        # wrap around the map, starting from the left
                        while maze_coord_dict[next_coord] == " ":
                            if next_coord[1] < maze_width:
                                next_coord = (next_coord[0], next_coord[1] + 1)
                            else:
                                next_coord = (next_coord[0], 1)

                        # after wrapping around the map, if we see a wall, stop
                        if maze_coord_dict[next_coord] == "#":
                            break
                        # after wrapping around the map, if it isn't a wall, we take a step to the right
                        else:
                            maze_coord_dict[next_coord] = current_direction
                            current_coord = next_coord

                    # we take a step to the right
                    else:
                        maze_coord_dict[next_coord] = current_direction
                        current_coord = next_coord

            elif current_direction == "<":
                for step_num in range(instruction):
                    if current_coord[1] == 1:
                        next_coord = (current_coord[0], maze_width)
                    else:
                        next_coord = (current_coord[0], current_coord[1]-1)

                    # if the next coordinate is the wall, stop
                    if maze_coord_dict[next_coord] == "#":
                        break

                    # if the next coordinate reaches to the right edge of the map
                    elif maze_coord_dict[next_coord] == " ":
                        # wrap around the map, starting from the left
                        while maze_coord_dict[next_coord] == " ":
                            if next_coord[1] > 1:
                                next_coord = (next_coord[0], next_coord[1] - 1)
                            else:
                                next_coord = (next_coord[0], maze_width)

                        # after wrapping around the map, if we see a wall, stop
                        if maze_coord_dict[next_coord] == "#":
                            break
                        # after wrapping around the map, if it isn't a wall, we take a step to the right
                        else:
                            maze_coord_dict[next_coord] = current_direction
                            current_coord = next_coord

                    # we take a step to the right
                    else:
                        maze_coord_dict[next_coord] = current_direction
                        current_coord = next_coord

            elif current_direction == "v":
                for step_num in range(instruction):
                    if current_coord[0] == maze_length:
                        next_coord = (1, current_coord[1])
                    else:
                        next_coord = (current_coord[0] + 1, current_coord[1])

                    # if the next coordinate is the wall, stop
                    if maze_coord_dict[next_coord] == "#":
                        break

                    # if the next coordinate reaches to the right edge of the map
                    elif maze_coord_dict[next_coord] == " ":
                        # wrap around the map, starting from the left
                        while maze_coord_dict[next_coord] == " ":
                            if next_coord[0] < maze_length:
                                next_coord = (next_coord[0] + 1, next_coord[1])
                            else:
                                next_coord = (1, next_coord[1])

                        # after wrapping around the map, if we see a wall, stop
                        if maze_coord_dict[next_coord] == "#":
                            break
                        # after wrapping around the map, if it isn't a wall, we take a step to the right
                        else:
                            maze_coord_dict[next_coord] = current_direction
                            current_coord = next_coord

                    # we take a step to the right
                    else:
                        maze_coord_dict[next_coord] = current_direction
                        current_coord = next_coord

            elif current_direction == "^":
                for step_num in range(instruction):
                    if current_coord[0] == 1:
                        next_coord = (maze_length, current_coord[1])
                    else:
                        next_coord = (current_coord[0] - 1, current_coord[1])

                    # if the next coordinate is the wall, stop
                    if maze_coord_dict[next_coord] == "#":
                        break

                    # if the next coordinate reaches to the right edge of the map
                    elif maze_coord_dict[next_coord] == " ":
                        # wrap around the map, starting from the left
                        while maze_coord_dict[next_coord] == " ":
                            if next_coord[0] > 1:
                                next_coord = (next_coord[0] - 1, next_coord[1])
                            else:
                                next_coord = (maze_length, next_coord[1])

                        # after wrapping around the map, if we see a wall, stop
                        if maze_coord_dict[next_coord] == "#":
                            break
                        # after wrapping around the map, if it isn't a wall, we take a step to the right
                        else:
                            maze_coord_dict[next_coord] = current_direction
                            current_coord = next_coord

                    # we take a step to the right
                    else:
                        maze_coord_dict[next_coord] = current_direction
                        current_coord = next_coord

    print(current_coord, current_direction_index % 4)
    print((current_coord[0] * 1000) + (current_coord[1] * 4) + (current_direction_index % 4))
    print_map(maze_coord_dict, maze_width, maze_length)


# hard code a representation of the sube folding for the real input
def make_cube(maze_list, output_file_path):
    output_file = open(output_file_path, "w")

    row_count = 0
    for row in maze_list:
        cube_row = list()
        column_count = 0
        append_char = 1

        if 100 > row_count >= 50:
            append_char = 3
        elif 150 > row_count >= 100:
            append_char = 4
        elif row_count >= 150:
            append_char = 6
        for c in row:
            if (column_count >= 100) and (row_count <= 50):
                append_char = 2
            elif (column_count >= 50) and (row_count >= 100):
                append_char = 5

            if c != " ":
                cube_row.append(str(append_char))
            else:
                cube_row.append(" ")
            column_count += 1
        row_count += 1

        cube_row = "".join(cube_row)
        output_file.write(str(cube_row) + "\n")


def make_cube_face_dict(maze_coord_dict):
    cube_face_dict = dict()
    for coord, symbol in maze_coord_dict.items():
        row_num = coord[0]
        column_num = coord[1]
        if (100 > column_num >= 50) and (row_num <= 50):
            cube_face_dict[coord] = "1"
        elif (column_num >= 100) and (row_num <= 50):
            cube_face_dict[coord] = "2"
        elif (100 > column_num >= 50) and (100 > row_num >= 50):
            cube_face_dict[coord] = "3"
        elif (50 > column_num >= 0) and (150 > row_num >= 100):
            cube_face_dict[coord] = "4"
        elif (100 > column_num >= 50) and (150 > row_num >= 100):
            cube_face_dict[coord] = "5"
        elif (50 > column_num >= 0) and (200 > row_num >= 150):
            cube_face_dict[coord] = "6"
        else:
            cube_face_dict[coord] = " "

    return cube_face_dict


def make_a_move(current_coord, current_direction_index):
    # 0 = ">"
    # 1 = "v"
    # 2 = "<"
    # 3 = "^"
    row = current_coord[0]
    column = current_coord[1]

    # left edge of 1, going left
    if (1 <= row <= 50) and (column == 51) and (current_direction_index % 4 == 2):
        return (151 - row, 1), 0
    # top edge of 1, going up
    elif (row == 1) and (51 <= column <= 100) and (current_direction_index % 4 == 3):
        return (100 + column, 1), 0
    # top edge of 2, going up
    elif (row == 1) and (101 <= column <= 150) and (current_direction_index % 4 == 3):
        return (200, column - 100), 3
    # right edge of 2, going right
    elif (1 <= row <= 50) and (column == 150) and (current_direction_index % 4 == 0):
        return (151 - row, 100), 2
    # bottom edge of 2, going down
    elif (row == 50) and (101 <= column <= 150) and (current_direction_index % 4 == 1):
        return (column - 50, 100), 2
    # left edge of 3, going left
    elif (51 <= row <= 100) and (column == 51) and (current_direction_index % 4 == 2):
        return (101, row - 50), 1
    # right edge of 3, going right
    elif (51 <= row <= 100) and (column == 100) and (current_direction_index % 4 == 0):
        return (50, row + 50), 3
    # top edge of 4, going up
    elif (101 == row) and (1 <= column <= 50) and (current_direction_index % 4 == 3):
        return (column + 50, 51), 0
    # left edge of 4, going left
    elif (101 <= row <= 150) and (column == 1) and (current_direction_index % 4 == 2):
        return (151 - row, 51), 0
    # right edge of 5, going right
    elif (101 <= row <= 150) and (column == 100) and (current_direction_index % 4 == 0):
        return (151 - row, 150), 2
    # bottom edge of 5, going down
    elif (row == 150) and (51 <= column <= 100) and (current_direction_index % 4 == 1):
        return (column + 100, 50), 2
    # left edge of 6, going left
    elif (151 <= row <= 200) and (column == 1) and (current_direction_index % 4 == 2):
        return (1, row - 100), 1
    # bottom edge of 6, going down
    elif (row == 200) and (1 <= column <= 50) and (current_direction_index % 4 == 1):
        return (1, column + 100), 1
    # right edge of 6, going right
    elif (151 <= row <= 200) and (column == 50) and (current_direction_index % 4 == 0):
        return (150, row - 100), 3
    # everything else is normal
    else:
        if current_direction_index % 4 == 0:
            return (row, column + 1), 0
        elif current_direction_index % 4 == 1:
            return (row + 1, column), 1
        elif current_direction_index % 4 == 2:
            return (row, column - 1), 2
        else:
            return (row - 1, column), 3


def part_2(maze_coord_dict, maze_width, maze_length, instructions):
    # test input start at (1, 9), real input starts at (1, 51)
    current_coord = (1, 51)
    current_direction_index = 0
    direction_list_right_90 = [">", "v", "<", "^"]
    current_direction = direction_list_right_90[current_direction_index]

    maze_coord_dict[current_coord] = current_direction
    for instruction in instructions:#[:60]:

        print(instruction)

        # instruction is to change direction
        if isinstance(instruction, str):
            if instruction == "L":
                current_direction_index = (current_direction_index - 1) % 4
            elif instruction == "R":
                current_direction_index = (current_direction_index + 1) % 4

        # instruction is to walk n steps
        elif isinstance(instruction, int):
            for step_num in range(instruction):
                next_coord, new_direction_index = make_a_move(current_coord, current_direction_index)
                print(next_coord)

                # if the next coordinate is the wall, stop
                if maze_coord_dict[next_coord] == "#":
                    break

                current_direction_index = new_direction_index
                current_direction = direction_list_right_90[current_direction_index]
                maze_coord_dict[next_coord] = current_direction
                current_coord = next_coord

    print(current_coord, current_direction_index % 4)
    print((current_coord[0] * 1000) + (current_coord[1] * 4) + (current_direction_index % 4))
    print_map(maze_coord_dict, maze_width, maze_length)


if __name__ == "__main__":
    # # part 1 test
    # maze_map, maze_dict, instruction_list = parse_input("test_input.txt")
    # #print_map(maze_dict, len(maze_map[0]), len(maze_map))
    # part_1(maze_dict, len(maze_map[0]), len(maze_map), instruction_list)

    # part 1
    # maze_map, maze_dict, instruction_list = parse_input("real_input.txt")
    # #print_map(maze_dict, len(maze_map[0]), len(maze_map))
    # part_1(maze_dict, len(maze_map[0]), len(maze_map), instruction_list)

    # part 2 test
    maze_map, maze_dict, instruction_list = parse_input("real_input.txt")
    # make_cube(maze_map, "cube_lookup.txt")
    # cube_dict = make_cube_face_dict(maze_dict)
    # print_map(cube_dict, len(maze_map[0]), len(maze_map))
    # print_map(maze_dict, len(maze_map[0]), len(maze_map))
    part_2(maze_dict, len(maze_map[0]), len(maze_map), instruction_list)
    # wrong answer: 14451, < 73263, 115369
