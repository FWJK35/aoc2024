lines = []
with open("dec5/input.txt", "r") as file:
    for line in file.readlines():
        lines.append(line.strip())


total = 0
rules = []
gettingrules = True
updates = []
for line in lines:
    if line == "":
        gettingrules = False
        continue
    if gettingrules:
        rules.append([int(i) for i in line.split("|")])
    else:
        updates.append([int(i) for i in line.split(",")])
    pass

masterorder = {}
for r in range(len(rules)):
    rule = rules[r]
    masterorder.setdefault(rule[0], [])
    masterorder[rule[0]].append(rule[1])


for update in updates:
    valid = True
    for i in range(len(update)):
        if update[i] in masterorder:
            thisbefore = masterorder[update[i]]
            for j in range(i):
                if update[j] in thisbefore:
                    valid = False
                    break
            if not valid:
                break
    if valid:
        total += update[len(update) // 2]

# print(rules)
# print(updates)

print(total)