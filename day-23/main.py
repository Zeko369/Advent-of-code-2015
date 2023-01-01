import sys
import dataclasses


@dataclasses.dataclass
class Instruction:
    name: str
    args: list[str]

    def __init__(self, line: str):
        self.name, *tmp_args = line.split()
        self.args = ' '.join(tmp_args).split(", ")

    def exec(self, part="a"):
        global registers
        match self.name:
            case "hlf":
                registers[part][self.args[0]] //= 2
            case 'tpl':
                registers[part][self.args[0]] *= 3
            case 'inc':
                registers[part][self.args[0]] += 1
            case 'jmp':
                return int(self.args[0])
            case 'jie':
                if registers[part][self.args[0]] % 2 == 0:
                    return int(self.args[1])
            case 'jio':
                if registers[part][self.args[0]] == 1:
                    return int(self.args[1])
            case _:
                raise ValueError(f"Unknown instruction {self.name}")
        return 1


lines = sys.stdin.readlines()
data = [Instruction(line) for line in lines]

pointerA = 0
pointerB = 0
registers = {"a": {"a": 0, "b": 0}, "b": {"a": 1, "b": 0}}

while pointerA < len(data):
    pointerA += data[pointerA].exec('a')
while pointerB < len(data):
    pointerB += data[pointerB].exec('b')

print(registers["a"]['b'])
print(registers["b"]['b'])
