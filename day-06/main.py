import sys

lines = sys.stdin.readlines()
grid_a = [[False for i in range(1000)] for j in range(1000)]
grid_b = [[0 for i in range(1000)] for j in range(1000)]


def get_op(line):
    if line.startswith('turn on'):
        return (lambda x: True, lambda x: x + 1)
    elif line.startswith('turn off'):
        return (lambda x: False, lambda x: x - 1 if x > 0 else 0)
    elif line.startswith('toggle'):
        return (lambda x: not x, lambda x: x + 2)

    raise ValueError('Invalid line: {}'.format(line))


for line in lines:
    words = line.split()

    op_a, op_b = get_op(line)

    x1, y1 = map(int, words[-3].split(','))
    x2, y2 = map(int, words[-1].split(','))
    for i in range(x1, x2+1):
        for j in range(y1, y2+1):
            grid_a[i][j] = op_a(grid_a[i][j])
            grid_b[i][j] = op_b(grid_b[i][j])

x1 = 0
x2 = 0

for i in range(1000):
    for j in range(1000):
        if grid_a[i][j]:
            x1 += 1
        x2 += grid_b[i][j]

print(x1)
print(x2)
