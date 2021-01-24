with open("../input/day2.txt") as passwords:
    counter = 0
    for password in passwords:
        password = password.split(' ')
        bounds = password[0].split('-')
        lowerbound = int(bounds[0])
        upperbound = int(bounds[1])
        letter = password[1][0]
        tempcount = 0
        if (password[2][lowerbound - 1] == letter) ^ (password[2][upperbound - 1] == letter):
            counter += 1
    print(counter)
