import sys
import dataclasses


@dataclasses.dataclass
class Reindeer:
    name: str
    speed: int
    fly_time: int
    rest_time: int

    distance: int = 0
    score: int = 0

    def __init__(self, line):
        # Rudolph can fly 22 km/s for 8 seconds, but then must rest for 165 seconds.
        words = line.strip().split(' ')

        self.name = words[0]
        self.speed = int(words[3])
        self.fly_time = int(words[6])
        self.rest_time = int(words[-2])


lines = sys.stdin.readlines()
data = [Reindeer(line) for line in lines]

for i in range(2503):
    for reindeer in data:
        if i % (reindeer.fly_time + reindeer.rest_time) < reindeer.fly_time:
            reindeer.distance += reindeer.speed

    tmp = sorted(data, key=lambda x: x.distance, reverse=True)
    tmp[0].score += 1

x1 = sorted(data, key=lambda x: x.distance, reverse=True)
print(x1[0].distance)
x2 = sorted(data, key=lambda x: x.score, reverse=True)
print(x2[0].score)
