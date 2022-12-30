import sys

data = sys.stdin.readlines()

x1 = 0
x2 = 0

for line in data:
    l, w, h = map(int, line.split('x'))
    sides = [l*w, w*h, h*l]

    x1 += 2 * sum(sides) + min(sides)
    x2 += l * w * h + 2 * min(l + w, w + h, h + l)

print(x1)
print(x2)
