def read_file_double_new_line(file_name: str) -> list[list[str]]:
    with open(file_name, 'r', encoding='utf-8') as file:
        data = file.read().split("\n\n")
    data_list = [i.split("\n") for i in data]

    file.close()
    return data_list


def read_file_with_new_line(file_name: str) -> list[str]:
    with open(file_name, 'r', encoding='utf-8') as file:
        data = file.read().split("\n")

    file.close()
    return data
