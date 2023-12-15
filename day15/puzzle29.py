def puzzle29():
    with open("input", "r", encoding="utf8") as fp:
        input_data = fp.read()

    total_hash = 0
    hash = 0
    for c in input_data:
        if c == ',':
            total_hash += hash
            hash = 0
        elif c in '\n\r':
            continue
        else:
            hash += ord(c)
            hash *= 17
            hash %= 256
    total_hash += hash

    print(total_hash)


if __name__ == '__main__':
    puzzle29()