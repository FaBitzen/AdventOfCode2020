with open("../input/day6.txt") as f:
    data = f.read().split("\n\n")
    sum1, sum2 = 0, 0
    for d in data:
        different = set()
        for c in d:
            different.add(c)
        sum1 += len(different - {'\n'})

    for dat in data:
        da = dat.splitlines()
        base = da[0]
        temp = ""
        for d in da[1:]:
            for c in base:
                if c in d:
                    temp += c
            base, temp = temp, ""
        sum2 += len(base)
print(sum1, sum2)
