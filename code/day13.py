def part1():
    with open("../input/day13.txt") as f:
        times = f.read().splitlines()
        time, busIDs = int(times[0]), [int(c) for c in times[1].split(',') if c != 'x']

    depart = []
    for bus in busIDs:
        depart.append((time // bus + 1) * bus - time)

    ind = depart.index(min(depart))
    return depart[ind] * busIDs[ind]


def part2():
    with open("../input/day13.txt") as f:
        ids = f.read().splitlines()[1].split(',')
        ids = [((int(bid) - i % int(bid)) % int(bid), int(bid)) for i, bid in enumerate(ids) if bid != 'x']

    N = 1
    for _, b in ids:
        N *= b

    def mod_inverse(a, m):
        return pow(a % m, m - 2, m)

    ans = 0
    for i, b in ids:
        ni = N//b
        mi = mod_inverse(ni, b)
        for_b = i * mi * ni
        ans += for_b
    return ans % N


print(part1(), part2())
