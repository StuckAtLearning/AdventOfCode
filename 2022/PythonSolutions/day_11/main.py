import ReadFileFunctions as RFF


def part_1(test_input_file_path: str) -> int:
    test_input = RFF.read_file_double_new_line(test_input_file_path)
    monkey_info = dict()
    for monkey in test_input:
        monkey_id = int(monkey[0][-2])
        monkey_items = [int(i) for i in (monkey[1].split(":")[-1]).split(",")]
        monkey_op = ("*" if monkey[2].split("=")[-1][5] == "*" else "+", "old" if monkey[2].split(" ")[-1] == "old" else int(monkey[2].split(" ")[-1]))
        monkey_test = int(monkey[3].split(" ")[-1])
        monkey_true = int(monkey[4].split(" ")[-1])
        monkey_false = int(monkey[5].split(" ")[-1])
        monkey_info[monkey_id] = {"items": monkey_items, "op": monkey_op, "test": monkey_test, "true": monkey_true, "false": monkey_false, "inspection_num": 0}

    # Part 1 only:
    # for each_round in range(20):
    for each_round in range(10000):
        # for one_monkey in all monkeys
        for monkey_id, info in monkey_info.items():
            # for one item in all items one monkey has
            while info["items"]:
                item = info["items"].pop(0)
                # the monkey does the operation
                if info["op"][0] == "*":
                    if isinstance(info["op"][1], int):
                        new = item * info["op"][1]
                    else:
                        new = item * item
                else:
                    if isinstance(info["op"][1], int):
                        new = item + info["op"][1]
                    else:
                        new = item + item
                # Part 1 only: divide the worry level by 3
                # new = new // 3

                # if true, goes to that monkey's end of list
                if new % info["test"] == 0:
                    next_monkey_id = info["true"]
                # if false, goes to that monkey's end of list
                else:
                    next_monkey_id = info["false"]
                # monkey_info[next_monkey_id]["items"].append(new % 96577)
                monkey_info[next_monkey_id]["items"].append(new % 9699690)

                # add one to the inspection_num
                monkey_info[monkey_id]["inspection_num"] += 1

    # multiply the highest two inspection_num
    sorted_inspection_num = sorted([monkey_info[key]["inspection_num"] for key in monkey_info.keys()])
    monkey_business = sorted_inspection_num[-1] * sorted_inspection_num[-2]

    return monkey_business


if __name__ == "__main__":
    # test_answer = part_1("advanced_test_input.txt.txt")
    # print(test_answer)

    # part_1_answer = part_1("real_input.txt")
    # print(part_1_answer)

    # part_2_answer = part_1("advanced_test_input.txt.txt")
    # print(part_2_answer)

    part_2_answer = part_1("real_input.txt")
    print(part_2_answer)
