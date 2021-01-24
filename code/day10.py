import itertools

with open("../input/day10.txt") as f:
    nums = [0]
    nums.extend([int(d) for d in f])
    nums.append(max(nums) + 3)
    nums.sort()
dis1 = 0
dis3 = 0
i = 0
while i < len(nums) - 1:
    if nums[i] + 1 == nums[i+1]:
        dis1 += 1
    if nums[i] + 3 == nums[i+1]:
        dis3 += 1
    i += 1
print("""{} with Distance of 1, {} with Distance of \
3, {} being the Product of both""".format(dis1, dis3, dis1 * dis3))


def splitupdata(data, step=3):
    head = 1
    tail = 0
    while head < len(data):
        if data[head] - data[head - 1] == step:
            yield data[tail:head]
            tail = head
        head += 1
    yield data[tail:head]


def validate(subset: list, mini, maxi):
    if len(subset) < 2:
        return False
    if subset[0] != mini or subset[-1] != maxi:
        return False
    j = 1
    while j < len(subset):
        if subset[j] - subset[j-1] > 3:
            return False
        j += 1
    return True


pt2 = 1
for sub in splitupdata(nums):
    if len(sub) < 2:
        continue
    acc = 0
    for k in range(2, len(sub)+1):
        for com in itertools.combinations(sub, k):
            acc += validate(list(com), min(sub), max(sub))
    pt2 *= acc

print(nums)
print("there are {} different combinations of adapters".format(pt2))
