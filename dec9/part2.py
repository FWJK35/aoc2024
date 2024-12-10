lines = []
with open("dec9/input.txt", "r") as file:
    for line in file.readlines():
        lines.append(line.strip())

blocks = []
total = 0
for ind, c in enumerate(lines[0]):
    if ind % 2 == 0:
        blocks+= [ind // 2] * int(c)
    else:
        blocks+= [-1] * int(c)
    pass
swapped = -1

for b in range(len(lines[0]) // 2, -1, -1):
    isfreeblock = False
    freecount = 0
    freeindex = -1
    needed = int(lines[0][2 * b])
    thisindex = blocks.index(b)
    print(b)
    for check in range(thisindex):
        if blocks[check] == -1:
            freecount += 1
            if not isfreeblock:
                isfreeblock = True
                freeindex = check
            if freecount == needed:
                for i in range(needed):
                    blocks[freeindex + i], blocks[thisindex + i] = blocks[thisindex + i], blocks[freeindex + i]
                break
        else:
            if isfreeblock:
                freecount = 0
                isfreeblock = False





for b in range(len(blocks)):
    total += b * (blocks[b]) if blocks[b] != -1 else 0

print("".join([str(i) if i != -1 else "." for i in blocks ]))
print(total)
