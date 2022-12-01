# Day 1 of Advent of Code

def calories_tracker(): # I swear this function is forcing me to go to the gym...
    input_file = open("elf_calories.txt", "r")
    max_calories = 0
    current_elf_calories = 0
    elf_record = list()

    single_calorie = input_file.readline()
    while single_calorie:
        if single_calorie != "\n":
            single_calorie = int(single_calorie)
            current_elf_calories += single_calorie
        else:
            if max_calories < current_elf_calories:
                max_calories = current_elf_calories
            elf_record.append(current_elf_calories)
            current_elf_calories = 0

        single_calorie = input_file.readline()

    return max_calories, sorted(elf_record)


if __name__ == '__main__':
    way_too_much_food, all_the_food = calories_tracker()
    top_three_calories = sum(all_the_food[-3:])
    print(way_too_much_food)
    print(top_three_calories)