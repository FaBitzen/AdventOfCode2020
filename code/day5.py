with open("../input/day5.txt") as f:
    seatIDs = [int(d.replace("B", "1").replace("F", "0").replace(
               "R", "1").replace("L", "0"), 2) for d in f.readlines()]
    [print(max(seatIDs), i) for i in range(min(seatIDs), max(seatIDs))
     if i not in seatIDs]
