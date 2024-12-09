lines = []
with open("dec8/input.txt", "r") as file:
    for line in file.readlines():
        lines.append(line.strip())


total = 0
ants = {}
for ind, line in enumerate(lines):
    for x, c in enumerate(line):
        if c != ".":
            ants.setdefault(c, [])
            ants[c].append((x, ind))
    pass
found = []
for ant in ants.keys():
    freq = ants[ant]
    for a in range(len(freq)):
        for b in range(len(freq)):
            if a != b:
                loc = (freq[a][0]* 2 - freq[b][0], freq[a][1]* 2 - freq[b][1])
                if 0 <= loc[0] < len(lines[0]) and 0 <= loc[1] < len(lines):
                    if loc not in found:
                        found.append(loc)
                        total += 1
print(ants)
print(total)
