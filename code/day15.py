def insert_num(numbers: dict, num: int, step: int):
    if num in numbers:
        ret = step - numbers[num]
    else:
        ret = 0
    numbers[num] = step
    return ret


def part(until):
    inp = [2, 0, 1, 9, 5, 19]
    inp = [17, 1, 3, 16, 19]
    numbers_said = dict()
    nextnum = -1
    ind = -1
    for i, n in enumerate(inp, 1):
        nextnum, ind = insert_num(numbers_said, n, i), i + 1

    while ind < until:
        nextnum = insert_num(numbers_said, nextnum, ind)
        ind += 1

    return nextnum


print(part(2020))
print(part(30000000))
