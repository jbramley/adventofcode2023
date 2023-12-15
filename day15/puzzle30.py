
def update_hash_map(hashmap, hash_, label, op, focal_length):
    r = None
    for i, v in enumerate(hashmap[hash_]):
        if v[0] == label:
            r = i
            break
    if op == '-':
        if r is not None:
            hashmap[hash_] = hashmap[hash_][:r] + hashmap[hash_][r + 1:]
    if op == '=':
        if r is not None:
            hashmap[hash_][r] = (label, int(focal_length))
        else:
            hashmap[hash_].append((label, int(focal_length)))


def puzzle30():
    with open("input", "r", encoding="utf8") as fp:
        input_data = fp.read()
    hashmap = [list() for _ in range(256)]
    hash_ = 0
    label = ""
    op = ""
    focal_length = ""
    for c in input_data:
        if c == ',':
            update_hash_map(hashmap, hash_, label, op, focal_length)
            hash_ = 0
            label = ""
            op = ""
            focal_length = ""
        elif c in '\n\r':
            continue
        else:

            if c in '-=':
                op = c
            elif op and '1' <= c <= '9':
                focal_length = c
            else:
                label += c
                hash_ += ord(c)
                hash_ *= 17
                hash_ %= 256
    update_hash_map(hashmap, hash_, label, op, focal_length)

    total_v = 0
    for i, values in enumerate(hashmap):
        for j, lens in enumerate(values):
            total_v += ((1+i)*(1+j)*lens[1])

    print(total_v)


if __name__ == '__main__':
    puzzle30()