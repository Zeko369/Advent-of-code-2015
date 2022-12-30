data = input()


def calculate(number: str):
    arr = [number[0]]
    for i in range(1, len(number)):
        if arr[-1][-1] != number[i]:
            arr.append(number[i])
        else:
            arr[-1] += number[i]

    return ''.join([str(len(i)) + i[0] for i in arr])


x1 = data + ''

for i in range(40):
    x1 = calculate(x1)

x2 = x1 + ''
for i in range(10):
    x2 = calculate(x2)

print(len(x1))
print(len(x2))
