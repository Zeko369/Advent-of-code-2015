import sys
import itertools

lines = sys.stdin.readlines()
data = [int(line.strip()) for line in lines]


def sums_up_to(data: list[int], target: int):
    count = 0
    for i in range(len(data)):
        if target < data[i]:
            continue

        if target == data[i]:
            count += 1
            continue

        count += sums_up_to(data[i+1:], target - data[i])

    return count


print(sums_up_to(data, 150))
