from AOCH import InputManager as im


def get_info_from_file(input_file_path: str) -> str:
    info = im.read_file(input_file_path)
    return info


def get_floor_num(info: str) -> int:
    up = info.count('(')
    down = info.count(')')
    return up - down


def get_input_position(info: str) -> int:
    stair_num = [1 if i == '(' else -1 for i in info]
    input_position = 1
    for i in range(len(stair_num)):
        input_position += stair_num[i]
        if input_position == -1:
            return i


def get_answers():
    stairs_info = get_info_from_file('day1/real_input.txt')
    part_1_answer = get_floor_num(stairs_info)
    part_2_answer = get_input_position(stairs_info)
    return part_1_answer, part_2_answer


if __name__ == '__main__':
    print(get_answers())
