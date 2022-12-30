data = input()

pos = (0, 0)
grid: dict[tuple[int, int], int] = {(0, 0): 1}

pos_santa = (0, 0)
pos_robot = (0, 0)
grid2: dict[tuple[int, int], int] = {(0, 0): 1}


def move(pos_var, c):
    match(c):
        case '^':
            pos_var = (pos_var[0], pos_var[1] + 1)
        case '>':
            pos_var = (pos_var[0]+1, pos_var[1])
        case '<':
            pos_var = (pos_var[0]-1, pos_var[1])
        case 'v':
            pos_var = (pos_var[0], pos_var[1] - 1)
    return pos_var


def plus_plus(grid_var, pos_var):
    if pos_var not in grid_var:
        grid_var[pos_var] = 0

    grid_var[pos_var] += 1
    return grid_var


for i, c in enumerate(data):
    pos = move(pos, c)
    grid = plus_plus(grid, pos)

    if i % 2 == 0:
        pos_santa = move(pos_santa, c)
        grid2 = plus_plus(grid2, pos_santa)
    else:
        pos_robot = move(pos_robot, c)
        grid2 = plus_plus(grid2, pos_robot)


print(len(grid.keys()))
print(len(grid2.keys()))
