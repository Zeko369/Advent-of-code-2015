import itertools
import sys


class Grid:
    data: list[list[bool]] = []
    broken = False

    def __init__(self, lines: list[str], broken=False):
        self.data = [[c == '#' for c in line.strip()] for line in lines]
        self.broken = broken

    def step(self):
        tmp = [[False for _ in row] for row in self.data]

        for i in range(0, len(self.data)):
            for j in range(0, len(self.data[i])):
                offset = [
                    (x, y)
                    for x, y in itertools.product([-1, 0, 1], repeat=2)
                    if 0 <= i + x < len(self.data) and 0 <= j + y < len(self.data[i]) and (x, y) != (0, 0)
                ]

                current_count = sum(self.data[i + x][j + y] for x, y in offset)

                if self.data[i][j]:
                    tmp[i][j] = current_count in (2, 3)
                else:
                    tmp[i][j] = current_count == 3

        self.data = tmp
        if self.broken:
            self.data[0][0] = True
            self.data[0][-1] = True
            self.data[-1][0] = True
            self.data[-1][-1] = True

    def count(self):
        x = 0
        for row in self.data:
            x += sum(row)

        return x

    def __repr__(self) -> str:
        return '\n'.join(''.join('#' if c else '.' for c in row) for row in self.data)


lines = sys.stdin.readlines()
grid1 = Grid(lines)
grid2 = Grid(lines, broken=True)

for i in range(100):
    grid1.step()
    grid2.step()

print(grid1.count())
print(grid2.count())
