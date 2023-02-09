import InputManager as im


def get_info_from_file(input_file_path: str) -> str:
    info = im.read_file(input_file_path)
    return info


def part_1(info: str) -> int:
    up = info.count('(')
    down = info.count(')')
    return up - down


def part_2(info: str) -> int:
    stair_num = [1 if i == '(' else -1 for i in info]
    stair_count = 1
    for i in range(len(stair_num)):
        stair_count += stair_num[i]
        if stair_count == -1:
            return i


def get_answers():
    stairs_info = get_info_from_file('day_1/real_input.txt')
    print(part_1(stairs_info))
    print(part_2(stairs_info))


if __name__ == '__main__':
    get_answers()
