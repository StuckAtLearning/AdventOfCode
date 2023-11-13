import ReadFileFunctions as RFF


def part_1(test_input_file_path: str) -> int:
    test_input = RFF.read_file_with_new_line(test_input_file_path)
    input_list = map(lambda x: int(x.split(" ")[-1]) if x.split(" ") != ["noop"] else False, test_input)

    cycle_counter = 0
    x = 1
    special_cycles = [i for i in range(20, 221, 40)]
    signal_strength = 0
    for instruction in input_list:
        if instruction:
            if special_cycles:
                if (cycle_counter == special_cycles[0] - 2) or (cycle_counter == special_cycles[0] - 1):
                    current_cycle = special_cycles.pop(0)
                    signal_strength += current_cycle * x
                    print("special: ", current_cycle, x)
            cycle_counter += 2
            x += instruction
        else:
            if special_cycles:
                if cycle_counter == special_cycles[0] - 1:
                    current_cycle = special_cycles.pop(0)
                    signal_strength += current_cycle * x
                    print("special: ", current_cycle, x)
            cycle_counter += 1
        # print(cycle_counter, x)

    # print(cycle_counter)
    return signal_strength


def part_2(test_input_file_path: str, output_file_path: str) -> None:
    test_input = RFF.read_file_with_new_line(test_input_file_path)
    input_list = map(lambda y: int(y.split(" ")[-1]) if y.split(" ") != ["noop"] else False, test_input)
    output_file = open(output_file_path, "w")

    cycle_counter = 1
    last_cycle = cycle_counter
    x = 1
    sprite = {x-1, x, x+1}

    new_line = str()
    for instruction in input_list:
        # update the cycle number and execute x
        if instruction:
            cycle_counter += 2
            x += instruction
        else:
            cycle_counter += 1

        for c in range(cycle_counter-last_cycle):
            # if the current cycle number align with one of the sprite
            if (last_cycle+c-1) % 40 in sprite:
                new_line += "#"
            elif (last_cycle+c-1) % 40 not in sprite:
                new_line += "."

            # write the new line into the file
            if len(new_line) == 40:
                output_file.write(new_line + "\n")
                new_line = str()

        last_cycle = cycle_counter

        # moving the sprite based on the position of x
        sprite = {(x - 1), x, (x + 1)}
    return None


if __name__ == "__main__":
    # print(part_1("small_test_input.txt"))
    # print(part_1("large_test_input.txt"))
    # print(part_1("real_input.txt"))

    part_2("large_test_input.txt", "test_output.txt")
    part_2("real_input.txt", "real_output.txt")