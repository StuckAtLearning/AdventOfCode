import ReadFileFunctions as RFF
from collections import deque

SYMBOL_LOOKUP = {(1, 0): ">", (0, 1): "v", (-1, 0): "<", (0, -1): "^", None: "#", (0, 0): "."}
DICT_LOOKUP = {value: key for key, value in SYMBOL_LOOKUP.items()}


def parse_input(input_file_path):
    input_file = RFF.read_file_with_new_line(input_file_path)

    width = len(input_file[0])
    length = len(input_file)

    coord_dict = dict()

    for y in range(length):
        for x in range(width):
            coord_dict[(x, y)] = [DICT_LOOKUP[input_file[y][x]]]

    starting_coord = (input_file[0].index("."), 0)
    ending_coord = (input_file[-1].index("."), len(input_file) - 1)
    print("starting coord is: ", starting_coord)
    print("ending coord is: ", ending_coord)
    # coord_dict[starting_coord] = "E"
    # coord_dict[ending_coord] = "T" # as in Terminate

    return coord_dict, width, length


def print_map(coord_dict, width, length, current_coord=None):
    coord_list = list()
    for i in range(length):
        coord_list.append(list())
        for j in range(width):
            coord_list[i].append("#")

    for coord, symbol in coord_dict.items():
        x, y = coord
        if isinstance(symbol, str):
            coord_list[y][x] = symbol
        elif len(symbol) == 1:
            coord_list[y][x] = SYMBOL_LOOKUP[symbol[0]]
        else:
            coord_list[y][x] = str(len(symbol))

    if current_coord:
        x, y = current_coord
        coord_list[y][x] = "E"

    print("\n".join("".join(row) for row in coord_list), "\n")


def wrap_action(action, current_coord, width, length):
    if action == (1, 0):
        return (1, current_coord[1])
    elif action == (-1, 0):
        return (width-2, current_coord[1])
    elif action == (0, 1):
        return (current_coord[0], 1)
    elif action == (0, -1):
        return (current_coord[0], length-2)


def move_blizzard(coord_dict, width, length):
    new_coord_dict = dict()
    for coord, symbol in coord_dict.items():
        # if it is a wall or the starting/ending point
        if (not symbol[0]) or (isinstance(symbol, str)):
            new_coord_dict[coord] = symbol

        # if the symbol is a list of tuple(s)
        else:
            while symbol:
                action = symbol.pop(0)
                new_coord = (coord[0]+action[0], coord[1]+action[1])

                if coord_dict[new_coord] == [None]:
                    new_coord = wrap_action(action, new_coord, width, length)

                if new_coord in new_coord_dict.keys():
                    new_coord_dict[new_coord].append(action)
                    if (0, 0) in new_coord_dict[new_coord]:
                        new_coord_dict[new_coord].remove((0, 0))
                else:
                    new_coord_dict[new_coord] = [action]

        if coord not in new_coord_dict.keys():
            new_coord_dict[coord] = [(0, 0)]

    return new_coord_dict


def get_empty_neighbours(current_coord, coord_dict):
    x, y = current_coord
    above = (x, y-1)
    below = (x, y+1)
    left = (x-1, y)
    right = (x+1, y)
    neighbours = [above, below, left, right]

    empty_neighbours = list()
    for neighbour in neighbours:
        if neighbour in coord_dict:
            if coord_dict[neighbour] == [(0, 0)]:
                empty_neighbours.append(neighbour)
    return empty_neighbours


def part_1(blizzards, width, length, starting_coord, destination_coord):
    queue = deque([(starting_coord, 0)])
    seen = set()
    prev_minute = 0
    while queue:
        current_coord, minutes = queue.popleft()

        if (current_coord, minutes) in seen:
            continue
        seen.add((current_coord, minutes))

        if minutes != prev_minute:
            prev_minute = minutes
            blizzards = move_blizzard(blizzards, width, length)

        if current_coord == destination_coord:
            return minutes - 1, blizzards

        neighbours = get_empty_neighbours(current_coord, blizzards)
        if blizzards[current_coord] == [(0, 0)]:
            neighbours.append(current_coord)

        for neighbour in neighbours:
            queue.append((neighbour, minutes + 1))


if __name__ == "__main__":
    # # part 1 test
    # map_dict, map_width, map_length = parse_input("easy_test_input.txt")
    # print_map(map_dict, map_width, map_length)
    #
    # start = (1, 0)
    # end = (5, 6)
    # answer = part_1(map_dict, map_width, map_length, start, end)
    # print(answer)

    # # part 1
    # map_dict, map_width, map_length = parse_input("real_input.txt")
    # start = (1, 0)
    # end = (120, 26)
    # answer = part_1(map_dict, map_width, map_length, start, end)
    # print(answer)

    # # part 2 test
    # map_dict, map_width, map_length = parse_input("advanced_test_input.txt")
    # print_map(map_dict, map_width, map_length)
    #
    # start = (1, 0)
    # end = (6, 5)
    # total = 0
    # answer, new_blizzards = part_1(map_dict, map_width, map_length, start, end)
    # total += answer
    # print(answer, total)
    # answer, new_blizzards = part_1(new_blizzards, map_width, map_length, end, start)
    # total += answer
    # print(answer, total)
    # answer, new_blizzards = part_1(new_blizzards, map_width, map_length, start, end)
    # total += answer
    # print(answer, total)

    # part 2
    map_dict, map_width, map_length = parse_input("real_input.txt")
    print_map(map_dict, map_width, map_length)

    start = (1, 0)
    end = (120, 26)
    total = 0
    answer, new_blizzards = part_1(map_dict, map_width, map_length, start, end)
    total += answer
    print(answer, total)
    answer, new_blizzards = part_1(new_blizzards, map_width, map_length, end, start)
    total += answer
    print(answer, total)
    answer, new_blizzards = part_1(new_blizzards, map_width, map_length, start, end)
    total += answer
    print(answer, total)
