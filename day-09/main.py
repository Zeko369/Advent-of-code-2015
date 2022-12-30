from dataclasses import dataclass
import sys


@dataclass
class Path:
    start: str
    end: str
    val: int

    def __init__(self, x):
        f, _, t, _, d = x.split()
        self.start, self.end, self.val = f, t, int(d)


lines = [Path(x.strip()) for x in sys.stdin.readlines()]
cities = set(map(lambda x: x.start, lines)) | set(map(lambda x: x.end, lines))
size = len(cities)


def bfs(start, end):
    min_val = None
    max_val = None

    queue: list[tuple[list[str], int]] = [([start], 0)]

    while queue:
        points, value = queue.pop(0)

        if points[-1] == end and len(points) == size:
            if min_val is None or min_val > value:
                min_val = value
            if max_val is None or max_val < value:
                max_val = value
            continue

        for line in lines:
            if line.start == points[-1] and line.end not in points:
                queue.append((points + [line.end], value + line.val))
            if line.end == points[-1] and line.start not in points:
                queue.append((points + [line.start], value + line.val))

    return min_val, max_val


final_min_val = None
final_max_val = None

for c1 in cities:
    for c2 in cities:
        if c1 == c2:
            continue

        min_val, max_val = bfs(c1, c2)
        if min_val and (final_min_val is None or final_min_val > min_val):
            final_min_val = min_val
        if max_val and (final_max_val is None or final_max_val < max_val):
            final_max_val = max_val

print('min', final_min_val)
print('max', final_max_val)
