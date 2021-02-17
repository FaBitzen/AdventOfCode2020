import regex

with open("../input/day16.txt") as f:
    raw_rules, myticket, othertickets = f.read().split('\n\n')


def ticket_to_int_list(ticket: str):
    res = []
    for val in ticket.split(','):
        res.append(int(val))
    return res


myticket = ticket_to_int_list(myticket.split(':\n')[1])

othertickets = othertickets.split(':\n')[1].split('\n')[:-1]
othertickets = list(map(ticket_to_int_list,  othertickets))

rules = dict()
pattern = "(.*?): ([\d]+)-([\d]+) or ([\d]+)-([\d]+)"
for rule in raw_rules.split('\n'):
    match = regex.match(pattern, rule)
    values = set(range(int(match[2]), int(match[3]) + 1))
    values = values.union(set(range(int(match[4]), int(match[5]) + 1)))
    rules[match[1]] = values

possible_values = set()
for value in rules.values():
    possible_values = possible_values.union(value)


def validate_tickets(tickets: list[list[int]]) -> list[list[int]]:
    res = []
    for ticket in tickets:
        for para in ticket:
            if para not in possible_values:
                break
        else:
            res.append(ticket)
    return res


def part1():
    acc = 0
    for ticket in othertickets:
        for para in ticket:
            if para not in possible_values:
                acc += para
    return acc


valid_tickets = validate_tickets(othertickets)
valid_tickets.append(myticket)
categories = list(zip(*valid_tickets))


def isvalid(check, val):
    if val in check:
        return False
    return rules[val].issuperset(categories[len(check)])


def addvalue(check, val, n):
    if isvalid(check, val):
        if len(check) < n - 1:
            print(check + (val,))
            for i in rules.keys():
                yield from addvalue(check + (val,), i, n)
        else:
            yield check + (val,)
    return False


def get_order() -> list:
    res = [None for _ in range(len(rules))]
    possibilyties = dict([(i, []) for i in rules.keys()])
    for key, val in rules.items():
        for i, category in enumerate(categories):
            if val.issuperset(category):
                possibilyties[key].append(i)
    possibilyties = list(possibilyties.items())
    possibilyties.sort(key=lambda t: len(t[1]))
    for key, val in possibilyties:
        for i in val:
            if not res[i]:
                res[i] = key
    return res


def part2():
    acc = 1
    for val, name in zip(myticket, get_order()):
        if name.startswith("departure"):
            acc *= val
    return acc


print(part1(), part2())
