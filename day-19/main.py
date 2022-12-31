import sys

lines = sys.stdin.readlines()
data = [(y[0], y[2]) for y in [x.split() for x in lines[:-2]]]
final = lines[-1].strip()

results = set()
for old, new in data:
    options = final.split(old)
    for i in range(len(options) - 1):
        tmp = old.join(options[:i+1]) + new + old.join(options[i + 1:])
        results.add(tmp)

print(len(results))
