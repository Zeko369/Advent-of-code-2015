import hashlib

data = input()

x1 = 0
x2 = 0

for i in range(100000000):
    hash = hashlib.md5((data + str(i)).encode()).hexdigest()
    if hash.startswith('000000'):
        x2 = i
        break
    if hash.startswith('00000') and x1 == 0:
        x1 = i

print(x1)
print(x2)
