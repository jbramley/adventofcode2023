import itertools
from collections import Counter

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

    loop = set()
    loop_v = set()
    loop_h = set()
    for starting_dir in set(t for x in zip(*PIPES.values()) for t in x):
        p = starting_pos
        d = starting_dir
        last_dir = ()
        fl = False
        while True:
            loop.add(p)
            if input_data[p[0]][p[1]] == '|':
                loop_v.add(p)
            elif input_data[p[0]][p[1]] == '-':
                loop_h.add(p)
            n = (p[0] + d[0], p[1] + d[1])
            if n[0] < 0 or n[1] < 0 or n[0] >= max_y or n[1] >= max_x:
                break
            if input_data[n[0]][n[1]] == 'S':
                last_dir = (d[0]*-1, d[1]*-1)
                fl = True
                break
            if input_data[n[0]][n[1]] not in VALID_PIPES[d]:
                break
            p = n
            o = PIPES[input_data[p[0]][p[1]]]
            d = o[(o.index((d[0]*-1, d[1]*-1)) + 1) % 2]

        if fl:
            for p, ds in PIPES.items():
                if ds == (starting_dir, last_dir) or ds == (last_dir, starting_dir):
                    line = input_data[starting_pos[0]]
                    input_data[starting_pos[0]] = line[:starting_pos[1]] + p + line[starting_pos[1] + 1:]
                    break
            break
        else:
            loop_v.clear()
            loop_h.clear()
            loop.clear()

    inside_loop = 0
    for y, x in itertools.product(range(max_y), range(max_x)):
        if (y,x) in loop:
            continue
        last_c = None
        sides = 0
        for x1 in range(x):
            if (y, x1) not in loop:
                continue
            c = input_data[y][x1]
            if last_c == 'F' and c == 'J':
                sides += 1
                last_c = None
            elif last_c == 'F' and c == '7':
                last_c = None
            elif last_c == 'L' and c == '7':
                sides += 1
                last_c = None
            elif last_c == 'L' and c == 'J':
                last_c = None
            elif c == '|':
                sides += 1
            if c in "FL":
                last_c = c

        if sides % 2:
            inside_loop += 1

    print(inside_loop)


if __name__ == '__main__':
    puzzle19()