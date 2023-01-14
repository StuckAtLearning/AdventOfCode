import ReadFileFunctions as RFF


def parse_info(input_file_path: str) -> list[list[tuple[int, int]]]:
    input_file = RFF.read_file_with_new_line(input_file_path)
    input_list = list()
    for line in input_file:
        line = line.split(":")
        sensor_info = line[0].split(",")
        sensor_x = sensor_info[0].split("=")[1]
        sensor_y = sensor_info[1].split("=")[1]

        beacon_info = line[1].split(",")
        beacon_x = beacon_info[0].split("=")[1]
        beacon_y = beacon_info[1].split("=")[1]

        input_list.append([(int(sensor_x), int(sensor_y)), (int(beacon_x), int(beacon_y))])

    return input_list


def get_signal_relations(input_list: list[list[tuple[int, int]]]) -> dict[tuple[int, int], list[tuple[int, int]]]:
    signal_info_dict = dict()
    beacon_seen = set()
    for signal_info in input_list:
        sensor_info = signal_info[0]
        beacon_info = signal_info[1]
        if beacon_info not in beacon_seen:
            beacon_seen.add(beacon_info)
            signal_info_dict[beacon_info] = [sensor_info]
        else:
            signal_info_dict[beacon_info].append(sensor_info)

    return signal_info_dict


def find_width(input_list: list[list[tuple[int, int]]]) -> :
    width_start = int()
    width_end = int()
    for signal_info in input_list:
        sensor_x = signal_info[0][0]
        beacon_x = signal_info[1][0]
        width_start = min(width_start, sensor_x, beacon_x)
        width_end = max(width_end, sensor_x, beacon_x)

    return width_start, width_end


def get_sensor_beacon_distance(signal_info_dict):
    distance_info_list = list()
    for beacon_info, sensor_info in signal_info_dict.items():
        for each_sensor_coord in sensor_info:
            sensor_x, sensor_y = each_sensor_coord[0], each_sensor_coord[1]
            beacon_x, beacon_y = beacon_info[0], beacon_info[1]
            distance = abs(sensor_x-beacon_x) + abs(sensor_y-beacon_y)
            distance_info = (sensor_x, sensor_y, distance)
            distance_info_list.append(distance_info)

    return distance_info_list


def find_distress_signal(distance_info_list, signal_dict, left_boundary, right_boundary, check_y_coord):
    count = 0
    beacon_positions = signal_dict.keys()
    for i in range(left_boundary-4_000_000, right_boundary+4_000_000):
        check_x, check_y = i, check_y_coord
        if (check_x, check_y) not in beacon_positions:
            flag = False
            for x, y, distance in distance_info_list:
                check_distance = abs(check_x-x) + abs(check_y-y)
                if check_distance <= distance:
                    flag = True
            if flag:
                count += 1
        if i % 1_000_000 == 0:
            print(count)
    return count


def find_possible_beacon(signal_info_list, left_boundary, right_boundary):
    for y in range(left_boundary, right_boundary+1):
        check_list = list()
        for signal_info in signal_info_list:
            sensor_info = signal_info[0]
            beacon_info = signal_info[1]
            sensor_x, sensor_y = sensor_info
            beacon_x, beacon_y = beacon_info
            beacon_sensor_distance = abs(sensor_x-beacon_x) + abs(sensor_y-beacon_y)

            sensor_current_y_distance = abs(sensor_y - y)
            reachable_distance = beacon_sensor_distance - sensor_current_y_distance
            if reachable_distance < 0:
                continue
            reach_left = sensor_x-reachable_distance if sensor_x-reachable_distance > left_boundary else left_boundary
            reach_right = sensor_x+reachable_distance if sensor_x+reachable_distance < right_boundary else right_boundary

            check_list.append((reach_left, reach_right))

        check_list = sorted(check_list, key=lambda x: x[0])
        # print(check_list)
        right_range = check_list[0][1]
        for each_range in check_list[1:]:
            next_left_range = each_range[0]
            next_right_range = each_range[1]
            # print('jujuju', right_range, next_left_range, next_right_range)
            if right_range < next_left_range and right_range < next_right_range:
                return right_range+1, y
            right_range = max(next_right_range, right_range)


if __name__ == "__main__":
    # test part 1:
    # input_info = parse_info("advanced_test_input.txt.txt")
    # signal_dict = get_signal_relations(input_info)
    # left_bound, right_bound = find_width(input_info)
    # distance_info = get_sensor_beacon_distance(signal_dict)
    # count_distress_signal = find_distress_signal(distance_info, signal_dict, left_bound, right_bound, 10)
    # print(count_distress_signal)

    # part 1:
    # 4204324
    # 4204334
    # input_info = parse_info("real_input.txt")
    # signal_dict = get_signal_relations(input_info)
    # left_bound, right_bound = find_width(input_info)
    # print(left_bound, right_bound)
    # distance_info = get_sensor_beacon_distance(signal_dict)
    # count_distress_signal = find_distress_signal(distance_info, signal_dict, left_bound, right_bound, 2000000)
    # print(count_distress_signal)

    # part 2 test:
    input_info = parse_info("test_input.txt")
    test_answer = find_possible_beacon(input_info, 0, 20)
    print(test_answer, test_answer[0]*4000000 + test_answer[1])

    input_info = parse_info("real_input.txt")
    real_answer = find_possible_beacon(input_info, 0, 4_000_000)
    print(real_answer, real_answer[0]*4000000 + real_answer[1])
