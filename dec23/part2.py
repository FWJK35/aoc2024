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

largest = []
testsize = 3

def findmutuals(connected, depth):
    if depth == 0:
        return set((connected,))
    totest = []
    connectedlist = [connected[i * 2: i * 2 + 2] for i in range(len(connected) // 2)]
    connectedlist.sort()
    for newcon in cons.keys():
        badcon = False
        for comp in connectedlist:
            if comp not in cons[newcon]:
                badcon = True
        if badcon:
            continue
        totest.append(connectedlist + [newcon])
    
    output = set()
    for tt in totest:
        tt.sort()
        output |= findmutuals("".join(tt), depth - 1)

    return output

viable = set()
for start in cons.keys():
    viable |= findmutuals(start, 2)
partysize = 3
print(viable)
while True:
    newviable = set()
    for v in viable:
        newviable |= findmutuals(v, 1)
    print(partysize, len(newviable), newviable)
    if len(newviable) == 0:
        print(viable)
        break
    viable = newviable
    partysize += 1

for v in viable:
    lanparty = [v[i * 2: i * 2 + 2] for i in range(len(v) // 2)]
    break
lanparty.sort()
print(",".join(lanparty))
    
    

