def part1():
    with open("../input/day14.txt") as f:
        ormask, andmask = 0, 1
        mem = dict()
        for line in f.read().splitlines():
            op, val = line.split(" = ")
            if op == "mask":
                ormask = int(str(val).replace('X', '0'), 2)
                andmask = int(str(val).replace('X', '1'), 2)
            else:
                mem[op[4:-1]] = int(val) & andmask | ormask

    acc = 0
    for val in mem.values():
        acc += val
    print(acc)


def part2():
    with open("../input/day14.txt") as f:
        mask, loc = "", ""
        mem = dict()
        for line in f.read().splitlines():
            op, val = line.split(" = ")
            if op == "mask":
                mask = val
            else:
                loc = bin(int(op[4:-1]))[2:].zfill(len(mask))
                assert len(mask) == len(loc)
                save = ""
                for k, m in zip(loc, mask):
                    if m == '1' or m == 'X':
                        save += m
                    if m == '0':
                        save += k
                assert save
                finished = []
                work = [save]

                while work:
                    for el in work:
                        if "X" not in el:
                            finished.append(el)
                            work.remove(el)
                            continue
                        work.append(el.replace("X", "0", 1))
                        work.append(el.replace("X", "1", 1))
                        work.remove(el)

                for num in finished:
                    mem[int(num, 2)] = int(val)

    acc = 0
    for val in mem.values():
        acc += val
    print(acc)


part1()
part2()
