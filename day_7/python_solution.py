import InputManager as im


def parse_wire_info(all_inputs: list[str]) -> dict[str, tuple[str]]:
    wire_info = [tuple(i.replace(' -> ', ' ').replace('NOT', '0 NOT').split(' ')) for i in all_inputs]
    return {info[-1]: tuple(info[:-1]) for info in wire_info}


def get_value(parsed_wire_info: dict[str, tuple[str]], target_wire_name: str) -> int:
    wire_instruction = parsed_wire_info[target_wire_name]
    if len(wire_instruction) == 1:
        if wire_instruction[0].isdigit():
            print(wire_instruction)
            return int(wire_instruction[0])
        return get_value(parsed_wire_info, wire_instruction[0])

    # note to self: change the assignment below because it is ugly.
    left, op, right = wire_instruction
    if not left.isdigit():
        left = get_value(parsed_wire_info, left)
    if not right.isdigit():
        right = get_value(parsed_wire_info, right)
    if op == "AND":
        return int(left) & int(right)
    elif op == "OR":
        return int(left) | int(right)
    elif op == "RSHIFT":
        return int(left) >> int(right)
    elif op == "LSHIFT":
        return int(left) << int(right)
    elif op == "NOT":
        return ~int(right) & 65535


def get_answers():
    input_file = im.read_file("day_7/real_input.txt")
    all_inputs = im.group_file_info_with_single_new_line(input_file)
    wire_info = parse_wire_info(all_inputs)
    print(wire_info)
    part_1_answer = get_value(wire_info, "a")
    print(part_1_answer)


if __name__ == '__main__':
    get_answers()
