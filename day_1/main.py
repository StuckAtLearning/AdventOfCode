# Day 1 of Advent of Code

import ReadFileFunctions as RFF


def calories_tracker():
    # I swear this function is forcing me to go to the gym...
    calories_profile = RFF.read_file_double_new_line("elf_calories.txt")

    max_calories = max(map(lambda x: sum(map(int, x)), calories_profile))
    top_three_calories = sum(sorted(map(lambda x: sum(map(int, x)), calories_profile))[-3:])

    return max_calories, top_three_calories


if __name__ == '__main__':
    way_too_much_food, all_the_food = calories_tracker()
    print(way_too_much_food)
    print(all_the_food)

    # Answer for Part 1: 69206
    # Answer for Part 2: 197400


