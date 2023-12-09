import itertools
import math


def puzzle15():
    with open("input", "r", encoding="utf8") as fp:
        input_data = fp.read()

    directions, _, *map_nodes = input_data.splitlines()

    desert_map = {}
    current_poses = []
    for node in map_nodes:
        desert_map[node[:3]] = {"L": node[7:10], "R": node[12:15]}
        if node[2] == 'A':
            current_poses.append(node[:3])

    initial_steps = [0]*len(current_poses)
    cycle_steps = [0]*len(current_poses)
    for i, pos in enumerate(current_poses):
        for d in itertools.cycle(directions):
            pos = desert_map[pos][d]
            initial_steps[i] += 1
            if pos[2] == 'Z':
                break
        offset = initial_steps[i] % len(directions)
        cycle_directions = directions[offset:] + directions[:offset]
        print(f"{pos}: {desert_map[pos]}")
        for d in itertools.cycle(cycle_directions):
            pos = desert_map[pos][d]
            cycle_steps[i] += 1
            if pos[2] == 'Z':
                break

    print(initial_steps)
    print(cycle_steps)
    # seems awfully coincidental that these happen to be the same, but because they are, we can just do this:
    print(math.lcm(*cycle_steps))


if __name__ == '__main__':
    puzzle15()