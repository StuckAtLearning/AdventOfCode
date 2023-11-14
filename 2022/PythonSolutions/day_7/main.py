import ReadFileFunctions as RFF


def part_1(input_file_name: str) -> tuple[int, dict[str, int]]:
    input_file = RFF.read_file_with_new_line(input_file_name)
    cleaned_input = [line.split(" ") for line in input_file]

    dir_his = list()
    file_seen = set()
    dir_dict = {"/": 0}

    for line in cleaned_input:
        current_path = "/".join(dir_his)
        if line[0].isdigit():
            file_path = current_path + "/" + line[1]
            if file_path not in file_seen:
                all_paths = list()
                higher_path = "/"
                for the_dir in dir_his[1:]:
                    all_paths.append(higher_path)
                    higher_path += "/" + the_dir
                all_paths.append(higher_path)
                for path in all_paths:
                    dir_dict[path] += int(line[0])
                file_seen.add(file_path)
        elif line[0] == "dir":
            dir_path = current_path + "/" + line[1]
            if dir_path not in dir_dict:
                dir_dict[dir_path] = 0
        elif line[1] == "cd":
            if line[2] == "/":
                dir_his = ["/"]
            elif line[2] == "..":
                dir_his.pop(-1)
            else:
                dir_his.append(line[2])

    total_sum = sum([value for value in dir_dict.values() if value <= 100000])
    # print(dir_dict)

    return total_sum, dir_dict


def part_2(dir_lookup: dict[str, int]) -> int:
    space_now = 70_000_000 - dir_lookup["/"]
    delete_space = 30_000_000 - space_now
    file_sizes = sorted(dir_lookup.values())
    for i in file_sizes:
        if i >= delete_space:
            return i


if __name__ == '__main__':
    test_sum, test_dict = part_1("test_input.txt")
    # 95437
    real_sum, real_dict = part_1("real_input.txt")

    delete_size = part_2(test_dict)
    print(delete_size)
    real_delete_size = part_2(real_dict)
    print(real_dict)
    print(real_delete_size)

