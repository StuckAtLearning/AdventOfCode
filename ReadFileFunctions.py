from typing import List


def read_file_double_new_line(file_name: str) -> List[List[str]]:
    with open(file_name, 'r', encoding='utf-8') as file:
        data = file.read().split("\n\n")
    data_list = [i.split("\n") for i in data]

    # print(data_list)
    return data_list
