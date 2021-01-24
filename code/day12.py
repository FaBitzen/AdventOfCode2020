from enum import Enum

with open("../input/day12.txt") as f:
    data = [(line[:1], int(line[1:])) for line in f.read().splitlines()]


def part1(route):
    class Facing(Enum):
        EAST = 0
        SOUTH = 90
        WEST = 180
        NORTH = 270

    ns, we = 0, 0
    facing = 0
    for op, val in route:
        if op in "NEWS":
            if op == 'N':
                ns -= val
            elif op == 'S':
                ns += val
            elif op == 'W':
                we -= val
            else:
                we += val
        elif op in "LR":
            if op == 'L':
                facing -= val
            else:
                facing += val
            facing = (facing + 360) % 360
        elif op == "F":
            if Facing(facing) == Facing.EAST:
                we += val
            elif Facing(facing) == Facing.WEST:
                we -= val
            elif Facing(facing) == Facing.NORTH:
                ns -= val
            elif Facing(facing) == Facing.SOUTH:
                ns += val
    return sum((abs(ns), abs(we)))


def part2(route):
    sns, swe = 0, 0
    wns, wwe = -1, 10
    for op, val in route:
        if op in "NEWS":
            if op == 'N':
                wns -= val
            elif op == 'S':
                wns += val
            elif op == 'W':
                wwe -= val
            else:
                wwe += val
        elif op in "LR":
            for _ in range(val//90):
                if op == 'L':
                    wns, wwe = -wwe, wns
                else:
                    wns, wwe = wwe, -wns
        elif op == "F":
            sns, swe = sns + wns * val, swe + wwe * val
    return sum((abs(sns), abs(swe)))


print("{}, {}".format(part1(data), part2(data)))
