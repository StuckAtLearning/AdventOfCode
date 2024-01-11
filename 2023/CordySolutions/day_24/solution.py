def parse_input(input_file):
    parsed_input = list()
    with open(input_file) as file:
        for line in file:
            position, velocity = line.split(" @ ")
            px, py, pz = position.split(", ")
            vx, vy, vz = velocity.split(", ")
            parsed_input.append((
                (int(px), int(py), int(pz)),
                (int(vx), int(vy), int(vz))
            ))
    return parsed_input


def main():
    parsed_input = parse_input("test_input.txt")
    print(parsed_input)


main()
