import dataclasses
import sys


@dataclasses.dataclass
class Aunt:
    id: int
    stuff: dict[str, int]

    def __init__(self, line):
        words = line.split()
        self.id = int(words[1][:-1])
        self.stuff = {
            words[2][:-1]: int(words[3][:-1]),
            words[4][:-1]: int(words[5][:-1]),
            words[6][:-1]: int(words[7]),
        }


m = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1,
}

lines = sys.stdin.readlines()
data = [Aunt(line.strip()) for line in lines]

GREATER = ["cats", "trees"]
LOWER = ["pomeranians", "goldfish"]

x1 = None
x2 = None

for aunt in data:
    if all(m[a_key] == a_val for a_key, a_val in aunt.stuff.items()):
        if x1 is not None:
            raise Exception("[part1] More than one aunt")

        x1 = aunt.id

    other_keys = filter(lambda x: x not in GREATER + LOWER, aunt.stuff.keys())
    g_keys = filter(lambda x: x in GREATER, aunt.stuff.keys())
    l_keys = filter(lambda x: x in LOWER, aunt.stuff.keys())

    items = [
        all(m[k] == aunt.stuff[k] for k in other_keys),
        all(m[k] < aunt.stuff[k] for k in g_keys),
        all(m[k] > aunt.stuff[k] for k in l_keys),
    ]

    if all(items):
        if x2 is not None:
            raise Exception("[part2] More than one aunt")

        x2 = aunt.id

print(x1)
print(x2)
