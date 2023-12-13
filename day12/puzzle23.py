import itertools


def valid_map_square(t_m):
    t, m = t_m
    return t == '?' or t == m


def gen_maps(tmpl, cts, st, mp=""):
    if any(itertools.filterfalse(valid_map_square, zip(tmpl, mp))):
        # print(f"[INV] {tmpl[:len(mp)]} | {mp}")
        return 0
    if not cts:
        if any(itertools.filterfalse(valid_map_square, itertools.zip_longest(tmpl, mp, fillvalue='.'))):
            # print(f"[NOM] {tmpl} | {mp}")
            return 0
        else:
            # print(f"[VAL] {tmpl[:len(mp)]} | {mp}")
            return 1
    if st >= len(tmpl):
        # print(f"[OOR] {tmpl[:len(mp)]} | {mp}")
        return 0
    c = cts[0]
    perms = 0
    for i in range(st, len(tmpl) - c + 1):
        perms += gen_maps(tmpl, cts[1:], i + c + 1, mp + "." * (i-st) + "#" * c + ".")
    return perms


def puzzle23():
    with open("input", "r", encoding="utf8") as fp:
        input_data = fp.read().splitlines()

    perms = 0
    i = 0
    for line in input_data:
        springs, counts = line.split(" ")
        counts = [int(c) for c in counts.split(",")]
        # print(line)
        perms += gen_maps(springs, counts, 0)
    # 7236
    print(perms)


if __name__ == '__main__':
    puzzle23()