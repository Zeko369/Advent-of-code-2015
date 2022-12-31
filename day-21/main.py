from functools import reduce
import itertools
import sys
from dataclasses import dataclass


@dataclass
class Item:
    name: str
    cost: int
    damage: int
    armor: int


weapons = [
    Item('Dagger', 8, 4, 0),
    Item('Shortsword', 10, 5, 0),
    Item('Warhammer', 25, 6, 0),
    Item('Longsword', 40, 7, 0),
    Item('Greataxe', 74, 8, 0),
]

armors = [
    Item("Leather", 13, 0, 1),
    Item("Chainmail", 31, 0, 2),
    Item("Splintmail", 53, 0, 3),
    Item("Bandedmail", 75, 0, 4),
    Item("Platemail", 102, 0, 5)
]

rings = [
    Item("Damage + 1", 25, 1, 0),
    Item("Damage + 2", 50, 2, 0),
    Item("Damage + 3", 100, 3, 0),
    Item("Defense + 1", 20, 0, 1),
    Item("Defense + 2", 40, 0, 2),
    Item("Defense + 3", 80, 0, 3)
]


@dataclass
class Character:
    hitPoints: int
    damage: int
    armor: int

    @staticmethod
    def from_lines(lines):
        return Character(
            int(lines[0].split(':')[1]),
            int(lines[1].split(':')[1]),
            int(lines[2].split(':')[1]),
        )

    def copy(self):
        return Character(self.hitPoints, self.damage, self.armor)

    def add_item(self, item: Item | None):
        if item is None:
            return

        self.damage += item.damage
        self.armor += item.armor


def simulate(me: Character, enemy: Character) -> bool:
    while True:
        enemy.hitPoints -= max(1, me.damage - enemy.armor)
        if enemy.hitPoints <= 0:
            return True
        me.hitPoints -= max(1, enemy.damage - me.armor)
        if me.hitPoints <= 0:
            return False


lines = sys.stdin.read().splitlines()

enemy = Character.from_lines(lines)
me = Character(100, 0, 0)

min_cost = None
max_cost = None

for weapon in weapons:
    for armor in [None, *armors]:
        for ring1, ring2 in itertools.combinations([None, None, *rings], 2):
            tmp_me = me.copy()
            tmp_me.add_item(weapon)
            tmp_me.add_item(armor)
            tmp_me.add_item(ring1)
            tmp_me.add_item(ring2)

            items = [weapon, armor, ring1, ring2]
            non_nulls = [x for x in items if x is not None]
            cost = reduce(lambda acc, item: acc + item.cost, non_nulls, 0)

            if simulate(tmp_me, enemy.copy()):
                if min_cost is None or cost < min_cost:
                    min_cost = cost
            else:
                if max_cost is None or cost > max_cost:
                    max_cost = cost


print(min_cost)
print(max_cost)
