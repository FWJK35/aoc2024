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
    current = {0:1}
    if ind == 3:
        pass
    flag = False
    while len(t) not in current or len(current) > 1:
        newcurrent = {}
        for c in current.keys():
            if c != len(t):
                for p in patterns:
                    if t[c:].startswith(p):
                        newcurrent.setdefault(c + len(p), 0)
                        newcurrent[c + len(p)] += current[c]
            else:
                newcurrent.setdefault(len(t), 0)
                newcurrent[len(t)] += current[len(t)]
        if len(newcurrent) == 0:
            break
        current = newcurrent
    if len(t) in current:
        total += current[len(t)]
    print(ind)
print(total)
