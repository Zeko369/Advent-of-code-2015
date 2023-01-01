from functools import reduce
import sys
import itertools

lines = list(map(int, sys.stdin.readlines()))
part1 = sum(lines) // 3
part2 = sum(lines) // 4

x1 = None
x2 = None

for i in range(len(lines)):
    for j in itertools.combinations(lines, i):
        if sum(j) == part1 and x1 is None:
            x1 = reduce(lambda x, y: x * y, j)
            break
        if sum(j) == part2 and x2 is None:
            x2 = reduce(lambda x, y: x * y, j)
            break

    if x1 is not None and x2 is not None:
        break

print(x1)
print(x2)
