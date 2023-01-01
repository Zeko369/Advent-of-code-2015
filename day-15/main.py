import sys
import dataclasses
import itertools


@dataclasses.dataclass
class Ingredient:
    name: str
    capacity: int
    durability: int
    flavor: int
    texture: int
    calories: int

    KEYS = ['capacity', 'durability', 'flavor', 'texture', 'calories']
    PART_A_KEYS = ['capacity', 'durability', 'flavor', 'texture']

    def __init__(self, line):
        # Sprinkles: capacity 5, durability -1, flavor 0, texture 0, calories 5
        words = line.strip().split(': ')

        self.name = words[0]
        items = words[1].split(', ')

        for i, key in enumerate(Ingredient.KEYS):
            setattr(self, key, int(items[i].split(' ')[1]))


lines = sys.stdin.readlines()
data = [Ingredient(line) for line in lines]

x1 = 0
x2 = 0

# Make it work with permutations (this only works for real input)
# for perm in itertools.permutations(range(100 + len(data) - 1), len(data)):
for i in range(101):
    for j in range(101):
        for k in range(101):
            for o in range(101):
                perm = [i, j, k, o]
                if sum(perm) == 100:
                    score = 1

                    for key in Ingredient.PART_A_KEYS:
                        all_items = [getattr(data[i], key) * perm[i]
                                     for i in range(len(data))]
                        score *= max(0, sum(all_items))

                    x1 = max(x1, score)
                    if sum([data[i].calories * perm[i] for i in range(len(data))]) == 500:
                        x2 = max(x2, score)


print(x1)
print(x2)  # 11162880 < x < 13882464
