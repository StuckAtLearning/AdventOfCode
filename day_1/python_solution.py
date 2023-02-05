import InputManager as im


def get_info_from_file(input_file_path: str) -> str:
    info = im.read_file_with_single_new_line(input_file_path, False)
    return info[0]


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


if __name__ == '__main__':
    stairs_info = get_info_from_file('AdventOfCode2015/day_1/real_input.txt')
    print(part_1(stairs_info))
    print(part_2(stairs_info))
