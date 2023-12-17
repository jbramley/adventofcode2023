# import sys
# from dataclasses import dataclass, field
#
# eset = set[tuple[int, int]]
#
#
# @dataclass(frozen=True)
# class Path:
#     x: int
#     y: int
#     in_dx: int
#     in_dy: int
#
#
# def follow_path(p: Path, grid: list[str], paths: dict[Path, eset],
#                 current_path: list[Path] = None,
#                 reverse_graph: dict[Path, Path] = None) -> int:
#     if current_path is None:
#         current_path = []
#     if reverse_graph is None:
#         reverse_graph = {}
#
#     if p.x < 0 or p.x >= len(grid[0]) or p.y < 0 or p.y >= len(grid):
#         return 0
#
#     if p in paths:
#         return len(paths[p])
#
#     if p.in_dx and grid[p.y][p.x] == '|':
#         p1 = Path(p.x, p.y + 1, 0, 1)
#         p2 = Path(p.x, p.y - 1, 0, -1)
#     elif p.in_dy and grid[p.y][p.x] == '-':
#         p1 = Path(p.x + 1, p.y, 1, 0)
#         p2 = Path(p.x - 1, p.y, -1, 0)
#     else:
#         p2 = None
#         if grid[p.y][p.x] == '\\':
#             p1 = Path(p.x + p.in_dy, p.y + p.in_dx, p.in_dy, p.in_dx)
#         elif grid[p.y][p.x] == '/':
#             p1 = Path(p.x - p.in_dy, p.y - p.in_dx, -p.in_dy, -p.in_dx)
#         else:
#             p1 = Path(p.x + p.in_dx, p.y + p.in_dy, p.in_dx, p.in_dy)
#     if p1:
#         if p1 in reverse_graph:
#             px = p
#             loop_set = {p1}
#             while px != p1:
#                 loop_set.add(px)
#                 px = reverse_graph[px]
#             eloop = {(pl.x, pl.y) for pl in loop_set}
#             for pl in loop_set:
#                 paths[pl] = eloop
#             return len(paths[p])
#         else:
#             reverse_graph[p1] = p
#             follow_path(p1, grid, paths, current_path[:], reverse_graph.copy())
#
#         p1_set = paths.get(p1, set())
#     else:
#         p1_set = set()
#
#     if p2:
#         if p2 in reverse_graph:
#             px = p
#             loop_set = {p2}
#             while px != p2:
#                 loop_set.add(px)
#                 px = reverse_graph[px]
#             eloop = {(pl.x, pl.y) for pl in loop_set}
#             for pl in loop_set:
#                 paths[pl] = eloop
#             return len(paths[p])
#         else:
#             reverse_graph[p2] = p
#             follow_path(p2, grid, paths, current_path[:], reverse_graph.copy())
#         p2_set = paths.get(p2, set())
#     else:
#         p2_set = set()
#
#     paths[p] = p1_set | p2_set | {(p.x, p.y)}
#     return len(paths[p])


# def follow_path(init_p: Path, grid: list[str], paths: dict[Path, eset]) -> int:
#     current_path = []
#     reverse_graph = {}
#     path_stack = [init_p]
#     while path_stack:
#         p = path_stack.pop()
#
#         if p.in_dx and grid[p.y][p.x] == '|':
#             p1 = Path(p.x, p.y + 1, 0, 1)
#             p2 = Path(p.x, p.y - 1, 0, -1)
#         elif p.in_dy and grid[p.y][p.x] == '-':
#             p1 = Path(p.x + 1, p.y, 1, 0)
#             p2 = Path(p.x - 1, p.y, -1, 0)
#         else:
#             p2 = None
#             if grid[p.y][p.x] == '\\':
#                 p1 = Path(p.x + p.in_dy, p.y + p.in_dx, p.in_dy, p.in_dx)
#             elif grid[p.y][p.x] == '/':
#                 p1 = Path(p.x - p.in_dy, p.y - p.in_dx, -p.in_dy, -p.in_dx)
#             else:
#                 p1 = Path(p.x + p.in_dx, p.y + p.in_dy, p.in_dx, p.in_dy)
#
#         next_steps = []
#         if 0 <= p1.x < len(grid[0]) and 0 <= p1.y < len(grid) and p1 not in paths:
#             if p1 in reverse_graph:
#                 px = reverse_graph[p]
#                 loop_set = {p, p1}
#                 while px != p1:
#                     loop_set.add(px)
#                     pxn = reverse_graph[px]
#                     del reverse_graph[px]
#                     px = pxn
#                 del reverse_graph[p1]
#                 loop_energized = {(pl.x, pl.y) for pl in loop_set}
#                 for pl in loop_set:
#                     paths[pl] = loop_energized
#             else:
#                 path_stack.append(p1)
#                 next_steps.append(p1)
#                 reverse_graph[p1] = p
#         if p2 and 0 <= p2.x < len(grid[0]) and 0 <= p2.y < len(grid) and p2 not in paths:
#             if p2 in reverse_graph:
#                 px = reverse_graph[p]
#                 loop_set = {p, p2}
#                 while px != p2:
#                     loop_set.add(px)
#                     pxn = reverse_graph[px]
#                     del reverse_graph[px]
#                     px = pxn
#                 del reverse_graph[p2]
#                 loop_energized = {(pl.x, pl.y) for pl in loop_set}
#                 for pl in loop_set:
#                     paths[pl] = loop_energized
#             else:
#                 path_stack.append(p2)
#                 next_steps.append(p2)
#                 reverse_graph[p2] = p
#         current_path.append((p, next_steps))
#
#     while current_path:
#         p = current_path.pop()
#         e = set()
#         for pk in p[1]:
#             e |= paths.get(pk, set())
#         paths[p[0]] = e | {(p[0].x, p[0].y)}
#
#     return len(paths[init_p])
#
import timeit
from dataclasses import dataclass


@dataclass(frozen=True)
class Beam:
    x: int
    y: int
    dx: int
    dy: int


def puzzle32():
    with open("input", "r", encoding="utf8") as fp:
        grid = fp.read().splitlines()

    grid_y = len(grid)
    grid_x = len(grid[0])

    max_energized = 0
    for y in range(grid_y):
        max_energized = max(max_energized, path_len(-1, y, 1, 0, grid, grid_x, grid_y))
        max_energized = max(max_energized, path_len(grid_x, y, -1, 0, grid, grid_x, grid_y))
    for x in range(grid_x):
        max_energized = max(max_energized, path_len(x, -1, 0, 1, grid, grid_x, grid_y))
        max_energized = max(max_energized, path_len(x, grid_y, 0, -1, grid, grid_x, grid_y))

    print(max_energized)


def path_len(x, y, dx, dy, grid, grid_x, grid_y):
    beams = [Beam(x, y, dx, dy)]
    energized = set()
    while beams:
        b = beams.pop()
        while True:
            b = Beam(b.x + b.dx, b.y + b.dy, b.dx, b.dy)
            if b.y < 0 or b.y >= grid_y or b.x < 0 or b.x >= grid_x:
                break
            if b in energized:
                break
            energized.add(b)
            if b.dx and grid[b.y][b.x] == '|':
                b = Beam(b.x, b.y, 0, 1)
                beams.append(Beam(b.x, b.y, 0, -1))
            if b.dy and grid[b.y][b.x] == '-':
                b = Beam(b.x, b.y, 1, 0)
                beams.append(Beam(b.x, b.y, -1, 0))
            if grid[b.y][b.x] == '\\':
                b = Beam(b.x, b.y, b.dy, b.dx)
            if grid[b.y][b.x] == '/':
                b = Beam(b.x, b.y, -1 * b.dy, -1 * b.dx)
    return len({(b.x, b.y) for b in energized})


if __name__ == '__main__':
    print(timeit.timeit(puzzle32, number=1))

