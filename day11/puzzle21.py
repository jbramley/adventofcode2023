import itertools


def puzzle21():
    with open("input", "r", encoding="utf8") as fp:
        input_data = fp.read().splitlines()

    galaxies = []
    empty_rows = 0
    galaxy_cols = set()
    for i, line in enumerate(input_data):
        if '#' not in line:
            empty_rows += 1
            continue
        for j, char in enumerate(line):
            if char == '#':
                galaxies.append((i + empty_rows, j))
                galaxy_cols.add(j)
    empty_cols = set(range(len(input_data[0]))) - galaxy_cols
    col_bumps = [int(i in empty_cols) for i in range(len(input_data[0]))]
    col_adds = list(itertools.accumulate(col_bumps))

    total_d = 0
    for g1, g2 in itertools.combinations(galaxies, 2):
        total_d += abs(g2[0] - g1[0]) + abs((g2[1] + col_adds[g2[1]]) - (g1[1] + col_adds[g1[1]]))

    print(total_d)


if __name__ == '__main__':
    puzzle21()

