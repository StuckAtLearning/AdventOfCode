import ReadFileFunctions as RFF


def move_coord(current_coord, check_coord):
    # both coordinates in the format of [x, y]
    # return current_coord is on the _ side of check_coord
    move_coord = [0, 0]
    if current_coord[0] - check_coord[0] > 0:
        move_coord[0] -= 1
    if current_coord[0] - check_coord[0] < 0:
        move_coord[0] += 1
    if current_coord[1] - check_coord[1] > 0:
        move_coord[1] -= 1
    if current_coord[1] - check_coord[1] < 0:
        move_coord[1] += 1
    return (current_coord[0]+move_coord[0], current_coord[1]+move_coord[1])


def check_neighbours(current_coord, check_coord):
    if (abs(current_coord[0] - check_coord[0]) < 2) and (abs(current_coord[1] - check_coord[1]) < 2):
        return True
    return False


    # if (current_coord[0] == check_coord[0]) and (current_coord[1] == (check_coord[1]-2)):
    #     return (current_coord[0], current_coord[1] + 1)
    # elif (current_coord[0] == check_coord[0]) and (current_coord[1] == (check_coord[1]+2)):
    #     return (current_coord[0], current_coord[1] - 1)
    # elif (current_coord[0] == (check_coord[0]-2)) and (current_coord[1] == check_coord[1]):
    #     return (current_coord[0] + 1, current_coord[1])
    # elif (current_coord[0] == (check_coord[0]+2)) and (current_coord[1] == check_coord[1]):
    #     return (current_coord[0] - 1, current_coord[1])
    #
    # elif (current_coord[0] == (check_coord[0]+1)) and (current_coord[1] == (check_coord[1]+1)):
    #     return current_coord #(current_coord[0] - 1, current_coord[1] - 1)
    # elif (current_coord[0] == (check_coord[0]+1)) and (current_coord[1] == (check_coord[1]-1)):
    #     return current_coord #(current_coord[0] - 1, current_coord[1] + 1)
    # elif (current_coord[0] == (check_coord[0]-1)) and (current_coord[1] == (check_coord[1]+1)):
    #     return current_coord #(current_coord[0] + 1, current_coord[1] - 1)
    # elif (current_coord[0] == (check_coord[0]-1)) and (current_coord[1] == (check_coord[1]-1)):
    #     return current_coord #(current_coord[0] + 1, current_coord[1] + 1)
    # return current_coord

    # elif (current_coord[0] == (check_coord[0] + 1)) and (current_coord[1] == (check_coord[1] + 1)):
    #     return (current_coord[0]-1, current_coord[1]-1), "north-east"
    # elif (current_coord[0] == (check_coord[0] + 1)) and (current_coord[1] == (check_coord[1] - 1)):
    #     return (current_coord[0]-1, current_coord[1]+1), "south-east"
    # elif (current_coord[0] == (check_coord[0] - 1)) and (current_coord[1] == (check_coord[1] + 1)):
    #     return (current_coord[0]+1, current_coord[1]-1), "north-west"
    # elif (current_coord[0] == (check_coord[0] - 1)) and (current_coord[1] == (check_coord[1] - 2)):
    #     return (current_coord[0]+1, current_coord[1]+1), "south-west"
    #
    # else:
    #     return (0, 0), "none"


def part_1(test_input_file):
    test_input = RFF.read_file_with_new_line(test_input_file)
    point_visited = set()
    starting_point = (0, 0)
    H_coord = starting_point
    T_coord = starting_point

    point_visited.add(starting_point)

    for move in test_input:
        direction = move.split(" ")[0]
        step_num = int(move.split(" ")[1])

        if direction == "R":
            for i in range(step_num):
                H_coord = (H_coord[0]+1, H_coord[1])
                if not check_neighbours(T_coord, H_coord):
                    T_coord = move_coord(T_coord, H_coord)
                print(H_coord, T_coord)
                point_visited.add(T_coord)

        elif direction == "L":
            for i in range(step_num):
                H_coord = (H_coord[0]-1, H_coord[1])
                if not check_neighbours(T_coord, H_coord):
                    T_coord = move_coord(T_coord, H_coord)
                print(H_coord, T_coord)
                point_visited.add(T_coord)

        elif direction == "U":
            for i in range(step_num):
                H_coord = (H_coord[0], H_coord[1]+1)
                if not check_neighbours(T_coord, H_coord):
                    T_coord = move_coord(T_coord, H_coord)
                print(H_coord, T_coord)
                point_visited.add(T_coord)

        else:
            for i in range(step_num):
                H_coord = (H_coord[0], H_coord[1]-1)
                if not check_neighbours(T_coord, H_coord):
                    T_coord = move_coord(T_coord, H_coord)
                print(H_coord, T_coord)
                point_visited.add(T_coord)

    return len(point_visited)


def part_2(test_input_file):
    test_input = RFF.read_file_with_new_line(test_input_file)
    point_visited = set()
    starting_point = (0, 0)
    H_coord = starting_point
    mid_coords = [(0, 0)] * 9
    T_coord = starting_point

    point_visited.add(starting_point)

    for move in test_input:
        direction = move.split(" ")[0]
        step_num = int(move.split(" ")[1])

        if direction == "R":
            for i in range(step_num):
                H_coord = (H_coord[0] + 1, H_coord[1])
                temp_H_coord = H_coord
                for j in range(9):
                    if not check_neighbours(mid_coords[j], temp_H_coord):
                        mid_coords[j] = move_coord(mid_coords[j], temp_H_coord)
                    temp_H_coord = mid_coords[j]
                    # print(mid_coords)
                point_visited.add(mid_coords[-1])

        elif direction == "L":
            for i in range(step_num):
                H_coord = (H_coord[0]-1, H_coord[1])
                temp_H_coord = H_coord
                for j in range(9):
                    if not check_neighbours(mid_coords[j], temp_H_coord):
                        mid_coords[j] = move_coord(mid_coords[j], temp_H_coord)
                    temp_H_coord = mid_coords[j]
                    # print(mid_coords)
                point_visited.add(mid_coords[-1])

        elif direction == "U":
            for i in range(step_num):
                H_coord = (H_coord[0], H_coord[1]+1)
                temp_H_coord = H_coord
                for j in range(9):
                    if not check_neighbours(mid_coords[j], temp_H_coord):
                        mid_coords[j] = move_coord(mid_coords[j], temp_H_coord)
                    temp_H_coord = mid_coords[j]
                    # print(mid_coords)
                point_visited.add(mid_coords[-1])

        else:
            for i in range(step_num):
                H_coord = (H_coord[0], H_coord[1]-1)
                temp_H_coord = H_coord
                for j in range(9):
                    if not check_neighbours(mid_coords[j], temp_H_coord):
                        mid_coords[j] = move_coord(mid_coords[j], temp_H_coord)
                    temp_H_coord = mid_coords[j]
                    # print(mid_coords)
                point_visited.add(mid_coords[-1])

    return len(point_visited)


if __name__ == "__main__":
    # print(part_1("test_input.txt"))
    # print(part_1("real_input.txt"))

    print(part_2("test_input.txt"))
    print(part_2("part_2_test_input.txt"))
    print(part_2("real_input.txt"))