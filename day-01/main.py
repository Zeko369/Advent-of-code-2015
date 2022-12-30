data = input()

x1 = 0
x2 = -1

for i, c in enumerate(data):
    if c == "(":
        x1 += 1
    elif c == ")":
        x1 -= 1

    if x1 < 0:
        if x2 == -1:
            x2 = i

print(x1)
print(x2 + 1)
