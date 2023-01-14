import ReadFileFunctions as RFF
from typing import List, Dict, Tuple


def parse_crates(crates_input_file_name: str) -> Dict[str, str]:
    crates_input_file = open(crates_input_file_name, "r")
    crates_info = crates_input_file.readlines()

    crates_stacks, crates_number = crates_info[:-1], crates_info[-1]

    crates_tuples = [(crate_num, "") for crate_num in crates_number if crate_num != " "]
    crate_dict = {crate_num: crates for (crate_num, crates) in crates_tuples}

    for crates in crates_stacks:
        crate_position = 1
        for crate_index in range(1, len(crates), 4):
            if crates[crate_index] != " ":
                crate_dict[str(crate_position)] += crates[crate_index]
            crate_position += 1

    return crate_dict


def parse_instructions(instruction_input_file_name: str) -> List[Tuple[int, str, str]]:
    instruction_file = RFF.read_file_with_new_line(instruction_input_file_name)
    instruction_list = list()

    for instruction in instruction_file:
        instruction = instruction.split(" ")
        instruction_list.append((int(instruction[1]), instruction[3], instruction[5]))

    return instruction_list


def move_crates(crates: Dict[str, str], instructions: List[Tuple[int, str, str]]) -> str:
    for instruction in instructions:
        move_num, from_num, to_num = instruction[0], instruction[1], instruction[2]
        crates_moved = crates[from_num][:move_num]
        crates[from_num] = crates[from_num][move_num:]

        # Part 1:
        crates[to_num] = crates_moved[::-1] + crates[to_num]

        # Part 2:
        # crates[to_num] = crates_moved + crates[to_num]

    first_crates = "".join([value[0] for value in crates.values()])
    return first_crates


if __name__ == '__main__':
    # test_crates = parse_crates("test_crates.txt")
    # test_instructions = parse_instructions("test_instructions.txt")
    # test_top_crates = move_crates(test_crates, test_instructions)
    # print(test_top_crates)

    input_crates = parse_crates("crates.txt")
    input_instructions = parse_instructions("instructions.txt")
    top_crates = move_crates(input_crates, input_instructions)
    print(top_crates)

    # answers:
    # RFFFWBPNS
    # CQQBBJFCS