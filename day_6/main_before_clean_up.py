def part_1(input_file_name):
    input_file = open(input_file_name, "r")
    input_file_line = input_file.readlines()
    input_file_line = [line.strip("\n") for line in input_file_line]
    answer_list = list()

    for line in input_file_line:
        for c in range(len(line)-4):
            seen = set(line[i] for i in range(c, c+4))
            if len(seen) > 3:
                answer_list.append(c + 4)
                break

    return answer_list


if __name__ == '__main__':
    test_answer = part_1("test_input.txt")
    print(test_answer)
    real_answer = part_1("real_input.txt")
    print(real_answer)

