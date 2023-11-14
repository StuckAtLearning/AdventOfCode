import ReadFileFunctions as RFF
from collections import defaultdict, deque


def find_point(input_list: list[str], target_point: str) -> tuple[int, int] | str:
    for i in range(len(input_list)):
        for j in range(len(input_list[i])):
            if input_list[i][j] == target_point:
                return i, j
    return "input does not have target point"


def get_neighbours(current_index: tuple[int, int], dimensions: tuple[int, int]) -> list[tuple[int, int]]:
    x, y = current_index
    length, width = dimensions
    all_neighbours = []

    if x > 0:
        left = (x - 1, y)
        all_neighbours.append(left)
    if y > 0:
        up = (x, y - 1)
        all_neighbours.append(up)
    if x < length - 1:
        right = (x + 1, y)
        all_neighbours.append(right)
    if y < width - 1:
        down = (x, y + 1)
        all_neighbours.append(down)

    return all_neighbours


def find_all_chr(input_list: list[str], target_point: str) -> list[tuple[tuple[int, int], 0]]:
    all_points = list()
    for i in range(len(input_list)):
        for j in range(len(input_list[i])):
            if input_list[i][j] == target_point:
                all_points.append(((i, j), 0))
    return all_points


def find_distance(start_index: tuple[int, int], end_index: tuple[int, int], input_list: list[str]) -> \
        int | "fucked up you dingus":
    length, width = len(input_list), len(input_list[0])
    # start_indices = deque([(start_index, 0)])
    start_indices = deque(find_all_chr(input_list, "a"))
    path_dict = defaultdict(list)
    indices_seen = set()

    while start_indices:
        start_index, distance = start_indices.popleft()
        if start_index not in indices_seen:
            print(start_index, distance)
            indices_seen.add(start_index)
            if start_index == end_index:
                # print(start_index, distance)
                return distance
            neighbours = get_neighbours(start_index, (length, width))
            for neighbour in neighbours:
                if ord(input_list[neighbour[0]][neighbour[1]]) <= ord(input_list[start_index[0]][start_index[1]]) + 1:
                    if neighbour not in indices_seen:
                        start_indices.append((neighbour, distance + 1))
    #                    path_dict[start_index].append(neighbour)

    return "fucked up you dingus"


def part_1(test_input_file_path: str) -> int:
    test_input = RFF.read_file_with_new_line(test_input_file_path)

    # tuples
    starting_point = find_point(test_input, "S")
    ending_point = find_point(test_input, "E")

    # set S to a and E to z
    test_input[starting_point[0]] = test_input[starting_point[0]][:starting_point[1]] + "a" + test_input[starting_point[0]][starting_point[1]+1:]
    test_input[ending_point[0]] = test_input[ending_point[0]][:ending_point[1]] + "z" + test_input[ending_point[0]][ending_point[1]+1:]

    # find path
    distance = find_distance(starting_point, ending_point, test_input)

    return distance


if __name__ == "__main__":
    # part_1_test_answer = part_1("advanced_test_input.txt.txt")
    # print(part_1_test_answer)
    #
    # part_1_answer = part_1("real_input.txt")
    # print(part_1_answer)

    # part_2_test_answer = part_1("advanced_test_input.txt.txt")
    # print(part_2_test_answer)

    part_2_answer = part_1("real_input.txt")
    print(part_2_answer)