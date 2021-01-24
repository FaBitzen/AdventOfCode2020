with open("../input/day7.txt") as f:
    rawdata = f.readlines()
    data = []
    structureddata1 = dict()
    for line in rawdata:
        data.append(line.strip().replace(" bags", '').replace(" bag", '').replace('.', '').split("contain"))
    for d, l in data:
        for bag in l.split(','):
            if structureddata1.get(bag[3:]) is None:
                structureddata1[bag[3:]] = [d.strip()]
            else:
                structureddata1[bag[3:]].append(d.strip())
    structureddata2 = dict()
    data = []
    for line in rawdata:
        data.append(line.strip().replace(" bags", '').replace(" bag", '').replace('.', '').split(" contain "))
    for col, cont in data:
        structureddata2[col] = cont.split(", ")


def num_of1(color: str, bags: dict, result=set()):
    if bags.get(color) is not None:
        for colo in bags[color]:
            result.add(colo)
            num_of1(colo, bags, result)
        return result


def num_of2(color: str, bags: dict):
    sum2 = 0
    for ba in bags[color]:
        if ba == "no other":
            pass
        else:
            sum2 += int(ba[0]) + int(ba[0]) * num_of2(ba[2:], bags)
    return sum2


amount1 = num_of1("shiny gold", structureddata1)
amount2 = num_of2("shiny gold", structureddata2)
print(len(amount1))
print(amount2)
print(structureddata2)
