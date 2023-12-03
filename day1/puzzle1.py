def puzzle1():
    with open("input", "r", encoding="utf8") as fp:
        input_lines = fp.readlines()
    calibration_sum = 0
    for line in input_lines:
        digits = [c for c in line if '0' <= c <= '9']
        calibration_sum += int(digits[0] + digits[-1])
    print(f"Calibration sum: {calibration_sum}")


if __name__ == '__main__':
    puzzle1()