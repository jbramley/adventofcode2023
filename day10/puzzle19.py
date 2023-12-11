PIPES = {
    'F': ((0, 1), (1, 0)),
    '7': ((0, -1), (1, 0)),
    'L': ((0, 1), (-1, 0)),
    'J': ((0, -1), (-1, 0)),
    '|': ((-1, 0), (1, 0)),
    '-': ((0, -1), (0, 1))
}

VALID_PIPES = {
    (0, 1): {'7', 'J', '-'},
    (0, -1): {'F', 'L', '-'},
    (1, 0): { 'J', 'L', '|'},
    (-1, 0): {'F', '7', '|'}
}


def puzzle19():
    with open("input", "r", encoding="utf8") as fp:
        input_data = fp.read().splitlines()

    starting_pos = (-1, -1)
    max_x = len(input_data[0])
    max_y = len(input_data)
    for i, line in enumerate(input_data):
        if (x := line.find("S")) >= 0:
            starting_pos = (i, x)
            break
    else:
        print("wtf?")

    print(starting_pos)
    for starting_dir in set(t for x in zip(*PIPES.values()) for t in x):
        p = starting_pos
        d = starting_dir
        pl = 0
        fl = False
        while True:
            n = (p[0] + d[0], p[1] + d[1])
            pl += 1
            if n[0] < 0 or n[1] < 0 or n[0] >= max_y or n[1] >= max_x:
                break
            if input_data[n[0]][n[1]] == 'S':
                fl = True
                break
            if input_data[n[0]][n[1]] not in VALID_PIPES[d]:
                break
            # print(f"{p}, {n}, {d}, {input_data[n[0]][n[1]]}, {PIPES[input_data[n[0]][n[1]]]}")
            p = n
            o = PIPES[input_data[p[0]][p[1]]]
            d = o[(o.index((d[0]*-1, d[1]*-1)) + 1) % 2]

        if fl:
            print(pl/2)
            break
    else:
        print("we got bugs!")


if __name__ == '__main__':
    puzzle19()