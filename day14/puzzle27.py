def puzzle27():
    with open("input", "r", encoding="utf8") as fp:
        input_data = fp.read().splitlines()

    stops = [-1] * len(input_data[0])
    p_len = len(input_data)
    total_load = 0

    for i, row in enumerate(input_data):
        for j, c in enumerate(row):
            if c == '#':
                stops[j] = i
            if c == 'O':
                stops[j] += 1
                total_load += p_len - stops[j]
    print(total_load)


if __name__ == '__main__':
    puzzle27()
