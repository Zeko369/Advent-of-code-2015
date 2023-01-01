import sys

lines = sys.stdin.readlines()
data = [int(line.strip()) for line in lines[1:]]
N = int(lines[0][1:])


def sums_up_to(data: list[int], target: int, path: list[int] = []):
    count = 0
    paths = []

    for i in range(len(data)):
        if target < data[i]:
            continue

        if target == data[i]:
            paths.append(path + [data[i]])
            count += 1
            continue

        tc, tp = sums_up_to(data[i+1:], target - data[i], path + [data[i]])

        count += tc
        paths.extend(tp)

    return [count, paths]


num, paths = sums_up_to(data, N)
shortest = min([len(path) for path in paths])

print(num)
print(len(list(filter(lambda path: len(path) == shortest, paths))))
