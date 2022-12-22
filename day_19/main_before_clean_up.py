import ReadFileFunctions as RFF


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

        info_dict[int(blue_print_num)] = {"ore": ore_bot_info, "clay": clay_bot_info, "obsidian": obsidian_bot_info, "geo": geo_bot_info}

    return info_dict


if __name__ == "__main__":
    input_info_dict = convert_file_to_dict("test_input.txt")
    print(input_info_dict)