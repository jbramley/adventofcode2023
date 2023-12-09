import itertools


def puzzle15():
    with open("input", "r", encoding="utf8") as fp:
        input_data = fp.read()

    directions, _, *map_nodes = input_data.splitlines()

    desert_map = {}
    for node in map_nodes:
        desert_map[node[:3]] = {"L": node[7:10], "R": node[12:15]}

    current_pos = 'AAA'
    steps = 0
    for d in itertools.cycle(directions):
        current_pos = desert_map[current_pos][d]
        steps += 1
        if current_pos == 'ZZZ':
            break
    print(steps)


if __name__ == '__main__':
    puzzle15()