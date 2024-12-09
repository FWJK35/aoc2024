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
        for b in range(a + 1, len(freq)):
            if a != b:
                loca = freq[a]
                locb = freq[b]
                if loca[0] == locb[0]:
                    pass
                else:
                    slope = (loca[1]-locb[1])/(loca[0]-locb[0])
                    for test in range(-50, 50):
                        if int(round(slope * test, 8)) == round(slope * test, 8):
                            loc = (loca[0] + test, loca[1] + round(slope * test, 8))
                            if 0 <= loc[0] < len(lines[0]) and 0 <= loc[1] < len(lines):
                                if loc not in found:
                                    found.append(loc)
                                    total += 1
print(ants)
print(total)
