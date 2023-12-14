from functools import cache


@cache
def tilt_north(p):
    p = p.splitlines()
    new_p = [["."]*len(p[0]) for _ in range(len(p))]
    stops = [-1] * len(p[0])

    for i, row in enumerate(p):
        for j, c in enumerate(row):
            if c == '#':
                stops[j] = i
                new_p[i][j] = '#'
            if c == 'O':
                stops[j] += 1
                new_p[stops[j]][j] = 'O'
    return "\n".join("".join(x) for x in new_p)


@cache
def tilt_south(p):
    p = "\n".join(reversed(p.splitlines()))
    new_p = tilt_north(p)
    return "\n".join(reversed(new_p.splitlines()))


@cache
def tilt_west(p):
    p = "\n".join("".join(r) for r in zip(*[c for c in p.splitlines()]))
    new_p = tilt_north(p)
    return "\n".join("".join(r) for r in zip(*[c for c in new_p.splitlines()]))


@cache
def tilt_east(p):
    p = "\n".join("".join(r) for r in reversed(list(zip(*[c for c in p.splitlines()]))))
    new_p = tilt_north(p)
    return "\n".join("".join(reversed(r)) for r in zip(*[c for c in new_p.splitlines()]))


@cache
def cycle(p):
    return tilt_east(tilt_south(tilt_west(tilt_north(p))))


def puzzle28():
    with open("input", "r", encoding="utf8") as fp:
        input_data = fp.read()

    p = input_data
    for i in range(1_000_000_000):
        p = cycle(p)
        if i % 1_000_000 == 0:
            print(i)

    total_load = 0
    final_p = p.splitlines()
    for i, row in enumerate(final_p):
        for c in row:
            if c == 'O':
                total_load += len(final_p) - i
    print(f"total load: {total_load}")


if __name__ == '__main__':
    puzzle28()
