from itertools import groupby
import InputManager as im
import string
import re

DISALLOWED_SUBSTRING = ["ab", "cd", "pq", "xy"]
VOWELS = ["a", "e", "i", "o", "u"]


def check_allowed_substring_only(current_input: str) -> bool:
    return not any(i in current_input for i in DISALLOWED_SUBSTRING)


def check_double_letter(current_input: str) -> bool:
    groups = groupby(current_input)
    result = [(label, sum(1 for _ in group)) for label, group in groups]
    return any((_, occurrence) for _, occurrence in result if occurrence >= 2)
    # for letter, occurrence in result:
    #     if occurrence >= 2:
    #         return True
    # return False


def check_vowels(current_input: str) -> bool:
    count_vowels = sum(1 for i in current_input if i in VOWELS)
    return count_vowels >= 3


def get_nice_strings_num(all_inputs: list[str]) -> int:
    return sum(1 for i in all_inputs if
               (check_vowels(i) and check_double_letter(i) and check_allowed_substring_only(i)))


def check_pairs(current_input: str) -> bool:
    for i in range(len(current_input)-1):
        check_substring = current_input[i] + current_input[i+1]
        if (check_substring in current_input[:i]) or (check_substring in current_input[i+1:][1:]):
            return True
    return False


def check_sandwich_letter(current_input: str) -> bool:
    alphabet_lower = string.ascii_lowercase
    for i in alphabet_lower:
        pattern = r"[a-z]*" + i + "." + i + "[a-z]*"
        if re.search(pattern, current_input):
            return True
    return False


def get_better_strings_num(all_inputs: list[str]) -> int:
    return sum(1 for i in all_inputs if (check_sandwich_letter(i)) and check_pairs(i))


def get_answers():
    input_file = im.read_file("day_5/real_input.txt")
    all_inputs = im.group_file_info_with_single_new_line(input_file)
    part_1_answer = get_nice_strings_num(all_inputs)
    part_2_answer = get_better_strings_num(all_inputs)
    return part_1_answer, part_2_answer


if __name__ == '__main__':
    print(get_answers())