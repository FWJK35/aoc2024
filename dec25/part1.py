lines = []
with open("dec25/input.txt", "r") as file:
    for line in file.readlines():
        lines.append(line.strip())

total = 0

locks = []
keys = []

lockkey = []


reset = True
for ind, line in enumerate(lines):
    if line == "":
        thiscode = []
        if lockkey[0] == "#" * 5:
            for i in range(5):
                thiscode.append([lline[i] for lline in lockkey].count("#") - 1)
            locks.append(thiscode)
        else:
            for i in range(5):
                thiscode.append([kline[i] for kline in lockkey].count("#") - 1)
            keys.append(thiscode)
        lockkey = []

    else:
        lockkey.append(line)
    pass

for l in locks:
    for k in keys:
        for i in range(5):
            if l[i] + k[i] > 5:
                break
        else:
            total += 1

print(locks, keys)
print(total)
