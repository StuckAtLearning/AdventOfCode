import ReadFileFunctions as RFF


def test_function(test_input_file):
    test_input = RFF.read_file_with_new_line(test_input_file)
    total_count = 0
    for backpack in test_input:
        sectioner = int(len(backpack) / 2)
        section_1 = backpack[:sectioner]
        section_2 = backpack[sectioner:]

        section_1 = sorted(section_1)
        section_2 = sorted(section_2)

        while (section_1 != []) or (section_2 != []):
            if section_1[0] == section_2[0]:
                if ord(section_1[0]) < 97: # Uppercase
                    total_count += ord(section_1[0]) - 38
                else:
                    total_count += ord(section_1[0]) - 96
                break
            elif section_1[0] < section_2[0]:
                section_1.pop(0)
            else:
                section_2.pop(0)
    return total_count


def part_2_function(test_input_file):
    test_input = RFF.read_file_with_new_line(test_input_file)
    total_count = 0
    for i in range(int((len(test_input)/3))):
        common_ground = list()

        first_elf = test_input[0+(i*3)]
        second_elf = test_input[1+(i*3)]
        third_elf = test_input[2+(i*3)]

        first_elf = sorted(first_elf)
        second_elf = sorted(second_elf)
        third_elf = sorted(third_elf)

        first_elf = list(dict.fromkeys(first_elf))
        second_elf = list(dict.fromkeys(second_elf))
        third_elf = list(dict.fromkeys(third_elf))

        while (first_elf != []) and (second_elf != []):
            if first_elf[0] == second_elf[0]:
                common_ground.append(first_elf[0])
                first_elf.pop(0)
                second_elf.pop(0)
            elif first_elf[0] < second_elf[0]:
                first_elf.pop(0)
            else:
                second_elf.pop(0)

        # print(common_ground)
        # print(third_elf)

        while (common_ground != []) or (third_elf != []):
            if common_ground[0] == third_elf[0]:
                if ord(common_ground[0]) < 97: # Uppercase
                    total_count += ord(common_ground[0]) - 38
                else:
                    total_count += ord(common_ground[0]) - 96
                break
            elif common_ground[0] < third_elf[0]:
                common_ground.pop(0)
            else:
                third_elf.pop(0)

    return total_count



if __name__ == '__main__':
    # count_total = test_function("real_input.txt")
    # print(count_total)

    part_2_ans = part_2_function("real_input.txt")
    print(part_2_ans)

