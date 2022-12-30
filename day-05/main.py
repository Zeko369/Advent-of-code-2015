import sys

lines = sys.stdin.readlines()

vowels = 'aeiou'
not_allowed = ['ab', 'cd', 'pq', 'xy']

x1 = 0
x2 = 0

for line in lines:
    check = 0
    for i in range(len(line)-3):
        pair = line[i:i+2]
        for j in range(i+2, len(line)-1):
            if pair == line[j:j+2]:
                check += 1
                break
        if check > 0:
            break
    for i in range(len(line)-2):
        if line[i] == line[i+2]:
            check += 1
            break

    if check == 2:
        x2 += 1

    if sum([line.count(v) for v in vowels]) < 3:
        continue
    if any([line.count(n) for n in not_allowed]):
        continue
    if not any([line[i] == line[i+1] for i in range(len(line)-1)]):
        continue

    x1 += 1

print(x1)
print(x2)
