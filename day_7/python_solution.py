import InputManager as im


def parse_wire_info(all_inputs: list[str]) -> dict[str, tuple[str]]:
    wire_info = [tuple(i.replace(' -> ', ' ').replace('NOT', '0 NOT').split(' ')) for i in all_inputs]
    return {info[-1]: tuple(info[:-1]) for info in wire_info}


# Let's start with pseudocode, shall we? Is this what you want Eric?
# We first have a target wire we want to know the value of. This is "a" in our case. We use dictionary. idk if it works.
# We then have a iterable instructions that is not in particular order.
# We know "lx" is assigned to "a", so now we need to know what value "lx" has.
# We find out what was assigned to "lx", eventually we will come across int values.
# Ok so the strategy is kind of like finding what wires are connected to "a" and calculate the values.
# To do that, we first loop through the instructions and find any instruction that has to do with "a";
# Then, we need to loop through the instructions again to find instructions that has second degree connection with "a";
# We can probably do this recursively to torture ourselves; until we reach all number assigning instructions.
# Problem: what if "a" is changed after it was assigned?
# Anyway, ignore that for now: can we somehow follow the instructions backwards to calculate "a"?
# We can probably do that with the recursive step earlier?
# Well okay I tried, and that was a failure, just like me.


def get_value(parsed_wire_info: dict[str, tuple[str]], target_wire_name: str) -> int:
    wire_instruction = parsed_wire_info[target_wire_name]
    if len(wire_instruction) == 1:
        if wire_instruction[0].isdigit():
            print(wire_instruction)
            return int(wire_instruction[0])
        return get_value(parsed_wire_info, wire_instruction[0])

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
