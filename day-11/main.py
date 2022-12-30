data = input()

blacklist = ['i', 'o', 'l']


def hasIncrement(w):
    return any(ord(w[i]) == ord(w[i + 1]) - 1 == ord(w[i + 2]) - 2 for i in range(len(w) - 2))


def hasPairs(w):
    pairs = 0
    last = ''

    for i in range(len(w) - 1):
        if w[i] == w[i + 1] and w[i] != last:
            last = w[i]
            pairs += 1

    return pairs >= 2


def increment(w):
    if w[-1] != 'z':
        return w[:-1] + chr(ord(w[-1]) + 1)

    return increment(w[:-1]) + 'a'


x1 = data + ''

while True:
    x1 = increment(x1)
    if all(c not in blacklist for c in x1) and hasIncrement(x1) and hasPairs(x1):
        break

x2 = x1 + ''
while True:
    x2 = increment(x2)
    if all(c not in blacklist for c in x2) and hasIncrement(x2) and hasPairs(x2):
        break

print(x1)
print(x2)
