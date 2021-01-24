from copy import deepcopy

seats = [[c for c in line]
         for line in open("../input/day11.txt").read().splitlines()]


def return_halt(seat: list[list], tolerance=4, pt2=False):
    while True:
        step = next_step(seat, tolerance, pt2)
        if step == seat:
            break
        seat = step
    return step


def next_step(d: list[list], tolerance=4, pt2=False):
    dcopy = deepcopy(d)
    for x, row in enumerate(d):
        for y, seat in enumerate(row):
            if seat == '.':
                continue
            if seat == 'L' and adjacent_occupied(d, x, y, pt2) == 0:
                dcopy[x][y] = '#'
                continue
            if seat == '#' and adjacent_occupied(d, x, y, pt2) >= tolerance:
                dcopy[x][y] = 'L'
    return dcopy


def adjacent_occupied(seat: list[list], x: int, y: int, pt2):
    if pt2:
        return next_occupied(seat, x, y)
    occupied = 0
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            if dx == 0 and dy == 0:
                continue
            if 0 <= x + dx < len(seat) and 0 <= y + dy < len(seat[x]):
                occupied += seat[x+dx][y+dy] == '#'
    return occupied


def next_occupied(seat: list[list], x: int, y: int):
    occupied = 0
    for dx in range(x - 1, -1, -1):
        if seat[dx][y] == 'L':
            break
        if seat[dx][y] == '#':
            occupied += 1
            break
    for dx in range(x+1, len(seat)):
        if seat[dx][y] == 'L':
            break
        if seat[dx][y] == '#':
            occupied += 1
            break
    for dy in range(y - 1, -1, -1):
        if seat[x][dy] == 'L':
            break
        if seat[x][dy] == '#':
            occupied += 1
            break
    for dy in range(y + 1, len(seat[x])):
        if seat[x][dy] == 'L':
            break
        if seat[x][dy] == '#':
            occupied += 1
            break
    for dx, dy in zip(range(x - 1, -1, -1), range(y - 1, -1, -1)):
        if seat[dx][dy] == 'L':
            break
        if seat[dx][dy] == '#':
            occupied += 1
            break
    for dx, dy in zip(range(x - 1, -1, -1), range(y + 1, len(seat[x]))):
        if seat[dx][dy] == 'L':
            break
        if seat[dx][dy] == '#':
            occupied += 1
            break
    for dx, dy in zip(range(x+1, len(seat)), range(y - 1, -1, -1)):
        if seat[dx][dy] == 'L':
            break
        if seat[dx][dy] == '#':
            occupied += 1
            break
    for dx, dy in zip(range(x+1, len(seat)), range(y + 1, len(seat[x]))):
        if seat[dx][dy] == 'L':
            break
        if seat[dx][dy] == '#':
            occupied += 1
            break
    return occupied


def count_seats(seat: list[list]):
    acc = 0
    for row in seat:
        for s in row:
            acc += s == '#'
    return acc


def part1(seat: list[list]):
    halt = return_halt(seat)
    return count_seats(halt)


def part2(seat: list[list]):
    halt = return_halt(seat, 5, True)
    return count_seats(halt)


print("{} seats occuied from 1st rule set, {} from the 2nd rule set.".format(
    part1(seats), part2(seats)))
