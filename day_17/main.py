import copy


def get_rock(n_th_fall: int) -> list[list[int]]:
    order_of_rocks = ["-", "+", "L", "I", "#"]
    rocks_shape_dict = {"-": [[1, 1, 1, 1]],
                        "+": [[0, 1, 0],
                              [1, 1, 1],
                              [0, 1, 0]],
                        "L": [[0, 0, 1],
                              [0, 0, 1],
                              [1, 1, 1]],
                        "I": [[1],
                              [1],
                              [1],
                              [1]],
                        "#": [[1, 1],
                              [1, 1]]}
    current_rock = order_of_rocks[(n_th_fall-1) % 5]
    current_rock_shape = rocks_shape_dict[current_rock]

    return current_rock_shape


def get_rock_height(rock_shape: list[list[int]]) -> int:
    rock_height = len(rock_shape)
    return rock_height


def get_rock_width(rock_shape: list[list[int]]) -> int:
    rock_width = len(rock_shape[0])
    return rock_width


def read_push_directions(directions_file_path: str) -> list[str]:
    directions_file = open(directions_file_path, "r")
    directions = directions_file.readlines()
    directions_list = [str(direction) for direction in directions[0]]
    return directions_list


def push_rock(directions: list[str], direction_index: int, rock_width: int, start_index: int) -> int:
    # push to the right
    if directions[direction_index % len(directions)] == ">":
        if start_index + rock_width < 7:
            start_index += 1
            # print("moved right")

    # push to the left
    else:
        if start_index > 0:
            start_index -= 1
            # print("moved left")

    # the new index where the rock should fall
    return start_index


def get_rock_index(one_row: list[list[int]]) -> list[int]:
    indices = list()
    for index_count, cell in enumerate(one_row):
        if cell == 1:
            indices.append(index_count)
    return indices


def check_going_down(current_checking_row_num: int, current_rock: list[list[int]], base_floor_map: list[list[int]],
                     start_index: int) -> bool:
    row_window = list()
    for i in range(len(current_rock)):
        row_window.append(base_floor_map[current_checking_row_num + 1 + i])

    # construct the current rock with the base floor environment
    current_rock_window = list()
    for row in current_rock:
        new_row = [0] * start_index + row + [0] * (7 - get_rock_width(current_rock) - start_index)
        current_rock_window.append(new_row)

    assert len(row_window) == len(current_rock_window)

    # print('=== Down rock window ==\n' + '\n'.join([''.join('.#'[y] for y in x) for x in current_rock_window]) + '\n===')
    # print('=== Down floor window ==\n' + '\n'.join([''.join('.#'[y] for y in x) for x in row_window]) + '\n===')

    for row, rock_row in zip(row_window, current_rock_window):
        for floor_val, rock_val in zip(row, rock_row):
            if (floor_val == rock_val) and (floor_val != 0):
                return False
    return True



    # if rock_shape != [[0, 1, 0], [1, 1, 1], [0, 1, 0]]:
    #     bottom_row = [0] * rock_left_index + rock_shape[-1] + [0] * (7-get_rock_width(rock_shape)-rock_left_index)
    #     top_row = base_floor_map[rock_top_index + get_rock_height(rock_shape)]
    #     bottom_rock_positions = set(get_rock_index(bottom_row))
    #     top_rock_positions = set(get_rock_index(top_row))
    #
    #     #print('bottom row of rock', ''.join('.#'[r] for r in bottom_row))
    #     #print('top row of floor', ''.join(['.#'[r] for r in top_row]))
    #
    #     # if there is intersection where 1 is in the list, then the rock should stop falling and rest in place
    #     safe_landing = bottom_rock_positions.intersection(top_rock_positions)
    #     return not safe_landing
    # else:
    #     bottom_row = [0] * rock_left_index + rock_shape[-2] + [0] * (7-get_rock_width(rock_shape)-rock_left_index)
    #     top_row = base_floor_map[rock_top_index + get_rock_height(rock_shape)]
    #     bottom_rock_positions = set(get_rock_index(bottom_row))
    #     top_rock_positions = set(get_rock_index(top_row))
    #
    #     safe_landing = bottom_rock_positions.intersection(top_rock_positions)
    #     if safe_landing:
    #         bottom_row = [0] * rock_left_index + rock_shape[-1] + [0] * (7-get_rock_width(rock_shape)-rock_left_index)
    #         top_row = base_floor_map[rock_top_index + get_rock_height(rock_shape) + 1]
    #         bottom_rock_positions = set(get_rock_index(bottom_row))
    #         top_rock_positions = set(get_rock_index(top_row))
    #
    #         # if there is intersection where 1 is in the list, then the rock should stop falling and rest in place
    #         safe_landing = bottom_rock_positions.intersection(top_rock_positions)
    #         return not safe_landing
    #     return False


def check_go_right(current_checking_row_num: int, current_rock: list[list[int]], base_floor_map: list[list[int]],
                   start_index: int) -> bool:
    row_window = list()
    for i in range(len(current_rock)):
        row_window.append(base_floor_map[current_checking_row_num + i])

    # construct the current rock with the base floor environment
    current_rock_window = list()
    for row in current_rock:
        new_row = [0] * start_index + row + [0] * (7 - get_rock_width(current_rock) - start_index)
        current_rock_window.append(new_row)

    # print('row window for floor[0]', len(row_window), ''.join('.#'[r] for r in row_window[0]))
    # print('row window for rock[0]', len(current_rock_window), ''.join(['.#'[r] for r in current_rock_window[0]]))

    assert len(row_window) == len(current_rock_window)

    for row, rock_row in zip(row_window, current_rock_window):
        rock_row = [0] + rock_row[:-1]
        for floor_val, rock_val in zip(row, rock_row):
            if (floor_val == rock_val) and (floor_val != 0):
                return False
    return True

    #
    # row_window = list()
    # for i in range(len(current_rock)):
    #     row_window.append(base_floor_map[current_checking_row_num + i])
    #
    # # construct the current rock with the base floor environment
    # current_rock_window = list()
    # for row in current_rock:
    #     new_row = [0] * current_checking_row_num + row + [0] * (7 - get_rock_width(current_rock) - current_checking_row_num)
    #     current_rock_window.append(new_row)
    #
    # # to check if the current rock can go right
    # # get all indices of the left most 1 from all the four rows, [top, 2nd row, 3rd row, bottom]
    # left_edge_indices = list()
    # for row in row_window:
    #     left_edge_index = len(row)
    #     for i in range(len(row)):
    #         if row[i] == 1:
    #             left_edge_index = min(left_edge_index, i)
    #     left_edge_indices.append(left_edge_index)
    #
    # # get all indices of the right most 1 of the current rock, [top, 2nd row, 3rd row, bottom]
    # right_edge_indices = list()
    # for row in current_rock_window:
    #     right_most_index = 0
    #     for i in range(len(row)):
    #         if row[i] == 1:
    #             right_most_index = max(right_most_index, i)
    #     right_edge_indices.append(right_most_index)
    #
    # # print(left_edge_indices)
    # # print("base floor: \n", '===\n' + '\n'.join([''.join('.#'[y] for y in x) for x in row_window]) + '\n===')
    # # print(right_edge_indices)
    # # print("block window: \n", '===\n' + '\n'.join([''.join('.#'[y] for y in x) for x in current_rock_window]) + '\n===')
    # # if there is no overlapping indices, then it can go right
    # for i in range(len(left_edge_indices)):
    #     if left_edge_indices[i] == right_edge_indices[i]:
    #         return False
    # return True


def check_go_left(current_checking_row_num: int, current_rock: list[list[int]], base_floor_map: list[list[int]],
                  start_index: int) -> bool:
    row_window = list()
    for i in range(len(current_rock)):
        row_window.append(base_floor_map[current_checking_row_num + i])

    # construct the current rock with the base floor environment
    current_rock_window = list()
    for row in current_rock:
        new_row = [0] * start_index + row + [0] * (7 - get_rock_width(current_rock) - start_index)
        current_rock_window.append(new_row)

    # print('row window for floor[0]', len(row_window), ''.join('.#'[r] for r in row_window[0]))
    # print('row window for rock[0]', len(current_rock_window), ''.join(['.#'[r] for r in current_rock_window[0]]))

    assert len(row_window) == len(current_rock_window)

    for row, rock_row in zip(row_window, current_rock_window):
        rock_row = rock_row[1:] + [0]
        for floor_val, rock_val in zip(row, rock_row):
            if (floor_val == rock_val) and (floor_val != 0):
                return False
    return True


    # # to check if the current rock can go left
    # # get all indices of the right most 1 from all the four rows, [top, 2nd row, 3rd row, bottom]
    # right_edge_indices = list()
    # for row in row_window:
    #     right_most_index = 0
    #     for i in range(len(row)):
    #         if row[i] == 1:
    #             right_most_index = max(right_most_index, i)
    #     right_edge_indices.append(right_most_index)
    #
    # # get all indices of the left most 1 of the current rock, [top, 2nd row, 3rd row, bottom]
    # left_edge_indices = list()
    # for row in current_rock_window:
    #     left_edge_index = len(row)
    #     for i in range(len(row)):
    #         if row[i] == 1:
    #             left_edge_index = min(left_edge_index, i)
    #     left_edge_indices.append(left_edge_index)
    #
    # # print(left_edge_indices, right_edge_indices)
    # # print("base floor: \n", '===\n' + '\n'.join([''.join('.#'[y] for y in x) for x in row_window]) + '\n===')
    # # print("block window: \n", '===\n' + '\n'.join([''.join('.#'[y] for y in x) for x in current_rock_window]) + '\n===')
    #
    # # if there is no overlapping indices, then it can go left
    # for i in range(len(left_edge_indices)):
    #     if left_edge_indices[i] == right_edge_indices[i]:
    #         return False
    # return True


def get_top_rock_height(base_floor_map: list[list[int]]) -> int:
    for i in range(len(base_floor_map)):
        if 1 in base_floor_map[i]:
            return i


def organize_base_floor(old_base_floor: list[list[int]]) -> list[list[int]]:
    top_rock_height = get_top_rock_height(old_base_floor)
    new_base_floor = old_base_floor[top_rock_height:]
    return new_base_floor


def part_1_tetris(directions: list[str]) -> int:
    buffer_room = [0]*7
    base_floor = [[1] * 7]
    floor_height = len(base_floor) - 3
    directions_length = len(directions)

    current_direction_index = 0
    # 1_000_000_000_000
    # 2849 is the second occurrence, height 4438
    # 1154 is the first occurrence, height 1804
    for round_num in range(1, 2501):

        # print('=== Before Rock Falling ==\n' + '\n'.join([''.join('.#'[y] for y in x) for x in base_floor]) + '\n===')

        # the rock that is falling right now
        current_rock_shape = get_rock(round_num)
        curren_rock_height = get_rock_height(current_rock_shape)
        current_rock_width = get_rock_width(current_rock_shape)
        current_rock_left_edge = [i[0] for i in current_rock_shape]
        current_rock_right_edge = [i[-1] for i in current_rock_shape]
        top_rock_height = get_top_rock_height(base_floor)

        base_floor = organize_base_floor(base_floor)
        for i in range((curren_rock_height + 3)):
            base_floor.insert(0, buffer_room[:])
        start_index = 2
        rock_bottom_row = [0] * start_index + current_rock_shape[-1] + [0] * (7-current_rock_width-start_index)
        examine_row_num = 0
        row_to_examine = base_floor[examine_row_num]

        # print('=== Start of Rock Falling ==\n' + '\n'.join([''.join('.#'[y] for y in x) for x in base_floor]) + '\n===')

        flag = True
        while flag:

            # print(('=== Before Rock %s ==\n' % {'>': 'Right', '<': 'Left'}[directions[current_direction_index]]) + '\n'.join([
            #     ''.join((
            #         '.@'[current_rock_shape[y - examine_row_num][x - start_index]]
            #         if examine_row_num <= y < len(current_rock_shape) + examine_row_num and
            #            start_index <= x < len(current_rock_shape[y - examine_row_num]) + start_index
            #         else '.#'[r]
            #     ) for x, r in enumerate(row)) for y, row in enumerate(base_floor)
            # ]) + '\n===')

            # print("examine row num: ", examine_row_num, "total floor height: ", get_rock_height(base_floor))
            if directions[current_direction_index % directions_length] == ">":
                if check_go_right(examine_row_num, current_rock_shape, base_floor, start_index):
                    # print("can't go right at: ", start_index)
                    # print('Passed Rock check')
                    start_index = push_rock(directions, current_direction_index % directions_length, current_rock_width, start_index)

                    # update the new bottom row
                    rock_bottom_row = [0] * start_index + current_rock_shape[-1] + [0] * (
                                7 - current_rock_width - start_index)
            else:
                if check_go_left(examine_row_num, current_rock_shape, base_floor, start_index):
                    # print('Passed rock check')
                    start_index = push_rock(directions, current_direction_index % directions_length, current_rock_width, start_index)

                    # update the new bottom row
                    rock_bottom_row = [0] * start_index + current_rock_shape[-1] + [0] * (7-current_rock_width-start_index)
                    # read the next direction

            # read the next direction
            current_direction_index += 1

            # print('=== Before Rock Down ==\n' + '\n'.join([
            #     ''.join((
            #                 '.@'[current_rock_shape[y - examine_row_num][x - start_index]]
            #                 if examine_row_num <= y < len(current_rock_shape) + examine_row_num and
            #                    start_index <= x < len(current_rock_shape[y - examine_row_num]) + start_index
            #                 else '.#'[r]
            #             ) for x, r in enumerate(row)) for y, row in enumerate(base_floor)
            # ]) + '\n===')

            # check the next row of the floor
            if check_going_down(examine_row_num, current_rock_shape, base_floor, start_index):
                examine_row_num += 1
                # print('Moved Down')
            else:
                flag = False

        for h, row in enumerate(current_rock_shape):
            new_row = [0] * start_index + row + [0] * (7-current_rock_width-start_index)
            #base_floor.insert(examine_row_num + len(current_rock_shape), new_row)
            old_row = base_floor[examine_row_num + h]
            for i, new in enumerate(new_row):
                if new == 1:
                    old_row[i] = 1

        # check_delete = [False] * 7
        # for row_num, row in enumerate(reversed(base_floor[:-1])):
        #     if False not in check_delete:
        #         #print("before: ", len(base_floor))
        #         deleted_row_num += (row_num + 1)
        #         #print("number of rows deleted: ", row_num)
        #         base_floor = base_floor[:len(base_floor) - (row_num + 1)]
        #         base_floor.append([1]*7)
        #         #print("after: ", len(base_floor))
        #         # return
        #         break
        #     for i in range(7):
        #         if row[i] == 1:
        #             check_delete[i] = True


        # print('=== After Fill ==\n' + '\n'.join([''.join('.#'[y] for y in x) for x in base_floor]) + '\n===')

    # print(base_floor)
    print('===\n' + '\n'.join([''.join('.#'[y] for y in x) for x in base_floor]) + '\n===')

    for i, row in enumerate(base_floor):
        if 1 in row:
            return len(base_floor) - i - 1


    """
..#....
####...
..###..
...#...
####...
..##...
..##...
..#....
..#....
..#....
..#....
..#....
..#....
###....
.#.....
###....
.#####.
    """


if __name__ == "__main__":
    hot_air_push_list = read_push_directions("real_input.txt")
    print(part_1_tetris(hot_air_push_list))

    # IT"S BROKEN