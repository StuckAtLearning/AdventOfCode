import ReadFileFunctions as RFF


def parse_input(input_file_path):
    input_file = RFF.read_file_with_new_line(input_file_path)

    dot_coords = set()
    hash_tag_coords = set()
    for row in range(len(input_file)):
        for column in range(len(input_file[row])):
            if input_file[row][column] == ".":
                dot_coords.add((row, column))
            else:
                hash_tag_coords.add((column, row))

    return dot_coords, hash_tag_coords


def shift_coords(coords_set: set):
    new_coords_set = set()
    for coord in coords_set:
        new_coord = (coord[0] + 1, coord[1] + 1)
        new_coords_set.add(new_coord)
    return new_coords_set


def get_map_dimension(hash_tag_coords):
    length = abs(max(hash_tag_coords, key=lambda a: a[0])[0] - min(hash_tag_coords, key=lambda a: a[0])[0])
    width = abs(max(hash_tag_coords, key=lambda a: a[1])[1] - min(hash_tag_coords, key=lambda a: a[1])[1])

    return length, width


def print_map(hash_tag_coords):
    min_x = min(x for x, _ in hash_tag_coords)
    max_x = max(x for x, _ in hash_tag_coords)
    min_y = min(y for _, y in hash_tag_coords)
    max_y = max(y for _, y in hash_tag_coords)

    print('\n'.join(''.join(
        '.#'[(x, y) in hash_tag_coords]
        for x in range(min_x, 1 + max_x)
    ) for y in range(min_y, 1 + max_y)))

    count_white_space = 0
    for x in range(min_x, 1 + max_x):
        for y in range(min_y, 1 + max_y):
            if (x, y) not in hash_tag_coords:
                count_white_space += 1

    return count_white_space


def propose_position(current_coord, hash_tag_coords, round_count):
    x = current_coord[0]
    y = current_coord[1]
    nw = (x-1, y-1)
    ne = (x+1, y-1)
    sw = (x-1, y+1)
    se = (x+1, y+1)
    north = (x, y-1)
    south = (x, y+1)
    west = (x-1, y)
    east = (x+1, y)
    neighbours_coords = {nw, ne, sw, se, north, south, west, east}

    # if the current elf position is surrounded by free space, do not move
    if len(hash_tag_coords.intersection(neighbours_coords)) == 0:
        return current_coord

    # otherwise, follow the moving priority
    if round_count % 4 == 0:
        if len(hash_tag_coords.intersection({north, ne, nw})) == 0:
            return north
        elif len(hash_tag_coords.intersection({south, se, sw})) == 0:
            return south
        elif len(hash_tag_coords.intersection({west, nw, sw})) == 0:
            return west
        elif len(hash_tag_coords.intersection({east, ne, se})) == 0:
            return east
        return current_coord
    elif round_count % 4 == 1:
        if len(hash_tag_coords.intersection({south, se, sw})) == 0:
            return south
        elif len(hash_tag_coords.intersection({west, nw, sw})) == 0:
            return west
        elif len(hash_tag_coords.intersection({east, ne, se})) == 0:
            return east
        elif len(hash_tag_coords.intersection({north, ne, nw})) == 0:
            return north
        return current_coord
    elif round_count % 4 == 2:
        if len(hash_tag_coords.intersection({west, nw, sw})) == 0:
            return west
        elif len(hash_tag_coords.intersection({east, ne, se})) == 0:
            return east
        elif len(hash_tag_coords.intersection({north, ne, nw})) == 0:
            return north
        elif len(hash_tag_coords.intersection({south, se, sw})) == 0:
            return south
        return current_coord
    elif round_count % 4 == 3:
        if len(hash_tag_coords.intersection({east, ne, se})) == 0:
            return east
        elif len(hash_tag_coords.intersection({north, ne, nw})) == 0:
            return north
        elif len(hash_tag_coords.intersection({south, se, sw})) == 0:
            return south
        elif len(hash_tag_coords.intersection({west, nw, sw})) == 0:
            return west
        return current_coord


def part_1(hash_tag_coords):
    # part 1 only
    # for i in range(10):
    i = 0
    while True:
        # print(i)

        # first half:
        proposal_look_up = dict()
        seen_proposed_positions = set()
        for elf_position in hash_tag_coords:
            proposed_position = propose_position(elf_position, hash_tag_coords, i)
            if proposed_position not in seen_proposed_positions:
                seen_proposed_positions.add(proposed_position)
                proposal_look_up[proposed_position] = [elf_position]
            else:
                proposal_look_up[proposed_position].append(elf_position)

        # second half:
        for new_position, elf_position in proposal_look_up.items():
            if len(elf_position) == 1:
                elf_position = elf_position[0]
                hash_tag_coords.remove(elf_position)
                hash_tag_coords.add(new_position)

        # part 2 only:
        num_elves_in_position = 0
        for new_position, elf_position in proposal_look_up.items():
            if new_position == elf_position[0]:
                num_elves_in_position += 1
        if num_elves_in_position == len(hash_tag_coords):
            return i + 1

        i += 1

    # part 1 only
    # white_space_num = print_map(hash_tag_coords)
    # return white_space_num


if __name__ == "__main__":
    # # part 1 and 2 test
    # empty_coords, elves_coords = parse_input("test_input.txt")
    # answer = part_1(elves_coords)
    # print(answer)

    # part 1 and 2
    empty_coords, elves_coords = parse_input("real_input.txt")
    answer = part_1(elves_coords)
    print(answer)

