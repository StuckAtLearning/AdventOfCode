import ReadFileFunctions as RFF
import HelperFunctions as HF


def get_priority_sum(single_char: str) -> int:
    priority_sum = 0
    priority_sum += ord(single_char) - 38 if ord(single_char) < 97 else ord(single_char) - 96
    return priority_sum


def calculate_priority_sum_for_sections(test_input_file: str) -> int:
    test_input = RFF.read_file_with_new_line(test_input_file)
    priority_sum = 0
    for backpack in test_input:
        sectioner = len(backpack) // 2
        first_half, second_half = backpack[:sectioner], backpack[sectioner:]
        common_snack = HF.find_common_element([first_half, second_half])
        priority_sum += get_priority_sum(common_snack[0])
    return priority_sum


def calculate_priority_sum_for_elf_groups(test_input_file: str) -> int:
    test_input = RFF.read_file_with_new_line(test_input_file)
    priority_sum = 0
    for i in range(0, len(test_input), 3):
        first_half, second_elf, third_elf = test_input[i], test_input[i+1], test_input[i+2]
        common_snack = HF.find_common_element([first_half, second_elf, third_elf])
        priority_sum += get_priority_sum(common_snack[0])
    return priority_sum


if __name__ == '__main__':
    backpack_priority_sum = calculate_priority_sum_for_sections("real_input.txt")
    print(backpack_priority_sum)

    group_priority_sum = calculate_priority_sum_for_elf_groups("real_input.txt")
    print(group_priority_sum)
