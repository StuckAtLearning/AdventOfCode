import ReadFileFunctions as RFF
import ast


def part_1(input_file_path):
    input_file = RFF.read_file_with_new_line(input_file_path)
    rock_list = list()
    for line in input_file:
        line = [ast.literal_eval(point.strip(" ")) for point in line.split("->")]
        rock_list.append(line)

    # fill in the rock:
    filled_rock_map = set()
    for rock_blue_print in rock_list:
        for i in range(len(rock_blue_print)-1):
            x, y = rock_blue_print[i]
            next_x, next_y = rock_blue_print[i+1]
            if x == next_x:
                fill_rocks = [(x, y+i) for i in range(next_y - y)] if next_y - y > 0 else [(x, y-i) for i in range(y - next_y)]
                for rock in fill_rocks:
                    filled_rock_map.add(rock)
            elif y == next_y:
                fill_rocks = [(x+j, y) for j in range(next_x - x)] if next_x - x > 0 else [(x-j, y) for j in range(x - next_x)]
                for rock in fill_rocks:
                    filled_rock_map.add(rock)
            else:
                print("not connected rock points?")
        filled_rock_map.add(rock_blue_print[-1])

    bottom = max(filled_rock_map, key=lambda a: a[1])[1]
    part_2_bottom = bottom + 2
    left_edge = min(filled_rock_map, key=lambda l: l[0])[0]
    super_left_edge = 500 - part_2_bottom - 9
    right_edge = max(filled_rock_map, key=lambda r: r[0])[0]
    super_right_edge = 500 + part_2_bottom + 9
    for i in range(super_left_edge, super_right_edge):
        filled_rock_map.add((i, part_2_bottom))

    sand_source = (500, 0)
    sand_journey = (500, 0)
    sand_count = 0

    # part 1
    # while (sand_journey[1] <= bottom) and (sand_journey[1] >= 0) and (sand_journey[0] >= left_edge) and (sand_journey[0] <= right_edge):
    #     x, y = sand_journey
    #     print(sand_journey)
    #     if (x, y+1) not in filled_rock_map:
    #         sand_journey = (x, y+1)
    #     elif (x, y+1) in filled_rock_map:
    #         if (x-1, y+1) not in filled_rock_map:
    #             sand_journey = (x-1, y+1)
    #         elif (x+1, y+1) not in filled_rock_map:
    #             sand_journey = (x+1, y+1)
    #         else:
    #             filled_rock_map.add(sand_journey)
    #             sand_journey = sand_source
    #             sand_count += 1

    # part 2
    while (sand_journey[1] <= part_2_bottom) and (sand_journey[0] >= super_left_edge) and (sand_journey[0] <= super_right_edge):
        x, y = sand_journey
        #print(sand_journey)
        if (x, y+1) not in filled_rock_map:
            sand_journey = (x, y+1)
        elif (x, y+1) in filled_rock_map:
            if (x-1, y+1) not in filled_rock_map:
                sand_journey = (x-1, y+1)
            elif (x+1, y+1) not in filled_rock_map:
                sand_journey = (x+1, y+1)
            else:
                if sand_journey == (500, 0):
                    return sand_count + 1
                filled_rock_map.add(sand_journey)
                sand_journey = sand_source
                sand_count += 1

    # part 1
    # return sand_count


if __name__ == "__main__":
    # part_1_test_answer = part_1("test_input.txt")
    # print(part_1_test_answer)
    #
    # part_1_answer = part_1("real_input.txt")
    # print(part_1_answer)

    part_2_test_answer = part_1("test_input.txt")
    print(part_2_test_answer)

    part_2_answer = part_1("real_input.txt")
    print(part_2_answer)