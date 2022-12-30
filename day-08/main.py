import sys
import json

lines = map(lambda x: x.strip(), sys.stdin.readlines())

x1 = 0
x2 = 0

for line in lines:
    a_val = len(line) - len(eval(line))
    x1 += a_val

    tmp_encoded = json.dumps(line)
    x2 += len(tmp_encoded) - len(line)


print(x1)
print(x2)
