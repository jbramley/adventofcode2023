from dataclasses import dataclass


@dataclass(frozen=True)
class Beam:
    x: int
    y: int
    dx: int
    dy: int


def puzzle31():
    with open("input", "r", encoding="utf8") as fp:
        grid = fp.read().splitlines()

    grid_y = len(grid)
    grid_x = len(grid[0])
    beams = [Beam(-1, 0, 1, 0)]
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

    energized = {(b.x, b.y) for b in energized}
    print(len(energized))


if __name__ == '__main__':
    puzzle31()