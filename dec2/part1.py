lines = []
with open("dec2/input.txt", "r") as file:
    for line in file.readlines():
        lines.append(line.strip())

safecount = 0
for line in lines:
    levels = [int(i) for i in line.split()]
    incr = levels[1] > levels[0]
    safe = True
    for l in range(len(levels)-1):
        if incr:
            if levels[l+1] - levels[l] > 3 or levels[l+1] - levels[l] < 1:
                safe = False
        else:
            if levels[l] - levels[l+1] > 3 or levels[l] - levels[l+1] < 1:
                safe = False
    if safe: safecount += 1
print(safecount)
