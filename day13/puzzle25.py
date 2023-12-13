def find_mirror_row(m):
    for i, row in enumerate(m[:-1]):
        if row == m[i + 1]:
            j = i - 1
            k = i + 2
            while j >= 0 and k < len(m):
                if m[j] != m[k]:
                    break
                j -= 1
                k += 1
            else:
                return i + 1
    return None


def puzzle25():
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
    h_ref, v_ref = 0, 0
    for m_i, m in enumerate(maps):
        print(f"Processing {m_i}")
        ref = find_mirror_row(m)
        if ref is not None:
            total_ref += (100 * ref)
            continue
        total_ref += find_mirror_row(list(zip(*m)))

    print(f"{h_ref} + {v_ref} = {total_ref}")


if __name__ == '__main__':
    puzzle25()
