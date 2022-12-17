import ReadFileFunctions as RFF
import copy
import ast
import itertools
import functools


def parse_file_to_dict(file_path):
    input_file = RFF.read_file_with_new_line(file_path)
    valve_dict = dict()

    for line in input_file:
        valve_rate_info = line.split(";")[0]
        valve_rate = int(valve_rate_info.split("=")[-1])
        valve_name = line.split(" ")[1]
        valve_tunnels_info = line.split(",")
        valve_tunnels_info[0] = valve_tunnels_info[0][-2:]
        valve_tunnels = list()
        for valve in valve_tunnels_info:
            valve = valve.strip(" ")
            valve_tunnels.append(valve)
        valve_dict[valve_name] = [valve_rate, valve_tunnels]

    return valve_dict


def calculate_distance(starting_valve, destination_valve, valve_info_dict, seen_valve):
    next_valves = valve_info_dict[starting_valve][1]
    if destination_valve in next_valves:
        return 1
    valve_dis = 999999999
    for valve in next_valves:
        if valve not in seen_valve:
            # because fuck this
            fuck_this = set(seen_valve)
            fuck_this.add(valve)
            valve_dis = min(valve_dis, calculate_distance(valve, destination_valve, valve_info_dict, fuck_this) + 1)
    return valve_dis


def build_paths(valve_info_dict):
    paths = dict()
    all_valves = valve_info_dict.keys()
    for valve, info in valve_info_dict.items():
        path = dict()
        for destination in all_valves:
            if (destination != valve) and (valve_info_dict[destination][0] != 0):
                path[destination] = calculate_distance(valve, destination, valve_info_dict, set())
        paths[valve] = path
    return paths


def get_all_pressures(time_left):
    all_pressures = dict()
    for valve, paths in all_paths.items():
        pressure_info = dict()
        for next_valve, time in paths.items():
            if time_left-time-1 <= 0:
                pressure = 0
            else:
                pressure = (time_left-time-1) * valve_dict[next_valve][0]
            pressure_info[next_valve] = pressure

        all_pressures[valve] = pressure_info
    return all_pressures


@functools.lru_cache(None)
def get_most_pressures(opened_valves, starting_valve, current_time):
    if current_time >= 30:
        return 0
    max_pressure = 0
    paths_info = all_paths[starting_valve]
    for next_valve, time_needed in paths_info.items():
        if current_time + time_needed + 1 <= 30:
            if next_valve not in opened_valves:
                next_open_valves = set(opened_valves)
                next_open_valves.add(next_valve)
                pressure_will_get = (30-current_time-time_needed-1) * valve_dict[next_valve][0]
                next_pressure = get_most_pressures(frozenset(next_open_valves), next_valve, current_time+time_needed+1) + pressure_will_get
                max_pressure = max(max_pressure, next_pressure)
    return max_pressure


# def get_combinations(iterable, num_of_elements):
#     if num_of_elements == 0:
#         return [[]]
#     combination = []
#     for i in range(0, len(iterable)):
#         mine = iterable[i]
#         rest = iterable[:i] + iterable[i+1:]
#
#         rest_combination = get_combinations(rest, num_of_elements - 1)
#         for r in rest_combination:
#             combination.append([mine]+r)
#         return combination


def divide_work():
    all_valves = list(all_paths.keys())
    # I don't know if this is going to work:
    non_zero_valves = [v for v in all_valves if valve_dict[v][0] != 0]
    # it worked lol
    total_paths_num = len(non_zero_valves)
    # max > 2344
    max_pressure = 0
    for i in range(1, total_paths_num):
        # starting dividing work
        my_assignment = itertools.combinations(non_zero_valves, i)
        # my_assignment = combinations(all_valves, i)
        for count, ass in enumerate(my_assignment):
            my_valves = set(ass)
            elephant_valves = set(set(non_zero_valves) - my_valves)

            my_pressure = get_most_pressures(frozenset(elephant_valves), "AA", 4)
            elephant_pressure = get_most_pressures(frozenset(my_valves), "AA", 4)

            max_pressure = max(max_pressure, my_pressure + elephant_pressure)
            if count % 10 == 0:
                print(ass)
                print(max_pressure)

    return max_pressure


def dp():
    all_valves = set(valve_dict.keys())
    my_ass = divide_work()
    dp = dict()
    for ass in my_ass:
        if len(ass) == 1:
            my_valves = set(ass)
            print(my_valves)
            elephant_valves = set(all_valves - my_valves)
            dp[ass] = get_most_pressures(elephant_valves, "AA", 4)
            my_ass.remove(ass)

    # for ass in my_ass:
    #     my_valves = set(ass)
    #     dp[ass] = dp[] + get_most_pressures(all_paths, valve_info_dict, my_valves-, "AA", 4)

    return dp


# def part_2():
#     all_valves = set(valve_info_dict.keys())
#     print("before dividing work")
#     my_ass = divide_work()
#     max_pressure = 0
#     for i, ass in enumerate(my_ass):
#         my_valves = set(ass)
#         elephant_valves = set(all_valves - my_valves)
#
#         print("where???")
#         my_pressure = get_most_pressures(frozenset(elephant_valves), "AA", 4)
#         elephant_pressure = get_most_pressures(frozenset(my_valves), "AA", 4)
#
#         max_pressure = max(max_pressure, my_pressure + elephant_pressure)
#         if my_pressure == my_pressure + elephant_pressure:
#             print(max_pressure)
#             print("in my ass: ", i / len(my_ass))
#
#     return max_pressure


if __name__ == "__main__":
    # part 1 test:
    # valve_info = parse_file_to_dict("test_input.txt")
    # print(valve_info)
    # distance_paths_dict = build_paths(valve_info)
    # print(distance_paths_dict)
    # # pressures_dict = get_all_pressures(distance_paths_dict, valve_info, 30)
    # # print(pressures_dict)
    # print(get_most_pressures(distance_paths_dict, valve_info, set(), "AA", 0))

    # part 1:
    # valve_info = parse_file_to_dict("real_input.txt")
    # print(valve_info)
    # distance_paths_dict = build_paths(valve_info)
    # print(distance_paths_dict)
    # # pressures_dict = get_all_pressures(distance_paths_dict, valve_info, 30)
    # # print(pressures_dict)
    # print(get_most_pressures(distance_paths_dict, valve_info, set(), "AA", 0))

    # part 2 test:
    # valve_info = parse_file_to_dict("test_input.txt")
    # print(valve_info)
    # distance_paths_dict = build_paths(valve_info)
    # print(distance_paths_dict)
    # print(part_2(distance_paths_dict, valve_info))

    # part 2:
    valve_info = parse_file_to_dict("real_input.txt")
    distance_paths_dict = build_paths(valve_info)
    all_paths = distance_paths_dict
    valve_dict = valve_info
    print(divide_work())

