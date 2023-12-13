import itertools





def find_mirror_row_with_smudge(m):
    for i, row in enumerate(m[:-1]):
        j, k = i, i + 1
        diffs = 0
        while j >= 0 and k < len(m):
            diffs += len(list(itertools.filterfalse(lambda x: x[0] == x[1], zip(m[j], m[k]))))
            if diffs > 1:
                break
            j -= 1
            k += 1
        if diffs == 1:
            return i + 1
    return None


def puzzle26():
    with open("input", "r", encoding="utf8") as fp:
        input_data = fp.read().splitlines()

    maps = []
    m = []
    for line in input_data:
        if line == "":
            maps.append(m[:])
            m = []
        else:
            m.append(line)
    maps.append(m[:])

    total_ref = 0
    for m_i, m in enumerate(maps):
        ref = find_mirror_row_with_smudge(m)
        if ref is not None:
            total_ref += (100 * ref)
            continue
        total_ref += find_mirror_row_with_smudge(list(zip(*m)))
    print(total_ref)


if __name__ == '__main__':
    puzzle26()
