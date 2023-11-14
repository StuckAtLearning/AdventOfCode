import hashlib


def find_secret_key_md5(input_prefix: str, leading_zero_num: int) -> int:
    for i in range(10000000):
        md5_input = input_prefix + str(i)
        md5_output = hashlib.md5(md5_input.encode('utf-8')).hexdigest()
        if md5_output[:leading_zero_num] == '0' * leading_zero_num:
            return i


def get_answers():
    part_1_answer = find_secret_key_md5('iwrupvqb', 5)
    part_2_answer = find_secret_key_md5('iwrupvqb', 6)
    return part_1_answer, part_2_answer


if __name__ == "__main__":
    print(get_answers())
