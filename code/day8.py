with open("../input/day8.txt") as f:
    data = f.readlines()
cleandata = []
for d in data:
    cleandata.append(d.strip().split(' '))


def test_programm(canditate: list):
    alreadyvisited = set()
    i1, i, acc = 0, 0, 0
    while i1 not in alreadyvisited and i1 < len(canditate):
        alreadyvisited.add(i1)
        i = i1
        if canditate[i][0] == "acc":
            acc += int(canditate[i][1])
            i1 += 1
        if canditate[i][0] == "nop":
            i1 += 1
        if canditate[i][0] == "jmp":
            i1 += int(canditate[i][1])
    return i1, i, acc


def generate_canditates(base: list):
    for j in range(len(base)):
        doub = []
        for b in base:
            doub.append(b)
        if base[j][0] == "jmp":
            doub[j] = ["nop", base[j][1]]
        elif base[j][0] == "nop":
            doub[j] = ["jmp", base[j][1]]
        yield doub


print(test_programm(cleandata))

for c in generate_canditates(cleandata):
    k, _, val = test_programm(c)
    if k >= len(c):
        print(test_programm(c))
