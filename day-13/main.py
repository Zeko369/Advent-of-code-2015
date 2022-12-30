import itertools
import sys
from dataclasses import dataclass


@dataclass
class Person:
    name: str
    others: dict


lines = sys.stdin.readlines()

map: dict[str, Person] = {}

for x in lines:
    words = x.strip().split(' ')

    name = words[0]
    score = int(words[3]) * (1 if words[2] == 'gain' else -1)
    to_person = words[-1][:-1]
    if name not in map:
        map[name] = Person(name, {})

    map[name].others[to_person] = score


def calc_score(map):
    keys = list(map.keys())
    score = 0

    for perm in itertools.permutations(keys):
        tmp_score = 0
        for i in range(len(perm)):
            a = perm[i]
            b = perm[(i + 1) % len(perm)]

            tmp_score += map[a].others[b] + map[b].others[a]

        score = max(score, tmp_score)

    return score


x1 = calc_score(map)

part2_map = {**map, 'Me': Person('Me', {k: 0 for k in map.keys()})}
for key in map.keys():
    map[key].others['Me'] = 0

x2 = calc_score(part2_map)

print(x1)
print(x2)
