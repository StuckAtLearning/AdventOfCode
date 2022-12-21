import ReadFileFunctions as RFF
import ast


def check_sides(input_file_path):
    input_file = RFF.read_file_with_new_line(input_file_path)
    input_file = [ast.literal_eval(i) for i in input_file]

    sides_dict = {key: [1]*6 for key in input_file}
    # list info = [n, s, w, e, front, back], 1 if it is open, 0 if it is covered
    for i in range(len(input_file)):
        for j in range(len(input_file)):
            if i == j:
                continue
            current_x, current_y, current_z = input_file[i]
            check_x, check_y, check_z = input_file[j]

            if (current_y == check_y) and (current_z == check_z):
                if current_x == check_x + 1:
                    sides_dict[input_file[i]][2] = 0
                    sides_dict[input_file[j]][3] = 0
                elif current_x + 1 == check_x:
                    sides_dict[input_file[i]][3] = 0
                    sides_dict[input_file[j]][2] = 0
            elif (current_x == check_x) and (current_z == check_z):
                if current_y + 1 == check_y:
                    sides_dict[input_file[i]][4] = 0
                    sides_dict[input_file[j]][5] = 0
                elif current_y == check_y + 1:
                    sides_dict[input_file[i]][5] = 0
                    sides_dict[input_file[j]][4] = 0
            elif (current_x == check_x) and (current_y == check_y):
                if current_z + 1 == check_z:
                    sides_dict[input_file[i]][0] = 0
                    sides_dict[input_file[j]][1] = 0
                elif current_z == check_z + 1:
                    sides_dict[input_file[i]][1] = 0
                    sides_dict[input_file[j]][0] = 0

    return sides_dict


def part_1(sides_dict):
    side_count = 0
    for sides in sides_dict.values():
        side_count += sides.count(1)

    return side_count


def part_2(input_file_path, output_file_path):
    output_file = open(output_file_path, "w")
    input_file = RFF.read_file_with_new_line(input_file_path)
    coords_list = [ast.literal_eval(i) for i in input_file]

    # get the dimensions
    coords_on_x = sorted(coords_list, key=lambda a: a[0])
    smallest_x = coords_on_x[0][0]
    largest_x = coords_on_x[-1][0]

    coords_on_y = sorted(coords_list, key=lambda a: a[1])
    smallest_y = coords_on_y[0][1]
    largest_y = coords_on_y[-1][1]

    coords_on_z = sorted(coords_list, key=lambda a: a[2])
    smallest_z = coords_on_z[0][2]
    largest_z = coords_on_z[-1][2]

    # box surface area (with one more width on each side as padding)
    box_outside_sa = (((largest_x-smallest_x + 1 + 2) * (largest_y-smallest_y + 1 + 2)) * 2) + \
                     (((largest_x-smallest_x + 1 + 2) * (largest_z-smallest_z + 1 + 2)) * 2) + \
                     (((largest_z-smallest_z + 1 + 2) * (largest_y-smallest_y + 1 + 2)) * 2)

    # build the box
    all_box_coords = list()
    for x in range(smallest_x-1, largest_x+2):
        for y in range(smallest_y-1, largest_y+2):
            for z in range(smallest_z-1, largest_z+2):
                all_box_coords.append((x, y, z))

    # get none overlapping coords
    remaining_box_coords = list()
    for box_coord in all_box_coords:
        if box_coord not in coords_list:
            remaining_box_coords.append(box_coord)

    # trace the cubes
    starting_piece = (smallest_x, smallest_y, smallest_z)
    connected_pieces = [starting_piece]
    connected_box_pieces = {starting_piece}
    output_file.write(str(starting_piece) + "\n")
    while connected_pieces:
        current_cube = connected_pieces.pop(0)
        for check_cube in remaining_box_coords:
            if (check_cube != current_cube) and (check_cube not in connected_box_pieces):
                if check_connection(current_cube, check_cube):
                    connected_pieces.append(check_cube)
                    connected_box_pieces.add(check_cube)
                    if not connected_pieces:
                        output_file.write(str(check_cube))
                    else:
                        output_file.write(str(check_cube) + "\n")

    output_file.close()
    return box_outside_sa


def check_connection(current_cube, check_cube):
    current_x, current_y, current_z = current_cube
    check_x, check_y, check_z = check_cube

    if (current_y == check_y) and (current_z == check_z):
        if current_x == check_x + 1:
            return True
        elif current_x + 1 == check_x:
            return True
    elif (current_x == check_x) and (current_z == check_z):
        if current_y + 1 == check_y:
            return True
        elif current_y == check_y + 1:
            return True
    elif (current_x == check_x) and (current_y == check_y):
        if current_z + 1 == check_z:
            return True
        elif current_z == check_z + 1:
            return True
    return False


if __name__ == "__main__":
    # # part 1 test
    # sides_info = check_sides("test_input.txt")
    # print(sides_info)
    # open_sides_num = part_1(sides_info)
    # print(open_sides_num)

    # # part 1
    # sides_info = check_sides("real_input.txt")
    # print(sides_info)
    # open_sides_num = part_1(sides_info)
    # print(open_sides_num)

    # part 2 test
    # box_surface_area = part_2("test_input.txt", "test_output.txt")
    # print(box_surface_area)
    # 210
    # sides_info = check_sides("test_output.txt")
    # open_sides_num = part_1(sides_info)
    # print(open_sides_num)
    # print("final answer: ", open_sides_num - 210)

    # part 2 test
    # box_surface_area = part_2("real_input.txt", "real_output.txt")
    # print(box_surface_area)
    # 2730
    sides_info = check_sides("real_output.txt")
    open_sides_num = part_1(sides_info)
    print(open_sides_num)
    print("final answer: ", open_sides_num - 2730)

