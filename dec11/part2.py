lines = []
with open("dec11/input.txt", "r") as file:
    for line in file.readlines():
        lines.append(line.strip())

total = 0
stones = {}
for ind, stone in enumerate(lines[0].split()):
    stones.setdefault(int(stone), 0)
    stones[int(stone)] += 1
    pass
for blink in range(75):
    newstones = {}
    for s in stones.keys():
        if s == 0:
            newstones.setdefault(1, 0)
            newstones[1] += stones[s]
        elif len(str(s)) % 2 == 0:
            newstones.setdefault(int(str(s)[:len(str(s))//2]), 0)
            newstones.setdefault(int(str(s)[len(str(s))//2:]), 0)
            newstones[int(str(s)[:len(str(s))//2])] += stones[s]
            newstones[int(str(s)[len(str(s))//2:])] += stones[s]
        else:
            newstones.setdefault(2024 * s, 0)
            newstones[2024 * s] += stones[s]

    stones = newstones

    print(blink)


print(sum(stones.values()))
