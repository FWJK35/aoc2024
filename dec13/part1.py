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
        prizes.append((int(line[line.index("X=") + 2:line.index(",")]), int(line[line.index("Y=") + 2:])))
    pass
print(avals, bvals, prizes)
for test, prize in enumerate(prizes):
    cheapest = -1
    for apos in range(101):
        for bpos in range(101):
            if apos * avals[test][0] + bpos * bvals[test][0] == prize[0] and \
                apos * avals[test][1] + bpos * bvals[test][1] == prize[1]:
                if apos * 3 + bpos < cheapest or cheapest == -1:
                    cheapest = apos * 3 + bpos
    if cheapest != -1:
        total += cheapest


print(total)
