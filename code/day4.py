required = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

pt1 = 0
pt2 = 0
with open("../input/day4.txt") as f:
    data = ' '.join(f.readlines())
    data = data.split("\n \n")
    for d in data:
        tests = dict()
        for c in d.split():
            for req in required:
                if req not in d:
                    break
                if req in c:
                    tests[req] = c.split(':')[1]
            else:
                continue
            tests.clear()
            break
        if not tests:
            continue

        pt1 += 1

        if len(tests["pid"]) != 9:
            continue

        if not (1920 <= int(tests["byr"]) <= 2002):
            continue

        if not (2010 <= int(tests["iyr"]) <= 2020):
            continue

        if not (2020 <= int(tests["eyr"]) <= 2030):
            continue

        if "cm" in tests["hgt"]:
            if not (150 <= int(tests["hgt"][:-2]) <= 193):
                continue
        elif "in" in tests["hgt"]:
            if not (59 <= int(tests["hgt"][:-2]) <= 76):
                continue
        else:
            continue

        if not (tests["hcl"][0] == '#'):
            continue
        for n in tests["hcl"][1:]:
            if n not in ['0', '1', '2', '3', '4', '5', '6',
                         '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']:
                break
        else:
            safe = True
        if not safe:
            continue

        if tests["ecl"] not in ["amb", "blu", "brn",
                                "gry", "grn", "hzl", "oth"]:
            continue
        pt2 += 1


print(pt1, pt2)
