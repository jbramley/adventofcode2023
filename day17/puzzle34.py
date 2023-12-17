from collections import defaultdict, namedtuple


node_t = namedtuple('node_t', 'x,y,dx,dy')


def puzzle33():
    with open("input", "r", encoding="utf8") as fp:
        grid = fp.read().splitlines()

    grid_x = len(grid[0])
    grid_y = len(grid)

    unvisited: dict[int, set[node_t]] = {}
    nodes: dict[node_t, int | None] = defaultdict(lambda: None)
    n = node_t(0, 0, 0, 0)
    nodes[n] = 0

    shortest_path = None
    while True:
        l_x = node_t(n.x - 1, n.y, n.dx - 1, 0)
        r_x = node_t(n.x + 1, n.y, n.dx + 1, 0)
        u_y = node_t(n.x, n.y - 1, 0, n.dy - 1)
        d_y = node_t(n.x, n.y + 1, 0, n.dy + 1)
        if n.x > 0 and ((0 > n.dx > -10) or (n.dx == 0 and (n.dy == 0 or abs(n.dy) >= 4))) and nodes[l_x] is None:
            nodes[l_x] = nodes[n] + int(grid[n.y][n.x - 1])
            unvisited.setdefault(nodes[n] + int(grid[n.y][n.x - 1]), set())
            unvisited[nodes[n] + int(grid[n.y][n.x - 1])].add(l_x)
        if n.x < (grid_x - 1) and ((0 < n.dx < 10) or (n.dx == 0 and (n.dy == 0 or abs(n.dy) >= 4))) and nodes[r_x] is None:
            if n.y == (grid_y - 1) and (n.x + 1) == (grid_x - 1) and n.dx >= 3:
                shortest_path = nodes[n] + int(grid[n.y][n.x + 1])
                break
            nodes[r_x] = nodes[n] + int(grid[n.y][n.x + 1])
            unvisited.setdefault(nodes[n] + int(grid[n.y][n.x + 1]), set())
            unvisited[nodes[n] + int(grid[n.y][n.x + 1])].add(r_x)
        if n.y > 0 and ((0 > n.dy > -10) or (n.dy == 0 and (n.dx == 0 or abs(n.dx) >= 4))) and nodes[u_y] is None:
            nodes[u_y] = nodes[n] + int(grid[n.y - 1][n.x])
            unvisited.setdefault(nodes[n] + int(grid[n.y -1][n.x]), set())
            unvisited[nodes[n] + int(grid[n.y - 1][n.x])].add(u_y)
        if n.y < (grid_y - 1) and ((0 < n.dy < 10) or (n.dy == 0 and (n.dx == 0 or abs(n.dx) >= 4))) and nodes[d_y] is None:
            if (n.y + 1) == (grid_y - 1) and n.x == (grid_x - 1) and n.dy >= 3:
                shortest_path = nodes[n] + int(grid[n.y + 1][n.x])
                break
            nodes[d_y] = nodes[n] + int(grid[n.y + 1][n.x])
            unvisited.setdefault(nodes[n] + int(grid[n.y + 1][n.x]), set())
            unvisited[nodes[n] + int(grid[n.y + 1][n.x])].add(d_y)

        k = sorted(unvisited.keys())[0]
        n = unvisited[k].pop()
        if not unvisited[k]:
            del unvisited[k]

    print(shortest_path)


if __name__ == '__main__':
    puzzle33()

