import itertools
import pprint
from collections import defaultdict


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


def puzzle24():
    with open("input", "r", encoding="utf8") as fp:
        input_data = fp.read().splitlines()

    perms = 0
    for line_no, line in enumerate(input_data):
        springs, counts = line.split(" ")
        # counts = [int(c) for c in counts.split(",")]
        springs = "?".join(springs for _ in range(5))
        counts = [int(c) for c in counts.split(",")] * 5
        reqd_space = list(reversed(list(itertools.accumulate(c + 1 for i, c in enumerate(reversed(counts))))))
        reqd_space.append(0)
        possibilities = {0: 1}
        total_len = len(springs)
        max_i = len(counts) - 1
        for i, c in enumerate(counts):
            new_possibilities = defaultdict(lambda: 0)
            for p_len, p_perms in possibilities.items():
                for j in range(total_len - c - reqd_space[i+1] - p_len + 1):
                    if p_len+j+c > total_len:
                        break
                    if "#" in springs[p_len:p_len+j]:
                        break
                    if '.' in springs[p_len+j:p_len+j+c]:
                        continue
                    if p_len + j +c < total_len and springs[p_len+j+c] == '#':
                        continue
                    if i == max_i and '#' in springs[p_len+j+c:]:
                        continue
                    new_possibilities[p_len+j+c+1] += p_perms
            possibilities = new_possibilities
            # pprint.pprint(possibilities)
        line_perms = sum(possibilities.values())
        # p1 = gen_maps(springs, counts, 0)
        # if line_perms != p1:
        #     print(f"{line_no}: {line_perms} / {p1}")
        # if line_no == 3:
        #     break
        perms += line_perms
    print(perms)


if __name__ == '__main__':
    puzzle24()
