import ReadFileFunctions as RFF
import math


SNAFU_LOOK_UP = {"2": 2, "1": 1, "0": 0, "-": -1, "=": -2}
DECIMAL_LOOK_UP = {value: key for key, value in SNAFU_LOOK_UP.items()}


def parse_input(input_file_path):
    input_file = RFF.read_file_with_new_line(input_file_path)

    return input_file


def snafu_to_decimal(snafu: str):
    digits = [5**i for i in range(len(snafu))][::-1]
    decimal = 0
    for i, c in enumerate(snafu):
        decimal += SNAFU_LOOK_UP[c] * digits[i]
    return decimal


def decimal_to_snafu(decimal: int):
    decimal_length = 0
    while decimal > 5**decimal_length:
        decimal_length += 1

    digits = [5 ** i for i in range(decimal_length)][::-1]
    snafu = str()
    for d in digits:
        if decimal > 0:
            if abs(decimal - (2*d)) < abs(decimal - d):
                if abs(decimal - (2*d)) < abs(decimal - math.sqrt(d)):
                    snafu += DECIMAL_LOOK_UP[2]
                    decimal -= (2 * d)
                else:
                    snafu += DECIMAL_LOOK_UP[0]
            else:
                if abs(decimal - d) < abs(decimal - math.sqrt(d)):
                    snafu += DECIMAL_LOOK_UP[1]
                    decimal -= d
                else:
                    snafu += DECIMAL_LOOK_UP[0]
        elif decimal < 0:
            if abs(decimal + (2*d)) < abs(decimal + d):
                if abs(decimal + (2 * d)) < abs(decimal + math.sqrt(d)):
                    snafu += DECIMAL_LOOK_UP[-2]
                    decimal += (2 * d)
                else:
                    snafu += DECIMAL_LOOK_UP[0]
            else:
                if abs(decimal + d) < abs(decimal + math.sqrt(d)):
                    snafu += DECIMAL_LOOK_UP[-1]
                    decimal += d
                else:
                    snafu += DECIMAL_LOOK_UP[0]

    return snafu


def part_1(snafu_inputs: list):
    total = 0
    for number in snafu_inputs:
        total += snafu_to_decimal(number)

    print(total)
    decimal = decimal_to_snafu(total)
    return decimal


if __name__ == "__main__":
    # # part 1 test
    # test_file = parse_input("test_input.txt")
    # answer = part_1(test_file)
    # print(answer)

    # part 1
    test_file = parse_input("real_input.txt")
    answer = part_1(test_file)
    # print(answer)

    print(snafu_to_decimal("2--2-0=--0--100-=210"))
