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



if __name__ == "__main__":
    # part 1 test
    # sides_info = check_sides("test_input.txt")
    # print(sides_info)
    # open_sides_num = part_1(sides_info)
    # print(open_sides_num)

    # part 1
    sides_info = check_sides("real_input.txt")
    print(sides_info)
    open_sides_num = part_1(sides_info)
    print(open_sides_num)