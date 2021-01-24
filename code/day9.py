with open("../input/day9.txt") as f:
    data = [int(line) for line in f.read().splitlines()]


def partone(d, pre=25):
    return [d[i] for i in range(pre, len(d)) if d[i] not in {j + n
            for ii, n in enumerate(d[i-pre:i]) for j in d[i-pre+ii:i]}][0]


def parttwo(d: list, num=partone(data), pre=25):
    out = [d[start:start+step] for step in range(2, len(d) - pre) for start in
           range(0, d.index(num) - step) if sum(d[start:start+step]) == num][0]
    return min(out) + max(out)


print("weakness: {}, sum to fix: {}".format(partone(data), parttwo(data)))
