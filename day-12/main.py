import json
import sys

data = sys.stdin.read()
obj = json.loads(data)


def get_stuff(obj, ignore_red=False):
    if isinstance(obj, dict):
        if ignore_red and any(obj[key] == 'red' for key in obj):
            return 0

        for key in obj:
            yield from get_stuff(obj[key], ignore_red)
    elif isinstance(obj, list):
        for item in obj:
            yield from get_stuff(item, ignore_red)
    elif isinstance(obj, int):
        yield obj


print(sum(get_stuff(obj)))
print(sum(get_stuff(obj, True)))
