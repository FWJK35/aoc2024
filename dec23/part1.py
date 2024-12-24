lines = []
with open("dec23/input.txt", "r") as file:
    for line in file.readlines():
        lines.append(line.strip())

total = 0
cons = {}

for ind, line in enumerate(lines):
    c1,c2 = line.split("-")
    cons.setdefault(c1, set())
    cons.setdefault(c2, set())
    cons[c1].add(c2)
    cons[c2].add(c1)
    pass

for p1 in cons.keys():
    for p2 in cons.keys():
        if p2 in cons[p1]:
            for p3 in cons.keys():
                if p1 in cons[p3] and p2 in cons[p3]:
                    if "-t" in f'-{p1}-{p2}-{p3}':
                        total += 1
    
total //= 6
print(total)
