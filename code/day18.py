import regex


def simplify(expr: str, func):
    pattern = ".*?(\([^\(\)]+\))"
    while match := regex.match(pattern, expr):
        expr = expr.replace(match[1], func(match[1][1:-1]))
    return func(expr)


def evaluate1(expr: str):
    pattern = "(\d+ [\*\+] \d+)"
    while match := regex.match(pattern, expr):
        expr = expr.replace(match[1], str(eval(match[1])))
    return expr


def evaluate2(expr: str):
    pattern1 = ".*?(\d+ \+ \d+)"
    while match := regex.match(pattern1, expr):
        expr = expr.replace(match[1], str(eval(match[1])))
    pattern2 = "(\d+ \* \d+)"
    while match := regex.match(pattern2, expr):
        expr = expr.replace(match[1], str(eval(match[1])))
    return expr


def part1():
    acc = 0
    with open("../input/day18.txt") as f:
        while line := f.readline():
            acc += int(simplify(line, evaluate1))
    return acc


def part2():
    acc = 0
    with open("../input/day18.txt") as f:
        while line := f.readline():
            acc += int(simplify(line, evaluate2))
    return acc


print(part1(), part2())
