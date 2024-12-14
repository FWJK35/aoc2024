lines = []
with open("dec13/input.txt", "r") as file:
    for line in file.readlines():
        lines.append(line.strip())

total = 0
avals = []
bvals = []
prizes = []
for ind, line in enumerate(lines):
    if ind % 4 == 0:
        avals.append((int(line[line.index("X+") + 2:line.index(",")]), int(line[line.index("Y+") + 2:])))
    elif ind % 4 == 1:
        bvals.append((int(line[line.index("X+") + 2:line.index(",")]), int(line[line.index("Y+") + 2:])))
    elif ind % 4 == 2:
        prizes.append((int(line[line.index("X=") + 2:line.index(",")]) + 10000000000000, int(line[line.index("Y=") + 2:]) + 10000000000000))
    pass
print(avals, bvals, prizes)
for test, prize in enumerate(prizes):
    b = round((prize[0]-avals[test][0]/avals[test][1]*prize[1])/(bvals[test][0]-avals[test][0]/avals[test][1]*bvals[test][1]), 3)
    print(b)
    if int(b) == b and b >= 0:
        a = round((prize[1] - bvals[test][1]*b) / avals[test][1], 3)
        if int(a) == a and a >= 0:

            cost = 3 * a + b
            total += int(cost)
            print(test)


print(total)
