from functools import reduce

data = int(input())


def factors(n):
    return set(reduce(list.__add__,
                      ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))


x1 = None
x2 = None
for i in range(1, 1000000):
    f = factors(i)
    if x1 is None and sum(f) * 10 >= data:
        x1 = i
    if x2 is None and sum(filter(lambda x: i / x < 50, sorted(f))) * 11 >= data:
        x2 = i

    if x1 is not None and x2 is not None:
        break
else:
    print("No answer")

print(x1)
print(x2)
