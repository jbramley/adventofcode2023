import re


def puzzle2():
    numbers_re = re.compile(r"(one|two|three|four|five|six|seven|eight|nine|[0-9])")
    numbers_map = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
    calibration_sum = 0
    with open("../puzzle2/input", "r", encoding="utf8") as fp:
        input_lines = fp.readlines()
        for line in input_lines:
            line_numbers = []
            for i, c in enumerate(line):
                if '0' <= c <= '9':
                    line_numbers.append(int(c))
                else:
                    for k in numbers_map.keys():
                        if line[i:].startswith(k):
                            line_numbers.append(numbers_map[k])
                            continue
            digit_0 = numbers_map.get(line_numbers[0], line_numbers[0])
            digit_1 = numbers_map.get(line_numbers[-1], line_numbers[-1])
            print(f"{line} -> {line_numbers} -> {digit_0}{digit_1}")
            calibration_sum += int(f"{digit_0}{digit_1}")
    print(calibration_sum)


if __name__ == '__main__':
    puzzle2()