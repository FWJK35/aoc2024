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

for b in range(len(blocks)):
    if blocks[b] == -1:
        while blocks[swapped] == -1:
            swapped -= 1
        if len(blocks) + swapped <= b:
               break
        blocks[swapped], blocks[b] = blocks[b], blocks[swapped]


for b in range(len(blocks)):
    total += b * (blocks[b]) if blocks[b] != -1 else 0

print("".join([str(i) if i != -1 else "." for i in blocks ]))
print(total)
