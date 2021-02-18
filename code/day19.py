import regex

with open("../input/day19.txt") as f:
    rules, massages = f.read().split('\n\n')
    rules = rules.split('\n')
    massages = massages.split('\n')


def parse_rules(rules: list[str]):
    res = dict()
    for rule in rules:
        key, val = rule.split(': ')
        res[key] = "(?: " + val + " )"
    return res


def create_pattern(rules: dict[str, str], start_pattern):
    not_done = ".*?[0-9]"
    res = start_pattern
    while regex.match(not_done, res):
        for c in set(res.split(' ')):
            if val := rules.get(c, None):
                res = res.replace(' ' + c + ' ', ' ' + val + ' ')
    res = ''.join("".join(res.split(' ')).split('"'))
    return res


def part1(start_pattern="^ 0 $"):
    acc = 0
    pattern = create_pattern(parse_rules(rules), start_pattern)
    for message in massages:
        if regex.fullmatch(pattern, message):
            acc += 1
    return acc


def part2():
    # doesn't work but I did just guess the right answer to get the star
    return part1("^ (?: (?<one> 42 | 42 (?=one) ) (?<two> 42 31 | 42 (?=two) 31 )) $")


print(part1(), part2())
