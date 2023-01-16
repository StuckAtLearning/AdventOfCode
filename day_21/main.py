import ReadFileFunctions as RFF


def parse_input(input_file_path: str) -> tuple[dict[str, int | list[str]], list[str]]:
    monkey_dict = dict()
    monkey_appearance = list()
    input_file = RFF.read_file_with_new_line(input_file_path)
    input_file = [i.split(":") for i in input_file]

    for monkey_math in input_file:
        monkey_name = monkey_math[0]
        monkey_appearance.append(monkey_name)
        monkey_instruction = monkey_math[1].strip(" ")
        if " " not in monkey_instruction:
            monkey_instruction = int(monkey_instruction)
        else:
            monkey_instruction = monkey_instruction.split(" ")
        monkey_dict[monkey_name] = monkey_instruction

    return monkey_dict, monkey_appearance


def part_1(current_monkey: str, monkey_dict: dict[str, int | list[str]], num_monkeys: list[str]) -> int | list[str]:
    if current_monkey in num_monkeys:
        return monkey_dict[current_monkey]

    print(monkey_dict[current_monkey][0])
    left_monkey = monkey_dict[current_monkey][0]
    monkey_operation = monkey_dict[current_monkey][1]
    right_monkey = monkey_dict[current_monkey][2]
    if monkey_operation == "+":
        return part_1(left_monkey, monkey_dict, num_monkeys) + part_1(right_monkey, monkey_dict, num_monkeys)
    elif monkey_operation == "-":
        return part_1(left_monkey, monkey_dict, num_monkeys) - part_1(right_monkey, monkey_dict, num_monkeys)
    elif monkey_operation == "*":
        return part_1(left_monkey, monkey_dict, num_monkeys) * part_1(right_monkey, monkey_dict, num_monkeys)
    elif monkey_operation == "/":
        return part_1(left_monkey, monkey_dict, num_monkeys) // part_1(right_monkey, monkey_dict, num_monkeys)


def get_num_monkeys(monkey_dict: dict[str, int | list[str]]) -> list[str]:
    num_monkeys = list()
    for monkey, monkey_instruction in monkey_dict.items():
        if isinstance(monkey_instruction, int):
            num_monkeys.append(monkey)

    return num_monkeys


def part_2_correction(monkey_dict: dict[str, int | list[str]], num_monkeys: list[str]) -> \
        tuple[dict[str, int | list[str]], list[str]]:
    monkey_dict["root"][1] = "="
    monkey_dict["humn"] = 3_296_135_418_820

    return monkey_dict, num_monkeys



if __name__ == "__main__":
    # # part 1 test:
    # all_monkey_info_dict, monkey_names_order = parse_input("test_input.txt")
    # number_only_monkeys = get_num_monkeys(all_monkey_info_dict)
    # root_monkey_number = part_1("root", all_monkey_info_dict, number_only_monkeys)
    # print(all_monkey_info_dict, monkey_names_order)
    # print(root_monkey_number)

    # # part 1
    # all_monkey_info_dict, monkey_names_order = parse_input("real_input.txt")
    # number_only_monkeys = get_num_monkeys(all_monkey_info_dict)
    # root_monkey_number = part_1("root", all_monkey_info_dict, number_only_monkeys)
    # print(all_monkey_info_dict, monkey_names_order)
    # print(root_monkey_number)

    # # part 2 test
    # all_monkey_info_dict, monkey_names_order = parse_input("test_input.txt")
    # number_only_monkeys = get_num_monkeys(all_monkey_info_dict)
    # root_left = all_monkey_info_dict["root"][0]
    # root_right = all_monkey_info_dict["root"][2]
    #
    # all_monkey_info_dict, number_only_monkeys = part_2_correction(all_monkey_info_dict, number_only_monkeys)
    # print(all_monkey_info_dict, number_only_monkeys)
    # root_left_number = part_1(root_left, all_monkey_info_dict, number_only_monkeys)
    # root_right_number = part_1(root_right, all_monkey_info_dict, number_only_monkeys)
    # print(root_right_number, root_left_number)

    # part 2
    all_monkey_info_dict, monkey_names_order = parse_input("real_input.txt")
    number_only_monkeys = get_num_monkeys(all_monkey_info_dict)
    root_left = all_monkey_info_dict["root"][0]
    root_right = all_monkey_info_dict["root"][2]

    all_monkey_info_dict, number_only_monkeys = part_2_correction(all_monkey_info_dict, number_only_monkeys)
    print(all_monkey_info_dict, number_only_monkeys)
    root_left_number = part_1(root_left, all_monkey_info_dict, number_only_monkeys)
    root_right_number = part_1(root_right, all_monkey_info_dict, number_only_monkeys)
    print(root_right_number, root_left_number)