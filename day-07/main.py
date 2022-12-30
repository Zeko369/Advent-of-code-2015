import re
import sys

lines = list(map(lambda x: x.strip(), sys.stdin.readlines()))

lines_done1 = [False for _ in lines]
lines_done2 = [False for _ in lines]
reg1 = {}
reg2 = {"b": 16076}


def wrap(x): return x & 0xFFFF


def run_line(l, reg, lines_done):
    i, line = l
    if re.match(r'^\w+ (AND|OR) \w+ -> \w+$', line):
        a, op, b, _, c = line.split()

        av = int(a) if re.match(r'^\d+$', a) else reg.get(a)
        bv = int(b) if re.match(r'^\d+$', b) else reg.get(b)

        if av is not None and bv is not None:
            reg[c] = wrap(av | bv) if op == 'OR' else wrap(av & bv)
            lines_done[i] = True
    elif re.match(r'^\w+ (LSHIFT|RSHIFT) \d+ -> \w+$', line):
        a, op, b, _, c = line.split()
        if a in reg:
            if op == 'LSHIFT':
                reg[c] = wrap(reg[a] << int(b))
            else:
                reg[c] = wrap(reg[a] >> int(b))
            lines_done[i] = True
    elif re.match(r'^\d+ -> \w+$', line):
        a, _, b = line.split()
        reg[b] = wrap(int(a))
        lines_done[i] = True
    elif re.match(r'^\w+ -> \w+$', line):
        a, _, b = line.split()
        if a in reg:
            reg[b] = wrap(reg[a])
            lines_done[i] = True
    elif re.match(r'^NOT \w+ -> \w+$', line):
        _, a, _, b = line.split()
        if a in reg:
            reg[b] = wrap(~reg[a])
            lines_done[i] = True

    return (reg, lines_done)


while not all(lines_done1):
    for i, line in enumerate(lines):
        if lines_done1[i]:
            continue
        reg1, lines_done1 = run_line((i, line), reg1, lines_done1)

while not all(lines_done2):
    for i, line in enumerate(lines):
        if lines_done2[i]:
            continue
        if line.endswith('-> b'):
            line = '16076 -> b'

        reg2, lines_done2 = run_line((i, line), reg2, lines_done2)


print(reg1['a'])
print(reg2['a'])
