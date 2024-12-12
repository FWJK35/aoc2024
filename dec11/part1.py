lines = []
with open("dec11/input.txt", "r") as file:
    for line in file.readlines():
        lines.append(line.strip())

total = 0
stones = []
for ind, stone in enumerate(lines[0].split()):
    stones.append(int(stone))
    pass
for blink in range(25):
    newstones = []
    for ind, s in enumerate(stones):
        if s == 0:
            newstones.append(1)
        elif len(str(s)) % 2 == 0:
            newstones.append(int(str(s)[:len(str(s))//2]))
            newstones.append(int(str(s)[len(str(s))//2:]))
        else:
            newstones.append(2024 * s)
    stones = newstones
    print(blink)


print(len(stones))
