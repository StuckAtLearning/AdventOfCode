import InputManager as im


def execute_assembly(all_inputs: list[str]):
    all_inputs = [i.split(' ') for i in all_inputs]
    print(all_inputs)


def get_answers():
    input_file = im.read_file("day_7/real_input.txt")
    all_inputs = im.group_file_info_with_single_new_line(input_file)
    execute_assembly(all_inputs)


if __name__ == '__main__':
    get_answers()