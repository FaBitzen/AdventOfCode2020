from copy import deepcopy as dc


def part1():
    cube = [[[True if c == '#' else False for c in line]
             for line in open("../input/day17.txt").read().splitlines()]]

    def alive_neighbors(field: list[list[list[bool]]], z, y, x):
        neighbors = 0
        for dz in range(-1, 2):
            for dy in range(-1, 2):
                for dx in range(-1, 2):
                    if not dz and not dy and not dx:
                        continue
                    if 0 <= z + dz < len(field) and \
                            0 <= y + dy < len(field[z + dz]) and \
                            0 <= x + dx < len(field[z + dz][y + dy]):
                        neighbors += field[z + dz][y + dy][x + dx]
        return neighbors

    def expand_field(field: list[list[list[bool]]]):
        step = dc(field)
        outer = dc(step[0])
        for i, _ in enumerate(outer):
            for j, _ in enumerate(outer[i]):
                outer[i][j] = False
        step.insert(0, dc(outer))
        step.append(dc(outer))
        line = dc(step[0][0])
        for z in step:
            z.insert(0, dc(line))
            z.append(dc(line))
            for y in z:
                y.insert(0, False)
                y.append(False)
        return step

    def next_step(field: list[list[list[bool]]]):
        step = expand_field(field)
        step2 = dc(step)
        for z, _ in enumerate(step):
            for y, _ in enumerate(step[z]):
                for x, _ in enumerate(step[z][y]):
                    neighbors = alive_neighbors(step, z, y, x)
                    if neighbors == 2:
                        step2[z][y][x] = step[z][y][x]
                    elif neighbors == 3:
                        step2[z][y][x] = True
                    else:
                        step2[z][y][x] = False
        return step2

    def count(field: list[list[list[bool]]]):
        acc = 0
        for z in field:
            for y in z:
                for x in y:
                    acc += x
        return acc

    for _ in range(6):
        cube = next_step(cube)
    return count(cube)


def part2():
    hypercube = [[[[True if c == '#' else False for c in line] for line
                   in open("../input/day17.txt").read().splitlines()]]]

    def alive_neighbors(field: list[list[list[list[bool]]]], w, z, y, x):
        neighbors = 0
        for dw in range(-1, 2):
            for dz in range(-1, 2):
                for dy in range(-1, 2):
                    for dx in range(-1, 2):
                        if not dw and not dz and not dy and not dx:
                            continue
                        if 0 <= w + dw < len(field) and \
                                0 <= z + dz < len(field[w + dw]) and \
                                0 <= y + dy < len(field[w + dw][z + dz]) and \
                                0 <= x + dx < \
                                len(field[w + dw][z + dz][y + dy]):
                            neighbors += field[w + dw][z + dz][y + dy][x + dx]
        return neighbors

    def expand_field(field: list[list[list[list[bool]]]]):
        step = dc(field)
        outer = dc(step[0])
        for i, _ in enumerate(outer):
            for j, _ in enumerate(outer[i]):
                for k, _ in enumerate(outer[i][j]):
                    outer[i][j][k] = False
        step.insert(0, dc(outer))
        step.append(dc(outer))
        plane = dc(step[0][0])
        for w in step:
            w.insert(0, dc(plane))
            w.append(dc(plane))
            line = dc(step[0][0][0])
            for z in w:
                z.insert(0, dc(line))
                z.append(dc(line))
                for y in z:
                    y.insert(0, False)
                    y.append(False)
        return step

    def next_step(field: list[list[list[list[bool]]]]):
        step = expand_field(field)
        step2 = dc(step)
        for w, _ in enumerate(step):
            for z, _ in enumerate(step[w]):
                for y, _ in enumerate(step[w][z]):
                    for x, _ in enumerate(step[w][z][y]):
                        neighbors = alive_neighbors(step, w, z, y, x)
                        if neighbors == 2:
                            step2[w][z][y][x] = step[w][z][y][x]
                        elif neighbors == 3:
                            step2[w][z][y][x] = True
                        else:
                            step2[w][z][y][x] = False
        return step2

    def count(field: list[list[list[list[bool]]]]):
        acc = 0
        for w in field:
            for z in w:
                for y in z:
                    for x in y:
                        acc += x
        return acc

    for _ in range(6):
        hypercube = next_step(hypercube)
    return count(hypercube)


print(part1(), part2())
