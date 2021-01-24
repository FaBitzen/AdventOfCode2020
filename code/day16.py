with open("../input/day16.txt") as f:
    rules, myticket, othertickets = f.read().split('\n\n')

_, myticket = myticket.split('\n')
_, *othertickets, _ = othertickets.split('\n')

temp = rules.split('\n')
rules = dict()
for rule in temp:
    pos, ran = rule.split(": ")
    rules[pos] = set()
    ran1, ran2 = ran.split(" or ")
    op1, op2 = ran1.split('-')
    for i in range(int(op1), int(op2) + 1):
        rules[pos].add(i)
    op1, op2 = ran2.split('-')
    for i in range(int(op1), int(op2) + 1):
        rules[pos].add(i)

vals = set()
for i in rules.values():
    for j in i:
        vals.add(j)

invalid = []
notright = set()
for n, i in enumerate(othertickets):
    for j in i.split(','):
        if int(j) not in vals:
            notright.add(n)
            invalid.append(int(j))
print(sum(invalid))

notright = list(notright)
notright.sort(reverse=True)
for i in notright:
    othertickets.pop(i)

fields = dict()
for i, field in enumerate(rules.keys()):
    fields[i] = field

otherrows = dict()
for i in range(len(othertickets[0].split(','))):
    otherrows[i] = set()
    for j in othertickets:
        otherrows[i].add(int(j.split(',')[i]))


def addvalue(check, value, n):
    if isvalid(check, value):
        if len(check) > 8:
            print(check + (value,))
        if len(check) < n - 1:
            for i in range(n):
                yield from addvalue(check + (value,), i, n)
        else:
            yield check + (value,)
    return False


def isvalid(check,  value) -> bool:
    if value in check:
        return False
    if otherrows[len(check)].issubset(rules[fields[value]]):
        return False
    return True


def queens(n: int):
    for i in range(n):
        yield from addvalue((), i, n)


result = queens(len(fields))
print(list(result))
