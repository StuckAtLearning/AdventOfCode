import ReadFileFunctions as RFF
import functools
import math


def blue_print_passer(blue_print_dict):

    max_ore_needed = max(blue_print_dict["ore"], blue_print_dict["clay"], blue_print_dict["obs"][0], blue_print_dict["geo"][0])
    max_clay_needed = blue_print_dict["obs"][1]
    max_obs_needed = blue_print_dict["geo"][1]

    @functools.lru_cache(None)
    def calculate_geodes(time_spent, ore_bot_num, ore_num, can_afford_ore_last_round, clay_bot_num, clay_num,
                         can_afford_clay_last_round, obs_bot_num, obs_num, can_afford_obs_last_round, geo_bot_num,
                         can_afford_geo_last_round):

        # # part 2 only
        if time_spent >= 32 - 1:
            return geo_bot_num

        # # part 1 only:
        # if time_spent >= 24:
        #     return 0

        possible_steps = [0]

        can_build_geo_bot = bool((ore_num >= blue_print_dict["geo"][0]) and (obs_num >= blue_print_dict["geo"][1]))
        can_build_obs_bot = bool(ore_num >= blue_print_dict["obs"][0] and clay_num >= blue_print_dict["obs"][1])
        can_build_ore_bot = bool(ore_num >= blue_print_dict["ore"])
        can_build_clay_bot = bool(ore_num >= blue_print_dict["clay"])

        allow_build_ore_bot = bool((ore_num >= max_ore_needed) and (ore_bot_num >= max_ore_needed))
        allow_build_clay_bot = bool((clay_num >= max_clay_needed) and (clay_bot_num >= max_clay_needed))
        allow_build_obs_bot = bool((obs_num >= max_obs_needed) and (obs_bot_num >= max_obs_needed))

        if allow_build_ore_bot:
            ore_num = max_ore_needed
            ore_bot_num = max_ore_needed
        if allow_build_clay_bot:
            clay_num = max_clay_needed
            clay_bot_num = max_clay_needed
        if allow_build_obs_bot:
            obs_num = max_obs_needed
            obs_bot_num = max_obs_needed

        # if I can afford this round, and I didn't make it, then I should not make it next round either?
        # so then what happens next round?

        if can_build_geo_bot and (not can_afford_geo_last_round):
            possible_next_step = calculate_geodes(time_spent + 1,
                                                  ore_bot_num, ore_bot_num + ore_num - blue_print_dict["geo"][0],
                                                  False,
                                                  clay_bot_num, clay_bot_num + clay_num,
                                                  False,
                                                  obs_bot_num, obs_bot_num + obs_num - blue_print_dict["geo"][1],
                                                  False,
                                                  geo_bot_num + 1,
                                                  False) + geo_bot_num
            possible_steps.append(possible_next_step)

        if can_build_obs_bot and (not allow_build_obs_bot) and (not can_afford_obs_last_round):
            possible_next_step = calculate_geodes(time_spent + 1,
                                                  ore_bot_num, ore_bot_num + ore_num - blue_print_dict["obs"][0],
                                                  False,
                                                  clay_bot_num, clay_bot_num + clay_num - blue_print_dict["obs"][1],
                                                  False,
                                                  obs_bot_num + 1, obs_bot_num + obs_num,
                                                  False,
                                                  geo_bot_num,
                                                  False) + geo_bot_num
            possible_steps.append(possible_next_step)

        if can_build_ore_bot and (not allow_build_ore_bot) and (not can_afford_ore_last_round):
            possible_next_step = calculate_geodes(time_spent + 1,
                                                  ore_bot_num + 1, ore_bot_num + ore_num - blue_print_dict["ore"],
                                                  False,
                                                  clay_bot_num, clay_bot_num + clay_num,
                                                  False,
                                                  obs_bot_num, obs_bot_num + obs_num,
                                                  False,
                                                  geo_bot_num,
                                                  False) + geo_bot_num
            possible_steps.append(possible_next_step)

        if can_build_clay_bot and (not allow_build_clay_bot) and (not can_afford_clay_last_round):
            possible_next_step = calculate_geodes(time_spent + 1,
                                                  ore_bot_num, ore_bot_num + ore_num - blue_print_dict["clay"],
                                                  False,
                                                  clay_bot_num + 1, clay_bot_num + clay_num,
                                                  False,
                                                  obs_bot_num, obs_bot_num + obs_num,
                                                  False,
                                                  geo_bot_num,
                                                  False) + geo_bot_num
            possible_steps.append(possible_next_step)

        if (not can_build_ore_bot) or (not can_build_clay_bot) or (not can_build_obs_bot) or (not can_build_geo_bot):
            possible_next_step = calculate_geodes(time_spent + 1,
                                                  ore_bot_num, ore_bot_num + ore_num, can_build_ore_bot,
                                                  clay_bot_num, clay_bot_num + clay_num, can_build_clay_bot,
                                                  obs_bot_num, obs_bot_num + obs_num, can_build_obs_bot,
                                                  geo_bot_num, can_build_geo_bot) + geo_bot_num
            possible_steps.append(possible_next_step)

        return max(possible_steps)

    return calculate_geodes(0, 1, 0, False, 0, 0, False, 0, 0, False, 0, False)


def part_1(input_dict: dict):
    total_quality_level = list()
    for blue_print_num, blue_print_info in input_dict.items():
        # part 2 only:
        if blue_print_num == 4:
            break

        geodes_count = blue_print_passer(blue_print_info)
        print(blue_print_num, geodes_count)

        # # part 1 only:
        # quality_level = geodes_count * blue_print_num
        # total_quality_level.append(quality_level)

        # part 2 only:
        total_quality_level.append(geodes_count)

    # # part 1 only:
    # return sum(total_quality_level)

    # part 2 only:
    return math.prod(total_quality_level)


def convert_file_to_dict(input_file_path):
    input_file = RFF.read_file_with_new_line(input_file_path)

    info_dict = dict()
    for line in input_file:
        blue_print_num_info = line.split(":")[0]
        blue_print_num = int(blue_print_num_info.split(" ")[-1])

        bot_info = line.split(":")[1]
        each_bot_info = bot_info.split(".")
        ore_bot_info = int(each_bot_info[0].split(" ")[5])
        clay_bot_info = int(each_bot_info[1].split(" ")[5])
        obsidian_bot_info = (int(each_bot_info[2].split(" ")[5]), int(each_bot_info[2].split(" ")[8]))
        geo_bot_info = (int(each_bot_info[3].split(" ")[5]), int(each_bot_info[3].split(" ")[8]))

        info_dict[int(blue_print_num)] = {"ore": ore_bot_info, "clay": clay_bot_info, "obs": obsidian_bot_info,
                                          "geo": geo_bot_info}

    return info_dict


if __name__ == "__main__":
    # # part 1 test
    # input_info_dict = convert_file_to_dict("test_input.txt")
    # print(input_info_dict)
    # part_1_test_answer = part_1(input_info_dict)
    # print(part_1_test_answer)

    # part 1
    # input_info_dict = convert_file_to_dict("real_input.txt")
    # print(input_info_dict)
    # part_1_test_answer = part_1(input_info_dict)
    # print(part_1_test_answer)

    # # part 2 test
    # input_info_dict = convert_file_to_dict("test_input.txt")
    # print(input_info_dict)
    # part_1_test_answer = part_1(input_info_dict)
    # print(part_1_test_answer)

    # part 2
    input_info_dict = convert_file_to_dict("real_input.txt")
    print(input_info_dict)
    part_1_test_answer = part_1(input_info_dict)
    print(part_1_test_answer)

