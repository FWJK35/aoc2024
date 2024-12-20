lines = []
with open("dec19/input.txt", "r") as file:
    for line in file.readlines():
        lines.append(line.strip())

total = 0
targets = []
patterns = [i.strip() for i in lines[0].split(",")]

for ind, line in enumerate(lines):
    if ind > 1:
        targets.append(line)
    pass

for ind, t in enumerate(targets):
    current = set()
    current.add(0)
    while len(t) not in current:
        newcurrent = set()
        for c in current:
            for p in patterns:
                if t[c:].startswith(p):
                    newcurrent.add(c + len(p))
        if len(newcurrent) == 0:
            break
        current = newcurrent
    if len(t) in current:
        total += 1
print(total)
